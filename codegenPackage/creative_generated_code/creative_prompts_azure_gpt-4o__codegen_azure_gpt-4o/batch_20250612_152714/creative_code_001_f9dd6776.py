"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pre-mpeppe-live.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with the $MPEPE token to allow staking and automatic reward distribution, ensuring compliance with the Ethereum blockchain.
Generated: DETERMINISTIC_f9dd6776db67bab9
Batch ID: 20250612_152714
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
 * @title MPEPE Staking Contract
 * @dev Allows users to stake $MPEPE tokens and earn rewards automatically based on staking duration.
 *      Complies with the Ethereum blockchain standards.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MPEPEStaking {
    // Address of the $MPEPE token contract
    IERC20 public mpepeToken;

    // Reward rate in percentage (e.g., 5 means 5%)
    uint256 public rewardRate;

    // Mapping to track stakes of each address
    mapping(address => uint256) public stakes;

    // Mapping to track staking timestamps for each address
    mapping(address => uint256) public stakeTimestamps;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the $MPEPE token address and reward rate.
     * @param _mpepeToken Address of the $MPEPE token contract.
     * @param _rewardRate Annual reward rate percentage.
     */
    constructor(address _mpepeToken, uint256 _rewardRate) {
        require(_mpepeToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        mpepeToken = IERC20(_mpepeToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to allow users to stake $MPEPE tokens.
     * @param _amount Amount of $MPEPE tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer $MPEPE tokens from the user to the contract
        require(mpepeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update stakes and staking timestamp
        stakes[msg.sender] += _amount;
        stakeTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate the reward for a user based on staking duration.
     * @param _user Address of the user.
     * @return Reward amount in $MPEPE tokens.
     */
    function calculateReward(address _user) public view returns (uint256) {
        uint256 stakeAmount = stakes[_user];
        uint256 stakingDuration = block.timestamp - stakeTimestamps[_user];

        // Annual reward rate applied proportionally to staking duration in seconds
        uint256 reward = (stakeAmount * rewardRate * stakingDuration) / (365 days * 100);
        return reward;
    }

    /**
     * @dev Function to allow users to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer reward tokens to the user
        require(mpepeToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Reset staking timestamp
        stakeTimestamps[msg.sender] = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to allow users to unstake their $MPEPE tokens.
     *      Rewards will be automatically claimed before unstaking.
     */
    function unstake() external {
        uint256 stakeAmount = stakes[msg.sender];
        require(stakeAmount > 0, "No staked tokens to unstake");

        // Claim rewards before unstaking
        claimRewards();

        // Transfer staked tokens back to the user
        require(mpepeToken.transfer(msg.sender, stakeAmount), "Unstake transfer failed");

        // Reset stakes and staking timestamp
        stakes[msg.sender] = 0;
        stakeTimestamps[msg.sender] = 0;

        emit Unstaked(msg.sender, stakeAmount);
    }

    /**
     * @dev Function to retrieve the contract's $MPEPE token balance.
     * @return Balance of $MPEPE tokens in the contract.
     */
    function contractBalance() external view returns (uint256) {
        return mpepeToken.balanceOf(address(this));
    }
}
```
