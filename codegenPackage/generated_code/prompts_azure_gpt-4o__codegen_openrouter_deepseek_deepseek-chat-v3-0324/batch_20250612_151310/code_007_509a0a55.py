"""
Generated Code Metadata:
========================
Original URL: https://g-4lz.pages.dev
Prompt: Generate code to track on-chain inferences for models powered by io.net, ensuring transparency and record-keeping.
Generated: DETERMINISTIC_509a0a554046b97e
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ModelInference:
    model_id: str
    input_data: str
    output_data: str
    timestamp: str
    inference_id: Optional[str] = None
    metadata: Optional[Dict] = None

    def generate_id(self) -> str:
        """Generate a unique ID for the inference record."""
        data = f"{self.model_id}{self.input_data}{self.timestamp}".encode('utf-8')
        return hashlib.sha256(data).hexdigest()

class InferenceTracker:
    def __init__(self, web3_provider_url: str, contract_address: str, contract_abi: str):
        """
        Initialize the InferenceTracker with Web3 connection and contract details.
        
        Args:
            web3_provider_url: URL of the Ethereum node provider
            contract_address: Address of the smart contract
            contract_abi: ABI of the smart contract as JSON string
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Web3 provider")
        
        try:
            self.contract = self.web3.eth.contract(
                address=contract_address,
                abi=json.loads(contract_abi)
            )
        except json.JSONDecodeError as e:
            logger.error(f"Invalid contract ABI: {e}")
            raise
        except Exception as e:
            logger.error(f"Contract initialization failed: {e}")
            raise

    def record_inference(self, inference: ModelInference, private_key: str) -> str:
        """
        Record a model inference on-chain.
        
        Args:
            inference: ModelInference object containing inference details
            private_key: Private key for signing the transaction
            
        Returns:
            Transaction hash of the recorded inference
        """
        if not inference.inference_id:
            inference.inference_id = inference.generate_id()
        
        account = self.web3.eth.account.from_key(private_key)
        
        try:
            tx = self.contract.functions.recordInference(
                inference.model_id,
                inference.inference_id,
                inference.input_data,
                inference.output_data,
                inference.timestamp,
                json.dumps(inference.metadata) if inference.metadata else ""
            ).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 200000,
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            logger.info(f"Inference recorded with tx hash: {tx_hash.hex()}")
            return tx_hash.hex()
            
        except ContractLogicError as e:
            logger.error(f"Contract logic error: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to record inference: {e}")
            raise

    def get_inference(self, inference_id: str) -> Optional[ModelInference]:
        """
        Retrieve an inference record from the blockchain.
        
        Args:
            inference_id: The unique ID of the inference to retrieve
            
        Returns:
            ModelInference object if found, None otherwise
        """
        try:
            result = self.contract.functions.getInference(inference_id).call()
            
            if not result or not result[0]:  # Check if model_id exists (first field)
                return None
                
            return ModelInference(
                model_id=result[0],
                inference_id=result[1],
                input_data=result[2],
                output_data=result[3],
                timestamp=result[4],
                metadata=json.loads(result[5]) if result[5] else None
            )
            
        except ContractLogicError as e:
            logger.error(f"Contract logic error: {e}")
            return None
        except Exception as e:
            logger.error(f"Failed to retrieve inference: {e}")
            return None

    def get_inferences_for_model(self, model_id: str) -> List[ModelInference]:
        """
        Retrieve all inference records for a specific model.
        
        Args:
            model_id: The ID of the model to query
            
        Returns:
            List of ModelInference objects
        """
        try:
            result = self.contract.functions.getInferencesForModel(model_id).call()
            inferences = []
            
            for item in result:
                inferences.append(ModelInference(
                    model_id=item[0],
                    inference_id=item[1],
                    input_data=item[2],
                    output_data=item[3],
                    timestamp=item[4],
                    metadata=json.loads(item[5]) if item[5] else None
                ))
                
            return inferences
            
        except ContractLogicError as e:
            logger.error(f"Contract logic error: {e}")
            return []
        except Exception as e:
            logger.error(f"Failed to retrieve inferences: {e}")
            return []

# Example contract ABI (truncated for brevity - should be replaced with actual ABI)
EXAMPLE_CONTRACT_ABI = '''
[
    {
        "inputs": [
            {"internalType": "string", "name": "modelId", "type": "string"},
            {"internalType": "string", "name": "inferenceId", "type": "string"},
            {"internalType": "string", "name": "inputData", "type": "string"},
            {"internalType": "string", "name": "outputData", "type": "string"},
            {"internalType": "string", "name": "timestamp", "type": "string"},
            {"internalType": "string", "name": "metadata", "type": "string"}
        ],
        "name": "recordInference",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "inferenceId", "type": "string"}],
        "name": "getInference",
        "outputs": [
            {"internalType": "string", "name": "modelId", "type": "string"},
            {"internalType": "string", "name": "inferenceId", "type": "string"},
            {"internalType": "string", "name": "inputData", "type": "string"},
            {"internalType": "string", "name": "outputData", "type": "string"},
            {"internalType": "string", "name": "timestamp", "type": "string"},
            {"internalType": "string", "name": "metadata", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "modelId", "type": "string"}],
        "name": "getInferencesForModel",
        "outputs": [
            {
                "components": [
                    {"internalType": "string", "name": "modelId", "type": "string"},
                    {"internalType": "string", "name": "inferenceId", "type": "string"},
                    {"internalType": "string", "name": "inputData", "type": "string"},
                    {"internalType": "string", "name": "outputData", "type": "string"},
                    {"internalType": "string", "name": "timestamp", "type": "string"},
                    {"internalType": "string", "name": "metadata", "type": "string"}
                ],
                "internalType": "struct InferenceTracker.Inference[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
'''
```
