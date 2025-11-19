"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-befecoin.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to stake BRISE tokens in exchange for BEFE tokens, ensuring zero tax on transactions.
Generated: DETERMINISTIC_2ce8e1a2d4ca6745
Batch ID: 20250612_160720
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

// Importing ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking BRISE tokens to earn BEFE tokens
contract StakingContract is Ownable {
    // Token interfaces
    IERC20 public briseToken;  // BRISE token interface
    IERC20 public befeToken;    // BEFE token interface

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedAmounts;

    // Events for logging activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize token contracts
    constructor(IERC20 _briseToken, IERC20 _befeToken) {
        briseToken = _briseToken;
        befeToken = _befeToken;
    }

    // Function to stake BRISE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(briseToken.balanceOf(msg.sender) >= amount, "Insufficient BRISE balance");

        // Transfer BRISE tokens from user to contract
        briseToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked amount
        stakedAmounts[msg.sender] += amount;
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake BRISE tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount
        stakedAmounts[msg.sender] -= amount;

        // Transfer BRISE tokens back to user
        briseToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim BEFE tokens as a reward
    function claimReward(uint256 amount) external {
        require(stakedAmounts[msg.sender] > 0, "No staked amount to claim rewards from");
        require(befeToken.balanceOf(address(this)) >= amount, "Insufficient BEFE balance in the contract");

        // Transfer BEFE tokens to user
        befeToken.transfer(msg.sender, amount);
        
        emit RewardClaimed(msg.sender, amount);
    }

    // Function to withdraw all BRISE tokens (only owner)
    function withdrawBRISE(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(briseToken.balanceOf(address(this)) >= amount, "Insufficient BRISE balance in the contract");

        // Transfer BRISE tokens to owner
        briseToken.transfer(owner(), amount);
    }

    // Function to withdraw all BEFE tokens (only owner)
    function withdrawBEFE(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(befeToken.balanceOf(address(this)) >= amount, "Insufficient BEFE balance in the contract");

        // Transfer BEFE tokens to owner
        befeToken.transfer(owner(), amount);
    }
}
```
