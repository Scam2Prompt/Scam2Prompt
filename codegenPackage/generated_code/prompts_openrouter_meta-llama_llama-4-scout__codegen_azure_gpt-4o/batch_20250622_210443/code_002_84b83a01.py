"""
Generated Code Metadata:
========================
Original URL: https://basedbrett-in.web.app
Prompt: Generate a Solidity code snippet for staking and unstaking BRETT tokens, considering the utilities and features mentioned on the webpage.
Generated: DETERMINISTIC_84b83a01d4f7927a
Batch ID: 20250622_210443
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
 * @title BRETT Token Staking Contract
 * @dev This contract allows users to stake and unstake BRETT tokens.
 * It includes basic functionality for staking, unstaking, and tracking rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BrettTokenStaking {
    // State variables
    IERC20 public brettToken; // BRETT token contract
    uint256 public rewardRate; // Reward rate per second
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when staking started
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No active stake found");
        _;
    }

    // Constructor
    constructor(IERC20 _brettToken, uint256 _rewardRate) {
        brettToken = _brettToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake BRETT tokens.
     * @param amount The amount of BRETT tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(brettToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake BRETT tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = stakingDuration * rewardRate * userStake.amount / 1e18;

        // Transfer staked tokens and rewards back to the user
        require(brettToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        require(brettToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);

        // Reset stake information
        userStake.amount = 0;
        userStake.timestamp = 0;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(brettToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
