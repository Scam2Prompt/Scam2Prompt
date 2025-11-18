"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-app.pages.dev
Prompt: Create a smart contract in Solidity to implement a staking mechanism similar to TrustPad's staking requirements for guaranteed allocations.
Generated: DETERMINISTIC_95295c9c0c23e232
Batch ID: 20250612_152000
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

// Import OpenZeppelin Contracts library for security and standard functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking mechanism
contract StakingPool is Ownable {
    // Staker information structure
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakedAt;
        uint256 rewardsEarned;
    }

    // Mapping from address to Staker information
    mapping(address => Staker) public stakers;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // The ERC20 token being staked
    IERC20 public stakingToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardRate; // Rewards per token staked per second

    // Constructor to set the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Modifier to check if the user has staked
    modifier hasStaked() {
        require(stakers[msg.sender].amountStaked > 0, "You have not staked any tokens.");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0.");
        
        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker information
        Staker storage staker = stakers[msg.sender];
        
        // Claim any existing rewards before adding new stake
        claimRewards();
        
        staker.amountStaked += amount;
        staker.lastStakedAt = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external hasStaked {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount.");
        
        // Claim rewards before unstaking
        claimRewards();
        
        // Update staker information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() public hasStaked {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        
        require(rewards > 0, "No rewards available to claim.");
        
        // Update rewards and last staking time
        staker.rewardsEarned += rewards;
        staker.lastStakedAt = block.timestamp;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a given staker
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 stakedDuration = block.timestamp - staker.lastStakedAt;

        return (staker.amountStaked * rewardRate * stakedDuration) / 1e18; // Adjust for precision
    }

    // Function to withdraw remaining tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        uint256 contractBalance = stakingToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance.");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
