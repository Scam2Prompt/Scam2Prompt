"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growbit.tech
Prompt: Write a smart contract in Solidity for a token similar to GrowBTC, ensuring it includes features like capped supply, token locking for a specified duration, and interoperability with other blockchains.
Generated: DETERMINISTIC_8bed6f59cdc5cb5f
Batch ID: 20250612_154452
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract for ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a capped supply ERC20 token with locking features
contract GrowBTCToken is ERC20, Ownable, Pausable, ERC20Burnable {
    using SafeMath for uint256;

    // Maximum supply of tokens
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10 ** decimals();

    // Struct to hold lock information
    struct Lock {
        uint256 amount;       // Amount of tokens locked
        uint256 unlockTime;   // Timestamp when tokens can be unlocked
    }

    // Mapping of addresses to their locked tokens
    mapping(address => Lock) private _locks;

    // Events for logging
    event TokensLocked(address indexed account, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed account, uint256 amount);

    // Constructor to initialize token details and mint initial supply to owner
    constructor() ERC20("GrowBTC Token", "GBTC") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    // Function to lock tokens for a specified duration
    function lockTokens(uint256 amount, uint256 duration) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(_locks[msg.sender].amount == 0, "Existing lock exists");
        
        // Calculate unlock time
        uint256 unlockTime = block.timestamp + duration;

        // Transfer tokens to the contract for locking
        _transfer(msg.sender, address(this), amount);
        
        // Set lock information
        _locks[msg.sender] = Lock(amount, unlockTime);
        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    // Function to unlock tokens after the lock duration
    function unlockTokens() external whenNotPaused {
        Lock storage lock = _locks[msg.sender];

        require(lock.amount > 0, "No tokens locked");
        require(block.timestamp >= lock.unlockTime, "Tokens are still locked");

        // Transfer the locked tokens back to the user
        _transfer(address(this), msg.sender, lock.amount);
        emit TokensUnlocked(msg.sender, lock.amount);

        // Reset the lock information
        delete _locks[msg.sender];
    }

    // Function to check the locked tokens of a user
    function lockedTokens(address account) external view returns (uint256 amount, uint256 unlockTime) {
        Lock storage lock = _locks[account];
        return (lock.amount, lock.unlockTime);
    }

    // Owner can pause the contract in case of emergency
    function pause() external onlyOwner {
        _pause();
    }

    // Owner can unpause the contract
    function unpause() external onlyOwner {
        _unpause();
    }

    // Override transfer functions to implement locking logic
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(from == address(0) || _locks[from].amount == 0, "Tokens are locked");
    }
}
```
