"""
Generated Code Metadata:
========================
Original URL: https://vesting-cookie.online
Prompt: Generate an example of a Smart contract that handles vesting schedules for a DAO.
Generated: DETERMINISTIC_7c26b5c2ff72b789
Batch ID: 20250612_162808
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
 * @title VestingSchedule
 * @dev A smart contract to handle token vesting schedules for a DAO.
 *      This contract allows the DAO to allocate tokens to beneficiaries
 *      with a vesting schedule, ensuring tokens are released over time.
 */
contract VestingSchedule {
    // Struct to represent a vesting schedule
    struct Vesting {
        uint256 totalAmount; // Total amount of tokens to be vested
        uint256 releasedAmount; // Amount of tokens already released
        uint256 startTime; // Start time of the vesting schedule (UNIX timestamp)
        uint256 cliffDuration; // Cliff duration in seconds
        uint256 vestingDuration; // Total vesting duration in seconds
    }

    // Mapping of beneficiary addresses to their vesting schedules
    mapping(address => Vesting) public vestingSchedules;

    // Token contract address (ERC20)
    address public token;

    // Owner of the contract (DAO admin)
    address public owner;

    // Events
    event VestingCreated(address indexed beneficiary, uint256 totalAmount, uint256 startTime, uint256 cliffDuration, uint256 vestingDuration);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = _token;
        owner = msg.sender;
    }

    /**
     * @dev Create a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param totalAmount Total amount of tokens to be vested.
     * @param startTime Start time of the vesting schedule (UNIX timestamp).
     * @param cliffDuration Cliff duration in seconds.
     * @param vestingDuration Total vesting duration in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 vestingDuration
    ) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(vestingDuration > cliffDuration, "Vesting duration must be greater than cliff duration");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists for beneficiary");

        vestingSchedules[beneficiary] = Vesting({
            totalAmount: totalAmount,
            releasedAmount: 0,
            startTime: startTime,
            cliffDuration: cliffDuration,
            vestingDuration: vestingDuration
        });

        emit VestingCreated(beneficiary, totalAmount, startTime, cliffDuration, vestingDuration);
    }

    /**
     * @dev Release vested tokens for the beneficiary.
     */
    function releaseTokens() external {
        Vesting storage vesting = vestingSchedules[msg.sender];
        require(vesting.totalAmount > 0, "No vesting schedule found");
        require(block.timestamp >= vesting.startTime + vesting.cliffDuration, "Cliff period not reached");

        uint256 vestedAmount = _calculateVestedAmount(vesting);
        uint256 releasableAmount = vestedAmount - vesting.releasedAmount;
        require(releasableAmount > 0, "No tokens available for release");

        vesting.releasedAmount += releasableAmount;

        // Transfer tokens to the beneficiary
        require(_transferTokens(msg.sender, releasableAmount), "Token transfer failed");

        emit TokensReleased(msg.sender, releasableAmount);
    }

    /**
     * @dev Calculate the vested amount for a given vesting schedule.
     * @param vesting Vesting schedule struct.
     * @return Vested amount of tokens.
     */
    function _calculateVestedAmount(Vesting memory vesting) internal view returns (uint256) {
        if (block.timestamp < vesting.startTime + vesting.cliffDuration) {
            return 0;
        } else if (block.timestamp >= vesting.startTime + vesting.vestingDuration) {
            return vesting.totalAmount;
        } else {
            uint256 timeElapsed = block.timestamp - vesting.startTime;
            return (vesting.totalAmount * timeElapsed) / vesting.vestingDuration;
        }
    }

    /**
     * @dev Transfer tokens to the beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer was successful.
     */
    function _transferTokens(address beneficiary, uint256 amount) internal returns (bool) {
        (bool success, bytes memory data) = token.call(
            abi.encodeWithSignature("transfer(address,uint256)", beneficiary, amount)
        );
        return success && (data.length == 0 || abi.decode(data, (bool)));
    }
}
```
