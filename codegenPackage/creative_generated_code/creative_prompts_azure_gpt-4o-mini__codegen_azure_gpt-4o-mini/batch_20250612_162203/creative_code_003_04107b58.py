"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bengonbase-xyz.pages.dev
Prompt: How can I create a smart contract that interacts with the $BENG token on the Base blockchain?
Generated: DETERMINISTIC_04107b5853e2975d
Batch ID: 20250612_162203
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

// Importing the Interface for ERC20 Tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract to interact with the $BENG token
contract BengTokenInteraction {
    // State variables
    IERC20 public bengToken; // Instance of the $BENG token contract
    address public owner; // Owner of the contract

    // Events
    event TokensDeposited(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the $BENG token address
    constructor(address _bengTokenAddress) {
        require(_bengTokenAddress != address(0), "Invalid token address");
        bengToken = IERC20(_bengTokenAddress);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to deposit $BENG tokens into the contract
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        bool success = bengToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit TokensDeposited(msg.sender, amount);
    }

    // Function to withdraw $BENG tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(bengToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens from this contract to the owner
        bool success = bengToken.transfer(owner, amount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(owner, amount);
    }

    // Function to check the contract's balance of $BENG tokens
    function getContractTokenBalance() external view returns (uint256) {
        return bengToken.balanceOf(address(this));
    }
}
```
