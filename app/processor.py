def process_tests(tests, threshold):
    results = []

    for test in tests:
        status = "PASS" if test["value"] >= threshold else "FAIL"
        results.append({
            "name": test["name"],
            "value": test["value"],
            "status": status
        })

    return results
