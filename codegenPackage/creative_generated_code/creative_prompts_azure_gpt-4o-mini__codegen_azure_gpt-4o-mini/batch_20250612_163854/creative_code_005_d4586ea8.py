"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Develop a smart contract for the $FROP token that includes features for transparency and security, as highlighted in the Popo The Frog documentation.
Generated: DETERMINISTIC_d4586ea85c1d6813
Batch ID: 20250612_163854
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FROP Token Contract
 * @dev Implementation of the $FROP token with transparency and security features.
 */
contract FROP is Context, ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Events for tracking
    event TokensBurned(address indexed account, uint256 amount);
    event TokensFrozen(address indexed account);
    event TokensUnfrozen(address indexed account);

    // Mapping to track frozen accounts
    mapping(address => bool) private frozenAccounts;

    /**
     * @dev Sets the values for {name} and {symbol} and mints initial supply to the owner.
     */
    constructor(uint256 initialSupply) ERC20("FROP Token", "$FROP") {
        _mint(_msgSender(), initialSupply);
    }

    /**
     * @dev Modifier to check if the account is frozen.
     */
    modifier notFrozen(address account) {
        require(!frozenAccounts[account], "Account is frozen");
        _;
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external notFrozen(_msgSender()) {
        _burn(_msgSender(), amount);
        emit TokensBurned(_msgSender(), amount);
    }

    /**
     * @dev Function to freeze an account, preventing it from transferring tokens.
     * @param account The address to be frozen.
     */
    function freezeAccount(address account) external onlyOwner {
        require(!frozenAccounts[account], "Account is already frozen");
        frozenAccounts[account] = true;
        emit TokensFrozen(account);
    }

    /**
     * @dev Function to unfreeze a previously frozen account.
     * @param account The address to be unfrozen.
     */
    function unfreezeAccount(address account) external onlyOwner {
        require(frozenAccounts[account], "Account is not frozen");
        frozenAccounts[account] = false;
        emit TokensUnfrozen(account);
    }

    /**
     * @dev Overridden transfer function to include frozen account check.
     */
    function transfer(address recipient, uint256 amount) 
        public 
        virtual 
        override 
        notFrozen(_msgSender())
        notFrozen(recipient)
        returns (bool) 
    {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Overridden transferFrom function to include frozen account check.
     */
    function transferFrom(address sender, address recipient, uint256 amount) 
        public 
        virtual 
        override 
        notFrozen(sender)
        notFrozen(recipient)
        returns (bool) 
    {
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Pauses all token transfers.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers.
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}
```
