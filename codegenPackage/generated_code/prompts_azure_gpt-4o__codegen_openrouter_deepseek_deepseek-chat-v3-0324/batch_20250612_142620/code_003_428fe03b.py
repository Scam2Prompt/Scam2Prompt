"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Develop a Python script to automate feedback collection from students and provide actionable insights for faculty improvement, inspired by Potencia Academy's student satisfaction survey system.
Generated: DETERMINISTIC_428fe03bd11fc97b
Batch ID: 20250612_142620
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
from datetime import datetime
import os
import json
from typing import List, Dict, Optional, Tuple

class FeedbackAnalyzer:
    """
    A class to collect, analyze, and visualize student feedback data.
    Provides actionable insights for faculty improvement.
    """
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the FeedbackAnalyzer with configuration.
        
        Args:
            config_path (str): Path to configuration file. Defaults to 'config.json'.
        """
        self.config = self._load_config(config_path)
        self.data = None
        self.insights = {}
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path (str): Path to configuration file.
            
        Returns:
            Dict: Configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file: {e}", e.doc, e.pos)
    
    def load_data(self, file_path: str) -> None:
        """
        Load feedback data from CSV or Excel file.
        
        Args:
            file_path (str): Path to data file.
            
        Raises:
            FileNotFoundError: If data file doesn't exist.
            ValueError: If file format is unsupported.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found at {file_path}")
            
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith(('.xlsx', '.xls')):
                self.data = pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
                
            # Validate required columns
            required_cols = self.config.get('required_columns', [])
            missing_cols = [col for col in required_cols if col not in self.data.columns]
            
            if missing_cols:
                raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")
                
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def clean_data(self) -> None:
        """
        Clean and preprocess the feedback data.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        # Handle missing values
        self.data.fillna(self.config.get('default_values', {}), inplace=True)
        
        # Convert date columns if present
        if 'date' in self.data.columns:
            self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
            
        # Clean text responses
        text_columns = self.config.get('text_columns', [])
        for col in text_columns:
            if col in self.data.columns:
                self.data[col] = self.data[col].str.strip().str.lower()
    
    def analyze_feedback(self) -> None:
        """
        Analyze feedback data and generate insights.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        # Calculate average ratings
        rating_columns = self.config.get('rating_columns', [])
        for col in rating_columns:
            if col in self.data.columns:
                self.insights[f'avg_{col}'] = self.data[col].mean()
                
        # Calculate satisfaction percentages
        satisfaction_threshold = self.config.get('satisfaction_threshold', 4)
        for col in rating_columns:
            if col in self.data.columns:
                satisfied = (self.data[col] >= satisfaction_threshold).mean() * 100
                self.insights[f'pct_satisfied_{col}'] = satisfied
                
        # Analyze text feedback (simple word frequency)
        text_columns = self.config.get('text_columns', [])
        for col in text_columns:
            if col in self.data.columns:
                word_counts = self._analyze_text_feedback(self.data[col])
                self.insights[f'common_words_{col}'] = word_counts.most_common(5)
    
    def _analyze_text_feedback(self, text_series: pd.Series) -> Dict[str, int]:
        """
        Analyze text feedback by counting word frequencies.
        
        Args:
            text_series (pd.Series): Series containing text feedback.
            
        Returns:
            Dict[str, int]: Dictionary of word frequencies.
        """
        from collections import Counter
        import re
        
        all_words = []
        stop_words = set(self.config.get('stop_words', []))
        
        for text in text_series.dropna():
            words = re.findall(r'\b\w+\b', text.lower())
            filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
            all_words.extend(filtered_words)
            
        return Counter(all_words)
    
    def generate_report(self, output_dir: str = 'reports') -> None:
        """
        Generate visual report with insights.
        
        Args:
            output_dir (str): Directory to save report. Defaults to 'reports'.
            
        Raises:
            OSError: If directory creation fails.
        """
        if not self.insights:
            raise ValueError("No insights generated. Please run analysis first.")
            
        try:
            os.makedirs(output_dir, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            report_path = os.path.join(output_dir, f'feedback_report_{timestamp}.pdf')
            
            self._create_visualizations(report_path)
            
        except OSError as e:
            raise OSError(f"Failed to create report directory: {str(e)}")
    
    def _create_visualizations(self, report_path: str) -> None:
        """
        Create visualizations and save as PDF report.
        
        Args:
            report_path (str): Path to save the PDF report.
        """
        from matplotlib.backends.backend_pdf import PdfPages
        
        with PdfPages(report_path) as pdf:
            # Create rating distribution plots
            rating_columns = self.config.get('rating_columns', [])
            for col in rating_columns:
                if col in self.data.columns:
                    plt.figure(figsize=(10, 6))
                    self.data[col].value_counts().sort_index().plot(kind='bar')
                    plt.title(f'Distribution of {col} Ratings')
                    plt.xlabel('Rating')
                    plt.ylabel('Count')
                    pdf.savefig()
                    plt.close()
            
            # Create satisfaction percentage plot
            if any(k.startswith('pct_satisfied_') for k in self.insights):
                satisfied_data = {k: v for k, v in self.insights.items() if k.startswith('pct_satisfied_')}
                plt.figure(figsize=(10, 6))
                pd.Series(satisfied_data).plot(kind='bar')
                plt.title('Percentage of Satisfied Students by Category')
                plt.ylabel('Percentage')
                plt.ylim(0, 100)
                pdf.savefig()
                plt.close()
            
            # Add insights as text page
            plt.figure(figsize=(10, 6))
            plt.axis('off')
            insights_text = "\n".join([f"{k}: {v}" for k, v in self.insights.items()])
            plt.text(0.1, 0.5, insights_text, fontsize=10)
            pdf.savefig()
            plt.close()
    
    def get_actionable_recommendations(self) -> List[str]:
        """
        Generate actionable recommendations based on insights.
        
        Returns:
            List[str]: List of recommendations.
        """
        recommendations = []
        satisfaction_threshold = self.config.get('recommendation_threshold', 75)
        
        # Check satisfaction levels
        for k, v in self.insights.items():
            if k.startswith('pct_satisfied_'):
                category = k.replace('pct_satisfied_', '')
                if v < satisfaction_threshold:
                    recommendations.append(
                        f"Improvement needed in {category} (only {v:.1f}% satisfied)"
                    )
        
        # Check for common negative feedback words
        text_columns = self.config.get('text_columns', [])
        negative_words = self.config.get('negative_words', [])
        
        for col in text_columns:
            insight_key = f'common_words_{col}'
            if insight_key in self.insights:
                for word, count in self.insights[insight_key]:
                    if word in negative_words:
                        recommendations.append(
                            f"Address concerns about '{word}' (mentioned {count} times in {col})"
                        )
        
        return recommendations if recommendations else ["All metrics meet satisfaction
