"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Develop a Solidity contract for distributing community rewards, ensuring that 10% of the $MK token supply is allocated fairly among active participants in Meme Kombat battles.
Generated: DETERMINISTIC_50ad4d94d0231b05
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for distributing community rewards
contract CommunityRewards is Ownable {
    // Token that will be used for rewards
    IERC20 public mkToken;

    // Total supply of MK tokens
    uint256 public totalSupply;
    
    // Total reward pool (10% of total supply)
    uint256 public rewardPool;

    // Mapping to track participant rewards
    mapping(address => uint256) public rewards;

    // Event to log reward distribution
    event RewardsDistributed(address indexed participant, uint256 amount);
    
    // Constructor to set up the MK token and total supply
    constructor(address _mkToken, uint256 _totalSupply) {
        mkToken = IERC20(_mkToken);
        totalSupply = _totalSupply;
        rewardPool = totalSupply * 10 / 100; // 10% allocation
    }

    // Function to distribute rewards to participants
    function distributeRewards(address[] calldata participants, uint256[] calldata amounts) external onlyOwner {
        require(participants.length == amounts.length, "Participants and amounts length mismatch");
        
        uint256 totalDistributed = 0;

        for (uint256 i = 0; i < participants.length; i++) {
            require(participants[i] != address(0), "Invalid participant address");
            require(amounts[i] > 0, "Reward amount must be greater than zero");
            require(totalDistributed + amounts[i] <= rewardPool, "Exceeds available reward pool");

            rewards[participants[i]] += amounts[i];
            totalDistributed += amounts[i];

            emit RewardsDistributed(participants[i], amounts[i]);
        }
        
        // Transfer rewards from the contract to the participants
        bool success = mkToken.transferFrom(address(this), msg.sender, totalDistributed);
        require(success, "Token transfer failed");
    }

    // Function to withdraw remaining rewards by the owner
    function withdrawRemainingRewards() external onlyOwner {
        uint256 remainingRewards = mkToken.balanceOf(address(this));
        require(remainingRewards > 0, "No remaining rewards to withdraw");

        bool success = mkToken.transfer(msg.sender, remainingRewards);
        require(success, "Withdrawal failed");
    }

    // Function to check the reward balance of a participant
    function checkRewardBalance(address participant) external view returns (uint256) {
        return rewards[participant];
    }
}
```
