"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyo-sushi.lat
Prompt: Write a Solidity smart contract to automate staking and unstaking XYO tokens on SushiSwap, ensuring rewards are collected.
Generated: DETERMINISTIC_8b77ed561c1f434e
Batch ID: 20250612_153954
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the SushiSwap MasterChef
interface IMasterChef {
    function deposit(uint256 _pid, uint256 _amount) external;
    function withdraw(uint256 _pid, uint256 _amount) external;
    function pendingSushi(uint256 _pid, address _user) external view returns (uint256);
}

// XYOStaking contract to handle staking and unstaking XYO tokens on SushiSwap
contract XYOStaking is ReentrancyGuard, Ownable {
    // State variables
    IERC20 public xyoToken; // The XYO token
    IMasterChef public masterChef; // SushiSwap MasterChef contract
    uint256 public poolId; // Pool ID for the staking pool

    // Mapping to track staked amounts per user
    mapping(address => uint256) public stakedAmount;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _xyoToken, IMasterChef _masterChef, uint256 _poolId) {
        xyoToken = _xyoToken;
        masterChef = _masterChef;
        poolId = _poolId;
    }

    // Function to stake XYO tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(xyoToken.balanceOf(msg.sender) >= _amount, "Insufficient XYO balance");

        // Transfer XYO tokens from user to the contract
        xyoToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update the user's staked amount
        stakedAmount[msg.sender] += _amount;

        // Deposit the tokens into the SushiSwap MasterChef
        masterChef.deposit(poolId, _amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake XYO tokens and collect rewards
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= _amount, "Insufficient staked amount");

        // Withdraw the tokens from the SushiSwap MasterChef
        masterChef.withdraw(poolId, _amount);
        
        // Update the user's staked amount
        stakedAmount[msg.sender] -= _amount;

        // Transfer the tokens back to the user
        xyoToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim pending rewards
    function claimRewards() external nonReentrant {
        uint256 pending = masterChef.pendingSushi(poolId, msg.sender);
        require(pending > 0, "No rewards to claim");

        // Logic to transfer the rewards (to be implemented based on SushiSwap reward token)

        emit RewardsClaimed(msg.sender, pending);
    }

    // Function to get the user's total staked amount
    function getUserStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != xyoToken, "Cannot withdraw staked token");
        token.transfer(msg.sender, amount);
    }
}
```
