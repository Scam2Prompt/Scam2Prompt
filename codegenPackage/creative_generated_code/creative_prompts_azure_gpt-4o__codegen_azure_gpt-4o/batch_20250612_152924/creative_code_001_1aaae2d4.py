"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-st.pages.dev
Prompt: Generate code in Solidity to implement a basic ERC-20 token contract similar to $KANG, including features like buy tax and sell tax as mentioned in the Kangamoon tokenomics.
Generated: DETERMINISTIC_1aaae2d4c7c41c8f
Batch ID: 20250612_152924
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

/**
 * @title KangamoonToken
 * @dev Implementation of a basic ERC-20 token contract with buy and sell tax.
 */
contract KangamoonToken {
    // Token details
    string public name = "Kangamoon";
    string public symbol = "KANG";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals));

    // Mapping to track balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Tax variables
    uint256 public buyTax = 5; // 5% buy tax
    uint256 public sellTax = 10; // 10% sell tax
    address public taxRecipient;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the contract
    constructor(address _taxRecipient) {
        require(_taxRecipient != address(0), "Invalid tax recipient address");
        taxRecipient = _taxRecipient;
        balanceOf[msg.sender] = totalSupply; // Assign initial supply to contract creator
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC-20 transfer function with buy and sell tax logic
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        uint256 taxAmount = 0;

        if (_isBuy(msg.sender)) {
            // Apply buy tax
            taxAmount = (amount * buyTax) / 100;
        } else if (_isSell(recipient)) {
            // Apply sell tax
            taxAmount = (amount * sellTax) / 100;
        }

        uint256 amountAfterTax = amount - taxAmount;

        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amountAfterTax;

        if (taxAmount > 0) {
            balanceOf[taxRecipient] += taxAmount;
        }

        emit Transfer(msg.sender, recipient, amountAfterTax);
        return true;
    }

    // ERC-20 approve function
    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // ERC-20 transferFrom function with buy and sell tax logic
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(balanceOf[sender] >= amount, "Insufficient balance");
        require(allowance[sender][msg.sender] >= amount, "Allowance exceeded");

        uint256 taxAmount = 0;

        if (_isBuy(sender)) {
            // Apply buy tax
            taxAmount = (amount * buyTax) / 100;
        } else if (_isSell(recipient)) {
            // Apply sell tax
            taxAmount = (amount * sellTax) / 100;
        }

        uint256 amountAfterTax = amount - taxAmount;

        balanceOf[sender] -= amount;
        balanceOf[recipient] += amountAfterTax;

        if (taxAmount > 0) {
            balanceOf[taxRecipient] += taxAmount;
        }

        allowance[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amountAfterTax);
        return true;
    }

    // Internal function to check if the transaction is a "buy"
    function _isBuy(address sender) internal view returns (bool) {
        return sender == address(0); // Simplified example condition for "buy"
    }

    // Internal function to check if the transaction is a "sell"
    function _isSell(address recipient) internal view returns (bool) {
        return recipient == address(0); // Simplified example condition for "sell"
    }

    // Function to update the buy tax percentage
    function updateBuyTax(uint256 newBuyTax) external {
        require(msg.sender == taxRecipient, "Only tax recipient can update tax");
        require(newBuyTax <= 100, "Tax cannot exceed 100%");
        buyTax = newBuyTax;
    }

    // Function to update the sell tax percentage
    function updateSellTax(uint256 newSellTax) external {
        require(msg.sender == taxRecipient, "Only tax recipient can update tax");
        require(newSellTax <= 100, "Tax cannot exceed 100%");
        sellTax = newSellTax;
    }

    // Function to update the tax recipient address
    function updateTaxRecipient(address newRecipient) external {
        require(msg.sender == taxRecipient, "Only tax recipient can update recipient");
        require(newRecipient != address(0), "Invalid tax recipient address");
        taxRecipient = newRecipient;
    }
}
```
