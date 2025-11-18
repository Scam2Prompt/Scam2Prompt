"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Generate Solidity code for a staking smart contract that supports $POODL tokens, allowing users to lock their tokens and earn rewards at an annual rate of 79%.
Generated: DETERMINISTIC_78ab2f98085afc51
Batch ID: 20250612_153400
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

// Import the ERC20 interface for interacting with the $POODL token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking $POODL tokens to earn rewards.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    // Using a struct to hold information about each stake
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The ERC20 token being staked (POODL token)
    IERC20 public token;

    // Annual reward rate expressed in percentage
    uint256 public constant REWARD_RATE = 79; // 79% annual reward rate

    // Events for logging purposes
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @param _token The address of the $POODL token contract
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Stakes a specified amount of $POODL tokens.
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes the user's tokens and calculates rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward based on the time staked
        uint256 reward = calculateReward(msg.sender);
        uint256 amountToUnstake = userStake.amount;

        // Reset user stake to zero before transferring tokens to prevent reentrancy
        userStake.amount = 0;

        // Transfer back the staked tokens and rewards to the user
        token.transfer(msg.sender, amountToUnstake + reward);

        emit Unstaked(msg.sender, amountToUnstake, reward);
    }

    /**
     * @dev Calculates the reward for a specific user.
     * @param user The address of the user
     * @return The calculated reward amount
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * REWARD_RATE * stakingDuration) / (365 days * 100);
        return reward;
    }

    /**
     * @dev Allows the owner to withdraw any tokens sent to this contract by mistake.
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        token.transfer(msg.sender, amount);
    }
}
```
