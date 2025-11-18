"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://team-finance-solana-dk4sprfr7-trustswap.vercel.app
Prompt: Write a Solidity smart contract for token vesting that mimics the functionality of Team Finance's "Hourly Release Vesting Dashboard," ensuring compatibility with multiple blockchains.
Generated: DETERMINISTIC_44802c13eabf6b69
Batch ID: 20250612_153526
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

/**
 * @title TokenVesting
 * @dev This contract manages the vesting of ERC20 tokens for specified beneficiaries.
 * It allows for hourly release of tokens.
 */
contract TokenVesting is Ownable {
    struct VestingSchedule {
        uint256 totalAmount;        // Total amount of tokens to be released
        uint256 releasedAmount;     // Amount of tokens already released
        uint256 startTime;          // Start time of the vesting period
        uint256 vestingDuration;    // Duration of the vesting in seconds
        uint256 releaseInterval;    // Interval for hourly release in seconds
    }

    // Token to be vested
    IERC20 public token;

    // Mapping of beneficiaries to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the token and set the owner.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Creates a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary receiving tokens.
     * @param totalAmount Total amount of tokens to be vested.
     * @param vestingDuration Duration of the vesting in seconds.
     * @param releaseInterval Interval for hourly release in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 vestingDuration,
        uint256 releaseInterval
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(vestingDuration > 0, "Vesting duration must be greater than zero");
        require(releaseInterval > 0, "Release interval must be greater than zero");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            releasedAmount: 0,
            startTime: block.timestamp,
            vestingDuration: vestingDuration,
            releaseInterval: releaseInterval
        });
    }

    /**
     * @dev Releases the vested tokens to the beneficiary.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];

        require(schedule.totalAmount > 0, "No tokens vested for this address");
        
        uint256 currentTime = block.timestamp;
        uint256 vestedAmount = _calculateVestedAmount(schedule, currentTime);

        require(vestedAmount > schedule.releasedAmount, "No tokens available for release");

        uint256 amountToRelease = vestedAmount - schedule.releasedAmount;
        schedule.releasedAmount += amountToRelease;

        // Transfer tokens to the beneficiary
        require(token.balanceOf(address(this)) >= amountToRelease, "Insufficient contract balance");
        token.transfer(msg.sender, amountToRelease);
        
        emit TokensReleased(msg.sender, amountToRelease);
    }

    /**
     * @dev Internal function to calculate the amount of tokens vested.
     * @param schedule The vesting schedule of the beneficiary.
     * @param currentTime The current block timestamp.
     * @return The vested amount of tokens.
     */
    function _calculateVestedAmount(VestingSchedule memory schedule, uint256 currentTime) internal view returns (uint256) {
        if (currentTime < schedule.startTime) {
            return 0;
        }
        uint256 elapsedTime = currentTime - schedule.startTime;
        uint256 totalReleases = elapsedTime / schedule.releaseInterval;
        uint256 totalVested = (totalReleases * schedule.totalAmount) / (schedule.vestingDuration / schedule.releaseInterval);
        
        return totalVested > schedule.totalAmount ? schedule.totalAmount : totalVested;
    }

    /**
     * @dev Allows the owner to withdraw any tokens that were mistakenly sent to the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }
}
```
