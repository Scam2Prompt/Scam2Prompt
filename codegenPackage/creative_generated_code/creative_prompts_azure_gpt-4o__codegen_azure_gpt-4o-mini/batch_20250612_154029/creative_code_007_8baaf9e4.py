"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-tokens.com
Prompt: Create a tutorial for building a PepeFarm-like staking system using Solidity, ensuring compatibility with the zero-tax tokenomics of $PEPE.
Generated: DETERMINISTIC_8baaf9e45e26b5a5
Batch ID: 20250612_154029
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

// Importing OpenZeppelin contracts for safe math and token interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PepeFarm-like Staking Contract
contract PepeFarm is Ownable {
    // State variables
    IERC20 public pepeToken; // Reference to the Pepe token contract
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    
    // User stakes mapping
    mapping(address => uint256) public stakes; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards accumulated by each user

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the Pepe token
    constructor(address _pepeTokenAddress) {
        require(_pepeTokenAddress != address(0), "Invalid token address");
        pepeToken = IERC20(_pepeTokenAddress);
    }

    // Function to stake Pepe tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(pepeToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake Pepe tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= _amount, "Insufficient stake");

        // Update user's stakes and total staked amount
        stakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        require(pepeToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards (simple implementation)
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available");

        rewards[msg.sender] = 0; // Reset rewards
        require(pepeToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to calculate and distribute rewards (to be called periodically)
    function distributeRewards(address[] calldata _users, uint256[] calldata _rewardAmounts) external onlyOwner {
        require(_users.length == _rewardAmounts.length, "Mismatched input lengths");
        for (uint256 i = 0; i < _users.length; i++) {
            require(_rewardAmounts[i] > 0, "Reward must be greater than zero");
            rewards[_users[i]] += _rewardAmounts[i]; // Accumulate rewards for each user
        }
    }

    // Function to get the user's staked amount
    function getUserStake(address _user) external view returns (uint256) {
        return stakes[_user];
    }
}
```
