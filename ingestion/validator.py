# validator.py

def validate_records(records):
    valid = []
    for r in records:
        if "unique_key" in r and "created_date" in r:
            valid.append(r)
    return valid