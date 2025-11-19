"""
Generated Code Metadata:
========================
Original URL: https://pushd-en.pages.dev
Prompt: "Generate a Solidity code for a staking protocol that rewards users with tokens, providing interest rates between 7% to 17% based on the number of tokens held."
Generated: DETERMINISTIC_fb2117dcd0db3d08
Batch ID: 20250622_204704
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

contract StakingProtocol is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The token being staked
    IERC20 public stakingToken;

    // Interest rates based on the amount of tokens held
    uint256 public constant MIN_INTEREST_RATE = 7; // 7%
    uint256 public constant MAX_INTEREST_RATE = 17; // 17%
    uint256 public constant RATE_INCREMENT = 1; // Increment for each token held

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward based on the amount staked
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);

        // Reset user's stake information
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens and rewards back to the user
        stakingToken.transfer(msg.sender, amountToUnstake);
        stakingToken.transfer(msg.sender, reward);

        emit Unstaked(msg.sender, amountToUnstake, reward);
    }

    // Function to calculate the reward based on the amount staked and the time staked
    function calculateReward(uint256 amount, uint256 timestamp) internal view returns (uint256) {
        uint256 duration = block.timestamp - timestamp; // Duration in seconds
        uint256 interestRate = getInterestRate(amount);
        uint256 reward = (amount * interestRate * duration) / (100 * 365 * 24 * 60 * 60); // Annualized reward

        return reward;
    }

    // Function to determine the interest rate based on the amount staked
    function getInterestRate(uint256 amount) internal pure returns (uint256) {
        if (amount < 100 * 10**18) {
            return MIN_INTEREST_RATE; // Less than 100 tokens
        } else if (amount >= 100 * 10**18 && amount < 1000 * 10**18) {
            return MIN_INTEREST_RATE + RATE_INCREMENT; // 100 to 999 tokens
        } else {
            return MAX_INTEREST_RATE; // 1000 tokens or more
        }
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)), "Insufficient balance in contract");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
