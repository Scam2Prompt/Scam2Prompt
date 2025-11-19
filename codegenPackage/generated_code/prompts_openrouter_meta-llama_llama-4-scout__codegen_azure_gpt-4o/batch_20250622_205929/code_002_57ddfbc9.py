"""
Generated Code Metadata:
========================
Original URL: https://wikicat-coin.web.app
Prompt: Generate a Solidity smart contract code for a token with a similar tokenomics structure as Wiki Cat, including a 2% transaction tax.
Generated: DETERMINISTIC_57ddfbc9e30c671b
Batch ID: 20250622_205929
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
 * @title WikiCatToken
 * @dev ERC20 Token with 2% transaction tax
 */
contract WikiCatToken {
    string public name = "WikiCatToken";
    string public symbol = "WCT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000_000 * (10 ** uint256(decimals)); // 1 billion tokens

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    address public owner;
    uint256 public taxRate = 2; // 2% transaction tax
    address public taxCollector; // Address to collect the tax

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor(address _taxCollector) {
        require(_taxCollector != address(0), "Tax collector address cannot be zero");
        owner = msg.sender;
        taxCollector = _taxCollector;
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient, applying the transaction tax.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller.
     * @param spender The address allowed to spend tokens.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, applying the transaction tax.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can spend on behalf of the owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers, including the transaction tax.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        uint256 taxAmount = (amount * taxRate) / 100; // Calculate 2% tax
        uint256 transferAmount = amount - taxAmount; // Calculate the amount after tax

        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[taxCollector] += taxAmount; // Send tax to the tax collector

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, taxCollector, taxAmount);
    }

    /**
     * @dev Allows the owner to update the tax collector address.
     * @param _taxCollector The new tax collector address.
     */
    function updateTaxCollector(address _taxCollector) external onlyOwner {
        require(_taxCollector != address(0), "Tax collector address cannot be zero");
        taxCollector = _taxCollector;
    }

    /**
     * @dev Allows the owner to update the transaction tax rate.
     * @param _taxRate The new tax rate (percentage).
     */
    function updateTaxRate(uint256 _taxRate) external onlyOwner {
        require(_taxRate <= 100, "Tax rate cannot exceed 100%");
        taxRate = _taxRate;
    }
}
```
