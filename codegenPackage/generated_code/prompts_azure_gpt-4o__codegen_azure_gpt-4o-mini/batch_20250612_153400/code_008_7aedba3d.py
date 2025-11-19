"""
Generated Code Metadata:
========================
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a Solidity contract for DOGE20 that prevents inflation by enforcing a fixed token supply, as mentioned in the website's tokenomics section.
Generated: DETERMINISTIC_7aedba3df7abc7f2
Batch ID: 20250612_153400
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

/// @title DOGE20 Token Contract
/// @author Your Name
/// @notice This contract implements a fixed supply ERC20 token to prevent inflation.
/// @dev The total supply is set at deployment and cannot be changed thereafter.

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DOGE20 is ERC20, Ownable {
    // Fixed total supply of the token
    uint256 private constant _totalSupply = 1_000_000 * 10 ** decimals(); // 1 million tokens

    /// @notice Constructor that initializes the token with a fixed supply
    /// @dev The total supply is minted to the deployer's address
    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, _totalSupply);
    }

    /// @notice Function to transfer tokens
    /// @param recipient The address to receive the tokens
    /// @param amount The amount of tokens to transfer
    /// @return success A boolean indicating the success of the transfer
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    /// @notice Function to approve tokens for delegated transfer
    /// @param spender The address allowed to spend the tokens
    /// @param amount The amount of tokens to approve
    /// @return success A boolean indicating the success of the approval
    function approve(address spender, uint256 amount) public override returns (bool success) {
        require(spender != address(0), "Approval to the zero address is not allowed");
        return super.approve(spender, amount);
    }

    /// @notice Function to transfer tokens on behalf of another address
    /// @param sender The address from which to transfer tokens
    /// @param recipient The address to receive the tokens
    /// @param amount The amount of tokens to transfer
    /// @return success A boolean indicating the success of the transfer
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transferFrom(sender, recipient, amount);
    }

    /// @notice Function to get the total supply of the token
    /// @return totalSupply The total supply of the token
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```
