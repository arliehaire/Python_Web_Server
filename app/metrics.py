import requests

global_metrics = {}

def fetch_metrics(ip):
    url = f"http://{ip}:19999/api/v1/allmetrics?format=json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        print(f"[INFO] Fetched metrics from {ip}, sample keys: {list(data.keys())[:5]}")
        global_metrics[ip] = data

        return data

    except Exception as e:
        print(f"[ERROR] Failed to fetch from {ip}: {e}")
        global_metrics[ip] = None
        return None

