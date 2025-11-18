"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: Provide a code example of a smart contract that integrates MOR token staking with frontend rewards allocation, allowing users to direct emissions to specific smart agents or frontends they prefer.
Generated: DETERMINISTIC_5abd60dc4500b921
Batch ID: 20250612_151329
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

// Importing OpenZeppelin Contracts for ERC20 and SafeMath functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the MOR token
interface IMORToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Smart contract for staking MOR tokens
contract MORStaking {
    using SafeMath for uint256;

    // State variables
    IMORToken public morToken; // The MOR token contract
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of MOR tokens staked
    mapping(address => uint256) public stakedAmount; // Staked amount per user
    mapping(address => uint256) public rewards; // Rewards allocation per user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsAllocated(address indexed user, uint256 amount);

    // Constructor to set the MOR token contract address
    constructor(address _morToken) {
        morToken = IMORToken(_morToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Function to stake MOR tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(morToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedAmount[msg.sender] = stakedAmount[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake MOR tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        stakedAmount[msg.sender] = stakedAmount[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(morToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to allocate rewards to users based on their preferences
    function allocateRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than 0");

        rewards[user] = rewards[user].add(amount);
        morToken.mint(address(this), amount); // Minting rewards to the contract
        emit RewardsAllocated(user, amount);
    }

    // Function to claim allocated rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0; // Reset rewards
        require(morToken.transfer(msg.sender, rewardAmount), "Transfer failed");
    }
}
```
