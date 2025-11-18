"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a smart contract in Solidity for staking $GGG tokens, referencing the staking platform details from Good Games Guild documentation.
Generated: DETERMINISTIC_9bc49b47b0c0c857
Batch ID: 20250612_153820
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
 * @title StakingContract
 * @dev This contract allows users to stake $GGG tokens and earn rewards based on the duration of their staking.
 * Reference: Good Games Guild documentation.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract StakingContract {
    // Address of the $GGG token contract
    IERC20 public immutable gggToken;

    // Structure to keep track of staking details
    struct Stake {
        uint256 amount;    // Amount of $GGG tokens staked
        uint256 timestamp; // Timestamp of when the stake was created
    }

    // Mapping of user addresses to their staking details
    mapping(address => Stake) public stakes;

    // Reward percentage per second (in basis points, e.g., 10000 = 100%)
    uint256 public immutable rewardRatePerSecond; // Example: 50 basis points = 0.5%

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No stake found for the user");
        _;
    }

    /**
     * @notice Constructor to initialize the staking contract
     * @param _gggToken Address of the $GGG token contract
     * @param _rewardRatePerSecond Reward rate per second in basis points
     */
    constructor(IERC20 _gggToken, uint256 _rewardRatePerSecond) {
        require(address(_gggToken) != address(0), "Invalid token address");
        require(_rewardRatePerSecond > 0, "Reward rate must be greater than zero");

        gggToken = _gggToken;
        rewardRatePerSecond = _rewardRatePerSecond;
        owner = msg.sender;
    }

    /**
     * @notice Allows users to stake $GGG tokens
     * @param _amount Amount of $GGG tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer $GGG tokens from the user's wallet to the contract
        bool success = gggToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // If the user already has a stake, calculate the rewards for existing stake
        if (userStake.amount > 0) {
            uint256 reward = calculateReward(msg.sender);
            userStake.amount += reward;
        }

        // Update staking details
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to unstake their $GGG tokens and withdraw rewards
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender);

        // Reset stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked amount + rewards back to the user
        require(gggToken.transfer(msg.sender, stakedAmount + reward), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @notice Calculates the staking rewards for a user
     * @param _user Address of the user
     * @return reward Calculated reward based on staking duration and rate
     */
    function calculateReward(address _user) public view hasStake(_user) returns (uint256 reward) {
        Stake storage userStake = stakes[_user];
        uint256 duration = block.timestamp - userStake.timestamp;
        reward = (userStake.amount * rewardRatePerSecond * duration) / 10000;
    }

    /**
     * @notice Emergency function to allow the owner to withdraw tokens
     * @param _amount Amount of $GGG tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(gggToken.transfer(owner, _amount), "Token transfer failed");
    }
}
```
