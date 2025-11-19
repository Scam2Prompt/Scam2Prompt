"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-etuktuk-io.pages.dev
Prompt: Write a smart contract function to withdraw staked $TUK tokens, ensuring gas fees are covered and smart contracts are approved, based on the eTukTuk guidelines.
Generated: DETERMINISTIC_b3e2d23eb0c2dcd1
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

/**
 * @title eTukTuk Stake Withdrawal Smart Contract
 * @dev This contract allows users to withdraw staked $TUK tokens while ensuring gas fees are covered and required approvals are in place.
 */
contract ETukTukStakeWithdrawal {
    IERC20 public tukToken; // Reference to the $TUK token contract
    mapping(address => uint256) public stakedBalances; // Tracks staked amounts per user

    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Sets the $TUK token address during contract deployment.
     * @param _tukToken Address of the $TUK token contract.
     */
    constructor(address _tukToken) {
        require(_tukToken != address(0), "Invalid token contract address");
        tukToken = IERC20(_tukToken);
    }

    /**
     * @dev Withdraw staked tokens for the caller.
     * Ensures sufficient balance and proper approvals.
     * Gas fees are factored by the caller.
     */
    function withdrawStakedTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero"); // Check for valid withdrawal amount
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance"); // Check user's staked balance

        // Update staked balance before transferring tokens to prevent reentrancy attacks
        stakedBalances[msg.sender] -= amount;

        // Transfer the tokens back to the caller
        bool success = tukToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount); // Emit event for successful withdrawal
    }

    /**
     * @dev Stake tokens (not part of the withdrawal function but required for completeness).
     * @param amount The number of $TUK tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero"); // Check for valid deposit amount

        // Transfer tokens from the user to the contract
        bool success = tukToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's staked balance
        stakedBalances[msg.sender] += amount;
    }
}

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
