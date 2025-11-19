"""
Generated Code Metadata:
========================
Original URL: https://kenduinu-an.web.app
Prompt: Write a smart contract in Solidity for staking $KENDU tokens as described in the Kendu Inu ecosystem, ensuring users can lock their tokens for rewards and withdraw them after a specified period.
Generated: DETERMINISTIC_37c08c563ab22756
Batch ID: 20250612_153812
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

// Importing the ERC20 interface for interacting with the KENDU token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for KENDU tokens
contract KenduStaking is Ownable {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 startTime;     // Timestamp when the tokens were staked
        uint256 unlockTime;    // Timestamp when the tokens can be withdrawn
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // The KENDU token contract
    IERC20 public kenduToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the KENDU token address and reward rate
    constructor(IERC20 _kenduToken, uint256 _rewardRate) {
        kenduToken = _kenduToken;
        rewardRate = _rewardRate;
    }

    // Function to stake KENDU tokens
    function stake(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(lockDuration > 0, "Lock duration must be greater than 0");

        // Transfer KENDU tokens from the user to the contract
        require(kenduToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake information
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            unlockTime: block.timestamp + lockDuration
        });

        emit Staked(msg.sender, amount, stakes[msg.sender].unlockTime);
    }

    // Function to withdraw staked tokens after the lock period
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");

        // Reset the user's stake information
        uint256 amountToWithdraw = userStake.amount;
        delete stakes[msg.sender];

        // Transfer the staked tokens back to the user
        require(kenduToken.transfer(msg.sender, amountToWithdraw), "Token transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    // Function to calculate rewards based on the staked amount and duration
    function calculateRewards(address user) external view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakedDuration = block.timestamp - userStake.startTime;
        return (stakedDuration * userStake.amount * rewardRate) / 1e18; // Adjust reward calculation as needed
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != kenduToken, "Cannot recover KENDU tokens");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
