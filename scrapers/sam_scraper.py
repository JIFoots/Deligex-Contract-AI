import requests
import json

# Replace with your actual API key
API_KEY = "cMOe9CLiZLwnx0TUMhDiAnOtXHNanCY5z2u1adiZ"

def fetch_sam_contracts():
    url = "https://api.sam.gov/opportunities/v2/search"
    params = {
        "api_key": API_KEY,
        "q": "IT Services"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        contracts = response.json()
        with open("sam_contracts.json", "w") as f:
            json.dump(contracts, f, indent=4)
        print("✅ Contracts saved!")
    else:
        print(f"❌ Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_sam_contracts()
