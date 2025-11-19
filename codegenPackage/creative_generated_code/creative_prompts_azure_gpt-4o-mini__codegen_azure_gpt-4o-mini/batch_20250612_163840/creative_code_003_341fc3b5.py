"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowonbasenets.pages.dev
Prompt: Provide an example of how to set up a contract address for a token with renounced ownership, similar to the $COW token.
Generated: DETERMINISTIC_341fc3b504c18f63
Batch ID: 20250612_163840
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title COWToken
 * @dev ERC20 Token with renounced ownership feature
 */
contract COWToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1000000 * 10**18; // 1 million tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of the initial tokens.
     */
    constructor() ERC20("COW Token", "COW") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to renounce ownership of the contract.
     * This will ensure no further changes can be made to the contract.
     * Ownership is renounced by calling the renounceOwnership function from Ownable.
     */
    function renounceOwnership() public override onlyOwner {
        // Call the parent contract's renounceOwnership function
        super.renounceOwnership();
    }

    /**
     * @dev Transfer tokens from one address to another.
     * @param recipient The address to receive the tokens.
     * @param amount The number of tokens to be transferred.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "COWToken: transfer to the zero address");
        require(amount > 0, "COWToken: transfer amount must be greater than zero");

        // Call the parent contract's transfer function and return the result
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Transfer tokens from one address to another using allowance mechanism.
     * @param sender The address which will send the tokens.
     * @param recipient The address which will receive the tokens.
     * @param amount The number of tokens to be transferred.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "COWToken: transfer from the zero address");
        require(recipient != address(0), "COWToken: transfer to the zero address");
        require(amount > 0, "COWToken: transfer amount must be greater than zero");

        // Call the parent contract's transferFrom function and return the result
        return super.transferFrom(sender, recipient, amount);
    }
}
```
