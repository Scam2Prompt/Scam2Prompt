"""
Generated Code Metadata:
========================
Original URL: https://normilio.pages.dev
Prompt: Create a smart contract snippet for managing $NORMILIO token claims, emphasizing the "no funny business" principle.
Generated: DETERMINISTIC_f5f43c2e570e5a65
Batch ID: 20250612_150622
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

contract NormilioClaim is Ownable, ReentrancyGuard {
    IERC20 public normilioToken;
    
    // Claim period details
    uint256 public claimStart;
    uint256 public claimEnd;
    
    // Total tokens allocated for claims
    uint256 public totalClaimable;
    
    // Track claimed amounts
    mapping(address => uint256) public claimedAmounts;
    
    // Events
    event TokensClaimed(address indexed claimant, uint256 amount);
    event ClaimPeriodUpdated(uint256 newStart, uint256 newEnd);
    event EmergencyWithdraw(address indexed owner, uint256 amount);
    
    constructor(
        address _tokenAddress,
        uint256 _claimStart,
        uint256 _claimEnd,
        uint256 _totalClaimable
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_claimStart < _claimEnd, "Invalid claim period");
        
        normilioToken = IERC20(_tokenAddress);
        claimStart = _claimStart;
        claimEnd = _claimEnd;
        totalClaimable = _totalClaimable;
    }
    
    /**
     * @dev Claim allocated tokens
     * @param amount Amount to claim (must be <= allocation)
     */
    function claimTokens(uint256 amount) external nonReentrant {
        require(block.timestamp >= claimStart, "Claim period not started");
        require(block.timestamp <= claimEnd, "Claim period ended");
        require(amount > 0, "Amount must be positive");
        
        uint256 newClaimed = claimedAmounts[msg.sender] + amount;
        require(newClaimed <= getClaimableAmount(msg.sender), "Exceeds claimable amount");
        
        claimedAmounts[msg.sender] = newClaimed;
        require(normilioToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit TokensClaimed(msg.sender, amount);
    }
    
    /**
     * @dev Get claimable amount for address
     * @param claimant Address to check
     * @return Amount claimable
     */
    function getClaimableAmount(address claimant) public view returns (uint256) {
        // In a real implementation, this would check allocation logic
        // For simplicity, we're using a fixed totalClaimable per address
        return totalClaimable - claimedAmounts[claimant];
    }
    
    /**
     * @dev Update claim period (owner only)
     */
    function updateClaimPeriod(uint256 newStart, uint256 newEnd) external onlyOwner {
        require(newStart < newEnd, "Invalid claim period");
        claimStart = newStart;
        claimEnd = newEnd;
        emit ClaimPeriodUpdated(newStart, newEnd);
    }
    
    /**
     * @dev Emergency withdraw remaining tokens (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        require(block.timestamp > claimEnd, "Claim period not ended");
        uint256 balance = normilioToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(normilioToken.transfer(owner(), balance), "Transfer failed");
        emit EmergencyWithdraw(owner(), balance);
    }
    
    /**
     * @dev Reject any direct ETH transfers
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
