"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Generate an example of a smart contract that manages lengthy lock-ups for liquidity providers, inspired by the Shadow Exchange's approach to discourage premature exits.
Generated: DETERMINISTIC_6e6e5cd807934350
Batch ID: 20250612_162335
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
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title LiquidityLockupContract
 * @author [Your Name]
 * @notice A smart contract to manage lengthy lock-ups for liquidity providers.
 */
contract LiquidityLockupContract is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of liquidity provider addresses to their lock-up information
    mapping(address => LockupInfo) public lockupInfo;

    // Mapping of token addresses to their respective lock-up periods
    mapping(address => uint256) public lockupPeriods;

    // Mapping of token addresses to their respective reward rates
    mapping(address => uint256) public rewardRates;

    // Event emitted when a liquidity provider locks up tokens
    event LockupStarted(address indexed provider, address indexed token, uint256 amount, uint256 lockupEnd);

    // Event emitted when a liquidity provider exits a lock-up
    event LockupExited(address indexed provider, address indexed token, uint256 amount, uint256 rewards);

    // Struct to store lock-up information for a liquidity provider
    struct LockupInfo {
        uint256 lockupEnd;
        uint256 amount;
        bool exited;
    }

    /**
     * @notice Initializes the contract.
     */
    constructor() public {}

    /**
     * @notice Sets the lock-up period for a token.
     * @param token The address of the token.
     * @param period The lock-up period in seconds.
     */
    function setLockupPeriod(address token, uint256 period) public onlyOwner {
        require(period > 0, "Lock-up period must be greater than 0");
        lockupPeriods[token] = period;
    }

    /**
     * @notice Sets the reward rate for a token.
     * @param token The address of the token.
     * @param rate The reward rate per second.
     */
    function setRewardRate(address token, uint256 rate) public onlyOwner {
        require(rate > 0, "Reward rate must be greater than 0");
        rewardRates[token] = rate;
    }

    /**
     * @notice Locks up tokens for a liquidity provider.
     * @param token The address of the token to lock up.
     * @param amount The amount of tokens to lock up.
     */
    function lockup(address token, uint256 amount) public whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(lockupPeriods[token] > 0, "Lock-up period not set for token");

        IERC20(token).transferFrom(msg.sender, address(this), amount);

        uint256 lockupEnd = block.timestamp.add(lockupPeriods[token]);
        lockupInfo[msg.sender] = LockupInfo(lockupEnd, amount, false);

        emit LockupStarted(msg.sender, token, amount, lockupEnd);
    }

    /**
     * @notice Exits a lock-up for a liquidity provider.
     * @param token The address of the token to exit.
     */
    function exit(address token) public whenNotPaused {
        LockupInfo storage info = lockupInfo[msg.sender];
        require(info.lockupEnd > 0, "No lock-up found for provider");
        require(info.lockupEnd <= block.timestamp, "Lock-up period not ended");
        require(!info.exited, "Lock-up already exited");

        uint256 rewards = calculateRewards(token, info.amount, info.lockupEnd);
        IERC20(token).transfer(msg.sender, info.amount.add(rewards));

        info.exited = true;

        emit LockupExited(msg.sender, token, info.amount, rewards);
    }

    /**
     * @notice Calculates the rewards for a lock-up.
     * @param token The address of the token.
     * @param amount The amount of tokens locked up.
     * @param lockupEnd The end of the lock-up period.
     * @return The rewards.
     */
    function calculateRewards(address token, uint256 amount, uint256 lockupEnd) internal view returns (uint256) {
        uint256 duration = lockupEnd.sub(block.timestamp);
        return duration.mul(rewardRates[token]).mul(amount);
    }

    /**
     * @notice Pauses the contract.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @notice Unpauses the contract.
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
```
