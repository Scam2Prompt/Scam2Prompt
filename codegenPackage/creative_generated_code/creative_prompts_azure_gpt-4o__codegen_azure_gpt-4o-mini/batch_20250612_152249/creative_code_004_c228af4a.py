"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Develop a staking protocol in Solidity for a blockchain-based platform like Pushd, allowing users to stake tokens and earn interest ranging from 7% to 17%.
Generated: DETERMINISTIC_c228af4a8f6a704d
Batch ID: 20250612_152249
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

/**
 * @title StakingProtocol
 * @dev This contract allows users to stake tokens and earn interest over time.
 */
contract StakingProtocol is Ownable {
    // Struct to hold staking details for each user
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 interestRate; // Interest rate in basis points (e.g. 700 for 7%)
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // The ERC20 token that users will stake
    IERC20 public stakingToken;

    // Events for logging activity
    event Staked(address indexed user, uint256 amount, uint256 interestRate);
    event Unstaked(address indexed user, uint256 amount, uint256 earnedInterest);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens to earn interest.
     * @param amount The amount of tokens to stake.
     * @param interestRate The interest rate to apply (in basis points).
     */
    function stake(uint256 amount, uint256 interestRate) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(interestRate >= 700 && interestRate <= 1700, "Interest rate must be between 7% and 17%");

        // Transfer the tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            timestamp: block.timestamp,
            interestRate: interestRate
        });

        emit Staked(msg.sender, amount, interestRate);
    }

    /**
     * @dev Unstake tokens and claim earned interest.
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the earned interest
        uint256 earnedInterest = calculateInterest(userStake.amount, userStake.interestRate, userStake.timestamp);
        
        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the original staked amount plus earned interest back to the user
        require(stakingToken.transfer(msg.sender, userStake.amount + earnedInterest), "Token transfer failed");

        emit Unstaked(msg.sender, userStake.amount, earnedInterest);
    }

    /**
     * @dev Calculate the earned interest based on the staked amount, interest rate, and duration.
     * @param amount The amount staked.
     * @param interestRate The interest rate (in basis points).
     * @param timestamp The timestamp when the tokens were staked.
     * @return The calculated interest earned.
     */
    function calculateInterest(uint256 amount, uint256 interestRate, uint256 timestamp) internal view returns (uint256) {
        uint256 duration = block.timestamp - timestamp; // Duration in seconds
        uint256 interest = (amount * interestRate * duration) / (365 days * 10000); // Annual interest calculation
        return interest;
    }

    /**
     * @dev Get the staked amount and interest rate for a user.
     * @param user The address of the user.
     * @return amount The staked amount.
     * @return interestRate The interest rate.
     */
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 interestRate) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.interestRate);
    }
}
```
