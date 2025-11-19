"""
Generated Code Metadata:
========================
Original URL: https://gain-oriviumio.pages.dev
Prompt: Generate a smart contract code snippet for a simple staking mechanism similar to Orivium's staking feature.
Generated: DETERMINISTIC_8d450a1b56fa197b
Batch ID: 20250622_210856
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
 * @title StakingContract
 * @dev A simple staking mechanism where users can stake and withdraw tokens.
 */
contract StakingContract {
    // State variables
    mapping(address => uint256) public stakes; // Tracks the amount staked by each user
    mapping(address => uint256) public rewards; // Tracks rewards for each user
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Reward rate per second (e.g., 1 token per second)

    address public owner; // Contract owner
    uint256 public lastUpdateTime; // Last time rewards were updated

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] += _earned(account);
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Transfer tokens from the user to the contract
        // Assumes the token contract implements ERC20 and is already approved
        require(
            IERC20(owner).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(IERC20(owner).transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(IERC20(owner).transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the earned rewards for a user.
     * @param account The address of the user.
     * @return The amount of rewards earned.
     */
    function _earned(address account) internal view returns (uint256) {
        return
            (stakes[account] * rewardRate * (block.timestamp - lastUpdateTime)) /
            1e18;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate The new reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
