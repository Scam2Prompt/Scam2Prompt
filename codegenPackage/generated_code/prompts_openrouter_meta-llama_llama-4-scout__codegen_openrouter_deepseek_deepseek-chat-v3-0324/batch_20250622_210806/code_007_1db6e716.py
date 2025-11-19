"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: Describe the role of Pyth Network's data providers, including major financial institutions, in contributing to the oracle's reliability and accuracy.
Generated: DETERMINISTIC_1db6e7160e91db1a
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module demonstrates the role of Pyth Network's data providers in contributing
to the oracle's reliability and accuracy.
"""

class DataProvider:
    """
    Represents a data provider in the Pyth Network ecosystem.
    
    Attributes:
        name (str): Name of the data provider (e.g., financial institution)
        reputation_score (float): Provider's reliability score (0-1)
        data_quality_score (float): Quality score of provided data (0-1)
        stake (float): Amount staked in the network as collateral
    """
    
    def __init__(self, name: str, reputation_score: float, data_quality_score: float, stake: float):
        """
        Initialize a DataProvider instance.
        
        Args:
            name: Name of the data provider
            reputation_score: Provider's reliability score (0-1)
            data_quality_score: Quality score of provided data (0-1)
            stake: Amount staked in the network
        """
        self.name = name
        self.reputation_score = reputation_score
        self.data_quality_score = data_quality_score
        self.stake = stake
        
    def update_reputation(self, new_score: float) -> None:
        """
        Update the provider's reputation score.
        
        Args:
            new_score: New reputation score (0-1)
            
        Raises:
            ValueError: If score is outside valid range
        """
        if not 0 <= new_score <= 1:
            raise ValueError("Reputation score must be between 0 and 1")
        self.reputation_score = new_score
        
    def update_data_quality(self, new_score: float) -> None:
        """
        Update the provider's data quality score.
        
        Args:
            new_score: New data quality score (0-1)
            
        Raises:
            ValueError: If score is outside valid range
        """
        if not 0 <= new_score <= 1:
            raise ValueError("Data quality score must be between 0 and 1")
        self.data_quality_score = new_score
        
    def update_stake(self, amount: float) -> None:
        """
        Update the provider's staked amount.
        
        Args:
            amount: Amount to add (positive) or subtract (negative)
            
        Raises:
            ValueError: If resulting stake would be negative
        """
        if self.stake + amount < 0:
            raise ValueError("Stake cannot be negative")
        self.stake += amount


class PythOracle:
    """
    Represents the Pyth Network oracle aggregating data from multiple providers.
    
    Attributes:
        providers (list[DataProvider]): List of registered data providers
    """
    
    def __init__(self):
        """Initialize an empty PythOracle instance."""
        self.providers = []
        
    def add_provider(self, provider: DataProvider) -> None:
        """
        Add a new data provider to the network.
        
        Args:
            provider: DataProvider instance to add
        """
        self.providers.append(provider)
        
    def remove_provider(self, provider_name: str) -> None:
        """
        Remove a data provider from the network.
        
        Args:
            provider_name: Name of provider to remove
            
        Raises:
            ValueError: If provider not found
        """
        for i, provider in enumerate(self.providers):
            if provider.name == provider_name:
                self.providers.pop(i)
                return
        raise ValueError(f"Provider {provider_name} not found")
        
    def calculate_weighted_price(self, asset: str) -> float:
        """
        Calculate the weighted price for an asset based on provider data.
        
        Args:
            asset: Asset identifier to calculate price for
            
        Returns:
            Weighted average price
            
        Raises:
            ValueError: If no providers available
        """
        if not self.providers:
            raise ValueError("No data providers available")
            
        total_weight = 0
        weighted_sum = 0
        
        # In a real implementation, this would fetch actual price data
        # from each provider for the specified asset
        for provider in self.providers:
            # Simplified: weight = reputation * quality * stake
            weight = (provider.reputation_score * 
                     provider.data_quality_score * 
                     provider.stake)
            total_weight += weight
            
            # Mock price data - in reality this would come from provider API
            mock_price = 100.0  # Base price
            price_variation = (1 - provider.reputation_score) * 10
            price = mock_price + price_variation
            
            weighted_sum += price * weight
            
        return weighted_sum / total_weight if total_weight > 0 else 0
    
    def get_top_providers(self, n: int = 3) -> list[DataProvider]:
        """
        Get the top n providers by combined score.
        
        Args:
            n: Number of top providers to return
            
        Returns:
            List of top n DataProvider instances
        """
        if n <= 0:
            return []
            
        # Sort providers by combined score (reputation * quality * stake)
        sorted_providers = sorted(
            self.providers,
            key=lambda p: p.reputation_score * p.data_quality_score * p.stake,
            reverse=True
        )
        return sorted_providers[:n]


# Example usage demonstrating major financial institutions as data providers
if __name__ == "__main__":
    oracle = PythOracle()
    
    # Add major financial institutions as data providers
    oracle.add_provider(DataProvider("Goldman Sachs", 0.95, 0.92, 1000000))
    oracle.add_provider(DataProvider("JPMorgan Chase", 0.93, 0.94, 1200000))
    oracle.add_provider(DataProvider("Citadel Securities", 0.96, 0.95, 1500000))
    oracle.add_provider(DataProvider("Jane Street", 0.94, 0.93, 900000))
    
    try:
        weighted_price = oracle.calculate_weighted_price("BTC/USD")
        print(f"Calculated weighted price: {weighted_price:.2f}")
        
        top_providers = oracle.get_top_providers(2)
        print("\nTop providers:")
        for provider in top_providers:
            print(f"{provider.name}: Reputation={provider.reputation_score:.2f}, "
                  f"Quality={provider.data_quality_score:.2f}, Stake={provider.stake:,}")
    except ValueError as e:
        print(f"Error: {e}")
```
