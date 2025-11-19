"""
Generated Code Metadata:
========================
Original URL: https://zachetpedagog.ru
Prompt: Develop a smart contract to participate in liquidity farming on Saddle Finance.
Generated: DETERMINISTIC_dd115c1fd03609f6
Batch ID: 20250622_212427
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

/**
 * @title LiquidityFarmingContract
 * @dev A smart contract to participate in liquidity farming on Saddle Finance.
 *      This contract allows users to deposit liquidity tokens into Saddle Finance pools
 *      and earn rewards. It includes basic error handling and follows best practices.
 */
contract LiquidityFarmingContract {
    // Address of the Saddle Finance liquidity pool
    address public immutable saddlePool;

    // Address of the ERC20 token used for liquidity farming
    address public immutable liquidityToken;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Event emitted when a user deposits liquidity
    event LiquidityDeposited(address indexed user, uint256 amount);

    // Event emitted when a user withdraws liquidity
    event LiquidityWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the Saddle pool and liquidity token addresses.
     * @param _saddlePool Address of the Saddle Finance liquidity pool.
     * @param _liquidityToken Address of the ERC20 token used for liquidity farming.
     */
    constructor(address _saddlePool, address _liquidityToken) {
        require(_saddlePool != address(0), "Invalid Saddle pool address");
        require(_liquidityToken != address(0), "Invalid liquidity token address");

        saddlePool = _saddlePool;
        liquidityToken = _liquidityToken;
    }

    /**
     * @dev Deposit liquidity tokens into the Saddle Finance pool.
     * @param amount The amount of liquidity tokens to deposit.
     */
    function depositLiquidity(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer liquidity tokens from the user to this contract
        bool success = IERC20(liquidityToken).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Approve the Saddle pool to spend the tokens
        success = IERC20(liquidityToken).approve(saddlePool, amount);
        require(success, "Token approval failed");

        // Interact with the Saddle pool to deposit liquidity
        ISaddlePool(saddlePool).addLiquidity(amount);

        // Update user deposit balance
        userDeposits[msg.sender] += amount;

        emit LiquidityDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw liquidity tokens from the Saddle Finance pool.
     * @param amount The amount of liquidity tokens to withdraw.
     */
    function withdrawLiquidity(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userDeposits[msg.sender] >= amount, "Insufficient balance");

        // Interact with the Saddle pool to withdraw liquidity
        ISaddlePool(saddlePool).removeLiquidity(amount);

        // Transfer liquidity tokens back to the user
        bool success = IERC20(liquidityToken).transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Update user deposit balance
        userDeposits[msg.sender] -= amount;

        emit LiquidityWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the balance of liquidity tokens deposited by a user.
     * @param user The address of the user.
     * @return The balance of liquidity tokens deposited by the user.
     */
    function getUserDepositBalance(address user) external view returns (uint256) {
        return userDeposits[user];
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

/**
 * @dev Interface for the Saddle Finance pool.
 */
interface ISaddlePool {
    function addLiquidity(uint256 amount) external;
    function removeLiquidity(uint256 amount) external;
}
```
