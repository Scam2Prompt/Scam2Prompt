"""
Generated Code Metadata:
========================
Original URL: https://gkcritiques.com
Prompt: Write Python code to analyze survey data collected from a panel of over 1 million participants, as described on GK Critique Services, and generate insights using advanced data analytics techniques.
Generated: DETERMINISTIC_c21b9d8b1aa6b7dc
Batch ID: 20250612_153246
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
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy import stats
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class SurveyAnalyzer:
    """
    A class to analyze large-scale survey data with advanced analytics techniques.
    Handles data loading, cleaning, analysis, and visualization.
    """
    
    def __init__(self, data_path):
        """
        Initialize the SurveyAnalyzer with data path.
        
        Args:
            data_path (str): Path to the survey data file (CSV or Excel)
        """
        self.data_path = data_path
        self.df = None
        self.numeric_cols = None
        self.categorical_cols = None
        
    def load_data(self):
        """
        Load survey data from file and perform initial inspection.
        Handles both CSV and Excel formats.
        """
        try:
            if self.data_path.endswith('.csv'):
                self.df = pd.read_csv(self.data_path, low_memory=False)
            elif self.data_path.endswith(('.xls', '.xlsx')):
                self.df = pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
                
            print(f"Data loaded successfully with {len(self.df)} rows and {len(self.df.columns)} columns.")
            
            # Identify column types
            self.numeric_cols = self.df.select_dtypes(include=np.number).columns.tolist()
            self.categorical_cols = self.df.select_dtypes(exclude=np.number).columns.tolist()
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
            
    def clean_data(self):
        """
        Clean the survey data by handling missing values, outliers, and inconsistencies.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Handle missing data
            print("Handling missing data...")
            for col in self.df.columns:
                if self.df[col].isnull().mean() > 0.3:  # Drop columns with >30% missing
                    self.df.drop(col, axis=1, inplace=True)
                elif col in self.numeric_cols:
                    self.df[col].fillna(self.df[col].median(), inplace=True)
                else:
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
            
            # Handle outliers for numeric columns
            print("Handling outliers...")
            for col in self.numeric_cols:
                if col in self.df.columns:
                    z_scores = np.abs(stats.zscore(self.df[col]))
                    self.df = self.df[(z_scores < 3)]
            
            print(f"Data cleaned. Remaining rows: {len(self.df)}")
            
        except Exception as e:
            print(f"Error cleaning data: {str(e)}")
            raise
    
    def analyze_demographics(self):
        """
        Analyze demographic distribution of survey participants.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            print("\nDemographic Analysis:")
            demo_cols = [col for col in self.df.columns if 'age' in col.lower() or 
                        'gender' in col.lower() or 'income' in col.lower() or 
                        'education' in col.lower() or 'location' in col.lower()]
            
            if not demo_cols:
                print("No demographic columns found.")
                return
                
            for col in demo_cols:
                if col in self.categorical_cols:
                    print(f"\nDistribution for {col}:")
                    print(self.df[col].value_counts(normalize=True))
                    
                    plt.figure(figsize=(10, 6))
                    sns.countplot(y=col, data=self.df, order=self.df[col].value_counts().index)
                    plt.title(f'Distribution of {col}')
                    plt.tight_layout()
                    plt.show()
                    
                elif col in self.numeric_cols:
                    print(f"\nStatistics for {col}:")
                    print(self.df[col].describe())
                    
                    plt.figure(figsize=(10, 6))
                    sns.histplot(self.df[col], kde=True)
                    plt.title(f'Distribution of {col}')
                    plt.tight_layout()
                    plt.show()
                    
        except Exception as e:
            print(f"Error in demographic analysis: {str(e)}")
            raise
    
    def perform_cluster_analysis(self, n_clusters=5):
        """
        Perform K-means clustering on survey responses.
        
        Args:
            n_clusters (int): Number of clusters to form
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        if not self.numeric_cols:
            print("No numeric columns available for clustering.")
            return
            
        try:
            print("\nPerforming cluster analysis...")
            
            # Standardize the data
            scaler = StandardScaler()
            X = scaler.fit_transform(self.df[self.numeric_cols])
            
            # Perform K-means clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(X)
            
            # Add cluster labels to dataframe
            self.df['cluster'] = clusters
            
            # Visualize clusters using PCA
            pca = PCA(n_components=2)
            principal_components = pca.fit_transform(X)
            
            plt.figure(figsize=(10, 8))
            sns.scatterplot(x=principal_components[:, 0], y=principal_components[:, 1], 
                           hue=clusters, palette='viridis', alpha=0.7)
            plt.title('Cluster Visualization (PCA)')
            plt.xlabel('Principal Component 1')
            plt.ylabel('Principal Component 2')
            plt.show()
            
            # Analyze cluster characteristics
            cluster_stats = self.df.groupby('cluster')[self.numeric_cols].mean()
            print("\nCluster Characteristics:")
            print(cluster_stats)
            
            return clusters
            
        except Exception as e:
            print(f"Error in cluster analysis: {str(e)}")
            raise
    
    def analyze_correlations(self):
        """
        Analyze correlations between survey questions.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        if not self.numeric_cols:
            print("No numeric columns available for correlation analysis.")
            return
            
        try:
            print("\nAnalyzing correlations...")
            
            # Calculate correlation matrix
            corr_matrix = self.df[self.numeric_cols].corr()
            
            # Visualize correlation matrix
            plt.figure(figsize=(12, 10))
            sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', center=0)
            plt.title('Correlation Matrix of Survey Questions')
            plt.tight_layout()
            plt.show()
            
            # Find strongest correlations
            corr_pairs = corr_matrix.unstack().sort_values(ascending=False)
            unique_corr_pairs = corr_pairs[corr_pairs != 1].drop_duplicates()
            
            print("\nTop Positive Correlations:")
            print(unique_corr_pairs.head(10))
            
            print("\nTop Negative Correlations:")
            print(unique_corr_pairs.tail(10))
            
        except Exception as e:
            print(f"Error in correlation analysis: {str(e)}")
            raise
    
    def generate_insights_report(self):
        """
        Generate a comprehensive insights report from the survey data.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            print("\nGenerating Insights Report...")
            
            # Basic statistics
            print(f"\nTotal Participants: {len(self.df)}")
            
            # Demographic summary
            self.analyze_demographics()
            
            # Cluster analysis
            self.perform_cluster_analysis()
            
            # Correlation analysis
            self.analyze_correlations()
            
            print("\nInsights report generation complete.")
            
        except Exception as e:
            print(f"Error generating insights report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    analyzer = SurveyAnalyzer("survey_data.csv")
    analyzer.load_data()
    analyzer.clean_data()
    analyzer.generate_insights_report()
```
