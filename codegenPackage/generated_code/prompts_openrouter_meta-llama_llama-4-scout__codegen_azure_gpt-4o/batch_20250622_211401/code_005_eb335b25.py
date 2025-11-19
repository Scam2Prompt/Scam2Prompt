"""
Generated Code Metadata:
========================
Original URL: https://segroegg.gitbook.io
Prompt: "Develop a smart contract to facilitate the staking and claiming of Aethir tokens, incorporating the tokenomics outlined in the Aethir documentation."
Generated: DETERMINISTIC_eb335b2506831e17
Batch ID: 20250622_211401
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
 * @title AethirTokenStaking
 * @dev A smart contract to facilitate staking and claiming of Aethir tokens.
 * Users can stake tokens, earn rewards, and claim their staked tokens along with rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AethirTokenStaking {
    // Address of the Aethir token contract
    IERC20 public immutable aethirToken;

    // Reward rate per second (tokenomics defined in Aethir documentation)
    uint256 public immutable rewardRate;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already claimed
        uint256 lastUpdated; // Timestamp of the last update
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token address and reward rate.
     * @param _aethirToken Address of the Aethir token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _aethirToken, uint256 _rewardRate) {
        require(address(_aethirToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        aethirToken = _aethirToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address user) public view returns (uint256) {
        Stake memory stake = stakes[user];
        if (stake.amount == 0) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - stake.lastUpdated;
        uint256 rewards = (stake.amount * rewardRate * timeElapsed) / 1e18;
        return rewards - stake.rewardDebt;
    }

    /**
     * @dev Function to stake Aethir tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        Stake storage stakeInfo = stakes[msg.sender];

        // Update pending rewards before modifying stake
        uint256 pending = pendingRewards(msg.sender);
        stakeInfo.rewardDebt += pending;

        // Transfer tokens from user to contract
        require(aethirToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        stakeInfo.amount += amount;
        stakeInfo.lastUpdated = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        Stake storage stakeInfo = stakes[msg.sender];

        // Calculate pending rewards
        uint256 pending = pendingRewards(msg.sender);
        require(pending > 0, "No rewards to claim");

        // Update reward debt and last updated timestamp
        stakeInfo.rewardDebt += pending;
        stakeInfo.lastUpdated = block.timestamp;

        // Transfer rewards to user
        require(aethirToken.transfer(msg.sender, pending), "Reward transfer failed");

        emit Claimed(msg.sender, pending);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 pending = pendingRewards(msg.sender);

        // Transfer staked tokens and rewards to user
        uint256 amountToUnstake = stakeInfo.amount;
        require(aethirToken.transfer(msg.sender, amountToUnstake + pending), "Unstake transfer failed");

        // Update contract state
        totalStaked -= stakeInfo.amount;
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, amountToUnstake);
        emit Claimed(msg.sender, pending);
    }
}
```
