"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Using the tokenomics details provided, create a Solidity smart contract for $SCOTTY that includes functionality for staking, presale allocation, and reward distribution.
Generated: DETERMINISTIC_68a4412416238871
Batch ID: 20250612_153420
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

// Import the OpenZeppelin ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ScottyToken is ERC20, Ownable {
    // State variables
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate per block for stakers
    uint256 public presaleAllocation;
    
    // Structure to hold staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeBlock;
    }
    
    // Mapping of addresses to their staking information
    mapping(address => Stake) public stakes;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 reward);

    // Constructor to initialize the token
    constructor(uint256 initialSupply, uint256 _rewardRate, uint256 _presaleAllocation) 
        ERC20("Scotty Token", "$SCOTTY") 
    {
        _mint(msg.sender, initialSupply * 10 ** decimals());
        rewardRate = _rewardRate;
        presaleAllocation = _presaleAllocation;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Update rewards and state
        _updateReward(msg.sender);
        
        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
        
        // Update the staker's information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakeBlock = block.number;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update rewards and state
        _updateReward(msg.sender);

        // Transfer tokens from contract to user
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards
    function distributeRewards() external {
        _updateReward(msg.sender);
    }

    // Internal function to update the rewards for a staker
    function _updateReward(address user) internal {
        Stake storage stakeInfo = stakes[user];
        
        // Calculate pending rewards
        uint256 pendingReward = (block.number - stakeInfo.lastStakeBlock) * rewardRate * stakeInfo.amount / 1e18;
        
        // Update user's reward debt
        stakeInfo.rewardDebt += pendingReward;
        stakeInfo.lastStakeBlock = block.number;

        // Transfer rewards to the user if any
        if (pendingReward > 0) {
            _transfer(address(this), user, pendingReward);
            emit RewardDistributed(user, pendingReward);
        }
    }

    // Function to allocate tokens for presale
    function allocateForPresale(address participant, uint256 amount) external onlyOwner {
        require(amount <= presaleAllocation, "Exceeds presale allocation");
        require(participant != address(0), "Invalid address");

        // Mint the tokens for presale
        _transfer(owner(), participant, amount);
        presaleAllocation -= amount;
    }

    // Function to withdraw remaining tokens after presale
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        _transfer(address(this), owner(), balance);
    }
}
```
