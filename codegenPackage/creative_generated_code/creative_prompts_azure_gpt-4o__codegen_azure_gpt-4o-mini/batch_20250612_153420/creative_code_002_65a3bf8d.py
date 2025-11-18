"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origin-usd.com
Prompt: Generate code to convert Ethereum-based tokens to Origin USD (OUSD) using a smart contract.
Generated: DETERMINISTIC_65a3bf8d64b3744f
Batch ID: 20250612_153420
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

// Import the ERC20 interface for interacting with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the contract for converting Ethereum-based tokens to Origin USD (OUSD)
contract TokenConverter {
    // Declare state variables
    IERC20 public ousdToken;  // The OUSD token contract
    address public owner;      // Owner of the contract

    // Events for logging conversions
    event TokenConverted(address indexed user, address indexed token, uint256 amount, uint256 ousdAmount);

    // Constructor to set the OUSD token address
    constructor(address _ousdToken) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        ousdToken = IERC20(_ousdToken);
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to convert a specified token to OUSD
    function convertToken(address tokenAddress, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tokenAddress != address(0), "Invalid token address");

        IERC20 token = IERC20(tokenAddress);
        
        // Transfer the tokens from the sender to this contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Calculate the OUSD amount based on a simple exchange rate (1:1 for demonstration)
        uint256 ousdAmount = amount; // Adjust this logic based on actual exchange rate

        // Transfer OUSD to the user
        success = ousdToken.transfer(msg.sender, ousdAmount);
        require(success, "OUSD transfer failed");

        // Emit the conversion event
        emit TokenConverted(msg.sender, tokenAddress, amount, ousdAmount);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(tokenAddress != address(0), "Invalid token address");
        
        IERC20 token = IERC20(tokenAddress);
        uint256 contractBalance = token.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient balance in contract");
        
        // Transfer the specified amount of tokens to the owner
        bool success = token.transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }

    // Function to allow the owner to change the OUSD token address
    function setOUSDToken(address _ousdToken) external onlyOwner {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        ousdToken = IERC20(_ousdToken);
    }
}
```
