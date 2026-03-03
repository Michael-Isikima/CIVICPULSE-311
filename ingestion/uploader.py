# uploader.py
import json
import os
from config import LOCAL_BRONZE_DIR

def save_to_local_bronze(records):
    if not os.path.exists(LOCAL_BRONZE_DIR):
        os.makedirs(LOCAL_BRONZE_DIR)
    filename = os.path.join(LOCAL_BRONZE_DIR, "311_batch.json")
    with open(filename, "w") as f:
        json.dump(records, f, indent=2)
    print(f"Saved {len(records)} records to {filename}")