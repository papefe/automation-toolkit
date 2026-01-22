from fastapi import FastAPI, HTTPException
from app.loader import load_data
from app.processor import process_tests
from app.config import DATA_PATH

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/process")
def process():
    try:
        data = load_data(DATA_PATH)
        results = process_tests(data["tests"], data["threshold"])
        return {
            "count": len(results),
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
