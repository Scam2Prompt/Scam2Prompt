"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-im.pages.dev
Prompt: Generate Solidity code for a staking contract that allows users to stake $QUBE tokens and earn rewards from the 5% sell tax reward pool, as described on the InQubeta platform.
Generated: DETERMINISTIC_ba2348e3eb0c86e2
Batch ID: 20250612_150228
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

// Import the ERC20 interface to interact with the QUBE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// The StakingContract allows users to stake QUBE tokens and earn rewards
contract StakingContract is Ownable, ReentrancyGuard {
    // Interface for the QUBE token
    IERC20 public qubeToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping from user address to Staker information
    mapping(address => Staker) public stakers;

    // Total amount of staked tokens
    uint256 public totalStaked;

    // Total rewards distributed for the duration of the contract
    uint256 public totalRewards;

    // Sell tax percentage (5% as a multiplier)
    uint256 public constant SELL_TAX_PERCENTAGE = 5; // 5% reward pool

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the QUBE token address
    constructor(address _qubeTokenAddress) {
        require(_qubeTokenAddress != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeTokenAddress);
    }

    // Function to stake QUBE tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(qubeToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update total staked amount and user's staked amount
        totalStaked += _amount;
        staker.amountStaked += _amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake QUBE tokens
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);

        // Update total staked amount and user's staked amount
        totalStaked -= _amount;
        staker.amountStaked -= _amount;

        // Transfer the staked tokens back to the user
        require(qubeToken.transfer(msg.sender, _amount), "Transfer failed");

        // Claim rewards if available
        if (rewards > 0) {
            totalRewards -= rewards;
            require(qubeToken.transfer(msg.sender, rewards), "Reward transfer failed");
            emit RewardClaimed(msg.sender, rewards);
        }

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards based on the user's staked amount
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.amountStaked == 0) {
            return 0;
        }
        
        // Calculate rewards based on the total sell tax pool and user's stake proportion
        uint256 reward = (staker.amountStaked * totalRewards) / totalStaked;
        return reward - staker.rewardDebt;
    }

    // Function to claim rewards (can be invoked separately)
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt += rewards; // Update reward debt

        // Transfer rewards to user
        require(qubeToken.transfer(msg.sender, rewards), "Reward transfer failed");
        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to distribute rewards (to be called by the owner)
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(qubeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        totalRewards += amount;
    }

    // Function to get the user's staked amount
    function getStakedAmount(address _staker) external view returns (uint256) {
        return stakers[_staker].amountStaked;
    }

    // Function to get the user's total rewards
    function getTotalRewards(address _staker) external view returns (uint256) {
        return calculateRewards(_staker);
    }
}
```
