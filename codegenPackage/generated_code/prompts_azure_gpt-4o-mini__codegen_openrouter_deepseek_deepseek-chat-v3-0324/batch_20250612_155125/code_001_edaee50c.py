"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Generate a code snippet for a decentralized application that allows users to deposit $BIBBY tokens and track their dividends in real-time.
Generated: DETERMINISTIC_edaee50c1985fe1e
Batch ID: 20250612_155125
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

contract BibbyDividendTracker is Ownable, ReentrancyGuard {
    IERC20 public bibbyToken;
    
    struct Deposit {
        uint256 amount;
        uint256 timestamp;
    }
    
    struct Dividend {
        uint256 amount;
        uint256 timestamp;
    }
    
    mapping(address => Deposit[]) public userDeposits;
    mapping(address => Dividend[]) public userDividends;
    mapping(address => uint256) public totalClaimedDividends;
    
    uint256 public totalDeposits;
    uint256 public totalDividendsDistributed;
    uint256 public lastDividendDistribution;
    
    event Deposited(address indexed user, uint256 amount);
    event DividendDistributed(address indexed user, uint256 amount);
    event DividendClaimed(address indexed user, uint256 amount);
    
    constructor(address _bibbyToken) {
        require(_bibbyToken != address(0), "Invalid token address");
        bibbyToken = IERC20(_bibbyToken);
    }
    
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        bool success = bibbyToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        userDeposits[msg.sender].push(Deposit({
            amount: amount,
            timestamp: block.timestamp
        }));
        
        totalDeposits += amount;
        emit Deposited(msg.sender, amount);
    }
    
    function distributeDividends(uint256 totalAmount) external onlyOwner {
        require(totalAmount > 0, "Amount must be greater than 0");
        require(totalDeposits > 0, "No deposits to distribute to");
        
        bool success = bibbyToken.transferFrom(msg.sender, address(this), totalAmount);
        require(success, "Token transfer failed");
        
        uint256 dividendPerToken = (totalAmount * 1e18) / totalDeposits;
        lastDividendDistribution = block.timestamp;
        totalDividendsDistributed += totalAmount;
        
        // In a real implementation, you would iterate through all depositors
        // This is simplified for demonstration
    }
    
    function calculateDividends(address user) public view returns (uint256) {
        uint256 totalDividends;
        Deposit[] storage deposits = userDeposits[user];
        
        for (uint256 i = 0; i < deposits.length; i++) {
            uint256 depositAmount = deposits[i].amount;
            uint256 depositTime = deposits[i].timestamp;
            
            if (depositTime < lastDividendDistribution) {
                // Simplified calculation - in reality would use proper distribution logic
                totalDividends += (depositAmount * totalDividendsDistributed) / totalDeposits;
            }
        }
        
        return totalDividends - totalClaimedDividends[user];
    }
    
    function claimDividends() external nonReentrant {
        uint256 dividends = calculateDividends(msg.sender);
        require(dividends > 0, "No dividends to claim");
        
        totalClaimedDividends[msg.sender] += dividends;
        userDividends[msg.sender].push(Dividend({
            amount: dividends,
            timestamp: block.timestamp
        }));
        
        bool success = bibbyToken.transfer(msg.sender, dividends);
        require(success, "Token transfer failed");
        
        emit DividendClaimed(msg.sender, dividends);
    }
    
    function getUserDeposits(address user) external view returns (Deposit[] memory) {
        return userDeposits[user];
    }
    
    function getUserDividends(address user) external view returns (Dividend[] memory) {
        return userDividends[user];
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = bibbyToken.balanceOf(address(this));
        bibbyToken.transfer(owner(), balance);
    }
}
```
