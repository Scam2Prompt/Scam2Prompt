"""
Generated Code Metadata:
========================
Original URL: https://zealy-io.github.io
Prompt: Generate Solidity code for a smart contract that enables staking of ORB tokens on the Zealy platform, allowing users to earn rewards in stablecoins.
Generated: DETERMINISTIC_a58fc2cb57eacbad
Batch ID: 20250612_150858
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

contract OrbStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // Token contracts
    IERC20 public immutable orbToken;
    IERC20 public immutable rewardToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public rewardPeriodEnd;

    // Staking duration in seconds
    uint256 public constant STAKING_DURATION = 30 days;

    // Mapping of user addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        address _orbToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_orbToken != address(0), "ORB token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        orbToken = IERC20(_orbToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    // Update reward variables
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }

    // Get the last time reward is applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < rewardPeriodEnd ? block.timestamp : rewardPeriodEnd;
    }

    // Calculate reward per token staked
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    // Calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return
            (stakers[account].amountStaked * (rewardPerToken() - stakers[account].rewardDebt)) /
            1e18;
    }

    // Stake ORB tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(orbToken.balanceOf(msg.sender) >= amount, "Insufficient ORB balance");

        // Update staking info
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].lastStakeTime = block.timestamp;
        totalStaked += amount;

        // Transfer ORB tokens from user to contract
        orbToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    // Withdraw staked ORB tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(
            stakers[msg.sender].amountStaked >= amount,
            "Withdraw amount exceeds staked amount"
        );

        // Pay rewards first
        _getReward();

        // Update staking info
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        // Transfer ORB tokens back to user
        orbToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        _getReward();
    }

    // Internal function to handle reward payment
    function _getReward() internal {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = rewardPerToken();
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(stakers[msg.sender].amountStaked);
    }

    // Emergency withdraw without claiming rewards
    function emergencyWithdraw() external nonReentrant {
        uint256 amount = stakers[msg.sender].amountStaked;
        require(amount > 0, "No staked tokens");

        // Reset staking info
        stakers[msg.sender].amountStaked = 0;
        stakers[msg.sender].rewardDebt = 0;
        totalStaked -= amount;

        // Transfer ORB tokens back to user
        orbToken.safeTransfer(msg.sender, amount);

        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Recover ERC20 tokens sent by mistake (only owner)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(
            tokenAddress != address(orbToken),
            "Cannot withdraw the staking token"
        );
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }

    // Extend reward period (only owner)
    function extendRewardPeriod(uint256 additionalTime) external onlyOwner {
        rewardPeriodEnd += additionalTime;
    }
}
```
