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

/**
 * @title TokenSwapWithVesting
 * @dev Smart contract to facilitate token swaps with a vesting schedule.
 *      Built for Binance Smart Chain.
 */
contract TokenSwapWithVesting {
    struct VestingSchedule {
        uint256 totalAmount; // Total tokens to be vested
        uint256 claimedAmount; // Amount of tokens already claimed
        uint256 startTime; // Vesting start time (UNIX timestamp)
        uint256 cliffDuration; // Cliff period in seconds
        uint256 vestingDuration; // Total vesting duration in seconds
    }

    // Address of the token being swapped
    address public tokenAddress;

    // Mapping of user addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Address of the admin (contract owner)
    address public admin;

    // Event emitted whenever a claim is made
    event TokensClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to admin only
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        admin = msg.sender;
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Function to set a vesting schedule for a user.
     * @param _user Address of the user
     * @param _totalAmount Total amount of tokens to be vested
     * @param _startTime Vesting start time (UNIX timestamp)
     * @param _cliffDuration Cliff duration in seconds
     * @param _vestingDuration Total vesting duration in seconds
     */
    function setVestingSchedule(
        address _user,
        uint256 _totalAmount,
        uint256 _startTime,
        uint256 _cliffDuration,
        uint256 _vestingDuration
    ) external onlyAdmin {
        require(_user != address(0), "Invalid user address");
        require(_totalAmount > 0, "Total amount must be greater than 0");
        require(_vestingDuration > _cliffDuration, "Vesting duration must be greater than cliff duration");

        vestingSchedules[_user] = VestingSchedule({
            totalAmount: _totalAmount,
            claimedAmount: 0,
            startTime: _startTime,
            cliffDuration: _cliffDuration,
            vestingDuration: _vestingDuration
        });
    }

    /**
     * @dev Function to claim vested tokens.
     */
    function claimTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule found for the user");

        uint256 currentTime = block.timestamp;
        require(currentTime >= schedule.startTime + schedule.cliffDuration, "Cliff period not reached");

        uint256 vestingEndTime = schedule.startTime + schedule.vestingDuration;
        uint256 vestedAmount;

        if (currentTime >= vestingEndTime) {
            // All tokens are vested if vesting period is completed
            vestedAmount = schedule.totalAmount;
        } else {
            // Calculate the amount vested based on time elapsed
            uint256 timeElapsed = currentTime - schedule.startTime;
            vestedAmount = (schedule.totalAmount * timeElapsed) / schedule.vestingDuration;
        }

        uint256 claimableAmount = vestedAmount - schedule.claimedAmount;
        require(claimableAmount > 0, "No tokens available for claim");

        schedule.claimedAmount += claimableAmount;

        require(ERC20(tokenAddress).transfer(msg.sender, claimableAmount), "Token transfer failed");
        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract (admin-only).
     * @param _amount Amount of tokens to withdraw
     */
    function adminWithdraw(uint256 _amount) external onlyAdmin {
        require(ERC20(tokenAddress).transfer(admin, _amount), "Token transfer failed");
    }
}

/**
 * @dev ERC20 Interface to interact with the token contract.
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
