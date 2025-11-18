"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdccash.xyz
Prompt: Generate Solidity code for a smart contract that mimics the functionality of $UPRINT, including automatic USDC reflections to holders based on transaction activity.
Generated: DETERMINISTIC_deb3c8d495f8298c
Batch ID: 20250612_154728
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

/*
 * @title UPRINT-Like Token Contract with USDC Reflections
 * @dev Implements automatic USDC reflections to token holders based on transaction activity.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract UPRINTToken {
    // Token metadata
    string public name = "UPRINT Token";
    string public symbol = "UPRINT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // USDC token contract address
    IERC20 public usdcToken;

    // Reflection percentage (e.g., 5%)
    uint256 public reflectionFee = 5;

    // Mapping of balances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Mapping to keep track of rewards distributed
    mapping(address => uint256) public reflections;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ReflectionDistributed(address indexed account, uint256 amount);

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply, address _usdcToken) {
        totalSupply = _initialSupply * 10**decimals;
        balanceOf[msg.sender] = totalSupply;
        usdcToken = IERC20(_usdcToken);
    }

    // Transfer function with reflection logic
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        // Calculate reflection amount
        uint256 reflectionAmount = (amount * reflectionFee) / 100;
        uint256 transferAmount = amount - reflectionAmount;

        // Distribute reflections
        _distributeReflections(reflectionAmount);

        // Transfer tokens
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += transferAmount;

        emit Transfer(msg.sender, recipient, transferAmount);
        return true;
    }

    // TransferFrom function with reflection logic
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(balanceOf[sender] >= amount, "Insufficient balance");
        require(allowance[sender][msg.sender] >= amount, "Allowance exceeded");

        // Calculate reflection amount
        uint256 reflectionAmount = (amount * reflectionFee) / 100;
        uint256 transferAmount = amount - reflectionAmount;

        // Distribute reflections
        _distributeReflections(reflectionAmount);

        // Transfer tokens
        balanceOf[sender] -= amount;
        balanceOf[recipient] += transferAmount;
        allowance[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, transferAmount);
        return true;
    }

    // Approve function
    function approve(address spender, uint256 amount) public returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Internal function to distribute reflections
    function _distributeReflections(uint256 reflectionAmount) internal {
        uint256 totalTokens = totalSupply;
        if (totalTokens == 0 || reflectionAmount == 0) {
            return;
        }

        // Iterate over token holders and distribute USDC
        for (uint256 i = 0; i < totalTokens; i++) {
            address holder = address(i); // Placeholder logic for holder enumeration
            uint256 holderBalance = balanceOf[holder];
            if (holderBalance > 0) {
                uint256 holderReflection = (reflectionAmount * holderBalance) / totalTokens;
                reflections[holder] += holderReflection;

                // Transfer USDC to the holder
                require(
                    usdcToken.transfer(holder, holderReflection),
                    "Failed to transfer USDC reflections"
                );

                emit ReflectionDistributed(holder, holderReflection);
            }
        }
    }
}
```
