from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from news_api import NewsAPI
import openai

app = FastAPI()

# Initialize NewsAPI and ChatGPTBot
news_api = NewsAPI(api_key='42ed7193249c4cd9beeaefc1bb88b25c')

class UserQuery(BaseModel):
    query: str
    history = [{"role":"system","content":"You are a news summarizer and personal Assistant!"}]

@app.post("/query/")
async def query_news(query_data: UserQuery):
    try:
        # Get the user query
        user_query = query_data.query
        
        # Use NewsAPI to fetch news articles based on user query
        articles = news_api.get_news(user_query)

        # Using LM Studio for GenAI

        client = openai.OpenAI(api_key="lm-studio",base_url="https://localhost:1234/v1")

        history.append({"role":"user","content":"Here is the query "+user_query+" and here are few articles please answer the question accordingly! "+str(articles)})

        completion = client.chat.completions.create(
            stream=False,
            model="model-identifier",
            messages=history,
            temperature=0.2
        )
        
        return {"articles": articles, "response": completion.choices[0].message.content }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
