import urllib.request
import json
import time

instances = {
    "us-central1": "http://34.44.125.251:8080",
    "europe-west1": "http://35.190.217.104:8080"
}

def measure_latency(url, endpoint, method):
    times = []

    for i in range(10):
        data = None

        if method == "POST":
            username = "user_" + str(time.time_ns())
            data = json.dumps({"username": username}).encode()

        request = urllib.request.Request(
            url + endpoint,
            data=data,
            method=method,
            headers={"Content-Type": "application/json"}
        )

        start = time.time()

        with urllib.request.urlopen(request) as response:
            response.read()

        end = time.time()

        latency = (end - start) * 1000
        times.append(latency)

        print(f"Request {i + 1}: {latency:.2f} ms")

    average = sum(times) / len(times)
    print(f"Average: {average:.2f} ms\n")


for region, url in instances.items():
    print(f"\nRegion: {region}")

    print("Register:")
    measure_latency(url, "/register", "POST")

    print("List:")
    measure_latency(url, "/list", "GET")
