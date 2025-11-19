"""
Generated Code Metadata:
========================
Original URL: https://staking-xprojecterc.pages.dev
Prompt: Develop a staking contract with a customizable locking period and penalty structure, inspired by the X Project Staking platform.
Generated: DETERMINISTIC_11e0b914e68aaff3
Batch ID: 20250622_205709
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
 * @title Staking Contract
 * @author [Your Name]
 * @notice A customizable staking contract with locking period and penalty structure.
 */
contract StakingContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // Staking token
    IERC20 public stakingToken;

    // Locking period in seconds
    uint256 public lockingPeriod;

    // Penalty percentage (in basis points)
    uint256 public penaltyPercentage;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when penalty applied
    event PenaltyApplied(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the staking token
     * @param _lockingPeriod Locking period in seconds
     * @param _penaltyPercentage Penalty percentage (in basis points)
     */
    constructor(
        IERC20 _stakingToken,
        uint256 _lockingPeriod,
        uint256 _penaltyPercentage
    ) {
        require(_lockingPeriod > 0, "Locking period must be greater than 0");
        require(_penaltyPercentage <= 10000, "Penalty percentage must not exceed 100%");

        stakingToken = _stakingToken;
        lockingPeriod = _lockingPeriod;
        penaltyPercentage = _penaltyPercentage;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.lockingEnd = block.timestamp.add(lockingPeriod);

        totalStaked = totalStaked.add(_amount);

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "User has no staked tokens");
        require(staker.lockingEnd <= block.timestamp, "Locking period has not expired");

        uint256 stakedAmount = staker.stakedAmount;
        totalStaked = totalStaked.sub(stakedAmount);

        staker.stakedAmount = 0;
        staker.lockingEnd = 0;

        stakingToken.safeTransfer(msg.sender, stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Apply penalty and unstake tokens
     */
    function applyPenalty() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "User has no staked tokens");
        require(staker.lockingEnd > block.timestamp, "Locking period has expired");

        uint256 penaltyAmount = staker.stakedAmount.mul(penaltyPercentage).div(10000);
        uint256 remainingAmount = staker.stakedAmount.sub(penaltyAmount);

        totalStaked = totalStaked.sub(staker.stakedAmount);

        staker.stakedAmount = 0;
        staker.lockingEnd = 0;

        stakingToken.safeTransfer(msg.sender, remainingAmount);
        stakingToken.safeTransfer(owner(), penaltyAmount);

        emit PenaltyApplied(msg.sender, penaltyAmount);
        emit Unstaked(msg.sender, remainingAmount);
    }

    /**
     * @dev Get staker information
     * @param _user User address
     * @return Staker information
     */
    function getStakerInfo(address _user) external view returns (Staker memory) {
        return stakers[_user];
    }

    // Struct to store staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 lockingEnd;
    }

    // Owner of the contract
    address private owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }
}
```
