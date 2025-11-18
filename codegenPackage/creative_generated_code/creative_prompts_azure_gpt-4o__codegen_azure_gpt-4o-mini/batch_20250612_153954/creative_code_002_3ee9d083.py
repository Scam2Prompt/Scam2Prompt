"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldmobiletokenupgrade.pages.dev
Prompt: Create a smart contract on Ethereum that allows users to stake WMTx tokens and earn rewards as described in the World Mobile Token staking mechanism.
Generated: DETERMINISTIC_3ee9d0837c21c5da
Batch ID: 20250612_153954
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WMTxStaking
 * @dev A smart contract for staking WMTx tokens and earning rewards.
 */
contract WMTxStaking is Ownable {
    IERC20 public immutable wmtxToken; // The WMTx token contract
    uint256 public rewardRate; // Reward rate per token staked
    uint256 public constant REWARD_MULTIPLIER = 1e18; // For reward calculation precision

    struct Stake {
        uint256 amount; // Amount of WMTx staked
        uint256 rewards; // Accumulated rewards
        uint256 lastUpdated; // Last timestamp when rewards were updated
    }

    mapping(address => Stake) public stakes; // User stakes mapping

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the WMTx token address and reward rate.
     * @param _wmtxToken Address of the WMTx token contract.
     * @param _rewardRate Initial reward rate for staking.
     */
    constructor(address _wmtxToken, uint256 _rewardRate) {
        require(_wmtxToken != address(0), "Invalid WMTx token address");
        wmtxToken = IERC20(_wmtxToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake WMTx tokens to earn rewards.
     * @param amount Amount of WMTx tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(wmtxToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update rewards for the user before staking
        _updateRewards(msg.sender);

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked WMTx tokens.
     * @param amount Amount of WMTx tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update rewards for the user before withdrawing
        _updateRewards(msg.sender);

        stakes[msg.sender].amount -= amount;
        require(wmtxToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accrued rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].rewards;
        require(rewards > 0, "No rewards to claim");

        stakes[msg.sender].rewards = 0;
        require(wmtxToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage stakeData = stakes[user];
        uint256 timeStaked = block.timestamp - stakeData.lastUpdated;

        // Calculate rewards
        uint256 accruedRewards = (stakeData.amount * rewardRate * timeStaked) / REWARD_MULTIPLIER;
        stakeData.rewards += accruedRewards;
        stakeData.lastUpdated = block.timestamp;
    }

    /**
     * @dev Set a new reward rate. Only callable by the owner.
     * @param newRewardRate New reward rate for staking.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Function to view the user's total rewards.
     * @param user Address of the user.
     * @return Total rewards for the user.
     */
    function viewRewards(address user) external view returns (uint256) {
        Stake memory stakeData = stakes[user];
        uint256 timeStaked = block.timestamp - stakeData.lastUpdated;
        
        uint256 accruedRewards = (stakeData.amount * rewardRate * timeStaked) / REWARD_MULTIPLIER;
        return stakeData.rewards + accruedRewards;
    }
}
```
