"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hpos10iclaim.pages.dev
Prompt: Develop a script in Solidity to wrap BITCOIN tokens on the BASE chain, referencing the HarryPotterObamaSonic10Inu token's functionality.
Generated: DETERMINISTIC_520b8ae58f920eff
Batch ID: 20250612_145619
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

/// @title Bitcoin Wrapper Contract on Base Chain
/// @author Your Name
/// @notice This contract wraps Bitcoin tokens using the functionality inspired by the HarryPotterObamaSonic10Inu token.
/// @dev Ensure to test thoroughly before deploying on the mainnet.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BitcoinWrapper is Ownable {
    using SafeMath for uint256;

    // Wrapped Bitcoin token interface
    IERC20 public immutable wrappedBitcoin;

    // Event emitted when Bitcoin tokens are wrapped
    event Wrapped(address indexed user, uint256 amount);

    // Event emitted when Bitcoin tokens are unwrapped
    event Unwrapped(address indexed user, uint256 amount);

    /// @param _wrappedBitcoin Address of the wrapped Bitcoin ERC20 token
    constructor(IERC20 _wrappedBitcoin) {
        require(address(_wrappedBitcoin) != address(0), "Invalid token address");
        wrappedBitcoin = _wrappedBitcoin;
    }

    /// @notice Wraps a specified amount of Bitcoin tokens
    /// @param amount The amount of Bitcoin tokens to wrap
    /// @dev The function will require the user to approve this contract to spend their Bitcoin tokens first
    function wrap(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer Bitcoin tokens from sender to this contract
        wrappedBitcoin.transferFrom(msg.sender, address(this), amount);

        // Emit the wrap event
        emit Wrapped(msg.sender, amount);
    }

    /// @notice Unwraps a specified amount of wrapped Bitcoin tokens back into Bitcoin
    /// @param amount The amount of wrapped Bitcoin tokens to unwrap
    function unwrap(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(wrappedBitcoin.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer wrapped Bitcoin tokens from this contract to the sender
        wrappedBitcoin.transfer(msg.sender, amount);

        // Emit the unwrap event
        emit Unwrapped(msg.sender, amount);
    }

    /// @notice Allows the owner to withdraw any ERC20 tokens sent to this contract
    /// @param token The address of the token to withdraw
    /// @param amount The amount of tokens to withdraw
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens from this contract to the owner
        token.transfer(msg.sender, amount);
    }
}
```
