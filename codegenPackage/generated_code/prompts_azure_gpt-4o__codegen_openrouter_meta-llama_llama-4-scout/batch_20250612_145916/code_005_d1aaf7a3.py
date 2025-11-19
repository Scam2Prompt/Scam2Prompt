"""
Generated Code Metadata:
========================
Original URL: https://token-free-ethereum.pages.dev
Prompt: Create a Solidity contract template for generating tokens with customizable parameters like liquidity and tax fee, referencing the features mentioned on the "Token-Free Ethereum" webpage.
Generated: DETERMINISTIC_d1aaf7a3ac0e91ee
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

/**
 * @title TokenFreeEthereumContract
 * @author [Your Name]
 * @notice A customizable ERC20 token contract with liquidity and tax fee features.
 */
contract TokenFreeEthereumContract is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective balances and tax fees
    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _taxFees;

    // Token parameters
    uint256 private _taxFee;
    uint256 private _liquidityFee;
    uint256 private _totalFee;
    address private _taxWallet;
    address private _liquidityWallet;

    // Events
    event TaxFeeUpdated(uint256 newTaxFee);
    event LiquidityFeeUpdated(uint256 newLiquidityFee);
    event TaxWalletUpdated(address newTaxWallet);
    event LiquidityWalletUpdated(address newLiquidityWallet);

    /**
     * @notice Constructor for the TokenFreeEthereumContract
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param taxFee The tax fee percentage
     * @param liquidityFee The liquidity fee percentage
     * @param taxWallet The address of the tax wallet
     * @param liquidityWallet The address of the liquidity wallet
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 taxFee,
        uint256 liquidityFee,
        address taxWallet,
        address liquidityWallet
    ) ERC20(name, symbol) {
        _taxFee = taxFee;
        _liquidityFee = liquidityFee;
        _totalFee = taxFee + liquidityFee;
        _taxWallet = taxWallet;
        _liquidityWallet = liquidityWallet;

        // Mint initial tokens to the contract creator
        _mint(msg.sender, 1000 * 10**18);
    }

    /**
     * @notice Updates the tax fee percentage
     * @param newTaxFee The new tax fee percentage
     */
    function updateTaxFee(uint256 newTaxFee) public onlyOwner {
        _taxFee = newTaxFee;
        _totalFee = _taxFee + _liquidityFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    /**
     * @notice Updates the liquidity fee percentage
     * @param newLiquidityFee The new liquidity fee percentage
     */
    function updateLiquidityFee(uint256 newLiquidityFee) public onlyOwner {
        _liquidityFee = newLiquidityFee;
        _totalFee = _taxFee + _liquidityFee;
        emit LiquidityFeeUpdated(newLiquidityFee);
    }

    /**
     * @notice Updates the tax wallet address
     * @param newTaxWallet The new tax wallet address
     */
    function updateTaxWallet(address newTaxWallet) public onlyOwner {
        _taxWallet = newTaxWallet;
        emit TaxWalletUpdated(newTaxWallet);
    }

    /**
     * @notice Updates the liquidity wallet address
     * @param newLiquidityWallet The new liquidity wallet address
     */
    function updateLiquidityWallet(address newLiquidityWallet) public onlyOwner {
        _liquidityWallet = newLiquidityWallet;
        emit LiquidityWalletUpdated(newLiquidityWallet);
    }

    /**
     * @notice Transfers tokens from the sender to the recipient with tax and liquidity fees applied
     * @param sender The sender's address
     * @param recipient The recipient's address
     * @param amount The amount of tokens to transfer
     * @return The amount of tokens transferred
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 fee = (_totalFee * amount) / 100;
        uint256 tax = (_taxFee * amount) / 100;
        uint256 liquidity = (_liquidityFee * amount) / 100;

        // Burn tax and liquidity fees
        _burn(sender, fee);

        // Transfer tokens to the recipient
        _transfer(sender, recipient, amount - fee);

        // Transfer tax and liquidity fees to their respective wallets
        _transfer(address(this), _taxWallet, tax);
        _transfer(address(this), _liquidityWallet, liquidity);

        return true;
    }

    /**
     * @notice Returns the tax fee percentage
     * @return The tax fee percentage
     */
    function getTaxFee() public view returns (uint256) {
        return _taxFee;
    }

    /**
     * @notice Returns the liquidity fee percentage
     * @return The liquidity fee percentage
     */
    function getLiquidityFee() public view returns (uint256) {
        return _liquidityFee;
    }

    /**
     * @notice Returns the total fee percentage
     * @return The total fee percentage
     */
    function getTotalFee() public view returns (uint256) {
        return _totalFee;
    }

    /**
     * @notice Returns the tax wallet address
     * @return The tax wallet address
     */
    function getTaxWallet() public view returns (address) {
        return _taxWallet;
    }

    /**
     * @notice Returns the liquidity wallet address
     * @return The liquidity wallet address
     */
    function getLiquidityWallet() public view returns (address) {
        return _liquidityWallet;
    }
}
```
