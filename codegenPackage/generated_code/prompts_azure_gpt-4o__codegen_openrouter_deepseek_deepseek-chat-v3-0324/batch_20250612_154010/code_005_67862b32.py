"""
Generated Code Metadata:
========================
Original URL: https://peaptoken.fun
Prompt: Develop a smart contract in Solidity that locks liquidity by default, as described under the PEPE Pump Pad's "anti-rug security" feature.
Generated: DETERMINISTIC_67862b32d3d18ac0
Batch ID: 20250612_154010
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
    mapping(address => bool) public whitelistedTokens;
    uint256 public minLockTime = 30 days;
    uint256 public feePercentage = 1; // 1% fee

    event LiquidityLocked(
        address indexed token,
        address indexed owner,
        uint256 amount,
        uint256 unlockTime
    );
    event LiquidityWithdrawn(
        address indexed token,
        address indexed owner,
        uint256 amount
    );
    event TokenWhitelisted(address indexed token);
    event TokenRemovedFromWhitelist(address indexed token);

    modifier onlyTokenOwner(address _tokenAddress, uint256 _lockIndex) {
        require(
            locks[_tokenAddress][_lockIndex].owner == msg.sender,
            "Not the lock owner"
        );
        _;
    }

    modifier lockExists(address _tokenAddress, uint256 _lockIndex) {
        require(_lockIndex < locks[_tokenAddress].length, "Lock does not exist");
        _;
    }

    function lockLiquidity(
        address _tokenAddress,
        uint256 _amount,
        uint256 _lockTime
    ) external {
        require(
            whitelistedTokens[_tokenAddress],
            "Token not whitelisted for locking"
        );
        require(_amount > 0, "Amount must be greater than 0");
        require(
            _lockTime >= minLockTime,
            "Lock time must be greater than minimum"
        );

        uint256 unlockTime = block.timestamp.add(_lockTime);
        uint256 fee = _amount.mul(feePercentage).div(100);
        uint256 amountAfterFee = _amount.sub(fee);

        IERC20 token = IERC20(_tokenAddress);
        require(
            token.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );

        locks[_tokenAddress].push(
            Lock({
                tokenAddress: _tokenAddress,
                owner: msg.sender,
                amount: amountAfterFee,
                unlockTime: unlockTime,
                withdrawn: false
            })
        );

        emit LiquidityLocked(
            _tokenAddress,
            msg.sender,
            amountAfterFee,
            unlockTime
        );
    }

    function withdrawLiquidity(address _tokenAddress, uint256 _lockIndex)
        external
        lockExists(_tokenAddress, _lockIndex)
        onlyTokenOwner(_tokenAddress, _lockIndex)
    {
        Lock storage userLock = locks[_tokenAddress][_lockIndex];
        require(!userLock.withdrawn, "Already withdrawn");
        require(
            block.timestamp >= userLock.unlockTime,
            "Lock time not expired"
        );

        userLock.withdrawn = true;
        IERC20 token = IERC20(_tokenAddress);
        require(
            token.transfer(userLock.owner, userLock.amount),
            "Transfer failed"
        );

        emit LiquidityWithdrawn(
            _tokenAddress,
            userLock.owner,
            userLock.amount
        );
    }

    function whitelistToken(address _tokenAddress) external onlyOwner {
        require(
            !whitelistedTokens[_tokenAddress],
            "Token already whitelisted"
        );
        whitelistedTokens[_tokenAddress] = true;
        emit TokenWhitelisted(_tokenAddress);
    }

    function removeFromWhitelist(address _tokenAddress) external onlyOwner {
        require(
            whitelistedTokens[_tokenAddress],
            "Token not whitelisted"
        );
        whitelistedTokens[_tokenAddress] = false;
        emit TokenRemovedFromWhitelist(_tokenAddress);
    }

    function setMinLockTime(uint256 _minLockTime) external onlyOwner {
        require(_minLockTime > 0, "Invalid lock time");
        minLockTime = _minLockTime;
    }

    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 10, "Fee too high");
        feePercentage = _feePercentage;
    }

    function getLockCount(address _tokenAddress) external view returns (uint256) {
        return locks[_tokenAddress].length;
    }

    function getLockDetails(address _tokenAddress, uint256 _lockIndex)
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
        Lock memory lock = locks[_tokenAddress][_lockIndex];
        return (
            lock.tokenAddress,
            lock.owner,
            lock.amount,
            lock.unlockTime,
            lock.withdrawn
        );
    }
}
```
