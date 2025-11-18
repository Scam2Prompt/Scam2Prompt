"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berryeth.vip
Prompt: Write code in Solidity to implement a zero-tax mechanism for a new token similar to $BERRY, ensuring it adheres to the tokenomics principles described.
Generated: DETERMINISTIC_658bf78b9e0dc539
Batch ID: 20250612_153947
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

// Importing OpenZeppelin's ERC20 implementation for secure token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BerryToken
 * @dev This contract implements a zero-tax ERC20 token similar to $BERRY.
 * The token has a fixed supply and does not impose any transaction taxes.
 */
contract BerryToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * (10 ** 18); // 1 million tokens with 18 decimal places

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Berry Token", "BERRY") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to transfer tokens, adhering to the ERC20 standard.
     * Overrides the transfer function to implement zero-tax transfers.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating the success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Call the ERC20 transfer function
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Function to transfer tokens on behalf of another address, adhering to the ERC20 standard.
     * Overrides the transferFrom function to implement zero-tax transfers.
     * @param sender The address which owns the tokens and will transfer them.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating the success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Call the ERC20 transferFrom function
        _transfer(sender, recipient, amount);

        // Update allowance
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "Transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);

        return true;
    }

    /**
     * @dev Function to mint new tokens. Only the contract owner can mint tokens.
     * @param account The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Minting to the zero address is not allowed");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint the new tokens and assign them to account
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(_msgSender(), amount);
    }
}
```
