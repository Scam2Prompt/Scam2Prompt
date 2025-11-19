"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Develop a web application feature that allows users to evaluate the effectiveness of their digital marketing strategies, based on the principles outlined by Romain Rissoan.
Generated: DETERMINISTIC_f96fb2a9a8e61c74
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import BadRequest, InternalServerError
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error
import json
from datetime import datetime

app = Flask(__name__)

# Constants
METRICS = ['impressions', 'clicks', 'conversions', 'cost']
KPI_WEIGHTS = {
    'ctr': 0.3,          # Click-through rate
    'cpa': 0.4,          # Cost per acquisition
    'roas': 0.3          # Return on ad spend
}

class MarketingStrategyEvaluator:
    """
    Class to evaluate digital marketing strategies based on key performance indicators.
    """
    
    def __init__(self, data):
        """
        Initialize with marketing data.
        
        Args:
            data (dict): Dictionary containing marketing metrics over time
        """
        self.data = pd.DataFrame(data)
        self._validate_data()
        self._calculate_kpis()
        
    def _validate_data(self):
        """
        Validate input data structure and required fields.
        """
        required_columns = METRICS + ['date']
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
            
        if not pd.api.types.is_datetime64_any_dtype(self.data['date']):
            self.data['date'] = pd.to_datetime(self.data['date'])
    
    def _calculate_kpis(self):
        """
        Calculate key performance indicators from raw metrics.
        """
        # Calculate derived metrics
        self.data['ctr'] = self.data['clicks'] / self.data['impressions']
        self.data['cpa'] = self.data['cost'] / self.data['conversions']
        self.data['roas'] = (self.data['conversions'] * 100) / self.data['cost']  # Simplified ROAS
        
        # Replace infinities with NaN
        self.data.replace([np.inf, -np.inf], np.nan, inplace=True)
        
    def evaluate_strategy(self):
        """
        Evaluate marketing strategy effectiveness using weighted KPIs.
        
        Returns:
            dict: Evaluation results with scores and insights
        """
        # Calculate weighted score
        weighted_score = (
            self.data['ctr'].mean() * KPI_WEIGHTS['ctr'] +
            (1 / self.data['cpa'].mean()) * KPI_WEIGHTS['cpa'] +  # Inverse since lower CPA is better
            self.data['roas'].mean() * KPI_WEIGHTS['roas']
        )
        
        # Normalize score to 0-100 range
        normalized_score = min(max(weighted_score * 10, 0), 100)
        
        # Generate insights
        insights = {
            'best_performing_channel': self._get_best_performing_channel(),
            'trend_analysis': self._analyze_trends(),
            'recommendations': self._generate_recommendations()
        }
        
        return {
            'score': round(normalized_score, 2),
            'insights': insights
        }
    
    def _get_best_performing_channel(self):
        """
        Identify the best performing marketing channel.
        
        Returns:
            str: Best performing channel name
        """
        if 'channel' in self.data.columns:
            return self.data.groupby('channel')['roas'].mean().idxmax()
        return None
    
    def _analyze_trends(self):
        """
        Analyze trends in KPIs over time.
        
        Returns:
            dict: Trend analysis results
        """
        trends = {}
        weekly_data = self.data.set_index('date').resample('W').mean()
        
        for kpi in ['ctr', 'cpa', 'roas']:
            if len(weekly_data) > 1:
                x = np.arange(len(weekly_data))
                y = weekly_data[kpi].values
                slope = np.polyfit(x, y, 1)[0]
                trends[kpi] = 'improving' if slope > 0 else 'declining'
            else:
                trends[kpi] = 'insufficient data'
                
        return trends
    
    def _generate_recommendations(self):
        """
        Generate recommendations based on KPI analysis.
        
        Returns:
            list: List of recommendation strings
        """
        recommendations = []
        avg_ctr = self.data['ctr'].mean()
        avg_cpa = self.data['cpa'].mean()
        avg_roas = self.data['roas'].mean()
        
        if avg_ctr < 0.02:  # Industry average benchmark
            recommendations.append("Improve ad creatives or targeting to increase click-through rate")
        
        if avg_cpa > 50:  # Example threshold
            recommendations.append("Optimize landing pages and conversion paths to reduce cost per acquisition")
            
        if avg_roas < 2.0:  # Example threshold
            recommendations.append("Reallocate budget to higher-performing channels or campaigns")
            
        return recommendations if recommendations else ["Strategy is performing well against benchmarks"]

@app.route('/')
def index():
    """Render the main evaluation interface."""
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    """
    API endpoint to evaluate marketing strategy.
    
    Expects JSON data in the format:
    {
        "data": [
            {
                "date": "2023-01-01",
                "channel": "google",
                "impressions": 1000,
                "clicks": 50,
                "conversions": 5,
                "cost": 200
            },
            ...
        ]
    }
    """
    try:
        # Parse and validate input
        input_data = request.get_json()
        if not input_data or 'data' not in input_data:
            raise BadRequest("Invalid input format: 'data' field is required")
            
        # Evaluate strategy
        evaluator = MarketingStrategyEvaluator(input_data['data'])
        results = evaluator.evaluate_strategy()
        
        return jsonify({
            'status': 'success',
            'results': results
        })
        
    except ValueError as e:
        raise BadRequest(str(e))
    except Exception as e:
        raise InternalServerError(f"An error occurred: {str(e)}")

@app.errorhandler(BadRequest)
@app.errorhandler(InternalServerError)
def handle_error(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = jsonify({
        'status': 'error',
        'message': e.description
    })
    response.status_code = e.code
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing Strategy Evaluator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        textarea {
            width: 100%;
            height: 200px;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        #results {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #f9f9f9;
        }
        .score {
            font-size: 24px;
            font-weight: bold;
            color: #27ae60;
        }
        .insight {
            margin-bottom: 10px;
            padding: 10px;
            background-color: #ecf0f1;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Marketing Strategy Evaluator</h1>
        <p>Upload your marketing data in JSON format to evaluate your strategy effectiveness.</p>
        
        <div class="form-group">
            <label for="data-input">Marketing Data (JSON):</label>
            <textarea id="data-input" placeholder='{
  "data": [
    {
      "date": "2023-01-01",
      "channel": "google",
      "impressions": 100
