"""
Generated Code Metadata:
========================
Original URL: https://trumpmaga-buy.pages.dev
Prompt: Create a Solidity smart contract that implements a 1% tax on token transactions (buys, sells, transfers) for marketing, development, donations, and liquidity, similar to the MAGA Memecoin tokenomics.
Generated: DETERMINISTIC_b6303c4fcafd128a
Batch ID: 20250612_150552
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
 * @title MAGAMemecoin
 * @author [Your Name]
 * @notice A token with 1% tax on transactions for marketing, development, donations, and liquidity.
 */
contract MAGAMemecoin is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tax distribution
    uint256 public marketingTax;
    uint256 public developmentTax;
    uint256 public donationsTax;
    uint256 public liquidityTax;

    // Tax recipients
    address public marketingWallet;
    address public developmentWallet;
    address public donationsWallet;
    address public liquidityWallet;

    // Tax rate (1% = 100)
    uint256 public taxRate;

    // Mapping of transaction exemptions
    mapping(address => bool) public exemptFromTax;

    /**
     * @notice Event emitted when tax recipients are updated.
     */
    event TaxRecipientsUpdated(
        address indexed marketingWallet,
        address indexed developmentWallet,
        address indexed donationsWallet,
        address liquidityWallet
    );

    /**
     * @notice Event emitted when tax distribution is updated.
     */
    event TaxDistributionUpdated(
        uint256 marketingTax,
        uint256 developmentTax,
        uint256 donationsTax,
        uint256 liquidityTax
    );

    /**
     * @notice Constructor.
     * @param _name Token name.
     * @param _symbol Token symbol.
     * @param _initialSupply Initial token supply.
     * @param _marketingWallet Marketing wallet address.
     * @param _developmentWallet Development wallet address.
     * @param _donationsWallet Donations wallet address.
     * @param _liquidityWallet Liquidity wallet address.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        address _marketingWallet,
        address _developmentWallet,
        address _donationsWallet,
        address _liquidityWallet
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);

        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;
        donationsWallet = _donationsWallet;
        liquidityWallet = _liquidityWallet;

        marketingTax = 25; // 25% of tax
        developmentTax = 25; // 25% of tax
        donationsTax = 25; // 25% of tax
        liquidityTax = 25; // 25% of tax

        taxRate = 100; // 1%

        exemptFromTax[msg.sender] = true;
    }

    /**
     * @notice Update tax recipients.
     * @param _marketingWallet Marketing wallet address.
     * @param _developmentWallet Development wallet address.
     * @param _donationsWallet Donations wallet address.
     * @param _liquidityWallet Liquidity wallet address.
     */
    function updateTaxRecipients(
        address _marketingWallet,
        address _developmentWallet,
        address _donationsWallet,
        address _liquidityWallet
    ) public onlyOwner {
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;
        donationsWallet = _donationsWallet;
        liquidityWallet = _liquidityWallet;

        emit TaxRecipientsUpdated(
            marketingWallet,
            developmentWallet,
            donationsWallet,
            liquidityWallet
        );
    }

    /**
     * @notice Update tax distribution.
     * @param _marketingTax Marketing tax percentage.
     * @param _developmentTax Development tax percentage.
     * @param _donationsTax Donations tax percentage.
     * @param _liquidityTax Liquidity tax percentage.
     */
    function updateTaxDistribution(
        uint256 _marketingTax,
        uint256 _developmentTax,
        uint256 _donationsTax,
        uint256 _liquidityTax
    ) public onlyOwner {
        marketingTax = _marketingTax;
        developmentTax = _developmentTax;
        donationsTax = _donationsTax;
        liquidityTax = _liquidityTax;

        emit TaxDistributionUpdated(
            marketingTax,
            developmentTax,
            donationsTax,
            liquidityTax
        );
    }

    /**
     * @notice Exempt an address from tax.
     * @param _address Address to exempt.
     * @param _exempt Exempt status.
     */
    function setExemptFromTax(address _address, bool _exempt) public onlyOwner {
        exemptFromTax[_address] = _exempt;
    }

    /**
     * @notice Transfer tokens with tax.
     * @param _to Recipient address.
     * @param _amount Amount to transfer.
     * @return bool Success status.
     */
    function transfer(address _to, uint256 _amount) public override nonReentrant returns (bool) {
        uint256 tax = calculateTax(_amount);
        uint256 netAmount = _amount - tax;

        _transfer(msg.sender, _to, netAmount);

        distributeTax(tax);

        return true;
    }

    /**
     * @notice Transfer tokens from with tax.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _amount Amount to transfer.
     * @return bool Success status.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = calculateTax(_amount);
        uint256 netAmount = _amount - tax;

        _transfer(_from, _to, netAmount);

        distributeTax(tax);

        return true;
    }

    /**
     * @notice Calculate tax amount.
     * @param _amount Amount to calculate tax for.
     * @return uint256 Tax amount.
     */
    function calculateTax(uint256 _amount) internal view returns (uint256) {
        if (exemptFromTax[msg.sender] || exemptFromTax[address(this)]) {
            return 0;
        }

        return (_amount * taxRate) / 10000;
    }

    /**
     * @notice Distribute tax to recipients.
     * @param _tax Tax amount to distribute.
     */
    function distributeTax(uint256 _tax) internal {
        uint256 marketingAmount = (_tax * marketingTax) / 100;
        uint256 developmentAmount = (_tax * developmentTax) / 100;
        uint256 donationsAmount = (_tax * donationsTax) / 100;
        uint256 liquidityAmount = (_tax * liquidityTax) / 100;

        _transfer(msg.sender, marketingWallet, marketingAmount);
        _transfer(msg.sender, developmentWallet, developmentAmount);
        _transfer(msg.sender, donationsWallet, donationsAmount);
        _transfer(msg.sender, liquidityWallet, liquidityAmount);
    }
}
```
