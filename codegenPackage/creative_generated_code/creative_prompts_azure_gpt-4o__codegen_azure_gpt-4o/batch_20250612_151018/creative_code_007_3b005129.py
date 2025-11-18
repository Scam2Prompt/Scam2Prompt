"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Write a script that generates a summary report of FOSS@RIT members who contribute to both GitHub and GitLab, including their usernames and areas of expertise.
Generated: DETERMINISTIC_3b005129f6a1dc07
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json

def load_data(github_contributors_file, gitlab_contributors_file, expertise_file):
    """
    Load data from CSV and JSON files.
    
    Parameters:
        github_contributors_file (str): Path to the CSV file containing GitHub contributors.
        gitlab_contributors_file (str): Path to the CSV file containing GitLab contributors.
        expertise_file (str): Path to the JSON file containing member expertise.

    Returns:
        tuple: Three dictionaries containing GitHub contributors, GitLab contributors, and expertise data.
    """
    try:
        # Load GitHub contributors
        with open(github_contributors_file, 'r') as file:
            github_contributors = {row['username']: row for row in csv.DictReader(file)}

        # Load GitLab contributors
        with open(gitlab_contributors_file, 'r') as file:
            gitlab_contributors = {row['username']: row for row in csv.DictReader(file)}

        # Load expertise data
        with open(expertise_file, 'r') as file:
            expertise_data = json.load(file)

        return github_contributors, gitlab_contributors, expertise_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}, {}, {}


def generate_summary_report(github_contributors, gitlab_contributors, expertise_data, output_file):
    """
    Generate a summary report of members who contribute to both GitHub and GitLab.

    Parameters:
        github_contributors (dict): Dictionary of GitHub contributors.
        gitlab_contributors (dict): Dictionary of GitLab contributors.
        expertise_data (dict): Dictionary of expertise data.
        output_file (str): Path to the output file for the summary report.
    """
    try:
        common_contributors = set(github_contributors.keys()) & set(gitlab_contributors.keys())
        
        # Prepare summary report
        summary = []
        for username in common_contributors:
            expertise = expertise_data.get(username, "Unknown")
            summary.append({
                'username': username,
                'expertise': expertise
            })

        # Write summary to a CSV file
        with open(output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['username', 'expertise'])
            writer.writeheader()
            writer.writerows(summary)

        print(f"Summary report generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating summary report: {e}")


def main():
    """
    Main entry point of the script.
    """
    # File paths
    github_contributors_file = 'github_contributors.csv'
    gitlab_contributors_file = 'gitlab_contributors.csv'
    expertise_file = 'expertise.json'
    output_file = 'summary_report.csv'

    # Load data
    github_contributors, gitlab_contributors, expertise_data = load_data(
        github_contributors_file, gitlab_contributors_file, expertise_file
    )

    # Generate summary report
    generate_summary_report(github_contributors, gitlab_contributors, expertise_data, output_file)


# Entry point of the script
if __name__ == "__main__":
    main()
```
