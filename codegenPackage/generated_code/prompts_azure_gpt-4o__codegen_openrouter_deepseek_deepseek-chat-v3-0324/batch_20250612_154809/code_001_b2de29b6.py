"""
Generated Code Metadata:
========================
Original URL: https://handsofgod.app
Prompt: Create a smart contract in Solidity for staking $GHOG tokens in the Sanctum module of the Hand of God protocol. Ensure the contract includes a 6-epoch lock for withdrawals and a 3-epoch lock for rewards.
Generated: DETERMINISTIC_b2de29b6e4eadeca
Batch ID: 20250612_154809
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SanctumStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Constants
    uint256 public constant WITHDRAWAL_LOCK_EPOCHS = 6;
    uint256 public constant REWARD_LOCK_EPOCHS = 3;
    uint256 public constant EPOCH_DURATION = 1 weeks;

    // State variables
    IERC20 public ghogToken;
    uint256 public currentEpoch;
    uint256 public lastEpochUpdate;

    // Structs
    struct Stake {
        uint256 amount;
        uint256 stakedAtEpoch;
        uint256 lastClaimedEpoch;
    }

    // Mappings
    mapping(address => Stake) public stakes;
    mapping(uint256 => uint256) public epochRewards; // epoch => reward amount

    // Events
    event Staked(address indexed user, uint256 amount, uint256 epoch);
    event WithdrawalRequested(address indexed user, uint256 amount, uint256 unlockEpoch);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EpochRewardAdded(uint256 epoch, uint256 amount);
    event EpochAdvanced(uint256 newEpoch);

    // Constructor
    constructor(address _ghogToken) {
        require(_ghogToken != address(0), "Invalid token address");
        ghogToken = IERC20(_ghogToken);
        currentEpoch = 1;
        lastEpochUpdate = block.timestamp;
    }

    // Modifiers
    modifier updateEpoch() {
        _updateEpoch();
        _;
    }

    // Internal functions
    function _updateEpoch() internal {
        uint256 epochsPassed = (block.timestamp - lastEpochUpdate) / EPOCH_DURATION;
        if (epochsPassed > 0) {
            currentEpoch += epochsPassed;
            lastEpochUpdate += epochsPassed * EPOCH_DURATION;
            emit EpochAdvanced(currentEpoch);
        }
    }

    function _calculateRewards(address user) internal view returns (uint256) {
        Stake memory stake = stakes[user];
        if (stake.amount == 0 || stake.lastClaimedEpoch >= currentEpoch) {
            return 0;
        }

        uint256 reward = 0;
        uint256 startEpoch = stake.lastClaimedEpoch + 1;
        uint256 endEpoch = currentEpoch;

        for (uint256 epoch = startEpoch; epoch <= endEpoch; epoch++) {
            if (epochRewards[epoch] > 0) {
                reward += (stake.amount * epochRewards[epoch]) / totalStakedAtEpoch(epoch);
            }
        }

        return reward;
    }

    function totalStakedAtEpoch(uint256 epoch) public view returns (uint256) {
        // In a real implementation, this would track historical staked amounts per epoch
        // For simplicity, we'll return current total staked
        return ghogToken.balanceOf(address(this));
    }

    // External functions
    function stake(uint256 amount) external nonReentrant updateEpoch {
        require(amount > 0, "Cannot stake 0");
        
        Stake storage userStake = stakes[msg.sender];
        
        // Claim any pending rewards first
        if (userStake.amount > 0) {
            _claimRewards();
        }

        // Transfer tokens from user
        ghogToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update stake
        if (userStake.amount == 0) {
            userStake.stakedAtEpoch = currentEpoch;
            userStake.lastClaimedEpoch = currentEpoch;
        }
        userStake.amount += amount;

        emit Staked(msg.sender, amount, currentEpoch);
    }

    function requestWithdrawal() external nonReentrant updateEpoch {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");

        // Calculate unlock epoch (current epoch + withdrawal lock)
        uint256 unlockEpoch = currentEpoch + WITHDRAWAL_LOCK_EPOCHS;

        // Claim any pending rewards
        _claimRewards();

        emit WithdrawalRequested(msg.sender, userStake.amount, unlockEpoch);
    }

    function withdraw() external nonReentrant updateEpoch {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");
        
        // Check if withdrawal lock period has passed
        uint256 unlockEpoch = currentEpoch - WITHDRAWAL_LOCK_EPOCHS;
        require(userStake.stakedAtEpoch <= unlockEpoch, "Withdrawal still locked");

        uint256 amount = userStake.amount;
        
        // Reset stake
        userStake.amount = 0;
        userStake.stakedAtEpoch = 0;
        userStake.lastClaimedEpoch = 0;

        // Transfer tokens back to user
        ghogToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    function claimRewards() external nonReentrant updateEpoch {
        _claimRewards();
    }

    function _claimRewards() internal {
        uint256 reward = _calculateRewards(msg.sender);
        if (reward > 0) {
            Stake storage userStake = stakes[msg.sender];
            userStake.lastClaimedEpoch = currentEpoch;

            // Check reward lock
            require(currentEpoch >= userStake.stakedAtEpoch + REWARD_LOCK_EPOCHS, "Rewards still locked");

            ghogToken.safeTransfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    // Admin functions
    function addEpochReward(uint256 amount) external onlyOwner updateEpoch {
        require(amount > 0, "Reward must be > 0");
        ghogToken.safeTransferFrom(msg.sender, address(this), amount);
        epochRewards[currentEpoch] = amount;
        emit EpochRewardAdded(currentEpoch, amount);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = ghogToken.balanceOf(address(this));
        ghogToken.safeTransfer(owner(), balance);
    }
}
```
