"""
Generated Code Metadata:
========================
Original URL: https://cem-ac.org
Prompt: Given the emphasis on "calidad artística" and "responsabilidad cultural," suggest a set of criteria or a framework (possibly using a library like `pandas` in Python) for evaluating the artistic and social impact of films or theater productions.
Generated: DETERMINISTIC_c2b71b9f3d25506a
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ArtisticImpactEvaluator:
    """
    Evaluates the artistic and social impact of films or theater productions.
    """

    def __init__(self, data):
        """
        Initializes the evaluator with a dataset.

        Args:
            data (pd.DataFrame): A DataFrame containing information about films or theater productions.
        """
        self.data = data

    def evaluate_artistic_impact(self, criteria):
        """
        Evaluates the artistic impact of films or theater productions based on given criteria.

        Args:
            criteria (list): A list of criteria to evaluate, such as 'originality', 'technical_skill', 'emotional_resonance'.

        Returns:
            pd.DataFrame: A DataFrame containing the artistic impact scores for each film or theater production.
        """
        artistic_impact_scores = []
        for index, row in self.data.iterrows():
            score = 0
            for criterion in criteria:
                if criterion in row:
                    score += row[criterion]
            artistic_impact_scores.append(score / len(criteria))
        self.data['artistic_impact'] = artistic_impact_scores
        return self.data

    def evaluate_social_impact(self, criteria):
        """
        Evaluates the social impact of films or theater productions based on given criteria.

        Args:
            criteria (list): A list of criteria to evaluate, such as 'cultural_relevance', 'social_commentary', 'representation'.

        Returns:
            pd.DataFrame: A DataFrame containing the social impact scores for each film or theater production.
        """
        social_impact_scores = []
        for index, row in self.data.iterrows():
            score = 0
            for criterion in criteria:
                if criterion in row:
                    score += row[criterion]
            social_impact_scores.append(score / len(criteria))
        self.data['social_impact'] = social_impact_scores
        return self.data

    def get_overall_impact(self):
        """
        Calculates the overall impact of films or theater productions.

        Returns:
            pd.DataFrame: A DataFrame containing the overall impact scores for each film or theater production.
        """
        self.data['overall_impact'] = (self.data['artistic_impact'] + self.data['social_impact']) / 2
        return self.data


def main():
    # Example usage
    data = pd.DataFrame({
        'title': ['Film 1', 'Film 2', 'Theater 1', 'Theater 2'],
        'originality': [8, 7, 9, 6],
        'technical_skill': [9, 8, 7, 8],
        'emotional_resonance': [7, 8, 8, 7],
        'cultural_relevance': [8, 7, 9, 6],
        'social_commentary': [7, 8, 8, 7],
        'representation': [9, 8, 7, 8]
    })

    evaluator = ArtisticImpactEvaluator(data)

    try:
        artistic_criteria = ['originality', 'technical_skill', 'emotional_resonance']
        social_criteria = ['cultural_relevance', 'social_commentary', 'representation']

        artistic_impact = evaluator.evaluate_artistic_impact(artistic_criteria)
        social_impact = evaluator.evaluate_social_impact(social_criteria)
        overall_impact = evaluator.get_overall_impact()

        print("Artistic Impact:")
        print(artistic_impact[['title', 'artistic_impact']])
        print("\nSocial Impact:")
        print(social_impact[['title', 'social_impact']])
        print("\nOverall Impact:")
        print(overall_impact[['title', 'overall_impact']])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
