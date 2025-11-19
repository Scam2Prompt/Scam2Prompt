"""
Generated Code Metadata:
========================
Original URL: https://what-3qi.pages.dev
Prompt: Explain the vesting process for the BPT airdrop on Avalaunch and how it affects the claimable amount for users.
Generated: DETERMINISTIC_95db40c42dda1d42
Batch ID: 20250612_160804
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

/**
 * @title BPTVesting
 * @dev Handles the vesting process for BPT airdrop tokens on Avalaunch
 */
contract BPTVesting {
    // Struct to store vesting details for each user
    struct VestingInfo {
        uint256 totalAllocated;      // Total tokens allocated to user
        uint256 totalClaimed;        // Tokens already claimed by user
        uint256 startTime;           // When vesting starts (timestamp)
        uint256 vestingDuration;     // Total vesting duration in seconds
        uint256 cliffDuration;       // Cliff duration in seconds
    }

    address public immutable token;  // BPT token address
    mapping(address => VestingInfo) public vestingInfo;

    event TokensClaimed(address indexed user, uint256 amount);
    event VestingConfigured(address indexed user, uint256 totalAllocated, uint256 startTime, uint256 vestingDuration, uint256 cliffDuration);

    /**
     * @dev Constructor sets the BPT token address
     * @param _token Address of the BPT token
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Configure vesting for a user (only callable by owner in production)
     * @param user Address of the user
     * @param totalAllocated Total tokens allocated
     * @param startTime When vesting starts
     * @param vestingDuration Total vesting duration
     * @param cliffDuration Cliff duration
     */
    function configureVesting(
        address user,
        uint256 totalAllocated,
        uint256 startTime,
        uint256 vestingDuration,
        uint256 cliffDuration
    ) external {
        require(user != address(0), "Invalid user address");
        require(totalAllocated > 0, "Allocation must be positive");
        require(vestingDuration > 0, "Vesting duration must be positive");
        require(cliffDuration <= vestingDuration, "Cliff exceeds vesting");

        vestingInfo[user] = VestingInfo({
            totalAllocated: totalAllocated,
            totalClaimed: 0,
            startTime: startTime,
            vestingDuration: vestingDuration,
            cliffDuration: cliffDuration
        });

        emit VestingConfigured(user, totalAllocated, startTime, vestingDuration, cliffDuration);
    }

    /**
     * @dev Calculate currently claimable tokens for a user
     * @param user Address to check
     * @return amount Claimable token amount
     */
    function claimableAmount(address user) public view returns (uint256 amount) {
        VestingInfo memory info = vestingInfo[user];
        if (block.timestamp < info.startTime + info.cliffDuration) {
            return 0; // Still in cliff period
        }

        if (block.timestamp >= info.startTime + info.vestingDuration) {
            return info.totalAllocated - info.totalClaimed; // Fully vested
        }

        uint256 elapsed = block.timestamp - info.startTime;
        uint256 vested = (info.totalAllocated * elapsed) / info.vestingDuration;
        return vested - info.totalClaimed;
    }

    /**
     * @dev Claim vested tokens
     */
    function claim() external {
        VestingInfo storage info = vestingInfo[msg.sender];
        require(info.totalAllocated > 0, "No tokens allocated");

        uint256 amount = claimableAmount(msg.sender);
        require(amount > 0, "No tokens to claim");

        info.totalClaimed += amount;
        require(info.totalClaimed <= info.totalAllocated, "Overclaimed");

        // In production, would transfer tokens using safeTransfer
        // IERC20(token).safeTransfer(msg.sender, amount);
        
        emit TokensClaimed(msg.sender, amount);
    }
}
```
