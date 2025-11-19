"""
Generated Code Metadata:
========================
Original URL: https://suifoundation.com
Prompt: Explain how to use Sui's Nautilus feature for verifiable offchain compute in a decentralized application, and provide example code.
Generated: DETERMINISTIC_d6bc6514d4046994
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.testnet.sui.io:443": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example demonstrating Sui's Nautilus feature for verifiable offchain compute.
"""

from typing import List, Tuple, Optional
import hashlib
import json
from dataclasses import dataclass
import sui_bindings as sui  # Hypothetical Sui SDK

@dataclass
class ComputeRequest:
    """Request for offchain computation."""
    input_data: bytes
    callback_address: str  # Sui address for result callback
    gas_budget: int

@dataclass
class ComputeResult:
    """Result of offchain computation."""
    request_id: bytes
    output_data: bytes
    proof: bytes  # Cryptographic proof of computation

class NautilusClient:
    """Client for interacting with Sui's Nautilus feature."""
    
    def __init__(self, sui_client: sui.Client):
        self.client = sui_client
    
    def submit_compute_request(
        self,
        input_data: bytes,
        callback_address: str,
        gas_budget: int = 1000000
    ) -> bytes:
        """Submit a computation request to Nautilus.
        
        Args:
            input_data: Input data for computation
            callback_address: Sui address to receive result
            gas_budget: Maximum gas budget for the transaction
            
        Returns:
            Request ID for tracking the computation
        """
        request = ComputeRequest(
            input_data=input_data,
            callback_address=callback_address,
            gas_budget=gas_budget
        )
        
        tx = sui.Transaction()
        tx.move_call(
            "0x2::nautilus::submit",
            type_arguments=[],
            arguments=[
                sui.vector(list(request.input_data)),
                sui.pure(request.callback_address),
                sui.pure(request.gas_budget)
            ]
        )
        
        tx_response = self.client.execute_tx(tx)
        if not tx_response.success:
            raise RuntimeError(f"Transaction failed: {tx_response.error}")
        
        # Extract request ID from events
        for event in tx_response.events:
            if event.type == "NautilusRequestEvent":
                return bytes.fromhex(event.data["request_id"])
        
        raise RuntimeError("No request ID found in transaction events")
    
    def verify_compute_result(self, result: ComputeResult) -> bool:
        """Verify a computation result using Nautilus.
        
        Args:
            result: Computation result to verify
            
        Returns:
            True if verification succeeds, False otherwise
        """
        tx = sui.Transaction()
        tx.move_call(
            "0x2::nautilus::verify",
            type_arguments=[],
            arguments=[
                sui.vector(list(result.request_id)),
                sui.vector(list(result.output_data)),
                sui.vector(list(result.proof))
            ]
        )
        
        tx_response = self.client.execute_tx(tx)
        return tx_response.success

class ExampleDApp:
    """Example DApp using Nautilus for offchain compute."""
    
    def __init__(self, nautilus_client: NautilusClient):
        self.client = nautilus_client
    
    def process_data_offchain(self, data: List[int]) -> Tuple[bool, Optional[List[int]]]:
        """Example method using Nautilus for verifiable offchain computation."""
        try:
            # Prepare input data
            input_bytes = json.dumps({"data": data}).encode()
            
            # Submit computation request
            request_id = self.client.submit_compute_request(
                input_data=input_bytes,
                callback_address="0x123...abc"  # Your Sui address
            )
            
            # In a real app, you'd wait for callback or poll for result
            # Here we simulate getting a result
            output_data = self._simulate_compute(input_bytes)
            proof = self._generate_proof(input_bytes, output_data)
            
            result = ComputeResult(
                request_id=request_id,
                output_data=output_data,
                proof=proof
            )
            
            # Verify the result
            if self.client.verify_compute_result(result):
                output = json.loads(output_data.decode())
                return True, output["result"]
            return False, None
            
        except Exception as e:
            print(f"Error in offchain computation: {e}")
            return False, None
    
    def _simulate_compute(self, input_data: bytes) -> bytes:
        """Simulate offchain computation (would be done by Nautilus workers)."""
        input_obj = json.loads(input_data.decode())
        result = [x * 2 for x in input_obj["data"]]  # Simple computation
        return json.dumps({"result": result}).encode()
    
    def _generate_proof(self, input_data: bytes, output_data: bytes) -> bytes:
        """Simulate proof generation (would be done by Nautilus)."""
        # In reality, this would be a proper cryptographic proof
        h = hashlib.sha256()
        h.update(input_data)
        h.update(output_data)
        return h.digest()

# Example usage
if __name__ == "__main__":
    sui_client = sui.Client("https://fullnode.testnet.sui.io:443")
    nautilus_client = NautilusClient(sui_client)
    dapp = ExampleDApp(nautilus_client)
    
    success, result = dapp.process_data_offchain([1, 2, 3, 4, 5])
    if success:
        print(f"Computation result: {result}")
    else:
        print("Computation failed")
```
