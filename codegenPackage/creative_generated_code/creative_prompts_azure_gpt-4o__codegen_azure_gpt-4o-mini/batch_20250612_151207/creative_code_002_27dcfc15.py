"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eursj.com
Prompt: Generate a Solidity smart contract compatible with Ethereum 2.0 that implements a basic staking mechanism with reward distribution.
Generated: DETERMINISTIC_27dcfc15d2f1bfa7
Batch ID: 20250612_151207
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

// Importing OpenZeppelin's SafeMath for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
// Importing OpenZeppelin's Ownable contract to manage ownership
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Ethereum
contract Staking is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 lastRewardTimestamp; // Last time rewards were updated
        uint256 rewards; // Accumulated rewards
    }

    // Mapping to track each staker's information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (can be adjusted)
    uint256 public rewardRate = 1e18; // 1 token per second per staked token

    // Emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);
    // Emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    
    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update the staker's rewards before staking
        updateRewards(msg.sender);
        
        // Update the total staked amount
        totalStaked = totalStaked.add(_amount);

        // Update the staker's details
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.add(_amount);
        stakers[msg.sender].lastRewardTimestamp = block.timestamp;

        // Transfer tokens from the staker to the contract
        // Assume there is an ERC20 token contract with a transferFrom method
        // Replace 'YourToken' with the actual token contract address
        YourToken token = YourToken(0xYourTokenAddress);
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit TokensStaked(msg.sender, _amount);
    }

    // Function to update rewards for a staker
    function updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp.sub(staker.lastRewardTimestamp);
        if (staker.amountStaked > 0) {
            // Calculate and update the rewards
            uint256 reward = timeStaked.mul(staker.amountStaked).mul(rewardRate).div(1e18);
            staker.rewards = staker.rewards.add(reward);
        }
        
        // Update the last reward timestamp
        staker.lastRewardTimestamp = block.timestamp;
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender); // Update rewards before claiming
        uint256 reward = stakers[msg.sender].rewards;
        require(reward > 0, "No rewards available");

        // Reset the staker's rewards to zero after claiming
        stakers[msg.sender].rewards = 0;

        // Transfer reward tokens to the staker
        YourToken token = YourToken(0xYourTokenAddress);
        require(token.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to withdraw staked tokens (only owner can withdraw)
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= totalStaked, "Cannot withdraw more than staked amount");
        totalStaked = totalStaked.sub(_amount);

        YourToken token = YourToken(0xYourTokenAddress);
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }

    // Function to set reward rate (only owner can call)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}

// Sample ERC20 interface for token interactions
interface YourToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
