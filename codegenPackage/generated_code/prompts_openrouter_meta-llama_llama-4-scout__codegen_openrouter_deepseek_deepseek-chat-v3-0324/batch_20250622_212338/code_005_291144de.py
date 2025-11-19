"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Create a code snippet in R or Python for analyzing customer data and providing insights for consultant or trainer services, highlighting the importance of data-driven decision-making in digital transformation.
Generated: DETERMINISTIC_291144de40c40621
Batch ID: 20250622_212338
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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Set style for visualizations
sns.set(style="whitegrid")

class CustomerAnalyzer:
    """
    A class to analyze customer data and provide insights for consultant/trainer services.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with customer data.
        
        Args:
            data_path (str): Path to the customer data file (CSV or Excel)
        """
        try:
            if data_path.endswith('.csv'):
                self.df = pd.read_csv(data_path)
            elif data_path.endswith('.xlsx'):
                self.df = pd.read_excel(data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            print(f"Data loaded successfully with {self.df.shape[0]} records and {self.df.shape[1]} features.")
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            self.df = None
    
    def clean_data(self):
        """
        Clean the customer data by handling missing values and outliers.
        """
        if self.df is None:
            print("No data to clean. Load data first.")
            return
        
        # Handle missing values
        self.df.fillna(self.df.median(numeric_only=True), inplace=True)
        
        # Remove duplicates
        self.df.drop_duplicates(inplace=True)
        
        # Handle outliers for numeric columns
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - (1.5 * iqr)
            upper_bound = q3 + (1.5 * iqr)
            self.df[col] = np.where(
                self.df[col] < lower_bound, lower_bound,
                np.where(
                    self.df[col] > upper_bound, upper_bound,
                    self.df[col]
                )
            )
        
        print("Data cleaning completed.")
    
    def exploratory_analysis(self):
        """
        Perform exploratory data analysis and generate visualizations.
        """
        if self.df is None:
            print("No data to analyze. Load data first.")
            return
        
        # Basic statistics
        print("\nBasic Statistics:")
        print(self.df.describe())
        
        # Customer segmentation visualization
        plt.figure(figsize=(12, 6))
        sns.countplot(data=self.df, x='customer_segment')
        plt.title("Customer Segment Distribution")
        plt.xticks(rotation=45)
        plt.show()
        
        # Revenue distribution
        if 'revenue' in self.df.columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df['revenue'], kde=True)
            plt.title("Revenue Distribution")
            plt.show()
        
        # Correlation heatmap
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        if len(numeric_cols) > 1:
            plt.figure(figsize=(10, 8))
            sns.heatmap(self.df[numeric_cols].corr(), annot=True, cmap='coolwarm')
            plt.title("Feature Correlation Heatmap")
            plt.show()
    
    def segment_customers(self, n_clusters=3):
        """
        Perform customer segmentation using K-means clustering.
        
        Args:
            n_clusters (int): Number of clusters to create
        """
        if self.df is None:
            print("No data to segment. Load data first.")
            return
        
        # Select relevant features for clustering
        features = ['annual_spend', 'engagement_score', 'product_usage']
        features = [f for f in features if f in self.df.columns]
        
        if len(features) < 2:
            print("Insufficient features for clustering.")
            return
        
        # Standardize the data
        scaler = StandardScaler()
        X = self.df[features]
        X_scaled = scaler.fit_transform(X)
        
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(X_scaled)
        
        # Add cluster labels to dataframe
        self.df['cluster'] = clusters
        
        # Calculate silhouette score
        score = silhouette_score(X_scaled, clusters)
        print(f"Silhouette Score: {score:.2f}")
        
        # Visualize clusters
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x=features[0], y=features[1],
            hue='cluster', data=self.df,
            palette='viridis'
        )
        plt.title("Customer Clusters")
        plt.show()
        
        # Cluster profiles
        print("\nCluster Profiles:")
        print(self.df.groupby('cluster')[features].mean())
    
    def generate_recommendations(self):
        """
        Generate data-driven recommendations for consultant/trainer services.
        """
        if self.df is None:
            print("No data to generate recommendations. Load data first.")
            return
        
        recommendations = []
        
        # Check if clustering was performed
        if 'cluster' in self.df.columns:
            cluster_sizes = self.df['cluster'].value_counts(normalize=True)
            for cluster, size in cluster_sizes.items():
                rec = {
                    'cluster': cluster,
                    'size': f"{size*100:.1f}%",
                    'recommendation': f"Develop targeted training program for cluster {cluster} customers"
                }
                recommendations.append(rec)
        
        # Check for engagement opportunities
        if 'engagement_score' in self.df.columns:
            low_engagement = self.df[self.df['engagement_score'] < self.df['engagement_score'].quantile(0.25)]
            if len(low_engagement) > 0:
                recommendations.append({
                    'cluster': 'Low Engagement',
                    'size': f"{len(low_engagement)/len(self.df)*100:.1f}%",
                    'recommendation': "Implement engagement improvement workshops"
                })
        
        # Convert to DataFrame for nice display
        rec_df = pd.DataFrame(recommendations)
        if not rec_df.empty:
            print("\nData-Driven Recommendations:")
            print(rec_df.to_string(index=False))
        else:
            print("No specific recommendations could be generated from the available data.")

# Example usage
if __name__ == "__main__":
    analyzer = CustomerAnalyzer("customer_data.csv")
    analyzer.clean_data()
    analyzer.exploratory_analysis()
    analyzer.segment_customers(n_clusters=4)
    analyzer.generate_recommendations()
```
