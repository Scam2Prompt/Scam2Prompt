"""
Generated Code Metadata:
========================
Original URL: https://tokencatgirl.pages.dev
Prompt: Generate a code snippet for a decentralized application (DApp) that allows users to stake CATGIRL¢ tokens and earn rewards, based on the features outlined in the Catgirl ecosystem.
Generated: DETERMINISTIC_e78d356830c29c88
Batch ID: 20250612_162404
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
 * @title CatgirlTokenStaking
 * @dev A decentralized application (DApp) for staking CATGIRL¢ tokens and earning rewards.
 */
contract CatgirlTokenStaking {
    // ERC20 interface for CATGIRL¢ token
    IERC20 public catgirlToken;

    // Reward rate (e.g., 10% annual reward rate)
    uint256 public rewardRate = 10; // 10% annual reward rate
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Mapping to track staked balances and timestamps
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingTimestamps;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the CATGIRL¢ token address.
     * @param _catgirlToken Address of the CATGIRL¢ token contract.
     */
    constructor(address _catgirlToken) {
        require(_catgirlToken != address(0), "Invalid token address");
        catgirlToken = IERC20(_catgirlToken);
    }

    /**
     * @dev Stake CATGIRL¢ tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer CATGIRL¢ tokens from the user to the contract
        require(
            catgirlToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake CATGIRL¢ tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to unstake");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Transfer staked tokens and rewards to the user
        require(
            catgirlToken.transfer(msg.sender, stakedAmount + reward),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the reward for a user based on their staked amount and staking duration.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[_user];
        uint256 stakingDuration = block.timestamp - stakingTimestamps[_user];

        // Calculate reward based on annual reward rate
        uint256 reward = (stakedAmount * rewardRate * stakingDuration) /
            (100 * SECONDS_IN_YEAR);

        return reward;
    }

    /**
     * @dev Get the staked balance of a user.
     * @param _user Address of the user.
     * @return Staked balance.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Get the staking timestamp of a user.
     * @param _user Address of the user.
     * @return Staking timestamp.
     */
    function getStakingTimestamp(address _user) external view returns (uint256) {
        return stakingTimestamps[_user];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
