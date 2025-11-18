"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yetiouro.co
Prompt: Write a Solidity smart contract for token creation that includes mechanisms for community rewards and Play-to-Earn opportunities, as outlined in Yeti Ouro's tokenomics.
Generated: DETERMINISTIC_1f0074a2ee13f3f6
Batch ID: 20250612_154752
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title YetiOuroToken
 * @dev This contract implements a token with community rewards and Play-to-Earn opportunities.
 */
contract YetiOuroToken is ERC20, Ownable {
    // Events for tracking rewards and earnings
    event RewardDistributed(address indexed to, uint256 amount);
    event PlayerEarned(address indexed player, uint256 amount);

    // Reward pool for community rewards
    uint256 public rewardPool;

    // Mapping to track player earnings
    mapping(address => uint256) public playerEarnings;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Tokenomics parameters
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10 ** decimals(); // Initial supply of tokens
    uint256 public constant REWARD_PERCENTAGE = 5; // Percentage to allocate for rewards

    // Modifier to check if the reward pool has enough tokens
    modifier hasRewards() {
        require(rewardPool > 0, "No rewards available");
        _;
    }

    // Constructor to initialize the token
    constructor() ERC20("YetiOuroToken", "YETI") {
        _mint(msg.sender, INITIAL_SUPPLY);
        rewardPool = INITIAL_SUPPLY * REWARD_PERCENTAGE / 100; // Allocate initial reward pool
    }

    /**
     * @dev Function to distribute rewards to a specified address.
     * @param to The address to distribute the reward to.
     * @param amount The amount of tokens to distribute as a reward.
     */
    function distributeReward(address to, uint256 amount) external onlyOwner hasRewards {
        require(amount <= rewardPool, "Insufficient reward pool");
        rewardPool -= amount; // Decrease the reward pool
        _transfer(owner(), to, amount); // Transfer the reward
        emit RewardDistributed(to, amount); // Emit the reward event
    }

    /**
     * @dev Function for players to earn tokens through gameplay.
     * @param player The address of the player earning tokens.
     * @param amount The amount of tokens the player earns.
     */
    function earnTokens(address player, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        playerEarnings[player] += amount; // Track player's earnings
        _mint(player, amount); // Mint the earned tokens
        emit PlayerEarned(player, amount); // Emit the earning event
    }

    /**
     * @dev Function to withdraw unallocated tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Function to get the current reward pool balance.
     * @return The current balance of the reward pool.
     */
    function getRewardPool() external view returns (uint256) {
        return rewardPool;
    }

    /**
     * @dev Function to get the total rewards distributed so far.
     * @return The total amount of rewards distributed.
     */
    function getTotalRewardsDistributed() external view returns (uint256) {
        return totalRewardsDistributed;
    }
}
```
