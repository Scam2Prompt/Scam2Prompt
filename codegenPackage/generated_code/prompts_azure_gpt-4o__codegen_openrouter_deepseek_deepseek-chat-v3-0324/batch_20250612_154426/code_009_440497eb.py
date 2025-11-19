"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Create a program to track and manage small-to-medium business investments, inspired by Genesis Investment Credit Union's business services offerings.
Generated: DETERMINISTIC_440497eb9e86ab87
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Business Investment Tracker
A program to track and manage small-to-medium business investments.
Inspired by Genesis Investment Credit Union's business services offerings.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union


class Investment:
    """Represents a single business investment."""

    def __init__(
        self,
        name: str,
        amount: float,
        date: str,
        category: str,
        roi: Optional[float] = None,
        notes: Optional[str] = None,
    ):
        """
        Initialize an investment.

        Args:
            name: Name of the investment
            amount: Investment amount
            date: Date of investment (YYYY-MM-DD)
            category: Investment category
            roi: Expected return on investment (percentage)
            notes: Additional notes about the investment
        """
        self.name = name
        self.amount = amount
        self.date = date
        self.category = category
        self.roi = roi
        self.notes = notes

    def to_dict(self) -> Dict:
        """Convert investment to dictionary for serialization."""
        return {
            "name": self.name,
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "roi": self.roi,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Investment":
        """Create Investment instance from dictionary."""
        return cls(
            name=data["name"],
            amount=data["amount"],
            date=data["date"],
            category=data["category"],
            roi=data.get("roi"),
            notes=data.get("notes"),
        )


class InvestmentTracker:
    """Manages a collection of business investments."""

    def __init__(self, data_file: str = "investments.json"):
        """
        Initialize the investment tracker.

        Args:
            data_file: Path to JSON file for storing investment data
        """
        self.data_file = data_file
        self.investments: List[Investment] = []
        self._load_investments()

    def _load_investments(self) -> None:
        """Load investments from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.investments = [
                        Investment.from_dict(item) for item in data
                    ]
            except (json.JSONDecodeError, IOError) as e:
                raise RuntimeError(
                    f"Failed to load investments from {self.data_file}: {e}"
                )

    def _save_investments(self) -> None:
        """Save investments to the data file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump(
                    [inv.to_dict() for inv in self.investments],
                    f,
                    indent=2,
                )
        except IOError as e:
            raise RuntimeError(
                f"Failed to save investments to {self.data_file}: {e}"
            )

    def add_investment(self, investment: Investment) -> None:
        """Add a new investment to the tracker."""
        self.investments.append(investment)
        self._save_investments()

    def remove_investment(self, investment_name: str) -> bool:
        """
        Remove an investment by name.

        Args:
            investment_name: Name of investment to remove

        Returns:
            bool: True if investment was found and removed, False otherwise
        """
        for i, inv in enumerate(self.investments):
            if inv.name == investment_name:
                del self.investments[i]
                self._save_investments()
                return True
        return False

    def get_investment(self, investment_name: str) -> Optional[Investment]:
        """
        Get an investment by name.

        Args:
            investment_name: Name of investment to retrieve

        Returns:
            Optional[Investment]: Investment if found, None otherwise
        """
        for inv in self.investments:
            if inv.name == investment_name:
                return inv
        return None

    def get_all_investments(self) -> List[Investment]:
        """Get all investments."""
        return self.investments

    def get_investments_by_category(self, category: str) -> List[Investment]:
        """
        Get investments by category.

        Args:
            category: Category to filter by

        Returns:
            List[Investment]: List of investments in the specified category
        """
        return [inv for inv in self.investments if inv.category == category]

    def get_total_investment(self) -> float:
        """Calculate total amount invested across all investments."""
        return sum(inv.amount for inv in self.investments)

    def get_expected_return(self) -> float:
        """Calculate total expected return across all investments."""
        total = 0.0
        for inv in self.investments:
            if inv.roi is not None:
                total += inv.amount * (inv.roi / 100)
        return total


def validate_date(date_str: str) -> bool:
    """
    Validate date format (YYYY-MM-DD).

    Args:
        date_str: Date string to validate

    Returns:
        bool: True if valid, False otherwise
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def display_menu() -> None:
    """Display the main menu options."""
    print("\nBusiness Investment Tracker")
    print("1. Add New Investment")
    print("2. View All Investments")
    print("3. View Investments by Category")
    print("4. Remove Investment")
    print("5. View Investment Details")
    print("6. View Total Investment")
    print("7. View Expected Return")
    print("8. Exit")


def get_user_input(prompt: str, input_type: type = str) -> Union[str, float]:
    """
    Get validated user input.

    Args:
        prompt: Input prompt to display
        input_type: Expected input type (str or float)

    Returns:
        Union[str, float]: Validated user input
    """
    while True:
        try:
            user_input = input(prompt)
            if input_type == float:
                return float(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")


def main() -> None:
    """Main program loop."""
    tracker = InvestmentTracker()

    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-8): ")

        if choice == "1":
            # Add new investment
            print("\nAdd New Investment")
            name = get_user_input("Investment name: ")
            amount = get_user_input("Amount: ", float)
            date = get_user_input("Date (YYYY-MM-DD): ")
            while not validate_date(date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                date = get_user_input("Date (YYYY-MM-DD): ")
            category = get_user_input("Category: ")
            roi_input = get_user_input(
                "Expected ROI (percentage, leave blank if unknown): "
            )
            roi = float(roi_input) if roi_input else None
            notes = get_user_input("Notes (optional): ") or None

            investment = Investment(
                name=name,
                amount=amount,
                date=date,
                category=category,
                roi=roi,
                notes=notes,
            )
            tracker.add_investment(investment)
            print(f"Investment '{name}' added successfully.")

        elif choice == "2":
            # View all investments
            print("\nAll Investments:")
            investments = tracker.get_all_investments()
            if not investments:
                print("No investments found.")
            else:
                for inv in investments:
                    print(
                        f"{inv.name}: ${inv.amount:.2f} ({inv.category}) - {inv.date}"
                    )

        elif choice == "3":
            # View investments by category
            category = get_user_input("\nEnter category to filter by: ")
            investments = tracker.get_investments_by_category(category)
            if not investments:
                print(f"No investments found in category '{category}'.")
            else:
                print(f"\nInvestments in category '{category}':")
                for inv in investments:
                    print(
                        f"{inv.name}: ${inv.amount:.2f} - {inv.date}"
                    )

        elif choice == "4":
            # Remove investment
            name = get_user_input("\nEnter investment name to remove: ")
            if tracker.remove_investment(name):
                print(f"Investment '{name}' removed successfully.")
            else:
                print(f"Investment '{name}' not found.")

        elif choice == "5":
            # View investment details
            name = get_user_input("\nEnter investment name to view: ")
            investment = tracker.get_investment(name)
            if investment:
                print("\nInvestment Details:")
                print(f"Name: {investment.name}")
                print(f"Amount: ${investment.amount:.2f}")
                print(f"Date: {investment.date}")
                print(f"Category: {investment.category}")
                print(f"ROI: {investment.roi}%" if investment.roi else "ROI:
