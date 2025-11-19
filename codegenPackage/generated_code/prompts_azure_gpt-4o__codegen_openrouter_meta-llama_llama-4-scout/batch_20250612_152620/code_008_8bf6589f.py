"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Create a smart contract in Solidity that locks liquidity for $SCOTTY tokens and ensures rewards distribution over the specified 3-year period.
Generated: DETERMINISTIC_8bf6589fe7995101
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ScottyTokenLockingContract
 * @author [Your Name]
 * @notice This contract locks liquidity for $SCOTTY tokens and distributes rewards over a 3-year period.
 */
contract ScottyTokenLockingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user addresses to their locked token balances
    mapping(address => uint256) public lockedBalances;

    // Mapping of user addresses to their reward claim timestamps
    mapping(address => uint256) public rewardClaimTimestamps;

    // Total locked tokens
    uint256 public totalLockedTokens;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Reward distribution period in seconds (3 years)
    uint256 public constant REWARD_PERIOD = 3 * 365 * 24 * 60 * 60;

    // Reward distribution start timestamp
    uint256 public rewardStartTimestamp;

    // $SCOTTY token contract
    ERC20 public scottyToken;

    /**
     * @notice Constructor
     * @param _scottyTokenAddress Address of the $SCOTTY token contract
     * @param _totalRewards Total rewards available for distribution
     */
    constructor(address _scottyTokenAddress, uint256 _totalRewards) {
        require(_scottyTokenAddress != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than 0");

        scottyToken = ERC20(_scottyTokenAddress);
        totalRewards = _totalRewards;
        rewardStartTimestamp = block.timestamp;
    }

    /**
     * @notice Locks tokens for a user
     * @param _amount Amount of tokens to lock
     */
    function lockTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(scottyToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        scottyToken.transferFrom(msg.sender, address(this), _amount);

        // Update locked balance and total locked tokens
        lockedBalances[msg.sender] = lockedBalances[msg.sender].add(_amount);
        totalLockedTokens = totalLockedTokens.add(_amount);
    }

    /**
     * @notice Claims rewards for a user
     */
    function claimRewards() external nonReentrant {
        uint256 _claimableRewards = calculateClaimableRewards(msg.sender);
        require(_claimableRewards > 0, "No claimable rewards");

        // Update reward claim timestamp
        rewardClaimTimestamps[msg.sender] = block.timestamp;

        // Transfer rewards to user
        scottyToken.transfer(msg.sender, _claimableRewards);
    }

    /**
     * @notice Calculates claimable rewards for a user
     * @param _user User address
     * @return Claimable rewards
     */
    function calculateClaimableRewards(address _user) public view returns (uint256) {
        uint256 _lockedBalance = lockedBalances[_user];
        uint256 _timestampDiff = block.timestamp.sub(rewardClaimTimestamps[_user]);

        // Calculate claimable rewards based on locked balance and time elapsed
        uint256 _claimableRewards = _lockedBalance.mul(_timestampDiff).mul(totalRewards).div(REWARD_PERIOD).div(totalLockedTokens);

        return _claimableRewards;
    }

    /**
     * @notice Calculates user rewards at any given timestamp
     * @param _user User address
     * @param _timestamp Timestamp
     * @return Rewards at the given timestamp
     */
    function getRewardsAtTimestamp(address _user, uint256 _timestamp) external view returns (uint256) {
        uint256 _lockedBalance = lockedBalances[_user];
        uint256 _timestampDiff = _timestamp.sub(rewardStartTimestamp);

        // Calculate rewards based on locked balance and time elapsed
        uint256 _rewards = _lockedBalance.mul(_timestampDiff).mul(totalRewards).div(REWARD_PERIOD).div(totalLockedTokens);

        return _rewards;
    }
}
```
