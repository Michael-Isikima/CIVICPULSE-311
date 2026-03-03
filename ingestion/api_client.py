
import requests
from config import API_BASE_URL, BATCH_SIZE, LAST_RUN_FILE
import os

def get_last_run_timestamp():
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, "r") as f:
            return f.read().strip()
    return "2026-01-01T00:00:00"  # fallback

def save_last_run_timestamp(ts):
    with open(LAST_RUN_FILE, "w") as f:
        f.write(ts)

def fetch_311_data():
    last_run = get_last_run_timestamp()
    offset = 0
    all_records = []

    while True:
        params = {
            "$where": f"updated_date>'{last_run}'",
            "$limit": BATCH_SIZE,
            "$offset": offset
        }
        response = requests.get(API_BASE_URL, params=params)
        data = response.json()
        if not data:
            break
        all_records.extend(data)
        offset += BATCH_SIZE

    # Save the last record timestamp for next incremental load
    if all_records:
        latest_ts = max([r['updated_date'] for r in all_records])
        save_last_run_timestamp(latest_ts)

    return all_records