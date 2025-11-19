"""
Generated Code Metadata:
========================
Original URL: https://celo.usdc20.com
Prompt: Generate an example of how to integrate the Celo USDC token with a DeFi application on Ethereum.
Generated: DETERMINISTIC_a8ca3d0b0f85ceae
Batch ID: 20250622_212513
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CeloUSDCDeFiIntegration
 * @dev A contract that integrates Celo USDC (bridged to Ethereum) with DeFi operations
 */
contract CeloUSDCDeFiIntegration is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Celo USDC token contract address (bridged to Ethereum)
    IERC20 public celoUSDC;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Total deposited amount
    uint256 public totalDeposited;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event YieldDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the Celo USDC token address
     * @param _celoUSDCAddress Address of the Celo USDC token on Ethereum
     */
    constructor(address _celoUSDCAddress) {
        require(_celoUSDCAddress != address(0), "Invalid token address");
        celoUSDC = IERC20(_celoUSDCAddress);
    }

    /**
     * @dev Deposit Celo USDC tokens into the contract
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to contract
        celoUSDC.safeTransferFrom(msg.sender, address(this), amount);

        // Update balances
        userDeposits[msg.sender] += amount;
        totalDeposited += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw Celo USDC tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userDeposits[msg.sender] >= amount, "Insufficient balance");

        // Update balances before transfer to prevent reentrancy
        userDeposits[msg.sender] -= amount;
        totalDeposited -= amount;

        // Transfer tokens back to user
        celoUSDC.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Simulate yield distribution (in a real scenario, this would interact with a yield protocol)
     * @param user Address of the user to distribute yield to
     * @param yieldAmount Amount of yield to distribute
     */
    function distributeYield(address user, uint256 yieldAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(yieldAmount > 0, "Yield amount must be greater than 0");
        require(celoUSDC.balanceOf(address(this)) >= totalDeposited + yieldAmount, "Insufficient contract balance");

        // Transfer yield to user
        celoUSDC.safeTransfer(user, yieldAmount);

        emit YieldDistributed(user, yieldAmount);
    }

    /**
     * @dev Get user deposit balance
     * @param user Address of the user
     * @return User's deposited balance
     */
    function getUserBalance(address user) external view returns (uint256) {
        return userDeposits[user];
    }

    /**
     * @dev Emergency withdraw all funds (onlyOwner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = celoUSDC.balanceOf(address(this));
        celoUSDC.safeTransfer(owner(), balance);
    }
}
```
