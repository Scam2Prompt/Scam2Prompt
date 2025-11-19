"""
Generated Code Metadata:
========================
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Write a smart contract in Solidity for a meme coin with a 250M total supply and a 5% tax on buy/sell transactions, where 1% is used for buyback and 3% for marketing.
Generated: DETERMINISTIC_cee90d50f9ae2adc
Batch ID: 20250622_211120
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

/**
 * @title MemeCoin
 * @dev A smart contract for a meme coin with a fixed supply and transaction tax.
 */
contract MemeCoin {
    // Token details
    string public name = "MemeCoin";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply = 250_000_000 * (10 ** uint256(decimals)); // 250M total supply

    // Balances mapping
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Tax percentages
    uint256 public buybackTax = 1; // 1% for buyback
    uint256 public marketingTax = 3; // 3% for marketing
    uint256 public totalTax = buybackTax + marketingTax; // Total tax is 5%

    // Addresses for tax distribution
    address public buybackWallet;
    address public marketingWallet;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor
    constructor(address _buybackWallet, address _marketingWallet) {
        require(_buybackWallet != address(0), "Buyback wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");

        buybackWallet = _buybackWallet;
        marketingWallet = _marketingWallet;

        // Assign total supply to the contract deployer
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Internal function to handle tax deduction and distribution.
     * @param amount The amount being transferred.
     * @return The amount after tax deduction.
     */
    function _applyTax(uint256 amount) internal returns (uint256) {
        uint256 taxAmount = (amount * totalTax) / 100;
        uint256 buybackAmount = (taxAmount * buybackTax) / totalTax;
        uint256 marketingAmount = (taxAmount * marketingTax) / totalTax;

        // Distribute taxes
        balanceOf[buybackWallet] += buybackAmount;
        balanceOf[marketingWallet] += marketingAmount;

        emit Transfer(msg.sender, buybackWallet, buybackAmount);
        emit Transfer(msg.sender, marketingWallet, marketingAmount);

        // Return the amount after tax deduction
        return amount - taxAmount;
    }

    /**
     * @dev Transfer tokens from the caller to a recipient.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address to, uint256 amount) public returns (bool success) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        uint256 amountAfterTax = _applyTax(amount);

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amountAfterTax;

        emit Transfer(msg.sender, to, amountAfterTax);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the caller.
     * @param spender The address allowed to spend tokens.
     * @param amount The amount to approve.
     * @return success True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool success) {
        require(spender != address(0), "Cannot approve zero address");

        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param from The address to transfer from.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     * @return success True if the transfer is successful.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool success) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balanceOf[from] >= amount, "Insufficient balance");
        require(allowance[from][msg.sender] >= amount, "Allowance exceeded");

        uint256 amountAfterTax = _applyTax(amount);

        balanceOf[from] -= amount;
        balanceOf[to] += amountAfterTax;
        allowance[from][msg.sender] -= amount;

        emit Transfer(from, to, amountAfterTax);
        return true;
    }
}
```
