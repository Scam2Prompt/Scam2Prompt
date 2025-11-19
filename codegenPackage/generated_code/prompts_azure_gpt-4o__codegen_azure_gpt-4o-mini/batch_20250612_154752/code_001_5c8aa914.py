"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Create a smart contract in Solidity that incorporates staking and yield farming mechanisms, aligning with Yeti Ouro's tokenomics and roadmap goals.
Generated: DETERMINISTIC_5c8aa914ae22c75a
Batch ID: 20250612_154752
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token management and ownership control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking and Yield Farming Smart Contract
contract YetiOuroStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the staker
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // The token being staked
    IERC20 public stakingToken;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        updateRewards(msg.sender);

        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update staker's data
        staker.amountStaked += _amount;
        staker.lastStakedTime = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, _amount);
        
        // Update staker's data
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset the reward debt
        staker.rewardDebt = 0;

        // Transfer rewards to the staker
        stakingToken.transfer(msg.sender, reward);
        totalRewards += reward;

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a staker
    function updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;

        // Calculate the reward based on the time staked and the amount staked
        uint256 reward = (staker.amountStaked * rewardRate * timeStaked) / 1e18;

        // Update the staker's reward debt
        staker.rewardDebt += reward;
        staker.lastStakedTime = block.timestamp;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= stakingToken.balanceOf(address(this)), "Insufficient balance");
        stakingToken.transfer(msg.sender, _amount);
    }
}
```
