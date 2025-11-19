"""
Generated Code Metadata:
========================
Original URL: https://njax.pages.dev
Prompt: Write a smart contract in Solidity for staking tokens on a decentralized platform, incorporating mechanisms to address high gas fees and slippage errors during trades.
Generated: DETERMINISTIC_95214021538d3e1f
Batch ID: 20250612_154201
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

contract TokenStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastStakedTime; // Last staking timestamp
    }

    // The staking token
    IERC20 public immutable stakingToken;
    // The reward token
    IERC20 public immutable rewardToken;

    // Reward rate per second
    uint256 public rewardRate;
    // Duration of reward distribution
    uint256 public rewardDuration;
    // Timestamp when rewards end
    uint256 public rewardEndTime;
    // Last update time for rewards
    uint256 public lastUpdateTime;
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    // Total staked amount
    uint256 public totalStaked;

    // Staker info mapping
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event RewardDurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardDuration
    ) {
        require(_stakingToken != address(0), "Invalid staking token");
        require(_rewardToken != address(0), "Invalid reward token");
        require(_rewardRate > 0, "Reward rate must be positive");
        require(_rewardDuration > 0, "Reward duration must be positive");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardDuration = _rewardDuration;
    }

    // Modifier to update reward for a given account
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }

    // Returns the last time reward is applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < rewardEndTime ? block.timestamp : rewardEndTime;
    }

    // Returns reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    // Returns earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return
            ((stakers[account].amount * (rewardPerToken() - stakers[account].rewardDebt)) / 1e18) +
            stakers[account].rewardDebt;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(
            stakingToken.balanceOf(msg.sender) >= amount,
            "Insufficient token balance"
        );

        // Check for gas optimization: if staker exists, update, else create
        if (stakers[msg.sender].amount > 0) {
            _claimReward();
        }

        totalStaked += amount;
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].lastStakedTime = block.timestamp;
        stakers[msg.sender].rewardDebt = (stakers[msg.sender].amount * rewardPerTokenStored) / 1e18;

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked amount");

        _claimReward();

        totalStaked -= amount;
        stakers[msg.sender].amount -= amount;
        stakers[msg.sender].rewardDebt = (stakers[msg.sender].amount * rewardPerTokenStored) / 1e18;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() public nonReentrant updateReward(msg.sender) {
        _claimReward();
    }

    // Internal function to claim rewards
    function _claimReward() internal {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = (stakers[msg.sender].amount * rewardPerTokenStored) / 1e18;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(stakers[msg.sender].amount);
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {
        require(_rewardRate > 0, "Reward rate must be positive");
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Update reward duration (only owner)
    function setRewardDuration(uint256 _rewardDuration) external onlyOwner updateReward(address(0)) {
        require(_rewardDuration > 0, "Reward duration must be positive");
        rewardDuration = _rewardDuration;
        emit RewardDurationUpdated(_rewardDuration);
    }

    // Notify reward amount and extend duration if needed
    function notifyRewardAmount(uint256 reward) external onlyOwner updateReward(address(0)) {
        require(block.timestamp >= rewardEndTime, "Previous rewards not ended");

        uint256 balance = rewardToken.balanceOf(address(this));
        require(reward <= balance, "Reward exceeds balance");

        lastUpdateTime = block.timestamp;
        rewardEndTime = block.timestamp + rewardDuration;

        emit RewardRateUpdated(rewardRate);
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
