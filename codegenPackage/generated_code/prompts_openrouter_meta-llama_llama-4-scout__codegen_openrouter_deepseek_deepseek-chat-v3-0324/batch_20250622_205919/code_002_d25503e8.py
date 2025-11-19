"""
Generated Code Metadata:
========================
Original URL: https://popofrog-6s6.pages.dev
Prompt: Develop a simple smart contract in Solidity for a multichain token like $FROP, ensuring transparency and security.
Generated: DETERMINISTIC_d25503e8db528989
Batch ID: 20250622_205919
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
 * @dev ERC20 token with multichain support, pausable functionality, and ownership
 */
contract MultichainToken is ERC20, Ownable, Pausable {
    uint256 private _maxSupply;
    mapping(address => bool) private _bridgeContracts;

    event BridgeContractAdded(address indexed bridge);
    event BridgeContractRemoved(address indexed bridge);

    /**
     * @dev Constructor that initializes the token
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param maxSupply_ Maximum token supply
     * @param initialSupply Initial token supply to mint
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        uint256 initialSupply
    ) ERC20(name_, symbol_) {
        require(initialSupply <= maxSupply_, "Initial supply exceeds max supply");
        _maxSupply = maxSupply_;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Returns the maximum token supply
     */
    function maxSupply() public view returns (uint256) {
        return _maxSupply;
    }

    /**
     * @dev Mints new tokens, can only be called by owner
     * @param to Address to mint to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= _maxSupply, "Minting would exceed max supply");
        _mint(to, amount);
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
     * @dev Adds a bridge contract address
     * @param bridge Address of the bridge contract
     */
    function addBridgeContract(address bridge) public onlyOwner {
        require(bridge != address(0), "Invalid bridge address");
        _bridgeContracts[bridge] = true;
        emit BridgeContractAdded(bridge);
    }

    /**
     * @dev Removes a bridge contract address
     * @param bridge Address of the bridge contract
     */
    function removeBridgeContract(address bridge) public onlyOwner {
        require(_bridgeContracts[bridge], "Bridge not found");
        _bridgeContracts[bridge] = false;
        emit BridgeContractRemoved(bridge);
    }

    /**
     * @dev Checks if an address is a bridge contract
     * @param bridge Address to check
     */
    function isBridgeContract(address bridge) public view returns (bool) {
        return _bridgeContracts[bridge];
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

    /**
     * @dev Burns tokens from the caller's account
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burns tokens from a specified account (only by bridge contracts)
     * @param account Account to burn from
     * @param amount Amount to burn
     */
    function bridgeBurn(address account, uint256 amount) public {
        require(_bridgeContracts[msg.sender], "Caller is not a bridge");
        _burn(account, amount);
    }

    /**
     * @dev Mints tokens to a specified account (only by bridge contracts)
     * @param account Account to mint to
     * @param amount Amount to mint
     */
    function bridgeMint(address account, uint256 amount) public {
        require(_bridgeContracts[msg.sender], "Caller is not a bridge");
        require(totalSupply() + amount <= _maxSupply, "Minting would exceed max supply");
        _mint(account, amount);
    }
}
```
