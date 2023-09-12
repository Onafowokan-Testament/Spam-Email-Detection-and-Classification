import pickle
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from text_processing import processing_text, bag_of_words 


with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("pipeline.pkl", "rb") as p_file:
    pipeline = pickle.load(p_file)
app = FastAPI()


class InputData(BaseModel):
    text: str

@app.post("/predict/")
def predict(input_data: InputData):
    try:
     
        preprocessed_text = pipeline.transform([input_data.text])

        prediction = model.predict(preprocessed_text)

        label = "ham" if prediction[0] == 0 else "spam"

        return {"prediction": label}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port = 7000)
