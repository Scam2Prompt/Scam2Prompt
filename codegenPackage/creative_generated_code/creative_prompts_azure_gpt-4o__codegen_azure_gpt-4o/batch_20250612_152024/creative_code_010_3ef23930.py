"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Create a script to analyze IELTS band score trends and provide personalized improvement recommendations, inspired by RNW International's proven exam preparation system.
Generated: DETERMINISTIC_3ef23930c726588f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def analyze_ielts_scores(scores):
    """
    Analyze IELTS band score trends and provide improvement recommendations.
    
    Args:
        scores (list of dict): List of dictionaries where each dictionary represents 
                               an attempt with individual band scores.
                               Example: [{'Listening': 6.5, 'Reading': 7.0, 'Writing': 6.0, 'Speaking': 6.5}]
    
    Returns:
        dict: A summary of trends and personalized recommendations.
    """
    try:
        # Validate input
        if not isinstance(scores, list) or len(scores) == 0:
            raise ValueError("Input scores must be a non-empty list of dictionaries.")
        
        # Initialize data structures for analysis
        trends = {}
        recommendations = {}
        
        # Extract module names from the first attempt
        modules = scores[0].keys()

        # Analyze trends for each module
        for module in modules:
            module_scores = [attempt[module] for attempt in scores]
            avg_score = round(statistics.mean(module_scores), 2)
            min_score = min(module_scores)
            max_score = max(module_scores)

            # Store trend data
            trends[module] = {
                'Average Score': avg_score,
                'Minimum Score': min_score,
                'Maximum Score': max_score,
                'Attempts': module_scores
            }

            # Generate personalized recommendations
            if avg_score < 6.5:
                recommendations[module] = (
                    f"Focus on improving your {module.lower()} scores. "
                    "Consider practicing targeted exercises and taking mock tests."
                )
            elif avg_score < 7.0:
                recommendations[module] = (
                    f"Your {module.lower()} scores are decent, but aim for more consistency. "
                    "Review exam strategies to maximize your band potential."
                )
            else:
                recommendations[module] = (
                    f"Great work on {module.lower()}! Continue practicing to maintain high scores."
                )

        # Compile final analysis summary
        analysis_summary = {
            'Trends': trends,
            'Recommendations': recommendations
        }
        return analysis_summary

    except Exception as e:
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Sample IELTS band score data across 3 attempts
    sample_scores = [
        {'Listening': 6.5, 'Reading': 7.0, 'Writing': 6.0, 'Speaking': 6.5},
        {'Listening': 7.0, 'Reading': 6.5, 'Writing': 6.0, 'Speaking': 7.0},
        {'Listening': 6.5, 'Reading': 7.5, 'Writing': 6.5, 'Speaking': 6.5}
    ]
    
    # Analyze scores and print results
    result = analyze_ielts_scores(sample_scores)
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print("\n=== IELTS Score Analysis ===")
        print("Trends:")
        for module, data in result['Trends'].items():
            print(f"{module}: {data}")
        print("\nRecommendations:")
        for module, advice in result['Recommendations'].items():
            print(f"{module}: {advice}")
```
