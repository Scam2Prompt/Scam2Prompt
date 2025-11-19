"""
Generated Code Metadata:
========================
Original URL: https://arbinu.app
Prompt: Write a Solidity function to implement a 4% transaction fee for Arbinu token transfers, as specified in the tokenomics section of the website.
Generated: DETERMINISTIC_6495d2d2fbdffdd2
Batch ID: 20250612_153916
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

contract ArbinuToken is ERC20, Ownable {
    // Address where transaction fees will be sent
    address public feeRecipient;
    // Transaction fee percentage (4%)
    uint256 public constant FEE_PERCENTAGE = 4;

    /**
     * @dev Constructor that initializes the token and sets the fee recipient
     * @param initialSupply Initial token supply
     * @param recipient Address to receive transaction fees
     */
    constructor(uint256 initialSupply, address recipient) ERC20("Arbinu Token", "ARBINU") {
        _mint(msg.sender, initialSupply);
        feeRecipient = recipient;
    }

    /**
     * @dev Override ERC20 transfer to implement 4% transaction fee
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        uint256 fee = (amount * FEE_PERCENTAGE) / 100;
        uint256 amountAfterFee = amount - fee;

        // Transfer fee to fee recipient
        _transfer(msg.sender, feeRecipient, fee);
        // Transfer remaining amount to recipient
        _transfer(msg.sender, recipient, amountAfterFee);

        return true;
    }

    /**
     * @dev Override ERC20 transferFrom to implement 4% transaction fee
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        uint256 fee = (amount * FEE_PERCENTAGE) / 100;
        uint256 amountAfterFee = amount - fee;

        // Transfer fee to fee recipient
        _transfer(sender, feeRecipient, fee);
        // Transfer remaining amount to recipient
        _transfer(sender, recipient, amountAfterFee);

        // Update allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        return true;
    }

    /**
     * @dev Update the fee recipient address (only callable by owner)
     * @param newRecipient New address to receive transaction fees
     */
    function setFeeRecipient(address newRecipient) external onlyOwner {
        require(newRecipient != address(0), "Invalid address");
        feeRecipient = newRecipient;
    }
}
```
