"""
Generated Code Metadata:
========================
Original URL: https://43jeeil.pages.dev
Prompt: Recommend tools and libraries for developing and testing smart contracts on Scroll's zkEVM Layer 2. Include details on bytecode-level compatibility with Ethereum.
Generated: DETERMINISTIC_8a42eb432e9cb713
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scroll_zkevm_tools.py

from typing import List, Dict, Optional
import subprocess
import json
import os

class ScrollZkEVMToolkit:
    """
    A toolkit for developing and testing smart contracts on Scroll's zkEVM Layer 2.
    Provides recommendations for tools and checks bytecode compatibility with Ethereum.
    """
    
    def __init__(self):
        self.recommended_tools = {
            "development": [
                "Hardhat",
                "Foundry",
                "Truffle"
            ],
            "testing": [
                "Hardhat Tests",
                "Foundry Tests",
                "Waffle"
            ],
            "debugging": [
                "Hardhat Console",
                "Tenderly",
                "Scroll Debug Tools"
            ],
            "deployment": [
                "Hardhat Deploy",
                "Scroll CLI",
                "ThirdWeb Deploy"
            ],
            "verification": [
                "Scroll Block Explorer",
                "Etherscan-compatible Verifiers"
            ]
        }
        
        self.compatibility_checks = {
            "opcodes": {
                "supported": ["ADD", "MUL", "SUB", "DIV", "SDIV", "MOD", "SMOD", "ADDMOD", "MULMOD", "EXP", "SIGNEXTEND"],
                "unsupported": ["DIFFICULTY", "COINBASE", "TIMESTAMP", "NUMBER", "GASLIMIT", "CHAINID", "SELFBALANCE"]
            },
            "precompiles": {
                "supported": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                "unsupported": []
            }
        }
    
    def get_recommended_tools(self) -> Dict[str, List[str]]:
        """Return recommended tools for Scroll zkEVM development"""
        return self.recommended_tools
    
    def check_bytecode_compatibility(self, bytecode: str) -> Dict[str, bool]:
        """
        Check if bytecode contains any unsupported opcodes for Scroll zkEVM
        
        Args:
            bytecode: Compiled EVM bytecode to check
            
        Returns:
            Dictionary with compatibility information
        """
        result = {
            "is_compatible": True,
            "unsupported_opcodes": [],
            "unsupported_precompiles": []
        }
        
        # Convert bytecode to uppercase for case-insensitive comparison
        bytecode_upper = bytecode.upper()
        
        # Check for unsupported opcodes
        for opcode in self.compatibility_checks["opcodes"]["unsupported"]:
            if opcode in bytecode_upper:
                result["is_compatible"] = False
                result["unsupported_opcodes"].append(opcode)
        
        # Check for unsupported precompiles (represented by addresses)
        for precompile in self.compatibility_checks["precompiles"]["unsupported"]:
            precompile_addr = f"60{precompile:02x}6000526008601ff3"  # Typical precompile call pattern
            if precompile_addr in bytecode_upper:
                result["is_compatible"] = False
                result["unsupported_precompiles"].append(precompile)
        
        return result
    
    def verify_contract_on_scroll(self, contract_address: str, compiler_version: str, optimizer_runs: int, source_code: str) -> bool:
        """
        Verify a contract on Scroll's block explorer (simulated)
        
        Args:
            contract_address: Address of deployed contract
            compiler_version: Solidity compiler version used
            optimizer_runs: Optimization runs setting
            source_code: Contract source code
            
        Returns:
            bool: True if verification succeeds
        """
        try:
            # In a real implementation, this would call Scroll's verification API
            print(f"Verifying contract {contract_address} with compiler {compiler_version}")
            print("Source code verified successfully on Scroll")
            return True
        except Exception as e:
            print(f"Verification failed: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    toolkit = ScrollZkEVMToolkit()
    
    # Get recommended tools
    print("Recommended Tools:")
    print(json.dumps(toolkit.get_recommended_tools(), indent=2))
    
    # Check bytecode compatibility
    sample_bytecode = "6080604052348015600f57600080fd5b506004361060325760003560e01c80632096525514603757806355241077146053575b600080fd5b603d6069565b6040518082815260200191505060405180910390f35b6059606f565b6040518082815260200191505060405180910390f35b60005481565b6000805490509056fea2646970667358221220b7c17a1e8eabf1b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b
