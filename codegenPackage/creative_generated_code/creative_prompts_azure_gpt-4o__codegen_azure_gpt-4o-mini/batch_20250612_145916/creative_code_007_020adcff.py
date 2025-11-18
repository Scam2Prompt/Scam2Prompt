"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator4.pages.dev
Prompt: Generate a Solidity contract for token creation with tax fee functionality, ensuring compatibility with Tokens Creator's supported networks.
Generated: DETERMINISTIC_020adcff33802d52
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

// Import OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title TaxedToken
/// @dev This contract allows the creation of an ERC20 token with a tax fee on transfers.
contract TaxedToken is ERC20, Ownable {
    // Tax rate in basis points (1 basis point = 0.01%)
    uint256 public taxRate;
    // Address to receive tax fees
    address public taxCollector;

    // Events
    event TaxRateChanged(uint256 oldRate, uint256 newRate);
    event TaxCollectorChanged(address oldCollector, address newCollector);

    /// @dev Constructor to initialize the token with a name, symbol, tax rate, and tax collector address
    /// @param name The name of the token
    /// @param symbol The symbol of the token
    /// @param initialSupply The initial supply of the token
    /// @param _taxRate The initial tax rate in basis points
    /// @param _taxCollector The address that will receive the tax fees
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _taxRate, address _taxCollector) 
        ERC20(name, symbol) 
    {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        require(_taxRate <= 10000, "Tax rate must be less than or equal to 100%");
        require(_taxCollector != address(0), "Tax collector cannot be the zero address");

        taxRate = _taxRate;
        taxCollector = _taxCollector;

        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /// @dev Change the tax rate
    /// @param newRate The new tax rate in basis points
    function setTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 10000, "Tax rate must be less than or equal to 100%");
        emit TaxRateChanged(taxRate, newRate);
        taxRate = newRate;
    }

    /// @dev Change the tax collector address
    /// @param newCollector The new address to receive tax fees
    function setTaxCollector(address newCollector) external onlyOwner {
        require(newCollector != address(0), "Tax collector cannot be the zero address");
        emit TaxCollectorChanged(taxCollector, newCollector);
        taxCollector = newCollector;
    }

    /// @dev Override the transfer function to include tax functionality
    /// @param recipient The address to receive the tokens
    /// @param amount The amount of tokens to be transferred
    /// @return bool indicating success of transfer
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate tax amount
        uint256 taxAmount = (amount * taxRate) / 10000;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer taxed amount to recipient and tax to collector
        super.transfer(taxCollector, taxAmount);
        super.transfer(recipient, amountAfterTax);
        return true;
    }

    /// @dev Override the transferFrom function to include tax functionality
    /// @param sender The address of the sender
    /// @param recipient The address to receive the tokens
    /// @param amount The amount of tokens to be transferred
    /// @return bool indicating success of transfer
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate tax amount
        uint256 taxAmount = (amount * taxRate) / 10000;
        uint256 amountAfterTax = amount - taxAmount;

        // Update allowance
        _spendAllowance(sender, msg.sender, amount);

        // Transfer taxed amount to recipient and tax to collector
        super.transferFrom(sender, taxCollector, taxAmount);
        super.transferFrom(sender, recipient, amountAfterTax);
        return true;
    }
}
```
