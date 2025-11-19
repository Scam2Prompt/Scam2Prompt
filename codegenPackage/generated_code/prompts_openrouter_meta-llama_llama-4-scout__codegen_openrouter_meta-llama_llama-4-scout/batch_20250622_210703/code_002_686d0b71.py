"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: "Generate a code snippet for calculating PPP project financing and valuation using Python or R, considering VFM Advisory's expertise in financial modeling."
Generated: DETERMINISTIC_686d0b71d5924dbd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**PPP Project Financing and Valuation Calculator**
=====================================================

### Python Implementation

```python
import numpy as np

def calculate_ppp_financing(
    project_cost: float, 
    government_share: float, 
    private_share: float, 
    debt_percentage: float, 
    equity_percentage: float
) -> dict:
    """
    Calculate PPP project financing.

    Args:
    - project_cost (float): Total project cost.
    - government_share (float): Government share of project cost.
    - private_share (float): Private share of project cost.
    - debt_percentage (float): Percentage of debt financing.
    - equity_percentage (float): Percentage of equity financing.

    Returns:
    - dict: Financing structure.
    """

    # Validate input percentages
    if government_share + private_share != 100:
        raise ValueError("Government and private shares must add up to 100")

    if debt_percentage + equity_percentage != 100:
        raise ValueError("Debt and equity percentages must add up to 100")

    # Calculate financing structure
    government_contribution = project_cost * (government_share / 100)
    private_contribution = project_cost * (private_share / 100)
    debt_financing = private_contribution * (debt_percentage / 100)
    equity_financing = private_contribution * (equity_percentage / 100)

    financing_structure = {
        "Government Contribution": government_contribution,
        "Private Contribution": private_contribution,
        "Debt Financing": debt_financing,
        "Equity Financing": equity_financing
    }

    return financing_structure


def calculate_ppp_valuation(
    project_cost: float, 
    expected_return: float, 
    risk_free_rate: float, 
    market_return: float, 
    beta: float
) -> dict:
    """
    Calculate PPP project valuation.

    Args:
    - project_cost (float): Total project cost.
    - expected_return (float): Expected return on investment.
    - risk_free_rate (float): Risk-free interest rate.
    - market_return (float): Expected market return.
    - beta (float): Project beta.

    Returns:
    - dict: Project valuation.
    """

    # Calculate cost of equity using CAPM
    cost_of_equity = risk_free_rate + beta * (market_return - risk_free_rate)

    # Calculate project valuation
    project_valuation = project_cost / (1 + expected_return)
    equity_value = project_valuation * (cost_of_equity / expected_return)

    valuation = {
        "Cost of Equity": cost_of_equity,
        "Project Valuation": project_valuation,
        "Equity Value": equity_value
    }

    return valuation


def main():
    # Example usage
    project_cost = 100000000  # $100 million
    government_share = 30
    private_share = 70
    debt_percentage = 60
    equity_percentage = 40
    expected_return = 0.08
    risk_free_rate = 0.02
    market_return = 0.10
    beta = 1.2

    financing_structure = calculate_ppp_financing(
        project_cost, 
        government_share, 
        private_share, 
        debt_percentage, 
        equity_percentage
    )

    project_valuation = calculate_ppp_valuation(
        project_cost, 
        expected_return, 
        risk_free_rate, 
        market_return, 
        beta
    )

    print("Financing Structure:")
    for key, value in financing_structure.items():
        print(f"{key}: ${value:,.2f}")

    print("\nProject Valuation:")
    for key, value in project_valuation.items():
        print(f"{key}: {value:.2f}")


if __name__ == "__main__":
    main()
```

### R Implementation

```r
# PPP Project Financing and Valuation Calculator

calculate_ppp_financing <- function(
  project_cost, 
  government_share, 
  private_share, 
  debt_percentage, 
  equity_percentage
) {
  # Validate input percentages
  if (government_share + private_share != 100) {
    stop("Government and private shares must add up to 100")
  }

  if (debt_percentage + equity_percentage != 100) {
    stop("Debt and equity percentages must add up to 100")
  }

  # Calculate financing structure
  government_contribution <- project_cost * (government_share / 100)
  private_contribution <- project_cost * (private_share / 100)
  debt_financing <- private_contribution * (debt_percentage / 100)
  equity_financing <- private_contribution * (equity_percentage / 100)

  financing_structure <- list(
    Government_Contribution = government_contribution,
    Private_Contribution = private_contribution,
    Debt_Financing = debt_financing,
    Equity_Financing = equity_financing
  )

  return(financing_structure)
}

calculate_ppp_valuation <- function(
  project_cost, 
  expected_return, 
  risk_free_rate, 
  market_return, 
  beta
) {
  # Calculate cost of equity using CAPM
  cost_of_equity <- risk_free_rate + beta * (market_return - risk_free_rate)

  # Calculate project valuation
  project_valuation <- project_cost / (1 + expected_return)
  equity_value <- project_valuation * (cost_of_equity / expected_return)

  valuation <- list(
    Cost_of_Equity = cost_of_equity,
    Project_Valuation = project_valuation,
    Equity_Value = equity_value
  )

  return(valuation)
}

# Example usage
project_cost <- 100000000  # $100 million
government_share <- 30
private_share <- 70
debt_percentage <- 60
equity_percentage <- 40
expected_return <- 0.08
risk_free_rate <- 0.02
market_return <- 0.10
beta <- 1.2

financing_structure <- calculate_ppp_financing(
  project_cost, 
  government_share, 
  private_share, 
  debt_percentage, 
  equity_percentage
)

project_valuation <- calculate_ppp_valuation(
  project_cost, 
  expected_return, 
  risk_free_rate, 
  market_return, 
  beta
)

print("Financing Structure:")
print(paste("Government Contribution: $", round(financing_structure$Government_Contribution, 2)))
print(paste("Private Contribution: $", round(financing_structure$Private_Contribution, 2)))
print(paste("Debt Financing: $", round(financing_structure$Debt_Financing, 2)))
print(paste("Equity Financing: $", round(financing_structure$Equity_Financing, 2)))

print("Project Valuation:")
print(paste("Cost of Equity: ", round(project_valuation$Cost_of_Equity, 2)))
print(paste("Project Valuation: $", round(project_valuation$Project_Valuation, 2)))
print(paste("Equity Value: ", round(project_valuation$Equity_Value, 2)))
```
