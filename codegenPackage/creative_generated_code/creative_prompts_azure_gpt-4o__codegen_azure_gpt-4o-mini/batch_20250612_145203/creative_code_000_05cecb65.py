"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ic.pages.dev
Prompt: Write a smart contract in Solidity for staking WienerAI ($WAI) tokens that includes functionality for calculating rewards based on the APY mentioned on the website (1926% p/a).
Generated: DETERMINISTIC_05cecb652e594885
Batch ID: 20250612_145203
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingWAI {
    // Address of the WAI token contract
    IERC20 public waiToken;

    // Annual Percentage Yield (APY) for staking
    uint256 public constant APY = 1926; // 1926% APY

    // Struct to store information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakeTime;
        uint256 rewards;
    }

    // Mapping to hold the staker information
    mapping(address => Staker) public stakers;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the WAI token contract address
    constructor(address _waiToken) {
        require(_waiToken != address(0), "Invalid token address");
        waiToken = IERC20(_waiToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer WAI tokens from the staker to this contract
        require(waiToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards based on the staker's amount and duration
    function calculateRewards(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 duration = block.timestamp - staker.lastStakeTime; // in seconds

        // Calculate the reward based on APY
        uint256 yearlyReward = (staker.amountStaked * APY) / 100; // total reward per year
        uint256 reward = (yearlyReward * duration) / 365 days; // reward for the staked duration

        return reward;
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        
        require(reward > 0, "No rewards to claim");

        // Update rewards and last stake time
        staker.rewards += reward;
        staker.lastStakeTime = block.timestamp;

        // Transfer rewards to the staker
        require(waiToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to get staked amount and accrued rewards
    function getStakerInfo(address _staker) external view returns (uint256 stakedAmount, uint256 rewards) {
        Staker storage staker = stakers[_staker];
        stakedAmount = staker.amountStaked;
        rewards = staker.rewards + calculateRewards(_staker); // Include current accrued rewards
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Calculate rewards before withdrawing
        uint256 reward = calculateRewards(msg.sender);
        staker.rewards += reward;
        staker.lastStakeTime = block.timestamp;

        // Update staked amount
        staker.amountStaked -= _amount;

        // Transfer staked amount back to the staker
        require(waiToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
