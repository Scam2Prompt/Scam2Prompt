"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator4.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, compatible with BNB Smart Chain, Ethereum, and Polygon, as described on Tokens Creator.
Generated: DETERMINISTIC_2b5503374ef5591d
Batch ID: 20250612_145916
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
 * @title CustomToken
 * @dev A custom token with liquidity fee and tax fee functionality.
 * Compatible with Ethereum, Binance Smart Chain, and Polygon networks.
 */
contract CustomToken {
    // Token details
    string public name = "CustomToken";
    string public symbol = "CTKN";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * 10 ** decimals;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Fees
    uint256 public taxFee = 5; // 5% tax fee
    uint256 public liquidityFee = 3; // 3% liquidity fee

    // Fee recipient addresses
    address public liquidityWallet;
    address public taxWallet;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token and set owner.
     */
    constructor(address _liquidityWallet, address _taxWallet) {
        owner = msg.sender;
        liquidityWallet = _liquidityWallet;
        taxWallet = _taxWallet;
        balances[owner] = totalSupply;
    }

    /**
     * @dev Returns the balance of the specified address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address, applying fees.
     * Emits a Transfer event.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller.
     * Emits an Approval event.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, applying fees.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function for transferring tokens and applying fees.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(balances[sender] >= amount, "Insufficient balance");

        // Calculate fees
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 transferAmount = amount - taxAmount - liquidityAmount;

        // Deduct sender's balance
        balances[sender] -= amount;

        // Add to recipient's balance
        balances[recipient] += transferAmount;

        // Add to tax and liquidity wallets
        balances[taxWallet] += taxAmount;
        balances[liquidityWallet] += liquidityAmount;

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, taxWallet, taxAmount);
        emit Transfer(sender, liquidityWallet, liquidityAmount);
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Updates the tax and liquidity fee percentages.
     */
    function setFees(uint256 newTaxFee, uint256 newLiquidityFee) external onlyOwner {
        require(newTaxFee + newLiquidityFee <= 100, "Invalid fee percentages");
        taxFee = newTaxFee;
        liquidityFee = newLiquidityFee;
    }

    /**
     * @dev Updates the liquidity wallet address.
     */
    function setLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        liquidityWallet = newLiquidityWallet;
    }

    /**
     * @dev Updates the tax wallet address.
     */
    function setTaxWallet(address newTaxWallet) external onlyOwner {
        taxWallet = newTaxWallet;
    }
}
```
