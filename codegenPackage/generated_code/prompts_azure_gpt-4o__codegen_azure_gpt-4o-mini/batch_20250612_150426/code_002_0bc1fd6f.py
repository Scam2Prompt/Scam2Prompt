"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Create a smart contract in Solidity for managing KI Token rewards based on player activity, including staking and earning mechanisms as described in Genopets.
Generated: DETERMINISTIC_0bc1fd6fa38a3725
Batch ID: 20250612_150426
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// KI Token contract for managing rewards based on player activity
contract KIToken is ERC20, Ownable {
    // Mapping to track staked balances of each player
    mapping(address => uint256) private _stakedBalances;
    // Mapping to track the last reward time for each player
    mapping(address => uint256) private _lastRewardTime;
    // Total staked amount in the contract
    uint256 private _totalStaked;
    // Reward rate per second (in tokens)
    uint256 public rewardRate = 1e18; // 1 KI Token per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("KI Token", "KIT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

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
        uint256 reward = _calculateReward(user);
        if (reward > 0) {
            _mint(user, reward);
            emit RewardsClaimed(user, reward);
        }
        _lastRewardTime[user] = block.timestamp;
    }

    // Internal function to calculate the reward for a user
    function _calculateReward(address user) internal view returns (uint256) {
        uint256 stakedTime = block.timestamp - _lastRewardTime[user];
        return (_stakedBalances[user] * rewardRate * stakedTime) / 1e18; // Adjusting for reward rate
    }

    // Function to get the staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount in the contract
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
