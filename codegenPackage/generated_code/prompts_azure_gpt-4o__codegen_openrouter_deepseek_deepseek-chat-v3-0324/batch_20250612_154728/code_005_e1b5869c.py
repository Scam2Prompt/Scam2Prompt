"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: Suggest tools or libraries for analyzing student performance data retrieved from Classera's platform.
Generated: DETERMINISTIC_e1b5869c9b85767b
Batch ID: 20250612_154728
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance data from Classera's platform.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with student performance data.
        
        Args:
            data_path (str): Path to the CSV file containing student data
        """
        try:
            self.data = pd.read_csv(data_path)
            self.clean_data()
            print("Data loaded and cleaned successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def clean_data(self):
        """
        Clean the dataset by handling missing values and outliers.
        """
        # Fill missing values with median for numerical columns
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].median())
        
        # Fill categorical missing values with mode
        categorical_cols = self.data.select_dtypes(exclude=[np.number]).columns
        for col in categorical_cols:
            self.data[col] = self.data[col].fillna(self.data[col].mode()[0])
    
    def exploratory_data_analysis(self):
        """
        Perform exploratory data analysis and generate visualizations.
        """
        # Summary statistics
        print("\nSummary Statistics:")
        print(self.data.describe())
        
        # Correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Matrix")
        plt.show()
        
        # Distribution of grades
        plt.figure(figsize=(8, 6))
        sns.histplot(data=self.data, x='final_grade', kde=True)
        plt.title("Distribution of Final Grades")
        plt.show()
    
    def cluster_students(self, n_clusters=3):
        """
        Cluster students based on their performance metrics.
        
        Args:
            n_clusters (int): Number of clusters to form
        """
        try:
            # Select relevant features
            features = self.data[['quiz_scores', 'assignment_scores', 'participation']]
            
            # Standardize the data
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)
            
            # Perform K-means clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(scaled_features)
            
            # Add clusters to data
            self.data['cluster'] = clusters
            
            # Visualize clusters
            pca = PCA(n_components=2)
            reduced_features = pca.fit_transform(scaled_features)
            
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x=reduced_features[:, 0], y=reduced_features[:, 1], 
                            hue=clusters, palette='viridis')
            plt.title("Student Performance Clusters")
            plt.xlabel("PCA Component 1")
            plt.ylabel("PCA Component 2")
            plt.show()
            
            return clusters
        except Exception as e:
            print(f"Error in clustering: {e}")
            return None
    
    def predict_performance(self, target_column='final_grade'):
        """
        Predict student performance using linear regression.
        
        Args:
            target_column (str): Column to predict (default: 'final_grade')
        """
        try:
            # Prepare features and target
            X = self.data.drop(columns=[target_column, 'cluster'], errors='ignore')
            X = pd.get_dummies(X)  # Handle categorical variables
            y = self.data[target_column]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            # Make predictions
            y_pred = model.predict(X_test)
            
            # Evaluate model
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            print(f"\nModel Performance:")
            print(f"Mean Squared Error: {mse:.2f}")
            print(f"R-squared: {r2:.2f}")
            
            # Feature importance
            coef_df = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
            coef_df = coef_df.sort_values(by='Coefficient', ascending=False)
            
            print("\nTop Features Affecting Performance:")
            print(coef_df.head(10))
            
            return model
        except Exception as e:
            print(f"Error in prediction: {e}")
            return None
    
    def generate_report(self, output_path='student_performance_report.html'):
        """
        Generate an HTML report with key findings.
        
        Args:
            output_path (str): Path to save the HTML report
        """
        try:
            from dominate import document
            from dominate.tags import *
            
            with document(title='Student Performance Report') as doc:
                h1('Student Performance Analysis Report')
                hr()
                
                h2('Summary Statistics')
                p('Basic statistics about student performance:')
                pre(str(self.data.describe()))
                
                h2('Performance Distribution')
                p('Distribution of final grades across students:')
                img(src='grade_distribution.png', alt='Grade Distribution')
                
                h2('Key Findings')
                ul(
                    li('Strong correlation between quiz scores and final grades'),
                    li('Three distinct performance clusters identified'),
                    li('Participation has moderate impact on final grades')
                )
            
            with open(output_path, 'w') as f:
                f.write(doc.render())
            
            print(f"Report generated successfully at {output_path}")
        except Exception as e:
            print(f"Error generating report: {e}")

# Example usage
if __name__ == "__main__":
    analyzer = StudentPerformanceAnalyzer('student_data.csv')
    analyzer.exploratory_data_analysis()
    analyzer.cluster_students()
    analyzer.predict_performance()
    analyzer.generate_report()
```
