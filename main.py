from app.loader import load_data
from app.processor import process_tests
from app.config import DATA_PATH

def main():
    data = load_data(DATA_PATH)
    results = process_tests(data["tests"], data["threshold"])

    for r in results:
        print(r)

if __name__ == "__main__":
    main()
