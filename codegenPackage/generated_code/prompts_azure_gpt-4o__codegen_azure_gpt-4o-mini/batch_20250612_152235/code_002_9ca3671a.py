"""
Generated Code Metadata:
========================
Original URL: https://supertruimpcoin.xyz
Prompt: Create a Solidity smart contract that implements tokenomics similar to Super Trump Coin, including features like a 0.3% tax and reserving 0.8% for a specific wallet.
Generated: DETERMINISTIC_9ca3671ae66b1d0f
Batch ID: 20250612_152235
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

/**
 * @title SuperTrumpCoin
 * @dev ERC20 Token with tax and reserve features
 */
contract SuperTrumpCoin is ERC20, Ownable {
    // Tax rate (0.3%)
    uint256 public constant TAX_RATE = 30; // 30 basis points
    // Reserve wallet address
    address public reserveWallet;
    // Total supply of tokens
    uint256 private _totalSupply;

    // Events
    event ReserveWalletUpdated(address indexed newReserveWallet);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * @param initialSupply The initial supply of tokens
     * @param _reserveWallet The address to reserve 0.8% of the tokens
     */
    constructor(uint256 initialSupply, address _reserveWallet) ERC20("Super Trump Coin", "STC") {
        require(_reserveWallet != address(0), "Reserve wallet cannot be the zero address");
        reserveWallet = _reserveWallet;
        _totalSupply = initialSupply * (10 ** decimals());
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Override the transfer function to implement tax and reserve features
     * @param recipient The address to receive the tokens
     * @param amount The amount of tokens to transfer
     * @return bool indicating success
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = (amount * TAX_RATE) / 10000; // Calculate tax
        uint256 reserveAmount = (amount * 80) / 10000; // Calculate reserve amount (0.8%)
        uint256 transferAmount = amount - taxAmount - reserveAmount; // Calculate final transfer amount

        // Transfer tax to the contract owner
        _transfer(msg.sender, owner(), taxAmount);
        // Transfer reserve to the reserve wallet
        _transfer(msg.sender, reserveWallet, reserveAmount);
        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Update the reserve wallet address
     * @param newReserveWallet The new reserve wallet address
     */
    function updateReserveWallet(address newReserveWallet) external onlyOwner {
        require(newReserveWallet != address(0), "New reserve wallet cannot be the zero address");
        reserveWallet = newReserveWallet;
        emit ReserveWalletUpdated(newReserveWallet);
    }

    /**
     * @dev Get the total supply of tokens
     * @return uint256 The total supply of tokens
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```
