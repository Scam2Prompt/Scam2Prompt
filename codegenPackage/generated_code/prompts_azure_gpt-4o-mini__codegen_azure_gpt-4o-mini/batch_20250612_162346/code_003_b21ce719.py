"""
Generated Code Metadata:
========================
Original URL: https://apps-greenbitcoin.pages.dev
Prompt: Generate a smart contract for staking $GBTC tokens that rewards users based on their staking duration and prediction accuracy.
Generated: DETERMINISTIC_b21ce719734cbd49
Batch ID: 20250612_162346
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $GBTC tokens
contract GBTCStaking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the stake was created
        uint256 prediction; // User's prediction accuracy score
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The token being staked
    IERC20 public gbtcToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 prediction);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _gbtcToken) {
        gbtcToken = _gbtcToken;
    }

    // Function to stake tokens
    function stake(uint256 amount, uint256 prediction) external {
        require(amount > 0, "Amount must be greater than zero");
        require(gbtcToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        gbtcToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            prediction: prediction
        });

        emit Staked(msg.sender, amount, prediction);
    }

    // Function to calculate rewards based on staking duration and prediction accuracy
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No active stake found");

        // Calculate duration in seconds
        uint256 duration = block.timestamp - userStake.startTime;

        // Reward calculation logic (example: 1 token per day staked + bonus for prediction accuracy)
        uint256 reward = (duration / 1 days) * userStake.amount / 100; // 1% of staked amount per day
        reward += userStake.prediction; // Add prediction score as a bonus

        return reward;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);

        // Reset user's stake information
        delete stakes[msg.sender];

        // Transfer staked tokens and rewards back to the user
        gbtcToken.transfer(msg.sender, userStake.amount);
        gbtcToken.transfer(msg.sender, reward);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(gbtcToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        gbtcToken.transfer(msg.sender, amount);
    }
}
```
