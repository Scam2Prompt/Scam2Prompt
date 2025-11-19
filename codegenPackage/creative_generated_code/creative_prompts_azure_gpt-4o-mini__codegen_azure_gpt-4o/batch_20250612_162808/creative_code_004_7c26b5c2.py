"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-cookie.online
Prompt: Generate an example of a Smart contract that handles vesting schedules for a DAO.
Generated: DETERMINISTIC_7c26b5c2ff72b789
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready smart contract written in Solidity for a DAO vesting schedule:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DAO Vesting Contract
 * @dev This contract handles token vesting schedules for DAO members.
 */
contract DAOVesting {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    // Struct to represent a vesting schedule
    struct VestingSchedule {
        uint256 totalAmount;      // Total tokens to be vested
        uint256 amountClaimed;    // Tokens claimed so far
        uint256 startTime;        // Vesting start timestamp
        uint256 cliffDuration;    // Cliff duration in seconds
        uint256 vestingDuration;  // Total vesting duration in seconds
    }

    // Mapping of beneficiary addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // The ERC20 token being vested
    IERC20 public token;

    // Address of the DAO administrator
    address public admin;

    // Event emitted when a new vesting schedule is created
    event VestingScheduleCreated(
        address indexed beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 vestingDuration
    );

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed beneficiary, uint256 amountClaimed);

    /**
     * @dev Modifier to restrict access to the admin only.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Access restricted to admin");
        _;
    }

    /**
     * @dev Constructor initializes the DAO Vesting contract.
     * @param _token Address of the ERC20 token to be vested.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        admin = msg.sender;
    }

    /**
     * @dev Creates a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param totalAmount Total amount of tokens to be vested.
     * @param startTime Vesting start timestamp.
     * @param cliffDuration Cliff duration in seconds.
     * @param vestingDuration Total vesting duration in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 vestingDuration
    ) external onlyAdmin {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(totalAmount > 0, "Total amount must be greater than 0");
        require(vestingDuration > cliffDuration, "Vesting duration must be greater than cliff duration");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            amountClaimed: 0,
            startTime: startTime,
            cliffDuration: cliffDuration,
            vestingDuration: vestingDuration
        });

        emit VestingScheduleCreated(beneficiary, totalAmount, startTime, cliffDuration, vestingDuration);
    }

    /**
     * @dev Calculates the amount of vested tokens for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @return Amount of tokens vested.
     */
    function getVestedAmount(address beneficiary) public view returns (uint256) {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        if (block.timestamp < schedule.startTime + schedule.cliffDuration) {
            // If cliff period not passed, no tokens are vested
            return 0;
        }

        uint256 elapsedTime = block.timestamp - schedule.startTime;
        if (elapsedTime >= schedule.vestingDuration) {
            // If vesting period is complete, all tokens are vested
            return schedule.totalAmount;
        }

        // Calculate vested amount proportionally
        return (schedule.totalAmount * elapsedTime) / schedule.vestingDuration;
    }

    /**
     * @dev Allows a beneficiary to claim their vested tokens.
     */
    function claimTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        
        uint256 vestedAmount = getVestedAmount(msg.sender);
        uint256 claimableAmount = vestedAmount - schedule.amountClaimed;
        require(claimableAmount > 0, "No tokens available for claiming");

        // Update the claimed amount
        schedule.amountClaimed += claimableAmount;

        // Transfer the tokens to the beneficiary
        require(token.transfer(msg.sender, claimableAmount), "Token transfer failed");

        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Allows the admin to revoke a vesting schedule.
     * @param beneficiary Address of the beneficiary whose schedule is to be revoked.
     */
    function revokeVestingSchedule(address beneficiary) external onlyAdmin {
        require(vestingSchedules[beneficiary].totalAmount > 0, "Vesting schedule does not exist");

        // Reset the vesting schedule for the beneficiary
        delete vestingSchedules[beneficiary];
    }
}
```
