"""
Generated Code Metadata:
========================
Original URL: https://galaxyfoxs.live
Prompt: Generate a smart contract code in Solidity for a token burn mechanism, similar to the one implemented in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_b8deb7d1f5724aa0
Batch ID: 20250622_211215
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenBurnable is an ERC20 token with a burn mechanism
contract TokenBurnable is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens by calling the internal _burn function
        _burn(msg.sender, amount);
        // Emit the TokensBurned event
        emit TokensBurned(msg.sender, amount);
    }

    // Function to burn tokens on behalf of another account (only owner)
    function burnFrom(address account, uint256 amount) external onlyOwner {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Burn amount must be greater than zero");
        // Ensure the account has enough tokens to burn
        require(balanceOf(account) >= amount, "Insufficient balance to burn");

        // Call the internal _burn function
        _burn(account, amount);
        // Emit the TokensBurned event
        emit TokensBurned(account, amount);
    }
}
```
