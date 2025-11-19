"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Write a smart contract in Solidity that mimics the functionality of Tenderize's liquid staking process, where users deposit tokens, receive ERC-20 compliant tenderized tokens, and accrue staking rewards dynamically.
Generated: DETERMINISTIC_0b1808712c218d7e
Batch ID: 20250612_145913
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the staking rewards contract
interface IStakingRewards {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function earned(address account) external view returns (uint256);
}

// TenderizeToken is the ERC20 token representing tenderized assets
contract TenderizeToken is ERC20, Ownable {
    // The underlying asset token (e.g., ETH, DAI)
    IERC20 public underlyingToken;
    // Staking rewards contract
    IStakingRewards public stakingRewards;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(
        string memory name,
        string memory symbol,
        address _underlyingToken,
        address _stakingRewards
    ) ERC20(name, symbol) {
        underlyingToken = IERC20(_underlyingToken);
        stakingRewards = IStakingRewards(_stakingRewards);
    }

    // Deposit function to stake underlying tokens and mint tenderized tokens
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer underlying tokens from user to this contract
        underlyingToken.transferFrom(msg.sender, address(this), amount);
        
        // Stake the tokens in the staking rewards contract
        stakingRewards.stake(amount);
        
        // Update user deposits
        userDeposits[msg.sender] += amount;

        // Mint tenderized tokens to the user
        _mint(msg.sender, amount);

        emit Deposited(msg.sender, amount);
    }

    // Withdraw function to redeem tenderized tokens for underlying tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient tenderized token balance");
        
        // Calculate the amount of underlying tokens to withdraw
        uint256 userAmount = userDeposits[msg.sender];
        require(userAmount >= amount, "Insufficient underlying token balance");

        // Burn tenderized tokens from the user
        _burn(msg.sender, amount);

        // Withdraw the underlying tokens from the staking rewards contract
        stakingRewards.withdraw(amount);
        
        // Transfer underlying tokens back to the user
        underlyingToken.transfer(msg.sender, amount);

        // Update user deposits
        userDeposits[msg.sender] -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim staking rewards for the user
    function claimRewards() external {
        uint256 rewards = stakingRewards.earned(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        // Assuming rewards are in the same token as the underlying token
        underlyingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the user's total deposits
    function getUserDeposits(address user) external view returns (uint256) {
        return userDeposits[user];
    }
}
```
