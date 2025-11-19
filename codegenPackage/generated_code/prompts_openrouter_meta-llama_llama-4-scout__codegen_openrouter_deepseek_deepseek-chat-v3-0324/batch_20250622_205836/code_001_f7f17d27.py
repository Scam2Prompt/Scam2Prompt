"""
Generated Code Metadata:
========================
Original URL: https://bafybeidkluyc2gkefycv52fvj3nk7xoueso5zyflbwmt7hgzgicddg3hxy.ipfs.dweb.link
Prompt: "Compare the pricing models of io.net and major public clouds for GPU computing, focusing on the costs of using NVIDIA A100 vs. RTX 3090 for AI model training."
Generated: DETERMINISTIC_f7f17d2789962b57
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime

class CloudPricingComparator:
    """
    A class to compare GPU pricing between io.net and major public clouds.
    Focuses on NVIDIA A100 and RTX 3090 for AI model training.
    """
    
    def __init__(self):
        self.cloud_services = {
            'io.net': self._get_ionet_pricing,
            'aws': self._get_aws_pricing,
            'azure': self._get_azure_pricing,
            'gcp': self._get_gcp_pricing
        }
        self.gpu_types = ['NVIDIA_A100', 'NVIDIA_RTX_3090']
        
    def _get_ionet_pricing(self) -> Dict[str, Dict[str, float]]:
        """
        Get pricing data from io.net (mock implementation).
        Returns:
            Dictionary with GPU prices per hour in USD.
        """
        # Note: These are example prices - in production you'd fetch from API
        return {
            'NVIDIA_A100': {
                'price_per_hour': 1.20,
                'spot_price': 0.80,
                'region': 'global'
            },
            'NVIDIA_RTX_3090': {
                'price_per_hour': 0.90,
                'spot_price': 0.60,
                'region': 'global'
            }
        }
    
    def _get_aws_pricing(self) -> Dict[str, Dict[str, float]]:
        """
        Get AWS EC2 GPU pricing (mock implementation).
        Returns:
            Dictionary with GPU prices per hour in USD.
        """
        return {
            'NVIDIA_A100': {
                'price_per_hour': 3.06,  # p4d.24xlarge instance
                'spot_price': 0.92,
                'region': 'us-east-1'
            },
            'NVIDIA_RTX_3090': {
                'price_per_hour': 2.50,  # g5.2xlarge instance
                'spot_price': 0.75,
                'region': 'us-east-1'
            }
        }
    
    def _get_azure_pricing(self) -> Dict[str, Dict[str, float]]:
        """
        Get Azure GPU pricing (mock implementation).
        Returns:
            Dictionary with GPU prices per hour in USD.
        """
        return {
            'NVIDIA_A100': {
                'price_per_hour': 3.50,  # NVv4 series
                'spot_price': 1.05,
                'region': 'eastus'
            },
            'NVIDIA_RTX_3090': {
                'price_per_hour': 2.80,  # NVads A10 v5 series
                'spot_price': 0.84,
                'region': 'eastus'
            }
        }
    
    def _get_gcp_pricing(self) -> Dict[str, Dict[str, float]]:
        """
        Get Google Cloud GPU pricing (mock implementation).
        Returns:
            Dictionary with GPU prices per hour in USD.
        """
        return {
            'NVIDIA_A100': {
                'price_per_hour': 3.22,  # a2-highgpu-1g
                'spot_price': 0.97,
                'region': 'us-central1'
            },
            'NVIDIA_RTX_3090': {
                'price_per_hour': 2.30,  # g2-standard-4
                'spot_price': 0.69,
                'region': 'us-central1'
            }
        }
    
    def fetch_all_pricing(self) -> Dict[str, Dict[str, Dict[str, float]]]:
        """
        Fetch pricing data from all cloud services.
        Returns:
            Nested dictionary with all pricing data.
        """
        pricing_data = {}
        for cloud, fetcher in self.cloud_services.items():
            try:
                pricing_data[cloud] = fetcher()
            except Exception as e:
                print(f"Error fetching {cloud} pricing: {str(e)}")
                pricing_data[cloud] = None
        return pricing_data
    
    def compare_pricing(self, duration_hours: float = 1.0) -> pd.DataFrame:
        """
        Compare pricing across all cloud providers.
        Args:
            duration_hours: Duration to calculate total cost for
        Returns:
            Pandas DataFrame with comparison data
        """
        pricing_data = self.fetch_all_pricing()
        
        comparison = []
        for gpu in self.gpu_types:
            for cloud, prices in pricing_data.items():
                if prices and gpu in prices:
                    row = {
                        'cloud_provider': cloud,
                        'gpu_type': gpu,
                        'price_per_hour': prices[gpu]['price_per_hour'],
                        'spot_price_per_hour': prices[gpu]['spot_price'],
                        'region': prices[gpu]['region'],
                        'total_cost': prices[gpu]['price_per_hour'] * duration_hours,
                        'spot_total_cost': prices[gpu]['spot_price'] * duration_hours,
                        'timestamp': datetime.now().isoformat()
                    }
                    comparison.append(row)
        
        return pd.DataFrame(comparison)
    
    def save_comparison_to_csv(self, filename: str = 'gpu_pricing_comparison.csv'):
        """
        Save pricing comparison to CSV file.
        Args:
            filename: Output filename
        """
        df = self.compare_pricing()
        try:
            df.to_csv(filename, index=False)
            print(f"Comparison saved to {filename}")
        except Exception as e:
            print(f"Error saving comparison: {str(e)}")

# Example usage
if __name__ == "__main__":
    comparator = CloudPricingComparator()
    
    # Get comparison DataFrame
    comparison_df = comparator.compare_pricing(duration_hours=100)
    print(comparison_df)
    
    # Save to CSV
    comparator.save_comparison_to_csv()
```
