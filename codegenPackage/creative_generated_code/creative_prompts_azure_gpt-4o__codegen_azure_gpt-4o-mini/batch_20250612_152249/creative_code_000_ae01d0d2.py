"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-chain.pages.dev
Prompt: Write a smart contract in Solidity for staking $MK tokens on the Meme Kombat platform, ensuring users can earn APY during the presale phase.
Generated: DETERMINISTIC_ae01d0d2fcbe74ad
Batch ID: 20250612_152249
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

// Importing the ERC20 interface for interaction with the $MK token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeKombatStaking is Ownable {
    // Events for logging staking and unstaking activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Variables for staking
    IERC20 public mkToken; // Reference to the $MK token contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public stakingStart; // Start time of the staking period
    uint256 public stakingEnd; // End time of the staking period
    uint256 public apy; // Annual Percentage Yield in basis points (e.g., 500 = 5%)

    // Struct to hold user staking data
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewards; // Accumulated rewards
        uint256 lastStakeTime; // Last time the user staked
    }
    
    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Modifier to check if the staking period is active
    modifier onlyDuringStaking() {
        require(block.timestamp >= stakingStart && block.timestamp <= stakingEnd, "Staking is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _mkToken, uint256 _stakingStart, uint256 _stakingEnd, uint256 _apy) {
        mkToken = _mkToken;
        stakingStart = _stakingStart;
        stakingEnd = _stakingEnd;
        apy = _apy; // Set APY in basis points
    }

    // Function to stake $MK tokens
    function stake(uint256 _amount) external onlyDuringStaking {
        require(_amount > 0, "Amount must be greater than 0");
        require(mkToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's staking data
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.lastStakeTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake $MK tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        staker.rewards += rewards;

        // Update the staker's data
        staker.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(mkToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewardsToClaim = staker.rewards + calculateRewards(msg.sender);
        require(rewardsToClaim > 0, "No rewards to claim");

        // Reset rewards
        staker.rewards = 0;
        staker.lastStakeTime = block.timestamp;

        // Transfer rewards to the user
        require(mkToken.transfer(msg.sender, rewardsToClaim), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    // Internal function to calculate rewards based on staked amount and time
    function calculateRewards(address _staker) internal view returns (uint256) {
        Staker memory staker = stakers[_staker];
        if (staker.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - staker.lastStakeTime;
        // Calculate rewards based on APY
        return (staker.amount * apy * stakingDuration) / (365 days * 10000);
    }

    // Function to withdraw any tokens sent to the contract by mistake
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != mkToken, "Cannot withdraw staked token");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
