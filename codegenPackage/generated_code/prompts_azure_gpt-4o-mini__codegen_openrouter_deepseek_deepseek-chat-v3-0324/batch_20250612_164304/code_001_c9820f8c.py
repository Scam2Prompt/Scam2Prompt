"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity contract that utilizes LayerZero's OFT standard to transfer fungible tokens across multiple blockchains without using liquidity pools.
Generated: DETERMINISTIC_c9820f8c3f8ead29
Batch ID: 20250612_164304
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

import "@layerzerolabs/solidity-examples/contracts/token/oft/OFT.sol";

/**
 * @title CrossChainToken
 * @dev An OFT-compatible fungible token that can be transferred across chains using LayerZero
 */
contract CrossChainToken is OFT {
    /**
     * @dev Constructor that initializes the token with a name, symbol, and LayerZero endpoint
     * @param _name The name of the token
     * @param _symbol The symbol of the token
     * @param _lzEndpoint The LayerZero endpoint address
     * @param _initialSupply The initial supply of tokens to mint to the deployer
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _lzEndpoint,
        uint256 _initialSupply
    ) OFT(_name, _symbol, _lzEndpoint) {
        if (_initialSupply > 0) {
            _mint(msg.sender, _initialSupply);
        }
    }

    /**
     * @dev Mints new tokens. Only callable by the owner.
     * @param _to The address to mint tokens to
     * @param _amount The amount of tokens to mint
     */
    function mint(address _to, uint256 _amount) external onlyOwner {
        _mint(_to, _amount);
    }

    /**
     * @dev Burns tokens. Only callable by the owner.
     * @param _from The address to burn tokens from
     * @param _amount The amount of tokens to burn
     */
    function burn(address _from, uint256 _amount) external onlyOwner {
        _burn(_from, _amount);
    }
}
```
