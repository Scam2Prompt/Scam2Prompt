"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-claim-akz.pages.dev
Prompt: Write a smart contract in Solidity for a staking system that distributes rewards over a period of two years, similar to Dogecoin20's staking mechanism.
Generated: DETERMINISTIC_a4cc9b002642bcc0
Batch ID: 20250622_210806
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingSystem is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Staking token and reward token
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public constant REWARD_DURATION = 730 days; // 2 years
    uint256 public constant LOCK_DURATION = 30 days; // Minimum lock period
    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public periodFinish;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User staking data
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 unlockTime;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardAdded(uint256 reward);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < periodFinish ? block.timestamp : periodFinish;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored.add(
                lastTimeRewardApplicable()
                    .sub(lastUpdateTime)
                    .mul(rewardRate)
                    .mul(1e18)
                    .div(totalStaked)
            );
    }

    function earned(address account) public view returns (uint256) {
        return
            stakes[account]
                .amount
                .mul(rewardPerToken().sub(userRewardPerTokenPaid[account]))
                .div(1e18)
                .add(rewards[account]);
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");
        }

        totalStaked = totalStaked.add(amount);
        userStake.amount = userStake.amount.add(amount);
        userStake.unlockTime = block.timestamp.add(LOCK_DURATION);
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(amount > 0, "Cannot withdraw 0");
        require(userStake.amount >= amount, "Insufficient staked balance");
        require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");

        totalStaked = totalStaked.sub(amount);
        userStake.amount = userStake.amount.sub(amount);
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function notifyRewardAmount(uint256 reward) external updateReward(address(0)) {
        require(reward > 0, "No reward provided");
        
        if (block.timestamp >= periodFinish) {
            rewardRate = reward.div(REWARD_DURATION);
        } else {
            uint256 remaining = periodFinish.sub(block.timestamp);
            uint256 leftover = remaining.mul(rewardRate);
            rewardRate = reward.add(leftover).div(REWARD_DURATION);
        }

        // Ensure the provided reward amount is not more than the balance in the contract
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardRate <= balance.div(REWARD_DURATION), "Provided reward too high");

        lastUpdateTime = block.timestamp;
        periodFinish = block.timestamp.add(REWARD_DURATION);
        emit RewardAdded(reward);
    }

    // Emergency function to recover ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        require(tokenAddress != address(rewardToken), "Cannot withdraw reward token");
        IERC20(tokenAddress).safeTransfer(msg.sender, tokenAmount);
    }
}
```
