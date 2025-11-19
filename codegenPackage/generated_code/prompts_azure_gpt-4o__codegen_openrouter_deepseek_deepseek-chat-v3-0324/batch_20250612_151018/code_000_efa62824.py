"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write Python code to interact with GitHub API v4 and retrieve release statistics, as described in the tubone BOYAKI blog post.
Generated: DETERMINISTIC_efa62824baf266cc
Batch ID: 20250612_151018
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

# Generated Code:
# ===============

```python
import os
import requests
from typing import Dict, List, Optional
from datetime import datetime

class GitHubGraphQLClient:
    """
    A client to interact with GitHub's GraphQL API (v4).
    Handles authentication, query execution, and error handling.
    """
    
    def __init__(self, github_token: str):
        """
        Initialize the GitHub GraphQL client with an access token.
        
        Args:
            github_token: GitHub personal access token with appropriate permissions
        """
        self.github_token = github_token
        self.api_url = "https://api.github.com/graphql"
        self.headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Content-Type": "application/json",
        }
    
    def execute_query(self, query: str, variables: Optional[Dict] = None) -> Dict:
        """
        Execute a GraphQL query against the GitHub API.
        
        Args:
            query: The GraphQL query string
            variables: Optional variables for the query
            
        Returns:
            The JSON response from the API
            
        Raises:
            ValueError: If the query fails or returns errors
            requests.exceptions.RequestException: For network-related errors
        """
        payload = {"query": query}
        if variables:
            payload["variables"] = variables
            
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            
            if "errors" in data:
                error_messages = [e["message"] for e in data["errors"]]
                raise ValueError(f"GraphQL errors: {', '.join(error_messages)}")
                
            return data
        
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Request failed: {str(e)}") from e

def get_release_statistics(
    owner: str,
    repo: str,
    github_token: str,
    release_count: int = 10
) -> List[Dict]:
    """
    Retrieve release statistics for a GitHub repository.
    
    Args:
        owner: Repository owner
        repo: Repository name
        github_token: GitHub personal access token
        release_count: Number of releases to fetch (default: 10)
        
    Returns:
        List of release statistics with download counts
        
    Raises:
        ValueError: If the query fails or data is invalid
    """
    query = """
    query ($owner: String!, $repo: String!, $releaseCount: Int!) {
        repository(owner: $owner, name: $repo) {
            releases(last: $releaseCount, orderBy: {field: CREATED_AT, direction: DESC}) {
                nodes {
                    name
                    publishedAt
                    releaseAssets(first: 10) {
                        nodes {
                            name
                            downloadCount
                        }
                    }
                }
            }
        }
    }
    """
    
    variables = {
        "owner": owner,
        "repo": repo,
        "releaseCount": release_count
    }
    
    client = GitHubGraphQLClient(github_token)
    response = client.execute_query(query, variables)
    
    try:
        releases = response["data"]["repository"]["releases"]["nodes"]
        result = []
        
        for release in releases:
            release_data = {
                "name": release["name"],
                "published_at": release["publishedAt"],
                "assets": []
            }
            
            for asset in release["releaseAssets"]["nodes"]:
                release_data["assets"].append({
                    "name": asset["name"],
                    "download_count": asset["downloadCount"]
                })
            
            result.append(release_data)
        
        return result
    
    except (KeyError, TypeError) as e:
        raise ValueError(f"Failed to parse response data: {str(e)}") from e

def format_release_stats(stats: List[Dict]) -> str:
    """
    Format release statistics into a human-readable string.
    
    Args:
        stats: Release statistics from get_release_statistics
        
    Returns:
        Formatted string with release information
    """
    output = []
    
    for release in stats:
        published_at = datetime.strptime(
            release["published_at"], "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%Y-%m-%d %H:%M:%S")
        
        output.append(f"Release: {release['name']} (Published: {published_at})")
        
        for asset in release["assets"]:
            output.append(
                f"  - {asset['name']}: {asset['download_count']:,} downloads"
            )
        
        output.append("")  # Add empty line between releases
    
    return "\n".join(output)

def main():
    """
    Main function to demonstrate usage of the GitHub release statistics tool.
    """
    try:
        # Get GitHub token from environment variable
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            raise ValueError("GITHUB_TOKEN environment variable not set")
        
        # Example: Get stats for tubone24/BOYAKI repository
        owner = "tubone24"
        repo = "BOYAKI"
        
        print(f"Fetching release statistics for {owner}/{repo}...")
        stats = get_release_statistics(owner, repo, github_token)
        
        print("\nRelease Statistics:")
        print(format_release_stats(stats))
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
