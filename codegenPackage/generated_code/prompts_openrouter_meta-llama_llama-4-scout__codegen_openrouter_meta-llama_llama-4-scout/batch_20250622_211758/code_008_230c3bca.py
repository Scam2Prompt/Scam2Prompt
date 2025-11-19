"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Recommend a suitable algorithm for matching influencers with a brand’s target audience based on niche, engagement rate, and values.
Generated: DETERMINISTIC_230c3bca1e76e88f
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InfluencerMatcher:
    """
    A class used to match influencers with a brand's target audience.

    Attributes:
    ----------
    influencers : pd.DataFrame
        A DataFrame containing information about influencers.
        It should have columns: 'id', 'niche', 'engagement_rate', 'values'.

    brands : pd.DataFrame
        A DataFrame containing information about brands.
        It should have columns: 'id', 'target_niche', 'target_values'.

    vectorizer : TfidfVectorizer
        A TF-IDF vectorizer used to convert text data into vectors.

    """

    def __init__(self, influencers, brands):
        """
        Initializes the InfluencerMatcher class.

        Parameters:
        ----------
        influencers : pd.DataFrame
            A DataFrame containing information about influencers.
        brands : pd.DataFrame
            A DataFrame containing information about brands.

        """
        self.influencers = influencers
        self.brands = brands
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def _calculate_niche_similarity(self, influencer_niche, target_niche):
        """
        Calculates the similarity between an influencer's niche and a brand's target niche.

        Parameters:
        ----------
        influencer_niche : str
            The influencer's niche.
        target_niche : str
            The brand's target niche.

        Returns:
        -------
        float
            The similarity between the two niches.

        """
        # Create a TF-IDF vectorizer and fit it to the niches
        niche_vectors = self.vectorizer.fit_transform([influencer_niche, target_niche])
        # Calculate the cosine similarity between the two vectors
        similarity = cosine_similarity(niche_vectors[0:1], niche_vectors[1:2])
        return similarity[0][0]

    def _calculate_values_similarity(self, influencer_values, target_values):
        """
        Calculates the similarity between an influencer's values and a brand's target values.

        Parameters:
        ----------
        influencer_values : str
            The influencer's values.
        target_values : str
            The brand's target values.

        Returns:
        -------
        float
            The similarity between the two values.

        """
        # Create a TF-IDF vectorizer and fit it to the values
        values_vectors = self.vectorizer.fit_transform([influencer_values, target_values])
        # Calculate the cosine similarity between the two vectors
        similarity = cosine_similarity(values_vectors[0:1], values_vectors[1:2])
        return similarity[0][0]

    def match_influencers(self):
        """
        Matches influencers with brands based on niche, engagement rate, and values.

        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the matched influencers and brands.

        """
        # Initialize an empty list to store the matched influencers and brands
        matches = []

        # Iterate over each brand
        for brand_index, brand in self.brands.iterrows():
            # Iterate over each influencer
            for influencer_index, influencer in self.influencers.iterrows():
                try:
                    # Calculate the niche similarity
                    niche_similarity = self._calculate_niche_similarity(influencer['niche'], brand['target_niche'])

                    # Calculate the values similarity
                    values_similarity = self._calculate_values_similarity(influencer['values'], brand['target_values'])

                    # Calculate a score based on niche similarity, values similarity, and engagement rate
                    score = niche_similarity * 0.4 + values_similarity * 0.3 + influencer['engagement_rate'] * 0.3

                    # Append the match to the list
                    matches.append({
                        'brand_id': brand['id'],
                        'influencer_id': influencer['id'],
                        'score': score,
                        'niche_similarity': niche_similarity,
                        'values_similarity': values_similarity,
                    })
                except Exception as e:
                    # Log any exceptions
                    print(f"Error matching influencer {influencer['id']} with brand {brand['id']}: {str(e)}")

        # Convert the list to a DataFrame and return it
        return pd.DataFrame(matches)

    def get_top_matches(self, num_matches):
        """
        Gets the top matches for each brand.

        Parameters:
        ----------
        num_matches : int
            The number of top matches to return.

        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the top matches for each brand.

        """
        # Get all matches
        matches = self.match_influencers()

        # Sort the matches by score in descending order
        matches = matches.sort_values(by='score', ascending=False)

        # Group the matches by brand ID and get the top matches for each brand
        top_matches = matches.groupby('brand_id').head(num_matches)

        return top_matches


# Example usage
if __name__ == "__main__":
    # Create sample data
    influencers = pd.DataFrame({
        'id': [1, 2, 3],
        'niche': ['Fashion', 'Beauty', 'Gaming'],
        'engagement_rate': [0.05, 0.03, 0.02],
        'values': ['Sustainability, Quality', 'Natural, Organic', 'Fun, Competitive']
    })

    brands = pd.DataFrame({
        'id': [1, 2],
        'target_niche': ['Fashion', 'Beauty'],
        'target_values': ['Sustainable, Eco-friendly', 'Natural, Cruelty-free']
    })

    # Create an InfluencerMatcher instance
    matcher = InfluencerMatcher(influencers, brands)

    # Get the top matches for each brand
    top_matches = matcher.get_top_matches(1)

    # Print the top matches
    print(top_matches)
```
