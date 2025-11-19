"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Create a digital marketing campaign script using Python, incorporating strategies from PDMA's Digital Marketing Professional program, such as audience segmentation and A/B testing.
Generated: DETERMINISTIC_ef63ca24e142c71c
Batch ID: 20250612_145730
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
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import random
import logging
from typing import Dict, List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DigitalMarketingCampaign:
    """
    A digital marketing campaign manager implementing PDMA strategies including:
    - Audience segmentation
    - A/B testing
    - Campaign performance analysis
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the campaign with customer data.
        
        Args:
            data_path: Path to CSV file containing customer data
        """
        try:
            self.df = pd.read_csv(data_path)
            logger.info(f"Successfully loaded data from {data_path}")
            self._clean_data()
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _clean_data(self) -> None:
        """Clean and preprocess the customer data."""
        # Handle missing values
        self.df.fillna({
            'age': self.df['age'].median(),
            'income': self.df['income'].median(),
            'purchase_history': 0
        }, inplace=True)
        
        # Convert categorical variables
        self.df = pd.get_dummies(self.df, columns=['gender', 'location'])
        
        logger.info("Data cleaning completed")
    
    def segment_audience(self, n_clusters: int = 4) -> Dict[int, pd.DataFrame]:
        """
        Segment audience using K-means clustering.
        
        Args:
            n_clusters: Number of segments to create
            
        Returns:
            Dictionary mapping segment IDs to customer DataFrames
        """
        try:
            # Select features for segmentation
            features = ['age', 'income', 'purchase_history', 'time_on_site']
            X = self.df[features]
            
            # Standardize features
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            
            # Perform clustering
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            self.df['segment'] = kmeans.fit_predict(X_scaled)
            
            # Create segment dictionary
            segments = {
                i: self.df[self.df['segment'] == i]
                for i in range(n_clusters)
            }
            
            logger.info(f"Successfully created {n_clusters} audience segments")
            return segments
        except Exception as e:
            logger.error(f"Error in audience segmentation: {str(e)}")
            raise
    
    def design_ab_test(
        self,
        segments: Dict[int, pd.DataFrame],
        test_variants: List[str],
        test_size: float = 0.3
    ) -> Dict[str, Dict[int, pd.DataFrame]]:
        """
        Design an A/B test by splitting segments into control and test groups.
        
        Args:
            segments: Audience segments dictionary
            test_variants: List of test variant names
            test_size: Proportion of audience to include in test
            
        Returns:
            Dictionary containing control and test groups for each variant
        """
        try:
            ab_groups = {'control': {}, 'test': {}}
            
            for seg_id, seg_df in segments.items():
                # Split segment into control and test
                control, test = train_test_split(
                    seg_df,
                    test_size=test_size,
                    random_state=42
                )
                
                # Assign variants randomly to test group
                test['variant'] = np.random.choice(
                    test_variants,
                    size=len(test)
                )
                
                ab_groups['control'][seg_id] = control
                ab_groups['test'][seg_id] = test
                
            logger.info("A/B test design completed")
            return ab_groups
        except Exception as e:
            logger.error(f"Error designing A/B test: {str(e)}")
            raise
    
    def run_campaign(
        self,
        ab_groups: Dict[str, Dict[int, pd.DataFrame]],
        campaign_message: str,
        variant_messages: Dict[str, str]
    ) -> Dict[str, Dict[int, pd.DataFrame]]:
        """
        Simulate running a marketing campaign with A/B testing.
        
        Args:
            ab_groups: A/B test groups from design_ab_test
            campaign_message: Message for control group
            variant_messages: Messages for each test variant
            
        Returns:
            Updated groups with campaign results
        """
        try:
            results = {'control': {}, 'test': {}}
            
            # Process control group
            for seg_id, control_df in ab_groups['control'].items():
                control_df['message'] = campaign_message
                control_df['response'] = self._simulate_response(control_df)
                results['control'][seg_id] = control_df
            
            # Process test group
            for seg_id, test_df in ab_groups['test'].items():
                test_df['message'] = test_df['variant'].map(variant_messages)
                test_df['response'] = self._simulate_response(test_df)
                results['test'][seg_id] = test_df
            
            logger.info("Campaign execution completed")
            return results
        except Exception as e:
            logger.error(f"Error running campaign: {str(e)}")
            raise
    
    def _simulate_response(self, df: pd.DataFrame) -> pd.Series:
        """
        Simulate customer response to campaign (for demonstration).
        
        Args:
            df: Customer DataFrame
            
        Returns:
            Series of response rates (0-1)
        """
        # Base response rate based on customer features
        base_rate = (
            0.1 * (df['age'] / 100) +
            0.3 * (df['income'] / df['income'].max()) +
            0.2 * (df['purchase_history'] / df['purchase_history'].max()) +
            0.4 * (df['time_on_site'] / df['time_on_site'].max())
        )
        
        # Add random noise
        noise = np.random.normal(0, 0.05, len(df))
        response = np.clip(base_rate + noise, 0, 1)
        
        return pd.Series(response, index=df.index)
    
    def analyze_results(
        self,
        campaign_results: Dict[str, Dict[int, pd.DataFrame]]
    ) -> Dict[str, Dict[str, float]]:
        """
        Analyze campaign results with statistical significance testing.
        
        Args:
            campaign_results: Output from run_campaign
            
        Returns:
            Dictionary of analysis results including response rates and p-values
        """
        try:
            analysis = {}
            
            # Aggregate control group results
            control_responses = pd.concat([
                df['response'] for seg_dict in campaign_results['control'].values()
                for df in [seg_dict]
            ])
            
            # Analyze each test variant
            for variant in campaign_results['test'][0]['variant'].unique():
                # Get responses for this variant
                variant_responses = pd.concat([
                    df[df['variant'] == variant]['response']
                    for seg_dict in campaign_results['test'].values()
                    for df in [seg_dict]
                ])
                
                # Calculate response rates
                control_rate = control_responses.mean()
                variant_rate = variant_responses.mean()
                
                # Perform t-test
                t_test = sm.stats.ttest_ind(
                    control_responses,
                    variant_responses
                )
                
                analysis[variant] = {
                    'control_response_rate': control_rate,
                    'variant_response_rate': variant_rate,
                    'lift': (variant_rate - control_rate) / control_rate,
                    'p_value': t_test[1]
                }
            
            logger.info("Campaign analysis completed")
            return analysis
        except Exception as e:
            logger.error(f"Error analyzing results: {str(e)}")
            raise
    
    def visualize_results(
        self,
        campaign_results: Dict[str, Dict[int, pd.DataFrame]],
        analysis_results: Dict[str, Dict[str, float]]
    ) -> None:
        """
        Visualize campaign results with plots.
        
        Args:
            campaign_results: Output from run_campaign
            analysis_results: Output from analyze_results
        """
        try:
            plt.figure(figsize=(15, 10))
            
            # Plot 1: Response rates by segment
            plt.subplot(2, 2, 1)
            segment_rates = []
            for seg_id in campaign_results['control']:
                control_rate = campaign_results['control'][seg_id]['response'].mean()
                test_rate = campaign_results['test'][seg_id]['response'].mean()
                segment_rates.append({'segment': seg_id, 'control': control_rate, 'test': test_rate})
            
            segment_df = pd.DataFrame(segment_rates)
            segment_df.plot(x='segment', y=['control', 'test'], kind='bar', ax=plt.gca())
            plt.title('Response Rates by Segment')
            plt.ylabel('
