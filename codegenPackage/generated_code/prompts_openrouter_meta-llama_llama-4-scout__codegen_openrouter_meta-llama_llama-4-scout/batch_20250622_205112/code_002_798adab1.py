"""
Generated Code Metadata:
========================
Original URL: https://bafybeiedqwx6srzg433ebdrurpgaguzcwborjnz2lsbvn24piyvd3gjysm.ipfs.dweb.link
Prompt: Design a smart contract for staking $ZERO tokens on zkSync, incorporating the 1.5X APR multiplier bonus for the first 48 hours after registration.
Generated: DETERMINISTIC_798adab188494c9e
Batch ID: 20250622_205112
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ZeroTokenStakingContract
 * @author [Your Name]
 * @notice A smart contract for staking $ZERO tokens on zkSync with a 1.5X APR multiplier bonus for the first 48 hours after registration.
 */
contract ZeroTokenStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public zeroToken;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Staking APR
    uint256 public constant BASE_APR = 100; // 100%

    // APR multiplier bonus for the first 48 hours
    uint256 public constant APR_MULTIPLIER_BONUS = 150; // 150%

    // Duration of the APR multiplier bonus
    uint256 public constant APR_MULTIPLIER_BONUS_DURATION = 48 hours;

    // Timestamp when the user registered
    mapping(address => uint256) public userRegistrationTimestamps;

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastUpdateTimestamp;
    }

    /**
     * @notice Constructor
     * @param _zeroTokenAddress Address of the $ZERO token contract
     */
    constructor(address _zeroTokenAddress) {
        require(_zeroTokenAddress != address(0), "ZeroTokenStakingContract: zero token address is zero");
        zeroToken = IERC20(_zeroTokenAddress);
    }

    /**
     * @notice Registers a user for staking
     */
    function register() external {
        require(userRegistrationTimestamps[msg.sender] == 0, "ZeroTokenStakingContract: user already registered");
        userRegistrationTimestamps[msg.sender] = block.timestamp;
    }

    /**
     * @notice Stakes $ZERO tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "ZeroTokenStakingContract: stake amount is zero");
        require(zeroToken.balanceOf(msg.sender) >= _amount, "ZeroTokenStakingContract: user balance is less than stake amount");

        // Update user staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        if (userStakingInfo.stakedAmount > 0) {
            // Calculate and distribute rewards for existing stake
            distributeRewards(msg.sender);
        }

        // Transfer tokens to the contract
        zeroToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.lastUpdateTimestamp = block.timestamp;
    }

    /**
     * @notice Unstakes $ZERO tokens and claims rewards
     */
    function unstake() external {
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        require(userStakingInfo.stakedAmount > 0, "ZeroTokenStakingContract: user stake is zero");

        // Calculate and distribute rewards for existing stake
        distributeRewards(msg.sender);

        // Transfer tokens back to the user
        uint256 stakeAmount = userStakingInfo.stakedAmount;
        userStakingInfo.stakedAmount = 0;
        zeroToken.safeTransfer(msg.sender, stakeAmount);
    }

    /**
     * @notice Calculates and distributes rewards for a user
     * @param _user Address of the user
     */
    function distributeRewards(address _user) internal {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        // Calculate APR with bonus if applicable
        uint256 apr = BASE_APR;
        if (block.timestamp.sub(userRegistrationTimestamps[_user]) <= APR_MULTIPLIER_BONUS_DURATION) {
            apr = APR_MULTIPLIER_BONUS;
        }

        // Calculate rewards
        uint256 rewards = userStakingInfo.stakedAmount.mul(apr).mul(block.timestamp.sub(userStakingInfo.lastUpdateTimestamp)).div(365 * 24 * 60 * 60);

        // Update user staking information
        userStakingInfo.lastUpdateTimestamp = block.timestamp;

        // Transfer rewards to the user
        zeroToken.safeTransfer(_user, rewards);
    }

    /**
     * @notice Withdraws tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "ZeroTokenStakingContract: withdraw amount is zero");
        require(zeroToken.balanceOf(address(this)) >= _amount, "ZeroTokenStakingContract: contract balance is less than withdraw amount");

        zeroToken.safeTransfer(msg.sender, _amount);
    }
}
```
