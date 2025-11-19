"""
Generated Code Metadata:
========================
Original URL: https://futureforai.com
Prompt: Write Python code to benchmark the performance of DeepSeek R1 against GPT-4 using publicly available datasets, considering the computational resource differences mentioned on the Future For AI website.
Generated: DETERMINISTIC_3cd51f5d1cda18f6
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.deepseek.com/v1/chat/completions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import time
import json
import openai
import requests
from typing import Dict, List, Tuple, Optional
import numpy as np
import pandas as pd
from datasets import load_dataset
from tqdm import tqdm
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('benchmark.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATASET_NAMES = ["lambada", "hellaswag", "truthfulqa"]
MAX_SAMPLES = 100  # Limit samples per dataset for benchmarking
TIMEOUT = 30  # seconds

class BenchmarkRunner:
    def __init__(self):
        self.results = []
        self.datasets = {}
        
    def load_datasets(self) -> None:
        """Load benchmark datasets from HuggingFace."""
        logger.info("Loading datasets...")
        for name in DATASET_NAMES:
            try:
                dataset = load_dataset(name, split='validation')
                if len(dataset) > MAX_SAMPLES:
                    dataset = dataset.select(range(MAX_SAMPLES))
                self.datasets[name] = dataset
                logger.info(f"Loaded {len(dataset)} samples from {name}")
            except Exception as e:
                logger.error(f"Error loading dataset {name}: {str(e)}")
    
    def query_deepseek(self, prompt: str) -> Tuple[Optional[str], float]:
        """Query DeepSeek R1 API."""
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-r1",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 100
        }
        
        try:
            start_time = time.time()
            response = requests.post(
                DEEPSEEK_API_URL,
                headers=headers,
                json=payload,
                timeout=TIMEOUT
            )
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"], response_time
            else:
                logger.error(f"DeepSeek API error: {response.status_code} - {response.text}")
                return None, response_time
        except Exception as e:
            logger.error(f"DeepSeek query failed: {str(e)}")
            return None, 0.0
    
    def query_gpt4(self, prompt: str) -> Tuple[Optional[str], float]:
        """Query OpenAI GPT-4 API."""
        openai.api_key = OPENAI_API_KEY
        
        try:
            start_time = time.time()
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=100
            )
            response_time = time.time() - start_time
            return response.choices[0].message.content, response_time
        except Exception as e:
            logger.error(f"GPT-4 query failed: {str(e)}")
            return None, 0.0
    
    def evaluate_response(self, model_response: str, reference: str, dataset_name: str) -> float:
        """Simple evaluation metric (can be replaced with dataset-specific metrics)."""
        if dataset_name == "lambada":
            # For LAMBADA, check if the response completes the sentence
            return float(reference.strip().lower() in model_response.strip().lower())
        elif dataset_name == "hellaswag":
            # For HellaSwag, check if the correct continuation is chosen
            return float(reference.strip().lower() == model_response.strip().lower())
        elif dataset_name == "truthfulqa":
            # For TruthfulQA, check if the answer is truthful (simplified)
            return float("yes" in model_response.strip().lower() or "true" in model_response.strip().lower())
        return 0.0
    
    def run_benchmark(self) -> None:
        """Run benchmark across all datasets for both models."""
        if not self.datasets:
            self.load_datasets()
        
        for dataset_name, dataset in self.datasets.items():
            logger.info(f"Running benchmark on {dataset_name} dataset...")
            
            for i, sample in tqdm(enumerate(dataset), total=len(dataset)):
                try:
                    # Get prompt and reference answer based on dataset
                    if dataset_name == "lambada":
                        prompt = sample['text'].rsplit(' ', 1)[0]
                        reference = sample['text'].rsplit(' ', 1)[1]
                    elif dataset_name == "hellaswag":
                        prompt = sample['ctx']
                        reference = sample['endings'][sample['label']]
                    elif dataset_name == "truthfulqa":
                        prompt = sample['question']
                        reference = "true"  # Simplified for benchmarking
                    else:
                        continue
                    
                    # Query both models
                    deepseek_response, deepseek_time = self.query_deepseek(prompt)
                    gpt4_response, gpt4_time = self.query_gpt4(prompt)
                    
                    # Evaluate responses
                    deepseek_score = 0.0
                    gpt4_score = 0.0
                    
                    if deepseek_response:
                        deepseek_score = self.evaluate_response(
                            deepseek_response, reference, dataset_name
                        )
                    
                    if gpt4_response:
                        gpt4_score = self.evaluate_response(
                            gpt4_response, reference, dataset_name
                        )
                    
                    # Store results
                    self.results.append({
                        "dataset": dataset_name,
                        "sample_id": i,
                        "model": "DeepSeek-R1",
                        "response_time": deepseek_time,
                        "score": deepseek_score,
                        "response": deepseek_response
                    })
                    
                    self.results.append({
                        "dataset": dataset_name,
                        "sample_id": i,
                        "model": "GPT-4",
                        "response_time": gpt4_time,
                        "score": gpt4_score,
                        "response": gpt4_response
                    })
                    
                except Exception as e:
                    logger.error(f"Error processing sample {i} in {dataset_name}: {str(e)}")
    
    def analyze_results(self) -> Dict[str, Dict[str, float]]:
        """Analyze and aggregate benchmark results."""
        if not self.results:
            return {}
        
        df = pd.DataFrame(self.results)
        analysis = {}
        
        for dataset in DATASET_NAMES:
            dataset_results = df[df['dataset'] == dataset]
            if dataset_results.empty:
                continue
            
            analysis[dataset] = {
                "DeepSeek-R1": {
                    "avg_score": dataset_results[dataset_results['model'] == 'DeepSeek-R1']['score'].mean(),
                    "avg_response_time": dataset_results[dataset_results['model'] == 'DeepSeek-R1']['response_time'].mean(),
                    "total_queries": len(dataset_results[dataset_results['model'] == 'DeepSeek-R1'])
                },
                "GPT-4": {
                    "avg_score": dataset_results[dataset_results['model'] == 'GPT-4']['score'].mean(),
                    "avg_response_time": dataset_results[dataset_results['model'] == 'GPT-4']['response_time'].mean(),
                    "total_queries": len(dataset_results[dataset_results['model'] == 'GPT-4'])
                }
            }
        
        return analysis
    
    def save_results(self, filename: str = "benchmark_results.json") -> None:
        """Save benchmark results to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "raw_results": self.results,
                    "analysis": self.analyze_results()
                }, f, indent=2)
            logger.info(f"Results saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")

if __name__ == "__main__":
    # Initialize and run benchmark
    benchmark = BenchmarkRunner()
    benchmark.run_benchmark()
    
    # Analyze and save results
    analysis = benchmark.analyze_results()
    for dataset, metrics in analysis.items():
        logger.info(f"\nDataset: {dataset}")
        for model, values in metrics.items():
            logger.info(f"{model}:")
            logger.info(f"  Average Score: {values['avg_score']:.2f}")
            logger.info(f"  Average Response Time: {values['avg_response_time']:.2f}s")
            logger.info(f"  Total Queries: {values['total_queries']}")
    
    benchmark.save_results()
```
