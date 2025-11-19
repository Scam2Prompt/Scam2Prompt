"""
Generated Code Metadata:
========================
Original URL: https://memekombat-chain.pages.dev
Prompt: Generate a smart contract in Solidity for handling $MK token transactions, staking, and rewards distribution on the Binance Smart Chain (BSC).
Generated: DETERMINISTIC_f4d935863f0549f8
Batch ID: 20250622_205751
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MKToken is an ERC20 token with staking and rewards distribution functionality
contract MKToken is ERC20, Ownable {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Mapping to track last reward distribution time for each staker
    mapping(address => uint256) private _lastRewardTime;
    // Total staked amount
    uint256 private _totalStaked;
    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // 1 MK token per second
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MK Token", "MK") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        uint256 reward = _calculateRewards(user);
        if (reward > 0) {
            _lastRewardTime[user] = block.timestamp;
            _mint(user, reward); // Mint rewards to the user
            emit RewardsClaimed(user, reward);
        }
    }

    // Internal function to calculate rewards for a user
    function _calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedAmount = _stakedBalances[user];
        uint256 timeStaked = block.timestamp - _lastRewardTime[user];
        return (stakedAmount * timeStaked * rewardRate) / 1e18; // Adjusting for reward rate
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
