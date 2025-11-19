"""
Generated Code Metadata:
========================
Original URL: https://bafybeie3l7e667ujuarffoatjdcaaydxgnjde2rbbwwt6zmewgsgowh4sm.ipfs.dweb.link
Prompt: "Develop a smart contract for managing $BasedAI token transactions on a blockchain platform."
Generated: DETERMINISTIC_9fb3d26f419751e4
Batch ID: 20250622_205111
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
 * @title BasedAI Token Contract
 * @dev ERC20 token with minting, burning, pausable, and ownership features
 */
contract BasedAIToken is ERC20, Ownable, Pausable {
    uint256 private constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    
    // Mapping to track blacklisted addresses
    mapping(address => bool) private _blacklisted;

    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);
    event Blacklisted(address indexed account);
    event Unblacklisted(address indexed account);

    /**
     * @dev Constructor that initializes the token with initial supply
     */
    constructor() ERC20("BasedAI", "BASEDAI") {
        _mint(msg.sender, MAX_SUPPLY / 2); // Mint initial 50% of total supply
    }

    /**
     * @dev Mint new tokens (only owner)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "BasedAIToken: Exceeds max supply");
        _mint(to, amount);
        emit Mint(to, amount);
    }

    /**
     * @dev Burn tokens from caller's balance
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Add address to blacklist
     * @param account Address to blacklist
     */
    function blacklist(address account) external onlyOwner {
        _blacklisted[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @dev Remove address from blacklist
     * @param account Address to remove from blacklist
     */
    function unblacklist(address account) external onlyOwner {
        _blacklisted[account] = false;
        emit Unblacklisted(account);
    }

    /**
     * @dev Check if address is blacklisted
     * @param account Address to check
     * @return bool True if address is blacklisted
     */
    function isBlacklisted(address account) external view returns (bool) {
        return _blacklisted[account];
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        require(!paused(), "BasedAIToken: Token transfer while paused");
        require(!_blacklisted[from], "BasedAIToken: Sender is blacklisted");
        require(!_blacklisted[to], "BasedAIToken: Recipient is blacklisted");
    }
}
```
