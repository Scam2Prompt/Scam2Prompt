"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Develop a financial planning API that includes features for retirement and wealth planning, inspired by the services offered by Grade World Investment Limited.
Generated: DETERMINISTIC_2fc939724fb443ae
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Planning API for retirement and wealth planning.
Inspired by Grade World Investment Limited services.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import date
import math
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Financial Planning API",
    description="API for retirement and wealth planning services",
    version="1.0.0"
)

class RetirementInput(BaseModel):
    current_age: int = Field(..., gt=0, description="Current age of the user")
    retirement_age: int = Field(..., gt=0, description="Planned retirement age")
    current_savings: float = Field(..., ge=0, description="Current savings amount")
    monthly_contribution: float = Field(..., ge=0, description="Monthly contribution amount")
    annual_return_rate: float = Field(..., ge=0, le=100, description="Expected annual return rate (%)")
    inflation_rate: float = Field(default=2.5, ge=0, le=100, description="Expected inflation rate (%)")
    life_expectancy: int = Field(default=85, gt=0, description="Expected life expectancy")

    @validator('retirement_age')
    def validate_retirement_age(cls, v, values):
        if 'current_age' in values and v <= values['current_age']:
            raise ValueError('Retirement age must be greater than current age')
        return v

class WealthInput(BaseModel):
    initial_investment: float = Field(..., ge=0, description="Initial investment amount")
    monthly_contribution: float = Field(..., ge=0, description="Monthly contribution amount")
    investment_period: int = Field(..., gt=0, description="Investment period in years")
    annual_return_rate: float = Field(..., ge=0, le=100, description="Expected annual return rate (%)")
    risk_tolerance: str = Field(default="medium", description="Risk tolerance level (low/medium/high)")

class FinancialPlanResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict]

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/retirement/calculate", response_model=FinancialPlanResponse)
async def calculate_retirement_plan(input: RetirementInput):
    """
    Calculate retirement plan based on user inputs.
    Returns projected savings at retirement and annual withdrawal amounts.
    """
    try:
        logger.info(f"Calculating retirement plan for age {input.current_age}")
        
        # Calculate working years and retirement years
        working_years = input.retirement_age - input.current_age
        retirement_years = input.life_expectancy - input.retirement_age
        
        if working_years <= 0 or retirement_years <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid age parameters"
            )

        # Calculate future value of current savings
        monthly_rate = input.annual_return_rate / 100 / 12
        months = working_years * 12
        
        future_value_current_savings = input.current_savings * (1 + monthly_rate) ** months
        
        # Calculate future value of monthly contributions
        future_value_contributions = (
            input.monthly_contribution * 
            ((1 + monthly_rate) ** months - 1) / 
            monthly_rate
        )
        
        total_at_retirement = future_value_current_savings + future_value_contributions
        
        # Calculate annual withdrawal amount adjusted for inflation
        real_return_rate = (1 + input.annual_return_rate/100) / (1 + input.inflation_rate/100) - 1
        annual_withdrawal = (
            total_at_retirement * real_return_rate * 
            (1 + real_return_rate) ** retirement_years / 
            ((1 + real_return_rate) ** retirement_years - 1)
        )

        result = {
            "total_at_retirement": round(total_at_retirement, 2),
            "annual_withdrawal": round(annual_withdrawal, 2),
            "working_years": working_years,
            "retirement_years": retirement_years
        }
        
        return FinancialPlanResponse(
            success=True,
            message="Retirement plan calculated successfully",
            data=result
        )
        
    except Exception as e:
        logger.error(f"Error calculating retirement plan: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error calculating retirement plan"
        )

@app.post("/wealth/calculate", response_model=FinancialPlanResponse)
async def calculate_wealth_plan(input: WealthInput):
    """
    Calculate wealth accumulation plan based on user inputs.
    Returns projected investment growth over time.
    """
    try:
        logger.info(f"Calculating wealth plan for {input.investment_period} years")
        
        # Adjust return rate based on risk tolerance
        risk_adjustment = {
            "low": 0.8,
            "medium": 1.0,
            "high": 1.2
        }.get(input.risk_tolerance.lower(), 1.0)
        
        adjusted_return_rate = input.annual_return_rate * risk_adjustment
        
        # Calculate future value
        monthly_rate = adjusted_return_rate / 100 / 12
        months = input.investment_period * 12
        
        future_value_initial = input.initial_investment * (1 + monthly_rate) ** months
        
        future_value_contributions = (
            input.monthly_contribution * 
            ((1 + monthly_rate) ** months - 1) / 
            monthly_rate
        )
        
        total_value = future_value_initial + future_value_contributions
        
        # Generate yearly projections
        yearly_projections = []
        for year in range(1, input.investment_period + 1):
            months_in_year = year * 12
            fv_initial = input.initial_investment * (1 + monthly_rate) ** months_in_year
            fv_contributions = (
                input.monthly_contribution * 
                ((1 + monthly_rate) ** months_in_year - 1) / 
                monthly_rate
            )
            yearly_projections.append({
                "year": year,
                "value": round(fv_initial + fv_contributions, 2)
            })

        result = {
            "final_value": round(total_value, 2),
            "adjusted_return_rate": round(adjusted_return_rate, 2),
            "yearly_projections": yearly_projections
        }
        
        return FinancialPlanResponse(
            success=True,
            message="Wealth plan calculated successfully",
            data=result
        )
        
    except Exception as e:
        logger.error(f"Error calculating wealth plan: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error calculating wealth plan"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
