"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcointoken.pages.dev
Prompt: Provide an example of a smart contract for staking Green Bitcoin ($GBTC) that incorporates gamification elements for user engagement.
Generated: DETERMINISTIC_1e62090e86d66ab0
Batch ID: 20250612_140246
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GreenBitcoinStaking
 * @dev A smart contract for staking Green Bitcoin ($GBTC) with gamification elements.
 */
contract GreenBitcoinStaking is Ownable {
    using SafeMath for uint256;

    IERC20 public gbtcToken; // Reference to the GBTC token contract

    struct Stake {
        uint256 amount; // Amount of GBTC staked
        uint256 timestamp; // Time of staking
        uint256 rewards; // Rewards accumulated
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    mapping(address => uint256) public lastClaimed; // Last claimed reward timestamp

    uint256 public rewardRatePerSecond = 1e18; // Reward rate per second
    uint256 public totalStaked; // Total GBTC staked in the contract

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the GBTC token address.
     * @param _gbtcToken Address of the Green Bitcoin token contract.
     */
    constructor(address _gbtcToken) {
        gbtcToken = IERC20(_gbtcToken);
    }

    /**
     * @dev Allows users to stake GBTC.
     * @param amount Amount of GBTC to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user stakes
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their GBTC and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No funds staked");

        uint256 rewards = calculateRewards(msg.sender);
        uint256 amountToUnstake = userStake.amount;

        // Reset the user's stake
        userStake.amount = 0;
        totalStaked = totalStaked.sub(amountToUnstake);

        // Transfer GBTC back and any rewards
        require(gbtcToken.transfer(msg.sender, amountToUnstake), "Transfer failed");
        if (rewards > 0) {
            require(gbtcToken.transfer(msg.sender, rewards), "Reward transfer failed");
            emit RewardsClaimed(msg.sender, rewards);
        }

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Calculates the rewards for a user based on staking duration.
     * @param user Address of the user to calculate rewards for.
     * @return The calculated rewards.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp.sub(userStake.timestamp);
        return timeStaked.mul(rewardRatePerSecond).add(userStake.rewards);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update the user's reward data
        stakes[msg.sender].timestamp = block.timestamp;
        stakes[msg.sender].rewards = 0;

        // Transfer the rewards
        require(gbtcToken.transfer(msg.sender, rewards), "Reward transfer failed");
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update the reward rate. Only owner can call this.
     * @param newRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRatePerSecond = newRate;
    }
}
```
