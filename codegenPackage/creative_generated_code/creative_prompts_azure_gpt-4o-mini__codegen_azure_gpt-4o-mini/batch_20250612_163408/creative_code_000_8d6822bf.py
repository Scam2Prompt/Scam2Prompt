"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Write a Python script that uses the GitHub API v4 to retrieve release history for a specific repository.
Generated: DETERMINISTIC_8d6822bf0096a721
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com/graphql": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

# Constants for the GitHub API
GITHUB_API_URL = "https://api.github.com/graphql"

# Replace with your GitHub personal access token
GITHUB_TOKEN = "YOUR_GITHUB_ACCESS_TOKEN"

# GraphQL query to retrieve release history for a specific repository
def get_release_history(owner: str, repo: str) -> dict:
    query = """
    query($owner: String!, $repo: String!) {
        repository(owner: $owner, name: $repo) {
            releases(first: 100) {
                nodes {
                    name
                    tagName
                    publishedAt
                    description
                }
            }
        }
    }
    """
    
    variables = {
        "owner": owner,
        "repo": repo
    }

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    # Send the request to the GitHub GraphQL API
    response = requests.post(GITHUB_API_URL, json={'query': query, 'variables': variables}, headers=headers)

    # Check for HTTP errors
    if response.status_code != 200:
        raise Exception(f"Query failed with status code {response.status_code}: {response.text}")

    # Parse and return the JSON response
    return response.json()

# Main function to execute the script
if __name__ == "__main__":
    # Specify the repository owner and name
    repo_owner = "octocat"  # Change this to the repository owner
    repo_name = "Hello-World"  # Change this to the repository name

    try:
        # Retrieve and print the release history
        release_history = get_release_history(repo_owner, repo_name)
        releases = release_history.get("data", {}).get("repository", {}).get("releases", {}).get("nodes", [])
        
        if releases:
            print("Release History:")
            for release in releases:
                print(f"Name: {release['name']}, Tag: {release['tagName']}, Published At: {release['publishedAt']}, Description: {release['description']}")
        else:
            print("No releases found for this repository.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `YOUR_GITHUB_ACCESS_TOKEN` with an actual GitHub personal access token that has access to the repository you want to query. Adjust `repo_owner` and `repo_name` variables to the desired repository.
