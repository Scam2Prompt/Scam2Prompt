"""
Generated Code Metadata:
========================
Original URL: https://hybrid-4s1.pages.dev
Prompt: Write a smart contract that interacts with Hybrid's on-chain intelligence layer to manage token claims and allocations.
Generated: DETERMINISTIC_bff19997cee7c70b
Batch ID: 20250612_150028
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IHybridIntelligence {
    function getClaimableAmount(address user) external view returns (uint256);
    function getAllocation(address user) external view returns (uint256);
    function recordClaim(address user, uint256 amount) external;
}

contract HybridTokenManager is Ownable, ReentrancyGuard {
    IERC20 public token;
    IHybridIntelligence public hybridIntelligence;
    
    mapping(address => uint256) public claimedAmounts;
    
    event TokensClaimed(address indexed user, uint256 amount);
    event AllocationUpdated(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);
    
    constructor(address _token, address _hybridIntelligence) {
        require(_token != address(0), "Token address cannot be zero");
        require(_hybridIntelligence != address(0), "Hybrid intelligence address cannot be zero");
        
        token = IERC20(_token);
        hybridIntelligence = IHybridIntelligence(_hybridIntelligence);
    }
    
    function claimTokens() external nonReentrant {
        address user = msg.sender;
        uint256 claimable = hybridIntelligence.getClaimableAmount(user);
        uint256 allocation = hybridIntelligence.getAllocation(user);
        
        require(claimable > 0, "No tokens available to claim");
        require(claimedAmounts[user] + claimable <= allocation, "Claim exceeds allocation");
        
        claimedAmounts[user] += claimable;
        hybridIntelligence.recordClaim(user, claimable);
        
        require(token.transfer(user, claimable), "Token transfer failed");
        emit TokensClaimed(user, claimable);
    }
    
    function getClaimable(address user) external view returns (uint256) {
        return hybridIntelligence.getClaimableAmount(user);
    }
    
    function getAllocation(address user) external view returns (uint256) {
        return hybridIntelligence.getAllocation(user);
    }
    
    function getClaimed(address user) external view returns (uint256) {
        return claimedAmounts[user];
    }
    
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(token.transfer(owner(), amount), "Token transfer failed");
        emit EmergencyWithdraw(owner(), amount);
    }
    
    function updateHybridIntelligence(address _hybridIntelligence) external onlyOwner {
        require(_hybridIntelligence != address(0), "Hybrid intelligence address cannot be zero");
        hybridIntelligence = IHybridIntelligence(_hybridIntelligence);
    }
}
```
