"""
Generated Code Metadata:
========================
Original URL: https://sun-dv6.pages.dev
Prompt: "Create a SunSwap V2 farm with SUN-USDT LP and APY UP TO 21.51%, using Solidity and TRON blockchain."
Generated: DETERMINISTIC_564be4f505b1dc3f
Batch ID: 20250622_210856
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the SUN-USDT LP token
interface ISunUsdtLP {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Main contract for the SunSwap V2 farm
contract SunSwapFarm is Ownable {
    // State variables
    ISunUsdtLP public sunUsdtLP; // SUN-USDT LP token contract
    uint256 public apy; // Annual Percentage Yield
    uint256 public totalStaked; // Total amount staked in the farm
    mapping(address => uint256) public stakedAmount; // Amount staked by each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _sunUsdtLP, uint256 _apy) {
        require(_sunUsdtLP != address(0), "Invalid LP token address");
        require(_apy > 0, "APY must be greater than 0");
        
        sunUsdtLP = ISunUsdtLP(_sunUsdtLP);
        apy = _apy;
    }

    // Function to stake LP tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer LP tokens from user to the contract
        require(sunUsdtLP.transfer(address(this), amount), "Transfer failed");
        
        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake LP tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer LP tokens back to the user
        require(sunUsdtLP.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on staked amount and APY
    function calculateRewards(address user) public view returns (uint256) {
        // Simple reward calculation based on APY and staked amount
        return (stakedAmount[user] * apy) / 100; // APY is assumed to be in percentage
    }

    // Function to claim rewards (not implemented in this example)
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Logic to distribute rewards would go here

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to update APY (only owner can update)
    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY > 0, "APY must be greater than 0");
        apy = newAPY;
    }
}
```
