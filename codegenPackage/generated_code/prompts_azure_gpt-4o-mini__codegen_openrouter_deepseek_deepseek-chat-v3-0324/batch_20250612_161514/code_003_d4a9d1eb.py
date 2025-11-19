"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.firebaseapp.com
Prompt: Create a smart contract that utilizes the USUAL token to manage treasury control and revenue distribution in a decentralized finance setting.
Generated: DETERMINISTIC_d4a9d1ebcaee5b4b
Batch ID: 20250612_161514
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

contract TreasuryManager is Ownable, ReentrancyGuard {
    IERC20 public usualToken;
    
    struct RevenueShare {
        address recipient;
        uint256 sharePercentage; // Basis points (1% = 100)
    }
    
    RevenueShare[] public revenueShares;
    uint256 public totalShares;
    uint256 public constant MAX_SHARES = 10000; // 100% in basis points
    
    event RevenueDistributed(address indexed recipient, uint256 amount);
    event RevenueShareAdded(address indexed recipient, uint256 sharePercentage);
    event RevenueShareRemoved(address indexed recipient);
    event RevenueShareUpdated(address indexed recipient, uint256 newSharePercentage);
    event TreasuryFunded(uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);
    
    constructor(address _usualToken) {
        require(_usualToken != address(0), "Invalid token address");
        usualToken = IERC20(_usualToken);
    }
    
    modifier validSharePercentage(uint256 _sharePercentage) {
        require(_sharePercentage > 0 && _sharePercentage <= MAX_SHARES, "Invalid share percentage");
        _;
    }
    
    function addRevenueShare(address _recipient, uint256 _sharePercentage) 
        external 
        onlyOwner 
        validSharePercentage(_sharePercentage)
    {
        require(_recipient != address(0), "Invalid recipient address");
        require(totalShares + _sharePercentage <= MAX_SHARES, "Total shares exceed 100%");
        
        revenueShares.push(RevenueShare({
            recipient: _recipient,
            sharePercentage: _sharePercentage
        }));
        
        totalShares += _sharePercentage;
        emit RevenueShareAdded(_recipient, _sharePercentage);
    }
    
    function removeRevenueShare(uint256 _index) external onlyOwner {
        require(_index < revenueShares.length, "Invalid index");
        
        totalShares -= revenueShares[_index].sharePercentage;
        emit RevenueShareRemoved(revenueShares[_index].recipient);
        
        if (_index != revenueShares.length - 1) {
            revenueShares[_index] = revenueShares[revenueShares.length - 1];
        }
        revenueShares.pop();
    }
    
    function updateRevenueShare(uint256 _index, uint256 _newSharePercentage) 
        external 
        onlyOwner 
        validSharePercentage(_newSharePercentage)
    {
        require(_index < revenueShares.length, "Invalid index");
        
        uint256 currentShare = revenueShares[_index].sharePercentage;
        require(totalShares - currentShare + _newSharePercentage <= MAX_SHARES, "Total shares exceed 100%");
        
        totalShares = totalShares - currentShare + _newSharePercentage;
        revenueShares[_index].sharePercentage = _newSharePercentage;
        
        emit RevenueShareUpdated(revenueShares[_index].recipient, _newSharePercentage);
    }
    
    function distributeRevenue() external nonReentrant {
        uint256 treasuryBalance = usualToken.balanceOf(address(this));
        require(treasuryBalance > 0, "No funds to distribute");
        require(totalShares > 0, "No revenue shares configured");
        
        for (uint256 i = 0; i < revenueShares.length; i++) {
            RevenueShare memory share = revenueShares[i];
            uint256 amount = (treasuryBalance * share.sharePercentage) / totalShares;
            
            if (amount > 0) {
                bool success = usualToken.transfer(share.recipient, amount);
                require(success, "Transfer failed");
                emit RevenueDistributed(share.recipient, amount);
            }
        }
    }
    
    function fundTreasury(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        bool success = usualToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Transfer failed");
        
        emit TreasuryFunded(_amount);
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = usualToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        
        bool success = usualToken.transfer(owner(), balance);
        require(success, "Transfer failed");
        
        emit EmergencyWithdraw(owner(), balance);
    }
    
    function getRevenueShareCount() external view returns (uint256) {
        return revenueShares.length;
    }
    
    function getTotalShares() external view returns (uint256) {
        return totalShares;
    }
    
    function getTreasuryBalance() external view returns (uint256) {
        return usualToken.balanceOf(address(this));
    }
}
```
