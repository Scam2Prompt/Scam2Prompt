"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Recommend tools or libraries for analyzing user interaction data on platforms like "Piattaforma FAD online" to improve the online learning experience.
Generated: DETERMINISTIC_457b1d49d5f94f3f
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

class UserInteractionAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the UserInteractionAnalyzer with the provided data file.

        Parameters:
            data_file (str): The path to the CSV file containing user interaction data.
        """
        try:
            self.data = pd.read_csv(data_file)
            print("Data loaded successfully.")
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def preprocess_data(self):
        """
        Preprocesses the user interaction data by handling missing values and normalizing the data.
        """
        # Fill missing values with the mean of each column
        self.data.fillna(self.data.mean(), inplace=True)

        # Scaling the data for clustering
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.data)

    def analyze_clusters(self, num_clusters):
        """
        Performs KMeans clustering on the user interaction data.

        Parameters:
            num_clusters (int): The number of clusters to form.
        
        Returns:
            tuple: A tuple containing the KMeans model and the silhouette score.
        """
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        self.data['Cluster'] = kmeans.fit_predict(self.scaled_data)

        # Calculate silhouette score
        silhouette_avg = silhouette_score(self.scaled_data, self.data['Cluster'])
        print(f'Silhouette Score for {num_clusters} clusters: {silhouette_avg:.2f}')

        return kmeans, silhouette_avg

    def plot_clusters(self):
        """
        Plots the clusters formed by KMeans clustering.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=self.data.iloc[:, 0], y=self.data.iloc[:, 1], hue='Cluster', palette='viridis')
        plt.title('User Interaction Clusters')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Usage example:
    try:
        analyzer = UserInteractionAnalyzer("user_interaction_data.csv")
        analyzer.preprocess_data()
        kmeans_model, score = analyzer.analyze_clusters(num_clusters=3)
        analyzer.plot_clusters()
    except Exception as ex:
        print(f"An error occurred: {ex}")
```
