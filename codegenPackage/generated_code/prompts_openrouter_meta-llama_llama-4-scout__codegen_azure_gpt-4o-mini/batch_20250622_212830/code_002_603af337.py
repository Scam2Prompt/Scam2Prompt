"""
Generated Code Metadata:
========================
Original URL: https://looksrare.tech
Prompt: "Design a staking mechanism for an NFT marketplace using LOOKS tokens, including staking contracts and reward distribution."
Generated: DETERMINISTIC_603af3373d9f59e8
Batch ID: 20250622_212830
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

// Importing OpenZeppelin's ERC20 interface for LOOKS token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for LOOKS tokens
contract NFTStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of LOOKS tokens staked
    uint256 public totalStaked;

    // LOOKS token contract
    IERC20 public looksToken;

    // Reward rate per second (in LOOKS tokens)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _looksToken, uint256 _rewardRate) {
        looksToken = _looksToken;
        rewardRate = _rewardRate;
    }

    // Function to stake LOOKS tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(looksToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update the staker's reward debt before staking
        updateReward(msg.sender);

        // Transfer LOOKS tokens from the staker to the contract
        looksToken.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.add(amount);
        stakers[msg.sender].lastStakedTime = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake LOOKS tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's reward debt before unstaking
        updateReward(msg.sender);

        // Transfer LOOKS tokens back to the staker
        looksToken.transfer(msg.sender, amount);

        // Update staker information
        stakers[msg.sender].amountStaked = stakers[msg.sender].amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateReward(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset the reward debt to zero after claiming
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the staker
        looksToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update the reward for a staker
    function updateReward(address staker) internal {
        Staker storage user = stakers[staker];
        if (user.amountStaked > 0) {
            uint256 timeStaked = block.timestamp.sub(user.lastStakedTime);
            uint256 reward = timeStaked.mul(rewardRate).mul(user.amountStaked).div(1e18);
            user.rewardDebt = user.rewardDebt.add(reward);
        }
        user.lastStakedTime = block.timestamp;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != looksToken, "Cannot withdraw staked token");
        token.transfer(msg.sender, amount);
    }
}
```
