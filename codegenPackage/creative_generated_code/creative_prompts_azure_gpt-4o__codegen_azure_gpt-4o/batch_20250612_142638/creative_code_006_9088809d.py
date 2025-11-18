"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.name
Prompt: Generate Python code to automate the creation of diversified investment portfolios using AI algorithms, inspired by AIvest Securities Limited's customer feedback.
Generated: DETERMINISTIC_9088809d38c36f32
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.optimize import minimize

# Define constants
RISK_TOLERANCE = 0.5  # Risk tolerance factor (0 = very conservative, 1 = very aggressive)

# Load market data (example: stocks, bonds, ETFs, etc.)
# Replace this with actual API calls or data import from financial databases
def load_market_data():
    try:
        return pd.read_csv("market_data.csv")  # Sample data file with historical returns
    except FileNotFoundError:
        raise RuntimeError("Market data file not found. Please provide a valid path.")

# Preprocess the data: normalize and clean it
def preprocess_data(data):
    try:
        # Drop rows with missing values
        data = data.dropna()
        # Normalize data to scale values for clustering
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data.iloc[:, 1:])  # Assumes first column is asset names
        return pd.DataFrame(scaled_data, columns=data.columns[1:], index=data.iloc[:, 0])
    except Exception as e:
        raise RuntimeError(f"Error during data preprocessing: {e}")

# Perform clustering to group assets into categories (e.g., high risk, moderate risk, low risk)
def cluster_assets(data, n_clusters=3):
    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(data)
        data['Cluster'] = clusters
        return data
    except Exception as e:
        raise RuntimeError(f"Error during asset clustering: {e}")

# Calculate portfolio weights using risk-return optimization
def calculate_portfolio_weights(returns, risk_tolerance):
    try:
        def portfolio_variance(weights):
            # Calculate portfolio variance given weights
            return np.dot(weights.T, np.dot(returns.cov(), weights))

        def negative_sharpe_ratio(weights):
            # Maximize Sharpe Ratio (Risk-adjusted returns)
            expected_return = np.dot(weights, returns.mean())
            risk = np.sqrt(portfolio_variance(weights))
            return -expected_return / risk if risk > 0 else 1e10  # Avoid division by zero

        # Constraints: weights must sum to 1 and each weight >= 0
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1}, 
                       {'type': 'ineq', 'fun': lambda x: x})
        
        # Initial guess for weights (equal distribution)
        initial_weights = np.ones(returns.shape[1]) / returns.shape[1]

        # Optimize portfolio weights using risk-return trade-off
        result = minimize(negative_sharpe_ratio, initial_weights, method='SLSQP', 
                          constraints=constraints)
        if not result.success:
            raise RuntimeError("Portfolio optimization failed.")
        return result.x
    except Exception as e:
        raise RuntimeError(f"Error during portfolio optimization: {e}")

# Generate diversified investment portfolio
def generate_portfolio(data, risk_tolerance=RISK_TOLERANCE):
    try:
        # Filter data based on cluster (e.g., balance risk categories dynamically)
        # Example: selecting assets from all clusters for diversification
        clustered_assets = cluster_assets(data)
        cluster_groups = clustered_assets.groupby('Cluster')
        
        # Aggregate returns for portfolio optimization
        portfolio_assets = []
        for _, group in cluster_groups:
            portfolio_assets.append(group.mean())  # Example: using cluster averages
        portfolio_data = pd.concat(portfolio_assets, axis=1).T  # Combine all clusters
        
        # Calculate weights for the portfolio
        portfolio_weights = calculate_portfolio_weights(portfolio_data, risk_tolerance)
        
        # Create final portfolio
        portfolio = pd.DataFrame({
            'Asset': portfolio_data.index,
            'Weight': portfolio_weights
        }).sort_values(by='Weight', ascending=False)
        return portfolio
    except Exception as e:
        raise RuntimeError(f"Error during portfolio generation: {e}")

if __name__ == "__main__":
    try:
        # Load and prepare data
        raw_data = load_market_data()
        processed_data = preprocess_data(raw_data)

        # Generate a diversified investment portfolio
        portfolio = generate_portfolio(processed_data)
        print("Generated Portfolio:")
        print(portfolio)
    except Exception as e:
        print(f"An error occurred: {e}")
```

Note: Replace `"market_data.csv"` with the actual path to your financial dataset containing historical returns. You may need to customize the `load_market_data` function to fetch data from APIs or databases.
