"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatime.pro
Prompt: Write a Python script that utilizes the principles of SQ (somatic intelligence) to analyze user feedback on personal coaching sessions.
Generated: DETERMINISTIC_b17e048d4258a462
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to analyze user feedback on personal coaching sessions using principles of Somatic Intelligence (SQ).
Somatic Intelligence involves understanding emotional, physical, and cognitive responses.

This script:
1. Accepts user feedback as input.
2. Categorizes feedback into emotional, physical, and cognitive aspects.
3. Provides an analysis of the feedback based on SQ principles.
"""

import re
import textblob
from textblob import TextBlob

def categorize_feedback(feedback):
    """
    Categorize feedback into emotional, physical, and cognitive aspects using keywords.
    
    Args:
        feedback (str): The user feedback text.
        
    Returns:
        dict: Categorized feedback with the emotional, physical, and cognitive aspects.
    """
    emotional_keywords = ['happy', 'sad', 'excited', 'angry', 'frustrated', 'content']
    physical_keywords = ['tired', 'energetic', 'pain', 'relaxed', 'tense', 'fatigue']
    cognitive_keywords = ['clarity', 'confused', 'focused', 'distracted', 'insightful', 'understanding']
    
    categorized = {"emotional": [], "physical": [], "cognitive": []}
    
    # Tokenize the feedback
    words = re.findall(r'\w+', feedback.lower())
    
    for word in words:
        if word in emotional_keywords:
            categorized["emotional"].append(word)
        elif word in physical_keywords:
            categorized["physical"].append(word)
        elif word in cognitive_keywords:
            categorized["cognitive"].append(word)
            
    return categorized


def analyze_feedback(feedback):
    """
    Provide an analysis of the user feedback based on SQ principles.
    
    Args:
        feedback (str): The user feedback text.
        
    Returns:
        dict: Sentiment analysis and categorized feedback.
    """
    try:
        # Categorize feedback
        categorized_feedback = categorize_feedback(feedback)
        
        # Sentiment analysis using TextBlob
        blob = TextBlob(feedback)
        sentiment = {
            "polarity": blob.sentiment.polarity,  # Polarity: -1 (negative) to 1 (positive)
            "subjectivity": blob.sentiment.subjectivity  # Subjectivity: 0 (objective) to 1 (subjective)
        }
        
        return {
            "categorized_feedback": categorized_feedback,
            "sentiment": sentiment
        }
    except Exception as e:
        # Error handling
        return {"error": f"An error occurred during analysis: {str(e)}"}


def main():
    """
    Main function to execute the feedback analysis.
    """
    print("Welcome to the Somatic Intelligence Feedback Analyzer!")
    print("Please enter your feedback below:")
    
    # Accept user feedback
    user_feedback = input("Feedback: ")
    
    # Validate input
    if not user_feedback.strip():
        print("Error: Feedback cannot be empty. Please try again.")
        return
    
    # Analyze feedback
    analysis = analyze_feedback(user_feedback)
    
    if "error" in analysis:
        print(analysis["error"])
    else:
        print("\nFeedback Analysis:")
        print("Categorized Feedback:")
        for aspect, keywords in analysis["categorized_feedback"].items():
            print(f"  {aspect.capitalize()}: {', '.join(keywords) if keywords else 'No relevant keywords found'}")
        print("Sentiment Analysis:")
        print(f"  Polarity: {analysis['sentiment']['polarity']:.2f} (Negative to Positive)")
        print(f"  Subjectivity: {analysis['sentiment']['subjectivity']:.2f} (Objective to Subjective)")


if __name__ == "__main__":
    main()
```
