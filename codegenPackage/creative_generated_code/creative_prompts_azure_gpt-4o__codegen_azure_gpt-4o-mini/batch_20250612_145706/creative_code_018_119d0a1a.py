"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Provide a guide for setting up a staking rewards system on a multichain token, ensuring compatibility with wallets like TrustWallet and MetaMask, as described for $FROP.
Generated: DETERMINISTIC_119d0a1a5d27a0c7
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin Contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingRewards contract allows users to stake $FROP tokens and earn rewards.
contract StakingRewards is Ownable {
    // ERC20 token to stake
    ERC20 public stakingToken;

    // Mapping to track staked amounts
    mapping(address => uint256) public stakedAmounts;

    // Rewards per block for staked tokens
    uint256 public rewardsPerBlock;

    // Total staked amount
    uint256 public totalStaked;

    // Events for tracking staking and rewards distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor to initialize staking token and rewards rate
    constructor(ERC20 _stakingToken, uint256 _rewardsPerBlock) {
        stakingToken = _stakingToken;
        rewardsPerBlock = _rewardsPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amounts and total staked
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked amounts and total staked
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) external view returns (uint256) {
        // This can include more complex logic based on time or other factors
        return stakedAmounts[user] * rewardsPerBlock;
    }

    // Function to distribute rewards to user (could be called periodically)
    function distributeRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to distribute");

        // Transfer rewards (assuming rewards are paid in the same token)
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsDistributed(msg.sender, reward);
    }
}
```

### Notes:
- This code leverages OpenZeppelin's libraries to ensure secure and standard implementations of ERC20 and ownership functionalities.
- Proper error handling is in place for token transfers and staking conditions.
- The contract emits events for key actions to facilitate tracking and logging on the blockchain, which is essential for user interfaces and wallet integrations.
- Users can interact with the StakingRewards contract through wallets like TrustWallet and MetaMask, ensuring compatibility with most Ethereum-based wallets.
