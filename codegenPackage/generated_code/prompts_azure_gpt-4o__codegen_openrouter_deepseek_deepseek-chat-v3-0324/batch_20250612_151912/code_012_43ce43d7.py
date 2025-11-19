"""
Generated Code Metadata:
========================
Original URL: https://orchidprotocols.com
Prompt: Write a Solidity contract that enables users to stake OXT tokens and access Orchid’s decentralized VPN services.
Generated: DETERMINISTIC_43ce43d73d3c83e6
Batch ID: 20250612_151912
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OrchidVPNStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // OXT token contract
    IERC20 public immutable oxtToken;

    // Struct to store staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
        uint256 vpnAccessExpiry;
    }

    // Minimum stake amount
    uint256 public constant MIN_STAKE = 1 ether; // 1 OXT (assuming 18 decimals)

    // VPN access duration per stake amount (1 day per 1 OXT)
    uint256 public constant ACCESS_PER_STAKE = 1 days;

    // Mapping of staker addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 expiry);
    event Unstaked(address indexed user, uint256 amount);
    event AccessExtended(address indexed user, uint256 newExpiry);

    constructor(address _oxtToken) {
        require(_oxtToken != address(0), "Invalid token address");
        oxtToken = IERC20(_oxtToken);
    }

    /**
     * @notice Stake OXT tokens to gain VPN access
     * @param amount Amount of OXT to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE, "Amount below minimum stake");
        
        Staker storage staker = stakers[msg.sender];
        uint256 currentTime = block.timestamp;

        // Transfer tokens from user to contract
        oxtToken.safeTransferFrom(msg.sender, address(this), amount);

        // Calculate new expiry time
        uint256 additionalAccess = amount * ACCESS_PER_STAKE / MIN_STAKE;
        uint256 newExpiry = staker.vpnAccessExpiry > currentTime 
            ? staker.vpnAccessExpiry + additionalAccess 
            : currentTime + additionalAccess;

        // Update staker info
        staker.stakedAmount += amount;
        staker.lastStakedTimestamp = currentTime;
        staker.vpnAccessExpiry = newExpiry;

        emit Staked(msg.sender, amount, newExpiry);
    }

    /**
     * @notice Unstake OXT tokens and forfeit remaining VPN access
     * @param amount Amount of OXT to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked balance");

        // Update staker info before transfer to prevent reentrancy
        staker.stakedAmount -= amount;
        if (staker.stakedAmount == 0) {
            staker.vpnAccessExpiry = 0;
        }

        // Transfer tokens back to user
        oxtToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Check if an address has active VPN access
     * @param user Address to check
     * @return True if access is active
     */
    function hasAccess(address user) external view returns (bool) {
        return stakers[user].vpnAccessExpiry > block.timestamp;
    }

    /**
     * @notice Get remaining access time for a user
     * @param user Address to check
     * @return Remaining access time in seconds
     */
    function remainingAccessTime(address user) external view returns (uint256) {
        uint256 expiry = stakers[user].vpnAccessExpiry;
        return expiry > block.timestamp ? expiry - block.timestamp : 0;
    }

    /**
     * @notice Emergency withdraw all OXT tokens (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = oxtToken.balanceOf(address(this));
        oxtToken.safeTransfer(owner(), balance);
    }
}
```
