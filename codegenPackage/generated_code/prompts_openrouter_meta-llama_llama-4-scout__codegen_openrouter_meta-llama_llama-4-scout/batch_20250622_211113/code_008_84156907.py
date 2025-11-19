"""
Generated Code Metadata:
========================
Original URL: https://starknet.news
Prompt: "Design a simple smart contract on Starknet for a memecoin, explaining its functionality and deployment process."
Generated: DETERMINISTIC_8415690719061390
Batch ID: 20250622_211113
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://starknet-mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8545": {
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
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IERC20 } from "./IERC20.sol";
import { starknet } from "starknet";

// Define the Memecoin contract
contract Memecoin {
    // Mapping of balances
    mapping(address => uint256) public balances;

    // Mapping of allowances
    mapping(address => mapping(address => uint256)) public allowances;

    // Total supply of the memecoin
    uint256 public totalSupply;

    // Name and symbol of the memecoin
    string public name;
    string public symbol;

    // Event emitted when transfer occurs
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when approval occurs
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply) {
        // Initialize variables
        name = _name;
        symbol = _symbol;
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
    }

    // Function to get the balance of an account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Function to transfer memecoins
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to approve a spender
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Function to transfer from an account
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Insufficient allowance");
        require(balances[sender] >= amount, "Insufficient balance");
        allowances[sender][msg.sender] -= amount;
        balances[sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }
}

// Define the IERC20 interface
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```

To compile and deploy on Starknet, use:

```bash
# Install starknet-devnet and starknet-compile
pip install starknet-devnet starknet-compile

# Compile the contract
starknet-compile Memecoin.cairo --output compiled

# Run a local devnet
starknet-devnet --fork-url https://starknet-mainnet.infura.io/v3/YOUR_PROJECT_ID

# Deploy the contract
starknet deploy --contract compiled/Memecoin.json --network http://localhost:8545
```
