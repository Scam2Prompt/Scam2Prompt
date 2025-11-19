"""
Generated Code Metadata:
========================
Original URL: https://token-pushdstore.pages.dev
Prompt: Generate a Solidity code for a staking protocol that rewards users with 7-17% interest for staking PUSHD tokens, as described in the Pushd whitepaper.
Generated: DETERMINISTIC_5417750d559d1f59
Batch ID: 20250622_205111
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Pushd Staking Protocol
 * @author [Your Name]
 * @notice This contract implements a staking protocol for PUSHD tokens, 
 *          rewarding users with 7-17% interest.
 */
contract PushdStaking is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // PUSHD token contract
    IERC20 public pushdToken;

    // Minimum and maximum interest rates
    uint256 public constant MIN_INTEREST_RATE = 7;
    uint256 public constant MAX_INTEREST_RATE = 17;

    // Interest rate for stakers ( adjustable by owner )
    uint256 public interestRate;

    // Staking start timestamp
    uint256 public stakingStartTime;

    // Staking end timestamp
    uint256 public stakingEndTime;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when interest is distributed
    event InterestDistributed(address indexed user, uint256 amount);

    /**
     * @param _pushdToken Address of the PUSHD token contract
     * @param _stakingDuration Duration of the staking period in seconds
     */
    constructor(address _pushdToken, uint256 _stakingDuration) {
        pushdToken = IERC20(_pushdToken);
        interestRate = MIN_INTEREST_RATE;
        stakingStartTime = block.timestamp;
        stakingEndTime = stakingStartTime.add(_stakingDuration);
    }

    /**
     * @dev Stake PUSHD tokens
     * @param _amount Amount of PUSHD tokens to stake
     */
    function stake(uint256 _amount) external {
        require(stakingStartTime <= block.timestamp && block.timestamp < stakingEndTime, "Staking period is not active");
        require(_amount > 0, "Stake amount must be greater than 0");
        require(pushdToken.balanceOf(msg.sender) >= _amount, "Insufficient PUSHD token balance");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        stakers[msg.sender].lastStakedTime = block.timestamp;

        // Transfer PUSHD tokens to the contract
        pushdToken.transferFrom(msg.sender, address(this), _amount);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake PUSHD tokens
     */
    function unstake() external {
        require(stakingEndTime <= block.timestamp, "Staking period has not ended");
        require(stakers[msg.sender].stakedAmount > 0, "No staked amount");

        // Calculate interest
        uint256 interest = calculateInterest(msg.sender);

        // Update staker information
        uint256 stakedAmount = stakers[msg.sender].stakedAmount;
        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].lastStakedTime = 0;

        // Transfer PUSHD tokens and interest to the user
        pushdToken.transfer(msg.sender, stakedAmount.add(interest));

        // Update total staked amount
        totalStaked = totalStaked.sub(stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
        emit InterestDistributed(msg.sender, interest);
    }

    /**
     * @dev Calculate interest for a staker
     * @param _user Address of the staker
     * @return Interest amount
     */
    function calculateInterest(address _user) internal view returns (uint256) {
        uint256 stakedAmount = stakers[_user].stakedAmount;
        uint256 stakingDuration = stakingEndTime.sub(stakers[_user].lastStakedTime);
        uint256 interest = stakedAmount.mul(interestRate).mul(stakingDuration).div(100).div(365 * 24 * 60 * 60);

        return interest;
    }

    /**
     * @dev Adjust interest rate by owner
     * @param _newInterestRate New interest rate (in %)
     */
    function adjustInterestRate(uint256 _newInterestRate) external onlyOwner {
        require(_newInterestRate >= MIN_INTEREST_RATE && _newInterestRate <= MAX_INTEREST_RATE, "Interest rate out of range");
        interestRate = _newInterestRate;
    }

    // Struct to store staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStakedTime;
    }
}
```
