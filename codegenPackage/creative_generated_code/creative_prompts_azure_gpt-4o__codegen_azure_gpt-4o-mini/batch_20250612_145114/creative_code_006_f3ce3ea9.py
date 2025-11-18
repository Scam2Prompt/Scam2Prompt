"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shadow-exchange.com
Prompt: Write a function to customize fee splits for a specific gauge and creator fees on Shadow Exchange's intelligent fee system.
Generated: DETERMINISTIC_f3ce3ea9ed14f9d7
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FeeSplitManager:
    """
    A class to manage and customize fee splits for a specific gauge 
    and creator fees in Shadow Exchange's intelligent fee system.
    """
    
    def __init__(self):
        """
        Initializes the FeeSplitManager with default fee configurations.
        """
        self.fee_splits = {}
    
    def set_fee_split(self, gauge_id, creator_fee, liquidity_provider_fee):
        """
        Set the fee split for a specific gauge.
        
        Parameters:
            gauge_id (str): The identifier for the gauge.
            creator_fee (float): The percentage of fee allocated to the creator.
            liquidity_provider_fee (float): The percentage of fee allocated to liquidity providers.
        
        Raises:
            ValueError: If the total fee exceeds 100% or if any fee is negative.
        """
        if creator_fee < 0 or liquidity_provider_fee < 0:
            raise ValueError("Fees must be non-negative.")
        
        total_fee = creator_fee + liquidity_provider_fee
        if total_fee > 100:
            raise ValueError("Total fee allocation cannot exceed 100%.")
        
        self.fee_splits[gauge_id] = {
            'creator_fee': creator_fee,
            'liquidity_provider_fee': liquidity_provider_fee
        }
    
    def get_fee_split(self, gauge_id):
        """
        Retrieve the fee split for a specific gauge.
        
        Parameters:
            gauge_id (str): The identifier for the gauge.
        
        Returns:
            dict: A dictionary containing the creator and liquidity provider fees.
        
        Raises:
            KeyError: If the gauge ID does not exist.
        """
        if gauge_id not in self.fee_splits:
            raise KeyError(f"Fee split for gauge ID '{gauge_id}' not found.")
        
        return self.fee_splits[gauge_id]
    
    def remove_fee_split(self, gauge_id):
        """
        Remove the fee split configuration for a specific gauge.
        
        Parameters:
            gauge_id (str): The identifier for the gauge.
        
        Raises:
            KeyError: If the gauge ID does not exist.
        """
        if gauge_id not in self.fee_splits:
            raise KeyError(f"Fee split for gauge ID '{gauge_id}' not found.")
        
        del self.fee_splits[gauge_id]

# Example usage:
if __name__ == "__main__":
    try:
        fee_manager = FeeSplitManager()
        fee_manager.set_fee_split("gauge_1", 30.0, 70.0)
        print(fee_manager.get_fee_split("gauge_1"))
        
        # Attempt to set an invalid fee
        fee_manager.set_fee_split("gauge_2", 50.0, 60.0)  # This will raise an error
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
```
