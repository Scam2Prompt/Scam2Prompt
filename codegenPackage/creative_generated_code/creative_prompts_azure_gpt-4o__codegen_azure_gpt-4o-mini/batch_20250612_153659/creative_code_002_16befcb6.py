"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helripairdrop.web.app
Prompt: Generate a smart contract in Solidity or Rust to facilitate payments for a project like "$RIP coin" on the Solana blockchain.
Generated: DETERMINISTIC_16befcb61cbf0734
Batch ID: 20250612_153659
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $RIP coin token on Ethereum
contract RIPCoin is ERC20, Ownable {
    // Event to log transfers
    event PaymentReceived(address indexed from, uint256 amount);
    
    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("RIP Coin", "$RIP") {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract deployer
    }

    // Function to facilitate payments to the project
    function pay() external payable {
        require(msg.value > 0, "Payment must be greater than zero");
        emit PaymentReceived(msg.sender, msg.value); // Emit event for logging
        
        // Optionally, you can transfer some tokens to the payer as a reward
        uint256 tokensToMint = msg.value; // Define the token amount to mint based on payment
        _mint(msg.sender, tokensToMint); // Mint tokens to the payer
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance; // Get the contract's ETH balance
        require(contractBalance > 0, "No funds to withdraw");
        payable(owner()).transfer(contractBalance); // Transfer the balance to the owner's address
    }

    // Function to retrieve the contract's ETH balance
    function getBalance() external view returns (uint256) {
        return address(this).balance; // Return the ETH balance of the contract
    }
}
```

### Note:
Ensure to install OpenZeppelin contracts by adding the following in your project:
```bash
npm install @openzeppelin/contracts
```
