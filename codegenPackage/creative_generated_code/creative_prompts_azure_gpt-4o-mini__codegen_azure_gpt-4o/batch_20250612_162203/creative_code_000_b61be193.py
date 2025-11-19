"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Generate a code snippet for a financial service application that includes features for credit process optimization as described on the SIF website.
Generated: DETERMINISTIC_b61be1935c98263f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Financial Service Application - Credit Process Optimization

This script provides features for credit process optimization such as credit evaluation,
application processing, and approval management. The code is designed to be modular, 
maintainable, and production-ready.
"""

import logging
from datetime import datetime
from typing import Dict, Any

# Configure logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class CreditApplicationError(Exception):
    """Custom exception for credit application errors."""
    pass


class CreditEvaluator:
    """
    Handles credit evaluation logic based on customer's financial data and credit history.
    """

    def evaluate_credit_score(self, customer_data: Dict[str, Any]) -> int:
        """
        Evaluate credit score based on customer financial data.

        Args:
            customer_data (dict): Customer's financial data and history.

        Returns:
            int: Credit score (0-850 scale).
        """
        try:
            income = customer_data.get("income", 0)
            debt = customer_data.get("debt", 0)
            payment_history = customer_data.get("payment_history", [])
            if income <= 0:
                raise ValueError("Invalid income value.")

            # Calculate credit score using simplified formula
            debt_to_income_ratio = debt / income if income > 0 else 1
            history_score = sum(payment_history) / len(payment_history) if payment_history else 0

            # Example formula for credit score calculation
            credit_score = max(0, min(850, int((income - debt_to_income_ratio * 1000) + history_score * 100)))
            return credit_score

        except Exception as e:
            logging.error(f"Failed to evaluate credit score: {e}")
            raise CreditApplicationError("Error evaluating credit score.") from e


class CreditProcessManager:
    """
    Manages the credit application process including approval logic.
    """

    def __init__(self):
        self.evaluator = CreditEvaluator()

    def process_application(self, application_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process credit application and determine approval status.

        Args:
            application_data (dict): Application details containing customer data and requested credit.

        Returns:
            dict: Result containing approval status and details.
        """
        try:
            # Extract customer data and requested credit
            customer_data = application_data.get("customer_data", {})
            requested_credit = application_data.get("requested_credit", 0)

            # Evaluate credit score
            credit_score = self.evaluator.evaluate_credit_score(customer_data)
            logging.info(f"Credit score evaluated: {credit_score}")

            # Determine approval status
            approval_status = "Pending"
            if credit_score > 700 and requested_credit <= customer_data.get("income", 0) * 0.5:
                approval_status = "Approved"
            elif credit_score > 500:
                approval_status = "Under Review"
            else:
                approval_status = "Denied"

            # Return result
            return {
                "credit_score": credit_score,
                "approval_status": approval_status,
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            logging.error(f"Failed to process application: {e}")
            raise CreditApplicationError("Error processing credit application.") from e


# Example usage
if __name__ == "__main__":
    try:
        manager = CreditProcessManager()
        example_application = {
            "customer_data": {
                "income": 75000,
                "debt": 15000,
                "payment_history": [1, 1, 0, 1, 1]  # 1 indicates timely payment
            },
            "requested_credit": 20000
        }

        result = manager.process_application(example_application)
        logging.info(f"Application Result: {result}")
    except CreditApplicationError as ce:
        logging.error(f"Application failed due to error: {ce}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
