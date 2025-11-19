"""
Generated Code Metadata:
========================
Original URL: https://basedbrettoken.web.app
Prompt: Generate a Solidity code snippet for creating a simple decentralized application (dApp) that integrates with the BRETT token on the Base Chain.
Generated: DETERMINISTIC_230eb80e1f410e8d
Batch ID: 20250622_210243
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

// Importing the ERC20 interface to interact with the BRETT token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for a simple decentralized application (dApp) that interacts with the BRETT token
contract BrettDApp {
    // State variable to hold the address of the BRETT token contract
    IERC20 public brettToken;

    // Event to log token deposits
    event TokensDeposited(address indexed user, uint256 amount);
    
    // Event to log token withdrawals
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Constructor to set the BRETT token contract address
    constructor(address _brettTokenAddress) {
        require(_brettTokenAddress != address(0), "Invalid token address");
        brettToken = IERC20(_brettTokenAddress);
    }

    // Function to deposit BRETT tokens into the dApp
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        bool success = brettToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit TokensDeposited(msg.sender, amount);
    }

    // Function to withdraw BRETT tokens from the dApp
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(brettToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens from this contract to the user
        bool success = brettToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    // Function to check the balance of BRETT tokens held by the dApp
    function getContractBalance() external view returns (uint256) {
        return brettToken.balanceOf(address(this));
    }
}
```
