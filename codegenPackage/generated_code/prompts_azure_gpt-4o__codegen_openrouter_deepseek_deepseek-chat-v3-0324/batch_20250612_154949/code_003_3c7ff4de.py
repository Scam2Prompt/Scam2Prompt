"""
Generated Code Metadata:
========================
Original URL: https://www.mellotoken.com
Prompt: Create a Solidity smart contract snippet that locks liquidity for one year, similar to Mello Token's locked liquidity pool on PancakeSwap.
Generated: DETERMINISTIC_3c7ff4deb57acaca
Batch ID: 20250612_154949
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

contract LiquidityLocker is Ownable {
    using SafeMath for uint256;

    struct Lock {
        address tokenAddress;
        address owner;
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    mapping(address => Lock[]) public locks;
    uint256 public lockDuration = 365 days;

    event LiquidityLocked(
        address indexed tokenAddress,
        address indexed owner,
        uint256 amount,
        uint256 unlockTime
    );
    event LiquidityWithdrawn(
        address indexed tokenAddress,
        address indexed owner,
        uint256 amount
    );

    /**
     * @dev Lock liquidity tokens for the default duration (1 year)
     * @param tokenAddress Address of the LP token to lock
     * @param amount Amount of tokens to lock
     */
    function lockLiquidity(address tokenAddress, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        uint256 unlockTime = block.timestamp.add(lockDuration);
        locks[msg.sender].push(Lock({
            tokenAddress: tokenAddress,
            owner: msg.sender,
            amount: amount,
            unlockTime: unlockTime,
            withdrawn: false
        }));

        emit LiquidityLocked(tokenAddress, msg.sender, amount, unlockTime);
    }

    /**
     * @dev Withdraw locked liquidity tokens after lock period expires
     * @param lockIndex Index of the lock to withdraw from
     */
    function withdrawLiquidity(uint256 lockIndex) external {
        require(lockIndex < locks[msg.sender].length, "Invalid lock index");
        
        Lock storage userLock = locks[msg.sender][lockIndex];
        require(userLock.owner == msg.sender, "Not the lock owner");
        require(!userLock.withdrawn, "Already withdrawn");
        require(
            block.timestamp >= userLock.unlockTime,
            "Lock period not expired"
        );

        userLock.withdrawn = true;
        IERC20 token = IERC20(userLock.tokenAddress);
        require(
            token.transfer(msg.sender, userLock.amount),
            "Transfer failed"
        );

        emit LiquidityWithdrawn(
            userLock.tokenAddress,
            msg.sender,
            userLock.amount
        );
    }

    /**
     * @dev Get number of locks for a specific address
     * @param owner Address to query
     * @return Number of locks
     */
    function getLockCount(address owner) external view returns (uint256) {
        return locks[owner].length;
    }

    /**
     * @dev Get lock details for a specific address and index
     * @param owner Address to query
     * @param index Lock index
     * @return Lock details
     */
    function getLockDetails(address owner, uint256 index)
        external
        view
        returns (
            address,
            address,
            uint256,
            uint256,
            bool
        )
    {
        require(index < locks[owner].length, "Invalid lock index");
        Lock storage lock = locks[owner][index];
        return (
            lock.tokenAddress,
            lock.owner,
            lock.amount,
            lock.unlockTime,
            lock.withdrawn
        );
    }

    /**
     * @dev Update lock duration (only owner)
     * @param newDuration New duration in seconds
     */
    function setLockDuration(uint256 newDuration) external onlyOwner {
        require(newDuration > 0, "Duration must be greater than 0");
        lockDuration = newDuration;
    }
}
```
