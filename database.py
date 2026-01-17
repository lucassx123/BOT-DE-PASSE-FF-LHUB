import json
import os
from datetime import datetime

DATA_FILE = "data/users.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user(user_id: str):
    data = load_data()
    if user_id not in data:
        data[user_id] = {
            "balance": 0.0,
            "total_spent": 0.0,
            "purchases": [],
            "created_at": datetime.now().isoformat()
        }
        save_data(data)
    return data[user_id]

def add_balance(user_id: str, amount: float):
    data = load_data()
    if user_id not in data:
        get_user(user_id)
        data = load_data()
    data[user_id]["balance"] = round(data[user_id]["balance"] + amount, 2)
    save_data(data)
    return data[user_id]["balance"]

def remove_balance(user_id: str, amount: float):
    data = load_data()
    if user_id not in data:
        return False
    if data[user_id]["balance"] < amount:
        return False
    data[user_id]["balance"] = round(data[user_id]["balance"] - amount, 2)
    data[user_id]["total_spent"] = round(data[user_id]["total_spent"] + amount, 2)
    save_data(data)
    return True

def get_balance(user_id: str):
    user = get_user(user_id)
    return user["balance"]

def add_purchase(user_id: str, product: str, details: dict):
    data = load_data()
    if user_id not in data:
        get_user(user_id)
        data = load_data()
    purchase = {
        "product": product,
        "details": details,
        "date": datetime.now().isoformat()
    }
    data[user_id]["purchases"].append(purchase)
    save_data(data)

def get_all_users():
    return load_data()

def set_balance(user_id: str, amount: float):
    data = load_data()
    if user_id not in data:
        get_user(user_id)
        data = load_data()
    data[user_id]["balance"] = round(amount, 2)
    save_data(data)
    return data[user_id]["balance"]
