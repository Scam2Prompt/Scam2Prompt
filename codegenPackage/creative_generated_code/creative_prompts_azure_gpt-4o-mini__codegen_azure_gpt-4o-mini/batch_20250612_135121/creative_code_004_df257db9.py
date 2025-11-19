"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-feature-vercel-audience-419labs.vercel.app
Prompt: Provide an example of a smart contract that integrates with services in the StarkNet ecosystem.
Generated: DETERMINISTIC_df257db95296f527
Batch ID: 20250612_135121
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title StarkNetIntegration
/// @notice A smart contract to integrate with the StarkNet ecosystem for token management
contract StarkNetIntegration is Ownable {
    // Event to log token deposits
    event TokensDeposited(address indexed user, uint256 amount);
    // Event to log token withdrawals
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Address of the ERC20 token to interact with
    IERC20 public token;

    /// @notice Constructor to set the token address
    /// @param _token Address of the ERC20 token contract
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    /// @notice Deposit tokens into the contract
    /// @param amount The amount of tokens to deposit
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update user balance
        balances[msg.sender] += amount;

        // Emit deposit event
        emit TokensDeposited(msg.sender, amount);
    }

    /// @notice Withdraw tokens from the contract
    /// @param amount The amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);

        // Emit withdrawal event
        emit TokensWithdrawn(msg.sender, amount);
    }

    /// @notice Get the balance of tokens for a specific user
    /// @param user The address of the user
    /// @return The token balance of the user
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /// @notice Emergency function to withdraw tokens from the contract by the owner
    /// @param amount The amount of tokens to withdraw
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        token.transfer(owner(), amount);
    }
}
```
