"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.pages.dev
Prompt: Create a sample smart contract for managing $QUBE token transactions, including buy and sell tax implementations as described on InQubeta.
Generated: DETERMINISTIC_dba459a90bcc7db7
Batch ID: 20250612_162050
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
 * @title QubeToken
 * @dev ERC20-compliant smart contract for managing $QUBE token transactions
 *      including buy and sell tax implementations.
 */
contract QubeToken {
    string public name = "Qube Token";
    string public symbol = "QUBE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    address public owner;

    uint256 public buyTaxPercentage = 2; // Buy tax (e.g., 2%)
    uint256 public sellTaxPercentage = 3; // Sell tax (e.g., 3%)
    address public taxReceiver; // Address to receive collected tax

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event BuyTaxUpdated(uint256 percentage);
    event SellTaxUpdated(uint256 percentage);
    event TaxReceiverUpdated(address indexed receiver);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with initial supply and tax receiver.
     * @param _initialSupply Initial token supply.
     * @param _taxReceiver Address to receive collected tax.
     */
    constructor(uint256 _initialSupply, address _taxReceiver) {
        require(_taxReceiver != address(0), "Invalid tax receiver address");

        owner = msg.sender;
        taxReceiver = _taxReceiver;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    // ERC20-compliant functions
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        _transfer(sender, recipient, amount);
        allowances[sender][msg.sender] -= amount;
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Internal transfer logic with buy/sell tax handling
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(balances[sender] >= amount, "Insufficient balance");

        uint256 tax = 0;

        // Apply buy tax if the recipient is not the owner (assumed to be a purchase)
        if (recipient != owner) {
            tax = (amount * buyTaxPercentage) / 100;
        }

        // Apply sell tax if the sender is not the owner (assumed to be a sale)
        if (sender != owner) {
            tax = (amount * sellTaxPercentage) / 100;
        }

        uint256 amountAfterTax = amount - tax;

        balances[sender] -= amount;
        balances[recipient] += amountAfterTax;

        // Distribute tax to the tax receiver
        if (tax > 0) {
            balances[taxReceiver] += tax;
            emit Transfer(sender, taxReceiver, tax);
        }

        emit Transfer(sender, recipient, amountAfterTax);
    }

    // Owner-only functions to manage tax rates and tax receiver
    function updateBuyTaxPercentage(uint256 percentage) external onlyOwner {
        require(percentage <= 10, "Buy tax too high"); // Example: Cap buy tax at 10%
        buyTaxPercentage = percentage;
        emit BuyTaxUpdated(percentage);
    }

    function updateSellTaxPercentage(uint256 percentage) external onlyOwner {
        require(percentage <= 10, "Sell tax too high"); // Example: Cap sell tax at 10%
        sellTaxPercentage = percentage;
        emit SellTaxUpdated(percentage);
    }

    function updateTaxReceiver(address receiver) external onlyOwner {
        require(receiver != address(0), "Invalid tax receiver address");
        taxReceiver = receiver;
        emit TaxReceiverUpdated(receiver);
    }
}
```
