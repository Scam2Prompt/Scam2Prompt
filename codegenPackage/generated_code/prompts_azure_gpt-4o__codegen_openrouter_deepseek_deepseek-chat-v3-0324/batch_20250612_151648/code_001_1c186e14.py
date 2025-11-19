"""
Generated Code Metadata:
========================
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate Solidity code for a smart contract that implements the "Stake-to-Mine" mechanism, where users stake BTCMTX tokens to earn non-transferable mining credits that can be burned for Bitcoin cloud mining power.
Generated: DETERMINISTIC_1c186e1408c93e4e
Batch ID: 20250612_151648
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakeToMine is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user's staking information
    struct UserInfo {
        uint256 amount; // Amount of BTCMTX tokens staked
        uint256 miningCredits; // Non-transferable mining credits earned
        uint256 lastUpdateTime; // Last time mining credits were updated
    }

    // BTCMTX token contract
    IERC20 public immutable btcMtxToken;

    // Mining credits per second per token staked (in wei)
    uint256 public miningRate;

    // Mapping from user address to their staking info
    mapping(address => UserInfo) public userInfo;

    // Total BTCMTX tokens staked
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event MiningCreditsClaimed(address indexed user, uint256 amount);
    event MiningPowerRedeemed(address indexed user, uint256 creditsBurned, uint256 miningPower);
    event MiningRateUpdated(uint256 newRate);

    constructor(address _btcMtxToken, uint256 _miningRate) {
        require(_btcMtxToken != address(0), "Invalid token address");
        btcMtxToken = IERC20(_btcMtxToken);
        miningRate = _miningRate;
    }

    /**
     * @dev Stake BTCMTX tokens to earn mining credits
     * @param amount Amount of BTCMTX tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        _updateMiningCredits(user);

        user.amount += amount;
        totalStaked += amount;

        btcMtxToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked BTCMTX tokens and claim mining credits
     * @param amount Amount of BTCMTX tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked balance");

        _updateMiningCredits(user);

        user.amount -= amount;
        totalStaked -= amount;

        btcMtxToken.safeTransfer(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated mining credits
     */
    function claimMiningCredits() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        _updateMiningCredits(user);

        uint256 creditsToClaim = user.miningCredits;
        require(creditsToClaim > 0, "No credits to claim");

        user.miningCredits = 0;

        emit MiningCreditsClaimed(msg.sender, creditsToClaim);
    }

    /**
     * @dev Redeem mining credits for Bitcoin cloud mining power
     * @param credits Amount of mining credits to burn
     */
    function redeemMiningPower(uint256 credits) external nonReentrant {
        require(credits > 0, "Credits must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        _updateMiningCredits(user);

        require(user.miningCredits >= credits, "Insufficient mining credits");

        user.miningCredits -= credits;

        // 1:1 conversion rate for simplicity (can be adjusted)
        uint256 miningPower = credits;

        emit MiningPowerRedeemed(msg.sender, credits, miningPower);
    }

    /**
     * @dev Update mining rate (only owner)
     * @param newRate New mining rate per second per token
     */
    function updateMiningRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        miningRate = newRate;
        emit MiningRateUpdated(newRate);
    }

    /**
     * @dev Internal function to update user's mining credits
     * @param user UserInfo storage reference
     */
    function _updateMiningCredits(UserInfo storage user) internal {
        if (user.amount > 0) {
            uint256 timeElapsed = block.timestamp - user.lastUpdateTime;
            if (timeElapsed > 0) {
                uint256 creditsEarned = user.amount * timeElapsed * miningRate / 1e18;
                user.miningCredits += creditsEarned;
            }
        }
        user.lastUpdateTime = block.timestamp;
    }

    /**
     * @dev View function to get pending mining credits for a user
     * @param user Address of the user
     * @return Pending mining credits
     */
    function pendingMiningCredits(address user) external view returns (uint256) {
        UserInfo storage info = userInfo[user];
        uint256 pending = info.miningCredits;
        
        if (info.amount > 0) {
            uint256 timeElapsed = block.timestamp - info.lastUpdateTime;
            pending += info.amount * timeElapsed * miningRate / 1e18;
        }
        
        return pending;
    }
}
```
