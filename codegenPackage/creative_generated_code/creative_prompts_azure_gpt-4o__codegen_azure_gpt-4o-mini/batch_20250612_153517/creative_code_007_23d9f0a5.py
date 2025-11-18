"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peng-six.vercel.app
Prompt: Design a smart contract for a meme token similar to $PENG, ensuring it includes features like revoked minting and liquidity freezing.
Generated: DETERMINISTIC_23d9f0a56d2f3328
Batch ID: 20250612_153517
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
 * @title MemeToken
 * @dev A simple ERC20 token with minting revocation and liquidity freezing features.
 */
contract MemeToken is ERC20, Ownable {
    // Variables to track minting and liquidity status
    bool public mintingRevoked;
    bool public liquidityFrozen;

    // Event to emit when minting is revoked
    event MintingRevoked();
    
    // Event to emit when liquidity is frozen
    event LiquidityFrozen();

    // Mapping to track frozen addresses for liquidity
    mapping(address => bool) public isLiquidityFrozen;

    // Modifier to check if minting is active
    modifier canMint() {
        require(!mintingRevoked, "Minting has been revoked");
        _;
    }

    // Modifier to check if liquidity is not frozen
    modifier notFrozen() {
        require(!liquidityFrozen, "Liquidity is currently frozen");
        _;
    }

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     */
    constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {
        mintingRevoked = false;
        liquidityFrozen = false;
    }

    /**
     * @dev Mint new tokens. Only callable if minting is not revoked.
     * @param to Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner canMint {
        _mint(to, amount);
    }

    /**
     * @dev Revoke further minting of the token.
     */
    function revokeMinting() public onlyOwner {
        mintingRevoked = true;
        emit MintingRevoked();
    }

    /**
     * @dev Freeze liquidity, preventing further actions on the liquidity pool.
     */
    function freezeLiquidity() public onlyOwner {
        liquidityFrozen = true;
        emit LiquidityFrozen();
    }

    /**
     * @dev Unfreeze liquidity, allowing actions on the liquidity pool.
     */
    function unfreezeLiquidity() public onlyOwner {
        liquidityFrozen = false;
    }

    /**
     * @dev Override transfer function to restrict transfers if liquidity is frozen.
     * @param to Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return success Boolean indicating success of the transfer
     */
    function transfer(address to, uint256 amount) public override notFrozen returns (bool success) {
        return super.transfer(to, amount);
    }

    /**
     * @dev Override transferFrom function to restrict transfers if liquidity is frozen.
     * @param from Address of the sender
     * @param to Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return success Boolean indicating success of the transfer
     */
    function transferFrom(address from, address to, uint256 amount) public override notFrozen returns (bool success) {
        return super.transferFrom(from, to, amount);
    }

    /**
     * @dev Function to check if liquidity is frozen for a specific address.
     * @param account Address to check
     * @return frozen Boolean indicating if the liquidity is frozen for the account
     */
    function isAccountLiquidityFrozen(address account) public view returns (bool) {
        return isLiquidityFrozen[account];
    }
}
```
