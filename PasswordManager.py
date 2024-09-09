import json
import os

# Save password to a file
def save_password(service, username, password):
    data = {}
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            data = json.load(file)
    
    data[service] = {"username": username, "password": password}
    
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

# Retrieve a password from the file
def get_password(service):
    if not os.path.exists("passwords.json"):
        print("No passwords saved yet.")
        return
    
    with open("passwords.json", "r") as file:
        data = json.load(file)
    
    if service in data:
        username = data[service]["username"]
        password = data[service]["password"]
        print(f"Service: {service}\nUsername: {username}\nPassword: {password}")
    else:
        print("Service not found.")

# Delete a password entry
def delete_password(service):
    if not os.path.exists("passwords.json"):
        print("No passwords saved yet.")
        return
    
    with open("passwords.json", "r") as file:
        data = json.load(file)
    
    if service in data:
        del data[service]
        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Password entry deleted.")
    else:
        print("Service not found.")

# Main function for user interaction
def main():
    while True:
        print("\nPassword Manager")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(service, username, password)
        elif choice == "2":
            service = input("Enter the service name: ")
            get_password(service)
        elif choice == "3":
            service = input("Enter the service name: ")
            delete_password(service)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()