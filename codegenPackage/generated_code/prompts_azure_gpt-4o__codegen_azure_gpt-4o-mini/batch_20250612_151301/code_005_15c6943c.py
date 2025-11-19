"""
Generated Code Metadata:
========================
Original URL: https://thisismyiguana.pages.dev
Prompt: Develop a smart contract in Solidity for managing $TIMI tokens, ensuring it adheres to the 1 billion supply and 0/0 tax tokenomics described on the webpage.
Generated: DETERMINISTIC_15c6943cbe011746
Batch ID: 20250612_151301
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

/**
 * @title TIMI Token
 * @dev This contract implements the TIMI token with a total supply of 1 billion tokens.
 * The token has no transaction tax (0/0 tax).
 */
contract TIMIToken is ERC20, Ownable {
    // Total supply of the TIMI token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     */
    constructor() ERC20("TIMI Token", "TIMI") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens. Only the owner can mint new tokens.
     * @param to The address to which the minted tokens will be sent.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    /**
     * @dev Override the transfer function to ensure no tax is applied.
     * @param recipient The address to which tokens are being sent.
     * @param amount The amount of tokens to send.
     * @return success A boolean indicating the success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to ensure no tax is applied.
     * @param sender The address from which tokens are being sent.
     * @param recipient The address to which tokens are being sent.
     * @param amount The amount of tokens to send.
     * @return success A boolean indicating the success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }
}
```
