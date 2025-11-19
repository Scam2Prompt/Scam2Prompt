"""
Generated Code Metadata:
========================
Original URL: https://aero-q62.pages.dev
Prompt: "Design a smart contract function to distribute AERO emissions to liquidity providers on Aerodrome Finance using a vote-lock governance model."
Generated: DETERMINISTIC_7a92c60c33a2ba74
Batch ID: 20250622_211342
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

contract AeroEmissionDistributor is Ownable, ReentrancyGuard {
    IERC20 public immutable aeroToken;
    uint256 public totalEmissionPerSecond;
    uint256 public lastDistributionTime;
    
    struct LockedPosition {
        uint256 amount;
        uint256 unlockTime;
        uint256 votingPower;
    }
    
    mapping(address => LockedPosition) public lockedPositions;
    mapping(address => uint256) public accumulatedRewards;
    
    uint256 public totalVotingPower;
    uint256 public constant MIN_LOCK_DURATION = 7 days;
    uint256 public constant MAX_LOCK_DURATION = 4 * 365 days;
    
    event TokensLocked(address indexed user, uint256 amount, uint256 duration);
    event TokensWithdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event EmissionRateUpdated(uint256 newRate);
    
    constructor(address _aeroToken) {
        require(_aeroToken != address(0), "Invalid token address");
        aeroToken = IERC20(_aeroToken);
        lastDistributionTime = block.timestamp;
    }
    
    function lockTokens(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(duration >= MIN_LOCK_DURATION, "Lock duration too short");
        require(duration <= MAX_LOCK_DURATION, "Lock duration too long");
        
        _distributeRewards();
        
        LockedPosition storage position = lockedPositions[msg.sender];
        if (position.amount > 0) {
            _withdrawLockedTokens(msg.sender);
        }
        
        uint256 votingPower = amount * duration / MAX_LOCK_DURATION;
        
        aeroToken.transferFrom(msg.sender, address(this), amount);
        
        lockedPositions[msg.sender] = LockedPosition({
            amount: amount,
            unlockTime: block.timestamp + duration,
            votingPower: votingPower
        });
        
        totalVotingPower += votingPower;
        
        emit TokensLocked(msg.sender, amount, duration);
    }
    
    function withdrawLockedTokens() external nonReentrant {
        _distributeRewards();
        _withdrawLockedTokens(msg.sender);
    }
    
    function _withdrawLockedTokens(address user) private {
        LockedPosition storage position = lockedPositions[user];
        require(position.amount > 0, "No locked tokens");
        require(block.timestamp >= position.unlockTime, "Tokens still locked");
        
        uint256 amount = position.amount;
        totalVotingPower -= position.votingPower;
        
        delete lockedPositions[user];
        aeroToken.transfer(user, amount);
        
        emit TokensWithdrawn(user, amount);
    }
    
    function claimRewards() external nonReentrant {
        _distributeRewards();
        
        uint256 reward = accumulatedRewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        accumulatedRewards[msg.sender] = 0;
        aeroToken.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }
    
    function _distributeRewards() private {
        if (totalVotingPower == 0) {
            lastDistributionTime = block.timestamp;
            return;
        }
        
        uint256 timeElapsed = block.timestamp - lastDistributionTime;
        if (timeElapsed == 0) return;
        
        uint256 totalReward = totalEmissionPerSecond * timeElapsed;
        lastDistributionTime = block.timestamp;
        
        if (totalReward == 0) return;
        
        uint256 balance = aeroToken.balanceOf(address(this));
        if (totalReward > balance) {
            totalReward = balance;
        }
        
        for (uint256 i = 0; i < _lockedUsers.length(); i++) {
            address user = _lockedUsers.at(i);
            LockedPosition storage position = lockedPositions[user];
            
            uint256 userReward = totalReward * position.votingPower / totalVotingPower;
            accumulatedRewards[user] += userReward;
        }
    }
    
    function setEmissionRate(uint256 newRate) external onlyOwner {
        _distributeRewards();
        totalEmissionPerSecond = newRate;
        emit EmissionRateUpdated(newRate);
    }
    
    // Additional utility functions
    function getPendingRewards(address user) external view returns (uint256) {
        if (totalVotingPower == 0) return accumulatedRewards[user];
        
        uint256 timeElapsed = block.timestamp - lastDistributionTime;
        uint256 totalReward = totalEmissionPerSecond * timeElapsed;
        
        LockedPosition storage position = lockedPositions[user];
        uint256 pendingReward = totalReward * position.votingPower / totalVotingPower;
        
        return accumulatedRewards[user] + pendingReward;
    }
    
    // Using EnumerableSet for efficient iteration (not shown here for brevity)
    // In production, you would import and use OpenZeppelin's EnumerableSet
    // to track locked users for reward distribution
    // EnumerableSet.AddressSet private _lockedUsers;
}
```
otalLockedVotes;
    }

    /**
     * @dev View function to check pending rewards for a provider
     * @param provider Address of the liquidity provider
     * @return Total pending rewards
     */
    function pendingRewards(address provider) external view returns (uint256) {
        return accumulatedRewards[provider] + _calculateRewards(provider);
    }
}
```
