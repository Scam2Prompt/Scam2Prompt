"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bimeme.pages.dev
Prompt: Develop a smart contract for MEME token staking and lending, utilizing MEMEex's governance and liquidity pool creation services.
Generated: DETERMINISTIC_de18ca572610b16e
Batch ID: 20250612_150122
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

// Import OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MEME token staking and lending smart contract
contract MEMEStaking is Ownable {
    // ERC20 Token being staked
    ERC20 public memeToken;

    // Structure to hold user's staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (e.g., rewards per block)
    uint256 public rewardRate = 1 ether; // Example value

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the MEME token
    constructor(address _tokenAddress) {
        memeToken = ERC20(_tokenAddress);
    }

    // Function to stake MEME tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(memeToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake MEME tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        require(memeToken.transfer(msg.sender, _amount), "Transfer failed");
        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        require(reward > 0, "No rewards available");
        // Update reward debt before transferring rewards
        staker.rewardDebt += reward;

        // Transfer rewards to staker
        require(memeToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate the reward for a user
    function calculateReward(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];
        return (staker.amountStaked * rewardRate) / 1 ether; // Example calculation
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
