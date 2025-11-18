"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbull.io
Prompt: Write code in Solidity to secure $BTCBULL staking rewards using Web3Toolkit technology, ensuring tokens are locked until the end of the Community Sale.
Generated: DETERMINISTIC_4dad5017f9e7cd00
Batch ID: 20250612_154757
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

// Importing interfaces for ERC20 and Ownable from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for securing BTCBULL staking rewards
contract BTCBULLStaking is Ownable {
    // State variables
    IERC20 public btcBullToken; // The ERC20 token to be staked
    uint256 public lockEndTime; // Timestamp when tokens can be unlocked
    mapping(address => uint256) public stakedAmount; // Amount of tokens staked by each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _btcBullToken, uint256 _communitySaleDuration) {
        btcBullToken = _btcBullToken;
        lockEndTime = block.timestamp + _communitySaleDuration; // Setting the lock end time
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(btcBullToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(btcBullToken.allowance(msg.sender, address(this)) >= amount, "Token allowance not sufficient");

        // Transfer tokens from user to contract
        btcBullToken.transferFrom(msg.sender, address(this), amount);

        // Update staked amount
        stakedAmount[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw tokens after lock period
    function withdraw() external {
        require(block.timestamp >= lockEndTime, "Tokens are locked until the end of the Community Sale");
        uint256 amount = stakedAmount[msg.sender];
        require(amount > 0, "No tokens to withdraw");

        // Reset staked amount before transfer to prevent reentrancy
        stakedAmount[msg.sender] = 0;

        // Transfer tokens back to user
        btcBullToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to view staked amount for a user
    function viewStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to check the remaining time until tokens can be unlocked
    function timeUntilUnlock() external view returns (uint256) {
        if (block.timestamp >= lockEndTime) {
            return 0;
        }
        return lockEndTime - block.timestamp;
    }

    // Owner can withdraw any tokens sent to the contract by mistake
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != btcBullToken, "Cannot withdraw staked token");
        token.transfer(msg.sender, amount);
    }
}
```
