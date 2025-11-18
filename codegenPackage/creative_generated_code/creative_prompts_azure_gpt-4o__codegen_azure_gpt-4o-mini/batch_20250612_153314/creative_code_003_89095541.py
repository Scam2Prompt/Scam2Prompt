"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasclub.xyz
Prompt: Create a smart contract in Solidity for managing FEG token staking on Binance Smart Chain, considering the transition details discussed.
Generated: DETERMINISTIC_89095541cb61ee25
Batch ID: 20250612_153314
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

// Interface for the FEG Token
interface IFegToken is IERC20 {
    function mint(address account, uint256 amount) external returns (bool);
}

// Staking Contract for FEG Token
contract FEGStaking is Ownable {
    // The FEG token contract
    IFegToken public immutable fegToken;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 stakingStartTime;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the FEG token contract address
    constructor(IFegToken _fegToken) {
        fegToken = _fegToken;
    }

    // Function to stake FEG tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(fegToken.balanceOf(msg.sender) >= amount, "Insufficient FEG token balance");

        // Transfer FEG tokens from the user to the contract
        fegToken.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].stakingStartTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake FEG tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        // Update staker information
        staker.amountStaked -= amount;

        // Transfer FEG tokens back to the user
        fegToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to get the staking duration of a user
    function getStakingDuration(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        require(staker.amountStaked > 0, "No tokens staked");
        return block.timestamp - staker.stakingStartTime;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        uint256 contractBalance = fegToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");
        fegToken.transfer(msg.sender, amount);
    }
}
```
