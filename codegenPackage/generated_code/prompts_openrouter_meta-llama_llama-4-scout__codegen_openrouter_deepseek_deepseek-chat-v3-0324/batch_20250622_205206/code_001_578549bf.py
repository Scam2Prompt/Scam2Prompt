"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: "Recommend a web server software for serving static websites, considering performance and speed, as seen with LiteSpeed Web Server."
Generated: DETERMINISTIC_578549bf96739a8d
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Static Web Server Recommendation Tool
This script recommends web server software for serving static websites
based on performance and speed considerations.
"""

import argparse

def recommend_web_server(use_case: str = "static") -> str:
    """
    Recommends web server software based on the specified use case.
    
    Args:
        use_case (str): The type of website being served. Defaults to "static".
        
    Returns:
        str: Recommended web server software.
        
    Raises:
        ValueError: If an unsupported use case is provided.
    """
    recommendations = {
        "static": {
            "top_choice": "LiteSpeed Web Server",
            "alternatives": [
                "Nginx",
                "Apache HTTP Server",
                "Caddy",
                "H2O"
            ],
            "reason": "Excellent performance for static content with low resource usage"
        },
        "dynamic": {
            "top_choice": "Nginx",
            "alternatives": [
                "Apache HTTP Server",
                "LiteSpeed Web Server",
                "Microsoft IIS"
            ],
            "reason": "Good balance of performance and features for dynamic content"
        }
    }
    
    if use_case not in recommendations:
        raise ValueError(f"Unsupported use case: {use_case}. Supported values are: {list(recommendations.keys())}")
    
    return recommendations[use_case]

def main():
    parser = argparse.ArgumentParser(description="Web Server Recommendation Tool")
    parser.add_argument(
        "--use-case",
        type=str,
        default="static",
        choices=["static", "dynamic"],
        help="Type of website being served (static/dynamic)"
    )
    
    args = parser.parse_args()
    
    try:
        recommendation = recommend_web_server(args.use_case)
        print(f"Top Recommendation: {recommendation['top_choice']}")
        print(f"Reason: {recommendation['reason']}")
        print("\nAlternatives:")
        for alt in recommendation['alternatives']:
            print(f"- {alt}")
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```
