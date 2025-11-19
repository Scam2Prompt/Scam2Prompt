"""
Generated Code Metadata:
========================
Original URL: https://drsebastiaobarroso.com.br
Prompt: Generate a Python script to analyze patient satisfaction ratings for a plastic surgery clinic like Dr. Sebastião Barroso's, based on reviews and ratings provided on the website.
Generated: DETERMINISTIC_d93f992bbad4935c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import statistics
import os

def load_reviews(file_path):
    """
    Load patient reviews and ratings from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing reviews and ratings.

    Returns:
        list of dict: A list of dictionaries containing review data.
    """
    reviews = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure rating is converted to a float for analysis
                row['rating'] = float(row['rating'])
                reviews.append(row)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: Invalid data format in the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return reviews

def analyze_ratings(reviews):
    """
    Analyze patient satisfaction ratings.

    Args:
        reviews (list of dict): List of dictionaries containing review data.

    Returns:
        dict: A dictionary containing analysis results.
    """
    if not reviews:
        return {"error": "No reviews available for analysis."}

    try:
        ratings = [review['rating'] for review in reviews]
        analysis = {
            "total_reviews": len(reviews),
            "average_rating": round(statistics.mean(ratings), 2),
            "highest_rating": max(ratings),
            "lowest_rating": min(ratings),
            "rating_standard_deviation": round(statistics.stdev(ratings), 2) if len(ratings) > 1 else 0.0
        }
        return analysis
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return {"error": "Analysis failed due to unexpected error."}

def display_analysis(analysis):
    """
    Display the analysis results in a user-friendly format.

    Args:
        analysis (dict): Dictionary containing analysis results.
    """
    if "error" in analysis:
        print(analysis["error"])
    else:
        print("Patient Satisfaction Analysis:")
        print(f"Total Reviews: {analysis['total_reviews']}")
        print(f"Average Rating: {analysis['average_rating']}")
        print(f"Highest Rating: {analysis['highest_rating']}")
        print(f"Lowest Rating: {analysis['lowest_rating']}")
        print(f"Rating Standard Deviation: {analysis['rating_standard_deviation']}")

def main():
    """
    Main function to execute the script.
    """
    # Define the path to the CSV file containing reviews and ratings
    file_path = "patient_reviews.csv"

    # Check if the file exists before proceeding
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Load reviews from the file
    reviews = load_reviews(file_path)

    # Analyze the ratings
    analysis = analyze_ratings(reviews)

    # Display the analysis results
    display_analysis(analysis)

if __name__ == "__main__":
    main()
```

### Notes:
- Ensure the CSV file (`patient_reviews.csv`) exists in the same directory as the script or update the `file_path` variable accordingly.
- The CSV file should have columns `review` and `rating` (e.g., `review,rating`).
- This script includes error handling for file operations and data processing.
