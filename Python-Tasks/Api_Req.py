#F - API Request
import requests

def users():
    url = "https://jsonplaceholder.typicode.com/users"  

    try:
        response = requests.get(url)
        response.raise_for_status()

        users = response.json()

        print("User Details:")
        for user in users:
            name = user.get("name", "N/A")
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")
            company = user.get("company", {}).get("name", "N/A")

            print("  Name:",name)
            print("  Email:",email)
            print("  City:",city)
            print("  Company:",company)
            print()

    except requests.exceptions.RequestException as e:
        print("An error occurred:",e)

users()
