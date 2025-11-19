"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Write a script in Solidity to implement a fee-sharing mechanism where 0.05% of each trade is distributed to staked $HEHE token holders.
Generated: DETERMINISTIC_296457f592968c0a
Batch ID: 20250612_153517
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

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Contract for the fee-sharing mechanism
contract FeeSharing {
    // State variables
    IERC20 public token; // The ERC20 token to be distributed
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each holder
    mapping(address => uint256) public lastClaimed; // Last claimed timestamp for each holder

    // Event emitted when fees are distributed
    event FeesDistributed(uint256 amount, uint256 totalStaked);

    // Constructor to set the token address
    constructor(address _token) {
        token = IERC20(_token);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        require(token.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to distribute fees from trades
    function distributeFees(uint256 tradeAmount) external {
        require(tradeAmount > 0, "Trade amount must be greater than 0");
        
        // Calculate fee (0.05% of trade amount)
        uint256 fee = (tradeAmount * 5) / 10000; // 0.05% fee
        require(fee > 0, "Fee must be greater than 0");

        // Emit event before distribution
        emit FeesDistributed(fee, totalStaked);

        // Distribute fees to staked holders
        for (uint256 i = 0; i < totalStaked; i++) {
            address holder = address(uint160(i)); // Placeholder for actual holder address retrieval
            uint256 holderShare = (stakedAmount[holder] * fee) / totalStaked;
            if (holderShare > 0) {
                require(token.transfer(holder, holderShare), "Transfer failed");
            }
        }
    }

    // Function to claim rewards (optional)
    function claimRewards() external {
        // Logic for claiming rewards can be implemented here
        // This can include updating lastClaimed and distributing rewards
    }

    // Function to get the staked amount of a holder
    function getStakedAmount(address holder) external view returns (uint256) {
        return stakedAmount[holder];
    }
}
```
