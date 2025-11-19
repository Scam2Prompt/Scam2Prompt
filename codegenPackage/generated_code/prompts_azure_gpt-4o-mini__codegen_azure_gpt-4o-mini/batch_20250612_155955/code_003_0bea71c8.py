"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe.pages.dev
Prompt: Explain how to implement a smart contract for the MIND of Pepe token that allows for staking and rewards distribution.
Generated: DETERMINISTIC_0bea71c80def56c0
Batch ID: 20250612_155955
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

// The MIND of Pepe token contract
contract MindOfPepeToken is ERC20, Ownable {
    // Mapping to track staked balances of each user
    mapping(address => uint256) private _stakedBalances;
    // Total amount of tokens staked
    uint256 private _totalStaked;
    // Reward rate per block for stakers
    uint256 public rewardRate = 1e18; // 1 token per block
    // Mapping to track rewards for each user
    mapping(address => uint256) private _rewards;
    // Last block number when rewards were updated for each user
    mapping(address => uint256) private _lastUpdateBlock;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MIND of Pepe", "MIND") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
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
        uint256 reward = _rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for the user
        _rewards[msg.sender] = 0;
        _transfer(address(this), msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        uint256 blocksPassed = block.number - _lastUpdateBlock[user];
        if (blocksPassed > 0) {
            uint256 reward = _stakedBalances[user] * rewardRate * blocksPassed / 1e18;
            _rewards[user] += reward;
            _lastUpdateBlock[user] = block.number;
        }
    }

    // Function to get the staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to get the rewards of a user
    function rewardsOf(address user) external view returns (uint256) {
        return _rewards[user];
    }
}
```
