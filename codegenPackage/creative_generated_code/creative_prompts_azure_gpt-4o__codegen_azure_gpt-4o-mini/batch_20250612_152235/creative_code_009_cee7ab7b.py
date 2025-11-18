"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophpon.pages.dev
Prompt: Generate a Solidity contract to implement the tokenomics of $SOPH, including cliffs, vesting schedules, and lock-up periods for various allocation categories.
Generated: DETERMINISTIC_cee7ab7b87e2b991
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// @title SOPH Token Contract
// @notice This contract implements the tokenomics for the $SOPH token, including vesting schedules, cliffs, and lock-up periods.
contract SOPHToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Struct to define vesting schedule
    struct VestingSchedule {
        uint256 totalAmount; // Total amount allocated
        uint256 releasedAmount; // Amount already released
        uint256 start; // Start time of the vesting
        uint256 cliff; // Cliff duration in seconds
        uint256 duration; // Total vesting duration in seconds
        bool isRevoked; // Flag for revoking the vesting
    }

    // Mapping from address to its vesting schedule
    mapping(address => VestingSchedule) private vestingSchedules;

    // Events
    event TokensReleased(address indexed beneficiary, uint256 amount);
    event VestingRevoked(address indexed beneficiary);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("SOPH Token", "SOPH") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10**decimals()); // Mint 1 million tokens
    }

    // @notice Create a vesting schedule for a beneficiary
    // @param beneficiary Address to receive the tokens
    // @param totalAmount Total amount allocated
    // @param cliff Duration of the cliff
    // @param duration Total vesting duration
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 cliff,
        uint256 duration
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary is the zero address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(cliff < duration, "Cliff must be less than duration");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting already exists");

        // Initialize the vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            releasedAmount: 0,
            start: block.timestamp,
            cliff: cliff,
            duration: duration,
            isRevoked: false
        });
    }

    // @notice Release tokens to the beneficiary based on the vesting schedule
    function release() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];

        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.isRevoked, "Vesting revoked");

        uint256 unreleased = _releasableAmount(schedule);

        require(unreleased > 0, "No tokens are due for release");

        // Update released amount
        schedule.releasedAmount = schedule.releasedAmount.add(unreleased);
        
        // Transfer tokens to the beneficiary
        _transfer(address(this), msg.sender, unreleased);
        
        emit TokensReleased(msg.sender, unreleased);
    }

    // @notice Calculate the amount of tokens that can be released
    // @param schedule The vesting schedule of the beneficiary
    // @return The amount of releasable tokens
    function _releasableAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.start.add(schedule.cliff)) {
            return 0; // No tokens are releasable during the cliff
        } else if (block.timestamp >= schedule.start.add(schedule.duration)) {
            return schedule.totalAmount.sub(schedule.releasedAmount); // All tokens are releasable
        } else {
            uint256 vestedAmount = schedule.totalAmount.mul(block.timestamp.sub(schedule.start)).div(schedule.duration);
            return vestedAmount.sub(schedule.releasedAmount); // Calculate releasable tokens
        }
    }

    // @notice Revokes the vesting schedule for a beneficiary, preventing further releases
    // @param beneficiary Address of the beneficiary whose vesting is to be revoked
    function revoke(address beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];

        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.isRevoked, "Vesting already revoked");

        schedule.isRevoked = true;

        emit VestingRevoked(beneficiary);
    }

    // @notice Allows the owner to withdraw any unallocated tokens from the contract
    function withdrawUnallocatedTokens() external onlyOwner {
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        _transfer(address(this), owner(), balance);
    }
}
```
