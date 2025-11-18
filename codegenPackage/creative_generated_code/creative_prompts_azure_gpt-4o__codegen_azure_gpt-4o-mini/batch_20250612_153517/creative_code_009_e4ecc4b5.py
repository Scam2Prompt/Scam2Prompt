"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Write a Solidity contract to implement staking functionality for dragon holders, allowing them to earn `$LEGACY` tokens and claim add-ons.
Generated: DETERMINISTIC_e4ecc4b5b66a8db2
Batch ID: 20250612_153517
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

// Importing OpenZeppelin Contracts for security and best practices
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DragonStaking is Ownable {
    using SafeMath for uint256;

    // ERC20 token contract for $LEGACY
    IERC20 public legacyToken;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 lastClaimed;  // Last timestamp when rewards were claimed
    }

    // Mapping of staker address to their staking information
    mapping(address => Staker) public stakers;

    // Reward rate in $LEGACY tokens per second per staked token
    uint256 public rewardRate = 1e18; // 1 $LEGACY token per second per token staked
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the $LEGACY token address
    constructor(address _legacyToken) {
        legacyToken = IERC20(_legacyToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        // Transfer $LEGACY tokens from the user to the contract
        legacyToken.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.lastClaimed = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Cannot unstake 0");
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards();

        // Transfer staked tokens back to the user
        staker.amountStaked = staker.amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);
        legacyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);

        require(rewards > 0, "No rewards to claim");

        // Update last claimed timestamp
        staker.lastClaimed = block.timestamp;

        // Transfer rewards to the user
        legacyToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards earned by a staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp.sub(staker.lastClaimed);
        return staker.amountStaked.mul(rewardRate).mul(timeStaked).div(1e18); // Adjust for rewardRate
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
