# run_ingestion.py
from api_client import fetch_311_data
from validator import validate_records
from uploader import save_to_local_bronze

def main():
    raw_records = fetch_311_data()
    print(f"Fetched {len(raw_records)} records from API")
    valid_records = validate_records(raw_records)
    print(f"{len(valid_records)} records passed validation")
    save_to_local_bronze(valid_records)

if __name__ == "__main__":
    main()