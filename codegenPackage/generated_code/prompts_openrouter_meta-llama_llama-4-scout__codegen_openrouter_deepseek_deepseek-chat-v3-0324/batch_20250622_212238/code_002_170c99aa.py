"""
Generated Code Metadata:
========================
Original URL: https://azt3c-st.webflow.io
Prompt: "Describe the process of building and testing a private smart contract on Aztec's sandbox environment."
Generated: DETERMINISTIC_170c99aac718e41c
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from aztec_sandbox import AztecSandbox, ContractCompiler, ContractDeployer, TestRunner
import os
import json
from typing import Dict, Any

# Initialize constants
CONTRACT_SOURCE_FILE = "private_contract.aztec"
CONFIG_FILE = "sandbox_config.json"
TEST_FILE = "test_contract.py"

class AztecPrivateContractBuilder:
    """
    A class to handle building, deploying, and testing private smart contracts on Aztec's sandbox environment.
    """
    
    def __init__(self):
        """
        Initialize the Aztec sandbox environment and required components.
        """
        self.sandbox = AztecSandbox()
        self.compiler = ContractCompiler()
        self.deployer = ContractDeployer(self.sandbox)
        self.test_runner = TestRunner(self.sandbox)
        
    def load_config(self) -> Dict[str, Any]:
        """
        Load configuration from JSON file.
        
        Returns:
            Dict[str, Any]: Configuration dictionary
        """
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file {CONFIG_FILE} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in config file {CONFIG_FILE}")
    
    def compile_contract(self) -> str:
        """
        Compile the Aztec private contract.
        
        Returns:
            str: Compiled contract bytecode
        """
        if not os.path.exists(CONTRACT_SOURCE_FILE):
            raise FileNotFoundError(f"Contract source file {CONTRACT_SOURCE_FILE} not found")
            
        try:
            with open(CONTRACT_SOURCE_FILE, 'r') as f:
                source_code = f.read()
            return self.compiler.compile(source_code)
        except Exception as e:
            raise RuntimeError(f"Contract compilation failed: {str(e)}")
    
    def deploy_contract(self, bytecode: str) -> str:
        """
        Deploy the compiled contract to Aztec sandbox.
        
        Args:
            bytecode (str): Compiled contract bytecode
            
        Returns:
            str: Contract address
        """
        try:
            config = self.load_config()
            return self.deployer.deploy(
                bytecode=bytecode,
                private_key=config["private_key"],
                chain_id=config["chain_id"]
            )
        except Exception as e:
            raise RuntimeError(f"Contract deployment failed: {str(e)}")
    
    def run_tests(self, contract_address: str) -> bool:
        """
        Run tests against the deployed contract.
        
        Args:
            contract_address (str): Address of the deployed contract
            
        Returns:
            bool: True if all tests pass, False otherwise
        """
        if not os.path.exists(TEST_FILE):
            raise FileNotFoundError(f"Test file {TEST_FILE} not found")
            
        try:
            return self.test_runner.run_tests(
                test_file=TEST_FILE,
                contract_address=contract_address
            )
        except Exception as e:
            raise RuntimeError(f"Test execution failed: {str(e)}")
    
    def build_and_test(self) -> bool:
        """
        Main method to compile, deploy and test the contract.
        
        Returns:
            bool: True if all steps succeed, False otherwise
        """
        try:
            print("Compiling contract...")
            bytecode = self.compile_contract()
            
            print("Deploying contract...")
            contract_address = self.deploy_contract(bytecode)
            print(f"Contract deployed at: {contract_address}")
            
            print("Running tests...")
            test_result = self.run_tests(contract_address)
            
            if test_result:
                print("All tests passed!")
            else:
                print("Some tests failed")
                
            return test_result
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    builder = AztecPrivateContractBuilder()
    success = builder.build_and_test()
    exit(0 if success else 1)
```
