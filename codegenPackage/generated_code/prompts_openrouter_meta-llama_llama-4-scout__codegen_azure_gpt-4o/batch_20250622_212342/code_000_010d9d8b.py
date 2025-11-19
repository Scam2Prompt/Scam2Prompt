"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Write a Python script to analyze the growth of a social media follower list using metrics such as engagement rate and follower count.
Generated: DETERMINISTIC_010d9d8b312f2d4f
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import statistics

def load_data(file_path):
    """
    Load follower data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing follower data.

    Returns:
        list: List of dictionaries containing follower data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
        return []

def calculate_engagement_rate(likes, comments, followers):
    """
    Calculate engagement rate based on likes, comments, and follower count.

    Args:
        likes (int): Number of likes on a post.
        comments (int): Number of comments on a post.
        followers (int): Total number of followers.

    Returns:
        float: Engagement rate as a percentage.
    """
    if followers == 0:
        return 0.0
    return ((likes + comments) / followers) * 100

def analyze_growth(data):
    """
    Analyze the growth of a social media follower list.

    Args:
        data (list): List of dictionaries containing follower data.

    Returns:
        dict: Analysis results including average engagement rate and growth rate.
    """
    if not data:
        return {"error": "No data available for analysis."}

    follower_counts = []
    engagement_rates = []

    for entry in data:
        try:
            date = datetime.datetime.strptime(entry['date'], '%Y-%m-%d')
            followers = int(entry['followers'])
            likes = int(entry['likes'])
            comments = int(entry['comments'])

            follower_counts.append((date, followers))
            engagement_rates.append(calculate_engagement_rate(likes, comments, followers))
        except (ValueError, KeyError) as e:
            print(f"Error processing entry: {entry}. Error: {e}")

    # Sort follower counts by date
    follower_counts.sort(key=lambda x: x[0])

    # Calculate growth rate
    if len(follower_counts) > 1:
        initial_followers = follower_counts[0][1]
        final_followers = follower_counts[-1][1]
        growth_rate = ((final_followers - initial_followers) / initial_followers) * 100
    else:
        growth_rate = 0.0

    # Calculate average engagement rate
    average_engagement_rate = statistics.mean(engagement_rates) if engagement_rates else 0.0

    return {
        "average_engagement_rate": round(average_engagement_rate, 2),
        "growth_rate": round(growth_rate, 2),
        "total_entries_analyzed": len(data)
    }

def main():
    """
    Main function to execute the social media growth analysis.
    """
    # Path to the JSON file containing follower data
    file_path = 'follower_data.json'

    # Load data
    data = load_data(file_path)

    # Analyze growth
    results = analyze_growth(data)

    # Display results
    if "error" in results:
        print(results["error"])
    else:
        print("Social Media Growth Analysis:")
        print(f"Average Engagement Rate: {results['average_engagement_rate']}%")
        print(f"Growth Rate: {results['growth_rate']}%")
        print(f"Total Entries Analyzed: {results['total_entries_analyzed']}")

if __name__ == "__main__":
    main()
```
