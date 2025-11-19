"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Develop a smart contract in Solidity for a crypto casino token with a staking rewards system, similar to $TGC, including functions for token staking, reward distribution, and airdrop management.
Generated: DETERMINISTIC_98d1f865caaec905
Batch ID: 20250622_205230
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for the Crypto Casino Token (CCT) with staking and rewards
contract CryptoCasinoToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track staked amounts of each user
    mapping(address => uint256) private _stakedBalances;
    // Mapping to track the last reward distribution time for each user
    mapping(address => uint256) private _lastRewardTime;
    // Total staked amount in the contract
    uint256 private _totalStaked;
    // Reward rate per second (in tokens)
    uint256 public rewardRate;
    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    // Event emitted when airdrop is executed
    event AirdropExecuted(address indexed recipient, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _rewardRate) 
        ERC20(name, symbol) 
    {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract owner
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].add(amount);
        _totalStaked = _totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);
        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].sub(amount);
        _totalStaked = _totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 rewards = _calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update last reward time and total rewards distributed
        _lastRewardTime[msg.sender] = block.timestamp;
        totalRewardsDistributed = totalRewardsDistributed.add(rewards);

        // Mint new tokens as rewards
        _mint(msg.sender, rewards);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        uint256 rewards = _calculateRewards(user);
        if (rewards > 0) {
            _lastRewardTime[user] = block.timestamp; // Update last reward time
        }
    }

    // Internal function to calculate rewards for a user
    function _calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedAmount = _stakedBalances[user];
        uint256 timeStaked = block.timestamp.sub(_lastRewardTime[user]);
        return stakedAmount.mul(rewardRate).mul(timeStaked).div(1e18); // Adjust for precision
    }

    // Function to execute an airdrop to a specific address
    function airdrop(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(totalSupply().add(amount) <= type(uint256).max, "Total supply exceeded");

        // Mint new tokens for the airdrop
        _mint(recipient, amount);
        emit AirdropExecuted(recipient, amount);
    }

    // Function to get the staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount in the contract
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }
}
```
