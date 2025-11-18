"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: Generate code for a decentralized application (dApp) that allows users to stake USDC and earn rewards on the Ethereum blockchain.
Generated: DETERMINISTIC_bd06cf3637785d49
Batch ID: 20250612_154002
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the USDC token
interface IUSDC is IERC20 {
    function decimals() external view returns (uint8);
}

// Staking contract
contract USDCStaking is Ownable {
    // Struct to hold user stakes
    struct Stake {
        uint256 amount;      // Amount of USDC staked
        uint256 startTime;   // Timestamp when the stake was created
    }

    // Mapping to hold each user's stakes
    mapping(address => Stake) public stakes;

    // USDC token contract
    IUSDC public usdcToken;

    // Reward rate (in percentage) per staking period (e.g., per day)
    uint256 public rewardRate;

    // Event to emit when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event to emit when a user unstakes
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Modifier to check that the user has staked
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No stake found.");
        _;
    }

    // Constructor to initialize the contract with the USDC token address and reward rate
    constructor(address _usdcToken, uint256 _rewardRate) {
        usdcToken = IUSDC(_usdcToken);
        rewardRate = _rewardRate;
    }

    // Function to stake USDC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0.");

        // Transfer USDC tokens from the user to the contract
        usdcToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake USDC tokens and claim rewards
    function unstake() external hasStake {
        Stake memory userStake = stakes[msg.sender];
        
        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset user's stake data
        delete stakes[msg.sender];

        // Transfer USDC back to the user
        usdcToken.transfer(msg.sender, userStake.amount + reward);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Internal function to calculate the rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 duration = block.timestamp - userStake.startTime;

        // Calculate reward based on the duration and the reward rate
        return (userStake.amount * rewardRate * duration) / (365 days * 100);
    }

    // Function to change the reward rate (only owner can modify)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent directly to the contract
    function withdrawToken(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(usdcToken), "Cannot withdraw staked token.");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```

### Requirements:
1. The contract uses OpenZeppelin's ERC20 and Ownable contracts for security and ownership management.
2. It allows users to stake USDC tokens, calculate rewards, and unstake with rewards.
3. Error handling is included for various scenarios (e.g., no stakes, invalid stake amount).
4. Events are emitted for key actions to allow front-end applications to listen for changes.
