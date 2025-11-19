"""
Generated Code Metadata:
========================
Original URL: https://btfdbull.pages.dev
Prompt: Write a Solidity smart contract for handling the vesting of staked $BTFD tokens and rewards, ensuring tokens are locked for a set period before becoming claimable.
Generated: DETERMINISTIC_e93bf34789994589
Batch ID: 20250612_154236
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BTFDVestingContract
 * @author [Your Name]
 * @notice Handles the vesting of staked $BTFD tokens and rewards.
 */
contract BTFDVestingContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Mapping of claimable rewards
    mapping(address => uint256) public claimableRewards;

    // IERC20 token instance for $BTFD
    IERC20 public btfdtToken;

    // IERC20 token instance for reward token
    IERC20 public rewardToken;

    // Duration for which tokens are locked before becoming claimable
    uint256 public vestingDuration;

    // Timestamp when the contract was deployed
    uint256 public deploymentTimestamp;

    /**
     * @dev Event emitted when a new vesting schedule is created
     * @param account Address of the account
     * @param startTimestamp Timestamp when vesting starts
     * @param duration Vesting duration
     * @param amount Amount of tokens to vest
     */
    event NewVestingSchedule(address indexed account, uint256 startTimestamp, uint256 duration, uint256 amount);

    /**
     * @dev Event emitted when tokens are claimed
     * @param account Address of the account
     * @param amount Amount of tokens claimed
     */
    event TokensClaimed(address indexed account, uint256 amount);

    /**
     * @dev Event emitted when rewards are claimed
     * @param account Address of the account
     * @param amount Amount of rewards claimed
     */
    event RewardsClaimed(address indexed account, uint256 amount);

    /**
     * @param _btfdtToken Address of the $BTFD token
     * @param _rewardToken Address of the reward token
     * @param _vestingDuration Duration for which tokens are locked
     */
    constructor(address _btfdtToken, address _rewardToken, uint256 _vestingDuration) {
        btfdtToken = IERC20(_btfdtToken);
        rewardToken = IERC20(_rewardToken);
        vestingDuration = _vestingDuration;
        deploymentTimestamp = block.timestamp;
    }

    /**
     * @dev Creates a new vesting schedule for an account
     * @param account Address of the account
     * @param amount Amount of tokens to vest
     */
    function createVestingSchedule(address account, uint256 amount) public {
        require(msg.sender == address(this) || msg.sender == account, "Only the contract or the account can create a vesting schedule");

        // Check if account already has a vesting schedule
        require(vestingSchedules[account].startTimestamp == 0, "Account already has a vesting schedule");

        // Calculate start timestamp
        uint256 startTimestamp = block.timestamp;

        // Create vesting schedule
        vestingSchedules[account] = VestingSchedule({
            startTimestamp: startTimestamp,
            duration: vestingDuration,
            amount: amount,
            claimed: 0
        });

        // Transfer tokens to the contract
        btfdtToken.safeTransferFrom(account, address(this), amount);

        emit NewVestingSchedule(account, startTimestamp, vestingDuration, amount);
    }

    /**
     * @dev Claims tokens for an account
     */
    function claimTokens() public {
        address account = msg.sender;
        VestingSchedule storage schedule = vestingSchedules[account];

        require(schedule.startTimestamp != 0, "Account does not have a vesting schedule");

        // Calculate claimable tokens
        uint256 claimableTokens = calculateClaimableTokens(account);

        require(claimableTokens > 0, "No tokens to claim");

        // Update claimed tokens
        schedule.claimed = schedule.claimed.add(claimableTokens);

        // Transfer tokens to the account
        btfdtToken.safeTransfer(account, claimableTokens);

        emit TokensClaimed(account, claimableTokens);
    }

    /**
     * @dev Claims rewards for an account
     * @param amount Amount of rewards to claim
     */
    function claimRewards(uint256 amount) public {
        address account = msg.sender;

        require(claimableRewards[account] >= amount, "Not enough rewards to claim");

        // Update claimable rewards
        claimableRewards[account] = claimableRewards[account].sub(amount);

        // Transfer rewards to the account
        rewardToken.safeTransfer(account, amount);

        emit RewardsClaimed(account, amount);
    }

    /**
     * @dev Calculates claimable tokens for an account
     * @param account Address of the account
     * @return Claimable tokens
     */
    function calculateClaimableTokens(address account) internal view returns (uint256) {
        VestingSchedule storage schedule = vestingSchedules[account];

        // Calculate vesting end timestamp
        uint256 vestingEndTimestamp = schedule.startTimestamp.add(schedule.duration);

        // Check if vesting period has ended
        if (block.timestamp >= vestingEndTimestamp) {
            return schedule.amount.sub(schedule.claimed);
        } else {
            // Calculate claimable tokens based on time elapsed
            uint256 timeElapsed = block.timestamp.sub(schedule.startTimestamp);
            uint256 claimableTokens = schedule.amount.mul(timeElapsed).div(schedule.duration).sub(schedule.claimed);

            return claimableTokens;
        }
    }

    /**
     * @dev Updates claimable rewards for an account
     * @param account Address of the account
     * @param amount Amount of rewards
     */
    function updateClaimableRewards(address account, uint256 amount) external {
        require(msg.sender == address(this), "Only the contract can update claimable rewards");

        claimableRewards[account] = claimableRewards[account].add(amount);
    }

    /**
     * @dev Vesting schedule structure
     */
    struct VestingSchedule {
        uint256 startTimestamp;
        uint256 duration;
        uint256 amount;
        uint256 claimed;
    }
}
```
