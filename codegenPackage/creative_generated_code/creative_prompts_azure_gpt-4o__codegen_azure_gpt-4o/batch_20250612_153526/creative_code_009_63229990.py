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

/**
 * @title TokenLock
 * @dev Smart contract for locking tokens with flexible vesting schedules.
 *      It ensures transparency and security for token holders.
 */
contract TokenLock {
    // ERC20 Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Struct to represent each token lock
    struct Lock {
        uint256 amount;          // Amount of tokens locked
        uint256 unlockTime;      // Timestamp when tokens become unlocked
        address beneficiary;     // Address that will receive unlocked tokens
        bool claimed;            // Whether the lock has been claimed
    }

    // State variables
    IERC20 public token;                // ERC20 token being locked
    address public owner;               // Owner of the contract
    uint256 public lockIdCounter = 0;   // Counter for lock IDs
    mapping(uint256 => Lock) public locks; // Mapping lock IDs to Lock structures

    // Events
    event TokenLocked(uint256 lockId, address beneficiary, uint256 amount, uint256 unlockTime);
    event TokenClaimed(uint256 lockId, address beneficiary, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validLock(uint256 lockId) {
        require(locks[lockId].amount > 0, "Invalid lock ID");
        _;
    }

    modifier notClaimed(uint256 lockId) {
        require(!locks[lockId].claimed, "Tokens already claimed");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the token address.
     * @param _token Address of the ERC20 token to lock.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new token lock.
     * @param _beneficiary Address that will receive the tokens after unlock.
     * @param _amount Amount of tokens to lock.
     * @param _unlockTime Timestamp when tokens will become unlocked.
     */
    function lockTokens(address _beneficiary, uint256 _amount, uint256 _unlockTime) external onlyOwner {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_amount > 0, "Amount must be greater than zero");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");

        // Transfer tokens from sender to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Create a new lock
        locks[lockIdCounter] = Lock({
            amount: _amount,
            unlockTime: _unlockTime,
            beneficiary: _beneficiary,
            claimed: false
        });

        emit TokenLocked(lockIdCounter, _beneficiary, _amount, _unlockTime);

        // Increment lock ID counter
        lockIdCounter++;
    }

    /**
     * @dev Function to claim tokens after unlock time.
     * @param lockId ID of the lock being claimed.
     */
    function claimTokens(uint256 lockId) external validLock(lockId) notClaimed(lockId) {
        Lock storage lock = locks[lockId];
        require(msg.sender == lock.beneficiary, "Caller is not the beneficiary");
        require(block.timestamp >= lock.unlockTime, "Tokens are not yet unlocked");

        // Mark the lock as claimed
        lock.claimed = true;

        // Transfer tokens to beneficiary
        require(token.transfer(lock.beneficiary, lock.amount), "Token transfer failed");

        emit TokenClaimed(lockId, lock.beneficiary, lock.amount);
    }

    /**
     * @dev Function for the owner to withdraw any accidentally sent tokens.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        IERC20(_token).transfer(owner, _amount);
    }

    /**
     * @dev Function to fetch details of a specific lock.
     * @param lockId ID of the lock to query.
     * @return Lock details (amount, unlockTime, beneficiary, claimed)
     */
    function getLockDetails(uint256 lockId) external view validLock(lockId) returns (uint256, uint256, address, bool) {
        Lock memory lock = locks[lockId];
        return (lock.amount, lock.unlockTime, lock.beneficiary, lock.claimed);
    }
}
```
