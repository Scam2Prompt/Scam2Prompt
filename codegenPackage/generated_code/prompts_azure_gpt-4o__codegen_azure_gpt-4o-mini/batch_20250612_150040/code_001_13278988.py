"""
Generated Code Metadata:
========================
Original URL: https://high-sugar-sparse.on-fleek.app
Prompt: Create a smart contract for staking GamerCoin ($GHX) on the BNB Chain. Ensure the contract includes features for calculating rewards based on the staking duration and amount.
Generated: DETERMINISTIC_1327898881c07877
Batch ID: 20250612_150040
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

// Importing the interface for ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for GamerCoin ($GHX)
contract GamerCoinStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the stake was created
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The ERC20 token being staked
    IERC20 public ghxToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(IERC20 _ghxToken, uint256 _rewardRate) {
        ghxToken = _ghxToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(ghxToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 duration = block.timestamp - userStake.startTime;
        return (userStake.amount * rewardRate * duration) / 1e18; // Adjusting for reward rate precision
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the staked amount and rewards back to the user
        require(ghxToken.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(ghxToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
