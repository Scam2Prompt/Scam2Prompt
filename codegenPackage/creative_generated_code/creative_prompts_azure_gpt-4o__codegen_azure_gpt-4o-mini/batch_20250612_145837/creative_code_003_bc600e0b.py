"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-cloudfix.pages.dev
Prompt: Provide an example of using Multichain's veMULTI token staking mechanism in a blockchain-based project.
Generated: DETERMINISTIC_bc600e0bdebcd04a
Batch ID: 20250612_145837
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// This contract demonstrates a simple staking mechanism using veMULTI tokens.
contract veMULTIStaking {
    using SafeMath for uint256;

    // Interface for the veMULTI token
    IERC20 public veMULTI;

    // Mapping to track stake balances of each user
    mapping(address => uint256) public stakes;
    
    // Total staked amount
    uint256 public totalStaked;

    // Events for tracking staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the veMULTI token address
    constructor(address _veMULTIAddress) {
        require(_veMULTIAddress != address(0), "Invalid veMULTI address");
        veMULTI = IERC20(_veMULTIAddress);
    }

    // Function to stake veMULTI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer veMULTI tokens from the user to the contract
        veMULTI.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake balance and total staked amount
        stakes[msg.sender] = stakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake veMULTI tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Not enough staked balance");

        // Update user's stake balance and total staked amount
        stakes[msg.sender] = stakes[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer veMULTI tokens back to the user
        veMULTI.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to get the stake balance of a user
    function getStakeBalance(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to get the total amount staked in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
