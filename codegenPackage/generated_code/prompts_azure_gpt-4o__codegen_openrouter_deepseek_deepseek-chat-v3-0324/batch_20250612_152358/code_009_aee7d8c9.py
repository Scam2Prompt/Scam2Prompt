"""
Generated Code Metadata:
========================
Original URL: https://marvinonbase.pages.dev
Prompt: Design a tokenomics model for a meme coin that includes taxes for burns, marketing, and development, as well as reserved tokens for future exchange listings.
Generated: DETERMINISTIC_aee7d8c9f6fb078c
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MemeCoin is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rates in basis points (1% = 100 bps)
    uint256 public constant BURN_TAX = 200;    // 2%
    uint256 public constant MARKETING_TAX = 300; // 3%
    uint256 public constant DEV_TAX = 200;      // 2%
    uint256 public constant TOTAL_TAX = BURN_TAX + MARKETING_TAX + DEV_TAX;

    // Addresses for tax distribution
    address public marketingWallet;
    address public devWallet;
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    // Reserved tokens for exchange listings
    uint256 public reservedForListings;
    address public listingReserveWallet;

    // Exclusions from tax
    mapping(address => bool) private _isExcludedFromTax;

    event TaxesDistributed(
        uint256 amountBurned,
        uint256 amountMarketing,
        uint256 amountDev
    );

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _marketingWallet,
        address _devWallet,
        address _listingReserveWallet,
        uint256 _reservedForListings
    ) ERC20(name, symbol) {
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero");
        require(_devWallet != address(0), "Dev wallet cannot be zero");
        require(_listingReserveWallet != address(0), "Listing reserve wallet cannot be zero");
        require(_reservedForListings <= initialSupply, "Reserved amount exceeds supply");

        marketingWallet = _marketingWallet;
        devWallet = _devWallet;
        listingReserveWallet = _listingReserveWallet;
        reservedForListings = _reservedForListings;

        // Exclude tax wallets and owner from tax
        _isExcludedFromTax[marketingWallet] = true;
        _isExcludedFromTax[devWallet] = true;
        _isExcludedFromTax[listingReserveWallet] = true;
        _isExcludedFromTax[owner()] = true;

        // Mint initial supply minus reserved tokens
        _mint(owner(), initialSupply.sub(_reservedForListings));
        // Mint reserved tokens to listing reserve wallet
        _mint(listingReserveWallet, _reservedForListings);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient] || TOTAL_TAX == 0) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TOTAL_TAX).div(10000);
            uint256 sendAmount = amount.sub(taxAmount);

            // Distribute taxes
            uint256 burnAmount = taxAmount.mul(BURN_TAX).div(TOTAL_TAX);
            uint256 marketingAmount = taxAmount.mul(MARKETING_TAX).div(TOTAL_TAX);
            uint256 devAmount = taxAmount.sub(burnAmount).sub(marketingAmount);

            super._transfer(sender, BURN_ADDRESS, burnAmount);
            super._transfer(sender, marketingWallet, marketingAmount);
            super._transfer(sender, devWallet, devAmount);
            super._transfer(sender, recipient, sendAmount);

            emit TaxesDistributed(burnAmount, marketingAmount, devAmount);
        }
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        require(account != address(0), "Cannot exclude zero address");
        _isExcludedFromTax[account] = excluded;
    }

    function updateMarketingWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Marketing wallet cannot be zero");
        marketingWallet = newWallet;
    }

    function updateDevWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Dev wallet cannot be zero");
        devWallet = newWallet;
    }

    function updateListingReserveWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Listing reserve wallet cannot be zero");
        listingReserveWallet = newWallet;
    }

    function releaseListingTokens(address exchangeWallet, uint256 amount) external onlyOwner {
        require(exchangeWallet != address(0), "Exchange wallet cannot be zero");
        require(amount <= balanceOf(listingReserveWallet), "Insufficient reserve balance");
        _transfer(listingReserveWallet, exchangeWallet, amount);
    }

    function isExcludedFromTax(address account) public view returns (bool) {
        return _isExcludedFromTax[account];
    }
}
```
