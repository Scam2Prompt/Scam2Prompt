"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinumult.pages.dev
Prompt: Develop a decentralized application (DApp) that allows users to lock $AI tokens for a specified term and receive soulbound receipt tokens. Include features for calculating multipliers based on lock duration.
Generated: DETERMINISTIC_2348d0cdf042149d
Batch ID: 20250612_152109
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
 * @title TokenLockDApp
 * @dev A decentralized application that allows users to lock $AI tokens for specified terms
 *      and receive soulbound receipt tokens. Multipliers are calculated based on lock duration.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract SoulboundToken {
    string public name = "Soulbound Receipt Token";
    string public symbol = "SBT";
    uint8 public decimals = 18;

    mapping(address => uint256) public balances;
    mapping(address => bool) public isSoulbound;

    event Mint(address indexed to, uint256 amount);

    /**
     * @dev Mint soulbound tokens for the given address.
     * @param to Address to mint tokens for.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external {
        require(to != address(0), "Invalid address");
        require(!isSoulbound[to], "Address already has soulbound tokens");

        balances[to] += amount;
        isSoulbound[to] = true;

        emit Mint(to, amount);
    }
}

contract TokenLockDApp {
    IERC20 public aiToken;
    SoulboundToken public soulboundToken;

    struct LockInfo {
        uint256 amount;
        uint256 unlockTime;
        uint256 multiplier;
    }

    mapping(address => LockInfo) public locks;

    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _aiToken Address of the $AI token contract.
     */
    constructor(address _aiToken) {
        aiToken = IERC20(_aiToken);
        soulboundToken = new SoulboundToken();
    }

    /**
     * @dev Function to lock $AI tokens for a specified duration.
     * @param amount Amount of tokens to lock.
     * @param lockDuration Duration (in seconds) to lock the tokens for.
     */
    function lockTokens(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Lock amount must be greater than 0");
        require(lockDuration >= 1 weeks && lockDuration <= 52 weeks, "Lock duration must be between 1 and 52 weeks");
        require(locks[msg.sender].amount == 0, "Tokens already locked");

        uint256 multiplier = calculateMultiplier(lockDuration);

        // Transfer $AI tokens from the user to the contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        locks[msg.sender] = LockInfo({
            amount: amount,
            unlockTime: block.timestamp + lockDuration,
            multiplier: multiplier
        });

        // Mint soulbound receipt tokens
        soulboundToken.mint(msg.sender, amount * multiplier);

        emit TokensLocked(msg.sender, amount, block.timestamp + lockDuration, multiplier);
    }

    /**
     * @dev Function to unlock $AI tokens after the lock period has expired.
     */
    function unlockTokens() external {
        LockInfo storage lockInfo = locks[msg.sender];
        require(lockInfo.amount > 0, "No tokens locked");
        require(block.timestamp >= lockInfo.unlockTime, "Lock period has not expired");

        uint256 amount = lockInfo.amount;
        lockInfo.amount = 0;

        // Transfer $AI tokens back to the user
        require(aiToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, amount);
    }

    /**
     * @dev Calculates the multiplier based on the lock duration.
     * @param lockDuration Duration of the lock (in seconds).
     * @return Multiplier value.
     */
    function calculateMultiplier(uint256 lockDuration) public pure returns (uint256) {
        if (lockDuration >= 52 weeks) {
            return 3; // 3x multiplier for 1 year
        } else if (lockDuration >= 26 weeks) {
            return 2; // 2x multiplier for 6 months
        } else if (lockDuration >= 12 weeks) {
            return 1.5e18; // 1.5x multiplier for 3 months
        } else {
            return 1; // No multiplier for less than 3 months
        }
    }

    /**
     * @dev Checks the current lock information for a user.
     * @param user Address of the user.
     * @return Lock information struct.
     */
    function getLockInfo(address user) external view returns (LockInfo memory) {
        return locks[user];
    }
}
```
