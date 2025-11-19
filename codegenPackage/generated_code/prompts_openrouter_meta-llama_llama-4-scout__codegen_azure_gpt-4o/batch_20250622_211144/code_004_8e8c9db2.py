"""
Generated Code Metadata:
========================
Original URL: https://defi-88.cc
Prompt: "Create a basic example of a DeFi staking pool using Solidity and OpenZeppelin's contracts."
Generated: DETERMINISTIC_8e8c9db2b77de71c
Batch ID: 20250622_211144
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

// Import OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingPool is Ownable {
    // Token used for staking
    IERC20 public stakingToken;

    // Reward token distributed to stakers
    IERC20 public rewardToken;

    // Reward rate per second (e.g., 1 reward token per second)
    uint256 public rewardRate;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Total rewards per token staked
    uint256 public rewardPerTokenStored;

    // Total staked tokens in the pool
    uint256 public totalStaked;

    // Mapping of user address to staked amount
    mapping(address => uint256) public balances;

    // Mapping of user address to rewards earned
    mapping(address => uint256) public rewards;

    // Mapping of user address to reward per token paid
    mapping(address => uint256) public userRewardPerTokenPaid;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before executing a function
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked;
    }

    // Calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18 + rewards[account];
    }

    // Stake tokens into the pool
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        balances[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens from the pool
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");
        balances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim earned rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Allow the owner to update the reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
