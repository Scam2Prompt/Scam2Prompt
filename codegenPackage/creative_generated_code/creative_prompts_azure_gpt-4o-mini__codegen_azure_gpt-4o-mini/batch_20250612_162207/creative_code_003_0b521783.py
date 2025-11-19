"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verified-greenbitcoin.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the staking and reward distribution for Green Bitcoin ($GBTC) on the Ethereum blockchain.
Generated: DETERMINISTIC_0b521783ca31a6a4
Batch ID: 20250612_162207
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

// Importing the ERC20 interface to interact with the GBTC token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract GreenBitcoinStaking {
    // State variables
    IERC20 public gbtcToken; // The GBTC token contract
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastStakedTime; // Last time the user staked
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the GBTC token address and reward rate
    constructor(IERC20 _gbtcToken, uint256 _rewardRate) {
        gbtcToken = _gbtcToken;
        rewardRate = _rewardRate;
    }

    // Function to stake GBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer GBTC tokens from the user to the contract
        gbtcToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staked amount and the last staked time
        stakedAmount[msg.sender] += amount;
        lastStakedTime[msg.sender] = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GBTC tokens and claim rewards
    function unstake(uint256 amount) external {
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate and transfer rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            gbtcToken.transfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer GBTC tokens back to the user
        gbtcToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on staked amount and time
    function calculateReward(address user) public view returns (uint256) {
        uint256 stakingDuration = block.timestamp - lastStakedTime[user];
        return (stakedAmount[user] * stakingDuration * rewardRate) / 1e18; // Using a denominator for precision
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get user's rewards
    function getUserRewards(address user) external view returns (uint256) {
        return calculateReward(user);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
