"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-en.web.app
Prompt: Create a staking mechanism for the Rebel Satoshi ecosystem that rewards users with percentage returns for locking up their $RBLZ tokens.
Generated: DETERMINISTIC_b5c68a86a1e7b872
Batch ID: 20250612_161616
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A contract for staking $RBLZ tokens with rewards based on the staked amount and duration.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    IERC20 public rblzToken; // The ERC20 token being staked
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5 for 5%)
    
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    /**
     * @dev Constructor to initialize the staking contract.
     * @param _rblzToken Address of the $RBLZ token contract.
     * @param _rewardRate Initial reward rate in percentage.
     */
    constructor(IERC20 _rblzToken, uint256 _rewardRate) {
        rblzToken = _rblzToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake their $RBLZ tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(rblzToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their $RBLZ tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset the user's stake
        userStake.amount = 0;

        // Transfer the staked tokens and rewards back to the user
        require(rblzToken.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Calculates the reward for a user based on their stake and the time staked.
     * @param user Address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp; // Duration in seconds
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (365 days * 100); // Annualized reward

        return reward;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate New reward rate in percentage.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw any tokens accidentally sent to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
