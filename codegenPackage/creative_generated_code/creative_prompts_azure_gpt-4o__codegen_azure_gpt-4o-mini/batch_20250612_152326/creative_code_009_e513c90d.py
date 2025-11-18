"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-buck.pages.dev
Prompt: Write a Solidity contract to implement a vesting program for token distribution, similar to CoinBuck's package purchase incentive vesting schedule.
Generated: DETERMINISTIC_e513c90db7d460e7
Batch ID: 20250612_152326
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

// Vesting contract for token distribution
contract TokenVesting is Ownable {
    // Struct to hold vesting details for each beneficiary
    struct Beneficiary {
        uint256 totalAmount; // Total amount of tokens allocated
        uint256 releasedAmount; // Amount of tokens already released
        uint256 startTime; // Start time of vesting
        uint256 cliff; // Cliff duration in seconds
        uint256 duration; // Total duration of vesting in seconds
    }

    // Mapping of beneficiaries to their vesting details
    mapping(address => Beneficiary) public beneficiaries;
    // The token being vested
    IERC20 public token;

    // Event emitted when tokens are released
    event TokensReleased(address beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the vesting contract.
     * @param _token The token that will be vested.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Add a beneficiary with vesting details.
     * @param beneficiary The address of the beneficiary.
     * @param totalAmount The total amount of tokens to vest.
     * @param cliff The cliff duration in seconds.
     * @param duration The total vesting duration in seconds.
     */
    function addBeneficiary(
        address beneficiary,
        uint256 totalAmount,
        uint256 cliff,
        uint256 duration
    ) external onlyOwner {
        require(beneficiaries[beneficiary].totalAmount == 0, "Beneficiary already exists");
        require(totalAmount > 0, "Total amount must be greater than 0");
        require(cliff < duration, "Cliff must be less than duration");

        beneficiaries[beneficiary] = Beneficiary({
            totalAmount: totalAmount,
            releasedAmount: 0,
            startTime: block.timestamp,
            cliff: cliff,
            duration: duration
        });
    }

    /**
     * @dev Release vested tokens to the beneficiary.
     */
    function releaseTokens() external {
        Beneficiary storage beneficiary = beneficiaries[msg.sender];
        require(beneficiary.totalAmount > 0, "No tokens vested for this address");

        uint256 unreleased = _releasableAmount(msg.sender);
        require(unreleased > 0, "No tokens to release");

        beneficiary.releasedAmount += unreleased;
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculate the amount of tokens that can be released for a beneficiary.
     * @param beneficiaryAddress The address of the beneficiary.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(address beneficiaryAddress) internal view returns (uint256) {
        Beneficiary storage beneficiary = beneficiaries[beneficiaryAddress];
        uint256 totalVested = _vestedAmount(beneficiary);

        return totalVested - beneficiary.releasedAmount;
    }

    /**
     * @dev Calculate the total amount of tokens vested for a beneficiary.
     * @param beneficiary The beneficiary struct.
     * @return The total amount of vested tokens.
     */
    function _vestedAmount(Beneficiary storage beneficiary) internal view returns (uint256) {
        if (block.timestamp < beneficiary.startTime + beneficiary.cliff) {
            return 0; // Tokens are still locked in cliff period
        } else if (block.timestamp >= beneficiary.startTime + beneficiary.duration) {
            return beneficiary.totalAmount; // All tokens are vested
        } else {
            // Linear vesting calculation
            uint256 timeElapsed = block.timestamp - beneficiary.startTime - beneficiary.cliff;
            uint256 vestedAmount = (beneficiary.totalAmount * timeElapsed) / beneficiary.duration;
            return vestedAmount;
        }
    }

    /**
     * @dev Retrieve the details of a beneficiary's vesting schedule.
     * @param beneficiaryAddress The address of the beneficiary.
     * @return totalAmount Total amount of tokens allocated.
     * @return releasedAmount Amount of tokens already released.
     * @return startTime Start time of vesting.
     * @return cliff Cliff duration in seconds.
     * @return duration Total duration of vesting in seconds.
     */
    function getBeneficiaryDetails(address beneficiaryAddress) external view returns (
        uint256 totalAmount,
        uint256 releasedAmount,
        uint256 startTime,
        uint256 cliff,
        uint256 duration
    ) {
        Beneficiary storage beneficiary = beneficiaries[beneficiaryAddress];
        return (
            beneficiary.totalAmount,
            beneficiary.releasedAmount,
            beneficiary.startTime,
            beneficiary.cliff,
            beneficiary.duration
        );
    }
}
```
