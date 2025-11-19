"""
Generated Code Metadata:
========================
Original URL: https://mindofpepetoken.network
Prompt: Explain how to implement a smart contract for the $MIND token that includes features for staking and rewards distribution as outlined in the MIND of Pepe documentation.
Generated: DETERMINISTIC_48395380cc5158c9
Batch ID: 20250612_163030
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract for the $MIND token with staking and rewards distribution
contract MindToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Mapping to track the last reward distribution time for each staker
    mapping(address => uint256) private _lastRewardTime;
    // Total staked amount
    uint256 private _totalStaked;
    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // Example: 1 token per second
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MIND Token", "MIND") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update the staked balance and total staked amount
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);

        // Update the last reward time
        _lastRewardTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the staked balance and total staked amount
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        // Update the last reward time
        _lastRewardTime[msg.sender] = block.timestamp;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update the last reward time
        _lastRewardTime[msg.sender] = block.timestamp;

        // Mint new tokens as rewards
        _mint(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = _stakedBalances[user];
        uint256 lastTime = _lastRewardTime[user];
        uint256 timeStaked = block.timestamp - lastTime;

        // Calculate rewards based on staked amount and time
        return (stakedAmount * rewardRate * timeStaked) / 1e18;
    }

    // Function to get the staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
