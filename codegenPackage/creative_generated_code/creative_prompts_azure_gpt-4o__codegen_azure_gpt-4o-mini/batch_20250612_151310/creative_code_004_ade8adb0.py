"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-edd.pages.dev
Prompt: Create a function in Solidity that prevents inflation by enforcing a fixed supply for DOGE20 tokens, as outlined in the tokenomics section.
Generated: DETERMINISTIC_ade8adb0b585b709
Batch ID: 20250612_151310
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
 * @title DOGE20 Token
 * @dev This contract implements a fixed supply ERC20 token with no minting capability,
 * preventing inflation by enforcing a hard cap on the total supply.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the DOGE20 token
    uint256 private constant _totalSupply = 1000000 * (10 ** 18); // 1 million tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Override the _mint function to prevent minting after deployment.
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function _mint(address account, uint256 amount) internal override {
        require(totalSupply() + amount <= _totalSupply, "DOGE20: Total supply exceeded");
        super._mint(account, amount);
    }

    /**
     * @dev Override the mint function to prevent minting completely.
     * This function will revert if called.
     */
    function mint(address account, uint256 amount) external {
        revert("DOGE20: Minting is not allowed");
    }
}
```
