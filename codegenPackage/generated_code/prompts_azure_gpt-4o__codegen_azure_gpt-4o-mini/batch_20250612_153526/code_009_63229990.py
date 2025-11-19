"""
Generated Code Metadata:
========================
Original URL: https://team-finance-solana-dk4sprfr7-trustswap.vercel.app
Prompt: Create a smart contract for locking tokens with flexible vesting schedules, ensuring transparency and security as described in Team Finance's "Token Locks" service.
Generated: DETERMINISTIC_63229990bc91d9fa
Batch ID: 20250612_153526
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

/**
 * @title TokenLock
 * @dev A smart contract for locking tokens with flexible vesting schedules.
 */
contract TokenLock is Ownable {
    // Struct to hold vesting information
    struct VestingSchedule {
        uint256 totalAmount; // Total amount of tokens locked
        uint256 releasedAmount; // Amount of tokens already released
        uint256 start; // Start time of the vesting
        uint256 duration; // Duration of the vesting in seconds
        bool isRevoked; // Indicates if the vesting is revoked
    }

    // Mapping of beneficiary addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // The token being locked
    IERC20 public token;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 start, uint256 duration);

    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Event emitted when vesting is revoked
    event VestingRevoked(address indexed beneficiary);

    /**
     * @dev Constructor to set the token address.
     * @param _token The address of the ERC20 token to be locked.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Locks tokens for a beneficiary with a vesting schedule.
     * @param beneficiary The address of the beneficiary.
     * @param amount The amount of tokens to lock.
     * @param start The start time of the vesting.
     * @param duration The duration of the vesting in seconds.
     */
    function lockTokens(address beneficiary, uint256 amount, uint256 start, uint256 duration) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Tokens already locked for this beneficiary");

        // Transfer tokens from the owner to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create a new vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: amount,
            releasedAmount: 0,
            start: start,
            duration: duration,
            isRevoked: false
        });

        emit TokensLocked(beneficiary, amount, start, duration);
    }

    /**
     * @dev Releases vested tokens to the beneficiary.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No tokens locked for this beneficiary");
        require(!schedule.isRevoked, "Vesting is revoked");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens are due for release");

        // Update the released amount
        schedule.releasedAmount += unreleased;

        // Transfer the tokens to the beneficiary
        require(token.transfer(msg.sender, unreleased), "Token transfer failed");

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Revokes the vesting schedule for a beneficiary.
     * @param beneficiary The address of the beneficiary.
     */
    function revokeVesting(address beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount > 0, "No tokens locked for this beneficiary");
        require(!schedule.isRevoked, "Vesting is already revoked");

        // Mark the vesting as revoked
        schedule.isRevoked = true;

        emit VestingRevoked(beneficiary);
    }

    /**
     * @dev Calculates the amount of tokens that can be released.
     * @param schedule The vesting schedule of the beneficiary.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0; // Vesting has not started
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.totalAmount - schedule.releasedAmount; // All tokens can be released
        } else {
            uint256 vestedAmount = (schedule.totalAmount * (block.timestamp - schedule.start)) / schedule.duration;
            return vestedAmount - schedule.releasedAmount; // Calculate the releasable amount
        }
    }
}
```
