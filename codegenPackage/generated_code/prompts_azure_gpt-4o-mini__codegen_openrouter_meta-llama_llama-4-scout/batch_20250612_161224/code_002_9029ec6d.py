"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Can you provide an example of a smart contract that manages a drawing system for a web3 platform, inspired by the dual incentivization model used by Everyworld?
Generated: DETERMINISTIC_9029ec6d4d0c176f
Batch ID: 20250612_161224
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
 * @title DrawingSystemSmartContract
 * @author [Your Name]
 * @notice A smart contract for managing a drawing system inspired by Everyworld's dual incentivization model.
 */
contract DrawingSystemSmartContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user addresses to their respective points balances
    mapping(address => uint256) public userPoints;

    // Mapping of user addresses to their respective participation status
    mapping(address => bool) public userParticipated;

    // Total points accumulated in the system
    uint256 public totalPoints;

    // Total rewards allocated to the system
    uint256 public totalRewards;

    // Address of the reward token
    address public rewardTokenAddress;

    // Event emitted when a user earns points
    event PointsEarned(address indexed user, uint256 points);

    // Event emitted when a user redeems rewards
    event RewardsRedeemed(address indexed user, uint256 rewards);

    /**
     * @notice Initializes the contract with the reward token address
     * @param _rewardTokenAddress Address of the reward token
     */
    constructor(address _rewardTokenAddress) public {
        require(_rewardTokenAddress != address(0), "Reward token address cannot be zero");
        rewardTokenAddress = _rewardTokenAddress;
    }

    /**
     * @notice Allows users to earn points by participating in the drawing system
     * @param _points Points to be earned by the user
     */
    function earnPoints(uint256 _points) public {
        require(_points > 0, "Points must be greater than zero");
        userPoints[msg.sender] = userPoints[msg.sender].add(_points);
        totalPoints = totalPoints.add(_points);
        userParticipated[msg.sender] = true;
        emit PointsEarned(msg.sender, _points);
    }

    /**
     * @notice Allows users to redeem rewards based on their points balance
     * @param _rewardsAmount Amount of rewards to be redeemed
     */
    function redeemRewards(uint256 _rewardsAmount) public nonReentrant {
        require(userPoints[msg.sender] > 0, "User has no points to redeem");
        require(_rewardsAmount > 0, "Rewards amount must be greater than zero");

        uint256 userRewardShare = userPoints[msg.sender].mul(totalRewards).div(totalPoints);
        require(userRewardShare >= _rewardsAmount, "Insufficient rewards");

        userPoints[msg.sender] = 0;
        totalPoints = totalPoints.sub(userPoints[msg.sender]);

        IERC20(rewardTokenAddress).transfer(msg.sender, _rewardsAmount);
        totalRewards = totalRewards.sub(_rewardsAmount);

        emit RewardsRedeemed(msg.sender, _rewardsAmount);
    }

    /**
     * @notice Allows the contract owner to allocate rewards to the system
     * @param _rewardsAmount Amount of rewards to be allocated
     */
    function allocateRewards(uint256 _rewardsAmount) public onlyOwner {
        require(_rewardsAmount > 0, "Rewards amount must be greater than zero");
        IERC20(rewardTokenAddress).transferFrom(msg.sender, address(this), _rewardsAmount);
        totalRewards = totalRewards.add(_rewardsAmount);
    }

    // Restrict function to only be callable by the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Get the contract owner
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
