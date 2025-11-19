"""
Generated Code Metadata:
========================
Original URL: https://etherealize.fi
Prompt: Generate a Solidity smart contract template for tokenizing Wall Street trading assets, ensuring compatibility with Ethereum's security and scalability features highlighted by Etherealize.
Generated: DETERMINISTIC_83be7a85872c55bc
Batch ID: 20250612_155042
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";

/**
 * @title WallStreetAssetToken
 * @dev ERC20 token representing tokenized Wall Street trading assets
 * Features:
 * - Ownable with transfer ownership
 * - Pausable for emergency stops
 * - Snapshot for historical balances
 * - Permit for gasless approvals
 * - Votes for governance
 * - Burnable
 */
contract WallStreetAssetToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable, ERC20Permit, ERC20Votes {
    /**
     * @dev Initializes the contract with a name, symbol, and initial supply
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply_ Initial token supply (in smallest units)
     * @param owner_ Address of the initial owner
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        address owner_
    ) ERC20(name_, symbol_) ERC20Permit(name_) {
        require(initialSupply_ > 0, "Initial supply must be greater than zero");
        require(owner_ != address(0), "Owner address cannot be zero");
        
        _mint(owner_, initialSupply_);
        transferOwnership(owner_);
    }

    /**
     * @dev Creates a new snapshot ID
     * @return uint256 The new snapshot ID
     */
    function snapshot() public onlyOwner returns (uint256) {
        return _snapshot();
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Mints new tokens
     * @param to Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     * @param from Address sending tokens
     * @param to Address receiving tokens
     * @param amount Amount of tokens being transferred
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Hook that is called after any transfer of tokens
     * @param from Address sending tokens
     * @param to Address receiving tokens
     * @param amount Amount of tokens being transferred
     */
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Votes) {
        super._afterTokenTransfer(from, to, amount);
    }

    /**
     * @dev Creates an amount of tokens and assigns them to account, increasing total supply
     * @param account Address receiving minted tokens
     * @param amount Amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._mint(account, amount);
    }

    /**
     * @dev Destroys an amount of tokens from account, reducing total supply
     * @param account Address whose tokens are burned
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._burn(account, amount);
    }
}
```
