# app_server.py
import sys
from database import check_number, save_number

N = 256

def process_number(number: int):
        
    if number == 0 or number >= N:
        sys.stdout.write(f"Error 0: Invalid 'number' parameter: {number}")
        return {"status": "ERROR0", "Description": f"The 'number' parameter must be an integer > 0 and < {N}"}, 415

    result_db = check_number(number)

    if result_db == "number_found":
        sys.stdout.write(f"Error 1: The 'number' parametr has already been processed")
        return {"status": "ERROR1", "Description": f"The 'number' parametr has already been processed"}, 418
    elif result_db == "number-1_found":
        sys.stdout.write(f"Error 2: The 'number' parameter received is one less than what has already been processed")
        return {"status": "ERROR2", "Description": f"The 'number' parameter received is one less than what has already been processed"}, 418
    else:
        save_number(number)

    return {"status": "success", "result": number + 1}, 200
