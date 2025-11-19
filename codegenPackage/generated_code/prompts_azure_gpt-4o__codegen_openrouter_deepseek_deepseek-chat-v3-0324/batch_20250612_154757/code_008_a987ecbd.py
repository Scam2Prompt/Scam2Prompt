"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Generate code to calculate the distribution of $INIT tokens across different categories (Community Reserve, Investors, Treasury, etc.) based on the tokenomics provided on the Initia website.
Generated: DETERMINISTIC_a987ecbdb837dbbd
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class TokenAllocation:
    """Data class representing a single token allocation category."""
    name: str
    percentage: float
    description: str = ""

class TokenDistributionCalculator:
    """
    A calculator for determining token distribution across different categories
    based on predefined tokenomics.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the calculator with total token supply.
        
        Args:
            total_supply: The total number of tokens to be distributed
        """
        self.total_supply = total_supply
        self.allocations: List[TokenAllocation] = []
        
    def add_allocation(self, name: str, percentage: float, description: str = "") -> None:
        """
        Add a new allocation category.
        
        Args:
            name: Name of the allocation category
            percentage: Percentage of total supply (0-100)
            description: Optional description of the category
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        self.allocations.append(
            TokenAllocation(name=name, percentage=percentage, description=description)
        )
        
    def validate_allocations(self) -> bool:
        """
        Validate that all allocations sum to 100%.
        
        Returns:
            bool: True if allocations sum to 100%, False otherwise
        """
        total = sum(alloc.percentage for alloc in self.allocations)
        return abs(total - 100) < 0.0001  # Account for floating point precision
    
    def calculate_distribution(self) -> Dict[str, int]:
        """
        Calculate the token distribution across all categories.
        
        Returns:
            Dict[str, int]: Mapping of category names to token amounts
            
        Raises:
            ValueError: If allocations don't sum to 100%
        """
        if not self.validate_allocations():
            raise ValueError("Allocations must sum to 100%")
            
        distribution = {}
        remaining = self.total_supply
        
        # Sort by percentage descending to minimize rounding errors
        sorted_allocations = sorted(self.allocations, key=lambda x: -x.percentage)
        
        for i, alloc in enumerate(sorted_allocations):
            # Calculate tokens for this allocation
            tokens = int(self.total_supply * alloc.percentage / 100)
            
            # For the last allocation, assign all remaining tokens to avoid rounding errors
            if i == len(sorted_allocations) - 1:
                tokens = remaining
            else:
                remaining -= tokens
                
            distribution[alloc.name] = tokens
            
        return distribution
    
    def get_distribution_report(self) -> str:
        """
        Generate a human-readable distribution report.
        
        Returns:
            str: Formatted report string
        """
        try:
            distribution = self.calculate_distribution()
        except ValueError as e:
            return f"Error: {str(e)}"
            
        report_lines = [
            "Token Distribution Report",
            "=======================",
            f"Total Supply: {self.total_supply:,} tokens",
            "",
            "Allocations:",
        ]
        
        for alloc in self.allocations:
            tokens = distribution[alloc.name]
            report_lines.append(
                f"- {alloc.name}: {tokens:,} tokens ({alloc.percentage}%)"
            )
            if alloc.description:
                report_lines.append(f"  Description: {alloc.description}")
                
        return "\n".join(report_lines)
    
    def save_to_json(self, file_path: str) -> None:
        """
        Save the distribution data to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            
        Raises:
            ValueError: If allocations don't sum to 100%
            IOError: If file cannot be written
        """
        try:
            distribution = self.calculate_distribution()
            data = {
                "total_supply": self.total_supply,
                "allocations": [
                    {
                        "name": alloc.name,
                        "percentage": alloc.percentage,
                        "tokens": distribution[alloc.name],
                        "description": alloc.description
                    }
                    for alloc in self.allocations
                ]
            }
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
                
        except ValueError as e:
            raise ValueError(f"Cannot save distribution: {str(e)}")
        except IOError as e:
            raise IOError(f"Failed to write to file: {str(e)}")

# Example usage with INIT token tokenomics
if __name__ == "__main__":
    # Initialize with total supply (example: 1 billion tokens)
    calculator = TokenDistributionCalculator(total_supply=1_000_000_000)
    
    # Add allocations based on INIT tokenomics
    calculator.add_allocation(
        name="Community Reserve",
        percentage=40.0,
        description="For community incentives, airdrops, and ecosystem growth"
    )
    calculator.add_allocation(
        name="Investors",
        percentage=25.0,
        description="Early investors and backers"
    )
    calculator.add_allocation(
        name="Treasury",
        percentage=20.0,
        description="Protocol treasury for future development"
    )
    calculator.add_allocation(
        name="Team",
        percentage=10.0,
        description="Core team and contributors"
    )
    calculator.add_allocation(
        name="Advisors",
        percentage=5.0,
        description="Strategic advisors and partners"
    )
    
    # Generate and print report
    print(calculator.get_distribution_report())
    
    # Save to JSON file
    try:
        calculator.save_to_json("init_token_distribution.json")
        print("\nDistribution saved to init_token_distribution.json")
    except (ValueError, IOError) as e:
        print(f"\nError saving distribution: {str(e)}")
```
