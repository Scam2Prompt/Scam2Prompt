"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-e.pages.dev
Prompt: Describe how to utilize the DOGE20 tokenomics in a smart contract to ensure fixed supply and prevent inflation.
Generated: DETERMINISTIC_166f1062631b5f80
Batch ID: 20250612_160804
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

// Importing OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token
 * @dev Implementation of a fixed supply ERC20 token to prevent inflation.
 * This contract sets a maximum supply and does not allow minting or burning tokens.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 100_000_000 * 10**18; // 100 million tokens with 18 decimals

    // Event emitted when tokens are minted (not used in this contract)
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Override the _mint function to prevent any further minting.
     * This ensures that the total supply is fixed after the contract deployment.
     */
    function _mint(address account, uint256 amount) internal virtual override {
        require(totalSupply() + amount <= _totalSupply, "Cannot mint beyond fixed supply");
        super._mint(account, amount);
    }

    /**
     * @dev Override the mint function to prevent minting.
     * This ensures that no additional tokens can be created.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        revert("Minting is disabled for DOGE20 token");
    }

    /**
     * @dev Override the burn function to prevent burning of tokens.
     * This ensures that tokens cannot be destroyed, maintaining the fixed supply.
     */
    function burn(uint256 amount) external {
        revert("Burning is disabled for DOGE20 token");
    }

    /**
     * @dev Function to check the total supply of the token.
     * @return uint256 representing the total supply
     */
    function totalSupply() public view virtual override returns (uint256) {
        return _totalSupply;
    }
}
```
