"""
Generated Code Metadata:
========================
Original URL: https://shib.club
Prompt: Generate a Solidity smart contract code for creating a decentralized application (dApp) that utilizes SHIB tokens.
Generated: DETERMINISTIC_de6e58beec29786a
Batch ID: 20250622_205315
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

contract SHIBdApp is Ownable, ReentrancyGuard {
    IERC20 public shibToken;
    
    // Events
    event TokensDeposited(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);
    
    // Constructor to initialize the SHIB token contract address
    constructor(address _shibTokenAddress) {
        require(_shibTokenAddress != address(0), "Invalid token address");
        shibToken = IERC20(_shibTokenAddress);
    }
    
    // Deposit SHIB tokens into the contract
    function depositTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        bool success = shibToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");
        
        emit TokensDeposited(msg.sender, _amount);
    }
    
    // Withdraw SHIB tokens from the contract
    function withdrawTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(shibToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        
        bool success = shibToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");
        
        emit TokensWithdrawn(msg.sender, _amount);
    }
    
    // Transfer SHIB tokens between users
    function transferTokens(address _to, uint256 _amount) external nonReentrant {
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");
        
        bool success = shibToken.transferFrom(msg.sender, _to, _amount);
        require(success, "Token transfer failed");
        
        emit TokensTransferred(msg.sender, _to, _amount);
    }
    
    // Get contract SHIB token balance
    function getContractBalance() external view returns (uint256) {
        return shibToken.balanceOf(address(this));
    }
    
    // Get user SHIB token balance
    function getUserBalance(address _user) external view returns (uint256) {
        return shibToken.balanceOf(_user);
    }
    
    // Emergency withdrawal of all SHIB tokens (owner only)
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = shibToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        bool success = shibToken.transfer(owner(), balance);
        require(success, "Token transfer failed");
    }
}
```
