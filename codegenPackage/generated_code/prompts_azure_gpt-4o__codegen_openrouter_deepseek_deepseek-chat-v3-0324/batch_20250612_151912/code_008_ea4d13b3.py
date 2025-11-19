"""
Generated Code Metadata:
========================
Original URL: https://originprotocol.typeform.com
Prompt: Create a Python script to analyze Typeform survey data using AI tools for extracting deeper customer insights.
Generated: DETERMINISTIC_ea4d13b3c99850dc
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import openai
from typing import Dict, List, Optional
import json
import logging
from pathlib import Path
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TypeformAnalyzer:
    """
    A class to analyze Typeform survey data using AI tools.
    """
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize the analyzer with OpenAI API key.
        
        Args:
            api_key: OpenAI API key
            model: OpenAI model to use (default: gpt-3.5-turbo)
        """
        openai.api_key = api_key
        self.model = model
        logger.info("TypeformAnalyzer initialized with model: %s", model)
    
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load Typeform data from JSON or CSV file.
        
        Args:
            file_path: Path to the data file
            
        Returns:
            DataFrame containing the survey data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is not supported
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        if path.suffix == '.json':
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            df = pd.json_normalize(data['responses'])
        elif path.suffix == '.csv':
            df = pd.read_csv(path)
        else:
            raise ValueError("Unsupported file format. Please provide JSON or CSV.")
            
        logger.info("Loaded data with %d responses", len(df))
        return df
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and preprocess the survey data.
        
        Args:
            df: Raw survey data DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        # Remove empty responses
        df = df.dropna(how='all')
        
        # Convert timestamps to datetime
        if 'submitted_at' in df.columns:
            df['submitted_at'] = pd.to_datetime(df['submitted_at'])
            
        logger.info("Data cleaned. %d valid responses remaining", len(df))
        return df
    
    def analyze_sentiment(self, text: str) -> Dict:
        """
        Analyze sentiment of a text response using OpenAI.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary containing sentiment analysis results
            
        Raises:
            Exception: If API call fails
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a sentiment analysis tool. Analyze the sentiment of the following text and return a JSON with keys: sentiment (positive, neutral, negative), confidence (0-1), and key_phrases (list of important phrases)."},
                    {"role": "user", "content": text}
                ],
                temperature=0.3,
                max_tokens=150
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
        except Exception as e:
            logger.error("Error in sentiment analysis: %s", str(e))
            raise
    
    def generate_insights(self, question: str, responses: List[str]) -> Dict:
        """
        Generate insights from multiple responses to a question.
        
        Args:
            question: The survey question
            responses: List of responses to analyze
            
        Returns:
            Dictionary containing generated insights
            
        Raises:
            Exception: If API call fails
        """
        try:
            prompt = f"""
            Analyze the following survey responses to the question: "{question}".
            Provide insights including:
            1. Common themes
            2. Notable outliers
            3. Actionable recommendations
            4. Sentiment summary
            
            Responses:
            {responses}
            """
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a survey analysis expert. Provide detailed insights from the survey responses."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            
            return {
                "question": question,
                "insights": response.choices[0].message.content
            }
        except Exception as e:
            logger.error("Error generating insights: %s", str(e))
            raise
    
    def analyze_survey(self, file_path: str, text_questions: List[str]) -> Dict:
        """
        Analyze a complete Typeform survey.
        
        Args:
            file_path: Path to survey data file
            text_questions: List of question IDs/keys that contain text responses
            
        Returns:
            Dictionary containing analysis results
            
        Raises:
            Exception: If analysis fails
        """
        try:
            # Load and clean data
            df = self.load_data(file_path)
            df = self.clean_data(df)
            
            results = {
                "summary": {
                    "total_responses": len(df),
                    "completion_rate": None,
                    "average_time": None
                },
                "question_insights": [],
                "sentiment_analysis": []
            }
            
            # Calculate completion rate if data available
            if 'answers' in df.columns:
                completed = df['answers'].apply(lambda x: len(x) > 0 if isinstance(x, dict) else False)
                results['summary']['completion_rate'] = completed.mean()
            
            # Calculate average time if data available
            if 'submitted_at' in df.columns and 'landed_at' in df.columns:
                time_diff = (df['submitted_at'] - df['landed_at']).dt.total_seconds()
                results['summary']['average_time'] = time_diff.mean()
            
            # Analyze text questions
            for question in text_questions:
                if question in df.columns:
                    responses = df[question].dropna().tolist()
                    
                    # Get insights for the question
                    insights = self.generate_insights(question, responses)
                    results['question_insights'].append(insights)
                    
                    # Perform sentiment analysis on sample responses
                    sample_responses = responses[:min(10, len(responses))]
                    sentiments = [self.analyze_sentiment(resp) for resp in sample_responses]
                    results['sentiment_analysis'].append({
                        "question": question,
                        "sample_sentiments": sentiments
                    })
            
            logger.info("Survey analysis completed successfully")
            return results
            
        except Exception as e:
            logger.error("Survey analysis failed: %s", str(e))
            raise

def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    # Initialize analyzer
    analyzer = TypeformAnalyzer(api_key)
    
    # Example usage
    try:
        # Replace with your actual file path and text questions
        results = analyzer.analyze_survey(
            file_path="survey_data.json",
            text_questions=["question1", "question2"]
        )
        
        # Save results
        with open('analysis_results.json', 'w') as f:
            json.dump(results, f, indent=2)
            
        logger.info("Analysis results saved to analysis_results.json")
        
    except Exception as e:
        logger.error("Error in analysis: %s", str(e))

if __name__ == "__main__":
    main()
```
