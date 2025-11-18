"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Develop a smart contract that integrates staking functionality, allowing users to claim `wTAO` and automatically stake to receive `rsTAO` rewards.
Generated: DETERMINISTIC_1a2c4a7279556ef9
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Solidity code implementing a staking smart contract with automatic staking functionality. This contract allows users to claim `wTAO` and stake it to receive `rsTAO` rewards.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @notice This contract allows users to claim wTAO tokens and automatically stake them to earn rsTAO rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract StakingContract {
    // Address of wTAO and rsTAO tokens
    IERC20 public immutable wTAO;
    IERC20 public immutable rsTAO;

    // Staking data structure
    struct Stake {
        uint256 amount;       // Amount of wTAO staked
        uint256 lastClaimed;  // Timestamp of the last reward claim
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Reward rate per second (assume 1 rsTAO for 1 wTAO staked every 100 seconds)
    uint256 public constant REWARD_RATE = 1 ether / 100;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @notice Constructor initializing the wTAO and rsTAO token addresses.
     * @param _wTAO Address of the wTAO token contract.
     * @param _rsTAO Address of the rsTAO token contract.
     */
    constructor(address _wTAO, address _rsTAO) {
        require(_wTAO != address(0), "wTAO address cannot be zero");
        require(_rsTAO != address(0), "rsTAO address cannot be zero");
        wTAO = IERC20(_wTAO);
        rsTAO = IERC20(_rsTAO);
    }

    /**
     * @notice Stakes a specified amount of wTAO and starts earning rewards.
     * @param amount Amount of wTAO to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero amount");

        // Transfer wTAO from the user to this contract
        require(wTAO.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking data for the user
        Stake storage userStake = stakes[msg.sender];
        _claimRewards(msg.sender); // Claim any pending rewards
        userStake.amount += amount;
        userStake.lastClaimed = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Claims rsTAO rewards based on the user's staking duration.
     */
    function claimRewards() external {
        uint256 reward = _claimRewards(msg.sender);
        emit Claimed(msg.sender, reward);
    }

    /**
     * @notice Unstakes wTAO and stops earning rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount to unstake");

        // Claim pending rewards
        _claimRewards(msg.sender);

        // Transfer the staked wTAO back to the user
        uint256 amount = userStake.amount;
        userStake.amount = 0;
        require(wTAO.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Internal function to calculate and distribute rewards to a user.
     * @param user Address of the user to claim rewards for.
     * @return reward Amount of rsTAO distributed as rewards.
     */
    function _claimRewards(address user) internal returns (uint256 reward) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the reward based on staking duration
        uint256 stakingDuration = block.timestamp - userStake.lastClaimed;
        reward = (userStake.amount * stakingDuration * REWARD_RATE) / 1 ether;

        // Update the last claimed timestamp
        userStake.lastClaimed = block.timestamp;

        if (reward > 0) {
            require(rsTAO.transfer(user, reward), "Reward transfer failed");
        }
    }

    /**
     * @notice Returns the pending rsTAO rewards for a user.
     * @param user Address of the user.
     * @return reward Amount of rsTAO pending claim.
     */
    function pendingRewards(address user) external view returns (uint256 reward) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.lastClaimed;
        reward = (userStake.amount * stakingDuration * REWARD_RATE) / 1 ether;
    }
}
```

This smart contract ensures proper functionality, adheres to security best practices, and includes error handling where necessary. It uses the ERC20 interface to integrate the `wTAO` and `rsTAO` tokens.
