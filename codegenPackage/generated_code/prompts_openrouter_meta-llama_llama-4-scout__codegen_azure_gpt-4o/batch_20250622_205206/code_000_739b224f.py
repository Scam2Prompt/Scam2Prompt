"""
Generated Code Metadata:
========================
Original URL: https://pepeunchaineden.pages.dev
Prompt: Write a smart contract in Solidity for a Layer 2 blockchain like Pepe Unchained that enables double staking rewards.
Generated: DETERMINISTIC_739b224f39054643
Batch ID: 20250622_205206
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

/**
 * @title DoubleStakingRewards
 * @dev A smart contract for double staking rewards on a Layer 2 blockchain.
 * Users can stake tokens and earn rewards from two separate reward pools.
 */
contract DoubleStakingRewards {
    // State variables
    address public owner; // Contract owner
    address public stakingToken; // Token to be staked
    address public rewardToken1; // First reward token
    address public rewardToken2; // Second reward token

    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate1; // Reward rate for the first reward pool
    uint256 public rewardRate2; // Reward rate for the second reward pool

    mapping(address => uint256) public stakedBalances; // Tracks staked balances of users
    mapping(address => uint256) public rewardBalances1; // Tracks rewards from pool 1
    mapping(address => uint256) public rewardBalances2; // Tracks rewards from pool 2
    mapping(address => uint256) public lastUpdateTime; // Tracks last update time for rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward1, uint256 reward2);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateRewards(address account) {
        if (account != address(0)) {
            rewardBalances1[account] += earned(account, rewardRate1);
            rewardBalances2[account] += earned(account, rewardRate2);
            lastUpdateTime[account] = block.timestamp;
        }
        _;
    }

    // Constructor
    constructor(
        address _stakingToken,
        address _rewardToken1,
        address _rewardToken2,
        uint256 _rewardRate1,
        uint256 _rewardRate2
    ) {
        owner = msg.sender;
        stakingToken = _stakingToken;
        rewardToken1 = _rewardToken1;
        rewardToken2 = _rewardToken2;
        rewardRate1 = _rewardRate1;
        rewardRate2 = _rewardRate2;
    }

    // Function to calculate earned rewards
    function earned(address account, uint256 rewardRate) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[account];
        return stakedBalances[account] * rewardRate * timeElapsed / 1e18;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");
        require(IERC20(stakingToken).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        require(IERC20(stakingToken).transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward1 = rewardBalances1[msg.sender];
        uint256 reward2 = rewardBalances2[msg.sender];

        require(reward1 > 0 || reward2 > 0, "No rewards to claim");

        rewardBalances1[msg.sender] = 0;
        rewardBalances2[msg.sender] = 0;

        if (reward1 > 0) {
            require(IERC20(rewardToken1).transfer(msg.sender, reward1), "Reward 1 transfer failed");
        }
        if (reward2 > 0) {
            require(IERC20(rewardToken2).transfer(msg.sender, reward2), "Reward 2 transfer failed");
        }

        emit RewardsClaimed(msg.sender, reward1, reward2);
    }

    // Function to update reward rates (only owner)
    function updateRewardRates(uint256 _rewardRate1, uint256 _rewardRate2) external onlyOwner {
        rewardRate1 = _rewardRate1;
        rewardRate2 = _rewardRate2;
    }

    // Function to recover tokens sent to the contract by mistake (only owner)
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(owner, amount), "Token recovery failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
