"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-site.pages.dev
Prompt: Provide a step-by-step guide to create a staking pool for $PEPU tokens on the Pepe Unchained Layer 2 blockchain, including reward distribution logic.
Generated: DETERMINISTIC_58bcc6da2af35adc
Batch ID: 20250612_153447
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking Pool contract for $PEPU tokens
contract StakingPool is Ownable {
    IERC20 public pepuToken; // ERC20 token instance for $PEPU
    uint256 public totalStaked; // Total amount of tokens staked in the pool
    uint256 public rewardRate; // Reward rate per second per token
    uint256 public lastUpdateTime; // Last time rewards were updated

    // User's staking information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // User's accumulated rewards
    }

    mapping(address => UserInfo) public userInfo; // Mapping of user address to their staking info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking pool
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        pepuToken = _pepuToken; // Set the $PEPU token address
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Modifier to check if the user has staked tokens
    modifier hasStakedTokens(address _user) {
        require(userInfo[_user].amount > 0, "No staked tokens");
        _;
    }

    // Update rewards for a user
    function updateRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];
        uint256 pendingReward = (user.amount * (block.timestamp - lastUpdateTime) * rewardRate) / 1e18;
        user.rewardDebt += pendingReward; // Update the user's reward debt
    }

    // Stake tokens into the pool
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        updateRewards(msg.sender); // Update rewards before staking

        userInfo[msg.sender].amount += _amount; // Update user's staked amount
        totalStaked += _amount; // Update total staked amount

        lastUpdateTime = block.timestamp; // Update last update time

        emit Staked(msg.sender, _amount); // Emit stake event
    }

    // Unstake tokens from the pool
    function unstake(uint256 _amount) external hasStakedTokens(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient staked amount");

        updateRewards(msg.sender); // Update rewards before unstaking

        userInfo[msg.sender].amount -= _amount; // Deduct unstaked amount
        totalStaked -= _amount; // Update total staked amount

        require(pepuToken.transfer(msg.sender, _amount), "Transfer failed"); // Transfer tokens back to the user

        lastUpdateTime = block.timestamp; // Update last update time

        emit Unstaked(msg.sender, _amount); // Emit unstake event
    }

    // Claim rewards for the user
    function claimRewards() external hasStakedTokens(msg.sender) {
        updateRewards(msg.sender); // Update rewards before claiming

        uint256 rewardToClaim = userInfo[msg.sender].rewardDebt; // Get the accumulated rewards
        require(rewardToClaim > 0, "No rewards to claim");

        userInfo[msg.sender].rewardDebt = 0; // Reset the user's reward debt

        require(pepuToken.transfer(msg.sender, rewardToClaim), "Transfer failed"); // Transfer rewards

        emit RewardClaimed(msg.sender, rewardToClaim); // Emit reward claim event
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate; // Update the reward rate
    }

    // Function to withdraw contract's balance (only owner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(pepuToken.transfer(msg.sender, _amount), "Transfer failed"); // Transfer tokens to owner
    }
}
```
