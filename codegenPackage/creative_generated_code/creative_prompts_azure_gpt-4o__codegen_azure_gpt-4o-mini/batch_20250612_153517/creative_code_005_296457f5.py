"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Write a script in Solidity to implement a fee-sharing mechanism where 0.05% of each trade is distributed to staked $HEHE token holders.
Generated: DETERMINISTIC_296457f592968c0a
Batch ID: 20250612_153517
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the $HEHE token to interact with it
interface IHEHE is IERC20 {
    function stake(address account, uint256 amount) external;
    function unstake(address account, uint256 amount) external;
    function totalStaked() external view returns (uint256);
}

contract FeeSharing is Ownable {
    // $HEHE token contract reference
    IHEHE public heheToken;

    // Mapping to track staked amounts
    mapping(address => uint256) public stakedAmounts;
    // Total staked amount tracker
    uint256 public totalStakedAmount;

    // Event to log the distribution of fees
    event FeesDistributed(uint256 amount);

    // Constructor to set the $HEHE token contract address
    constructor(address _heheToken) {
        require(_heheToken != address(0), "Invalid token address");
        heheToken = IHEHE(_heheToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the tokens to the contract
        heheToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked amounts
        stakedAmounts[msg.sender] += amount;
        totalStakedAmount += amount;

        // Staking in the HEHE token contract
        heheToken.stake(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");
        
        // Update staked amounts
        stakedAmounts[msg.sender] -= amount;
        totalStakedAmount -= amount;

        // Unstaking in the HEHE token contract
        heheToken.unstake(msg.sender, amount);
        
        // Transfer tokens back to the user
        heheToken.transfer(msg.sender, amount);
    }

    // Function to distribute fees from trades
    function distributeFees(uint256 tradeAmount) external onlyOwner {
        require(tradeAmount > 0, "Trade amount must be greater than zero");
        
        // Calculate the fee to distribute (0.05%)
        uint256 feeAmount = (tradeAmount * 5) / 10000; // 0.05%

        // Emit the event for fee distribution
        emit FeesDistributed(feeAmount);

        // Distribute fees to staked holders if there are any staked tokens
        if (totalStakedAmount > 0) {
            for (uint256 i = 0; i < totalStakedAmount; i++) {
                address staker = address(uint160(i)); // Placeholder for staker's address
                uint256 stakerShare = (stakedAmounts[staker] * feeAmount) / totalStakedAmount;
                heheToken.transfer(staker, stakerShare);
            }
        }
    }

    // Function to get the total staked amount for a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStakedAmount;
    }
}
```
