from fastapi import FastAPI
from app.loader import load_data
from app.processor import process_tests
from app.config import DATA_PATH

app = FastAPI(title="Automation Toolkit API")


@app.get("/tests")
def get_tests():
    data = load_data(DATA_PATH)

    results = process_tests(
        tests=data["tests"],
        threshold=data["threshold"]
    )

    return {
        "count": len(results),
        "results": results
    }


@app.get("/tests/{threshold}")
def get_tests_with_threshold(threshold: int):
    data = load_data(DATA_PATH)

    results = process_tests(
        tests=data["tests"],
        threshold=threshold
    )

    return {
        "count": len(results),
        "threshold": threshold,
        "results": results
    }
