"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-ai.web.app
Prompt: Generate a smart contract code in Solidity for the $QUBE token, implementing the tokenomics described on the InQubeta website, including a 5% buy tax and 10% sell tax.
Generated: DETERMINISTIC_5b3f2b2f499cf9a3
Batch ID: 20250622_204914
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
 * @title QUBE Token Smart Contract
 * @dev Implements ERC20 token with custom tokenomics: 5% buy tax and 10% sell tax.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QUBE is ERC20, Ownable {
    // Tax rates
    uint256 public buyTaxRate = 5; // 5% buy tax
    uint256 public sellTaxRate = 10; // 10% sell tax

    // Address to collect taxes
    address public taxCollector;

    // Mapping to track automated market maker (AMM) addresses
    mapping(address => bool) public isAMM;

    /**
     * @dev Constructor to initialize the token.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial supply of the token.
     * @param _taxCollector Address to collect taxes.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        address _taxCollector
    ) ERC20(_name, _symbol) {
        require(_taxCollector != address(0), "Tax collector address cannot be zero");
        taxCollector = _taxCollector;
        _mint(msg.sender, _initialSupply * (10**decimals()));
    }

    /**
     * @dev Override the transfer function to implement tax logic.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = calculateTax(msg.sender, recipient, amount);
        uint256 transferAmount = amount - taxAmount;

        if (taxAmount > 0) {
            super.transfer(taxCollector, taxAmount); // Send tax to the tax collector
        }
        return super.transfer(recipient, transferAmount); // Transfer remaining tokens
    }

    /**
     * @dev Override the transferFrom function to implement tax logic.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 taxAmount = calculateTax(sender, recipient, amount);
        uint256 transferAmount = amount - taxAmount;

        if (taxAmount > 0) {
            super.transferFrom(sender, taxCollector, taxAmount); // Send tax to the tax collector
        }
        return super.transferFrom(sender, recipient, transferAmount); // Transfer remaining tokens
    }

    /**
     * @dev Calculate the tax amount based on the sender and recipient.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens being transferred.
     * @return Tax amount to be deducted.
     */
    function calculateTax(
        address sender,
        address recipient,
        uint256 amount
    ) internal view returns (uint256) {
        if (isAMM[sender]) {
            // Buy transaction (sender is AMM)
            return (amount * buyTaxRate) / 100;
        } else if (isAMM[recipient]) {
            // Sell transaction (recipient is AMM)
            return (amount * sellTaxRate) / 100;
        }
        return 0; // No tax for regular transfers
    }

    /**
     * @dev Set the tax collector address.
     * @param _taxCollector Address to collect taxes.
     */
    function setTaxCollector(address _taxCollector) external onlyOwner {
        require(_taxCollector != address(0), "Tax collector address cannot be zero");
        taxCollector = _taxCollector;
    }

    /**
     * @dev Set the buy tax rate.
     * @param _buyTaxRate New buy tax rate (percentage).
     */
    function setBuyTaxRate(uint256 _buyTaxRate) external onlyOwner {
        require(_buyTaxRate <= 100, "Buy tax rate must be <= 100%");
        buyTaxRate = _buyTaxRate;
    }

    /**
     * @dev Set the sell tax rate.
     * @param _sellTaxRate New sell tax rate (percentage).
     */
    function setSellTaxRate(uint256 _sellTaxRate) external onlyOwner {
        require(_sellTaxRate <= 100, "Sell tax rate must be <= 100%");
        sellTaxRate = _sellTaxRate;
    }

    /**
     * @dev Add or remove an AMM address.
     * @param amm Address of the AMM.
     * @param status True to add, false to remove.
     */
    function setAMM(address amm, bool status) external onlyOwner {
        require(amm != address(0), "AMM address cannot be zero");
        isAMM[amm] = status;
    }
}
```
