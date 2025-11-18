"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotokenhub.com
Prompt: Create a script to adjust the initial supply of an ERC-20 token after deployment using CryptoTokenHub's intuitive token owner dashboard.
Generated: DETERMINISTIC_afd2de4204c9b72b
Batch ID: 20250612_152426
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AdjustableToken
 * @dev ERC20 Token with adjustable initial supply by token owner
 */
contract AdjustableToken is ERC20, Ownable {
    // Define the maximum supply for the token
    uint256 private _maxSupply;

    /**
     * @dev Sets the values for {name} and {symbol}, and initializes max supply.
     * The initial supply is assigned to the deployer of the contract.
     * @param name Name of the token
     * @param symbol Symbol of the token
     * @param initialSupply Initial amount of tokens to be minted
     * @param maxSupply Maximum allowable supply for the token
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 maxSupply) 
        ERC20(name, symbol) 
    {
        require(initialSupply <= maxSupply, "Initial supply exceeds max supply");
        _maxSupply = maxSupply;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Adjusts the total supply of the token.
     * Only the owner can call this function.
     * @param newSupply The new total supply of tokens
     */
    function adjustSupply(uint256 newSupply) external onlyOwner {
        require(newSupply <= _maxSupply, "New supply exceeds max supply");
        require(newSupply != totalSupply(), "New supply is the same as current supply");

        if (newSupply > totalSupply()) {
            // Mint additional tokens to reach new supply
            _mint(msg.sender, newSupply - totalSupply());
        } else {
            // Burn tokens to decrease supply
            _burn(msg.sender, totalSupply() - newSupply);
        }
    }

    /**
     * @dev Returns the maximum supply of the token.
     * @return uint256 Maximum supply of the token
     */
    function maxSupply() external view returns (uint256) {
        return _maxSupply;
    }
}
```
