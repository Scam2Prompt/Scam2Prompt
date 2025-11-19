"""
Generated Code Metadata:
========================
Original URL: https://kaicatclaim.pages.dev
Prompt: Create a step-by-step guide for deploying an ERC20 token on the Ethereum blockchain, ensuring it includes features like staking and token claiming as described in the KAI presale.
Generated: DETERMINISTIC_45436f463cb22b36
Batch ID: 20250612_152249
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract interface
interface IStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimRewards() external;
}

// ERC20 Token with staking and claiming features
contract KAIToken is ERC20, Ownable {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;
    // Reward rate per staked token (in wei)
    uint256 public rewardRate = 100; // Example reward rate
    // Mapping to track rewards for each staker
    mapping(address => uint256) private _rewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("KAI Token", "KAI") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        // Update rewards for the user
        _rewards[msg.sender] += calculateRewards(msg.sender);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _rewards[msg.sender] += calculateRewards(msg.sender);

        // Transfer tokens back to the user
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = _rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for the user
        _rewards[msg.sender] = 0;

        // Transfer rewards to the user
        _mint(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked amount
    function calculateRewards(address user) internal view returns (uint256) {
        return (_stakedBalances[user] * rewardRate) / 1e18; // Adjust reward calculation as needed
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
        return _rewards[user] + calculateRewards(user);
    }
}
```
