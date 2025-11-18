"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snsy-ai.pages.dev
Prompt: Write a function in Solidity to manage vesting schedules using smart contracts, referencing the features described on Sensay's platform.
Generated: DETERMINISTIC_6718558de85408e0
Batch ID: 20250612_152924
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

/**
 * @title VestingContract
 * @dev This contract manages vesting schedules for tokens.
 * It allows for multiple beneficiaries and ensures that
 * tokens are released according to specified schedules.
 */
contract VestingContract {
    // Structure to hold information of each beneficiary's vesting schedule
    struct Beneficiary {
        uint256 totalAmount; // Total amount allocated to the beneficiary
        uint256 releasedAmount; // Amount already released
        uint256 startTime; // Start time of the vesting period
        uint256 cliff; // Duration of the cliff in seconds
        uint256 duration; // Duration of the vesting period in seconds
    }

    // Mapping of addresses to their vesting schedules
    mapping(address => Beneficiary) public beneficiaries;
    
    // The token being vested
    IERC20 public token;

    // Event to log the release of tokens
    event TokensReleased(address beneficiary, uint256 amount);

    // Constructor to initialize the contract with the token
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Adds a new beneficiary with the specified vesting schedule.
     * @param _beneficiary The address of the beneficiary.
     * @param _totalAmount The total amount allocated to the beneficiary.
     * @param _startTime The start time of the vesting period.
     * @param _cliff The duration of the cliff in seconds.
     * @param _duration The duration of the vesting period in seconds.
     */
    function addBeneficiary(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _startTime,
        uint256 _cliff,
        uint256 _duration
    ) public {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_totalAmount > 0, "Total amount must be greater than 0");
        require(
            _startTime + _cliff + _duration > block.timestamp,
            "Vesting must end in the future"
        );

        // Create a new beneficiary's vesting schedule
        beneficiaries[_beneficiary] = Beneficiary({
            totalAmount: _totalAmount,
            releasedAmount: 0,
            startTime: _startTime,
            cliff: _cliff,
            duration: _duration
        });
    }

    /**
     * @dev Allows a beneficiary to release their vested tokens.
     */
    function releaseTokens() public {
        Beneficiary storage beneficiary = beneficiaries[msg.sender];

        require(beneficiary.totalAmount > 0, "No tokens to release");
        
        uint256 unreleased = _releasableAmount(beneficiary);
        
        require(unreleased > 0, "No tokens are due for release");

        // Update the released amount for the beneficiary
        beneficiary.releasedAmount += unreleased;

        // Transfer the tokens to the beneficiary
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculates the amount of tokens that can be released for a beneficiary.
     * @param beneficiary The beneficiary's vesting schedule.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(Beneficiary storage beneficiary) internal view returns (uint256) {
        uint256 vestedAmount = _vestedAmount(beneficiary);
        return vestedAmount - beneficiary.releasedAmount;
    }

    /**
     * @dev Calculates the total amount of tokens that are vested for a beneficiary.
     * @param beneficiary The beneficiary's vesting schedule.
     * @return The amount of tokens that are vested.
     */
    function _vestedAmount(Beneficiary storage beneficiary) internal view returns (uint256) {
        if (block.timestamp < beneficiary.startTime + beneficiary.cliff) {
            return 0; // Tokens are still in cliff period
        } else if (block.timestamp >= beneficiary.startTime + beneficiary.duration) {
            return beneficiary.totalAmount; // All tokens are vested
        } else {
            // Calculate vested tokens based on elapsed time
            uint256 timeElapsed = block.timestamp - beneficiary.startTime - beneficiary.cliff;
            uint256 vestingDuration = beneficiary.duration - beneficiary.cliff;
            return (beneficiary.totalAmount * timeElapsed) / vestingDuration;
        }
    }
}

// Interface for the ERC20 token to allow transfers
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
