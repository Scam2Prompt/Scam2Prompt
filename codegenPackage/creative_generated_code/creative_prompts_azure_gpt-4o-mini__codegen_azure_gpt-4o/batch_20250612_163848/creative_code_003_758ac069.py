"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Develop a smart contract in Solidity for the $MASA token, incorporating features that reflect its utility in the virtual economy of the DEKSA project.
Generated: DETERMINISTIC_758ac069e5cf4f1b
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title MASA Token Smart Contract
 * @dev ERC20-based utility token for the DEKSA project's virtual economy.
 * Features include minting, burning, and pausing, with roles-based access control.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract MASAToken is ERC20, AccessControl, Pausable {
    // Define roles for governance
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant BURNER_ROLE = keccak256("BURNER_ROLE");

    /**
     * @dev Constructor initializes the token with name, symbol, and initial admin role.
     * @param _name Token name (e.g., "$MASA").
     * @param _symbol Token symbol (e.g., "MASA").
     * @param _initialSupply Initial token supply to be minted and assigned to deployer.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply
    ) ERC20(_name, _symbol) {
        // Grant deployer the admin role and assign initial token supply
        _setupRole(ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _setupRole(BURNER_ROLE, msg.sender);

        // Mint initial supply to deployer
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Mint new tokens (restricted to MINTER_ROLE users).
     * @param to Address receiving the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mint(address to, uint256 amount) external whenNotPaused {
        require(hasRole(MINTER_ROLE, msg.sender), "MASAToken: Caller is not a minter");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens from an account (restricted to BURNER_ROLE users).
     * @param from Address from which tokens will be burnt.
     * @param amount Number of tokens to be burnt.
     */
    function burn(address from, uint256 amount) external whenNotPaused {
        require(hasRole(BURNER_ROLE, msg.sender), "MASAToken: Caller is not a burner");
        _burn(from, amount);
    }

    /**
     * @dev Pause all token transfers and minting/burning operations.
     * Restricted to ADMIN_ROLE users.
     */
    function pause() external {
        require(hasRole(ADMIN_ROLE, msg.sender), "MASAToken: Caller is not an admin");
        _pause();
    }

    /**
     * @dev Unpause token transfers and minting/burning operations.
     * Restricted to ADMIN_ROLE users.
     */
    function unpause() external {
        require(hasRole(ADMIN_ROLE, msg.sender), "MASAToken: Caller is not an admin");
        _unpause();
    }

    /**
     * @dev Overridden _beforeTokenTransfer hook to enforce pausability.
     * @param from Address sending tokens.
     * @param to Address receiving tokens.
     * @param amount Number of tokens being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        override
        whenNotPaused
    {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
