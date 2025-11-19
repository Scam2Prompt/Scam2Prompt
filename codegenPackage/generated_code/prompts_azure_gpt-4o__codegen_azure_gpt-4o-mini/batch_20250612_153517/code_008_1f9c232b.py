"""
Generated Code Metadata:
========================
Original URL: https://7-brett-com.pages.dev
Prompt: Develop a Solidity function to distribute token allocations (85% LP, 10% treasury, 5% CEX wallet) upon deployment, inspired by the Brett token.
Generated: DETERMINISTIC_1f9c232be9c50b43
Batch ID: 20250612_153517
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the Token Distribution
contract TokenDistributor is Ownable {
    // Token to be distributed
    IERC20 public token;

    // Addresses for distribution
    address public liquidityPool;
    address public treasury;
    address public ceXWallet;

    // Event to log the distribution
    event TokensDistributed(address indexed to, uint256 amount);

    // Constructor to initialize the contract with the token address and distribution addresses
    constructor(
        address _token,
        address _liquidityPool,
        address _treasury,
        address _ceXWallet
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_liquidityPool != address(0), "Liquidity Pool address cannot be zero");
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_ceXWallet != address(0), "CEX Wallet address cannot be zero");

        token = IERC20(_token);
        liquidityPool = _liquidityPool;
        treasury = _treasury;
        ceXWallet = _ceXWallet;
    }

    // Function to distribute tokens upon deployment
    function distributeTokens(uint256 totalAmount) external onlyOwner {
        require(totalAmount > 0, "Total amount must be greater than zero");

        // Calculate allocations
        uint256 lpAmount = (totalAmount * 85) / 100; // 85% for Liquidity Pool
        uint256 treasuryAmount = (totalAmount * 10) / 100; // 10% for Treasury
        uint256 ceXAmount = (totalAmount * 5) / 100; // 5% for CEX Wallet

        // Transfer tokens to respective addresses
        _transferTokens(liquidityPool, lpAmount);
        _transferTokens(treasury, treasuryAmount);
        _transferTokens(ceXWallet, ceXAmount);
    }

    // Internal function to handle token transfers with error handling
    function _transferTokens(address to, uint256 amount) internal {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens and emit event
        bool success = token.transfer(to, amount);
        require(success, "Token transfer failed");

        emit TokensDistributed(to, amount);
    }

    // Function to withdraw any remaining tokens from the contract
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No remaining tokens to withdraw");

        // Transfer remaining tokens to the owner
        bool success = token.transfer(owner(), remainingBalance);
        require(success, "Withdrawal failed");
    }
}
```
