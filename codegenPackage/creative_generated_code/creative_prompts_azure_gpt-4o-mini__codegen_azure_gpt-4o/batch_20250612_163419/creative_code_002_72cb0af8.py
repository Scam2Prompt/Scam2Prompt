"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mypaal.pages.dev
Prompt: Generate a code snippet for a decentralized application (dApp) that allows users to stake $PAAL tokens and view their accrued ETH rewards using the Paal AI staking model.
Generated: DETERMINISTIC_72cb0af8d9a67c8d
Batch ID: 20250612_163419
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
 * @title Paal AI Staking Contract
 * @notice This contract allows users to stake $PAAL tokens and view their accrued ETH rewards.
 */
contract PaalStaking {
    // Interface for the $PAAL token
    IERC20 public paalToken;

    // Reward calculation variables
    uint256 public rewardRate; // Rewards per second per staked token
    uint256 public totalStaked; // Total amount of $PAAL tokens staked

    // Struct to track user staking information
    struct StakeInfo {
        uint256 amount; // Amount of $PAAL tokens staked by the user
        uint256 rewardDebt; // Reward debt to avoid double counting
        uint256 lastStakedTime; // Timestamp of the last staking action
    }

    // Mapping to store staking information for each user
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _paalToken Address of the $PAAL token contract.
     * @param _rewardRate Reward rate in ETH per second per staked token.
     */
    constructor(IERC20 _paalToken, uint256 _rewardRate) {
        paalToken = _paalToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the caller has staked tokens.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Function to calculate the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards in ETH.
     */
    function calculateReward(address user) public view returns (uint256) {
        StakeInfo memory stake = stakes[user];
        uint256 timeStaked = block.timestamp - stake.lastStakedTime;
        return (stake.amount * rewardRate * timeStaked) / 1e18;
    }

    /**
     * @dev Function to stake $PAAL tokens.
     * @param amount Amount of $PAAL tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update user rewards before modifying state
        uint256 pendingReward = calculateReward(msg.sender);
        stakes[msg.sender].rewardDebt += pendingReward;

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;
        totalStaked += amount;

        // Transfer $PAAL tokens from the user to the contract
        require(paalToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $PAAL tokens.
     * @param amount Amount of $PAAL tokens to unstake.
     */
    function unstake(uint256 amount) external hasStake {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        // Update rewards before modifying state
        uint256 pendingReward = calculateReward(msg.sender);
        stakes[msg.sender].rewardDebt += pendingReward;

        // Update staking information
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;
        totalStaked -= amount;

        // Transfer $PAAL tokens back to the user
        require(paalToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim accrued ETH rewards.
     */
    function claimRewards() external hasStake {
        uint256 pendingReward = calculateReward(msg.sender) + stakes[msg.sender].rewardDebt;

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;
        stakes[msg.sender].lastStakedTime = block.timestamp;

        // Transfer ETH rewards to the user
        (bool success, ) = msg.sender.call{value: pendingReward}("");
        require(success, "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Function to receive ETH for reward distribution.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to receive ETH.
     */
    fallback() external payable {}
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
