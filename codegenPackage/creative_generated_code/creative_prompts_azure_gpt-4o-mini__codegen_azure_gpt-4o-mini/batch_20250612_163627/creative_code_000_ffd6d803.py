"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliamrewradnow.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a total supply of 420.69 trillion and 0% buy/sell tax, inspired by the Ice Land project.
Generated: DETERMINISTIC_ffd6d8032735aa09
Batch ID: 20250612_163627
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

// Importing OpenZeppelin's ERC20 implementation for secure token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title IceLandToken
 * @dev Implementation of the Ice Land inspired ERC20 token
 */
contract IceLandToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 420690000000000000000000000000; // 420.69 trillion tokens

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Ice Land Token", "ICE") {
        // Mint the total supply to the owner of the contract
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allows the owner to mint new tokens.
     * @param account The address to which the minted tokens will be sent.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Mint to the zero address");
        require(amount > 0, "Mint amount must be greater than 0");

        _mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from an account.
     * @param account The address from which the tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Burn from the zero address");
        require(amount > 0, "Burn amount must be greater than 0");

        _burn(account, amount);
    }

    /**
     * @dev Override the transfer function to include custom logic if needed in the future.
     * Currently, it allows transfer without any tax.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to include custom logic if needed in the future.
     * Currently, it allows transfer without any tax.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }
}
```
