"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelp-iota.vercel.app
Prompt: Create a smart contract that interacts with rsETH tokens to enable DeFi composability and liquidity on the Kelp platform.
Generated: DETERMINISTIC_9562c9cd3ac08370
Batch ID: 20250612_152358
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

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// Smart contract for interacting with rsETH tokens for DeFi composability on Kelp platform
contract KelpDeFi {
    // Token address for rsETH
    IERC20 public rsETH;

    // Mapping to store user balances
    mapping(address => uint256) public userBalances;

    // Event emitted when user deposits tokens
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the address of the rsETH token contract
    constructor(address _rsETH) {
        require(_rsETH != address(0), "Invalid rsETH address");
        rsETH = IERC20(_rsETH);
    }

    // Function to deposit rsETH tokens into the contract
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than 0");
        
        // Transfer rsETH tokens from the sender to this contract
        bool success = rsETH.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user balance
        userBalances[msg.sender] += amount;

        // Emit deposit event
        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw rsETH tokens from the contract
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance before transferring
        userBalances[msg.sender] -= amount;

        // Transfer rsETH tokens back to the user
        bool success = rsETH.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of rsETH tokens held by the contract
    function contractBalance() external view returns (uint256) {
        return rsETH.balanceOf(address(this));
    }
}
```
