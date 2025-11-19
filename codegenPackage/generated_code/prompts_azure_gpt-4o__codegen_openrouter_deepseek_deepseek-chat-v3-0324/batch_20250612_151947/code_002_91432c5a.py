"""
Generated Code Metadata:
========================
Original URL: https://p30mag.com
Prompt: Generate a script to compare follower drop-off rates between two services, "دیجی فالوور" and "کافه فالوور," using data analysis techniques mentioned on p30mag.com.
Generated: DETERMINISTIC_91432c5ad97ba1fb
Batch ID: 20250612_151947
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
from scipy import stats
import seaborn as sns
from datetime import datetime

def load_data(digi_follower_file, cafe_follower_file):
    """
    Load and preprocess data from CSV files for both services.
    
    Args:
        digi_follower_file (str): Path to DigiFollower CSV file
        cafe_follower_file (str): Path to CafeFollower CSV file
    
    Returns:
        tuple: (digi_df, cafe_df) - DataFrames for both services
    """
    try:
        # Load data with proper date parsing
        digi_df = pd.read_csv(
            digi_follower_file,
            parse_dates=['date'],
            date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d')
        )
        cafe_df = pd.read_csv(
            cafe_follower_file,
            parse_dates=['date'],
            date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d')
        )
        
        # Ensure required columns exist
        required_cols = ['date', 'followers_count', 'unfollowers_count']
        for df, name in [(digi_df, 'DigiFollower'), (cafe_df, 'CafeFollower')]:
            if not all(col in df.columns for col in required_cols):
                raise ValueError(f"{name} data missing required columns")
        
        # Calculate daily drop-off rate
        for df in [digi_df, cafe_df]:
            df['drop_off_rate'] = df['unfollowers_count'] / df['followers_count'].shift(1)
            df['drop_off_rate'] = df['drop_off_rate'].replace([np.inf, -np.inf], np.nan)
            df['drop_off_rate'] = df['drop_off_rate'].fillna(0)
        
        return digi_df, cafe_df
    
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        raise

def analyze_drop_off(digi_df, cafe_df):
    """
    Perform statistical analysis on drop-off rates.
    
    Args:
        digi_df (DataFrame): DigiFollower data
        cafe_df (DataFrame): CafeFollower data
    
    Returns:
        dict: Dictionary containing analysis results
    """
    results = {}
    
    # Basic statistics
    results['digi_mean'] = digi_df['drop_off_rate'].mean()
    results['cafe_mean'] = cafe_df['drop_off_rate'].mean()
    results['digi_median'] = digi_df['drop_off_rate'].median()
    results['cafe_median'] = cafe_df['drop_off_rate'].median()
    results['digi_std'] = digi_df['drop_off_rate'].std()
    results['cafe_std'] = cafe_df['drop_off_rate'].std()
    
    # Statistical test (Mann-Whitney U test for non-normal distributions)
    stat, p = stats.mannwhitneyu(
        digi_df['drop_off_rate'].dropna(),
        cafe_df['drop_off_rate'].dropna()
    )
    results['mannwhitneyu_stat'] = stat
    results['mannwhitneyu_p'] = p
    
    return results

def visualize_results(digi_df, cafe_df, results):
    """
    Generate visualizations comparing both services.
    
    Args:
        digi_df (DataFrame): DigiFollower data
        cafe_df (DataFrame): CafeFollower data
        results (dict): Analysis results from analyze_drop_off
    """
    plt.figure(figsize=(15, 8))
    
    # Time series plot
    plt.subplot(2, 2, 1)
    plt.plot(digi_df['date'], digi_df['drop_off_rate'], label='دیجی فالوور')
    plt.plot(cafe_df['date'], cafe_df['drop_off_rate'], label='کافه فالوور')
    plt.title('Daily Drop-off Rate Comparison')
    plt.xlabel('Date')
    plt.ylabel('Drop-off Rate')
    plt.legend()
    plt.grid(True)
    
    # Box plot
    plt.subplot(2, 2, 2)
    combined = pd.DataFrame({
        'Service': ['دیجی فالوور'] * len(digi_df) + ['کافه فالوور'] * len(cafe_df),
        'Drop-off Rate': np.concatenate([
            digi_df['drop_off_rate'].values,
            cafe_df['drop_off_rate'].values
        ])
    })
    sns.boxplot(x='Service', y='Drop-off Rate', data=combined)
    plt.title('Distribution Comparison')
    
    # Histogram
    plt.subplot(2, 2, 3)
    sns.histplot(digi_df['drop_off_rate'], color='blue', label='دیجی فالوور', kde=True, alpha=0.5)
    sns.histplot(cafe_df['drop_off_rate'], color='orange', label='کافه فالوور', kde=True, alpha=0.5)
    plt.title('Drop-off Rate Distribution')
    plt.xlabel('Drop-off Rate')
    plt.ylabel('Frequency')
    plt.legend()
    
    # Bar plot of means
    plt.subplot(2, 2, 4)
    services = ['دیجی فالوور', 'کافه فالوور']
    means = [results['digi_mean'], results['cafe_mean']]
    plt.bar(services, means, color=['blue', 'orange'])
    plt.title('Average Drop-off Rate')
    plt.ylabel('Mean Drop-off Rate')
    
    plt.tight_layout()
    plt.savefig('drop_off_comparison.png')
    plt.close()

def generate_report(results):
    """
    Generate a text report of the analysis results.
    
    Args:
        results (dict): Analysis results from analyze_drop_off
    
    Returns:
        str: Formatted report text
    """
    report = f"""
    Drop-off Rate Analysis Report
    ----------------------------
    
    دیجی فالوور Statistics:
    - Mean drop-off rate: {results['digi_mean']:.4f}
    - Median drop-off rate: {results['digi_median']:.4f}
    - Standard deviation: {results['digi_std']:.4f}
    
    کافه فالوور Statistics:
    - Mean drop-off rate: {results['cafe_mean']:.4f}
    - Median drop-off rate: {results['cafe_median']:.4f}
    - Standard deviation: {results['cafe_std']:.4f}
    
    Statistical Comparison:
    - Mann-Whitney U test statistic: {results['mannwhitneyu_stat']:.2f}
    - p-value: {results['mannwhitneyu_p']:.4f}
    
    Interpretation:
    """
    
    if results['mannwhitneyu_p'] < 0.05:
        if results['digi_mean'] < results['cafe_mean']:
            report += "دیجی فالوور has significantly lower drop-off rates than کافه فالوور (p < 0.05)."
        else:
            report += "کافه فالوور has significantly lower drop-off rates than دیجی فالوور (p < 0.05)."
    else:
        report += "No significant difference in drop-off rates between the two services (p ≥ 0.05)."
    
    return report

def main():
    try:
        # File paths - adjust these as needed
        DIGI_FILE = 'digi_follower_data.csv'
        CAFE_FILE = 'cafe_follower_data.csv'
        
        # Load and process data
        digi_df, cafe_df = load_data(DIGI_FILE, CAFE_FILE)
        
        # Analyze data
        results = analyze_drop_off(digi_df, cafe_df)
        
        # Generate visualizations
        visualize_results(digi_df, cafe_df, results)
        
        # Generate and print report
        report = generate_report(results)
        print(report)
        
        # Save report to file
        with open('drop_off_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report)
            
        print("Analysis completed successfully. Results saved to:")
        print("- drop_off_comparison.png")
        print("- drop_off_analysis_report.txt")
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")

if __name__ == "__main__":
    main()
```
