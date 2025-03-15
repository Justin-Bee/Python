#Application question for Close.com

import hashlib
import json
import requests


# API URL
url = "https://api.close.com/buildwithus/"

# Send GET request
response = requests.get(url)

# Print the response
print("Status Code:", response.status_code)
# Extract key from response
response_data = response.json()
key = response_data.get("key", "")
print("Key:", key)

# Given traits
traits = [
    "Craftsman",
    "Pragmatic",
    "Curious",
    "Methodical",
    "Driven",
    "Collaborator"
]

# Key provided in response
#key = "Close-b3a93523"

# Function to hash each trait correctly
def hash_trait(trait, key):
    h = hashlib.blake2b(digest_size=64, key=key.encode("utf-8"))
    h.update(trait.encode("utf-8"))
    return h.hexdigest().lower()  # Ensure lowercase

# Generate hashed traits
hashed_traits = [hash_trait(trait, key) for trait in traits]

# API endpoint
url = "https://api.close.com/buildwithus/"

# Send POST request with correctly formatted JSON array
response = requests.post(url, json=hashed_traits, headers={"Content-Type": "application/json"})

# Print response
print("Status Code:", response.status_code)
print("Response Text:", response.text)