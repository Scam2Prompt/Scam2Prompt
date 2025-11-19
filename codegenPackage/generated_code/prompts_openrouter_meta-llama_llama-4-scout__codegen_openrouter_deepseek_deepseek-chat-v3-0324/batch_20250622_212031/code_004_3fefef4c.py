"""
Generated Code Metadata:
========================
Original URL: https://opterisglobal.com
Prompt: "Create a blockchain solution for a crypto growth center with advanced security measures and protocols using Solidity."
Generated: DETERMINISTIC_3fefef4ce9e79c22
Batch ID: 20250622_212031
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CryptoGrowthToken
 * @dev A secure ERC20 token with advanced security features for a crypto growth center
 */
contract CryptoGrowthToken is ERC20, Ownable, Pausable, ReentrancyGuard {
    uint256 private constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 private constant INITIAL_SUPPLY = 100000000 * 10**18; // 100 million initial supply
    
    mapping(address => bool) private _whitelisted;
    mapping(address => bool) private _blacklisted;
    mapping(address => uint256) private _lockedBalances;
    mapping(address => uint256) private _lockTimestamps;
    
    event Whitelisted(address indexed account);
    event Blacklisted(address indexed account);
    event TokensLocked(address indexed account, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed account, uint256 amount);
    
    /**
     * @dev Constructor that initializes the token with initial supply
     */
    constructor() ERC20("CryptoGrowthToken", "CGT") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }
    
    /**
     * @dev Modifier to check if the address is whitelisted
     */
    modifier onlyWhitelisted() {
        require(_whitelisted[msg.sender], "CryptoGrowthToken: caller is not whitelisted");
        _;
    }
    
    /**
     * @dev Modifier to check if the address is not blacklisted
     */
    modifier notBlacklisted() {
        require(!_blacklisted[msg.sender], "CryptoGrowthToken: caller is blacklisted");
        _;
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
     * @dev Add an address to the whitelist
     * @param account The address to whitelist
     */
    function whitelist(address account) external onlyOwner {
        require(!_whitelisted[account], "CryptoGrowthToken: account already whitelisted");
        _whitelisted[account] = true;
        emit Whitelisted(account);
    }
    
    /**
     * @dev Remove an address from the whitelist
     * @param account The address to remove from whitelist
     */
    function removeFromWhitelist(address account) external onlyOwner {
        require(_whitelisted[account], "CryptoGrowthToken: account not whitelisted");
        _whitelisted[account] = false;
        emit Blacklisted(account);
    }
    
    /**
     * @dev Add an address to the blacklist
     * @param account The address to blacklist
     */
    function blacklist(address account) external onlyOwner {
        require(!_blacklisted[account], "CryptoGrowthToken: account already blacklisted");
        _blacklisted[account] = true;
        emit Blacklisted(account);
    }
    
    /**
     * @dev Remove an address from the blacklist
     * @param account The address to remove from blacklist
     */
    function removeFromBlacklist(address account) external onlyOwner {
        require(_blacklisted[account], "CryptoGrowthToken: account not blacklisted");
        _blacklisted[account] = false;
        emit Whitelisted(account);
    }
    
    /**
     * @dev Lock tokens for a specific duration
     * @param account The address to lock tokens for
     * @param amount The amount of tokens to lock
     * @param duration The duration in seconds to lock tokens
     */
    function lockTokens(address account, uint256 amount, uint256 duration) external onlyOwner {
        require(balanceOf(account) >= amount, "CryptoGrowthToken: insufficient balance");
        require(_lockedBalances[account] == 0, "CryptoGrowthToken: tokens already locked");
        
        _lockedBalances[account] = amount;
        _lockTimestamps[account] = block.timestamp + duration;
        
        emit TokensLocked(account, amount, _lockTimestamps[account]);
    }
    
    /**
     * @dev Unlock tokens if lock period has expired
     * @param account The address to unlock tokens for
     */
    function unlockTokens(address account) external nonReentrant {
        require(_lockedBalances[account] > 0, "CryptoGrowthToken: no locked tokens");
        require(block.timestamp >= _lockTimestamps[account], "CryptoGrowthToken: lock period not expired");
        
        uint256 amount = _lockedBalances[account];
        _lockedBalances[account] = 0;
        _lockTimestamps[account] = 0;
        
        emit TokensUnlocked(account, amount);
    }
    
    /**
     * @dev Mint new tokens (only owner can mint up to MAX_SUPPLY)
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "CryptoGrowthToken: exceeds max supply");
        _mint(account, amount);
    }
    
    /**
     * @dev Override transfer function with security checks
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override whenNotPaused notBlacklisted {
        require(!_blacklisted[sender] && !_blacklisted[recipient], "CryptoGrowthToken: blacklisted address");
        
        if (_lockedBalances[sender] > 0) {
            require(balanceOf(sender) - _lockedBalances[sender] >= amount, "CryptoGrowthToken: transfer exceeds unlocked balance");
        }
        
        super._transfer(sender, recipient, amount);
    }
    
    /**
     * @dev Get locked balance of an account
     * @param account The address to check
     * @return The locked balance
     */
    function getLockedBalance(address account) external view returns (uint256) {
        return _lockedBalances[account];
    }
    
    /**
     * @dev Get unlock timestamp of an account
     * @param account The address to check
     * @return The unlock timestamp
     */
    function getUnlockTimestamp(address account) external view returns (uint256) {
        return _lockTimestamps[account];
    }
    
    /**
     * @dev Check if an address is whitelisted
     * @param account The address to check
     * @return True if whitelisted, false otherwise
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelisted[account];
    }
    
    /**
     * @dev Check if an address is blacklisted
     * @param account The address to check
     * @return True if blacklisted, false otherwise
     */
    function isBlacklisted(address account) external view returns (bool) {
        return _blacklisted[account];
    }
}
```
