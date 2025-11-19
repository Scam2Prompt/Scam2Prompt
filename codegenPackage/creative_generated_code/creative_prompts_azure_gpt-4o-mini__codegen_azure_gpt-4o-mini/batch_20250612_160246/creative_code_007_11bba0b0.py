"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-testnet20250216.pages.dev
Prompt: Provide an example of how to port an existing Ethereum smart contract to the Monad Testnet.
Generated: DETERMINISTIC_11bba0b098be93ec
Batch ID: 20250612_160246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Example Solidity contract to be ported to the Monad Testnet
contract ExampleToken {
    // State variables
    string public name; // Name of the token
    string public symbol; // Symbol of the token
    uint8 public decimals; // Number of decimals
    uint256 public totalSupply; // Total supply of the token

    // Mapping to track balances of addresses 
    mapping(address => uint256) public balances;

    // Event to log transfers
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor to initialize the token
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign the entire supply to the creator
    }

    // Function to transfer tokens
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address"); // Check for zero address
        require(balances[msg.sender] >= _value, "Insufficient balance"); // Check for sufficient balance

        balances[msg.sender] -= _value; // Deduct from sender's balance
        balances[_to] += _value; // Add to recipient's balance
        emit Transfer(msg.sender, _to, _value); // Emit transfer event
        return true; // Return a success flag
    }

    // Function to get the balance of an address
    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner]; // Return the balance of the requested address
    }
}

// Deployment script for the Monad Testnet
// This should be executed in a JavaScript environment like Hardhat or Truffle
async function main() {
    const ExampleToken = await ethers.getContractFactory("ExampleToken");

    // Deploy the contract with parameters
    const exampleToken = await ExampleToken.deploy("Example Token", "ETK", 18, 1000000);
    
    // Wait for the deployment to be mined
    await exampleToken.deployed();

    console.log("ExampleToken deployed to:", exampleToken.address);
}

// Error handling for script execution
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Error deploying contract:", error);
        process.exit(1);
    });
```

Make sure to adapt the deployment script to your specific environment and include any necessary configurations for connecting to the Monad Testnet.
