"""
Generated Code Metadata:
========================
Original URL: https://btconbase-ai.pages.dev
Prompt: Create a cryptocurrency token with a similar supply mechanism to Bitcoin on Base, including a total supply of 21 million tokens and a burned token supply, using a library like OpenZeppelin.
Generated: DETERMINISTIC_16671518c12e2892
Batch ID: 20250622_205230
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

// Importing the OpenZeppelin ERC20 contract and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the cryptocurrency token
contract MyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 21_000_000 * 10 ** 18; // 21 million tokens with 18 decimals
    // Burned token supply
    uint256 public burnedSupply;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("MyToken", "MTK") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to burn tokens
    function burn(uint256 amount) external {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);
        // Update the burned supply
        burnedSupply += amount;

        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    // Function to get the total supply including burned tokens
    function totalSupplyIncludingBurned() external view returns (uint256) {
        return TOTAL_SUPPLY - burnedSupply;
    }
}
```
