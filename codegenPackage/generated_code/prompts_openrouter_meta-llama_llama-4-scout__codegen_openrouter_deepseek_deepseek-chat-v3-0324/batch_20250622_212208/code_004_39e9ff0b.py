"""
Generated Code Metadata:
========================
Original URL: https://clewx.cn
Prompt: "Design a smart contract on the OKC (OKX Chain) platform for a DeFi application, focusing on security and programmability."
Generated: DETERMINISTIC_39e9ff0b75500dfe
Batch ID: 20250622_212208
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DeFiContract
 * @dev A secure and programmable DeFi contract for OKC (OKX Chain)
 */
contract DeFiContract is Ownable, ReentrancyGuard {
    // Token contract address
    IERC20 public token;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Mapping to track approved spenders
    mapping(address => mapping(address => bool)) private _allowances;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);

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
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        balances[msg.sender] += amount;
        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        require(token.transfer(msg.sender, amount), "Transfer failed");
        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Transfer tokens to another user
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function transfer(address to, uint256 amount) external nonReentrant {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
    }

    /**
     * @dev Approve another address to spend tokens on your behalf
     * @param spender Address to approve
     * @param amount Amount to approve
     */
    function approve(address spender, uint256 amount) external {
        require(spender != address(0), "Invalid spender address");
        
        _allowances[msg.sender][spender] = true;
        emit Approval(msg.sender, spender, amount);
    }

    /**
     * @dev Transfer tokens from one address to another
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function transferFrom(address from, address to, uint256 amount) external nonReentrant {
        require(from != address(0), "Invalid sender address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(balances[from] >= amount, "Insufficient balance");
        require(_allowances[from][msg.sender], "Transfer not approved");

        balances[from] -= amount;
        balances[to] += amount;
        emit Transfer(from, to, amount);
    }

    /**
     * @dev Emergency withdraw all tokens (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), contractBalance), "Transfer failed");
    }

    /**
     * @dev Get contract token balance
     * @return uint256 Contract token balance
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
