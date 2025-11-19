"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Develop a Python program to analyze the impact of AIDA's projects, such as "Quality Education" and "Health and Nutrition", by calculating statistics and visualizing data.
Generated: DETERMINISTIC_93eccf3b718e5566
Batch ID: 20250622_210655
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
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AIDAAnalyzer:
    """
    A class to analyze and visualize AIDA project impact data.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from the given path.
        
        Args:
            data_path (str): Path to the CSV file containing project data
        """
        self.data_path = data_path
        self.data = None
        self.projects = None
        
    def load_data(self) -> None:
        """
        Load and preprocess the project data.
        
        Raises:
            FileNotFoundError: If the data file is not found
            ValueError: If the data is malformed
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully")
            
            # Basic data validation
            required_columns = ['project_name', 'year', 'impact_score', 'beneficiaries', 'location']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError("Missing required columns in the data")
                
            # Clean data
            self.data = self.data.dropna()
            self.data['impact_score'] = pd.to_numeric(self.data['impact_score'], errors='coerce')
            self.data['beneficiaries'] = pd.to_numeric(self.data['beneficiaries'], errors='coerce')
            self.data = self.data.dropna(subset=['impact_score', 'beneficiaries'])
            
            self.projects = self.data['project_name'].unique()
            logger.info(f"Found {len(self.projects)} unique projects")
            
        except FileNotFoundError:
            logger.error(f"Data file not found at {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Data loading failed: {str(e)}")
    
    def calculate_project_stats(self, project_name: str) -> Dict[str, float]:
        """
        Calculate statistics for a specific project.
        
        Args:
            project_name (str): Name of the project to analyze
            
        Returns:
            Dict[str, float]: Dictionary containing calculated statistics
            
        Raises:
            ValueError: If project name is not found in data
        """
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found in data")
            
        project_data = self.data[self.data['project_name'] == project_name]
        
        stats = {
            'total_beneficiaries': project_data['beneficiaries'].sum(),
            'average_impact': project_data['impact_score'].mean(),
            'max_impact': project_data['impact_score'].max(),
            'min_impact': project_data['impact_score'].min(),
            'yearly_growth': self._calculate_yearly_growth(project_data)
        }
        
        logger.info(f"Calculated stats for project {project_name}")
        return stats
    
    def _calculate_yearly_growth(self, project_data: pd.DataFrame) -> float:
        """
        Calculate yearly growth rate of beneficiaries.
        
        Args:
            project_data (pd.DataFrame): Filtered data for a specific project
            
        Returns:
            float: Yearly growth rate percentage
        """
        if len(project_data) < 2:
            return 0.0
            
        years = sorted(project_data['year'].unique())
        beneficiaries = [project_data[project_data['year'] == y]['beneficiaries'].sum() for y in years]
        
        if len(beneficiaries) < 2:
            return 0.0
            
        growth_rates = []
        for i in range(1, len(beneficiaries)):
            if beneficiaries[i-1] == 0:
                continue
            growth_rate = (beneficiaries[i] - beneficiaries[i-1]) / beneficiaries[i-1] * 100
            growth_rates.append(growth_rate)
            
        return np.mean(growth_rates) if growth_rates else 0.0
    
    def visualize_project_impact(self, project_name: str, save_path: Optional[str] = None) -> None:
        """
        Create visualizations for a project's impact.
        
        Args:
            project_name (str): Name of the project to visualize
            save_path (Optional[str]): Path to save the visualization (if None, shows plot)
            
        Raises:
            ValueError: If project name is not found in data
        """
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found in data")
            
        project_data = self.data[self.data['project_name'] == project_name]
        
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Impact score over time
        plt.subplot(2, 2, 1)
        sns.lineplot(data=project_data, x='year', y='impact_score', marker='o')
        plt.title(f'Impact Score Trend for {project_name}')
        plt.xlabel('Year')
        plt.ylabel('Impact Score')
        
        # Plot 2: Beneficiaries over time
        plt.subplot(2, 2, 2)
        sns.barplot(data=project_data, x='year', y='beneficiaries')
        plt.title(f'Beneficiaries for {project_name}')
        plt.xlabel('Year')
        plt.ylabel('Number of Beneficiaries')
        
        # Plot 3: Impact vs Beneficiaries
        plt.subplot(2, 2, 3)
        sns.scatterplot(data=project_data, x='beneficiaries', y='impact_score', hue='location')
        plt.title(f'Impact vs Beneficiaries for {project_name}')
        plt.xlabel('Number of Beneficiaries')
        plt.ylabel('Impact Score')
        
        # Plot 4: Location distribution
        plt.subplot(2, 2, 4)
        location_counts = project_data['location'].value_counts()
        plt.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%')
        plt.title(f'Location Distribution for {project_name}')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            logger.info(f"Visualization saved to {save_path}")
        else:
            plt.show()
    
    def compare_projects(self, project_names: List[str], save_path: Optional[str] = None) -> None:
        """
        Compare multiple projects using visualizations.
        
        Args:
            project_names (List[str]): List of project names to compare
            save_path (Optional[str]): Path to save the visualization (if None, shows plot)
            
        Raises:
            ValueError: If any project name is not found in data
        """
        for name in project_names:
            if name not in self.projects:
                raise ValueError(f"Project '{name}' not found in data")
                
        comparison_data = self.data[self.data['project_name'].isin(project_names)]
        
        plt.figure(figsize=(15, 8))
        
        # Plot 1: Impact score comparison
        plt.subplot(1, 2, 1)
        sns.boxplot(data=comparison_data, x='project_name', y='impact_score')
        plt.title('Impact Score Comparison')
        plt.xlabel('Project')
        plt.ylabel('Impact Score')
        plt.xticks(rotation=45)
        
        # Plot 2: Beneficiaries comparison
        plt.subplot(1, 2, 2)
        beneficiaries = comparison_data.groupby('project_name')['beneficiaries'].sum().reset_index()
        sns.barplot(data=beneficiaries, x='project_name', y='beneficiaries')
        plt.title('Total Beneficiaries Comparison')
        plt.xlabel('Project')
        plt.ylabel('Total Beneficiaries')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            logger.info(f"Comparison visualization saved to {save_path}")
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    try:
        analyzer = AIDAAnalyzer("aida_projects.csv")
        analyzer.load_data()
        
        # Analyze Quality Education project
        quality_edu_stats = analyzer.calculate_project_stats("Quality Education")
        print("Quality Education Stats:", quality_edu_stats)
        analyzer.visualize_project_impact("Quality Education", "quality_education_impact.png")
        
        # Analyze Health and Nutrition project
        health_stats = analyzer.calculate_project_stats("Health and Nutrition")
        print("Health and Nutrition Stats:", health_stats)
        analyzer.visualize_project_impact("Health and Nutrition", "health_nutrition_impact.png")
        
        # Compare projects
        analyzer.compare_projects(["Quality Education", "Health and Nutrition"], "project_comparison.png")
        
    except Exception as e:
        logger.error(f"Error in analysis
