"""
Generated Code Metadata:
========================
Original URL: https://clean-4dq.pages.dev
Prompt: Write a smart contract that demonstrates the issuance of assets on SatoshiVM, utilizing its compatibility with the Ethereum ecosystem and native BTC gas.
Generated: DETERMINISTIC_49b4436a30851ed2
Batch ID: 20250612_152326
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for issuing assets on SatoshiVM
contract AssetIssuer is ERC20, Ownable {
    // Event emitted when new assets are issued
    event AssetsIssued(address indexed to, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Function to issue new assets (tokens) to a specified address.
     * @param to The address to which the new assets will be issued.
     * @param amount The amount of assets to issue.
     */
    function issueAssets(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot issue to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        // Mint new tokens to the specified address
        _mint(to, amount);

        // Emit an event for the issuance
        emit AssetsIssued(to, amount);
    }

    /**
     * @dev Function to burn assets (tokens) from a specified address.
     * @param from The address from which the assets will be burned.
     * @param amount The amount of assets to burn.
     */
    function burnAssets(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(from) >= amount, "Insufficient balance to burn");

        // Burn tokens from the specified address
        _burn(from, amount);
    }

    /**
     * @dev Function to retrieve the total supply of assets.
     * @return The total supply of the asset tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return super.totalSupply();
    }

    /**
     * @dev Function to retrieve the balance of a specific address.
     * @param account The address to check the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }
}
```
