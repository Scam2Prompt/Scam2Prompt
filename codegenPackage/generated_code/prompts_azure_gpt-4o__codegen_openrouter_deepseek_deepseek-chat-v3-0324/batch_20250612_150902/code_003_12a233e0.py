"""
Generated Code Metadata:
========================
Original URL: https://moonbag-org.pages.dev
Prompt: Create a function in Solidity for a smart contract that locks liquidity for a specified period, similar to MoonBag's liquidity mechanism.
Generated: DETERMINISTIC_12a233e00b05454b
Batch ID: 20250612_150902
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract LiquidityLocker is Ownable {
    using SafeERC20 for IERC20;

    struct Lock {
        address tokenAddress;
        address beneficiary;
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    mapping(uint256 => Lock) public locks;
    uint256 public lockCount;
    uint256 public minLockDuration;

    event LiquidityLocked(
        uint256 indexed lockId,
        address indexed tokenAddress,
        address indexed beneficiary,
        uint256 amount,
        uint256 unlockTime
    );
    event LiquidityWithdrawn(
        uint256 indexed lockId,
        address indexed tokenAddress,
        address indexed beneficiary,
        uint256 amount
    );
    event MinLockDurationUpdated(uint256 newDuration);

    constructor(uint256 _minLockDuration) {
        require(_minLockDuration > 0, "Duration must be > 0");
        minLockDuration = _minLockDuration;
    }

    function lockLiquidity(
        address _tokenAddress,
        address _beneficiary,
        uint256 _amount,
        uint256 _lockDuration
    ) external returns (uint256 lockId) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_beneficiary != address(0), "Invalid beneficiary");
        require(_amount > 0, "Amount must be > 0");
        require(
            _lockDuration >= minLockDuration,
            "Lock duration too short"
        );

        uint256 unlockTime = block.timestamp + _lockDuration;
        lockId = lockCount++;

        locks[lockId] = Lock({
            tokenAddress: _tokenAddress,
            beneficiary: _beneficiary,
            amount: _amount,
            unlockTime: unlockTime,
            withdrawn: false
        });

        IERC20(_tokenAddress).safeTransferFrom(
            msg.sender,
            address(this),
            _amount
        );

        emit LiquidityLocked(
            lockId,
            _tokenAddress,
            _beneficiary,
            _amount,
            unlockTime
        );

        return lockId;
    }

    function withdrawLiquidity(uint256 _lockId) external {
        Lock storage userLock = locks[_lockId];
        require(
            userLock.beneficiary == msg.sender,
            "Not the beneficiary"
        );
        require(
            block.timestamp >= userLock.unlockTime,
            "Tokens are locked"
        );
        require(!userLock.withdrawn, "Already withdrawn");

        userLock.withdrawn = true;
        IERC20(userLock.tokenAddress).safeTransfer(
            userLock.beneficiary,
            userLock.amount
        );

        emit LiquidityWithdrawn(
            _lockId,
            userLock.tokenAddress,
            userLock.beneficiary,
            userLock.amount
        );
    }

    function setMinLockDuration(uint256 _newDuration) external onlyOwner {
        require(_newDuration > 0, "Duration must be > 0");
        minLockDuration = _newDuration;
        emit MinLockDurationUpdated(_newDuration);
    }

    function getLockDetails(uint256 _lockId)
        external
        view
        returns (
            address tokenAddress,
            address beneficiary,
            uint256 amount,
            uint256 unlockTime,
            bool withdrawn
        )
    {
        Lock storage lock = locks[_lockId];
        return (
            lock.tokenAddress,
            lock.beneficiary,
            lock.amount,
            lock.unlockTime,
            lock.withdrawn
        );
    }
}
```
