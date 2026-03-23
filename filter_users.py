"""CLI script to filter users from a JSON file by name, age, or email."""

import json


def filter_users_by_name(name):
    """Filter users by name (case-insensitive).

    Args:
        name (str): The name to search for in users.json.
    """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """Filter users by age.

    Args:
        age (int): The age to search for in users.json.
    """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    """Filter users by email (case-insensitive).

    Args:
        email (str): The email to search for in users.json.
    """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? "
                          "(Currently, only 'name', 'age' or 'email' is supported): "
                          ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
