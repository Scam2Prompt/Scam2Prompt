"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arebitrumbrudge.gitbook.io
Prompt: Create a smart contract that utilizes the Arbitrum network for faster transaction processing, referencing the key features of Arbitrum's layer-2 blockchain.
Generated: DETERMINISTIC_d6ed65a55f536a35
Batch ID: 20250612_154913
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

// Import OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ArbitrumToken
 * @dev This contract implements an ERC20 token optimized for the Arbitrum layer-2 blockchain.
 * It allows for faster transactions and lower fees compared to layer-1 solutions.
 */
contract ArbitrumToken is ERC20, Ownable {
    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Sets the values for {name} and {symbol} of the token.
     * The owner of the contract will have the ability to mint and burn tokens.
     * @param name The name of the token
     * @param symbol The symbol of the token
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Mint new tokens to the specified address.
     * Only the owner can call this function.
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burn tokens from the caller's balance.
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override the _beforeTokenTransfer function to include custom logic before token transfers.
     * This could include various checks or logging mechanisms.
     * @param from The address tokens are being transferred from
     * @param to The address tokens are being transferred to
     * @param amount The amount of tokens being transferred
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        // Custom logic could be added here if necessary
    }
}
```
