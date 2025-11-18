"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcprinter.xyz
Prompt: Using the $UPRINT tokenomics, create a Solidity smart contract that implements a similar buy/sell tax mechanism (5% each) and distributes USDC reflections to token holders.
Generated: DETERMINISTIC_cb2867ca2fa87e69
Batch ID: 20250612_150426
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract UPrintToken is ERC20Burnable, Ownable {
    // Constants
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // Total supply of 1 million tokens with 18 decimals
    uint256 public buyTax = 5; // Buy tax percentage
    uint256 public sellTax = 5; // Sell tax percentage
    IERC20 public USDC; // USDC token contract
    mapping(address => bool) public excludedFromTax; // Excluded addresses from tax

    // Events
    event TaxUpdated(uint256 newBuyTax, uint256 newSellTax);
    event ExcludedFromTax(address indexed account, bool isExcluded);

    // Constructor
    constructor(address _usdc) ERC20("UPrint Token", "UPRINT") {
        USDC = IERC20(_usdc);
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to buy tokens
    function buyTokens(uint256 amount) external payable {
        require(msg.value > 0, "Ether value must be greater than 0");
        uint256 taxAmount = (amount * buyTax) / 100;
        uint256 netAmount = amount - taxAmount;

        // Transfer tax to contract
        _transfer(msg.sender, address(this), taxAmount);
        // Transfer net amount to the buyer
        _transfer(address(this), msg.sender, netAmount);

        // Distribute USDC reflections to the sender
        distributeUSDC(msg.sender);
    }

    // Function to sell tokens
    function sellTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        uint256 taxAmount = (amount * sellTax) / 100;
        uint256 netAmount = amount - taxAmount;

        // Transfer tax to contract
        _transfer(msg.sender, address(this), taxAmount);
        // Transfer net amount to the seller
        _transfer(msg.sender, address(this), netAmount);

        // Distribute USDC reflections to the seller
        distributeUSDC(msg.sender);
    }

    // Function to distribute USDC reflections
    function distributeUSDC(address account) internal {
        uint256 usdcBalance = USDC.balanceOf(address(this));
        require(usdcBalance > 0, "No USDC available for distribution");

        uint256 reflectionAmount = (usdcBalance * balanceOf(account)) / TOTAL_SUPPLY;
        if(reflectionAmount > 0) {
            USDC.transfer(account, reflectionAmount);
        }
    }

    // Function to update tax percentages
    function updateTax(uint256 newBuyTax, uint256 newSellTax) external onlyOwner {
        require(newBuyTax <= 100 && newSellTax <= 100, "Tax must be <= 100%");
        buyTax = newBuyTax;
        sellTax = newSellTax;
        emit TaxUpdated(newBuyTax, newSellTax);
    }

    // Function to exclude an address from tax
    function excludeFromTax(address account, bool isExcluded) external onlyOwner {
        excludedFromTax[account] = isExcluded;
        emit ExcludedFromTax(account, isExcluded);
    }

    // Override transfer functions to implement tax logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        if (!excludedFromTax[sender] && !excludedFromTax[recipient]) {
            uint256 taxAmount = (amount * (sender == address(this) ? sellTax : buyTax)) / 100;
            uint256 netAmount = amount - taxAmount;

            super._transfer(sender, address(this), taxAmount); // Tax goes to the contract
            super._transfer(sender, recipient, netAmount); // Transfer net amount to recipient
        } else {
            super._transfer(sender, recipient, amount); // Regular transfer
        }
    }
}
```
