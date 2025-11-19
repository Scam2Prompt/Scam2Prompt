"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ea.pages.dev
Prompt: How can I implement a staking smart contract for DOGE20 on Ethereum to distribute rewards over two years?
Generated: DETERMINISTIC_a06ab84aeead537c
Batch ID: 20250612_161500
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

// Import OpenZeppelin Contracts for safe math and ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Doge20Staking {
    using SafeMath for uint256;

    // The ERC20 token being staked
    IERC20 public doge20Token;

    // Duration for rewards distribution (in seconds)
    uint256 public rewardDuration = 730 days; // 2 years

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already distributed
        uint256 lastTimestamp; // Last timestamp for reward calculation
    }

    // Mapping of addresses to their staking details
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward rate per token staked per second
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address and reward rate
    constructor(address _doge20Token, uint256 _rewardRate) {
        doge20Token = IERC20(_doge20Token);
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens from the sender to this contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate and update rewards before staking
        _updateRewards(msg.sender);

        // Update the staker's information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset reward debt to zero after claiming rewards
        stakers[msg.sender].rewardDebt = 0;

        // Transfer the rewards to the user
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 timeDiff = block.timestamp.sub(staker.lastTimestamp);
        
        // Calculate and update reward debt
        if (staker.amountStaked > 0) {
            uint256 pendingReward = timeDiff.mul(staker.amountStaked).mul(rewardRate).div(1e18);
            staker.rewardDebt = staker.rewardDebt.add(pendingReward);
        }

        // Update the last timestamp to the current block timestamp
        staker.lastTimestamp = block.timestamp;
    }

    // Function to withdraw staked tokens (with rewards)
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Calculate rewards before withdrawal
        _updateRewards(msg.sender);

        // Update the staker's amount staked
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer the withdrawn tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
