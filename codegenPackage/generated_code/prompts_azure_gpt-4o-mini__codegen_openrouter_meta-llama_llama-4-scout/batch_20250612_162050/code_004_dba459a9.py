"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-ai.pages.dev
Prompt: Create a sample smart contract for managing $QUBE token transactions, including buy and sell tax implementations as described on InQubeta.
Generated: DETERMINISTIC_dba459a90bcc7db7
Batch ID: 20250612_162050
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title QUBE Token Contract
 * @author InQubeta Team
 * @notice This contract manages QUBE token transactions, including buy and sell tax implementations.
 */
contract QUBE is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax rates for buy and sell transactions
    uint256 public buyTaxRate;
    uint256 public sellTaxRate;

    // Addresses for tax redistribution
    address public treasuryAddress;
    address public marketingAddress;

    // Flag to check if the contract is initialized
    bool public initialized;

    /**
     * @dev Constructor for QUBE token contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     */
    constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {}

    /**
     * @dev Initializes the contract with tax rates and treasury/marketing addresses
     * @param _buyTaxRate Buy tax rate (in percent)
     * @param _sellTaxRate Sell tax rate (in percent)
     * @param _treasuryAddress Treasury address for tax redistribution
     * @param _marketingAddress Marketing address for tax redistribution
     */
    function initialize(
        uint256 _buyTaxRate,
        uint256 _sellTaxRate,
        address _treasuryAddress,
        address _marketingAddress
    ) public {
        require(!initialized, "Contract already initialized");
        require(_buyTaxRate <= 100, "Buy tax rate exceeds 100%");
        require(_sellTaxRate <= 100, "Sell tax rate exceeds 100%");
        require(_treasuryAddress != address(0), "Treasury address is zero");
        require(_marketingAddress != address(0), "Marketing address is zero");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        treasuryAddress = _treasuryAddress;
        marketingAddress = _marketingAddress;
        initialized = true;
    }

    /**
     * @dev Burns tokens from the specified address
     * @param _amount Amount of tokens to burn
     */
    function burn(uint256 _amount) public override {
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");
        _burn(msg.sender, _amount);
    }

    /**
     * @dev Buys QUBE tokens with tax implementation
     * @param _amount Amount of tokens to buy
     */
    function buy(uint256 _amount) public nonReentrant {
        require(initialized, "Contract not initialized");
        require(msg.sender != address(0), "Buyer address is zero");

        // Calculate tax amount
        uint256 taxAmount = _amount.mul(buyTaxRate).div(100);

        // Calculate net tokens to transfer
        uint256 netAmount = _amount.sub(taxAmount);

        // Transfer tokens to buyer
        _mint(msg.sender, netAmount);

        // Redistribute tax
        _mint(treasuryAddress, taxAmount.mul(2).div(3));
        _mint(marketingAddress, taxAmount.mul(1).div(3));
    }

    /**
     * @dev Sells QUBE tokens with tax implementation
     * @param _amount Amount of tokens to sell
     */
    function sell(uint256 _amount) public nonReentrant {
        require(initialized, "Contract not initialized");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Calculate tax amount
        uint256 taxAmount = _amount.mul(sellTaxRate).div(100);

        // Calculate net tokens to transfer
        uint256 netAmount = _amount.sub(taxAmount);

        // Burn tokens from seller
        _burn(msg.sender, _amount);

        // Redistribute tax
        _mint(treasuryAddress, taxAmount.mul(2).div(3));
        _mint(marketingAddress, taxAmount.mul(1).div(3));

        // Transfer net tokens to seller
        payable(msg.sender).transfer(netAmount);
    }
}
```
