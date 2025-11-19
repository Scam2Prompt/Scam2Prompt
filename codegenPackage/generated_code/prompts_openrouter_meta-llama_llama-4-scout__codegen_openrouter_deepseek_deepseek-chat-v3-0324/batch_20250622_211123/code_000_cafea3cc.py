"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a smart contract for the $GGG token using Solidity, incorporating token utility and metrics as described in the Good Games Guild whitepaper.
Generated: DETERMINISTIC_cafea3cc8bd6cb88
Batch ID: 20250622_211123
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
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title Good Games Guild Token ($GGG)
 * @dev ERC20 token with burn, snapshot, access control, and pausable functionality
 * Implements token utility and metrics as per Good Games Guild whitepaper
 */
contract GGGToken is ERC20, ERC20Burnable, ERC20Snapshot, AccessControl, Pausable {
    bytes32 public constant SNAPSHOT_ROLE = keccak256("SNAPSHOT_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");

    // Token metrics
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 public constant INITIAL_SUPPLY = 100_000_000 * 10**18; // 100 million initial supply

    /**
     * @dev Constructor that initializes the token
     */
    constructor() ERC20("Good Games Guild", "GGG") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(SNAPSHOT_ROLE, msg.sender);
        _setupRole(PAUSER_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);

        // Mint initial supply to deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Creates a new snapshot and returns its id
     */
    function snapshot() public onlyRole(SNAPSHOT_ROLE) returns (uint256) {
        return _snapshot();
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     */
    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }

    /**
     * @dev Mints new tokens to the specified address
     * @param to The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        require(totalSupply() + amount <= MAX_SUPPLY, "GGGToken: Cannot exceed max supply");
        _mint(to, amount);
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     * Includes when minting and burning
     * @param from The address sending tokens
     * @param to The address receiving tokens
     * @param amount The amount of tokens being transferred
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
