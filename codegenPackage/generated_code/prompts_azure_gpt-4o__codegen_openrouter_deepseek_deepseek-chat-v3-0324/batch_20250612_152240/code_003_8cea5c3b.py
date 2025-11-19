"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Write code to calculate performance metrics for a Management Strategy Evaluation (MSE) using openMSE. Include steps for examining the MSE results.
Generated: DETERMINISTIC_8cea5c3bdb228b32
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openmse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean

def calculate_performance_metrics(mse_results):
    """
    Calculate performance metrics from MSE results.
    
    Args:
        mse_results (dict): Dictionary containing MSE results from openMSE.
        
    Returns:
        dict: Dictionary of calculated performance metrics.
    """
    metrics = {}
    
    # Extract relevant data from MSE results
    biomass = mse_results['biomass']
    catch = mse_results['catch']
    f = mse_results['fishing_mortality']
    years = mse_results['years']
    n_sims = biomass.shape[0]
    n_years = biomass.shape[1]
    
    # Calculate performance metrics
    
    # 1. Probability of being above biomass target (e.g., BMSY)
    bmsy = mse_results['reference_points']['BMSY']
    prob_above_bmsy = np.mean(biomass > bmsy, axis=0)
    metrics['prob_above_bmsy'] = prob_above_bmsy
    
    # 2. Average biomass relative to BMSY
    avg_biomass_rel = np.mean(biomass / bmsy, axis=0)
    metrics['avg_biomass_rel'] = avg_biomass_rel
    
    # 3. Average catch
    avg_catch = np.mean(catch, axis=0)
    metrics['avg_catch'] = avg_catch
    
    # 4. Catch variability (CV)
    catch_cv = np.std(catch, axis=0) / np.mean(catch, axis=0)
    metrics['catch_cv'] = catch_cv
    
    # 5. Probability of overfishing (F > FMSY)
    fmsy = mse_results['reference_points']['FMSY']
    prob_overfishing = np.mean(f > fmsy, axis=0)
    metrics['prob_overfishing'] = prob_overfishing
    
    # 6. Depletion risk (probability biomass falls below threshold)
    depletion_threshold = 0.2 * bmsy  # Example threshold
    depletion_risk = np.mean(biomass < depletion_threshold, axis=0)
    metrics['depletion_risk'] = depletion_risk
    
    # 7. Geometric mean of relative biomass
    geom_mean_biomass = gmean(biomass / bmsy, axis=0)
    metrics['geom_mean_biomass'] = geom_mean_biomass
    
    # 8. First year of recovery (if applicable)
    recovery_threshold = 0.8 * bmsy
    recovery_years = []
    for sim in range(n_sims):
        above_threshold = np.where(biomass[sim] > recovery_threshold)[0]
        if len(above_threshold) > 0:
            recovery_years.append(years[above_threshold[0]])
        else:
            recovery_years.append(np.nan)
    metrics['recovery_years'] = recovery_years
    
    return metrics

def plot_performance_metrics(metrics, years):
    """
    Plot performance metrics over time.
    
    Args:
        metrics (dict): Dictionary of performance metrics
        years (array): Array of years for x-axis
    """
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Probability metrics
    plt.subplot(2, 2, 1)
    plt.plot(years, metrics['prob_above_bmsy'], label='P(B > BMSY)')
    plt.plot(years, metrics['prob_overfishing'], label='P(F > FMSY)')
    plt.plot(years, metrics['depletion_risk'], label='Depletion risk')
    plt.xlabel('Year')
    plt.ylabel('Probability')
    plt.title('Probability Metrics')
    plt.legend()
    plt.grid(True)
    
    # Plot 2: Biomass metrics
    plt.subplot(2, 2, 2)
    plt.plot(years, metrics['avg_biomass_rel'], label='Avg B/BMSY')
    plt.plot(years, metrics['geom_mean_biomass'], label='Geom mean B/BMSY')
    plt.axhline(1, color='k', linestyle='--', label='BMSY')
    plt.xlabel('Year')
    plt.ylabel('Relative biomass')
    plt.title('Biomass Metrics')
    plt.legend()
    plt.grid(True)
    
    # Plot 3: Catch metrics
    plt.subplot(2, 2, 3)
    plt.plot(years, metrics['avg_catch'], label='Average catch')
    plt.xlabel('Year')
    plt.ylabel('Catch')
    plt.title('Catch Metrics')
    plt.legend()
    plt.grid(True)
    
    # Plot 4: Catch variability
    plt.subplot(2, 2, 4)
    plt.plot(years, metrics['catch_cv'], label='Catch CV')
    plt.xlabel('Year')
    plt.ylabel('Coefficient of Variation')
    plt.title('Catch Variability')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def summarize_performance_metrics(metrics, years):
    """
    Create a summary table of performance metrics.
    
    Args:
        metrics (dict): Dictionary of performance metrics
        years (array): Array of years
        
    Returns:
        pd.DataFrame: Summary table of metrics
    """
    # Select key years for summary (first, middle, last)
    key_years = [years[0], years[len(years)//2], years[-1]]
    summary_data = []
    
    for year in key_years:
        idx = np.where(years == year)[0][0]
        summary_data.append({
            'Year': year,
            'P(B > BMSY)': metrics['prob_above_bmsy'][idx],
            'Avg B/BMSY': metrics['avg_biomass_rel'][idx],
            'P(F > FMSY)': metrics['prob_overfishing'][idx],
            'Depletion Risk': metrics['depletion_risk'][idx],
            'Avg Catch': metrics['avg_catch'][idx],
            'Catch CV': metrics['catch_cv'][idx]
        })
    
    # Add recovery statistics if available
    recovery_years = np.array(metrics['recovery_years'])
    recovery_stats = {
        'Median recovery year': np.nanmedian(recovery_years),
        'Recovery probability': np.mean(~np.isnan(recovery_years))
    }
    
    summary_df = pd.DataFrame(summary_data)
    recovery_df = pd.DataFrame([recovery_stats])
    
    return summary_df, recovery_df

def analyze_mse_results(mse_results):
    """
    Main function to analyze MSE results.
    
    Args:
        mse_results (dict): Dictionary containing MSE results from openMSE
    """
    try:
        # Calculate performance metrics
        metrics = calculate_performance_metrics(mse_results)
        
        # Plot metrics
        plot_performance_metrics(metrics, mse_results['years'])
        
        # Generate summary tables
        summary_df, recovery_df = summarize_performance_metrics(metrics, mse_results['years'])
        
        print("Performance Metrics Summary:")
        print(summary_df.to_string(index=False))
        print("\nRecovery Statistics:")
        print(recovery_df.to_string(index=False))
        
        return metrics, summary_df, recovery_df
        
    except Exception as e:
        print(f"Error analyzing MSE results: {str(e)}")
        raise

# Example usage:
if __name__ == "__main__":
    # Load MSE results (example - replace with actual MSE results)
    # mse_results = openmse.run_mse(...)
    
    # For demonstration, create dummy data
    np.random.seed(42)
    dummy_results = {
        'biomass': np.random.lognormal(mean=1.0, sigma=0.2, size=(100, 20)) * 1000,
        'catch': np.random.lognormal(mean=0.8, sigma=0.15, size=(100, 20)) * 500,
        'fishing_mortality': np.random.lognormal(mean=0.2, sigma=0.1, size=(100, 20)),
        'years': np.arange(2020, 2040),
        'reference_points': {
            'BMSY': 1000,
            'FMSY': 0.3
        }
    }
    
    # Analyze the results
    metrics, summary, recovery = analyze_mse_results(dummy_results)
```
