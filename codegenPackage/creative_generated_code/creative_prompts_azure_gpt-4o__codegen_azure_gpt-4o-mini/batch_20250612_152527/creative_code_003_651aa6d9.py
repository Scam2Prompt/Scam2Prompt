"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-en.web.app
Prompt: Write a Solidity smart contract to implement staking functionality for $GIGA tokens, allowing users to lock their tokens and earn rewards.
Generated: DETERMINISTIC_651aa6d9ae7c518f
Batch ID: 20250612_152527
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

// Importing SafeERC20 from OpenZeppelin to handle ERC20 tokens safely
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for GIGA tokens
contract StakingGiga is Ownable {
    using SafeERC20 for IERC20;

    // Token to be staked
    IERC20 public immutable gigaToken;

    // Structure to hold user staking data
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 timestamp;      // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second for staking
    uint256 public rewardRate;

    // Events to emit on staking activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    // Constructor to initialize the contract with the GIGA token address and reward rate
    constructor(IERC20 _gigaToken, uint256 _rewardRate) {
        require(address(_gigaToken) != address(0), "Invalid GIGA token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        gigaToken = _gigaToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update user's stake data
        Stake storage userStake = stakes[msg.sender];
        
        // Transfer GIGA tokens from user to contract
        gigaToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update total staked amount and user's stake
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;
        
        // Calculate reward based on staking duration
        return (userStake.amount * rewardRate * (block.timestamp - userStake.timestamp)) / 1e18;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate reward before updating stake
        uint256 reward = calculateReward(msg.sender);
        
        // Update total staked amount and user's stake
        totalStaked -= userStake.amount;
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        
        // Transfer staked tokens back to user
        gigaToken.safeTransfer(msg.sender, amountToWithdraw);
        
        // Transfer rewards to user
        if (reward > 0) {
            payable(msg.sender).transfer(reward);
        }

        emit Unstaked(msg.sender, amountToWithdraw, reward);
    }

    // Function to withdraw rewards directly (can be called if user has staked tokens)
    function withdrawRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to withdraw");

        // Reset timestamp to prevent double claiming
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer rewards to user
        payable(msg.sender).transfer(reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;
    }

    // Function to receive Ether (for rewards distribution)
    receive() external payable {}

    // Fallback function to receive Ether
    fallback() external payable {}
}
```
