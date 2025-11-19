"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, similar to the functionality described on Tokens Creator, ensuring 100% token ownership.
Generated: DETERMINISTIC_0232b139356601b6
Batch ID: 20250612_145916
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

contract CustomToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token properties
    string private _tokenName;
    string private _tokenSymbol;
    uint256 private _tokenTotalSupply;

    // Tax fee properties
    uint256 public taxFee;
    address public taxWallet;

    // Liquidity properties
    uint256 public liquidityFee;
    address public liquidityWallet;
    bool public liquidityAdded;

    // Ownership properties
    address private _owner;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event TaxFeeUpdated(uint256 previousTaxFee, uint256 newTaxFee);
    event TaxWalletUpdated(address previousTaxWallet, address newTaxWallet);
    event LiquidityFeeUpdated(uint256 previousLiquidityFee, uint256 newLiquidityFee);
    event LiquidityWalletUpdated(address previousLiquidityWallet, address newLiquidityWallet);
    event LiquidityAdded();

    /**
     * @dev Constructor.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param totalSupply Token total supply.
     * @param _taxFee Tax fee.
     * @param _taxWallet Tax wallet.
     * @param _liquidityFee Liquidity fee.
     * @param _liquidityWallet Liquidity wallet.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 _taxFee,
        address _taxWallet,
        uint256 _liquidityFee,
        address _liquidityWallet
    ) ERC20(name, symbol) {
        _tokenName = name;
        _tokenSymbol = symbol;
        _tokenTotalSupply = totalSupply;
        _owner = msg.sender;

        // Mint total supply to owner
        _mint(msg.sender, totalSupply);

        // Set tax fee and wallet
        taxFee = _taxFee;
        taxWallet = _taxWallet;

        // Set liquidity fee and wallet
        liquidityFee = _liquidityFee;
        liquidityWallet = _liquidityWallet;

        liquidityAdded = false;
    }

    /**
     * @dev Returns the token owner.
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Transfers ownership.
     * @param newOwner New owner.
     */
    function transferOwnership(address newOwner) public {
        require(msg.sender == _owner, "Only the owner can transfer ownership");
        require(newOwner != address(0), "New owner cannot be zero");

        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }

    /**
     * @dev Updates tax fee.
     * @param newTaxFee New tax fee.
     */
    function updateTaxFee(uint256 newTaxFee) public {
        require(msg.sender == _owner, "Only the owner can update tax fee");

        emit TaxFeeUpdated(taxFee, newTaxFee);
        taxFee = newTaxFee;
    }

    /**
     * @dev Updates tax wallet.
     * @param newTaxWallet New tax wallet.
     */
    function updateTaxWallet(address newTaxWallet) public {
        require(msg.sender == _owner, "Only the owner can update tax wallet");
        require(newTaxWallet != address(0), "New tax wallet cannot be zero");

        emit TaxWalletUpdated(taxWallet, newTaxWallet);
        taxWallet = newTaxWallet;
    }

    /**
     * @dev Updates liquidity fee.
     * @param newLiquidityFee New liquidity fee.
     */
    function updateLiquidityFee(uint256 newLiquidityFee) public {
        require(msg.sender == _owner, "Only the owner can update liquidity fee");

        emit LiquidityFeeUpdated(liquidityFee, newLiquidityFee);
        liquidityFee = newLiquidityFee;
    }

    /**
     * @dev Updates liquidity wallet.
     * @param newLiquidityWallet New liquidity wallet.
     */
    function updateLiquidityWallet(address newLiquidityWallet) public {
        require(msg.sender == _owner, "Only the owner can update liquidity wallet");
        require(newLiquidityWallet != address(0), "New liquidity wallet cannot be zero");

        emit LiquidityWalletUpdated(liquidityWallet, newLiquidityWallet);
        liquidityWallet = newLiquidityWallet;
    }

    /**
     * @dev Adds liquidity.
     */
    function addLiquidity(uint256 amount) public nonReentrant {
        require(msg.sender == _owner, "Only the owner can add liquidity");
        require(!liquidityAdded, "Liquidity already added");

        // Transfer tokens to liquidity wallet
        _transfer(msg.sender, liquidityWallet, amount);

        liquidityAdded = true;

        emit LiquidityAdded();
    }

    /**
     * @dev Transfers tokens with tax fee.
     * @param recipient Recipient.
     * @param amount Amount.
     */
    function transferWithTax(address recipient, uint256 amount) public returns (bool) {
        uint256 taxAmount = amount.mul(taxFee).div(100);
        uint256 netAmount = amount.sub(taxAmount);

        // Transfer tax to tax wallet
        _transfer(msg.sender, taxWallet, taxAmount);

        // Transfer net amount to recipient
        _transfer(msg.sender, recipient, netAmount);

        return true;
    }

    /**
     * @dev Overrides transfer function to apply tax fee.
     * @param recipient Recipient.
     * @param amount Amount.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return transferWithTax(recipient, amount);
    }

    /**
     * @dev Overrides transferFrom function to apply tax fee.
     * @param sender Sender.
     * @param recipient Recipient.
     * @param amount Amount.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        return transferWithTax(recipient, amount);
    }
}
```
