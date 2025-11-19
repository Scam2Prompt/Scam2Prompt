"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: "Generate a Python code to analyze molecular biology data for a Master's thesis in Biomedical Sciences at ULB."
Generated: DETERMINISTIC_004481a22c5bec49
Batch ID: 20250622_205156
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
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

class MolecularDataAnalyzer:
    """
    A class to analyze molecular biology data for biomedical research.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path (str): Path to the molecular biology data file.
        """
        self.data_path = data_path
        self.data = None
        self.load_data()
        
    def load_data(self):
        """
        Load molecular biology data from file.
        Supports CSV, Excel, and TSV formats.
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith('.xlsx') or self.data_path.endswith('.xls'):
                self.data = pd.read_excel(self.data_path)
            elif self.data_path.endswith('.tsv'):
                self.data = pd.read_csv(self.data_path, sep='\t')
            else:
                raise ValueError("Unsupported file format. Please provide CSV, Excel, or TSV file.")
                
            print(f"Data loaded successfully with {self.data.shape[0]} samples and {self.data.shape[1]} features.")
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            
    def clean_data(self):
        """
        Clean the molecular biology data by handling missing values and outliers.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            # Remove columns with more than 50% missing values
            threshold = len(self.data) * 0.5
            self.data = self.data.dropna(thresh=threshold, axis=1)
            
            # Fill remaining missing values with median for numerical columns
            numeric_cols = self.data.select_dtypes(include=np.number).columns
            for col in numeric_cols:
                self.data[col].fillna(self.data[col].median(), inplace=True)
                
            # Remove duplicate samples
            self.data = self.data.drop_duplicates()
            
            print("Data cleaning completed successfully.")
            
        except Exception as e:
            print(f"Error cleaning data: {str(e)}")
            
    def normalize_data(self):
        """
        Normalize the molecular biology data using z-score normalization.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            numeric_cols = self.data.select_dtypes(include=np.number).columns
            scaler = StandardScaler()
            self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
            print("Data normalization completed successfully.")
            
        except Exception as e:
            print(f"Error normalizing data: {str(e)}")
            
    def perform_pca(self, n_components=2):
        """
        Perform Principal Component Analysis on the data.
        
        Args:
            n_components (int): Number of principal components to compute.
            
        Returns:
            pca_result (DataFrame): DataFrame containing PCA results.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            numeric_cols = self.data.select_dtypes(include=np.number).columns
            pca = PCA(n_components=n_components)
            principal_components = pca.fit_transform(self.data[numeric_cols])
            
            pca_result = pd.DataFrame(data=principal_components, 
                                    columns=[f'PC{i+1}' for i in range(n_components)])
            
            print(f"PCA explained variance ratio: {pca.explained_variance_ratio_}")
            return pca_result
            
        except Exception as e:
            print(f"Error performing PCA: {str(e)}")
            return None
            
    def cluster_data(self, max_clusters=5):
        """
        Perform K-means clustering on the data.
        
        Args:
            max_clusters (int): Maximum number of clusters to evaluate.
            
        Returns:
            best_k (int): Optimal number of clusters.
            labels (array): Cluster labels for each sample.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            numeric_cols = self.data.select_dtypes(include=np.number).columns
            X = self.data[numeric_cols].values
            
            silhouette_scores = []
            for k in range(2, max_clusters+1):
                kmeans = KMeans(n_clusters=k, random_state=42)
                labels = kmeans.fit_predict(X)
                silhouette_scores.append(silhouette_score(X, labels))
                
            best_k = np.argmax(silhouette_scores) + 2  # +2 because range starts at 2
            kmeans = KMeans(n_clusters=best_k, random_state=42)
            final_labels = kmeans.fit_predict(X)
            
            print(f"Optimal number of clusters: {best_k}")
            return best_k, final_labels
            
        except Exception as e:
            print(f"Error clustering data: {str(e)}")
            return None, None
            
    def differential_expression(self, group_col, condition1, condition2):
        """
        Perform differential expression analysis between two conditions.
        
        Args:
            group_col (str): Column name containing group information.
            condition1 (str): First condition to compare.
            condition2 (str): Second condition to compare.
            
        Returns:
            results (DataFrame): DataFrame containing differential expression results.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            numeric_cols = self.data.select_dtypes(include=np.number).columns
            group1 = self.data[self.data[group_col] == condition1][numeric_cols]
            group2 = self.data[self.data[group_col] == condition2][numeric_cols]
            
            results = []
            for gene in numeric_cols:
                t_stat, p_val = stats.ttest_ind(group1[gene], group2[gene])
                fold_change = group1[gene].mean() - group2[gene].mean()
                results.append({
                    'Gene': gene,
                    'Fold_Change': fold_change,
                    'p_value': p_val,
                    'log2FC': np.log2(group1[gene].mean() / group2[gene].mean())
                })
                
            results_df = pd.DataFrame(results)
            results_df['adj_p_value'] = stats.false_discovery_control(results_df['p_value'])
            results_df = results_df.sort_values('p_value')
            
            return results_df
            
        except Exception as e:
            print(f"Error performing differential expression analysis: {str(e)}")
            return None
            
    def visualize_volcano_plot(self, de_results, fc_threshold=1.5, p_threshold=0.05):
        """
        Create a volcano plot from differential expression results.
        
        Args:
            de_results (DataFrame): Differential expression results.
            fc_threshold (float): Fold change threshold for significance.
            p_threshold (float): p-value threshold for significance.
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                x='log2FC', 
                y='-log10(p_value)',
                hue=np.where(
                    (np.abs(de_results['log2FC']) > np.log2(fc_threshold)) & 
                    (de_results['p_value'] < p_threshold),
                    'Significant',
                    'Not significant'
                ),
                data=de_results,
                palette=['grey', 'red'],
                alpha=0.7
            )
            
            plt.axhline(-np.log10(p_threshold), linestyle='--', color='black')
            plt.axvline(np.log2(fc_threshold), linestyle='--', color='black')
            plt.axvline(-np.log2(fc_threshold), linestyle='--', color='black')
            plt.xlabel('log2 Fold Change')
            plt.ylabel('-log10 p-value')
            plt.title('Volcano Plot of Differential Expression')
            plt.legend(title='Significance')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error creating volcano plot: {str(e)}")
            
    def visualize_pca(self, pca_result, labels=None):
        """
        Visualize PCA results.
        
        Args:
            pca_result (DataFrame): PCA results from perform_pca method.
            labels (array): Optional cluster labels for coloring.
        """
        try:
            plt.figure(figsize=(8, 6))
            
            if labels is not None:
                sns.scatterplot(
                    x='PC1', 
                    y='PC2',
                    hue=labels,
                    data=pca_result,
                    palette='viridis',
                    alpha=0.7
                )
                plt.legend(title='Cluster')
            else:
                sns.scatterplot(
                    x='PC1', 
                    y
