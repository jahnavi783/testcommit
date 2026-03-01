from utils import greet_user
from calculator import add_numbers
from config import APP_NAME

def run():
    print(f"Welcome to {APP_NAME}")
    
    name = input("Enter your name")
    greet_user(name)
    
    result = add_numbers(5, 3)
    print("Addition Result:", result)

if __name__ == "__main__":
    run()