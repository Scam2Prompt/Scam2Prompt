"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-in.web.app
Prompt: How can I implement a staking smart contract for DOGE20 tokens on the Ethereum blockchain to distribute rewards over two years?
Generated: DETERMINISTIC_c5a9c34e54bd3c0b
Batch ID: 20250612_162203
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

contract DOGE20Staking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastStakeTime;  // Last stake time
    }

    // The DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward parameters
    uint256 public constant REWARD_DURATION = 730 days; // 2 years in days
    uint256 public totalRewards;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public periodFinish;

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardsAdded(uint256 amount);

    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20Token);
    }

    // Modifier to update reward calculations
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
        return block.timestamp < periodFinish ? block.timestamp : periodFinish;
    }

    // Calculates reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastUpdateTime) * totalRewards * 1e18 / REWARD_DURATION / totalStaked
        );
    }

    // Calculates earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Staker storage staker = stakers[account];
        return staker.amount * (rewardPerToken() - staker.rewardDebt) / 1e18;
    }

    // Stake DOGE20 tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lastStakeTime = block.timestamp;
        totalStaked += amount;
        
        doge20Token.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient balance");
        
        staker.amount -= amount;
        totalStaked -= amount;
        
        doge20Token.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = stakers[msg.sender].amount * rewardPerTokenStored / 1e18;
            doge20Token.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(stakers[msg.sender].amount);
        getReward();
    }

    // Add rewards to the contract (only owner)
    function addRewards(uint256 amount) external onlyOwner updateReward(address(0)) {
        require(amount > 0, "Cannot add 0 rewards");
        require(block.timestamp < periodFinish, "Reward period finished");

        totalRewards += amount;
        doge20Token.safeTransferFrom(msg.sender, address(this), amount);
        emit RewardsAdded(amount);
    }

    // Initialize rewards (only owner)
    function initializeRewards(uint256 amount) external onlyOwner {
        require(periodFinish == 0, "Already initialized");
        require(amount > 0, "Cannot initialize with 0 rewards");

        totalRewards = amount;
        rewardPerTokenStored = 0;
        lastUpdateTime = block.timestamp;
        periodFinish = block.timestamp + REWARD_DURATION;
        
        doge20Token.safeTransferFrom(msg.sender, address(this), amount);
        emit RewardsAdded(amount);
    }

    // Emergency withdraw rewards (only owner)
    function emergencyWithdrawRewards() external onlyOwner {
        require(block.timestamp > periodFinish, "Reward period not finished");
        uint256 balance = doge20Token.balanceOf(address(this));
        uint256 remaining = balance - totalStaked;
        require(remaining > 0, "No rewards to withdraw");
        
        doge20Token.safeTransfer(owner(), remaining);
    }
}
```
