"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claim-akz.pages.dev
Prompt: Write a Solidity smart contract function that calculates early staking incentives for presale buyers of $DOGE20 tokens.
Generated: DETERMINISTIC_0dbb65fa0eb1f09d
Batch ID: 20250612_153420
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

/**
 * @title Doge20Presale
 * @dev Smart contract for early staking incentives for presale buyers of $DOGE20 tokens
 */
contract Doge20Presale {
    // Mapping to store the amount of tokens staked by each address
    mapping(address => uint256) public stakedTokens;
    
    // Total amount of tokens staked
    uint256 public totalStaked;

    // The incentive rate (in percentage) for early stakers
    uint256 public incentiveRate;

    // Event to log staking activity
    event TokensStaked(address indexed buyer, uint256 amount);

    // Constructor to initialize the incentive rate
    constructor(uint256 _incentiveRate) {
        require(_incentiveRate > 0, "Incentive rate must be greater than zero");
        incentiveRate = _incentiveRate;
    }

    /**
     * @dev Function for presale buyers to stake their $DOGE20 tokens.
     * @param amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update the staking balance
        stakedTokens[msg.sender] += amount;
        totalStaked += amount;

        // Emit an event to log the staking activity
        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate the incentive for early stakers.
     * @param user The address of the staker.
     * @return incentive The calculated incentive based on staked amount.
     */
    function calculateIncentive(address user) external view returns (uint256) {
        uint256 stakedAmount = stakedTokens[user];
        require(stakedAmount > 0, "User has no staked tokens");

        // Calculate incentive based on the staked amount and incentive rate
        uint256 incentive = (stakedAmount * incentiveRate) / 100;
        return incentive;
    }

    /**
     * @dev Function to withdraw staked tokens and incentives.
     */
    function withdrawTokens() external {
        uint256 stakedAmount = stakedTokens[msg.sender];
        require(stakedAmount > 0, "No tokens to withdraw");

        // Calculate the incentive
        uint256 incentive = calculateIncentive(msg.sender);

        // Reset the user's staked amount
        stakedTokens[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Send the tokens and incentives back to the user
        // This example assumes the contract holds the tokens; implement token transfer logic appropriately.
        // Token.transfer(msg.sender, stakedAmount + incentive);

        // Emit an event for withdrawal (if required)
        // emit TokensWithdrawn(msg.sender, stakedAmount + incentive);
    }
}
```
