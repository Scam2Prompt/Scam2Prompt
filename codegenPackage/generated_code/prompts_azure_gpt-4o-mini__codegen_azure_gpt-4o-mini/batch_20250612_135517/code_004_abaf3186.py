"""
Generated Code Metadata:
========================
Original URL: https://celestia.farm
Prompt: Provide an example of a smart contract that utilizes Celestia's unique capabilities for scalability.
Generated: DETERMINISTIC_abaf3186211c9216
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary libraries for Celestia integration
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for a simple token that utilizes Celestia's scalability features
contract CelestiaToken is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Event emitted when tokens are transferred
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);

    // Mapping from address to balance
    mapping(address => uint256) private balances;

    // Total supply of the token
    uint256 private totalSupply;

    // Counter for token IDs (if needed for future features)
    Counters.Counter private tokenIdCounter;

    // Constructor to initialize the total supply
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = initialSupply;
        balances[msg.sender] = initialSupply; // Assign initial supply to the contract owner
    }

    // Function to mint new tokens
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        totalSupply += amount;
        balances[to] += amount;

        emit TokensMinted(to, amount);
    }

    // Function to transfer tokens
    function transferTokens(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit TokensTransferred(msg.sender, to, amount);
    }

    // Function to get the balance of an address
    function balanceOf(address account) external view returns (uint256) {
        require(account != address(0), "Cannot query the zero address");
        return balances[account];
    }

    // Function to get the total supply of tokens
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }
}
```
