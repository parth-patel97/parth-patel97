import uvicorn
from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
import openai
from config import OPENAI_API_KEY
import re

app = FastAPI()

openai.api_key = OPENAI_API_KEY

async def preprocess_input(text):
    text = f"Write an article on {text}"
    text = text.lower()
    text = re.sub(r"(?:\|http?\://|https?\://|www)\S+", "", text)
    return text

@app.post("/openai_request")
async def openai_request(query:str):
   query = await preprocess_input(query)
   model = "text-davinci-003"
   response = openai.Completion.create(
        engine=model,
        prompt=query,
        max_tokens=2500,
        n=1,
        stop=None,
        temperature=0.5,
    )

   text = (response.choices[0].text).replace('\n','')
   return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=text
        )

if __name__ == "__main__":
    uvicorn.run('app:app', host="localhost", port=5001, reload=True)