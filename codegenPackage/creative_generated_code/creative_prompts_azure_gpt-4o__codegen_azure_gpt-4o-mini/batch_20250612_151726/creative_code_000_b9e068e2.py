"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-moonbag-org.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token similar to MoonBag ($MBAG) that includes staking functionality with an APY of 88% and a mechanism to lock liquidity for two years.
Generated: DETERMINISTIC_b9e068e251eeecca
Batch ID: 20250612_151726
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

// Import interfaces and libraries required for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Define the MoonBag token contract
contract MoonBag is ERC20, Ownable, ReentrancyGuard {
    // Constants for staking
    uint256 public constant APY = 88; // Annual Percentage Yield
    uint256 public constant SECONDS_IN_A_YEAR = 365 days;
    uint256 public totalStaked;
    
    // Struct to hold stake information
    struct Stake {
        uint256 amount;
        uint256 reward;
        uint256 lastStakeTime;
    }

    // Mapping of addresses to their stakes
    mapping(address => Stake) private stakes;

    // Liquidity lock information
    uint256 public liquidityLockEndTime;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set initial supply and lock liquidity
    constructor(uint256 initialSupply) ERC20("MoonBag", "$MBAG") {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the deployer
        liquidityLockEndTime = block.timestamp + 730 days; // Lock liquidity for 2 years
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to contract
        transfer(address(this), amount);

        // Update stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;

        // Calculate rewards
        userStake.reward += calculateReward(msg.sender);
        userStake.lastStakeTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        // Calculate total rewards
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset user's stake
        totalStaked -= userStake.amount;
        userStake.amount = 0;
        userStake.reward = 0;

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, totalAmount);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to calculate the reward based on the staked amount and time
    function calculateReward(address staker) public view returns (uint256) {
        Stake storage userStake = stakes[staker];
        uint256 timeStaked = block.timestamp - userStake.lastStakeTime;
        
        // Calculate reward based on the APY
        return (userStake.amount * APY * timeStaked) / (SECONDS_IN_A_YEAR * 100);
    }

    // Function to get the stake information of a user
    function getStakeInfo(address staker) external view returns (uint256 amount, uint256 reward) {
        Stake storage userStake = stakes[staker];
        amount = userStake.amount;
        reward = userStake.reward + calculateReward(staker);
    }

    // Function to check if liquidity is locked
    function isLiquidityLocked() external view returns (bool) {
        return block.timestamp < liquidityLockEndTime;
    }
}
```
