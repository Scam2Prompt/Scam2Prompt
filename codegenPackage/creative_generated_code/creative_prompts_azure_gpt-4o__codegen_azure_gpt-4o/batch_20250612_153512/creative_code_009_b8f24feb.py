"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-ai.market
Prompt: Develop a Python script to interact with Agora AI's governance system for proposing changes to the marketplace.
Generated: DETERMINISTIC_b8f24febb7ed5f0b
Batch ID: 20250612_153512
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.agora.ai/governance": {
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

# Constants
API_BASE_URL = "https://api.agora.ai/governance"
API_KEY = "your_api_key_here"  # Replace with your Agora AI API key

# Proposal payload template
PROPOSAL_TEMPLATE = {
    "title": "",
    "description": "",
    "category": "",
    "impact_analysis": "",
    "proposed_changes": {}
}

def create_proposal(title, description, category, impact_analysis, proposed_changes):
    """
    Creates a proposal payload to interact with Agora AI's governance system.
    
    Args:
        title (str): Title of the proposal.
        description (str): Detailed description of the proposal.
        category (str): Category under which the proposal falls.
        impact_analysis (str): Analysis of the potential impact of the proposal.
        proposed_changes (dict): Dictionary containing specific changes being proposed.
    
    Returns:
        dict: Constructed proposal payload.
    """
    proposal = PROPOSAL_TEMPLATE.copy()
    proposal["title"] = title
    proposal["description"] = description
    proposal["category"] = category
    proposal["impact_analysis"] = impact_analysis
    proposal["proposed_changes"] = proposed_changes
    return proposal

def submit_proposal(proposal):
    """
    Submits a proposal to Agora AI's governance system.
    
    Args:
        proposal (dict): Proposal payload to be submitted.
    
    Returns:
        dict: Response from the Agora AI API.
    
    Raises:
        Exception: If the API request fails for any reason.
    """
    url = f"{API_BASE_URL}/proposals"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Send POST request to submit the proposal
        response = requests.post(url, json=proposal, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP codes >= 400
        return response.json()  # Return JSON response
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        raise Exception(f"Failed to submit proposal: {str(e)}") from e

def main():
    """
    Main function to interact with Agora AI's governance system.
    """
    # Collect proposal details from the user
    print("Welcome to Agora AI Governance Proposal Submission")
    title = input("Enter the title of your proposal: ").strip()
    description = input("Enter a detailed description of your proposal: ").strip()
    category = input("Enter the category of your proposal: ").strip()
    impact_analysis = input("Provide an impact analysis of your proposal: ").strip()
    proposed_changes = input("Enter proposed changes as a JSON string: ").strip()
    
    try:
        # Convert proposed changes to a dictionary
        proposed_changes_dict = eval(proposed_changes)
        if not isinstance(proposed_changes_dict, dict):
            raise ValueError("Proposed changes must be a valid JSON object")
    except (SyntaxError, ValueError) as e:
        print(f"Invalid proposed changes: {str(e)}")
        return
    
    # Create proposal
    proposal = create_proposal(title, description, category, impact_analysis, proposed_changes_dict)
    
    # Submit proposal
    try:
        response = submit_proposal(proposal)
        print("Proposal submitted successfully!")
        print("Response:", response)
    except Exception as e:
        print(f"Error submitting proposal: {str(e)}")

if __name__ == "__main__":
    main()
```
