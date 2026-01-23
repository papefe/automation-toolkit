from app.processor import process_tests

def test_all_pass_except_one():
    tests = [
        {"name": "t1", "value": 22},
        {"name": "t2", "value": 4},
        {"name": "t3", "value": 7},
        {"name": "t4", "value": 10},
    ]

    threshold = 5

    results = process_tests(tests, threshold)

    statuses = [r["status"] for r in results]

    assert statuses == ["PASS", "FAIL", "PASS", "PASS"]
