"""
Generated Code Metadata:
========================
Original URL: https://starsdapps.pro
Prompt: "What are the key considerations for ensuring safety in DeFi dApps, and how can they be implemented in a new project?"
Generated: DETERMINISTIC_fc6dc8ed358c3117
Batch ID: 20250622_212519
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SafeDeFi
 * @dev A secure DeFi dApp implementation with key safety considerations
 */
contract SafeDeFi is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Token contract
    IERC20 public token;

    // User balances mapping
    mapping(address => uint256) public balances;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Constructor sets the token address
     * @param _tokenAddress Address of the ERC20 token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Deposit tokens into the contract
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Check allowance
        uint256 allowance = token.allowance(msg.sender, address(this));
        require(allowance >= amount, "Check token allowance");

        // Transfer tokens
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update balance
        balances[msg.sender] = balances[msg.sender].add(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balance before transfer to prevent reentrancy
        balances[msg.sender] = balances[msg.sender].sub(amount);

        // Transfer tokens
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Emergency withdraw all tokens (owner only)
     * @notice Only for emergency situations
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = token.transfer(owner(), balance);
        require(success, "Token transfer failed");

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
