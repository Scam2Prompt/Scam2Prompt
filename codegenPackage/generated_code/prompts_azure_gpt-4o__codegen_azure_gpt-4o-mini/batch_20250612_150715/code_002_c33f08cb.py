"""
Generated Code Metadata:
========================
Original URL: https://tdapp.pages.dev
Prompt: Generate code to implement a staking feature in a DApp, ensuring assets are returned to the user's wallet upon redemption, as described in the staking/harvest section of the webpage.
Generated: DETERMINISTIC_c33f08cb113d8fa1
Batch ID: 20250612_150715
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a decentralized application (DApp)
contract Staking is Ownable {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) private stakes;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are redeemed
    event Redeemed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to redeem staked tokens
    function redeem() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to redeem");

        uint256 amountToRedeem = userStake.amount;

        // Reset user's stake information
        userStake.amount = 0;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amountToRedeem);

        emit Redeemed(msg.sender, amountToRedeem);
    }

    // Function to check the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to check the staking token address
    function getStakingToken() external view returns (address) {
        return address(stakingToken);
    }
}
```
