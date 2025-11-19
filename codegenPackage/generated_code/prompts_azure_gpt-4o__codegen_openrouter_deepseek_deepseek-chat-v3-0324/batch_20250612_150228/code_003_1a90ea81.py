"""
Generated Code Metadata:
========================
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Write a smart contract in Solidity for a utility token that supports gameplay rewards and integrates with the Pixels platform's Chapter Two release.
Generated: DETERMINISTIC_1a90ea8166379456
Batch ID: 20250612_150228
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
 * @title Pixels Utility Token
 * @dev ERC20 token with minting capabilities for gameplay rewards on Pixels platform
 */
contract PixelsUtilityToken is ERC20, Ownable, Pausable {
    // Address of the Pixels game server authorized to distribute rewards
    address public gameServer;

    // Mapping to track authorized minters (other than gameServer)
    mapping(address => bool) private _minters;

    // Event emitted when new minters are added/removed
    event MinterUpdated(address indexed account, bool canMint);
    event GameServerUpdated(address indexed newGameServer);

    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply Initial token supply to mint to contract owner
     */
    constructor(uint256 initialSupply) ERC20("Pixels Utility Token", "PXT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Modifier to check if caller is authorized to mint tokens
     */
    modifier onlyMinter() {
        require(
            msg.sender == gameServer || _minters[msg.sender],
            "PXT: Caller is not authorized to mint"
        );
        _;
    }

    /**
     * @dev Mint new tokens (only callable by authorized minters)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyMinter whenNotPaused {
        _mint(to, amount);
    }

    /**
     * @dev Set the game server address (only callable by owner)
     * @param newGameServer Address of the new game server
     */
    function setGameServer(address newGameServer) external onlyOwner {
        require(newGameServer != address(0), "PXT: Invalid game server address");
        gameServer = newGameServer;
        emit GameServerUpdated(newGameServer);
    }

    /**
     * @dev Add or remove a minter (only callable by owner)
     * @param account Address of the minter
     * @param canMint Whether the account can mint tokens
     */
    function setMinter(address account, bool canMint) external onlyOwner {
        require(account != address(0), "PXT: Invalid minter address");
        _minters[account] = canMint;
        emit MinterUpdated(account, canMint);
    }

    /**
     * @dev Check if an address is authorized to mint tokens
     * @param account Address to check
     * @return bool Whether the address can mint tokens
     */
    function isMinter(address account) external view returns (bool) {
        return _minters[account] || account == gameServer;
    }

    /**
     * @dev Pause token transfers and minting (only callable by owner)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers and minting (only callable by owner)
     */
    function unpause() external onlyOwner {
        _unpause();
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
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
