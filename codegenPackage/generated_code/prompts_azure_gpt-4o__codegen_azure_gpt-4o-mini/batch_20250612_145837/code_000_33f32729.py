"""
Generated Code Metadata:
========================
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Write a smart contract in Solidity for staking $TUK tokens, inspired by the eTukTuk ecosystem, ensuring users can lock tokens and earn rewards based on their stake duration.
Generated: DETERMINISTIC_33f327299e68ae66
Batch ID: 20250612_145837
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

// Importing the ERC20 interface for interacting with the $TUK token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $TUK tokens
contract TukStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 startTime;     // Timestamp when the tokens were staked
        uint256 duration;      // Duration for which tokens are staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The $TUK token contract
    IERC20 public tukToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 duration);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to set the $TUK token address
    constructor(IERC20 _tukToken) {
        tukToken = _tukToken;
    }

    // Function to stake $TUK tokens
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Transfer $TUK tokens from the user to the contract
        require(tukToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake information
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            duration: duration
        });

        emit Staked(msg.sender, amount, duration);
    }

    // Function to calculate rewards based on stake duration
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No active stake found");

        // Calculate the reward based on the duration of the stake
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        if (stakingDuration < userStake.duration) {
            return 0; // No rewards if the staking duration is not met
        }

        // Example reward calculation: 10% of the staked amount for each full duration
        return (userStake.amount * 10 / 100);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Transfer the reward to the user
        require(tukToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Reset the user's stake
        delete stakes[msg.sender];

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to withdraw staked tokens (only after the staking duration)
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(block.timestamp >= userStake.startTime + userStake.duration, "Stake duration not yet completed");

        // Transfer the staked tokens back to the user
        require(tukToken.transfer(msg.sender, userStake.amount), "Token transfer failed");

        // Reset the user's stake
        delete stakes[msg.sender];
    }

    // Function to check the user's stake information
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 startTime, uint256 duration) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.duration);
    }
}
```
