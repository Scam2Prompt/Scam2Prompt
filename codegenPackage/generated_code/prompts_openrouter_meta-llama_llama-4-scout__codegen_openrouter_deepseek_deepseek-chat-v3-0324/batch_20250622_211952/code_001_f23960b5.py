"""
Generated Code Metadata:
========================
Original URL: https://hyperliquid.how
Prompt: Compare the features of Hyperliquid's HyperBFT consensus algorithm with other blockchain consensus algorithms in terms of transaction speed and security.
Generated: DETERMINISTIC_f23960b5b696a27c
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Tuple

class ConsensusAlgorithm:
    """Base class for consensus algorithms with common attributes and methods."""
    
    def __init__(self, name: str, tps: int, security_level: str):
        """
        Initialize consensus algorithm with name, transactions per second (tps), and security level.
        
        Args:
            name: Name of the consensus algorithm.
            tps: Transactions per second supported.
            security_level: Security level (e.g., "high", "medium", "low").
        """
        self.name = name
        self.tps = tps
        self.security_level = security_level
    
    def to_dict(self) -> Dict:
        """Convert the algorithm's attributes to a dictionary."""
        return {
            "name": self.name,
            "tps": self.tps,
            "security_level": self.security_level
        }

class ConsensusComparator:
    """Compares different consensus algorithms based on transaction speed and security."""
    
    def __init__(self):
        """Initialize with a list of consensus algorithms."""
        self.algorithms = [
            ConsensusAlgorithm("HyperBFT", 100000, "high"),
            ConsensusAlgorithm("PoW (Bitcoin)", 7, "high"),
            ConsensusAlgorithm("PoS (Ethereum 2.0)", 1000, "high"),
            ConsensusAlgorithm("DPoS (EOS)", 4000, "medium"),
            ConsensusAlgorithm("PBFT", 1000, "high"),
            ConsensusAlgorithm("Tendermint", 10000, "high")
        ]
    
    def compare_tps(self) -> List[Dict]:
        """
        Compare algorithms based on transactions per second (tps).
        
        Returns:
            List of algorithms sorted by tps in descending order.
        """
        sorted_algorithms = sorted(
            self.algorithms,
            key=lambda x: x.tps,
            reverse=True
        )
        return [alg.to_dict() for alg in sorted_algorithms]
    
    def compare_security(self) -> List[Dict]:
        """
        Compare algorithms based on security level.
        
        Returns:
            List of algorithms sorted by security level (high to low).
        """
        security_rank = {"high": 3, "medium": 2, "low": 1}
        sorted_algorithms = sorted(
            self.algorithms,
            key=lambda x: security_rank[x.security_level],
            reverse=True
        )
        return [alg.to_dict() for alg in sorted_algorithms]
    
    def get_comparison_report(self) -> Dict:
        """
        Generate a comprehensive comparison report.
        
        Returns:
            Dictionary containing tps and security comparisons.
        """
        return {
            "tps_comparison": self.compare_tps(),
            "security_comparison": self.compare_security()
        }

def main():
    """Main function to execute the comparison and print results."""
    try:
        comparator = ConsensusComparator()
        report = comparator.get_comparison_report()
        
        print("Consensus Algorithms Comparison Report:")
        print("\nTransaction Speed (TPS) Comparison:")
        print(json.dumps(report["tps_comparison"], indent=2))
        
        print("\nSecurity Level Comparison:")
        print(json.dumps(report["security_comparison"], indent=2))
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
