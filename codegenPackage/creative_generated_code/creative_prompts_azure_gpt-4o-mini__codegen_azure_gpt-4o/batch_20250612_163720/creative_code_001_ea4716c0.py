"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofinance-claim.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to stake ONDO tokens and earn rewards based on their participation in the Ondo ecosystem.
Generated: DETERMINISTIC_ea4716c0f4ce9d0f
Batch ID: 20250612_163720
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
 * @dev This contract allows users to stake ONDO tokens and earn rewards based on their participation.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Token interface for ONDO
    IERC20 public ondoToken;

    uint256 public rewardRate; // Reward rate per second
    uint256 public constant REWARD_PRECISION = 1e18;

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdated; // Last timestamp the staking info was updated
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the ONDO token and initial reward rate.
     * @param _ondoToken Address of the ONDO token contract.
     * @param _rewardRate Rate at which rewards are earned per token per second.
     */
    constructor(IERC20 _ondoToken, uint256 _rewardRate) {
        ondoToken = _ondoToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake ONDO tokens.
     * @param amount Amount of ONDO tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Update rewards for the user before modifying their stake
        updateRewards(msg.sender);

        // Transfer ONDO tokens to the contract
        require(ondoToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked ONDO tokens.
     * @param amount Amount of ONDO tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        // Update rewards for the user before modifying their stake
        updateRewards(msg.sender);

        // Update staking information
        stakes[msg.sender].amount -= amount;

        // Transfer ONDO tokens back to the user
        require(ondoToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their earned rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);

        uint256 rewardsToClaim = stakes[msg.sender].rewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        stakes[msg.sender].rewards = 0;

        // Transfer rewards to the user
        require(ondoToken.transfer(msg.sender, rewardsToClaim), "Token transfer failed");

        emit RewardClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Updates the reward rate. Only callable by the contract owner.
     * @param _rewardRate New reward rate per token per second.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function updateRewards(address user) internal {
        Stake storage stakeInfo = stakes[user];

        if (stakeInfo.amount > 0) {
            uint256 timeElapsed = block.timestamp - stakeInfo.lastUpdated;
            uint256 newRewards = (stakeInfo.amount * rewardRate * timeElapsed) / REWARD_PRECISION;
            stakeInfo.rewards += newRewards;
        }

        stakeInfo.lastUpdated = block.timestamp;
    }
}
```
