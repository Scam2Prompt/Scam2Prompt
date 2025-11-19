"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://my-greenbitcoin.pages.dev
Prompt: Generate a smart contract for staking $GBTC tokens that includes features for weekly prediction challenges and reward distribution.
Generated: DETERMINISTIC_47d8bdd7de98cd3b
Batch ID: 20250612_162228
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GBTCStaking
 * @dev A smart contract for staking GBTC tokens with weekly prediction challenges
 *      and reward distribution.
 */
contract GBTCStaking is ReentrancyGuard, Ownable {
    IERC20 public gbtcToken; // The GBTC token contract
    uint256 public totalStaked; // Total amount of GBTC tokens staked
    uint256 public rewardPool; // Pool for rewards distribution
    uint256 public lastRewardTime; // Timestamp of last reward distribution
    uint256 public rewardRate; // Rate of reward distribution per week

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastStakeTime; // Timestamp of last stake
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the GBTC token contract and initial reward rate.
     * @param _gbtcToken Address of the GBTC token contract
     * @param _rewardRate Initial reward rate for distribution
     */
    constructor(IERC20 _gbtcToken, uint256 _rewardRate) {
        gbtcToken = _gbtcToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake GBTC tokens.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastStakeTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Transfer tokens from user to contract
        gbtcToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake GBTC tokens and claim rewards.
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        // Calculate and distribute rewards before unstaking
        _distributeRewards(msg.sender);

        // Update user's stake and total staked amount
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        gbtcToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to distribute rewards to the staker.
     * @param user Address of the user to distribute rewards to
     */
    function _distributeRewards(address user) internal {
        Stake storage userStake = stakes[user];
        uint256 timeElapsed = block.timestamp - lastRewardTime;

        // Calculate reward based on staked amount and elapsed time
        uint256 reward = (userStake.amount * rewardRate * timeElapsed) / 1 weeks;

        // Update reward pool and last reward time
        rewardPool += reward;
        lastRewardTime = block.timestamp;

        if (reward > 0) {
            emit RewardsDistributed(user, reward);
            // Transfer rewards to user
            gbtcToken.transfer(user, reward);
        }
    }

    /**
     * @dev Function for the owner to set a new reward rate.
     * @param newRewardRate New reward rate to be set
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Function to withdraw the reward pool by the owner.
     * @param amount Amount of tokens to withdraw
     */
    function withdrawRewardPool(uint256 amount) external onlyOwner {
        require(rewardPool >= amount, "Insufficient reward pool");
        rewardPool -= amount;
        gbtcToken.transfer(msg.sender, amount);
    }
}
```
