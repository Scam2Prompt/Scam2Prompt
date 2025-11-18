"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Provide an example of a Solidity smart contract that prevents inflation by enforcing a fixed token supply, similar to DOGE20.
Generated: DETERMINISTIC_eb7c1a021ffd6ea4
Batch ID: 20250612_153400
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

// Importing OpenZeppelin's ERC20 implementation for security and best practices
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FixedSupplyToken
 * @dev This contract implements a simple ERC20 token with a fixed supply
 */
contract FixedSupplyToken is ERC20, Ownable {
    // Total supply of tokens is fixed and defined during contract deployment
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    /**
     * @dev Constructor that gives the deployer all initial tokens
     */
    constructor() ERC20("FixedSupplyToken", "FST") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to mint tokens; restricted to the owner
     * @param account The address of the account to mint tokens to
     * @param amount The amount of tokens to mint
     * This function will always revert as minting is not allowed in this contract
     */
    function mint(address account, uint256 amount) external onlyOwner {
        revert("Minting is not allowed. Total supply is fixed.");
    }

    /**
     * @dev Override the _mint function to prevent any further minting
     * @param account The address of the account to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal override {
        // Disallow minting - total supply is fixed
        require(totalSupply() + amount <= TOTAL_SUPPLY, "Cannot mint beyond total supply");
        super._mint(account, amount);
    }
}
```
