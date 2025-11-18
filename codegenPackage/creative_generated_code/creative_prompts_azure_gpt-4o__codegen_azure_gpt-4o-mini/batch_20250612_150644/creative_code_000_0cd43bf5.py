"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-cookie.online
Prompt: Write a smart contract in Solidity for a vesting portal that integrates wallet connection functionality, similar to the features described on Cookie DAO's website.
Generated: DETERMINISTIC_0cd43bf5a62a53ef
Batch ID: 20250612_150644
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Vesting contract for managing token vesting
contract VestingPortal is Ownable {
    using SafeMath for uint256;

    // Structure to hold vesting information
    struct VestingSchedule {
        uint256 amount;           // Total amount of tokens to be vested
        uint256 released;         // Amount of tokens already released
        uint256 start;           // Start timestamp of the vesting period
        uint256 duration;        // Duration of the vesting period
        bool revocable;          // Indicates if the vesting is revocable
        bool revoked;            // Indicates if the vesting has been revoked
    }

    // Mapping from beneficiary address to their vesting schedule
    mapping(address => VestingSchedule) public vestingSchedules;

    // The ERC20 token being vested
    IERC20 public token;

    // Event emitted when tokens are released
    event TokensReleased(address beneficiary, uint256 amount);

    // Event emitted when vesting is revoked
    event VestingRevoked(address beneficiary);

    // Constructor to initialize the contract with the token address
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    // Function to create a new vesting schedule
    function createVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 start,
        uint256 duration,
        bool revocable
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(vestingSchedules[beneficiary].amount == 0, "Vesting already exists for this beneficiary");

        vestingSchedules[beneficiary] = VestingSchedule({
            amount: amount,
            released: 0,
            start: start,
            duration: duration,
            revocable: revocable,
            revoked: false
        });
    }

    // Function to release vested tokens for a beneficiary
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.amount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting has been revoked");

        uint256 vestedAmount = _vestedAmount(schedule);
        uint256 unreleased = vestedAmount.sub(schedule.released);

        require(unreleased > 0, "No tokens to release");

        schedule.released = schedule.released.add(unreleased);
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    // Internal function to calculate the amount of vested tokens
    function _vestedAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0;
        } else if (block.timestamp >= schedule.start.add(schedule.duration) || schedule.revoked) {
            return schedule.amount;
        } else {
            return schedule.amount.mul(block.timestamp.sub(schedule.start)).div(schedule.duration);
        }
    }

    // Function to revoke the vesting schedule
    function revokeVesting(address beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.revocable, "Vesting is not revocable");
        require(!schedule.revoked, "Vesting already revoked");

        schedule.revoked = true;

        emit VestingRevoked(beneficiary);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient balance");
        token.transfer(msg.sender, amount);
    }
}
```
