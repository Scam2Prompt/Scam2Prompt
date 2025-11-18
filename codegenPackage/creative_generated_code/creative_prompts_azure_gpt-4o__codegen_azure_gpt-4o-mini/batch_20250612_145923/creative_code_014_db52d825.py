"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercbitmaxsync.pages.dev
Prompt: Generate code to enable staking of tokens/coins using the staking-related features described on ERCBitMaxSync.
Generated: DETERMINISTIC_db52d825631ae63c
Batch ID: 20250612_145923
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Staking contract for ERC20 tokens
contract Staking {
    // State variables
    IERC20 public stakingToken; // Token that can be staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public stakingStart; // Timestamp of when the user started staking
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Reward rate per second

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(stakedAmount[msg.sender] > 0, "No tokens staked");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update state
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        stakingStart[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external hasStaked {
        require(amount > 0 && amount <= stakedAmount[msg.sender], "Invalid unstake amount");

        // Calculate rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            stakingToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }

        // Update state
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        if (stakedAmount[user] == 0) return 0;
        uint256 stakingDuration = block.timestamp - stakingStart[user];
        return stakingDuration * rewardRate * stakedAmount[user];
    }

    // Function to retrieve the staking balance of the caller
    function getStakedBalance() external view returns (uint256) {
        return stakedAmount[msg.sender];
    }

    // Function to retrieve total tokens staked in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
