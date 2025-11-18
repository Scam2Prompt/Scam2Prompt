"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Write a smart contract in Solidity to integrate WienerAI's staking mechanism, allowing users to stake $WAI tokens and earn rewards.
Generated: DETERMINISTIC_0cdc8505c8fbea6c
Batch ID: 20250612_152240
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

// Import the OpenZeppelin ERC20 contract interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WienerAI Staking Contract
 * @dev This contract allows users to stake WAI tokens and earn rewards.
 */
contract WienerAIStaking is Ownable {
    // The WAI token being staked
    IERC20 public waiToken;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 timestamp;   // Time of staking
        uint256 rewards;     // Accumulated rewards
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total rewards distributed
    uint256 public totalRewards;

    // Reward rate per token per second (example: 1 token for every 1 second per staked token)
    uint256 public rewardRate = 1e18; // Using 18 decimals for precision

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the WAI token address.
     * @param _waiToken Address of the WAI token contract.
     */
    constructor(address _waiToken) {
        require(_waiToken != address(0), "Invalid token address");
        waiToken = IERC20(_waiToken);
    }

    /**
     * @dev Allows users to stake WAI tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(waiToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update the user's rewards before staking
        updateRewards(msg.sender);

        // Transfer the specified amount of tokens from the user to the contract
        waiToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     */
    function withdraw() external {
        require(stakes[msg.sender].amount > 0, "No staked tokens");

        // Update the user's rewards before withdrawal
        updateRewards(msg.sender);

        uint256 amount = stakes[msg.sender].amount;

        // Reset user's stake amount to zero
        stakes[msg.sender].amount = 0;

        // Transfer the staked tokens back to the user
        waiToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 rewards = stakes[msg.sender].rewards;
        require(rewards > 0, "No rewards to claim");

        // Reset user's rewards to zero
        stakes[msg.sender].rewards = 0;

        // Transfer rewards to the user
        waiToken.transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user to update rewards for.
     */
    function updateRewards(address user) internal {
        Stake storage stakeInfo = stakes[user];

        // Calculate the duration for which the tokens have been staked
        uint256 duration = block.timestamp - stakeInfo.timestamp;

        // Calculate the new rewards
        stakeInfo.rewards += (stakeInfo.amount * rewardRate * duration) / 1e18;

        // Update the timestamp for the last stake
        stakeInfo.timestamp = block.timestamp;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRate The new reward rate.
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
