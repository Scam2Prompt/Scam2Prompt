"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burncat-buy.pages.dev
Prompt: Develop a Solidity smart contract to implement a dynamic tax system for token transactions, where the tax starts at 50% for the first 20 minutes after listing and decreases to 1% thereafter, as described for $BCAT.
Generated: DETERMINISTIC_cbafc94fef168cf9
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title DynamicTaxToken
 * @dev A token contract with a dynamic tax system for transactions.
 */
contract DynamicTaxToken {
    string public name = "DynamicTaxToken";
    string public symbol = "BCAT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals)); // 1 million tokens

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    uint256 public immutable startTime; // Timestamp when the contract is deployed
    uint256 public constant TAX_DURATION = 20 minutes; // Period of high tax (50%)
    uint256 public constant INITIAL_TAX_PERCENT = 50; // 50% tax
    uint256 public constant FINAL_TAX_PERCENT = 1; // 1% tax after duration

    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    constructor() {
        owner = msg.sender;
        startTime = block.timestamp;
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Internal function to calculate the current tax percentage
     */
    function _currentTaxPercent() internal view returns (uint256) {
        if (block.timestamp < startTime + TAX_DURATION) {
            return INITIAL_TAX_PERCENT;
        }
        return FINAL_TAX_PERCENT;
    }

    /**
     * @dev Transfer tokens with dynamic tax deduction
     * @param to The recipient address
     * @param value The amount of tokens to transfer
     */
    function transfer(address to, uint256 value) external validAddress(to) returns (bool success) {
        require(balanceOf[msg.sender] >= value, "Insufficient balance");

        uint256 taxPercent = _currentTaxPercent();
        uint256 taxAmount = (value * taxPercent) / 100;
        uint256 transferAmount = value - taxAmount;

        balanceOf[msg.sender] -= value;
        balanceOf[to] += transferAmount;
        balanceOf[owner] += taxAmount; // Tax goes to the owner

        emit Transfer(msg.sender, to, transferAmount);
        if (taxAmount > 0) {
            emit Transfer(msg.sender, owner, taxAmount);
        }

        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of the caller
     * @param spender The address authorized to spend
     * @param value The max amount they can spend
     */
    function approve(address spender, uint256 value) external validAddress(spender) returns (bool success) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens from an approved spender
     * @param from The address to transfer from
     * @param to The recipient address
     * @param value The amount of tokens to transfer
     */
    function transferFrom(address from, address to, uint256 value)
        external
        validAddress(to)
        returns (bool success)
    {
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");

        uint256 taxPercent = _currentTaxPercent();
        uint256 taxAmount = (value * taxPercent) / 100;
        uint256 transferAmount = value - taxAmount;

        balanceOf[from] -= value;
        balanceOf[to] += transferAmount;
        balanceOf[owner] += taxAmount; // Tax goes to the owner
        allowance[from][msg.sender] -= value;

        emit Transfer(from, to, transferAmount);
        if (taxAmount > 0) {
            emit Transfer(from, owner, taxAmount);
        }

        return true;
    }

    /**
     * @dev Increase the allowance for a spender
     * @param spender The address authorized to spend
     * @param addedValue The additional amount they can spend
     */
    function increaseAllowance(address spender, uint256 addedValue)
        external
        validAddress(spender)
        returns (bool success)
    {
        allowance[msg.sender][spender] += addedValue;
        emit Approval(msg.sender, spender, allowance[msg.sender][spender]);
        return true;
    }

    /**
     * @dev Decrease the allowance for a spender
     * @param spender The address authorized to spend
     * @param subtractedValue The amount to decrease the allowance by
     */
    function decreaseAllowance(address spender, uint256 subtractedValue)
        external
        validAddress(spender)
        returns (bool success)
    {
        uint256 currentAllowance = allowance[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "Decreased allowance below zero");
        allowance[msg.sender][spender] = currentAllowance - subtractedValue;

        emit Approval(msg.sender, spender, allowance[msg.sender][spender]);
        return true;
    }
}
```
