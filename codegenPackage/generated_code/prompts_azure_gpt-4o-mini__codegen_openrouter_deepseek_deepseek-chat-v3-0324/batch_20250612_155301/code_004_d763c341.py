"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: What are the best practices for developing decentralized finance (DeFi) applications on Ethereum?
Generated: DETERMINISTIC_d763c341cf4a65c7
Batch ID: 20250612_155301
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFiBestPractices
 * @dev Demonstrates best practices for DeFi development on Ethereum
 */
contract DeFiBestPractices is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // State variables
    mapping(address => uint256) public balances;
    uint256 public totalDeposits;
    IERC20 public token;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Constructor sets the token address
     * @param _token Address of the ERC20 token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Deposit tokens into the contract
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to contract
        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), amount);
        uint256 balanceAfter = token.balanceOf(address(this));
        uint256 actualAmount = balanceAfter.sub(balanceBefore);

        // Update balances
        balances[msg.sender] = balances[msg.sender].add(actualAmount);
        totalDeposits = totalDeposits.add(actualAmount);

        emit Deposited(msg.sender, actualAmount);
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances before transfer to prevent reentrancy
        balances[msg.sender] = balances[msg.sender].sub(amount);
        totalDeposits = totalDeposits.sub(amount);

        // Transfer tokens to user
        token.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Emergency withdraw all tokens (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        token.safeTransfer(owner(), balance);
        emit EmergencyWithdraw(owner(), balance);
    }

    /**
     * @dev Get contract token balance
     * @return uint256 Token balance
     */
    function getContractBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }

    /**
     * @dev Get user balance
     * @param user Address of the user
     * @return uint256 User balance
     */
    function getUserBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
