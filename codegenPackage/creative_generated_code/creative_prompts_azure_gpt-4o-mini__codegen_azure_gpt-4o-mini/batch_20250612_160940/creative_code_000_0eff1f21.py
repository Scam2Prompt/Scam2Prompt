"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellowfinance.pages.dev
Prompt: Generate code to implement a permissionless Liquid Restaking Token (LRT) using the Mellow Finance framework, detailing the risk profile and asset selection.
Generated: DETERMINISTIC_0eff1f21fe0a765b
Batch ID: 20250612_160940
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

// Importing necessary interfaces and libraries from Mellow Finance
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Liquid Restaking Token (LRT) Contract
contract LiquidRestakingToken is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public underlyingAsset;  // The underlying asset being staked
    uint256 public totalSupply;      // Total supply of LRT tokens
    mapping(address => uint256) public balanceOf; // Mapping of balances of LRT holders
    mapping(address => uint256) public stakeTimestamp; // Mapping of staking timestamps

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the underlying asset
    constructor(IERC20 _underlyingAsset) {
        underlyingAsset = _underlyingAsset;
    }

    // Function to stake underlying assets and mint LRT tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer underlying asset from user to this contract
        underlyingAsset.transferFrom(msg.sender, address(this), amount);
        
        // Update total supply and user balance
        totalSupply = totalSupply.add(amount);
        balanceOf[msg.sender] = balanceOf[msg.sender].add(amount);
        stakeTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake underlying assets and burn LRT tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(amount <= balanceOf[msg.sender], "Insufficient LRT balance");

        // Update total supply and user balance
        totalSupply = totalSupply.sub(amount);
        balanceOf[msg.sender] = balanceOf[msg.sender].sub(amount);

        // Transfer underlying asset back to user
        underlyingAsset.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards (mock implementation)
    function claimRewards() external {
        // This function would normally calculate rewards based on user's stake duration and amount
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        // Transfer rewards to the user (implement reward token transfer)
        // rewardToken.transfer(msg.sender, rewardAmount); // Uncomment and define rewardToken

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to calculate rewards based on staking duration
    function calculateRewards(address user) internal view returns (uint256) {
        // Logic to calculate rewards based on the time staked and amount staked
        // For demonstration, return a fixed amount (1% of staked amount as rewards)
        return balanceOf[user].mul(block.timestamp.sub(stakeTimestamp[user])).div(1 days).mul(1).div(100);
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= underlyingAsset.balanceOf(address(this)), "Insufficient balance in contract");
        underlyingAsset.transfer(msg.sender, amount);
    }

    // Function to retrieve the underlying asset balance of the contract
    function getUnderlyingAssetBalance() external view returns (uint256) {
        return underlyingAsset.balanceOf(address(this));
    }
}
```
