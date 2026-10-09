import urllib.request
import json
import time

US_URL = "http://34.44.125.251:8080"
EU_URL = "http://35.190.217.104:8080"

not_found = 0
iterations = 100

for i in range(iterations):
    username = "test_" + str(time.time_ns())

    data = json.dumps({"username": username}).encode()

    request = urllib.request.Request(US_URL + "/register", data=data, method="POST", headers={"Content-Type": "application/json"})

    with urllib.request.urlopen(request, timeout=15) as response:
        response.read()

    with urllib.request.urlopen(EU_URL + "/list", timeout=15) as response:
        result = json.loads(response.read().decode())

    if username not in result["users"]:
        not_found += 1

print("\nResults:")
print("Total iterations:", iterations)
print("Not found immediately:", not_found)
print("Not found percentage:", (not_found / iterations) * 100, "%")
