"""
Generated Code Metadata:
========================
Original URL: https://adexnetwork.vercel.app
Prompt: Create a smart contract for staking ADX tokens to support the AdEx ecosystem, incorporating DeFi protocol integration.
Generated: DETERMINISTIC_598176265a501566
Batch ID: 20250612_155032
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for security and token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for ADX tokens
contract AdExStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of ADX tokens staked
        uint256 rewardDebt;   // Reward debt for the staker
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of ADX tokens staked in the contract
    uint256 public totalStaked;

    // The ADX token contract
    IERC20 public adxToken;

    // Reward rate per block (example value, can be adjusted)
    uint256 public rewardRate = 1e18; // 1 ADX per block

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the ADX token address
    constructor(address _adxToken) {
        require(_adxToken != address(0), "Invalid token address");
        adxToken = IERC20(_adxToken);
    }

    // Function to stake ADX tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer ADX tokens from the staker to the contract
        adxToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked ADX tokens
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer ADX tokens back to the staker
        adxToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        return (staker.amountStaked * rewardRate) - staker.rewardDebt;
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update reward debt
        staker.rewardDebt += rewards;

        // Transfer rewards to the staker
        adxToken.transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to set the reward rate (only owner can call)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= adxToken.balanceOf(address(this)), "Insufficient balance");
        adxToken.transfer(msg.sender, _amount);
    }
}
```
