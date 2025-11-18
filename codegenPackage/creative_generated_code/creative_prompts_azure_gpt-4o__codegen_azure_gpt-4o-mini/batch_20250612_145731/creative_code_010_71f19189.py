"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-four-meme.pages.dev
Prompt: Generate a Solidity contract for a meme coin with integrated staking features, inspired by "FOUR DOGE" and "Binance Cat."
Generated: DETERMINISTIC_71f19189c4e43947
Batch ID: 20250612_145731
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoin contract is an ERC20 token with staking features
contract MemeCoin is ERC20, Ownable {
    // Mapping from user address to staked amount
    mapping(address => uint256) private _stakedAmounts;
    // Mapping from user address to staking start time
    mapping(address => uint256) private _stakingStartTime;

    // Total staked amount across all users
    uint256 private _totalStaked;

    // Reward rate per second (in wei) for staked tokens
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the token with name, symbol, and initial supply
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to the owner
        rewardRate = 1e16; // Set reward rate (1 token reward per second per 1 token staked)
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
        
        // Update user's staked amount and staking start time
        _stakedAmounts[msg.sender] += amount;
        _stakingStartTime[msg.sender] = block.timestamp;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(_stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before withdrawal
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward); // Mint the reward tokens
            emit RewardClaimed(msg.sender, reward);
        }

        // Update total staked amount and user staked amount
        _stakedAmounts[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer the staked tokens back to the user
        _transfer(address(this), msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) public view returns (uint256) {
        if (_stakedAmounts[user] == 0) {
            return 0; // No staked amount means no rewards
        }
        // Calculate the duration for which tokens are staked
        uint256 stakingTime = block.timestamp - _stakingStartTime[user];
        return (_stakedAmounts[user] * stakingTime * rewardRate) / 1e18; // calculate reward based on staked amount and time
    }

    // Function to check the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return _stakedAmounts[user];
    }

    // Function to check total staked amount in the contract
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to update reward rate (only callable by the owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
