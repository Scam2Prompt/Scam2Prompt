"""
Generated Code Metadata:
========================
Original URL: https://pad-chaingpt.pages.dev
Prompt: Write a smart contract in Solidity to facilitate token swaps on the Binance Smart Chain, adhering to the ChainGPT Pad's token claim structure and vesting schedule.
Generated: DETERMINISTIC_c3cc402b14924358
Batch ID: 20250612_145121
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ChainGPTPadTokenSwap
 * @author [Your Name]
 * @notice This contract facilitates token swaps on the Binance Smart Chain,
 *          following the ChainGPT Pad's token claim structure and vesting schedule.
 */
contract ChainGPTPadTokenSwap is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user claim information
    mapping(address => UserClaim) public userClaims;

    // Mapping of vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Token swap address
    address public tokenSwapAddress;

    // Token address
    address public tokenAddress;

    // Total tokens allocated for the sale
    uint256 public totalTokensAllocated;

    // Token price in BNB
    uint256 public tokenPrice;

    // Claim start timestamp
    uint256 public claimStartTimestamp;

    // Claim end timestamp
    uint256 public claimEndTimestamp;

    // Vesting duration in seconds
    uint256 public vestingDuration;

    // Token contract instance
    ERC20Burnable public token;

    /**
     * @notice Event emitted when a user claims tokens
     * @param user The user's address
     * @param amount The amount of tokens claimed
     */
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @notice Event emitted when a user swaps tokens
     * @param user The user's address
     * @param amount The amount of tokens swapped
     */
    event TokensSwapped(address indexed user, uint256 amount);

    /**
     * @param _tokenSwapAddress The token swap address
     * @param _tokenAddress The token address
     * @param _totalTokensAllocated The total tokens allocated for the sale
     * @param _tokenPrice The token price in BNB
     * @param _claimStartTimestamp The claim start timestamp
     * @param _claimEndTimestamp The claim end timestamp
     * @param _vestingDuration The vesting duration in seconds
     */
    constructor(
        address _tokenSwapAddress,
        address _tokenAddress,
        uint256 _totalTokensAllocated,
        uint256 _tokenPrice,
        uint256 _claimStartTimestamp,
        uint256 _claimEndTimestamp,
        uint256 _vestingDuration
    ) public {
        tokenSwapAddress = _tokenSwapAddress;
        tokenAddress = _tokenAddress;
        totalTokensAllocated = _totalTokensAllocated;
        tokenPrice = _tokenPrice;
        claimStartTimestamp = _claimStartTimestamp;
        claimEndTimestamp = _claimEndTimestamp;
        vestingDuration = _vestingDuration;

        // Initialize token contract instance
        token = ERC20Burnable(_tokenAddress);
    }

    /**
     * @notice Structure for user claim information
     */
    struct UserClaim {
        uint256 claimedAmount;
        uint256 claimTimestamp;
    }

    /**
     * @notice Structure for vesting schedule
     */
    struct VestingSchedule {
        uint256 vestingStartTimestamp;
        uint256 vestingEndTimestamp;
        uint256 totalVestingAmount;
        uint256 claimedVestingAmount;
    }

    /**
     * @notice Function to claim tokens
     * @param _amount The amount of tokens to claim
     */
    function claimTokens(uint256 _amount) public nonReentrant {
        require(msg.sender != address(0), "Invalid user address");
        require(_amount > 0, "Invalid claim amount");
        require(block.timestamp >= claimStartTimestamp, "Claim period not started");
        require(block.timestamp <= claimEndTimestamp, "Claim period ended");

        // Update user claim information
        UserClaim storage userClaim = userClaims[msg.sender];
        uint256 remainingTokens = totalTokensAllocated.sub(userClaim.claimedAmount);
        require(remainingTokens >= _amount, "Insufficient tokens available");

        userClaim.claimedAmount = userClaim.claimedAmount.add(_amount);
        userClaim.claimTimestamp = block.timestamp;

        // Transfer tokens to user
        token.transfer(msg.sender, _amount);

        emit TokensClaimed(msg.sender, _amount);
    }

    /**
     * @notice Function to swap tokens
     * @param _amount The amount of tokens to swap
     */
    function swapTokens(uint256 _amount) public nonReentrant {
        require(msg.sender == tokenSwapAddress, "Invalid token swap address");
        require(_amount > 0, "Invalid swap amount");

        // Update vesting schedule
        VestingSchedule storage vestingSchedule = vestingSchedules[msg.sender];
        vestingSchedule.totalVestingAmount = vestingSchedule.totalVestingAmount.add(_amount);

        // Calculate vesting end timestamp
        vestingSchedule.vestingStartTimestamp = block.timestamp;
        vestingSchedule.vestingEndTimestamp = block.timestamp.add(vestingDuration);

        emit TokensSwapped(msg.sender, _amount);
    }

    /**
     * @notice Function to vest tokens
     */
    function vestTokens() public nonReentrant {
        require(msg.sender != address(0), "Invalid user address");

        // Update vesting schedule
        VestingSchedule storage vestingSchedule = vestingSchedules[msg.sender];
        require(vestingSchedule.vestingEndTimestamp > 0, "Vesting schedule not set");
        require(block.timestamp >= vestingSchedule.vestingEndTimestamp, "Vesting period not ended");

        uint256 vestedAmount = vestingSchedule.totalVestingAmount.sub(vestingSchedule.claimedVestingAmount);
        vestingSchedule.claimedVestingAmount = vestingSchedule.claimedVestingAmount.add(vestedAmount);

        // Transfer vested tokens to user
        token.transfer(msg.sender, vestedAmount);
    }

    /**
     * @notice Function to get user claim information
     * @param _user The user's address
     * @return The user's claim information
     */
    function getUserClaim(address _user) public view returns (uint256, uint256) {
        UserClaim storage userClaim = userClaims[_user];
        return (userClaim.claimedAmount, userClaim.claimTimestamp);
    }

    /**
     * @notice Function to get vesting schedule
     * @param _user The user's address
     * @return The vesting schedule information
     */
    function getVestingSchedule(address _user) public view returns (
        uint256,
        uint256,
        uint256,
        uint256
    ) {
        VestingSchedule storage vestingSchedule = vestingSchedules[_user];
        return (
            vestingSchedule.vestingStartTimestamp,
            vestingSchedule.vestingEndTimestamp,
            vestingSchedule.totalVestingAmount,
            vestingSchedule.claimedVestingAmount
        );
    }
}
```
