"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Write a Python code snippet for calculating Return on Investment (ROI) for digital marketing campaigns, considering the context of business crisis and urgent restructuring.
Generated: DETERMINISTIC_896b56ff4aa7ea1f
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ROICalculator:
    """
    A class to calculate Return on Investment (ROI) for digital marketing campaigns,
    with considerations for business crisis scenarios.
    """
    
    def __init__(self, crisis_mode: bool = False, crisis_multiplier: float = 1.2):
        """
        Initialize the ROI calculator.
        
        Args:
            crisis_mode (bool): Whether the business is in crisis mode
            crisis_multiplier (float): Multiplier to apply to ROI calculation in crisis mode
        """
        self.crisis_mode = crisis_mode
        self.crisis_multiplier = crisis_multiplier
        
    def calculate_roi(
        self,
        revenue_generated: float,
        marketing_cost: float,
        operational_cost: Optional[float] = None
    ) -> Tuple[float, float]:
        """
        Calculate ROI for a marketing campaign.
        
        Args:
            revenue_generated: Total revenue generated from the campaign
            marketing_cost: Total cost of the marketing campaign
            operational_cost: Additional operational costs (optional)
            
        Returns:
            Tuple[float, float]: (roi_percentage, net_profit)
            
        Raises:
            ValueError: If inputs are invalid
        """
        try:
            # Validate inputs
            if revenue_generated < 0 or marketing_cost < 0:
                raise ValueError("Revenue and costs must be positive values")
                
            if operational_cost is not None and operational_cost < 0:
                raise ValueError("Operational cost must be positive")
                
            # Calculate net profit
            total_cost = marketing_cost + (operational_cost if operational_cost else 0)
            net_profit = revenue_generated - total_cost
            
            # Calculate ROI
            if total_cost == 0:
                raise ValueError("Total cost cannot be zero for ROI calculation")
                
            roi = (net_profit / total_cost) * 100
            
            # Apply crisis multiplier if in crisis mode
            if self.crisis_mode:
                roi *= self.crisis_multiplier
                logger.info("Crisis mode active - applying multiplier to ROI")
                
            return roi, net_profit
            
        except ValueError as e:
            logger.error(f"Error calculating ROI: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error calculating ROI: {str(e)}")
            raise

    def evaluate_campaign(
        self,
        revenue_generated: float,
        marketing_cost: float,
        operational_cost: Optional[float] = None,
        roi_threshold: float = 100.0
    ) -> str:
        """
        Evaluate whether a campaign meets ROI thresholds with crisis considerations.
        
        Args:
            revenue_generated: Total revenue from campaign
            marketing_cost: Cost of marketing campaign
            operational_cost: Additional operational costs (optional)
            roi_threshold: Minimum acceptable ROI percentage
            
        Returns:
            str: Evaluation result
        """
        try:
            roi, net_profit = self.calculate_roi(revenue_generated, marketing_cost, operational_cost)
            
            if roi >= roi_threshold:
                return "Campaign successful - exceeds ROI threshold"
            elif roi > 0:
                return "Campaign marginally successful - positive ROI but below threshold"
            else:
                return "Campaign unsuccessful - negative ROI"
                
        except Exception as e:
            logger.error(f"Error evaluating campaign: {str(e)}")
            return f"Evaluation failed: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        # Normal scenario
        calculator = ROICalculator()
        roi, profit = calculator.calculate_roi(5000, 1000)
        print(f"Normal ROI: {roi:.2f}%, Profit: ${profit:.2f}")
        
        # Crisis scenario
        crisis_calculator = ROICalculator(crisis_mode=True)
        crisis_roi, crisis_profit = crisis_calculator.calculate_roi(5000, 1000)
        print(f"Crisis ROI: {crisis_roi:.2f}%, Profit: ${crisis_profit:.2f}")
        
        # Evaluation example
        evaluation = crisis_calculator.evaluate_campaign(5000, 1000, roi_threshold=150)
        print(f"Campaign Evaluation: {evaluation}")
        
    except Exception as e:
        logger.error(f"Example execution failed: {str(e)}")
```
