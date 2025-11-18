"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertruimpcoin.xyz
Prompt: Create a Solidity smart contract that implements tokenomics similar to Super Trump Coin, including features like a 0.3% tax and reserving 0.8% for a specific wallet.
Generated: DETERMINISTIC_9ca3671ae66b1d0f
Batch ID: 20250612_152235
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

contract SuperTrumpCoin is ERC20, Ownable {
    uint256 public constant TAX_PERCENTAGE = 30; // 0.3% tax
    uint256 public constant RESERVE_PERCENTAGE = 80; // 0.8% reserve
    address public reserveWallet;

    event ReserveWalletChanged(address indexed oldWallet, address indexed newWallet);

    // Constructor to initialize the token with its name, symbol, and reserve wallet
    constructor(string memory name, string memory symbol, address _reserveWallet) ERC20(name, symbol) {
        require(_reserveWallet != address(0), "Reserve wallet cannot be zero address");
        reserveWallet = _reserveWallet;
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Minting initial supply
    }

    // Update the reserve wallet address
    function setReserveWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero address");
        emit ReserveWalletChanged(reserveWallet, _newWallet);
        reserveWallet = _newWallet;
    }

    // Override the _transfer function to include tax and reserve logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate tax and reserve amounts
        uint256 taxAmount = (amount * TAX_PERCENTAGE) / 10000; // 0.3% tax
        uint256 reserveAmount = (amount * RESERVE_PERCENTAGE) / 10000; // 0.8% reserve
        uint256 transferAmount = amount - taxAmount - reserveAmount;

        // Transfer tax and reserve amounts
        super._transfer(sender, reserveWallet, reserveAmount);
        super._transfer(sender, address(this), taxAmount); // Tax can be used for further features like burn or liquidity
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to withdraw tax collected to the owner's address (to be implemented later)
    function withdrawTax() external onlyOwner {
        uint256 taxBalance = balanceOf(address(this));
        require(taxBalance > 0, "No tax available to withdraw");

        // Transfer tax to the owner
        super._transfer(address(this), owner(), taxBalance);
    }
}
```
