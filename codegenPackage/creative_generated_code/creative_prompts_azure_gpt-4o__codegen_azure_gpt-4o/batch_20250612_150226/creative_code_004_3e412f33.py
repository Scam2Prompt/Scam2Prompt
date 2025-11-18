"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity function within an OFT contract to mint tokens on a destination blockchain using LayerZero's `_credit` method.
Generated: DETERMINISTIC_3e412f33604375a4
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@layerzerolabs/oft/contracts/OmnichainFungibleToken.sol";

// Extend the OmnichainFungibleToken (OFT) contract to create a custom minting functionality.
contract CustomOFT is OmnichainFungibleToken, Ownable {
    // Constructor to initialize the token name, symbol, and LayerZero endpoint.
    constructor(string memory name, string memory symbol, address endpoint)
        OmnichainFungibleToken(name, symbol, endpoint)
    {}

    /**
     * @notice Mints tokens on the destination blockchain using LayerZero's `_credit` method.
     * @dev Only callable by the owner (can be modified for more granular access control).
     * @param dstChainId The LayerZero destination chain ID where the tokens will be credited.
     * @param to The recipient address on the destination chain.
     * @param amount The amount of tokens to mint/credit.
     */
    function mintToDestination(
        uint16 dstChainId,
        address to,
        uint256 amount
    ) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Ensure sufficient balance exists to mint tokens on the destination.
        // `_credit` is a low-level LayerZero method that credits tokens to a user on the destination chain.
        try this._credit(dstChainId, to, amount) {
            // Minting/crediting was successful, nothing more to do here.
        } catch (bytes memory err) {
            // Handle the error if `_credit` fails for any reason.
            revert(string(abi.encodePacked("Mint failed: ", err)));
        }
    }
}
```
