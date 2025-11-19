"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Create a smart contract to enforce lengthy lock-up periods for liquidity providers, incorporating incentives for long-term ecosystem participation.
Generated: DETERMINISTIC_79f121062213b4ec
Batch ID: 20250612_155028
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityProviderLockup
 * @author [Your Name]
 * @notice A smart contract to enforce lengthy lock-up periods for liquidity providers,
 *         incorporating incentives for long-term ecosystem participation.
 */
contract LiquidityProviderLockup is Ownable {
    using SafeMath for uint256;

    // Mapping of liquidity provider addresses to their lock-up information
    mapping(address => LockupInfo) public lockupInfo;

    // Mapping of incentive rewards for different lock-up periods
    mapping(uint256 => uint256) public incentiveRewards;

    // ERC20 token used for liquidity provision
    IERC20 public token;

    // Minimum and maximum lock-up periods
    uint256 public minLockupPeriod;
    uint256 public maxLockupPeriod;

    // Event emitted when a liquidity provider locks up tokens
    event LockupStarted(address indexed provider, uint256 amount, uint256 lockupPeriod);

    // Event emitted when a liquidity provider unlocks tokens
    event LockupEnded(address indexed provider, uint256 amount);

    // Event emitted when incentive rewards are distributed
    event IncentivesDistributed(address indexed provider, uint256 reward);

    /**
     * @param _token Address of the ERC20 token used for liquidity provision
     * @param _minLockupPeriod Minimum lock-up period in seconds
     * @param _maxLockupPeriod Maximum lock-up period in seconds
     */
    constructor(
        address _token,
        uint256 _minLockupPeriod,
        uint256 _maxLockupPeriod
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_minLockupPeriod > 0, "Minimum lock-up period must be greater than zero");
        require(_maxLockupPeriod >= _minLockupPeriod, "Maximum lock-up period must be greater than or equal to minimum lock-up period");

        token = IERC20(_token);
        minLockupPeriod = _minLockupPeriod;
        maxLockupPeriod = _maxLockupPeriod;
    }

    /**
     * @dev Sets the incentive rewards for different lock-up periods
     * @param _lockupPeriods Array of lock-up periods
     * @param _rewards Array of incentive rewards corresponding to the lock-up periods
     */
    function setIncentiveRewards(uint256[] memory _lockupPeriods, uint256[] memory _rewards) public onlyOwner {
        require(_lockupPeriods.length == _rewards.length, "Lock-up periods and rewards arrays must have the same length");

        for (uint256 i = 0; i < _lockupPeriods.length; i++) {
            incentiveRewards[_lockupPeriods[i]] = _rewards[i];
        }
    }

    /**
     * @dev Locks up tokens for a specified period
     * @param _amount Amount of tokens to lock up
     * @param _lockupPeriod Lock-up period in seconds
     */
    function lockup(uint256 _amount, uint256 _lockupPeriod) public {
        require(_amount > 0, "Lock-up amount must be greater than zero");
        require(_lockupPeriod >= minLockupPeriod && _lockupPeriod <= maxLockupPeriod, "Lock-up period must be within the allowed range");

        // Check if the liquidity provider has sufficient tokens
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient tokens");

        // Transfer tokens to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update lock-up information
        LockupInfo storage info = lockupInfo[msg.sender];
        info.amount = info.amount.add(_amount);
        info.lockupPeriod = _lockupPeriod;
        info.unlockTime = block.timestamp.add(_lockupPeriod);

        emit LockupStarted(msg.sender, _amount, _lockupPeriod);
    }

    /**
     * @dev Unlocks tokens after the lock-up period has expired
     */
    function unlock() public {
        LockupInfo storage info = lockupInfo[msg.sender];
        require(info.amount > 0, "No locked-up tokens");
        require(block.timestamp >= info.unlockTime, "Lock-up period has not expired");

        // Transfer tokens back to the liquidity provider
        require(token.transfer(msg.sender, info.amount), "Token transfer failed");

        // Reset lock-up information
        info.amount = 0;
        info.lockupPeriod = 0;
        info.unlockTime = 0;

        emit LockupEnded(msg.sender, info.amount);

        // Distribute incentive rewards
        uint256 reward = incentiveRewards[info.lockupPeriod];
        if (reward > 0) {
            require(token.transfer(msg.sender, reward), "Incentive reward transfer failed");
            emit IncentivesDistributed(msg.sender, reward);
        }
    }

    // Struct to store lock-up information
    struct LockupInfo {
        uint256 amount;
        uint256 lockupPeriod;
        uint256 unlockTime;
    }
}
```
