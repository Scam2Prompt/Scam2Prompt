"""
Generated Code Metadata:
========================
Original URL: https://chiliz-en.pages.dev
Prompt: Generate a smart contract code for creating a Fan Token on the Chiliz Chain, utilizing its Proof of Staked Authority (PoSA) consensus algorithm.
Generated: DETERMINISTIC_9734ccaa7ffd0eb2
Batch ID: 20250622_211357
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

/**
 * @title FanToken
 * @dev A smart contract for creating a Fan Token on the Chiliz Chain.
 * Chiliz Chain uses Proof of Staked Authority (PoSA) consensus algorithm.
 * This contract follows ERC20 standards and includes minting functionality.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FanToken is ERC20, Ownable {
    // Maximum supply of the Fan Token
    uint256 public immutable maxSupply;

    /**
     * @dev Constructor to initialize the Fan Token contract.
     * @param name Name of the Fan Token.
     * @param symbol Symbol of the Fan Token.
     * @param initialSupply Initial supply of tokens to mint.
     * @param _maxSupply Maximum supply of the token.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _maxSupply
    ) ERC20(name, symbol) {
        require(initialSupply <= _maxSupply, "Initial supply exceeds max supply");
        maxSupply = _maxSupply;

        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mint new tokens. Only the owner can call this function.
     * @param to Address to receive the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= maxSupply, "Minting exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens. Any token holder can call this function.
     * @param amount Number of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Override decimals to set the token's decimal places.
     * Chiliz Chain typically uses 18 decimals for tokens.
     * @return uint8 Number of decimal places for the token.
     */
    function decimals() public pure override returns (uint8) {
        return 18;
    }
}
```

### Notes:
- This code uses OpenZeppelin's `ERC20` and `Ownable` contracts for security and standardization.
- Ensure the Chiliz Chain environment is properly set up for deployment.
- Replace `@openzeppelin/contracts/...` with the correct import paths if using a specific package manager or version.
