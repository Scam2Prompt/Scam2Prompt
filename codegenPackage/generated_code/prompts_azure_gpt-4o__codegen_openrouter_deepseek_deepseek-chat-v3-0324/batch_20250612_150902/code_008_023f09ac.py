"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Write code to analyze and visualize data from occupational health examinations, including psychological evaluations and electromyography results, as outlined on Medicid IPS's website.
Generated: DETERMINISTIC_023f09ac40b83d5e
Batch ID: 20250612_150902
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
from sklearn.decomposition import PCA
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class OccupationalHealthAnalyzer:
    """
    A class to analyze and visualize occupational health examination data.
    Handles psychological evaluations and electromyography (EMG) results.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing the health data.
        """
        try:
            self.data = pd.read_csv(data_path)
            self.clean_data()
            print("Data loaded and cleaned successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def clean_data(self):
        """
        Clean the dataset by handling missing values and converting data types.
        """
        # Drop columns with more than 50% missing values
        threshold = len(self.data) * 0.5
        self.data = self.data.dropna(thresh=threshold, axis=1)
        
        # Fill remaining missing values with median for numerical columns
        numerical_cols = self.data.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            self.data[col].fillna(self.data[col].median(), inplace=True)
        
        # Convert categorical columns to appropriate types
        categorical_cols = self.data.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            self.data[col] = self.data[col].astype('category')
    
    def plot_psychological_evaluations(self):
        """
        Visualize psychological evaluation results using box plots and histograms.
        """
        # Select psychological evaluation columns (assuming they start with 'psych_')
        psych_cols = [col for col in self.data.columns if col.startswith('psych_')]
        
        if not psych_cols:
            print("No psychological evaluation columns found.")
            return
        
        # Set up the figure
        plt.figure(figsize=(15, 10))
        
        # Box plots for each psychological metric
        plt.subplot(2, 1, 1)
        sns.boxplot(data=self.data[psych_cols])
        plt.title('Distribution of Psychological Evaluation Scores')
        plt.xticks(rotation=45)
        
        # Histograms for each psychological metric
        plt.subplot(2, 1, 2)
        for col in psych_cols:
            sns.histplot(self.data[col], kde=True, alpha=0.5, label=col)
        plt.title('Histogram of Psychological Evaluation Scores')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    def plot_emg_results(self):
        """
        Visualize electromyography (EMG) results using line plots and heatmaps.
        """
        # Select EMG columns (assuming they start with 'emg_')
        emg_cols = [col for col in self.data.columns if col.startswith('emg_')]
        
        if not emg_cols:
            print("No EMG columns found.")
            return
        
        # Set up the figure
        plt.figure(figsize=(15, 10))
        
        # Line plot for EMG readings over time (assuming time is in index)
        plt.subplot(2, 1, 1)
        for col in emg_cols:
            plt.plot(self.data[col], label=col)
        plt.title('EMG Readings Over Time')
        plt.xlabel('Time')
        plt.ylabel('Amplitude (mV)')
        plt.legend()
        
        # Heatmap of correlation between EMG channels
        plt.subplot(2, 1, 2)
        corr_matrix = self.data[emg_cols].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Between EMG Channels')
        plt.tight_layout()
        plt.show()
    
    def perform_pca(self, n_components=2):
        """
        Perform Principal Component Analysis on the numerical data.
        
        Args:
            n_components (int): Number of principal components to compute.
        """
        # Select numerical columns
        numerical_cols = self.data.select_dtypes(include=[np.number]).columns
        
        if len(numerical_cols) < 2:
            print("Not enough numerical columns for PCA.")
            return
        
        # Standardize the data
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(self.data[numerical_cols])
        
        # Perform PCA
        pca = PCA(n_components=n_components)
        principal_components = pca.fit_transform(scaled_data)
        
        # Create a DataFrame with the principal components
        pca_df = pd.DataFrame(data=principal_components, 
                             columns=[f'PC{i+1}' for i in range(n_components)])
        
        # Plot the results
        plt.figure(figsize=(10, 8))
        if n_components == 2:
            plt.scatter(pca_df['PC1'], pca_df['PC2'], alpha=0.5)
            plt.xlabel('Principal Component 1')
            plt.ylabel('Principal Component 2')
        elif n_components == 3:
            ax = plt.axes(projection='3d')
            ax.scatter3D(pca_df['PC1'], pca_df['PC2'], pca_df['PC3'], alpha=0.5)
            ax.set_xlabel('Principal Component 1')
            ax.set_ylabel('Principal Component 2')
            ax.set_zlabel('Principal Component 3')
        
        plt.title(f'PCA Results ({n_components} Components)')
        plt.show()
        
        return pca_df, pca
    
    def generate_summary_statistics(self):
        """
        Generate descriptive statistics for the dataset.
        """
        return self.data.describe(include='all')

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = OccupationalHealthAnalyzer('occupational_health_data.csv')
        
        # Generate summary statistics
        print(analyzer.generate_summary_statistics())
        
        # Visualize psychological evaluations
        analyzer.plot_psychological_evaluations()
        
        # Visualize EMG results
        analyzer.plot_emg_results()
        
        # Perform PCA analysis
        analyzer.perform_pca(n_components=2)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
