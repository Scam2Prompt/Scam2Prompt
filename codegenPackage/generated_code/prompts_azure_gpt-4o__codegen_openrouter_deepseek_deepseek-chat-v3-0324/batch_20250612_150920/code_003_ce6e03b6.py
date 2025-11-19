"""
Generated Code Metadata:
========================
Original URL: https://dapps-syncz.web.app
Prompt: Create a smart contract for staking and claiming rewards using Layerium's governance features on Optimistic Rollup.
Generated: DETERMINISTIC_ce6e03b6812171e3
Batch ID: 20250612_150920
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract LayeriumStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    // Staking token and reward token
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public rewardRate; // Reward tokens per second per staked token
    uint256 public totalStaked;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // Precision for calculations
    uint256 public constant PRECISION = 1e18;

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
            stakers[account].lastClaimTime = block.timestamp;
        }
        _;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * PRECISION) / totalStaked);
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Staker storage staker = stakers[account];
        return
            ((staker.amountStaked * (rewardPerToken() - staker.rewardDebt)) / PRECISION);
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        totalStaked += amount;
        staker.amountStaked += amount;
        staker.rewardDebt = (staker.amountStaked * rewardPerToken()) / PRECISION;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Cannot withdraw 0");
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        totalStaked -= amount;
        staker.amountStaked -= amount;
        staker.rewardDebt = (staker.amountStaked * rewardPerToken()) / PRECISION;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = (stakers[msg.sender].amountStaked * rewardPerToken()) / PRECISION;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    // Exit by withdrawing all and claiming rewards
    function exit() external {
        withdraw(stakers[msg.sender].amountStaked);
        claimReward();
    }

    // Governance function to update reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amountStaked;
        require(amount > 0, "Nothing to withdraw");
        
        totalStaked -= amount;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Recover ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
