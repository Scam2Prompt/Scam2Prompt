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
from dataclasses import dataclass
from enum import Enum
from typing import List

class BitcoinMixer:
    def __init__(self, name: str, security: int, fees: float, supported_cryptocurrencies: List[str]):
        self.name = name
        self.security = security
        self.fees = fees
        self.supported_cryptocurrencies = supported_cryptocurrencies

@dataclass
class MixerFeatures:
    security: int
    fees: float
    supported_cryptocurrencies: List[str]

class MixerName(str, Enum):
    SMARTMIXER = "Smartmixer"
    CHIPMIXER = "Chipmixer"

def evaluate_bitcoin_mixer(
    security_weight: int, 
    fees_weight: int, 
    cryptocurrency: str, 
    mixers: List[MixerFeatures]
) -> str:
    """
    Evaluates the best Bitcoin mixer based on user-defined parameters.

    Args:
    - security_weight (int): The weight of security in the evaluation (1-10).
    - fees_weight (int): The weight of fees in the evaluation (1-10).
    - cryptocurrency (str): The cryptocurrency to be mixed.
    - mixers (List[MixerFeatures]): A list of mixer features.

    Returns:
    - str: The name of the best Bitcoin mixer.

    Raises:
    - ValueError: If the weights are not between 1 and 10.
    - ValueError: If the cryptocurrency is not supported by any mixer.
    """

    if not (1 <= security_weight <= 10 and 1 <= fees_weight <= 10):
        raise ValueError("Weights must be between 1 and 10")

    best_mixer: str = ""
    best_score: float = 0.0

    for mixer in mixers:
        if cryptocurrency not in mixer.supported_cryptocurrencies:
            continue

        score: float = (mixer.security * security_weight / 10) - (mixer.fees * fees_weight / 100)
        if score > best_score:
            best_score = score
            best_mixer = MixerName.SMARTMIXER if mixer == mixers[0] else MixerName.CHIPMIXER

    if not best_mixer:
        raise ValueError("No mixer supports the specified cryptocurrency")

    return best_mixer


def main():
    smartmixer_features = MixerFeatures(
        security=9, 
        fees=2.5, 
        supported_cryptocurrencies=["Bitcoin", "Ethereum"]
    )

    chipmixer_features = MixerFeatures(
        security=8, 
        fees=1.5, 
        supported_cryptocurrencies=["Bitcoin", "Litecoin"]
    )

    mixers = [smartmixer_features, chipmixer_features]

    try:
        best_mixer = evaluate_bitcoin_mixer(
            security_weight=8, 
            fees_weight=2, 
            cryptocurrency="Bitcoin", 
            mixers=mixers
        )
        print(f"The best Bitcoin mixer is: {best_mixer}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
