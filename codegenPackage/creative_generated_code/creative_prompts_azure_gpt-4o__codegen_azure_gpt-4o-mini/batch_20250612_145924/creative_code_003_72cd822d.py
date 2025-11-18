"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: Create a smart contract on the Base chain that supports cross-pool staking programs for $MAFIA tokens and other meme coin projects.
Generated: DETERMINISTIC_72cd822d893a8d43
Batch ID: 20250612_145924
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

// Import the required libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the staking contract
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Smart contract for cross-pool staking of $MAFIA tokens and other meme coins
contract CrossPoolStaking is Ownable, ReentrancyGuard {
    // Events for logging staking and withdrawal actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Mapping of user balances
    mapping(address => uint256) private balances;
    
    // The token to be staked
    IERC20 public stakingToken;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Constructor to set the staking token
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    // Function to stake tokens into the contract
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer the tokens from the sender to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user balance and total staked amount
        balances[msg.sender] += amount;
        totalStaked += amount;

        // Emit the staking event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user balance and total staked amount
        balances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the sender
        stakingToken.transfer(msg.sender, amount);

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to withdraw all tokens (only owner)
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer all tokens to the owner
        stakingToken.transfer(owner(), balance);
    }
}
```
