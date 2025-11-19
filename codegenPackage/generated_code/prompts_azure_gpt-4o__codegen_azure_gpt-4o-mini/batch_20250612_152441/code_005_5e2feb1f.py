"""
Generated Code Metadata:
========================
Original URL: https://starsarena.trade
Prompt: Provide an example of a smart contract that could be used for monetization in a SocialFi application like the one described on starsarena.trade.
Generated: DETERMINISTIC_5e2feb1f5efb1c98
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a SocialFi application monetization
contract SocialFiMonetization is Ownable {
    using SafeMath for uint256;

    // Event emitted when a user earns rewards
    event RewardsEarned(address indexed user, uint256 amount);
    
    // Event emitted when a user withdraws funds
    event FundsWithdrawn(address indexed user, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) private userBalances;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Constructor to initialize the contract with the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to allow users to earn rewards
    function earnRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update user balance
        userBalances[msg.sender] = userBalances[msg.sender].add(amount);
        
        // Emit event for rewards earned
        emit RewardsEarned(msg.sender, amount);
    }

    // Function for users to withdraw their earned rewards
    function withdrawRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] = userBalances[msg.sender].sub(amount);
        
        // Transfer tokens to the user
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit event for funds withdrawn
        emit FundsWithdrawn(msg.sender, amount);
    }

    // Function to check user balance
    function checkBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }

    // Function to allow the owner to withdraw tokens from the contract
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
