"""
Generated Code Metadata:
========================
Original URL: https://scottyai-claim.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that handles the distribution of $SCOTTY token rewards to users based on their share of the staking pool and annual returns percentage.
Generated: DETERMINISTIC_94c278a0f434e6d2
Batch ID: 20250622_205709
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

contract ScottyRewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public scottyToken;
    uint256 public annualReturnsPercentage; // Basis points (10000 = 100%)
    uint256 public totalStaked;
    uint256 public lastRewardTimestamp;
    uint256 public rewardPerTokenStored;
    
    struct Staker {
        uint256 amount;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event AnnualReturnsUpdated(uint256 newPercentage);

    constructor(address _scottyToken, uint256 _annualReturnsPercentage) {
        scottyToken = IERC20(_scottyToken);
        annualReturnsPercentage = _annualReturnsPercentage;
        lastRewardTimestamp = block.timestamp;
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastRewardTimestamp = block.timestamp;
        
        if (account != address(0)) {
            stakers[account].rewards = earned(account);
            stakers[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
        uint256 additionalRewards = (timeElapsed * annualReturnsPercentage * 1e18) / (365 days * 10000);
        return rewardPerTokenStored + additionalRewards;
    }

    function earned(address account) public view returns (uint256) {
        Staker memory staker = stakers[account];
        uint256 currentRewardPerToken = rewardPerToken();
        uint256 rewardDifference = currentRewardPerToken - staker.userRewardPerTokenPaid;
        uint256 newlyEarned = (staker.amount * rewardDifference) / 1e18;
        return staker.rewards + newlyEarned;
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakers[msg.sender].amount += amount;
        totalStaked += amount;
        
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        
        staker.amount -= amount;
        totalStaked -= amount;
        
        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant updateReward(msg.sender) {
        uint256 reward = stakers[msg.sender].rewards;
        if (reward > 0) {
            stakers[msg.sender].rewards = 0;
            require(scottyToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    function setAnnualReturns(uint256 _annualReturnsPercentage) external onlyOwner {
        annualReturnsPercentage = _annualReturnsPercentage;
        emit AnnualReturnsUpdated(_annualReturnsPercentage);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(scottyToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
