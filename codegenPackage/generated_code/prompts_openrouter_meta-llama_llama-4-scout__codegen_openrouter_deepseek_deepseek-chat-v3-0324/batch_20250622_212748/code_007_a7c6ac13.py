"""
Generated Code Metadata:
========================
Original URL: https://claimhyperlane.foundation
Prompt: What are the key differences in the token claim process for EVM/SVM users versus Cosmos Ecosystem users, and how is this reflected in the Hyperlane protocol?
Generated: DETERMINISTIC_a7c6ac135206a9c6
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hyperlane_token_claim.py

from enum import Enum
from typing import Union, Dict, Any
from dataclasses import dataclass
from web3 import Web3
from cosmpy.aerial.client import LedgerClient
from cosmpy.aerial.wallet import LocalWallet
from hyperlane import HyperlaneSDK

class ChainType(Enum):
    """Enum representing different blockchain types"""
    EVM = 1
    SVM = 2
    COSMOS = 3

@dataclass
class TokenClaimParams:
    """Dataclass for token claim parameters"""
    chain_type: ChainType
    recipient_address: str
    amount: int
    claim_id: str
    signature: str = None

class TokenClaimProcessor:
    """Handles token claims across different blockchain ecosystems"""
    
    def __init__(self, hyperlane_sdk: HyperlaneSDK):
        self.hyperlane_sdk = hyperlane_sdk
    
    def _validate_evm_svm_claim(self, params: TokenClaimParams) -> bool:
        """Validate EVM/SVM claim parameters"""
        if params.chain_type not in (ChainType.EVM, ChainType.SVM):
            raise ValueError("Invalid chain type for EVM/SVM claim")
        
        if not Web3.is_address(params.recipient_address):
            raise ValueError("Invalid EVM/SVM recipient address")
        
        if params.signature is None:
            raise ValueError("Signature required for EVM/SVM claim")
        
        return True
    
    def _validate_cosmos_claim(self, params: TokenClaimParams) -> bool:
        """Validate Cosmos claim parameters"""
        if params.chain_type != ChainType.COSMOS:
            raise ValueError("Invalid chain type for Cosmos claim")
        
        try:
            LedgerClient.validate_address(params.recipient_address)
        except Exception as e:
            raise ValueError(f"Invalid Cosmos recipient address: {str(e)}")
        
        return True
    
    def process_claim(self, params: TokenClaimParams) -> Dict[str, Any]:
        """Process token claim based on chain type"""
        try:
            if params.chain_type in (ChainType.EVM, ChainType.SVM):
                self._validate_evm_svm_claim(params)
                # EVM/SVM specific claim logic
                tx_hash = self.hyperlane_sdk.claim_tokens(
                    recipient=params.recipient_address,
                    amount=params.amount,
                    claim_id=params.claim_id,
                    signature=params.signature
                )
                return {"status": "success", "tx_hash": tx_hash}
            
            elif params.chain_type == ChainType.COSMOS:
                self._validate_cosmos_claim(params)
                # Cosmos specific claim logic
                tx = self.hyperlane_sdk.claim_tokens_cosmos(
                    recipient=params.recipient_address,
                    amount=params.amount,
                    claim_id=params.claim_id
                )
                return {"status": "success", "tx_hash": tx.tx_hash}
            
            else:
                raise ValueError("Unsupported chain type")
        
        except Exception as e:
            return {"status": "error", "message": str(e)}
```
