"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write a Python script to analyze the energy consumption of AI models at scale, inspired by Finance StarGate's exploration of AI's energy appetite.
Generated: DETERMINISTIC_9363b64dc3843866
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy import stats

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class ModelEnergyConsumption:
    """Data class to store energy consumption metrics for an AI model."""
    model_name: str
    training_energy_kwh: float
    inference_energy_kwh: float
    carbon_footprint_kg: float
    hardware_used: str
    timestamp: str


class AIEnergyAnalyzer:
    """Analyzes energy consumption of AI models at scale."""
    
    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path: Path to JSON file containing energy consumption data.
                      If None, starts with empty dataset.
        """
        self.data: List[ModelEnergyConsumption] = []
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, file_path: str) -> None:
        """
        Load energy consumption data from JSON file.
        
        Args:
            file_path: Path to JSON file containing energy data.
            
        Raises:
            FileNotFoundError: If file doesn't exist.
            json.JSONDecodeError: If file contains invalid JSON.
            KeyError: If required fields are missing in the data.
        """
        try:
            with open(file_path, 'r') as f:
                raw_data = json.load(f)
            
            for item in raw_data:
                if not all(key in item for key in ['model_name', 'training_energy_kwh', 
                                                 'inference_energy_kwh', 'carbon_footprint_kg',
                                                 'hardware_used', 'timestamp']):
                    raise KeyError("Missing required fields in JSON data")
                
                self.data.append(ModelEnergyConsumption(
                    model_name=item['model_name'],
                    training_energy_kwh=float(item['training_energy_kwh']),
                    inference_energy_kwh=float(item['inference_energy_kwh']),
                    carbon_footprint_kg=float(item['carbon_footprint_kg']),
                    hardware_used=item['hardware_used'],
                    timestamp=item['timestamp']
                ))
            logger.info(f"Successfully loaded data from {file_path}")
            
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file: {file_path}")
            raise
        except KeyError as e:
            logger.error(f"Missing required field in data: {e}")
            raise
        except ValueError as e:
            logger.error(f"Invalid data format: {e}")
            raise
    
    def add_data_point(self, model_data: ModelEnergyConsumption) -> None:
        """Add a single data point to the analyzer."""
        self.data.append(model_data)
    
    def export_data(self, file_path: str) -> None:
        """
        Export current data to JSON file.
        
        Args:
            file_path: Path to save the JSON file.
            
        Raises:
            IOError: If file cannot be written.
        """
        try:
            export_data = [{
                'model_name': item.model_name,
                'training_energy_kwh': item.training_energy_kwh,
                'inference_energy_kwh': item.inference_energy_kwh,
                'carbon_footprint_kg': item.carbon_footprint_kg,
                'hardware_used': item.hardware_used,
                'timestamp': item.timestamp
            } for item in self.data]
            
            with open(file_path, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            logger.info(f"Successfully exported data to {file_path}")
        except IOError as e:
            logger.error(f"Failed to write to file {file_path}: {e}")
            raise
    
    def get_summary_statistics(self) -> Dict:
        """Calculate summary statistics for the dataset."""
        if not self.data:
            logger.warning("No data available for summary statistics")
            return {}
        
        training_energy = [d.training_energy_kwh for d in self.data]
        inference_energy = [d.inference_energy_kwh for d in self.data]
        carbon_footprint = [d.carbon_footprint_kg for d in self.data]
        
        return {
            'training_energy': {
                'mean': np.mean(training_energy),
                'median': np.median(training_energy),
                'std_dev': np.std(training_energy),
                'min': np.min(training_energy),
                'max': np.max(training_energy)
            },
            'inference_energy': {
                'mean': np.mean(inference_energy),
                'median': np.median(inference_energy),
                'std_dev': np.std(inference_energy),
                'min': np.min(inference_energy),
                'max': np.max(inference_energy)
            },
            'carbon_footprint': {
                'mean': np.mean(carbon_footprint),
                'median': np.median(carbon_footprint),
                'std_dev': np.std(carbon_footprint),
                'min': np.min(carbon_footprint),
                'max': np.max(carbon_footprint)
            }
        }
    
    def compare_models(self, model1: str, model2: str) -> Dict:
        """
        Compare energy consumption between two models.
        
        Args:
            model1: Name of first model to compare.
            model2: Name of second model to compare.
            
        Returns:
            Dictionary with comparison results including statistical tests.
            
        Raises:
            ValueError: If either model is not found in the dataset.
        """
        model1_data = [d for d in self.data if d.model_name == model1]
        model2_data = [d for d in self.data if d.model_name == model2]
        
        if not model1_data or not model2_data:
            missing = model1 if not model1_data else model2
            logger.error(f"Model not found in dataset: {missing}")
            raise ValueError(f"Model not found: {missing}")
        
        model1_training = [d.training_energy_kwh for d in model1_data]
        model2_training = [d.training_energy_kwh for d in model2_data]
        
        model1_inference = [d.inference_energy_kwh for d in model1_data]
        model2_inference = [d.inference_energy_kwh for d in model2_data]
        
        # Perform t-tests
        t_train, p_train = stats.ttest_ind(model1_training, model2_training)
        t_inf, p_inf = stats.ttest_ind(model1_inference, model2_inference)
        
        return {
            'training_comparison': {
                'model1_mean': np.mean(model1_training),
                'model2_mean': np.mean(model2_training),
                't_statistic': t_train,
                'p_value': p_train,
                'significant_diff': p_train < 0.05
            },
            'inference_comparison': {
                'model1_mean': np.mean(model1_inference),
                'model2_mean': np.mean(model2_inference),
                't_statistic': t_inf,
                'p_value': p_inf,
                'significant_diff': p_inf < 0.05
            }
        }
    
    def analyze_hardware_efficiency(self) -> pd.DataFrame:
        """
        Analyze energy efficiency by hardware type.
        
        Returns:
            Pandas DataFrame with efficiency metrics grouped by hardware.
        """
        if not self.data:
            logger.warning("No data available for hardware analysis")
            return pd.DataFrame()
        
        df = pd.DataFrame([{
            'hardware': d.hardware_used,
            'training_energy': d.training_energy_kwh,
            'inference_energy': d.inference_energy_kwh,
            'carbon_footprint': d.carbon_footprint_kg
        } for d in self.data])
        
        return df.groupby('hardware').agg({
            'training_energy': ['mean', 'median', 'std', 'count'],
            'inference_energy': ['mean', 'median', 'std'],
            'carbon_footprint': ['mean', 'median', 'std']
        }).reset_index()
    
    def generate_report(self, output_dir: str = "reports") -> str:
        """
        Generate a comprehensive report with analysis results.
        
        Args:
            output_dir: Directory to save the report.
            
        Returns:
            Path to the generated report file.
            
        Raises:
            IOError: If report cannot be generated.
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%
