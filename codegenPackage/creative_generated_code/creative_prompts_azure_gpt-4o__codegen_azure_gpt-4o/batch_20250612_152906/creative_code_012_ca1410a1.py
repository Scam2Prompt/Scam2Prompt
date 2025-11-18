"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bouncebit-7g1.pages.dev
Prompt: Write a Python script to analyze the club ranking data and generate insights about the top-performing clubs in the BounceBit ecosystem.
Generated: DETERMINISTIC_ca1410a13a15d35a
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_club_rankings(data_file):
    """
    Analyzes club ranking data to provide insights on top-performing clubs.

    Parameters:
        data_file (str): Path to the CSV file containing club ranking data.

    Returns:
        None: Prints insights about top-performing clubs.
    """
    try:
        # Load club data from CSV file.
        club_data = pd.read_csv(data_file)
        if club_data.empty:
            print("The provided data file is empty. Please check the data source.")
            return
        
        # Ensure necessary columns exist in the dataset.
        required_columns = ["Club Name", "Score", "Rank"]
        missing_columns = [col for col in required_columns if col not in club_data.columns]
        if missing_columns:
            print(f"Missing required columns in the dataset: {missing_columns}")
            return
        
        # Sort clubs by score in descending order to find top performers.
        top_clubs = club_data.sort_values(by="Score", ascending=False)

        # Generate insights.
        print("===== Top-Performing Clubs =====")
        print(top_clubs.head(10)[["Club Name", "Score", "Rank"]])  # Top 10 clubs.

        # Average score of all clubs.
        avg_score = club_data["Score"].mean()
        print(f"\nAverage score across all clubs: {avg_score:.2f}")

        # Club with the highest score.
        best_club = top_clubs.iloc[0]
        print(f"\nClub with the highest score: {best_club['Club Name']} "
              f"(Score: {best_club['Score']}, Rank: {best_club['Rank']})")

        # Club with the lowest rank.
        lowest_rank_club = club_data.loc[club_data["Rank"].idxmax()]
        print(f"Club with the lowest rank: {lowest_rank_club['Club Name']} "
              f"(Score: {lowest_rank_club['Score']}, Rank: {lowest_rank_club['Rank']})")

    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found. Please provide a valid file path.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{data_file}' is empty. Please check the contents of the file.")
    except pd.errors.ParserError:
        print(f"Error: Unable to parse the file '{data_file}'. Ensure it is a valid CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example: Replace 'club_rankings.csv' with the actual path to your data file.
    data_file = "club_rankings.csv"
    analyze_club_rankings(data_file)
```
