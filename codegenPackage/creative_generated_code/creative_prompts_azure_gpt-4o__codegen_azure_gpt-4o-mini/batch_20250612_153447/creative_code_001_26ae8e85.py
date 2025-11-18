"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeu.pages.dev
Prompt: Generate Solidity code for a smart contract that facilitates double staking rewards for $PEPU tokens on Pepe Unchained.
Generated: DETERMINISTIC_26ae8e8553ed9edb
Batch ID: 20250612_153447
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

// Importing the OpenZeppelin ERC20 interface for $PEPU token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Pepe Unchained staking contract
interface IPepeUnchained {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function rewardsOf(address account) external view returns (uint256);
}

// The DoubleStakingRewards contract facilitates double staking rewards for $PEPU tokens
contract DoubleStakingRewards {
    // State variables
    IERC20 public pepuToken; // Reference to the $PEPU token contract
    IPepeUnchained public pepeUnchained; // Reference to the Pepe Unchained staking contract

    mapping(address => uint256) public stakes; // Tracks the amount staked by each user

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifier to check if the caller has staked tokens
    modifier hasStaked() {
        require(stakes[msg.sender] > 0, "No tokens staked");
        _;
    }

    // Constructor to initialize the contract with the $PEPU token and Pepe Unchained staking contract addresses
    constructor(address _pepuToken, address _pepeUnchained) {
        require(_pepuToken != address(0), "Invalid $PEPU token address");
        require(_pepeUnchained != address(0), "Invalid Pepe Unchained address");

        pepuToken = IERC20(_pepuToken);
        pepeUnchained = IPepeUnchained(_pepeUnchained);
    }

    // Function to stake $PEPU tokens in the Pepe Unchained contract
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient $PEPU balance");

        // Transfer $PEPU tokens from user to this contract
        pepuToken.transferFrom(msg.sender, address(this), amount);

        // Update stakes mapping
        stakes[msg.sender] += amount;

        // Stake in Pepe Unchained contract
        pepuUnchained.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $PEPU tokens from the Pepe Unchained contract
    function unstake(uint256 amount) external hasStaked {
        require(amount > 0 && amount <= stakes[msg.sender], "Invalid unstake amount");

        // Unstake from Pepe Unchained contract
        pepeUnchained.unstake(amount);

        // Transfer $PEPU tokens back to user
        pepuToken.transfer(msg.sender, amount);

        // Update stakes mapping
        stakes[msg.sender] -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim staking rewards
    function claimRewards() external hasStaked {
        uint256 rewards = pepeUnchained.rewardsOf(msg.sender);

        require(rewards > 0, "No rewards available");

        // Transfer rewards ($PEPU tokens) to the user
        pepuToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the amount staked by a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to withdraw any $PEPU tokens accidentally sent to this contract
    function withdrawAccidentalTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(pepuToken.balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");

        pepuToken.transfer(msg.sender, amount);
    }
}
```
