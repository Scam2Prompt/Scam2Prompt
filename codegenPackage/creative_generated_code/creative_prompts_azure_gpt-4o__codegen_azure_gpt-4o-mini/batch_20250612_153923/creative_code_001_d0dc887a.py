"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-littlerabbits.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with LittleRabbitSwap to automatically stake LTRBT tokens and harvest rewards.
Generated: DETERMINISTIC_d0dc887ad875bba4
Batch ID: 20250612_153923
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

// Importing necessary interfaces for ERC20 and the LittleRabbitSwap staking pool
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the LittleRabbitSwap staking contract
interface ILittleRabbitSwap {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function harvest() external;
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for automatic staking and reward harvesting
contract AutoStaker is Ownable {
    // Instance of the LittleRabbitSwap staking contract
    ILittleRabbitSwap public littleRabbitSwap;
    
    // The LTRBT token contract
    IERC20 public ltrbtToken;

    // Events for logging staking and harvesting actions
    event TokensStaked(uint256 amount);
    event RewardsHarvested(uint256 amount);
    
    // Constructor to set up the token and staking contract addresses
    constructor(address _littleRabbitSwap, address _ltrbtToken) {
        require(_littleRabbitSwap != address(0), "Invalid LittleRabbitSwap address");
        require(_ltrbtToken != address(0), "Invalid LTRBT token address");
        
        littleRabbitSwap = ILittleRabbitSwap(_littleRabbitSwap);
        ltrbtToken = IERC20(_ltrbtToken);
    }

    // Function to stake LTRBT tokens
    function stakeTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(ltrbtToken.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to this contract
        ltrbtToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve the staking contract to spend the tokens
        ltrbtToken.approve(address(littleRabbitSwap), amount);

        // Stake the tokens in the LittleRabbitSwap contract
        littleRabbitSwap.stake(amount);
        
        emit TokensStaked(amount);
    }

    // Function to withdraw staked LTRBT tokens
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        // Withdraw tokens from the staking contract
        littleRabbitSwap.withdraw(amount);
        
        // Transfer tokens back to the owner's address
        ltrbtToken.transfer(msg.sender, amount);
    }

    // Function to harvest rewards from the staking contract
    function harvestRewards() external onlyOwner {
        littleRabbitSwap.harvest();
        
        uint256 rewardBalance = ltrbtToken.balanceOf(address(this));
        emit RewardsHarvested(rewardBalance);
    }

    // Function to check the staked balance of this contract
    function stakedBalance() external view returns (uint256) {
        return littleRabbitSwap.balanceOf(address(this));
    }
}
```
