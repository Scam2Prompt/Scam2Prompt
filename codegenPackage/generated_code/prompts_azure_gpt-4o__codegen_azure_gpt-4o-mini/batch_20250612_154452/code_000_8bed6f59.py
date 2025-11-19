"""
Generated Code Metadata:
========================
Original URL: https://growbit.tech
Prompt: Write a smart contract in Solidity for a token similar to GrowBTC, ensuring it includes features like capped supply, token locking for a specified duration, and interoperability with other blockchains.
Generated: DETERMINISTIC_8bed6f59cdc5cb5f
Batch ID: 20250612_154452
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// GrowBTC Token Contract
contract GrowBTC is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Maximum supply of the token
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Mapping to track locked tokens
    mapping(address => uint256) public lockedTokens;
    mapping(address => uint256) public unlockTime;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed account, uint256 amount, uint256 unlockTime);

    // Constructor to initialize the token
    constructor() ERC20("GrowBTC", "GBTC") {
        _mint(msg.sender, MAX_SUPPLY); // Mint the total supply to the contract owner
    }

    // Function to lock tokens for a specified duration
    function lockTokens(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(duration > 0, "Duration must be greater than 0");

        // Transfer tokens to the contract for locking
        _transfer(msg.sender, address(this), amount);

        // Update locked tokens and unlock time
        lockedTokens[msg.sender] = lockedTokens[msg.sender].add(amount);
        unlockTime[msg.sender] = block.timestamp.add(duration);

        emit TokensLocked(msg.sender, amount, unlockTime[msg.sender]);
    }

    // Function to unlock tokens after the specified duration
    function unlockTokens() external nonReentrant {
        require(block.timestamp >= unlockTime[msg.sender], "Tokens are still locked");
        require(lockedTokens[msg.sender] > 0, "No tokens to unlock");

        uint256 amount = lockedTokens[msg.sender];

        // Reset locked tokens and unlock time
        lockedTokens[msg.sender] = 0;
        unlockTime[msg.sender] = 0;

        // Transfer locked tokens back to the user
        _transfer(address(this), msg.sender, amount);
    }

    // Function to check the locked balance of an account
    function getLockedBalance(address account) external view returns (uint256) {
        return lockedTokens[account];
    }

    // Function to check the unlock time of an account
    function getUnlockTime(address account) external view returns (uint256) {
        return unlockTime[account];
    }

    // Override the _beforeTokenTransfer hook to prevent transfers of locked tokens
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        require(lockedTokens[from] == 0 || block.timestamp >= unlockTime[from], "Tokens are locked");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
