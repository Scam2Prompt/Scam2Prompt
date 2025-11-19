"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-io.pages.dev
Prompt: Write a tutorial on how to create a decentralized finance (DeFi) application that leverages the RACA token for liquidity provision on the BNB Chain.
Generated: DETERMINISTIC_d88eb570fe4eaffe
Batch ID: 20250612_155125
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
 * @title Decentralized Finance (DeFi) Liquidity Provision Application
 * @dev This contract allows users to provide liquidity using the RACA token
 *      on the BNB Chain. It includes methods for depositing, withdrawing, 
 *      and checking liquidity balances.
 */

// Importing necessary interfaces for interacting with ERC20 tokens.
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract LiquidityProvision {
    // Address of the RACA token contract on the BNB Chain
    address public immutable racaToken;

    // Mapping to track liquidity provided by each user
    mapping(address => uint256) public liquidityBalances;

    // Total liquidity pool balance
    uint256 public totalLiquidity;

    // Event emitted when liquidity is deposited
    event LiquidityDeposited(address indexed user, uint256 amount);

    // Event emitted when liquidity is withdrawn
    event LiquidityWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Sets the RACA token address during contract deployment.
     * @param _racaToken Address of the RACA token contract.
     */
    constructor(address _racaToken) {
        require(_racaToken != address(0), "Invalid token address");
        racaToken = _racaToken;
    }

    /**
     * @dev Deposit RACA tokens into the liquidity pool.
     * @param amount Amount of RACA tokens to deposit.
     */
    function depositLiquidity(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer RACA tokens from the user to the contract
        bool success = IERC20(racaToken).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user's liquidity balance and the total liquidity pool balance
        liquidityBalances[msg.sender] += amount;
        totalLiquidity += amount;

        // Emit an event for the deposit
        emit LiquidityDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw RACA tokens from the liquidity pool.
     * @param amount Amount of RACA tokens to withdraw.
     */
    function withdrawLiquidity(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(liquidityBalances[msg.sender] >= amount, "Insufficient liquidity balance");

        // Update user's liquidity balance and the total liquidity pool balance
        liquidityBalances[msg.sender] -= amount;
        totalLiquidity -= amount;

        // Transfer RACA tokens from the contract to the user
        bool success = IERC20(racaToken).transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit an event for the withdrawal
        emit LiquidityWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the liquidity balance of a specific user.
     * @param user Address of the user.
     * @return The liquidity balance of the user.
     */
    function getLiquidityBalance(address user) external view returns (uint256) {
        return liquidityBalances[user];
    }

    /**
     * @dev Get the total liquidity in the pool.
     * @return The total liquidity balance.
     */
    function getTotalLiquidity() external view returns (uint256) {
        return totalLiquidity;
    }
}
```
