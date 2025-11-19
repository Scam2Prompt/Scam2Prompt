"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gain-oriviumio.pages.dev
Prompt: Provide an example of a smart contract for staking ORI tokens in the Orivium ecosystem, focusing on sustainability and efficiency.
Generated: DETERMINISTIC_4f1ab704e18d51ec
Batch ID: 20250612_162325
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
 * @title ORI Token Staking Contract
 * @dev A smart contract for staking ORI tokens in the Orivium ecosystem, focusing on sustainability and efficiency.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ORIStaking {
    // Address of the ORI token contract
    IERC20 public immutable oriToken;

    // Data structure to hold staking information
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Timestamp of when the stake was created
    }

    // Mapping of user addresses to their staking details
    mapping(address => Stake) public stakes;

    // Rewards rate per second (scaled for precision, e.g., 10 wei per second)
    uint256 public immutable rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the ORI token address and reward rate.
     * @param _oriToken Address of the ORI token contract
     * @param _rewardRate Rewards rate per second
     */
    constructor(IERC20 _oriToken, uint256 _rewardRate) {
        require(address(_oriToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        oriToken = _oriToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake ORI tokens into the contract.
     * @param _amount The amount of ORI tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = oriToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the staking data for the user
        Stake storage userStake = stakes[msg.sender];

        // Calculate and distribute pending rewards before adding new stake
        uint256 pendingReward = calculateRewards(msg.sender);
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake ORI tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender);
        uint256 stakedAmount = userStake.amount;

        // Reset staking details
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked tokens and rewards back to the user
        bool successTokens = oriToken.transfer(msg.sender, stakedAmount);
        require(successTokens, "Token transfer failed");

        if (reward > 0) {
            bool successReward = oriToken.transfer(msg.sender, reward);
            require(successReward, "Reward transfer failed");
        }

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculate the rewards for a given user based on staking duration.
     * @param _user Address of the user to calculate rewards for.
     * @return The calculated reward amount.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0; // No tokens staked
        }

        // Calculate rewards based on the staking duration
        uint256 duration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * rewardRate * duration) / 1 ether; // Scale rewards for precision

        return reward;
    }

    /**
     * @dev Get the staked amount for a user.
     * @param _user Address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }
}
```
