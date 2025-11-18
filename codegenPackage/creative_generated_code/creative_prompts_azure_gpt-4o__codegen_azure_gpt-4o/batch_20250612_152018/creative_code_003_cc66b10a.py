"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-befecoin.pages.dev
Prompt: Write a smart contract in Solidity for staking BRISE to earn BEFE tokens, ensuring zero tax implementation as described on the BEFE website.
Generated: DETERMINISTIC_cc66b10a23a2a475
Batch ID: 20250612_152018
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
 * @title Staking Contract for BRISE to Earn BEFE
 * @author [Your Name]
 * @notice This contract allows users to stake BRISE tokens and earn BEFE tokens as rewards.
 * @dev This implementation assumes BEFE reward distribution without any tax deduction.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BRISEStaking {
    // Token addresses
    IERC20 public immutable BRISE;
    IERC20 public immutable BEFE;

    // Admin address
    address public admin;

    // Staker info
    struct Stake {
        uint256 amount; // Amount of BRISE staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    // Mapping to track stakes
    mapping(address => Stake) public stakes;

    // Reward rate (BEFE tokens per block per staked BRISE token)
    uint256 public rewardRate;

    // Total BRISE staked in the contract
    uint256 public totalStaked;

    // Last block number when reward distribution occurred
    uint256 public lastRewardBlock;

    // Accumulated BEFE tokens per staked BRISE token
    uint256 public accRewardPerShare;

    // Events
    event StakeDeposited(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Not authorized");
        _;
    }

    constructor(IERC20 _BRISE, IERC20 _BEFE, uint256 _rewardRate) {
        BRISE = _BRISE;
        BEFE = _BEFE;
        rewardRate = _rewardRate;
        admin = msg.sender;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Updates reward variables to keep them up-to-date.
     */
    function updateRewards() public {
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }
        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 reward = blocksSinceLastReward * rewardRate * totalStaked;
        accRewardPerShare += reward / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Allows users to deposit BRISE tokens to stake.
     * @param amount Amount of BRISE tokens to stake.
     */
    function depositStake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Update rewards before staking
        updateRewards();

        // Transfer BRISE tokens from the user to the contract
        require(BRISE.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // Calculate pending rewards for the user
        uint256 pendingReward = userStake.amount * accRewardPerShare - userStake.rewardDebt;

        // Update user's stake
        userStake.amount += amount;
        userStake.rewardDebt = userStake.amount * accRewardPerShare;

        totalStaked += amount;

        // Send any pending rewards
        if (pendingReward > 0) {
            require(BEFE.transfer(msg.sender, pendingReward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, pendingReward);
        }

        emit StakeDeposited(msg.sender, amount);
    }

    /**
     * @notice Allows users to withdraw their staked BRISE tokens and claim rewards.
     * @param amount Amount of BRISE tokens to withdraw.
     */
    function withdrawStake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update rewards before withdrawal
        updateRewards();

        // Calculate pending rewards for the user
        uint256 pendingReward = userStake.amount * accRewardPerShare - userStake.rewardDebt;

        // Update user's stake
        userStake.amount -= amount;
        userStake.rewardDebt = userStake.amount * accRewardPerShare;

        totalStaked -= amount;

        // Transfer the staked BRISE tokens back to the user
        require(BRISE.transfer(msg.sender, amount), "Token transfer failed");

        // Send any pending rewards
        if (pendingReward > 0) {
            require(BEFE.transfer(msg.sender, pendingReward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, pendingReward);
        }

        emit StakeWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Allows the admin to update the reward rate.
     * @param newRewardRate New reward rate in BEFE tokens per block per staked BRISE token.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyAdmin {
        updateRewards();
        rewardRate = newRewardRate;
    }

    /**
     * @notice Allows the admin to withdraw BEFE tokens from the contract.
     * @param amount Amount of BEFE tokens to withdraw.
     */
    function adminWithdrawBEFE(uint256 amount) external onlyAdmin {
        require(BEFE.transfer(admin, amount), "Token transfer failed");
    }
}
```
