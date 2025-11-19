"""
Generated Code Metadata:
========================
Original URL: https://stalyoud.io
Prompt: "Generate a smart contract code snippet in Solidity that handles the distribution of rewards in SOL to top contributors on a platform like Loud, based on their mindshare and trading volume."
Generated: DETERMINISTIC_a5d73502b7d171ee
Batch ID: 20250622_212813
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

contract RewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public solToken;
    
    struct Contributor {
        uint256 mindshareScore;
        uint256 tradingVolume;
        uint256 lastRewardTimestamp;
        uint256 totalRewards;
    }
    
    mapping(address => Contributor) public contributors;
    address[] public contributorAddresses;
    
    uint256 public rewardInterval = 7 days;
    uint256 public totalDistributed;
    
    event RewardDistributed(address indexed contributor, uint256 amount);
    event ContributorUpdated(address indexed contributor, uint256 mindshare, uint256 volume);
    
    constructor(address _solTokenAddress) {
        require(_solTokenAddress != address(0), "Invalid token address");
        solToken = IERC20(_solTokenAddress);
    }
    
    function updateContributor(
        address _contributor,
        uint256 _mindshareScore,
        uint256 _tradingVolume
    ) external onlyOwner {
        require(_contributor != address(0), "Invalid address");
        
        if (contributors[_contributor].mindshareScore == 0) {
            contributorAddresses.push(_contributor);
        }
        
        contributors[_contributor] = Contributor({
            mindshareScore: _mindshareScore,
            tradingVolume: _tradingVolume,
            lastRewardTimestamp: contributors[_contributor].lastRewardTimestamp,
            totalRewards: contributors[_contributor].totalRewards
        });
        
        emit ContributorUpdated(_contributor, _mindshareScore, _tradingVolume);
    }
    
    function distributeRewards() external onlyOwner nonReentrant {
        require(contributorAddresses.length > 0, "No contributors");
        
        uint256 totalScore;
        uint256 contractBalance = solToken.balanceOf(address(this));
        require(contractBalance > 0, "No rewards available");
        
        for (uint256 i = 0; i < contributorAddresses.length; i++) {
            address contributor = contributorAddresses[i];
            if (block.timestamp - contributors[contributor].lastRewardTimestamp >= rewardInterval) {
                uint256 score = calculateScore(contributor);
                totalScore += score;
            }
        }
        
        require(totalScore > 0, "No eligible contributors");
        
        for (uint256 i = 0; i < contributorAddresses.length; i++) {
            address contributor = contributorAddresses[i];
            if (block.timestamp - contributors[contributor].lastRewardTimestamp >= rewardInterval) {
                uint256 score = calculateScore(contributor);
                uint256 rewardAmount = (contractBalance * score) / totalScore;
                
                if (rewardAmount > 0) {
                    contributors[contributor].lastRewardTimestamp = block.timestamp;
                    contributors[contributor].totalRewards += rewardAmount;
                    totalDistributed += rewardAmount;
                    
                    require(
                        solToken.transfer(contributor, rewardAmount),
                        "Transfer failed"
                    );
                    
                    emit RewardDistributed(contributor, rewardAmount);
                }
            }
        }
    }
    
    function calculateScore(address _contributor) internal view returns (uint256) {
        Contributor memory c = contributors[_contributor];
        return (c.mindshareScore * 2) + c.tradingVolume;
    }
    
    function setRewardInterval(uint256 _interval) external onlyOwner {
        require(_interval > 0, "Interval must be positive");
        rewardInterval = _interval;
    }
    
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(solToken), "Cannot withdraw reward token");
        IERC20 token = IERC20(_token);
        require(token.transfer(owner(), _amount), "Transfer failed");
    }
    
    function getContributorCount() external view returns (uint256) {
        return contributorAddresses.length;
    }
}
```
