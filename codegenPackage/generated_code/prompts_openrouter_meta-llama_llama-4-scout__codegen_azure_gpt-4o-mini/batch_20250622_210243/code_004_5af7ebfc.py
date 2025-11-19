"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-st.pages.dev
Prompt: "Develop a basic smart contract in Solidity to manage staking rewards and tokenomics for a cryptocurrency like Green Bitcoin ($GBTC)."
Generated: DETERMINISTIC_5af7ebfc384715db
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for Green Bitcoin ($GBTC) staking rewards
contract GreenBitcoin is ERC20, Ownable {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Mapping to track staking timestamps
    mapping(address => uint256) private _stakingTimestamps;
    // Total staked amount
    uint256 private _totalStaked;
    // Reward rate (in tokens per second)
    uint256 public rewardRate = 1e18; // 1 GBTC per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Green Bitcoin", "GBTC") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million GBTC
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update staked balance and total staked amount
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        // Update staking timestamp
        _stakingTimestamps[msg.sender] = block.timestamp;

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate and distribute rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            _mint(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Update staked balance and total staked amount
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens from contract back to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = _stakedBalances[user];
        uint256 stakingDuration = block.timestamp - _stakingTimestamps[user];
        return (stakedAmount * stakingDuration * rewardRate) / 1e18;
    }

    // Function to get the staked balance of a user
    function stakedBalance(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get the total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
