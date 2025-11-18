"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ttrumpwallet.com
Prompt: Develop a blockchain-based token system in Solidity that functions as a symbol of support for specific ideals, similar to the "$TRUMP" token concept.
Generated: DETERMINISTIC_c053ef26f769faf3
Batch ID: 20250612_145114
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title SupportToken
// @dev A simple ERC20 token representing support for specific ideals.
// This token can be minted and burned by the owner.
contract SupportToken is ERC20, Ownable {
    // Events that can be emitted during token transfers
    event TokenMinted(address indexed recipient, uint256 amount);
    event TokenBurned(address indexed account, uint256 amount);

    // @dev The constructor initializes the token with a name and symbol.
    constructor() ERC20("SupportToken", "STKN") {}

    // @dev Mint new tokens to a specified address.
    // @param recipient The address that will receive the minted tokens.
    // @param amount The amount of tokens to mint.
    function mint(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero.");
        require(amount > 0, "Mint amount must be greater than zero.");

        // Mint the tokens
        _mint(recipient, amount);
        emit TokenMinted(recipient, amount);
    }

    // @dev Burn a specified amount of tokens from the caller's account.
    // @param amount The amount of tokens to burn.
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero.");
        _burn(msg.sender, amount);
        emit TokenBurned(msg.sender, amount);
    }

    // @dev Override the _beforeTokenTransfer hook to include additional logic if needed in the future.
    // @param from The address sending the tokens.
    // @param to The address receiving the tokens.
    // @param amount The amount of tokens being transferred.
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Add additional checks or logic if required
    }
}
```
