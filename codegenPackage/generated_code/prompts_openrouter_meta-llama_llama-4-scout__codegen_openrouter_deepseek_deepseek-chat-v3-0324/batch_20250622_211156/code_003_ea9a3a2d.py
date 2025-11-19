"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: Design a disbursement financing plan for a client with a pending injury claim in Canada, using Rhino Finance's services and taking into account the client's financial needs and litigation timeline.
Generated: DETERMINISTIC_ea9a3a2d39aae12d
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, Optional, Tuple

class DisbursementFinancingPlan:
    """
    A class to model a disbursement financing plan for a client with a pending injury claim in Canada.
    Uses Rhino Finance's services to provide financing based on the client's financial needs and litigation timeline.
    """

    def __init__(
        self,
        client_name: str,
        claim_amount: float,
        estimated_settlement_date: datetime.date,
        financial_needs: Dict[str, float],
        interest_rate: float = 0.12,  # Annual interest rate (12% default)
        service_fee: float = 0.05,    # 5% service fee
    ):
        """
        Initialize the disbursement financing plan.

        Args:
            client_name: Name of the client.
            claim_amount: Total amount of the pending injury claim (CAD).
            estimated_settlement_date: Expected date when the claim will be settled.
            financial_needs: Dictionary of financial needs (e.g., {'medical': 5000, 'living': 3000}).
            interest_rate: Annual interest rate for the financing (default 12%).
            service_fee: Service fee percentage (default 5%).
        """
        self.client_name = client_name
        self.claim_amount = claim_amount
        self.estimated_settlement_date = estimated_settlement_date
        self.financial_needs = financial_needs
        self.interest_rate = interest_rate
        self.service_fee = service_fee

        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """Validate the input parameters."""
        if not isinstance(self.client_name, str):
            raise TypeError("Client name must be a string.")
        if self.claim_amount <= 0:
            raise ValueError("Claim amount must be positive.")
        if not isinstance(self.estimated_settlement_date, datetime.date):
            raise TypeError("Estimated settlement date must be a datetime.date object.")
        if not all(isinstance(v, (int, float)) and v > 0 for v in self.financial_needs.values()):
            raise ValueError("Financial needs must be positive numbers.")
        if self.interest_rate <= 0:
            raise ValueError("Interest rate must be positive.")
        if self.service_fee <= 0:
            raise ValueError("Service fee must be positive.")

    def calculate_total_financing(self) -> float:
        """
        Calculate the total financing amount based on the client's financial needs.

        Returns:
            Total financing amount (CAD).
        """
        return sum(self.financial_needs.values())

    def calculate_days_until_settlement(self) -> int:
        """
        Calculate the number of days until the estimated settlement date.

        Returns:
            Number of days until settlement.
        """
        today = datetime.date.today()
        if self.estimated_settlement_date < today:
            raise ValueError("Estimated settlement date must be in the future.")
        return (self.estimated_settlement_date - today).days

    def calculate_interest(self) -> float:
        """
        Calculate the total interest payable based on the financing amount and days until settlement.

        Returns:
            Total interest amount (CAD).
        """
        total_financing = self.calculate_total_financing()
        days = self.calculate_days_until_settlement()
        daily_rate = self.interest_rate / 365
        return total_financing * daily_rate * days

    def calculate_service_fee(self) -> float:
        """
        Calculate the service fee based on the total financing amount.

        Returns:
            Service fee amount (CAD).
        """
        return self.calculate_total_financing() * self.service_fee

    def calculate_total_repayment(self) -> float:
        """
        Calculate the total repayment amount (financing + interest + service fee).

        Returns:
            Total repayment amount (CAD).
        """
        return (
            self.calculate_total_financing()
            + self.calculate_interest()
            + self.calculate_service_fee()
        )

    def generate_repayment_schedule(self) -> Dict[str, float]:
        """
        Generate a repayment schedule showing the breakdown of costs.

        Returns:
            Dictionary with repayment details.
        """
        return {
            "total_financing": self.calculate_total_financing(),
            "total_interest": self.calculate_interest(),
            "service_fee": self.calculate_service_fee(),
            "total_repayment": self.calculate_total_repayment(),
            "estimated_settlement_date": self.estimated_settlement_date,
            "days_until_settlement": self.calculate_days_until_settlement(),
        }

    def is_affordable(self) -> Tuple[bool, Optional[str]]:
        """
        Check if the total repayment is affordable based on the claim amount.

        Returns:
            Tuple of (is_affordable, reason if not affordable).
        """
        total_repayment = self.calculate_total_repayment()
        if total_repayment > self.claim_amount:
            return (False, "Total repayment exceeds the claim amount.")
        return (True, None)

    def generate_financing_plan(self) -> Dict:
        """
        Generate the complete financing plan for the client.

        Returns:
            Dictionary containing all financing plan details.
        """
        repayment_schedule = self.generate_repayment_schedule()
        affordable, reason = self.is_affordable()

        plan = {
            "client_name": self.client_name,
            "claim_amount": self.claim_amount,
            "financial_needs": self.financial_needs,
            "repayment_schedule": repayment_schedule,
            "is_affordable": affordable,
            "reason_if_not_affordable": reason,
        }

        return plan


# Example usage
if __name__ == "__main__":
    try:
        # Example client data
        client_name = "John Doe"
        claim_amount = 50000.0
        estimated_settlement_date = datetime.date.today() + datetime.timedelta(days=180)
        financial_needs = {
            "medical": 10000.0,
            "living_expenses": 5000.0,
            "legal_fees": 3000.0,
        }

        # Create financing plan
