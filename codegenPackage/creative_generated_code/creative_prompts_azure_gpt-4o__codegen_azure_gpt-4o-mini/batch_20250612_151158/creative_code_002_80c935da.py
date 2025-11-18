"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gainssatoshi.pages.dev
Prompt: Provide an example of how to use ZK Rollup fraud proofs in SatoshiVM to validate off-chain computations and submit validity proofs to Bitcoin.
Generated: DETERMINISTIC_80c935da363f9082
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from typing import Any, Dict, Tuple

class ZKRollup:
    def __init__(self, blockchain: str):
        """
        Initialize the ZK Rollup with a given blockchain.
        
        :param blockchain: The blockchain where the rollup will be submitted (e.g., Bitcoin).
        """
        self.blockchain = blockchain

    def compute_hash(self, data: Dict[str, Any]) -> str:
        """
        Compute the SHA-256 hash of the given data.

        :param data: The data to compute the hash for.
        :return: Hexadecimal string representation of the hash.
        """
        data_string = json.dumps(data, sort_keys=True).encode('utf-8')
        return hashlib.sha256(data_string).hexdigest()

    def validate_off_chain_computation(self, computation_result: Any, expected_result: Any) -> bool:
        """
        Validate the off-chain computation result against the expected result.

        :param computation_result: The result from the off-chain computation.
        :param expected_result: The expected result to validate against.
        :return: True if the results match, else False.
        """
        return computation_result == expected_result

    def create_fraud_proof(self, computation_data: Dict[str, Any], invalid_result: Any) -> str:
        """
        Create a fraud proof for invalid off-chain computations.

        :param computation_data: The data used in the computation.
        :param invalid_result: The result that is deemed invalid.
        :return: A fraud proof hash.
        """
        proof_data = {
            'computation_data': computation_data,
            'invalid_result': invalid_result
        }
        return self.compute_hash(proof_data)

    def submit_validity_proof(self, proof: str) -> None:
        """
        Submit the validity proof to the specified blockchain.

        :param proof: The fraud proof to submit.
        """
        try:
            # In a real implementation, this would interact with the blockchain API
            # For demonstration, we'll just print the proof
            print(f"Submitting proof to {self.blockchain}: {proof}")
            # Example: blockchain_api.submit_proof(self.blockchain, proof)
        except Exception as e:
            print(f"Error submitting proof: {e}")

# Example usage
if __name__ == "__main__":
    zk_rollup = ZKRollup(blockchain="Bitcoin")
    
    # Sample computation and expected result
    computation_data = {"input": [1, 2, 3], "operation": "sum"}
    computation_result = sum(computation_data["input"])  # Simulating an off-chain computation
    expected_result = 6  # Expected result for the sum operation
    
    # Validate the computation result
    if zk_rollup.validate_off_chain_computation(computation_result, expected_result):
        print("Computation is valid.")
    else:
        invalid_result = computation_result
        fraud_proof = zk_rollup.create_fraud_proof(computation_data, invalid_result)
        zk_rollup.submit_validity_proof(fraud_proof)
```
