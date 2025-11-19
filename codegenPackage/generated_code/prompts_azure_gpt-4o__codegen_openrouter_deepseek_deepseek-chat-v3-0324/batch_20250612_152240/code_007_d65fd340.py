"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Provide Python code to configure custom parameters for stock assessment models in the SAMtool package within openMSE.
Generated: DETERMINISTIC_d65fd34053009cb4
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import SAMtool
from openMSE import MSEtool

def configure_samtool_parameters(
    stock_name: str,
    natural_mortality: float,
    steepness: float,
    sigma_r: float,
    sigma_f: float,
    sigma_i: float,
    sigma_c: float,
    r_prior: tuple = (0.2, 0.6),
    k_prior: tuple = (1000, 10000),
    b0_prior: tuple = (0.2, 0.8),
    age_maturity: int = 2,
    plus_group: int = 15,
    verbose: bool = True
) -> SAMtool.Stock:
    """
    Configure custom parameters for a stock assessment model in SAMtool.
    
    Args:
        stock_name: Name of the stock
        natural_mortality: Natural mortality rate (M)
        steepness: Stock-recruitment steepness (h)
        sigma_r: Recruitment standard deviation
        sigma_f: Fishing mortality standard deviation
        sigma_i: Index standard deviation
        sigma_c: Catch standard deviation
        r_prior: Prior for intrinsic growth rate (low, high)
        k_prior: Prior for carrying capacity (low, high)
        b0_prior: Prior for initial depletion (low, high)
        age_maturity: Age at maturity
        plus_group: Plus group age
        verbose: Whether to print configuration details
    
    Returns:
        Configured SAMtool Stock object
    """
    try:
        # Initialize stock object
        stock = SAMtool.Stock(stock_name)
        
        # Set basic life history parameters
        stock.natM = natural_mortality
        stock.h = steepness
        stock.age_mature = age_maturity
        stock.plusgroup = plus_group
        
        # Set process error parameters
        stock.sigma_r = sigma_r
        stock.sigma_f = sigma_f
        
        # Set observation error parameters
        stock.sigma_i = sigma_i
        stock.sigma_c = sigma_c
        
        # Set priors
        stock.r_prior = r_prior
        stock.k_prior = k_prior
        stock.b0_prior = b0_prior
        
        if verbose:
            print(f"Successfully configured stock: {stock_name}")
            print(f"Natural Mortality (M): {natural_mortality}")
            print(f"Steepness (h): {steepness}")
            print(f"Age at maturity: {age_maturity}")
            print(f"Plus group age: {plus_group}")
        
        return stock
    
    except Exception as e:
        print(f"Error configuring stock parameters: {str(e)}")
        raise

def run_sam_assessment(
    stock: SAMtool.Stock,
    catch_data: list,
    index_data: list,
    years: list,
    ages: list,
    n_iter: int = 1000,
    n_burn: int = 500,
    thin: int = 5,
    chains: int = 3,
    verbose: bool = True
) -> SAMtool.Fit:
    """
    Run SAM stock assessment with configured parameters.
    
    Args:
        stock: Configured SAMtool Stock object
        catch_data: Catch-at-age matrix (years x ages)
        index_data: Index-at-age matrix (years x ages)
        years: List of assessment years
        ages: List of ages in assessment
        n_iter: Number of MCMC iterations
        n_burn: Number of burn-in iterations
        thin: Thinning rate
        chains: Number of MCMC chains
        verbose: Whether to print progress
    
    Returns:
        SAMtool Fit object with assessment results
    """
    try:
        # Prepare data objects
        data = SAMtool.Data()
        data.CAA = catch_data
        data.IAA = index_data
        data.years = years
        data.ages = ages
        
        # Configure MCMC settings
        control = SAMtool.Control()
        control.n_iter = n_iter
        control.n_burn = n_burn
        control.thin = thin
        control.n_chains = chains
        control.verbose = verbose
        
        # Run assessment
        fit = SAMtool.fit(stock, data, control)
        
        if verbose:
            print("Assessment completed successfully")
            print(f"Convergence R-hat: {fit.rhat:.3f}")
            print(f"Effective sample size: {fit.neff}")
        
        return fit
    
    except Exception as e:
        print(f"Error running assessment: {str(e)}")
        raise

def convert_to_mse_input(
    fit: SAMtool.Fit,
    mse_years: int = 50,
    n_sim: int = 100,
    seed: int = 42
) -> MSEtool.OM:
    """
    Convert SAM assessment results to MSE operating model.
    
    Args:
        fit: SAMtool Fit object
        mse_years: Number of projection years
        n_sim: Number of simulations
        seed: Random seed
    
    Returns:
        MSEtool Operating Model object
    """
    try:
        # Convert SAM fit to MSE operating model
        om = MSEtool.SAM2OM(
            fit,
            nsim=n_sim,
            proyears=mse_years,
            seed=seed
        )
        
        return om
    
    except Exception as e:
        print(f"Error converting to MSE input: {str(e)}")
        raise
```
