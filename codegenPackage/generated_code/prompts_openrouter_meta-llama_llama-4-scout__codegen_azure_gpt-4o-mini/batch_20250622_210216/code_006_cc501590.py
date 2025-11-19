"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-def.web.app
Prompt: Outline a smart contract for a community-driven crypto project like Scotty AI, including functions for token generation, staking, and reward distribution.
Generated: DETERMINISTIC_cc50159023cf9fe2
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// CommunityToken is an ERC20 token that allows for staking and reward distribution
contract CommunityToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track staked amounts of each user
    mapping(address => uint256) private _stakedBalances;
    // Total amount of tokens staked in the contract
    uint256 private _totalStaked;
    // Reward rate per block for stakers
    uint256 public rewardRate = 1e18; // 1 token per block
    // Mapping to track last update block for each user
    mapping(address => uint256) private _lastUpdateBlock;
    // Mapping to track rewards earned by each user
    mapping(address => uint256) private _rewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("CommunityToken", "CTK") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to user
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        // Update rewards before claiming
        _updateRewards(msg.sender);
        
        uint256 reward = _rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards and transfer to user
        _rewards[msg.sender] = 0;
        _transfer(address(this), msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        uint256 blocksPassed = block.number - _lastUpdateBlock[user];
        if (blocksPassed > 0) {
            uint256 reward = blocksPassed * rewardRate * _stakedBalances[user] / 1e18;
            _rewards[user] += reward;
            _lastUpdateBlock[user] = block.number;
        }
    }

    // Function to get the staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount in the contract
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to get the rewards of a user
    function rewardsOf(address user) external view returns (uint256) {
        return _rewards[user];
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
