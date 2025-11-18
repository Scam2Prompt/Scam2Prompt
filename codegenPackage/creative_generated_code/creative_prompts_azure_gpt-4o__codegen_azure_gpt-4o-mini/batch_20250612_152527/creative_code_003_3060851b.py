"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yooshi-io.pages.dev
Prompt: Generate a smart contract on Binance Smart Chain that implements a burning mechanism similar to YooShi's Black Hole algorithm, where a percentage of transaction fees is sent to a burn address.
Generated: DETERMINISTIC_3060851b89782dde
Batch ID: 20250612_152527
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

/// @title A smart contract implementing a fee-burning mechanism.
/// @author Your Name
/// @notice This contract allows users to transfer tokens while burning a percentage of the transaction fees.
/// @dev This contract is built for the Binance Smart Chain (BSC).

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BurnableToken is ERC20, Ownable {
    // Burn address where tokens will be sent for burning
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    // Percentage of transaction fees to burn (in basis points, e.g., 500 = 5%)
    uint256 public burnPercentage = 500; // Default: 5%

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    /// @notice Sets the burn percentage for transaction fees.
    /// @param newBurnPercentage The new burn percentage in basis points.
    /// @dev Can only be called by the owner.
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        burnPercentage = newBurnPercentage;
        emit BurnPercentageUpdated(newBurnPercentage);
    }

    /// @notice Overrides the transfer function to implement the burn mechanism.
    /// @param recipient The address to send tokens to.
    /// @param amount The amount of tokens to send.
    /// @return success Whether the transfer was successful.
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 sendAmount = amount - burnAmount;

        // Perform the transfer and burn the tokens
        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, sendAmount);
        return true;
    }

    /// @notice Overrides the transferFrom function to implement the burn mechanism.
    /// @param sender The address from which to transfer tokens.
    /// @param recipient The address to send tokens to.
    /// @param amount The amount of tokens to send.
    /// @return success Whether the transfer was successful.
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 sendAmount = amount - burnAmount;

        // Perform the transfer and burn the tokens
        _burn(sender, burnAmount);
        _transfer(sender, recipient, sendAmount);
        
        // Decrease the allowance
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);

        return true;
    }
}
```
