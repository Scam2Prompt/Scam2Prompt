"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sealanapresale.com
Prompt: Create a Solidity smart contract for staking $HEMI tokens in the Solana ecosystem.
Generated: DETERMINISTIC_b4accc3f2a484981
Batch ID: 20250612_160946
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

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HemiStaking {
    // State variables
    IERC20 public token; // The HEMI token contract
    mapping(address => uint256) public stakes; // Tracks the amount staked by each user
    mapping(address => uint256) public stakeTimestamps; // Tracks when the user staked
    uint256 public totalStaked; // Total amount of HEMI staked in the contract
    uint256 public rewardRate; // Rate at which rewards are calculated

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(address _tokenAddress, uint256 _rewardRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");
        token = IERC20(_tokenAddress);
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= amount, "Token allowance too low");

        // Transfer tokens from user to the contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update stakes and timestamps
        stakes[msg.sender] += amount;
        stakeTimestamps[msg.sender] = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update stakes
        stakes[msg.sender] -= amount;
        totalStaked -= amount;
        
        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to view the staked amount of a user
    function viewStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to view the total amount staked in the contract
    function viewTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to calculate rewards (this can be expanded based on your reward logic)
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakes[user];
        uint256 duration = block.timestamp - stakeTimestamps[user];
        return (stakedAmount * rewardRate * duration) / 1e18; // assuming rewardRate is in wei
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
