"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pad-chaingpt.pages.dev
Prompt: Write a smart contract in Solidity to facilitate token swaps on the Binance Smart Chain, adhering to the ChainGPT Pad's token claim structure and vesting schedule.
Generated: DETERMINISTIC_c3cc402b14924358
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title TokenSwap
/// @notice This contract facilitates token swaps with a vesting schedule.
contract TokenSwap is Ownable, ReentrancyGuard {
    // Struct representing the vesting schedule for each user
    struct VestingSchedule {
        uint256 totalAmount; // Total amount to be claimed
        uint256 claimedAmount; // Amount already claimed
        uint256 startTime; // Start time of the vesting
        uint256 duration; // Duration of the vesting in seconds
    }

    // Mapping of user addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // The token that will be swapped
    IERC20 public token;

    // Event emitted when a swap is initiated
    event SwapInitiated(address indexed user, uint256 amount);
    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    /// @param _token The address of the ERC20 token to swap
    constructor(IERC20 _token) {
        token = _token;
    }

    /// @notice Initiates a token swap with a vesting schedule
    /// @param amount The amount of tokens to be swapped
    /// @param vestingDuration The duration of the vesting in seconds
    function initiateSwap(uint256 amount, uint256 vestingDuration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(vestingSchedules[msg.sender].totalAmount == 0, "Swap already initiated");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Create a new vesting schedule for the user
        vestingSchedules[msg.sender] = VestingSchedule({
            totalAmount: amount,
            claimedAmount: 0,
            startTime: block.timestamp,
            duration: vestingDuration
        });

        emit SwapInitiated(msg.sender, amount);
    }

    /// @notice Claims the vested tokens for the sender
    function claimTokens() external nonReentrant {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];

        require(schedule.totalAmount > 0, "No tokens to claim");
        
        uint256 vestedAmount = calculateVestedAmount(schedule);
        uint256 claimableAmount = vestedAmount - schedule.claimedAmount;

        require(claimableAmount > 0, "No claimable tokens");

        // Update claimed amount
        schedule.claimedAmount += claimableAmount;

        // Transfer the claimable tokens to the user
        token.transfer(msg.sender, claimableAmount);

        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /// @notice Calculates the amount of tokens that are vested based on the vesting schedule
    /// @param schedule The vesting schedule for the user
    /// @return The amount of tokens that have vested
    function calculateVestedAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.startTime) {
            return 0; // No tokens have vested yet
        } else if (block.timestamp >= schedule.startTime + schedule.duration) {
            return schedule.totalAmount; // All tokens are vested
        } else {
            // Calculate vested amount based on time elapsed
            uint256 elapsedTime = block.timestamp - schedule.startTime;
            return (schedule.totalAmount * elapsedTime) / schedule.duration;
        }
    }

    /// @notice Allows the owner to withdraw tokens in case of an emergency
    /// @param amount The amount of tokens to withdraw
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        token.transfer(owner(), amount);
    }
}
```
