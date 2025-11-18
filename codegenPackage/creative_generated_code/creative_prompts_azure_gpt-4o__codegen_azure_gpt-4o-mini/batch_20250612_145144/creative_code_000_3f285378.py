"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-es.web.app
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring double staking rewards functionality.
Generated: DETERMINISTIC_3f28537827c35bee
Batch ID: 20250612_145144
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

// Interface for ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// Staking contract for PEPU tokens
contract PepuStaking {
    // Token to be staked
    IERC20 public pepuToken;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 timestamp;     // Timestamp of staking
        bool doubleReward;     // Flag for double rewards eligibility
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Events for staking and withdrawing
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize the contract with the PEPU token address
    constructor(address _pepuToken) {
        pepuToken = IERC20(_pepuToken);
    }

    // Modifier to check if the user has an active stake
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No active stake found");
        _;
    }

    // Function to stake PEPU tokens
    function stake(uint256 amount, bool doubleReward) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        stakes[msg.sender].doubleReward = doubleReward;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens with rewards
    function withdraw() external hasStake {
        Stake storage userStake = stakes[msg.sender];

        // Calculate rewards based on staked amount and duration
        uint256 rewards = calculateRewards(userStake.amount, userStake.timestamp, userStake.doubleReward);

        // Reset user's stake information
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        // Transfer staked amount and rewards back to the user
        require(pepuToken.transfer(msg.sender, userStake.amount + rewards), "Transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, rewards);
    }

    // Internal function to calculate rewards
    function calculateRewards(uint256 amount, uint256 timestamp, bool doubleReward) internal view returns (uint256) {
        uint256 duration = block.timestamp - timestamp;
        uint256 rewardRate = 100; // Define a base reward rate (e.g., 100 tokens per staked token per year)

        uint256 rewards = (amount * rewardRate * duration) / (365 days);

        // Double rewards if eligible
        if (doubleReward) {
            rewards *= 2;
        }

        return rewards;
    }
}
```
