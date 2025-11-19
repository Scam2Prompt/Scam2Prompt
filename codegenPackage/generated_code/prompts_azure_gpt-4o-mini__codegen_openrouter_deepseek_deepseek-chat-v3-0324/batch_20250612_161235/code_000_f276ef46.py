"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Generate a Python script that simulates the grading system for the Fiji Mathematics Competition (FMC), categorizing scores into Prize, Distinction, Credit, Pass, and Participation.
Generated: DETERMINISTIC_f276ef46bf222f1a
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Tuple

# Constants for grade boundaries
PRIZE_THRESHOLD = 90
DISTINCTION_THRESHOLD = 75
CREDIT_THRESHOLD = 60
PASS_THRESHOLD = 40

def categorize_score(score: int) -> str:
    """
    Categorize a single score into the appropriate grade category.
    
    Args:
        score: The score to categorize (0-100)
        
    Returns:
        str: The grade category
        
    Raises:
        ValueError: If score is outside valid range (0-100)
    """
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    
    if score >= PRIZE_THRESHOLD:
        return "Prize"
    elif score >= DISTINCTION_THRESHOLD:
        return "Distinction"
    elif score >= CREDIT_THRESHOLD:
        return "Credit"
    elif score >= PASS_THRESHOLD:
        return "Pass"
    else:
        return "Participation"

def process_scores(scores: List[int]) -> Dict[str, List[Tuple[int, int]]]:
    """
    Process a list of scores and categorize them.
    
    Args:
        scores: List of scores (0-100)
        
    Returns:
        Dict: A dictionary with grade categories as keys and lists of 
              (position, score) tuples as values
              
    Raises:
        ValueError: If any score is invalid
    """
    categorized = {
        "Prize": [],
        "Distinction": [],
        "Credit": [],
        "Pass": [],
        "Participation": []
    }
    
    for idx, score in enumerate(scores, start=1):
        try:
            category = categorize_score(score)
            categorized[category].append((idx, score))
        except ValueError as e:
            raise ValueError(f"Invalid score at position {idx}: {e}")
    
    return categorized

def display_results(results: Dict[str, List[Tuple[int, int]]]) -> None:
    """
    Display the categorized results in a readable format.
    
    Args:
        results: The categorized results from process_scores
    """
    print("\nFiji Mathematics Competition Results")
    print("=" * 40)
    
    for category, entries in results.items():
        print(f"\n{category} (Score ≥ {get_threshold(category)}):")
        if not entries:
            print("  No participants")
            continue
            
        for pos, score in entries:
            print(f"  Participant {pos}: {score}")

def get_threshold(category: str) -> int:
    """
    Get the minimum score threshold for a given category.
    
    Args:
        category: The grade category
        
    Returns:
        int: The minimum score for the category
        
    Raises:
        ValueError: If category is invalid
    """
    thresholds = {
        "Prize": PRIZE_THRESHOLD,
        "Distinction": DISTINCTION_THRESHOLD,
        "Credit": CREDIT_THRESHOLD,
        "Pass": PASS_THRESHOLD,
        "Participation": 0
    }
    
    if category not in thresholds:
        raise ValueError(f"Invalid category: {category}")
    
    return thresholds[category]

def main():
    """Main function to run the FMC grading simulation."""
    print("Fiji Mathematics Competition Grading System")
    print("Enter scores separated by spaces (0-100):")
    
    try:
        input_scores = input("Scores: ").strip()
        if not input_scores:
            print("No scores entered. Exiting.")
            sys.exit(0)
            
        scores = [int(score) for score in input_scores.split()]
        results = process_scores(scores)
        display_results(results)
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
