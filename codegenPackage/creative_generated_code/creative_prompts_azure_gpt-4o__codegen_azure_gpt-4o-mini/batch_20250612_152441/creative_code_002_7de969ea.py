"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-verification.pages.dev
Prompt: Create a smart contract example for staking SYNTH tokens to earn veSYNTH and access boosted syASSET/ASSET LP farming rewards.
Generated: DETERMINISTIC_7de969ea6a10b7c4
Batch ID: 20250612_152441
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the SYNTH token
interface ISYNTH is IERC20 {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function earned(address account) external view returns (uint256);
}

// Smart contract for staking SYNTH tokens to earn veSYNTH
contract SYNTHStaking is Ownable {
    // State variables
    ISYNTH public synthToken; // The SYNTH token contract
    mapping(address => uint256) public stakedBalances; // User's staked balances
    mapping(address => uint256) public veSYNTHBalances; // User's veSYNTH balances

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event veSYNTHClaimed(address indexed user, uint256 amount);

    // Constructor to set the SYNTH token contract
    constructor(address _synthToken) {
        require(_synthToken != address(0), "Invalid SYNTH token address");
        synthToken = ISYNTH(_synthToken);
    }

    // Function to stake SYNTH tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer SYNTH tokens from user to the contract
        synthToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked balance
        stakedBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked SYNTH tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        
        // Update staked balance
        stakedBalances[msg.sender] -= amount;
        
        // Transfer SYNTH tokens back to the user
        synthToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim veSYNTH rewards
    function claimVeSYNTH() external {
        uint256 earnedAmount = synthToken.earned(msg.sender);
        require(earnedAmount > 0, "No rewards available to claim");

        // Update veSYNTH balance
        veSYNTHBalances[msg.sender] += earnedAmount;

        emit veSYNTHClaimed(msg.sender, earnedAmount);
    }

    // Function to get the user's staked balance
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    // Function to get the user's veSYNTH balance
    function getVeSYNTHBalance(address user) external view returns (uint256) {
        return veSYNTHBalances[user];
    }
}
```
