"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a Solidity contract for staking Bitcoin ETF Token (BTCETF) that rewards users based on the number of tokens staked.
Generated: DETERMINISTIC_ac6c523fcb89b150
Batch ID: 20250612_163848
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

// Interface for the ERC20 token (BTCETF)
interface IBTCETF {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Staking contract for Bitcoin ETF Token (BTCETF)
contract BTCETFStaking {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // The ERC20 token contract
    IBTCETF public btcEftToken;

    // Reward rate in tokens per second
    uint256 public rewardRate = 1e18; // 1 BTCETF token per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the token contract address
    constructor(address _btcEftToken) {
        btcEftToken = IBTCETF(_btcEftToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to the contract
        require(btcEftToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens and claim rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward based on the time staked
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's stake information
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer the staked tokens and rewards back to the user
        require(btcEftToken.transfer(msg.sender, amountToWithdraw), "Transfer failed");
        require(btcEftToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw, reward);
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        return (stakedDuration * userStake.amount * rewardRate) / 1e18; // Adjust for reward rate
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
