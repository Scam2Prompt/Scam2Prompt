"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-creator.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee, similar to the functionality described on a platform that charges $1 for token creation and ensures 100% token ownership.
Generated: DETERMINISTIC_aa872a33b4b18d4a
Batch ID: 20250612_154321
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TaxableToken is ERC20, Ownable {
    // Fee percentage for transactions (scaled by 100)
    uint256 public taxFee;
    
    // Address to receive tax fees
    address public taxRecipient;

    // Mapping to track the balance of the tokens created
    mapping(address => bool) public tokenOwners;

    // Event to log token creation
    event TokenCreated(address indexed owner, string name, string symbol, uint256 totalSupply);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _taxFee, address _taxRecipient) 
        ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(_taxFee <= 100, "Tax fee must not exceed 100%");
        require(_taxRecipient != address(0), "Tax recipient cannot be the zero address");

        taxFee = _taxFee;
        taxRecipient = _taxRecipient;

        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * 10 ** decimals());
        tokenOwners[msg.sender] = true;

        emit TokenCreated(msg.sender, name, symbol, initialSupply);
    }

    // Override transfer function to include tax fee
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 feeAmount = (amount * taxFee) / 100;
        uint256 amountAfterFee = amount - feeAmount;

        // Transfer the fee to the tax recipient
        super._transfer(sender, taxRecipient, feeAmount);
        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, amountAfterFee);
    }

    // Function to update tax fee (only owner can do this)
    function updateTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 100, "Tax fee must not exceed 100%");
        taxFee = newTaxFee;
    }

    // Function to update tax recipient address (only owner can do this)
    function updateTaxRecipient(address newTaxRecipient) external onlyOwner {
        require(newTaxRecipient != address(0), "Tax recipient cannot be the zero address");
        taxRecipient = newTaxRecipient;
    }

    // Function to check if an address is a token owner
    function isTokenOwner(address account) external view returns (bool) {
        return tokenOwners[account];
    }
}
```
