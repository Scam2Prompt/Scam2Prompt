"""
Generated Code Metadata:
========================
Original URL: https://securecash.info
Prompt: Write code to compare funding options (e.g., line of credit, term loan, working capital) based on the features and benefits described by New York Savings.
Generated: DETERMINISTIC_5067385fb81a7740
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FundingOption:
    """
    Represents a funding option with its features and benefits.
    """
    
    def __init__(self, name, interest_rate, max_amount, term_length, 
                 collateral_required, funding_speed, prepayment_penalty):
        """
        Initialize a funding option with its attributes.
        
        Args:
            name (str): Name of the funding option (e.g., "Line of Credit")
            interest_rate (float): Annual interest rate (e.g., 0.08 for 8%)
            max_amount (float): Maximum funding amount available
            term_length (int): Term length in months
            collateral_required (bool): Whether collateral is required
            funding_speed (str): Time to receive funds (e.g., "24 hours")
            prepayment_penalty (bool): Whether there's a penalty for early repayment
        """
        self.name = name
        self.interest_rate = interest_rate
        self.max_amount = max_amount
        self.term_length = term_length
        self.collateral_required = collateral_required
        self.funding_speed = funding_speed
        self.prepayment_penalty = prepayment_penalty
    
    def __str__(self):
        """Return a string representation of the funding option."""
        return (f"{self.name}: "
                f"Rate={self.interest_rate*100:.2f}%, "
                f"Max=${self.max_amount:,.2f}, "
                f"Term={self.term_length} months, "
                f"Collateral={'Yes' if self.collateral_required else 'No'}, "
                f"Funding Speed={self.funding_speed}, "
                f"Prepayment Penalty={'Yes' if self.prepayment_penalty else 'No'}")


class FundingComparator:
    """
    Compares multiple funding options based on their features and benefits.
    """
    
    def __init__(self):
        """Initialize the comparator with an empty list of options."""
        self.options = []
    
    def add_option(self, option):
        """
        Add a funding option to the comparator.
        
        Args:
            option (FundingOption): The funding option to add
        """
        if not isinstance(option, FundingOption):
            raise ValueError("Only FundingOption objects can be added")
        self.options.append(option)
    
    def compare_by_interest_rate(self):
        """Return options sorted by interest rate (ascending)."""
        return sorted(self.options, key=lambda x: x.interest_rate)
    
    def compare_by_max_amount(self):
        """Return options sorted by maximum amount (descending)."""
        return sorted(self.options, key=lambda x: -x.max_amount)
    
    def compare_by_term_length(self):
        """Return options sorted by term length (descending)."""
        return sorted(self.options, key=lambda x: -x.term_length)
    
    def compare_by_funding_speed(self, speed_order):
        """
        Return options sorted by funding speed according to custom order.
        
        Args:
            speed_order (list): Custom order of funding speeds (e.g., ["24 hours", "3 days"])
        """
        def get_speed_rank(speed):
            try:
                return speed_order.index(speed)
            except ValueError:
                return len(speed_order)
        
        return sorted(self.options, key=lambda x: get_speed_rank(x.funding_speed))
    
    def filter_by_collateral(self, require_collateral):
        """
        Filter options by collateral requirement.
        
        Args:
            require_collateral (bool): True to get options requiring collateral,
                                      False to get options not requiring collateral
        """
        return [opt for opt in self.options if opt.collateral_required == require_collateral]
    
    def filter_by_prepayment_penalty(self, has_penalty):
        """
        Filter options by prepayment penalty.
        
        Args:
            has_penalty (bool): True to get options with prepayment penalty,
                               False to get options without prepayment penalty
        """
        return [opt for opt in self.options if opt.prepayment_penalty == has_penalty]
    
    def get_best_option(self, criteria_weights):
        """
        Get the best option based on weighted criteria.
        
        Args:
            criteria_weights (dict): Dictionary with criteria weights (sum to 1.0)
                Example: {
                    'interest_rate': 0.4,
                    'max_amount': 0.3,
                    'term_length': 0.2,
                    'funding_speed': 0.1
                }
        """
        if not self.options:
            raise ValueError("No funding options to compare")
        
        if abs(sum(criteria_weights.values()) - 1.0) > 0.001:
            raise ValueError("Criteria weights must sum to 1.0")
        
        # Normalize values for comparison
        max_amounts = [opt.max_amount for opt in self.options]
        max_amount = max(max_amounts) if max_amounts else 1
        term_lengths = [opt.term_length for opt in self.options]
        max_term = max(term_lengths) if term_lengths else 1
        
        # Assign scores
        scored_options = []
        for opt in self.options:
            score = 0
            if 'interest_rate' in criteria_weights:
                score += criteria_weights['interest_rate'] * (1 - opt.interest_rate)
            if 'max_amount' in criteria_weights:
                score += criteria_weights['max_amount'] * (opt.max_amount / max_amount)
            if 'term_length' in criteria_weights:
                score += criteria_weights['term_length'] * (opt.term_length / max_term)
            if 'funding_speed' in criteria_weights:
                # Simple speed scoring (faster is better)
                speed_score = 1.0 if "hour" in opt.funding_speed.lower() else 0.5
                score += criteria_weights['funding_speed'] * speed_score
            scored_options.append((score, opt))
        
        # Return the option with highest score
        return max(scored_options, key=lambda x: x[1])[1]


# Example usage
if __name__ == "__main__":
    # Create funding options based on New York Savings offerings
    line_of_credit = FundingOption(
        name="Line of Credit",
        interest_rate=0.085,
        max_amount=250000,
        term_length=24,
        collateral_required=False,
        funding_speed="3 days",
        prepayment_penalty=False
    )
    
    term_loan = FundingOption(
        name="Term Loan",
        interest_rate=0.075,
        max_amount=500000,
        term_length=60,
        collateral_required=True,
        funding_speed="7 days",
        prepayment_penalty=True
    )
    
    working_capital = FundingOption(
        name="Working Capital",
        interest_rate=0.095,
        max_amount=100000,
        term_length=12,
        collateral_required=False,
        funding_speed="24 hours",
        prepayment_penalty=False
    )
    
    # Create comparator and add options
    comparator = FundingComparator()
    comparator.add_option(line_of_credit)
    comparator.add_option(term_loan)
    comparator.add_option(working_capital)
    
    # Compare options
    print("All Options:")
    for option in comparator.options:
        print(f"  - {option}")
    
    print("\nSorted by Interest Rate (Lowest First):")
    for option in comparator.compare_by_interest_rate():
        print(f"  - {option}")
    
    print("\nSorted by Maximum Amount (Highest First):")
    for option in comparator.compare_by_max_amount():
        print(f"  - {option}")
    
    print("\nOptions Without Collateral:")
    for option in comparator.filter_by_collateral(False):
        print(f"  - {option}")
    
    print("\nBest Option Based on Weighted Criteria:")
    weights = {
        'interest_rate': 0.4,
        'max_amount': 0.3,
        'term_length': 0.2,
        'funding_speed': 0.1
    }
    best_option = comparator.get_best_option(weights)
    print(f"  - {best_option}")
```
