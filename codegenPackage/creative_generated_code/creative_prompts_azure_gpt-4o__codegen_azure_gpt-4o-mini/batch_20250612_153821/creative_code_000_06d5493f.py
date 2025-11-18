"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocket-pool.xyz
Prompt: Write a smart contract in Solidity that integrates Rocket Pool's rETH token into a DeFi protocol, allowing users to stake rETH and earn rewards. Include functionality for calculating rETH/ETH exchange rates based on Rocket Pool's reward distribution mechanism.
Generated: DETERMINISTIC_06d5493fe64c50a2
Batch ID: 20250612_153821
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

// Importing OpenZeppelin's ERC20 interface for rETH token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Rocket Pool rETH token
interface IReth is IERC20 {
    function getRewards() external view returns (uint256);
}

// Smart contract for staking rETH and earning rewards
contract RethStaking {
    // State variables
    IReth public rEthToken; // rETH token contract
    address public owner; // Owner of the contract

    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;

    // Event emitted when a user stakes rETH
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes rETH
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the rETH token address
    constructor(address _rEthToken) {
        rEthToken = IReth(_rEthToken);
        owner = msg.sender; // Set the owner to the contract deployer
    }

    // Function to stake rETH tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(rEthToken.balanceOf(msg.sender) >= amount, "Insufficient rETH balance");

        // Transfer rETH tokens from user to this contract
        rEthToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake
        userStakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake rETH tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(userStakes[msg.sender] >= amount, "Insufficient stake");

        // Update the user's stake before transferring
        userStakes[msg.sender] -= amount;

        // Transfer rETH tokens back to the user
        rEthToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate the rETH/ETH exchange rate
    function calculateExchangeRate() external view returns (uint256) {
        // Get the current rewards available
        uint256 rewards = rEthToken.getRewards();
        // Simplified calculation; should be based on actual distribution logic
        uint256 totalSupply = rEthToken.totalSupply();
        return totalSupply > 0 ? (rewards * 1e18) / totalSupply : 0;
    }

    // Function to allow owner to withdraw rETH tokens from the contract
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= rEthToken.balanceOf(address(this)), "Insufficient balance in contract");
        rEthToken.transfer(owner, amount);
    }

    // Fallback function to prevent accidental Ether deposits
    receive() external payable {
        revert("Direct ETH deposits are not allowed");
    }

    // Function to check the balance of rETH in this contract
    function balanceOfContract() external view returns (uint256) {
        return rEthToken.balanceOf(address(this));
    }
}
```
