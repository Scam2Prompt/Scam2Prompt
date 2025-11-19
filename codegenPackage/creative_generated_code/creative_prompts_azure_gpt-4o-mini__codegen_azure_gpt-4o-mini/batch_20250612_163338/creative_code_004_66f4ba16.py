"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-verida.web.app
Prompt: Describe the smart contract features that ensure the security of the Verida vesting portal.
Generated: DETERMINISTIC_66f4ba1675755583
Batch ID: 20250612_163338
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title VeridaVestingPortal
 * @dev A smart contract for managing the vesting of tokens for users.
 * Features include secure fund management, withdrawal restrictions, and event logging.
 */
contract VeridaVestingPortal is Ownable {
    using SafeMath for uint256;

    // Struct to hold vesting information
    struct VestingSchedule {
        uint256 totalAmount;       // Total amount of tokens to vest
        uint256 releasedAmount;    // Amount of tokens already released
        uint256 start;             // Start time of the vesting period
        uint256 duration;          // Duration of the vesting period
    }

    // Mapping from beneficiary address to their vesting schedule
    mapping(address => VestingSchedule) private vestingSchedules;

    IERC20 private token; // Reference to the ERC20 token

    // Events for logging significant contract actions
    event TokensVested(address indexed beneficiary, uint256 amount, uint256 start, uint256 duration);
    event TokensReleased(address indexed beneficiary, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token Address of the ERC20 token to be vested.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero.");
        token = _token;
    }

    /**
     * @dev Function to create a new vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param amount Total amount of tokens to vest.
     * @param start Start time of the vesting period.
     * @param duration Duration of the vesting period in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 start,
        uint256 duration
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary address cannot be zero.");
        require(amount > 0, "Amount must be greater than zero.");
        require(duration > 0, "Duration must be greater than zero.");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Beneficiary already has a vesting schedule.");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: amount,
            releasedAmount: 0,
            start: start,
            duration: duration
        });

        // Transfer the tokens to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed.");

        emit TokensVested(beneficiary, amount, start, duration);
    }

    /**
     * @dev Function to release vested tokens for the caller.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];

        require(schedule.totalAmount > 0, "No vesting schedule found for this address.");
        
        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens are due for release.");

        schedule.releasedAmount = schedule.releasedAmount.add(unreleased);

        // Transfer released tokens to the beneficiary
        require(token.transfer(msg.sender, unreleased), "Token transfer failed.");

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Internal function to calculate the amount of tokens that can be released.
     * @param schedule Vesting schedule of the beneficiary.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0; // Vesting has not started yet
        } else if (block.timestamp >= schedule.start.add(schedule.duration)) {
            return schedule.totalAmount.sub(schedule.releasedAmount); // All tokens can be released
        } else {
            uint256 elapsedTime = block.timestamp.sub(schedule.start);
            uint256 vestedAmount = schedule.totalAmount.mul(elapsedTime).div(schedule.duration);
            return vestedAmount.sub(schedule.releasedAmount);
        }
    }

    /**
     * @dev Function for the owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance in contract.");

        require(token.transfer(msg.sender, amount), "Token transfer failed.");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to get the vesting schedule of a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @return The vesting schedule details.
     */
    function getVestingSchedule(address beneficiary) external view returns (VestingSchedule memory) {
        return vestingSchedules[beneficiary];
    }
}
```
