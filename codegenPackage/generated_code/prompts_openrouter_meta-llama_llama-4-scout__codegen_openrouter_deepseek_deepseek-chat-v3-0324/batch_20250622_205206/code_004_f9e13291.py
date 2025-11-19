"""
Generated Code Metadata:
========================
Original URL: https://claim-popofrog.pages.dev
Prompt: Generate a smart contract code for a multichain token like $FROP, utilizing different blockchains such as BNB Chain, Arbitrum, and Ethereum.
Generated: DETERMINISTIC_f9e132919f01dd6e
Batch ID: 20250622_205206
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title MultichainToken
 * @dev ERC20 token with multichain support and admin controls
 */
contract MultichainToken is ERC20, Ownable, Pausable {
    // Mapping to track bridge contracts across different chains
    mapping(address => bool) public isBridge;
    
    // Maximum supply cap
    uint256 public immutable maxSupply;
    
    // Event emitted when bridge status changes
    event BridgeStatusChanged(address indexed bridge, bool status);
    
    /**
     * @dev Constructor initializes the token with name, symbol, and max supply
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param maxSupply_ Maximum token supply
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_
    ) ERC20(name_, symbol_) {
        require(maxSupply_ > 0, "Max supply must be greater than 0");
        maxSupply = maxSupply_;
    }
    
    /**
     * @dev Mints tokens, can only be called by owner or bridge contracts
     * @param to Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external whenNotPaused {
        require(isBridge[msg.sender] || msg.sender == owner(), "Caller not authorized");
        require(totalSupply() + amount <= maxSupply, "Exceeds max supply");
        _mint(to, amount);
    }
    
    /**
     * @dev Burns tokens, can only be called by bridge contracts
     * @param from Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burn(address from, uint256 amount) external whenNotPaused {
        require(isBridge[msg.sender], "Caller not authorized");
        _burn(from, amount);
    }
    
    /**
     * @dev Updates bridge status for an address
     * @param bridge Address of the bridge contract
     * @param status New bridge status (true = enabled)
     */
    function setBridge(address bridge, bool status) external onlyOwner {
        isBridge[bridge] = status;
        emit BridgeStatusChanged(bridge, status);
    }
    
    /**
     * @dev Pauses token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpauses token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
