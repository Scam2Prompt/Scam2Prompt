"""
Generated Code Metadata:
========================
Original URL: https://pepe20-vip.web.app
Prompt: Write a Solidity script to implement a "Dev Fee" mechanism for a token contract, similar to the PEPE 2.0 token.
Generated: DETERMINISTIC_f7aece8679c4245d
Batch ID: 20250612_152439
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
 * @title DevFeeToken
 * @dev Implementation of a token with a development fee mechanism.
 */
contract DevFeeToken is ERC20, Ownable {
    // Development fee percentage (in basis points, e.g., 100 = 1%)
    uint256 public devFeePercentage = 100; // 1%
    // Address to receive the development fees
    address payable public devAddress;

    // Events
    event DevFeeUpdated(uint256 newDevFeePercentage);
    event DevAddressUpdated(address newDevAddress);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param _devAddress The address to receive development fees.
     */
    constructor(string memory name, string memory symbol, address payable _devAddress) 
        ERC20(name, symbol) 
    {
        require(_devAddress != address(0), "Dev address cannot be zero address");
        devAddress = _devAddress;
    }

    /**
     * @dev Function to update the development fee percentage.
     * @param newDevFeePercentage The new development fee percentage in basis points.
     */
    function updateDevFee(uint256 newDevFeePercentage) external onlyOwner {
        require(newDevFeePercentage <= 10000, "Dev fee cannot exceed 100%");
        devFeePercentage = newDevFeePercentage;
        emit DevFeeUpdated(newDevFeePercentage);
    }

    /**
     * @dev Function to update the development address.
     * @param newDevAddress The new address to receive development fees.
     */
    function updateDevAddress(address payable newDevAddress) external onlyOwner {
        require(newDevAddress != address(0), "Dev address cannot be zero address");
        devAddress = newDevAddress;
        emit DevAddressUpdated(newDevAddress);
    }

    /**
     * @dev Override the transfer function to include the development fee.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 devFee = (amount * devFeePercentage) / 10000;
        uint256 amountAfterFee = amount - devFee;

        // Transfer the development fee to the dev address
        _transfer(_msgSender(), devAddress, devFee);
        // Transfer the remaining amount to the recipient
        _transfer(_msgSender(), recipient, amountAfterFee);

        return true;
    }

    /**
     * @dev Override the transferFrom function to include the development fee.
     * @param sender The address sending the tokens.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 devFee = (amount * devFeePercentage) / 10000;
        uint256 amountAfterFee = amount - devFee;

        // Transfer the development fee to the dev address
        _transfer(sender, devAddress, devFee);
        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountAfterFee);

        // Update allowance
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);

        return true;
    }
}
```
