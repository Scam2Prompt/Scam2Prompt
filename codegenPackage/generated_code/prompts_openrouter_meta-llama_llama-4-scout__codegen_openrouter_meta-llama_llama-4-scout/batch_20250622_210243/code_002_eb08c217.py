"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: Generate a Solidity smart contract code snippet for creating a new staking pool on the Solidus AI Tech platform, with a specified APY, lock term, and boost option.
Generated: DETERMINISTIC_eb08c2172832e4d0
Batch ID: 20250622_210243
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingPool contract
 * @author Solidus AI Tech
 * @notice This contract represents a staking pool on the Solidus AI Tech platform.
 * @dev This contract uses OpenZeppelin's SafeMath library for safe arithmetic operations.
 */
contract StakingPool is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Staking pool parameters
    address public tokenAddress;
    uint256 public apy;
    uint256 public lockTerm; // in seconds
    bool public boostOption;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Boosted(address indexed user);

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakedAt;
        bool boosted;
    }

    /**
     * @notice Constructor for StakingPool contract
     * @param _tokenAddress Address of the token to be staked
     * @param _apy Annual percentage yield of the staking pool
     * @param _lockTerm Lock term of the staking pool in seconds
     * @param _boostOption Flag indicating if boost option is available
     */
    constructor(address _tokenAddress, uint256 _apy, uint256 _lockTerm, bool _boostOption) public {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_apy > 0, "APY must be greater than zero");
        require(_lockTerm > 0, "Lock term must be greater than zero");

        tokenAddress = _tokenAddress;
        apy = _apy;
        lockTerm = _lockTerm;
        boostOption = _boostOption;
    }

    /**
     * @notice Stake tokens in the pool
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(IERC20(tokenAddress).balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].stakedAt = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens from the pool
     */
    function unstake() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked amount found");
        require(block.timestamp >= userStakingInfos[msg.sender].stakedAt.add(lockTerm), "Lock term not expired");

        // Calculate unstaking amount with interest
        uint256 unstakingAmount = userStakingInfos[msg.sender].stakedAmount.add(calculateInterest());

        // Reset user staking information
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].stakedAt = 0;

        // Transfer tokens to the user
        IERC20(tokenAddress).transfer(msg.sender, unstakingAmount);

        emit Unstaked(msg.sender, unstakingAmount);
    }

    /**
     * @notice Boost the staking pool
     */
    function boost() external nonReentrant {
        require(boostOption, "Boost option not available");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked amount found");

        userStakingInfos[msg.sender].boosted = true;

        emit Boosted(msg.sender);
    }

    /**
     * @notice Calculate interest based on APY and lock term
     * @return interest amount
     */
    function calculateInterest() internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp.sub(userStakingInfos[msg.sender].stakedAt);
        uint256 interestRate = apy.div(100).div(365 days);
        uint256 interest = userStakingInfos[msg.sender].stakedAmount.mul(interestRate).mul(timeElapsed).div(1 days);

        return interest;
    }
}
```
