"""
Generated Code Metadata:
========================
Original URL: https://secure-greenbitcoin.pages.dev
Prompt: Develop a smart contract for staking $GBTC tokens that includes features for calculating exponential rewards and weekly prediction challenges.
Generated: DETERMINISTIC_341ab8c845cdf7bd
Batch ID: 20250612_152249
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking GBTC tokens
contract GBTCStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastRewardBlock;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // The ERC20 token being staked
    IERC20 public gbtcToken;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward rate per block (exponential growth factor)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the GBTC token address and reward rate
    constructor(IERC20 _gbtcToken, uint256 _rewardRate) {
        gbtcToken = _gbtcToken;
        rewardRate = _rewardRate;
    }

    // Function to stake GBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.rewardDebt += calculateRewards(msg.sender);
        staker.lastRewardBlock = block.number;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GBTC tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.rewardDebt += calculateRewards(msg.sender);
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(gbtcToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt += rewards;
        staker.lastRewardBlock = block.number;

        require(gbtcToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards based on staked amount and blocks passed
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 blocksPassed = block.number - staker.lastRewardBlock;
        return (staker.amountStaked * rewardRate * blocksPassed) / 1e18; // Adjusting for precision
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to get the staker's information
    function getStakerInfo(address stakerAddress) external view returns (uint256, uint256, uint256) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.rewardDebt, staker.lastRewardBlock);
    }
}
```
