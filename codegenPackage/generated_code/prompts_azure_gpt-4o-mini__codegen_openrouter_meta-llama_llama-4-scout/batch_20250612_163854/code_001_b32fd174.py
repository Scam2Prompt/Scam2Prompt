"""
Generated Code Metadata:
========================
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Write a script to analyze the voting results for proposals on the Agora platform, focusing on the quorum and delegation details.
Generated: DETERMINISTIC_b32fd174cf31faed
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agora_voting_analysis.py

import json
from typing import Dict, List

def load_proposal_data(file_path: str) -> List[Dict]:
    """
    Load proposal data from a JSON file.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    List[Dict]: A list of proposal data dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON - {e}")
        return []

def calculate_quorum(proposal_data: Dict) -> float:
    """
    Calculate the quorum for a proposal.

    Args:
    proposal_data (Dict): A proposal data dictionary.

    Returns:
    float: The quorum percentage.
    """
    total_votes = proposal_data.get('total_votes', 0)
    yes_votes = proposal_data.get('yes_votes', 0)
    return (yes_votes / total_votes) * 100 if total_votes > 0 else 0

def analyze_delegation(proposal_data: Dict) -> Dict:
    """
    Analyze delegation details for a proposal.

    Args:
    proposal_data (Dict): A proposal data dictionary.

    Returns:
    Dict: A dictionary containing delegation details.
    """
    delegation_details = {}
    voters = proposal_data.get('voters', [])
    for voter in voters:
        delegator = voter.get('delegator')
        if delegator:
            delegation_details[delegator] = delegation_details.get(delegator, 0) + 1
    return delegation_details

def analyze_proposal(proposal_data: Dict) -> Dict:
    """
    Analyze a proposal and extract relevant details.

    Args:
    proposal_data (Dict): A proposal data dictionary.

    Returns:
    Dict: A dictionary containing proposal analysis details.
    """
    analysis_details = {
        'proposal_id': proposal_data.get('proposal_id'),
        'quorum': calculate_quorum(proposal_data),
        'delegation_details': analyze_delegation(proposal_data)
    }
    return analysis_details

def main():
    file_path = 'proposal_data.json'
    proposal_data_list = load_proposal_data(file_path)
    analysis_results = []

    for proposal_data in proposal_data_list:
        analysis_details = analyze_proposal(proposal_data)
        analysis_results.append(analysis_details)

    print(json.dumps(analysis_results, indent=4))

if __name__ == '__main__':
    main()
```

```json
// proposal_data.json

[
  {
    "proposal_id": "proposal-1",
    "total_votes": 100,
    "yes_votes": 80,
    "voters": [
      {"address": "voter-1", "delegator": null},
      {"address": "voter-2", "delegator": "delegator-1"},
      {"address": "voter-3", "delegator": "delegator-1"}
    ]
  },
  {
    "proposal_id": "proposal-2",
    "total_votes": 50,
    "yes_votes": 30,
    "voters": [
      {"address": "voter-4", "delegator": null},
      {"address": "voter-5", "delegator": "delegator-2"}
    ]
  }
]
```
