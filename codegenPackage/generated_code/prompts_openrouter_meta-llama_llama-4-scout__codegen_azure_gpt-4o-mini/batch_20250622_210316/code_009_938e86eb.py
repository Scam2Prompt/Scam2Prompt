"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Write a Solidity contract for creating a token like TPAD, with features such as staking, rewards, and governance.
Generated: DETERMINISTIC_938e86eb208d17a5
Batch ID: 20250622_210316
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

// Importing OpenZeppelin contracts for ERC20, Ownable, and SafeMath
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the staking contract
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getReward() external;
}

// Main token contract
contract TPADToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;
    // Reward rate (in percentage)
    uint256 public rewardRate = 5; // 5% reward rate
    // Mapping to track rewards
    mapping(address => uint256) private _rewards;

    // Events for staking and rewards
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the token
    constructor() ERC20("TPAD Token", "TPAD") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].add(amount);
        _totalStaked = _totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].sub(amount);
        _totalStaked = _totalStaked.sub(amount);

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get rewards
    function getReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update rewards mapping
        _rewards[msg.sender] = 0;

        // Transfer reward tokens to the user
        _mint(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        return _stakedBalances[user].mul(rewardRate).div(100);
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 rate) external onlyOwner {
        require(rate > 0, "Reward rate must be positive");
        rewardRate = rate;
    }

    // Function to get staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }
}
```
