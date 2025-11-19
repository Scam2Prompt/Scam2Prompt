"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ai.pages.dev
Prompt: "Design a smart contract for Green Bitcoin ($GBTC) staking and rewards distribution using Solidity, incorporating weekly prediction challenges and tokenomics."
Generated: DETERMINISTIC_5e97b4c92fa6cbd4
Batch ID: 20250622_210243
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

// Green Bitcoin Token Contract
contract GreenBitcoin is ERC20, Ownable {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;
    // Reward rate per week (in percentage)
    uint256 public rewardRate = 5; // 5% weekly rewards
    // Mapping to track last claim time for rewards
    mapping(address => uint256) private _lastClaimed;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Green Bitcoin", "GBTC") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;
        _lastClaimed[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate rewards before unstaking
        _claimRewards();

        // Update staked balance and total staked
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _claimRewards();
    }

    // Internal function to calculate and distribute rewards
    function _claimRewards() internal {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update last claimed time
        _lastClaimed[msg.sender] = block.timestamp;

        // Mint new tokens as rewards
        _mint(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate rewards based on staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = _stakedBalances[user];
        if (stakedAmount == 0) return 0;

        uint256 timeStaked = block.timestamp - _lastClaimed[user];
        uint256 weeksStaked = timeStaked / 1 weeks;

        // Calculate rewards based on the reward rate
        return (stakedAmount * rewardRate * weeksStaked) / 100;
    }

    // Function to get the staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;
    }
}
```
