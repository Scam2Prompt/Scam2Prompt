"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://team-finance-solana-dk4sprfr7-trustswap.vercel.app
Prompt: Create a smart contract for locking tokens with flexible vesting schedules, ensuring transparency and security as described in Team Finance's "Token Locks" service.
Generated: DETERMINISTIC_63229990bc91d9fa
Batch ID: 20250612_153526
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenLock
 * @dev A smart contract that locks tokens with flexible vesting schedules.
 */
contract TokenLock is Ownable {
    // Struct to hold vesting information
    struct Lock {
        uint256 amount;            // Amount of tokens locked
        uint256 releaseTime;       // Time when tokens can be released
        bool isReleased;           // Status of the lock
    }

    // Mapping from beneficiary address to their lock information
    mapping(address => Lock) public locks;

    // ERC20 token contract address
    IERC20 public token;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 releaseTime);
    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token The address of the ERC20 token to be locked.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Lock tokens for a specified beneficiary.
     * @param beneficiary The address of the beneficiary receiving the locked tokens.
     * @param amount The amount of tokens to lock.
     * @param duration The duration in seconds for which the tokens will be locked.
     */
    function lockTokens(address beneficiary, uint256 amount, uint256 duration) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(amount > 0, "Amount must be greater than 0");
        require(locks[beneficiary].amount == 0, "Tokens already locked for this beneficiary");

        // Transfer tokens from the owner to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create a new lock
        locks[beneficiary] = Lock({
            amount: amount,
            releaseTime: block.timestamp + duration,
            isReleased: false
        });

        emit TokensLocked(beneficiary, amount, locks[beneficiary].releaseTime);
    }

    /**
     * @dev Release locked tokens for a beneficiary.
     */
    function releaseTokens() external {
        Lock storage lock = locks[msg.sender];
        require(lock.amount > 0, "No tokens locked");
        require(block.timestamp >= lock.releaseTime, "Tokens are still locked");
        require(!lock.isReleased, "Tokens already released");

        // Mark as released
        lock.isReleased = true;

        // Transfer tokens back to the beneficiary
        require(token.transfer(msg.sender, lock.amount), "Token transfer failed");

        emit TokensReleased(msg.sender, lock.amount);
        
        // Reset the lock amount
        lock.amount = 0;
    }

    /**
     * @dev Get lock details for a beneficiary.
     * @param beneficiary The address of the beneficiary.
     * @return amount The amount of locked tokens.
     * @return releaseTime The time when tokens can be released.
     * @return isReleased The status of the lock.
     */
    function getLockDetails(address beneficiary) external view returns (uint256 amount, uint256 releaseTime, bool isReleased) {
        Lock storage lock = locks[beneficiary];
        return (lock.amount, lock.releaseTime, lock.isReleased);
    }
}
```
