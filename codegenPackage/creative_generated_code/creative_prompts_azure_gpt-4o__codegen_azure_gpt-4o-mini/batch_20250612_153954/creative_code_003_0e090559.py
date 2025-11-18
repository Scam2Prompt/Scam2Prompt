"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepetoken.network
Prompt: Create a smart contract in Solidity for staking $MIND tokens with dynamic APY rewards, ensuring compatibility with Ethereum-based wallets.
Generated: DETERMINISTIC_0e0905590dc23301
Batch ID: 20250612_153954
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $MIND tokens with dynamic APY rewards
contract MindStaking is Ownable {
    using SafeMath for uint256;

    // Token used for staking
    IERC20 public mindToken;

    // Struct to keep track of each staker's information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt of the staker
        uint256 lastStakedTime; // Timestamp of the last stake
    }

    // Mapping of stakers' addresses to their stakes
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Dynamic APY (annual percentage yield)
    uint256 public apy; // APY in basis points (e.g., 500 for 5%)
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 amount);
    event ApyUpdated(uint256 newApy);

    // Constructor to initialize the token and APY
    constructor(IERC20 _mindToken, uint256 _initialApy) {
        mindToken = _mindToken;
        apy = _initialApy;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        
        // Transfer tokens from the user to the contract
        mindToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update staker's information
        staker.amount = staker.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);
        staker.lastStakedTime = block.timestamp;
        
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");
        
        // Calculate rewards before unstaking
        _updateRewards(msg.sender);

        // Update staker's information
        staker.amount = staker.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to the user
        mindToken.transfer(msg.sender, _amount);
        
        emit Unstaked(msg.sender, _amount);
    }

    // Function to withdraw rewards
    function withdrawRewards() external {
        _updateRewards(msg.sender);
        
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;
        
        require(reward > 0, "No rewards to withdraw");
        
        // Reset reward debt before transferring
        staker.rewardDebt = 0;

        // Transfer rewards to the user (assuming rewards are also in $MIND tokens)
        mindToken.transfer(msg.sender, reward);
        
        emit RewardWithdrawn(msg.sender, reward);
    }

    // Internal function to update rewards
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        
        // Calculate the reward based on staked amount and APY
        uint256 duration = block.timestamp.sub(staker.lastStakedTime);
        uint256 reward = staker.amount.mul(apy).mul(duration).div(365 days).div(10000); // Dividing by 10000 to convert basis points

        // Update the reward debt
        staker.rewardDebt = staker.rewardDebt.add(reward);
        staker.lastStakedTime = block.timestamp;
    }

    // Function to update the APY (only owner)
    function updateApy(uint256 _newApy) external onlyOwner {
        apy = _newApy;
        emit ApyUpdated(_newApy);
    }

    // Function to get staker's information
    function getStakerInfo(address _staker) external view returns (uint256 amount, uint256 rewardDebt) {
        Staker memory staker = stakers[_staker];
        return (staker.amount, staker.rewardDebt);
    }
}
```
