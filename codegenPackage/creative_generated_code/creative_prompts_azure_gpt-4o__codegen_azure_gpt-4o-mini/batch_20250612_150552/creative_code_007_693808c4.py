"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20claim-now.pages.dev
Prompt: Generate code for an ERC-20 token contract in Solidity that prevents inflation by enforcing a fixed supply, similar to the DOGE20 tokenomics model.
Generated: DETERMINISTIC_693808c486f8567a
Batch ID: 20250612_150552
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

/// @title Fixed Supply ERC20 Token
/// @notice This contract implements an ERC20 token with a fixed supply to prevent inflation.
/// @dev Follows the ERC20 standard as defined in the EIP-20 specification.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FixedSupplyToken is ERC20Burnable, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens, with 18 decimals

    /// @dev Constructor that sets the name and symbol of the token and mints the total supply to the deployer's address.
    constructor() ERC20("Fixed Supply Token", "FST") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /// @notice Minting new tokens is not allowed, enforcing fixed supply.
    /// @dev This function will revert if called.
    function mint(address to, uint256 amount) public override onlyOwner {
        revert("Minting is not allowed: Fixed supply enforced.");
    }

    /// @notice Transfers tokens between addresses with built-in checks.
    /// @dev Overriding the transfer function to add custom error handling if needed.
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    /// @notice Transfers tokens from one address to another with built-in checks.
    /// @dev Overriding the transferFrom function for additional error handling.
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transferFrom(sender, recipient, amount);
    }

    /// @notice Function to retrieve the total supply of the token.
    /// @return Total supply of the token as a uint256.
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }
}
```
