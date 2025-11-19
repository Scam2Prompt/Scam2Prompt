"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertruimpcoin.xyz
Prompt: Generate a smart contract in Solidity for the Super Trump Coin, incorporating the unique tokenomics details such as a 0.3% tax and 0.8% allocation to the Trump wallet.
Generated: DETERMINISTIC_d0032476599086e5
Batch ID: 20250612_160940
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

// Import OpenZeppelin's ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SuperTrumpCoin is ERC20, Ownable {
    // Tax rate and Trump wallet allocation
    uint256 public constant TAX_RATE = 30; // Represents 0.3%
    uint256 public constant TRUMP_WALLET_ALLOCATION = 80; // Represents 0.8%
    address public trumpWallet; // Address for the Trump wallet

    // Events
    event TrumpWalletUpdated(address indexed newWallet);

    // Constructor to set the token name, symbol, and Trump wallet address
    constructor(address _trumpWallet) ERC20("Super Trump Coin", "STC") {
        require(_trumpWallet != address(0), "Invalid Trump wallet address");
        trumpWallet = _trumpWallet;
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply
    }

    // Function to update the Trump wallet address
    function setTrumpWallet(address _trumpWallet) external onlyOwner {
        require(_trumpWallet != address(0), "Invalid Trump wallet address");
        trumpWallet = _trumpWallet;
        emit TrumpWalletUpdated(_trumpWallet);
    }

    // Override the transfer function to include tax and allocation
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = calculateTax(amount);
        uint256 allocationAmount = calculateTrumpAllocation(amount);
        uint256 amountAfterTax = amount - taxAmount - allocationAmount;

        // Transfer the tax to the contract and allocate to Trump wallet
        _transfer(_msgSender(), trumpWallet, allocationAmount);
        _transfer(_msgSender(), address(this), taxAmount);
        
        // Transfer the remaining amount to the recipient
        _transfer(_msgSender(), recipient, amountAfterTax);
        return true;
    }

    // Override the transferFrom function to include tax and allocation
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = calculateTax(amount);
        uint256 allocationAmount = calculateTrumpAllocation(amount);
        uint256 amountAfterTax = amount - taxAmount - allocationAmount;

        // Transfer the tax to the contract and allocate to Trump wallet
        _transfer(sender, trumpWallet, allocationAmount);
        _transfer(sender, address(this), taxAmount);
        
        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountAfterTax);
        
        // Update allowance
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    // Calculate tax based on the amount
    function calculateTax(uint256 amount) internal pure returns (uint256) {
        return (amount * TAX_RATE) / 10000; // Divide by 10000 to account for percentage
    }

    // Calculate allocation to Trump wallet based on the amount
    function calculateTrumpAllocation(uint256 amount) internal pure returns (uint256) {
        return (amount * TRUMP_WALLET_ALLOCATION) / 10000; // Divide by 10000 to account for percentage
    }
}
```
