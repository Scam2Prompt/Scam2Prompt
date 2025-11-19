"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe.pages.dev
Prompt: Explain how to implement a smart contract for the MIND of Pepe token that allows for staking and rewards distribution.
Generated: DETERMINISTIC_0bea71c80def56c0
Batch ID: 20250612_155955
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

// Importing OpenZeppelin's ERC20 token standard and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the rewards distribution
interface IRewardDistribution {
    function distributeRewards(address recipient, uint256 amount) external;
}

// The MIND of Pepe token contract
contract MindOfPepe is ERC20, Ownable {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total amount staked
    uint256 private _totalStaked;
    // Reward rate (in tokens per block)
    uint256 public rewardRate;
    // Reward distribution contract
    IRewardDistribution public rewardDistribution;

    // Event to emit when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event to emit when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token and reward rate
    constructor(string memory name, string memory symbol, uint256 _rewardRate, address rewardDistributionAddress) 
        ERC20(name, symbol) 
    {
        rewardRate = _rewardRate;
        rewardDistribution = IRewardDistribution(rewardDistributionAddress);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");
        
        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        
        // Update staked balances and total staked
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance to unstake");

        // Update staked balances and total staked
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards
    function calculateRewards(address user) public view returns (uint256) {
        // Simple reward calculation based on staked amount and reward rate
        return _stakedBalances[user] * rewardRate;
    }

    // Function to distribute rewards to stakers
    function distributeRewards() external onlyOwner {
        for (uint256 i = 0; i < _totalStaked; i++) {
            address staker = /* logic to get staker address based on index */;
            uint256 rewards = calculateRewards(staker);
            rewardDistribution.distributeRewards(staker, rewards);
            emit RewardsDistributed(staker, rewards);
        }
    }

    // Function to get staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }
}
``` 

**Note**: The `distributeRewards` function assumes the existence of logic to iterate through stakers which is not implemented in this snippet, as Solidity does not have dynamic arrays for maintaining staker addresses. You would typically implement a separate data structure to maintain a list of stakers in a production environment.
