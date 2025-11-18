"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securecash.info
Prompt: Generate a script to analyze customer reviews and ratings for business funding providers, using the testimonials and TrustScore data from New York Savings.
Generated: DETERMINISTIC_0299b80664a24c6a
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import pandas as pd
from textblob import TextBlob

# Define constants
INPUT_FILE = "customer_reviews.csv"  # CSV file containing reviews and ratings
OUTPUT_FILE = "review_analysis_report.csv"  # Output file for analysis results

def clean_text(text):
    """
    Cleans the review text by removing special characters, numbers, and extra spaces.
    :param text: Raw review text
    :return: Cleaned review text
    """
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters and numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

def perform_sentiment_analysis(text):
    """
    Performs sentiment analysis on the given text using TextBlob.
    :param text: Cleaned review text
    :return: Sentiment polarity (range -1 to 1) and subjectivity (range 0 to 1)
    """
    if text == "":
        return 0.0, 0.0
    analysis = TextBlob(text)
    return analysis.polarity, analysis.subjectivity

def validate_data(df):
    """
    Validates the input data to ensure required fields are present.
    :param df: DataFrame containing customer reviews
    :return: True if data is valid, raises ValueError otherwise
    """
    required_columns = ["Review", "Rating", "TrustScore"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    return True

def analyze_reviews(input_file):
    """
    Analyzes customer reviews and ratings, performing sentiment analysis and aggregating TrustScores.
    :param input_file: Path to the CSV file containing reviews
    :return: DataFrame containing analysis results
    """
    try:
        # Load data
        reviews_df = pd.read_csv(input_file)
        
        # Validate data
        validate_data(reviews_df)
        
        # Clean review text and perform sentiment analysis
        reviews_df["CleanedReview"] = reviews_df["Review"].apply(clean_text)
        reviews_df["SentimentPolarity"], reviews_df["SentimentSubjectivity"] = zip(
            *reviews_df["CleanedReview"].apply(perform_sentiment_analysis)
        )
        
        # Aggregate TrustScore and Rating data
        avg_trust_score = reviews_df["TrustScore"].mean()
        avg_rating = reviews_df["Rating"].mean()
        
        print(f"Average TrustScore: {avg_trust_score:.2f}")
        print(f"Average Rating: {avg_rating:.2f}")
        
        # Generate summary DataFrame
        summary_df = reviews_df[[
            "Review", "Rating", "TrustScore", "SentimentPolarity", "SentimentSubjectivity"
        ]]
        
        return summary_df
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return pd.DataFrame()
    except ValueError as ve:
        print(f"Data Validation Error: {ve}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

def main():
    """
    Main function to execute the review analysis pipeline.
    """
    print("Starting customer review analysis...")
    
    # Analyze reviews
    results_df = analyze_reviews(INPUT_FILE)
    
    if not results_df.empty:
        # Save analysis results to CSV
        results_df.to_csv(OUTPUT_FILE, index=False)
        print(f"Analysis complete. Results saved to '{OUTPUT_FILE}'.")
    else:
        print("No analysis results generated due to an error.")

if __name__ == "__main__":
    main()
```
