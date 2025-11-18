"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webbridge.pages.dev
Prompt: Write a smart contract to stake tokens on the Tigris platform and handle staking-related issues.
Generated: DETERMINISTIC_d1cd78e54e10c43b
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TigrisTokenStaking
 * @dev A smart contract to stake tokens on the Tigris platform and handle staking-related operations.
 * Users can stake tokens, withdraw tokens, and check their staking balance.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TigrisTokenStaking {
    // State variables
    IERC20 public immutable stakingToken; // The token used for staking
    mapping(address => uint256) public stakes; // Tracks staking balances of users
    mapping(address => uint256) public rewards; // Tracks rewards for each user
    uint256 public totalStaked; // Total tokens staked in the platform
    uint256 public rewardRate; // Reward rate per token staked (e.g., per block or epoch)
    address public owner; // Contract owner

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] += earned(account);
            stakes[account] = stakes[account]; // Ensure staking balance is up-to-date
        }
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the staking token and reward rate.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardRate Reward rate per token staked.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        require(address(_stakingToken) != address(0), "Invalid staking token address");
        require(_rewardRate > 0, "Invalid reward rate");
        
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        stakes[msg.sender] -= amount;
        totalStaked -= amount;
        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        require(
            stakingToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward earned by a user.
     * @param account The user's address.
     * @return The reward amount.
     */
    function earned(address account) public view returns (uint256) {
        return stakes[account] * rewardRate;
    }

    /**
     * @dev Allows the owner to transfer contract ownership.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Allows the owner to set a new reward rate.
     * @param newRewardRate The new reward rate.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Invalid reward rate");
        rewardRate = newRewardRate;
    }
}
```
