"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mauvworld.pages.dev
Prompt: Generate a smart contract in Solidity that implements a token distribution schedule similar to MAUW's, including locked periods for marketing, staking, and competitions.
Generated: DETERMINISTIC_d252dfef44f9e936
Batch ID: 20250612_150919
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Token contract implementing a distribution schedule with locked periods
contract ScheduledToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Define struct for each locked period
    struct Lock {
        uint256 amount;    // Amount locked
        uint256 unlockTime; // Timestamp when the lock will be released
        bool isLocked;      // Status of the lock
    }

    // Mapping of addresses to their respective locked balances
    mapping(address => Lock) public locks;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 unlockTime);
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed beneficiary, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1,000,000 tokens
    }

    // Function to lock tokens with a specified unlock time
    function lockTokens(uint256 amount, uint256 duration) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to lock");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp.add(duration);

        // Lock tokens
        locks[msg.sender] = Lock(amount, unlockTime, true);

        // Transfer tokens to the contract (locked tokens)
        _transfer(msg.sender, address(this), amount);

        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];
        
        require(userLock.isLocked, "No locked tokens for this address");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Unlock tokens and reset lock
        uint256 amount = userLock.amount;
        userLock.isLocked = false;
        userLock.amount = 0;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit TokensUnlocked(msg.sender, amount);
    }

    // Function to check locked status
    function isLocked(address beneficiary) external view returns (bool) {
        return locks[beneficiary].isLocked;
    }

    // Function to check the unlock time
    function getUnlockTime(address beneficiary) external view returns (uint256) {
        return locks[beneficiary].unlockTime;
    }

    // Override transfer function to prevent transfers of locked tokens
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        require(!locks[from].isLocked, "Locked tokens cannot be transferred");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
