"""
Generated Code Metadata:
========================
Original URL: https://rpcdappnodefix.com
Prompt: Create a smart contract function to automate staking and unstaking tokens on the Tigris platform, addressing staking-related issues.
Generated: DETERMINISTIC_90b715ef7bd6c1d7
Batch ID: 20250612_150024
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

contract TigrisStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
        uint256 rewardDebt;
    }

    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public constant REWARD_DURATION = 7 days;

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    function earned(address account) public view returns (uint256) {
        return ((stakes[account].amount * 
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) 
                + rewards[account];
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        stakes[msg.sender].lastClaimed = block.timestamp;
        totalStaked += amount;

        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");

        _claimRewards();

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        require(
            stakingToken.transfer(msg.sender, amount),
            "Transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant updateReward(msg.sender) {
        _claimRewards();
    }

    function _claimRewards() private {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            stakes[msg.sender].lastClaimed = block.timestamp;
            
            require(
                rewardToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );

            emit RewardClaimed(msg.sender, reward);
        }
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    function emergencyWithdraw() external nonReentrant {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "No stake to withdraw");

        totalStaked -= amount;
        stakes[msg.sender].amount = 0;
        rewards[msg.sender] = 0;

        require(
            stakingToken.transfer(msg.sender, amount),
            "Transfer failed"
        );
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot withdraw staking or reward tokens"
        );
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
