"""
Generated Code Metadata:
========================
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a Solidity contract for DOGE20 that prevents inflation by enforcing a fixed token supply, as mentioned in the website's tokenomics section.
Generated: DETERMINISTIC_7aedba3df7abc7f2
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token Contract
 * @dev Implementation of the ERC20 standard token with fixed supply.
 * The total supply is set at deployment and cannot be changed afterwards.
 */
contract DOGE20 is ERC20, Ownable {
    uint256 private constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that initializes the token with the fixed supply.
     * The entire supply is minted to the deployer's address.
     */
    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Overrides the ERC20 _mint function to prevent any additional minting.
     * @param account The address that would receive the minted tokens
     * @param amount The amount of tokens to be minted
     */
    function _mint(address account, uint256 amount) internal virtual override {
        require(totalSupply() + amount <= MAX_SUPPLY, "DOGE20: Cannot exceed max supply");
        super._mint(account, amount);
    }

    /**
     * @dev Prevents the owner from renouncing ownership to maintain contract integrity.
     */
    function renounceOwnership() public override onlyOwner {
        revert("DOGE20: Ownership cannot be renounced");
    }
}
```
