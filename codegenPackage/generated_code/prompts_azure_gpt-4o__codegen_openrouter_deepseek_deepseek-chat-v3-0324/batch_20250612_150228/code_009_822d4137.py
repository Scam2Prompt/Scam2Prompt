"""
Generated Code Metadata:
========================
Original URL: https://token-pushdstore.pages.dev
Prompt: Write a Solidity contract to lock team tokens for 700 days and liquidity for 20 years, ensuring security and preventing rug pulls as outlined in Pushd's roadmap.
Generated: DETERMINISTIC_822d4137d7954aab
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenLocker is Ownable {
    using SafeMath for uint256;

    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    // Token to be locked
    IERC20 public immutable token;

    // Team locks
    mapping(address => Lock) public teamLocks;
    // Liquidity locks
    mapping(address => Lock) public liquidityLocks;

    // Lock durations
    uint256 public constant TEAM_LOCK_DURATION = 700 days;
    uint256 public constant LIQUIDITY_LOCK_DURATION = 20 * 365 days;

    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 unlockTime, bool isLiquidity);
    event TokensWithdrawn(address indexed beneficiary, uint256 amount);

    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Lock team tokens for 700 days
     * @param beneficiary Address that will receive tokens after lock period
     * @param amount Amount of tokens to lock
     */
    function lockTeamTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(teamLocks[beneficiary].amount == 0, "Tokens already locked for this beneficiary");

        uint256 unlockTime = block.timestamp.add(TEAM_LOCK_DURATION);
        teamLocks[beneficiary] = Lock(amount, unlockTime, false);

        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit TokensLocked(beneficiary, amount, unlockTime, false);
    }

    /**
     * @dev Lock liquidity tokens for 20 years
     * @param beneficiary Address that will receive tokens after lock period
     * @param amount Amount of tokens to lock
     */
    function lockLiquidityTokens(address beneficiary, uint256 amount) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(liquidityLocks[beneficiary].amount == 0, "Tokens already locked for this beneficiary");

        uint256 unlockTime = block.timestamp.add(LIQUIDITY_LOCK_DURATION);
        liquidityLocks[beneficiary] = Lock(amount, unlockTime, false);

        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit TokensLocked(beneficiary, amount, unlockTime, true);
    }

    /**
     * @dev Withdraw locked team tokens after lock period
     */
    function withdrawTeamTokens() external {
        Lock storage lock = teamLocks[msg.sender];
        require(lock.amount > 0, "No tokens locked");
        require(!lock.withdrawn, "Tokens already withdrawn");
        require(block.timestamp >= lock.unlockTime, "Tokens are still locked");

        uint256 amount = lock.amount;
        lock.withdrawn = true;

        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Withdraw locked liquidity tokens after lock period
     */
    function withdrawLiquidityTokens() external {
        Lock storage lock = liquidityLocks[msg.sender];
        require(lock.amount > 0, "No tokens locked");
        require(!lock.withdrawn, "Tokens already withdrawn");
        require(block.timestamp >= lock.unlockTime, "Tokens are still locked");

        uint256 amount = lock.amount;
        lock.withdrawn = true;

        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get remaining lock time for team tokens
     * @param beneficiary Address to check
     * @return Remaining lock time in seconds
     */
    function getTeamLockRemainingTime(address beneficiary) external view returns (uint256) {
        Lock memory lock = teamLocks[beneficiary];
        if (lock.unlockTime <= block.timestamp || lock.withdrawn) {
            return 0;
        }
        return lock.unlockTime.sub(block.timestamp);
    }

    /**
     * @dev Get remaining lock time for liquidity tokens
     * @param beneficiary Address to check
     * @return Remaining lock time in seconds
     */
    function getLiquidityLockRemainingTime(address beneficiary) external view returns (uint256) {
        Lock memory lock = liquidityLocks[beneficiary];
        if (lock.unlockTime <= block.timestamp || lock.withdrawn) {
            return 0;
        }
        return lock.unlockTime.sub(block.timestamp);
    }
}
```
