"""
Generated Code Metadata:
========================
Original URL: https://btc-xmr-mixer.com
Prompt: Create a function that evaluates the best Bitcoin mixer based on user-defined parameters like security, fees, and supported cryptocurrencies, referencing features from Smartmixer and Chipmixer.
Generated: DETERMINISTIC_921277bd45fb2c4a
Batch ID: 20250612_155701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple

class BitcoinMixer:
    """
    A class to evaluate and compare Bitcoin mixers based on user-defined parameters.
    """
    
    def __init__(self):
        """
        Initialize with default mixer data (can be extended or loaded from external source).
        """
        self.mixers = {
            "Smartmixer": {
                "security": 9,
                "fees": 0.5,  # percentage
                "supported_cryptos": ["BTC", "ETH", "LTC"],
                "minimum_mix": 0.001,  # BTC
                "delay_hours": 6,
                "logs": False
            },
            "Chipmixer": {
                "security": 8,
                "fees": 0.7,
                "supported_cryptos": ["BTC", "BCH", "XMR"],
                "minimum_mix": 0.002,
                "delay_hours": 12,
                "logs": True
            }
        }
    
    def evaluate_mixers(
        self,
        security_weight: float = 0.4,
        fees_weight: float = 0.3,
        supported_cryptos_weight: float = 0.2,
        required_cryptos: Optional[List[str]] = None,
        min_security: int = 7,
        max_fee: float = 1.0
    ) -> List[Tuple[str, float]]:
        """
        Evaluate and rank mixers based on user-defined parameters.
        
        Args:
            security_weight: Importance of security (0 to 1).
            fees_weight: Importance of low fees (0 to 1).
            supported_cryptos_weight: Importance of supported cryptocurrencies (0 to 1).
            required_cryptos: List of cryptocurrencies the mixer must support.
            min_security: Minimum security score to consider.
            max_fee: Maximum fee percentage to consider.
            
        Returns:
            List of tuples (mixer_name, score) sorted by score descending.
        """
        if required_cryptos is None:
            required_cryptos = []
        
        valid_mixers = []
        
        for name, data in self.mixers.items():
            # Filter by minimum requirements
            if data["security"] < min_security or data["fees"] > max_fee:
                continue
                
            # Check if required cryptos are supported
            if required_cryptos and not all(
                crypto in data["supported_cryptos"] for crypto in required_cryptos
            ):
                continue
                
            # Calculate score components (normalized)
            security_score = data["security"] / 10 * security_weight
            fees_score = (1 - data["fees"] / max_fee) * fees_weight
            
            # Supported cryptos score based on how many required cryptos are supported
            if required_cryptos:
                crypto_score = (
                    sum(1 for crypto in required_cryptos if crypto in data["supported_cryptos"])
                    / len(required_cryptos)
                ) * supported_cryptos_weight
            else:
                crypto_score = (len(data["supported_cryptos"]) / 5) * supported_cryptos_weight
                
            total_score = security_score + fees_score + crypto_score
            valid_mixers.append((name, total_score))
        
        # Sort by score descending
        valid_mixers.sort(key=lambda x: x[1], reverse=True)
        return valid_mixers
    
    def get_mixer_details(self, mixer_name: str) -> Optional[Dict]:
        """
        Get detailed information about a specific mixer.
        
        Args:
            mixer_name: Name of the mixer to retrieve details for.
            
        Returns:
            Dictionary with mixer details if found, None otherwise.
        """
        return self.mixers.get(mixer_name)
    
    def add_mixer(self, name: str, data: Dict) -> None:
        """
        Add a new mixer to the evaluation pool.
        
        Args:
            name: Name of the new mixer.
            data: Dictionary containing mixer attributes.
        """
        required_fields = {
            "security", "fees", "supported_cryptos", 
            "minimum_mix", "delay_hours", "logs"
        }
        if not required_fields.issubset(data.keys()):
            raise ValueError("Missing required fields in mixer data")
            
        self.mixers[name] = data
    
    def save_mixers_to_file(self, filename: str) -> None:
        """
        Save current mixer data to a JSON file.
        
        Args:
            filename: Path to the output file.
        """
        with open(filename, 'w') as f:
            json.dump(self.mixers, f, indent=4)
    
    def load_mixers_from_file(self, filename: str) -> None:
        """
        Load mixer data from a JSON file.
        
        Args:
            filename: Path to the input file.
        """
        try:
            with open(filename, 'r') as f:
                self.mixers = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the input file")


# Example usage
if __name__ == "__main__":
    mixer_evaluator = BitcoinMixer()
    
    # Evaluate with custom parameters
    results = mixer_evaluator.evaluate_mixers(
        security_weight=0.5,
        fees_weight=0.3,
        supported_cryptos_weight=0.2,
        required_cryptos=["BTC", "ETH"],
        min_security=8,
        max_fee=0.8
    )
    
    print("Top mixers:")
    for name, score in results:
        print(f"{name}: {score:.2f}")
    
    # Get details for a specific mixer
    details = mixer_evaluator.get_mixer_details("Smartmixer")
    print("\nSmartmixer details:", details)
```
