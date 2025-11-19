"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claims.pages.dev
Prompt: Provide an example of a smart contract for the $KANG token that includes buy and sell tax functionalities as described in the Kangamoon documentation.
Generated: DETERMINISTIC_1589c8aa75bf2bf1
Batch ID: 20250612_163848
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
 * @title KangToken
 * @dev ERC20 token implementation with buy and sell tax functionalities.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KangToken is ERC20, Ownable {
    // Tax rates for buy and sell transactions (in percentage points, e.g., 5 = 5%)
    uint256 public buyTaxRate;
    uint256 public sellTaxRate;

    // Address where tax amounts are sent
    address public taxWallet;

    // Mapping for automated market maker (AMM) pairs
    mapping(address => bool) public isAMMPair;

    // Events
    event TaxRatesUpdated(uint256 buyTaxRate, uint256 sellTaxRate);
    event TaxWalletUpdated(address indexed newTaxWallet);
    event AMMPairUpdated(address indexed pair, bool isAMMPair);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _buyTaxRate,
        uint256 _sellTaxRate,
        address _taxWallet
    ) ERC20(name, symbol) {
        require(_buyTaxRate <= 100 && _sellTaxRate <= 100, "Tax rates must be between 0 and 100%");
        require(_taxWallet != address(0), "Tax wallet cannot be the zero address");

        // Assign initial values for buy and sell tax rates
        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;

        // Set the tax wallet
        taxWallet = _taxWallet;

        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10**decimals()));
    }

    /**
     * @dev Set a new tax wallet.
     * @param _taxWallet The new tax wallet address.
     */
    function setTaxWallet(address _taxWallet) external onlyOwner {
        require(_taxWallet != address(0), "Tax wallet cannot be the zero address");
        taxWallet = _taxWallet;
        emit TaxWalletUpdated(_taxWallet);
    }

    /**
     * @dev Update tax rates for buy and sell transactions.
     * @param _buyTaxRate New buy tax rate (percentage).
     * @param _sellTaxRate New sell tax rate (percentage).
     */
    function updateTaxRates(uint256 _buyTaxRate, uint256 _sellTaxRate) external onlyOwner {
        require(_buyTaxRate <= 100 && _sellTaxRate <= 100, "Tax rates must be between 0 and 100%");
        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        emit TaxRatesUpdated(buyTaxRate, sellTaxRate);
    }

    /**
     * @dev Set an AMM pair address.
     * @param pair Address of the AMM pair.
     * @param _isAMMPair True if the address is an AMM pair, false otherwise.
     */
    function setAMMPair(address pair, bool _isAMMPair) external onlyOwner {
        isAMMPair[pair] = _isAMMPair;
        emit AMMPairUpdated(pair, _isAMMPair);
    }

    /**
     * @dev Override the _transfer function to include buy and sell tax logic.
     * @param sender The address sending tokens.
     * @param recipient The address receiving tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        uint256 taxAmount = 0;

        // Apply buy tax if recipient is an AMM pair
        if (isAMMPair[recipient]) {
            taxAmount = (amount * buyTaxRate) / 100;
        }
        // Apply sell tax if sender is an AMM pair
        else if (isAMMPair[sender]) {
            taxAmount = (amount * sellTaxRate) / 100;
        }

        // If there is a tax, transfer the tax amount to the tax wallet
        if (taxAmount > 0) {
            super._transfer(sender, taxWallet, taxAmount);
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, amount - taxAmount);
    }
}
```
