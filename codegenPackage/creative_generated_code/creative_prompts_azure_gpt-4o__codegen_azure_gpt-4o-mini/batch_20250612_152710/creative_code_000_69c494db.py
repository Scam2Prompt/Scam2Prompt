"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to stakers over a two-year period, as described on Dogecoin20's website.
Generated: DETERMINISTIC_69c494db87d1620a
Batch ID: 20250612_152710
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

// Importing the required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20Staking is Ownable {
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public rewardRate; // Reward rate per staked token
    uint256 public constant DURATION = 2 * 365 days; // Duration for staking rewards (2 years)
    
    struct Staker {
        uint256 amount; // Amount staked by the user
        uint256 lastRewardTime; // Last reward update time
    }
    
    mapping(address => Staker) public stakers; // Mapping of staker addresses to their information

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the DOGE20 token address
    constructor(address _doge20Token, uint256 _rewardRate) {
        doge20Token = IERC20(_doge20Token);
        rewardRate = _rewardRate;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer DOGE20 tokens from the user to the contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lastRewardTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards();

        // Update the staker's information
        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to the user
        doge20Token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim staking rewards
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        
        require(reward > 0, "No rewards to claim");

        // Update last reward time
        staker.lastRewardTime = block.timestamp;

        // Transfer rewards to the user
        doge20Token.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate the rewards for a staker
    function calculateReward(address stakerAddress) internal view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.amount == 0) return 0;

        uint256 timeStaked = block.timestamp - staker.lastRewardTime;
        return (staker.amount * rewardRate * timeStaked) / DURATION;
    }

    // Function to withdraw remaining tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= doge20Token.balanceOf(address(this)), "Insufficient balance");
        doge20Token.transfer(msg.sender, amount);
    }
}
```
