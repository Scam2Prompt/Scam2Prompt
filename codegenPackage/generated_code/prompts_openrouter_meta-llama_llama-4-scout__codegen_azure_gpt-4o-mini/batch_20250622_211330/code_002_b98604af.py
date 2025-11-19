"""
Generated Code Metadata:
========================
Original URL: https://mauvworld.pages.dev
Prompt: Generate a Solidity code snippet for a simple staking contract that locks tokens for a specified period, similar to the staking allocation in the MAUW tokenomics.
Generated: DETERMINISTIC_b98604affe1e702a
Batch ID: 20250622_211330
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for locking tokens for a specified period
contract StakingContract is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 unlockTime;    // Time when the tokens can be unlocked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // The ERC20 token being staked
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens for a specified duration
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Set the unlock time for the stake
        uint256 unlockTime = block.timestamp + duration;

        // Update the user's stake
        stakes[msg.sender] = Stake(amount, unlockTime);

        // Emit the Staked event
        emit Staked(msg.sender, amount, unlockTime);
    }

    // Function to withdraw staked tokens after the unlock time
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];

        // Check if the user has a stake
        require(userStake.amount > 0, "No tokens to withdraw");
        require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the staked tokens back to the user
        stakingToken.transfer(msg.sender, userStake.amount);

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, userStake.amount);
    }

    // Function to check the stake of a user
    function getStake(address user) external view returns (uint256 amount, uint256 unlockTime) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.unlockTime);
    }
}
```
