"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcoin.world
Prompt: Create a smart contract in Solidity that distributes 1% daily rewards in USDT to God Token holders, ensuring compatibility with the GBGC chain.
Generated: DETERMINISTIC_81d1a21b0db8cffa
Batch ID: 20250612_154339
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

// Import the interface for the ERC20 token (USDT)
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract GodTokenStaking {
    // State variables
    IERC20 public usdtToken; // USDT token contract
    address public owner; // Contract owner
    uint256 public rewardRate = 1; // Daily reward rate (1%)
    
    // Struct to hold information for each user's stake
    struct Stake {
        uint256 amount; // Amount of God Tokens staked
        uint256 lastClaimed; // Last time rewards were claimed
    }

    // Mapping from user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor(address _usdtToken) {
        usdtToken = IERC20(_usdtToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to stake God Tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer God Tokens from the user to this contract
        // Assuming God Token follows the ERC20 standard
        // IERC20(godToken).transferFrom(msg.sender, address(this), amount);

        // Update the stake for the user
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastClaimed = block.timestamp; // Set the last claimed time to now

        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update the last claimed time
        userStake.lastClaimed = block.timestamp;

        // Transfer USDT rewards to the user
        require(usdtToken.transfer(msg.sender, reward), "USDT transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];

        // Calculate the number of days since last claim
        uint256 daysSinceLastClaim = (block.timestamp - userStake.lastClaimed) / 1 days;

        // Calculate reward based on the stake amount and the reward rate
        uint256 reward = (userStake.amount * rewardRate / 100) * daysSinceLastClaim;

        return reward;
    }

    // Function to withdraw all staked tokens (only owner for this example)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        // Transfer the specified amount of USDT from the contract to the owner
        require(usdtToken.transfer(owner, amount), "USDT transfer failed");
    }

    // Function to check the user's total staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
