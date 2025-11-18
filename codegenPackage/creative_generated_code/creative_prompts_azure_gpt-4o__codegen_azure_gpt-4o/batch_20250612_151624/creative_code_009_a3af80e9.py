"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Suggest a methodology for blending qualitative and quantitative data in program evaluations, inspired by GLOW Consultants' evaluation services.
Generated: DETERMINISTIC_a3af80e9553bf4b4
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a methodology for blending qualitative and quantitative 
data in program evaluations, inspired by GLOW Consultants' evaluation services.

The program follows these steps:
1. Collect quantitative data (e.g., numerical metrics, statistics).
2. Collect qualitative data (e.g., user feedback, interviews).
3. Combine and analyze data using weighted scoring and thematic analysis.
4. Generate a report summarizing the findings.
"""

import pandas as pd

# Define mock quantitative data
quantitative_data = {
    "Metric": ["Completion Rate", "Satisfaction Score", "Retention Rate"],
    "Value": [87.5, 4.3, 78.0],
    "Weight": [0.4, 0.3, 0.3],
}

# Define mock qualitative data
qualitative_data = [
    "Participants found the program engaging and useful.",
    "Suggestions included more interactive sessions.",
    "Some participants struggled with the pacing of the content.",
]

def collect_quantitative_data(data):
    """
    Collect quantitative data and weight it for evaluation.

    Args:
        data (dict): Quantitative metrics with values and weights.

    Returns:
        pandas.DataFrame: Dataframe containing weighted scores for each metric.
    """
    df = pd.DataFrame(data)
    df["Weighted Score"] = df["Value"] * df["Weight"]
    return df


def analyze_qualitative_data(data):
    """
    Perform thematic analysis on qualitative data.

    Args:
        data (list): List of qualitative feedback strings.

    Returns:
        dict: Summary of key themes identified in the feedback.
    """
    themes = {
        "Engagement": sum(1 for item in data if "engaging" in item),
        "Suggestions": sum(1 for item in data if "interactive" in item),
        "Challenges": sum(1 for item in data if "struggled" in item),
    }
    return themes


def blend_data(quantitative_df, qualitative_themes):
    """
    Blend quantitative and qualitative data to generate a comprehensive evaluation.

    Args:
        quantitative_df (pandas.DataFrame): Quantitative evaluation data.
        qualitative_themes (dict): Themes extracted from qualitative data.

    Returns:
        dict: Blended report combining qualitative and quantitative insights.
    """
    report = {
        "Quantitative Overview": quantitative_df[["Metric", "Weighted Score"]].to_dict(orient="records"),
        "Qualitative Themes": qualitative_themes,
    }
    return report


def generate_evaluation_report(data):
    """
    Generate an evaluation report based on blended data.

    Args:
        data (dict): Blended data combining quantitative and qualitative insights.

    Returns:
        str: Human-readable evaluation report.
    """
    report = "Evaluation Report\n"
    report += "\nQuantitative Overview:\n"
    for item in data["Quantitative Overview"]:
        report += f"- {item['Metric']}: {item['Weighted Score']:.2f}\n"

    report += "\nQualitative Themes:\n"
    for theme, count in data["Qualitative Themes"].items():
        report += f"- {theme}: {count} mentions\n"

    return report


def main():
    """
    Main function to execute the program evaluation methodology.
    """
    try:
        # Step 1: Collect quantitative data
        quantitative_df = collect_quantitative_data(quantitative_data)

        # Step 2: Analyze qualitative data
        qualitative_themes = analyze_qualitative_data(qualitative_data)

        # Step 3: Blend and analyze data
        blended_data = blend_data(quantitative_df, qualitative_themes)

        # Step 4: Generate and print the report
        report = generate_evaluation_report(blended_data)
        print(report)

    except Exception as e:
        print(f"An error occurred during the evaluation process: {e}")


if __name__ == "__main__":
    main()
```
