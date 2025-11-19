"""
Generated Code Metadata:
========================
Original URL: https://burncat-buy.pages.dev
Prompt: Create a Solidity smart contract that locks liquidity and burns tokens forever, similar to the liquidity lock mechanism described for Burn Cat's $BCAT.
Generated: DETERMINISTIC_e797e09c5d5002a5
Batch ID: 20250612_150552
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

contract LiquidityLocker is Ownable {
    struct Lock {
        address tokenAddress;
        address owner;
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    mapping(uint256 => Lock) public locks;
    uint256 public lockCount;
    uint256 public minLockTime;

    event TokensLocked(
        uint256 lockId,
        address tokenAddress,
        address owner,
        uint256 amount,
        uint256 unlockTime
    );
    event TokensWithdrawn(uint256 lockId, address tokenAddress, address owner, uint256 amount);
    event TokensBurned(uint256 lockId, address tokenAddress, uint256 amount);

    constructor(uint256 _minLockTime) {
        minLockTime = _minLockTime;
    }

    function lockTokens(
        address _tokenAddress,
        uint256 _amount,
        uint256 _lockTime
    ) external {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");
        require(
            _lockTime >= minLockTime,
            "Lock time must be greater than or equal to minimum lock time"
        );

        IERC20 token = IERC20(_tokenAddress);
        require(
            token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        uint256 unlockTime = block.timestamp + _lockTime;
        uint256 lockId = lockCount++;

        locks[lockId] = Lock({
            tokenAddress: _tokenAddress,
            owner: msg.sender,
            amount: _amount,
            unlockTime: unlockTime,
            withdrawn: false
        });

        emit TokensLocked(lockId, _tokenAddress, msg.sender, _amount, unlockTime);
    }

    function withdrawTokens(uint256 _lockId) external {
        Lock storage lock = locks[_lockId];
        require(lock.owner == msg.sender, "Not the owner of these tokens");
        require(block.timestamp >= lock.unlockTime, "Tokens are still locked");
        require(!lock.withdrawn, "Tokens already withdrawn");

        lock.withdrawn = true;
        IERC20 token = IERC20(lock.tokenAddress);
        require(
            token.transfer(msg.sender, lock.amount),
            "Token transfer failed"
        );

        emit TokensWithdrawn(_lockId, lock.tokenAddress, msg.sender, lock.amount);
    }

    function burnTokens(uint256 _lockId) external onlyOwner {
        Lock storage lock = locks[_lockId];
        require(!lock.withdrawn, "Tokens already withdrawn");

        lock.withdrawn = true;
        IERC20 token = IERC20(lock.tokenAddress);
        require(
            token.transfer(address(0), lock.amount),
            "Token burn failed"
        );

        emit TokensBurned(_lockId, lock.tokenAddress, lock.amount);
    }

    function setMinLockTime(uint256 _minLockTime) external onlyOwner {
        minLockTime = _minLockTime;
    }
}
```
