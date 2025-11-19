"""
Generated Code Metadata:
========================
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: Create a Solidity smart contract to facilitate token-based interactions between users and developers on the AGIX AI Marketplace, ensuring proportional rewards for contributors.
Generated: DETERMINISTIC_6cf4c5b680751eb4
Batch ID: 20250612_152954
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";

/**
 * @title AGIX AI Marketplace Token Contract
 * @author [Your Name]
 * @notice This contract facilitates token-based interactions between users and developers on the AGIX AI Marketplace.
 */
contract AGIXToken {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user addresses to their contribution amounts
    mapping(address => uint256) public userContributions;

    // Mapping of developer addresses to their reward amounts
    mapping(address => uint256) public developerRewards;

    // Total contribution amount
    uint256 public totalContributions;

    // Total reward amount
    uint256 public totalRewards;

    // AGIX token instance
    IERC20 public agixToken;

    // Address of the AGIX token
    address public agixTokenAddress;

    // Percentage of rewards for developers
    uint256 public developerRewardPercentage;

    /**
     * @notice Constructor for the AGIXToken contract
     * @param _agixTokenAddress Address of the AGIX token
     * @param _developerRewardPercentage Percentage of rewards for developers
     */
    constructor(address _agixTokenAddress, uint256 _developerRewardPercentage) public {
        require(_agixTokenAddress != address(0), "Invalid AGIX token address");
        require(_developerRewardPercentage > 0 && _developerRewardPercentage <= 100, "Invalid developer reward percentage");

        agixTokenAddress = _agixTokenAddress;
        agixToken = IERC20(_agixTokenAddress);
        developerRewardPercentage = _developerRewardPercentage;
    }

    /**
     * @notice Allows users to contribute to the platform
     * @param _amount Amount of AGIX tokens to contribute
     */
    function contribute(uint256 _amount) public {
        require(_amount > 0, "Contribution amount must be greater than 0");
        require(agixToken.balanceOf(msg.sender) >= _amount, "Insufficient AGIX token balance");

        // Transfer AGIX tokens from user to the contract
        agixToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's contribution amount
        userContributions[msg.sender] = userContributions[msg.sender].add(_amount);

        // Update total contribution amount
        totalContributions = totalContributions.add(_amount);
    }

    /**
     * @notice Allows developers to claim their rewards
     */
    function claimReward() public {
        // Calculate developer's reward amount
        uint256 rewardAmount = calculateReward(msg.sender);

        require(rewardAmount > 0, "No rewards to claim");

        // Update developer's reward amount
        developerRewards[msg.sender] = 0;

        // Transfer AGIX tokens from the contract to the developer
        agixToken.safeTransfer(msg.sender, rewardAmount);
    }

    /**
     * @notice Calculates a developer's reward amount
     * @param _developer Address of the developer
     * @return Reward amount for the developer
     */
    function calculateReward(address _developer) internal view returns (uint256) {
        // Calculate total reward amount
        uint256 _totalRewardAmount = totalContributions.mul(developerRewardPercentage).div(100);

        // Calculate developer's reward amount
        uint256 rewardAmount = _totalRewardAmount.mul(developerRewards[_developer]).div(totalContributions);

        return rewardAmount;
    }

    /**
     * @notice Updates a developer's reward amount
     * @param _developer Address of the developer
     * @param _amount Amount of rewards to add
     */
    function updateDeveloperReward(address _developer, uint256 _amount) public onlyOwner {
        require(_developer != address(0), "Invalid developer address");
        require(_amount > 0, "Reward amount must be greater than 0");

        developerRewards[_developer] = developerRewards[_developer].add(_amount);
    }

    /**
     * @notice Updates the developer reward percentage
     * @param _newPercentage New percentage of rewards for developers
     */
    function updateDeveloperRewardPercentage(uint256 _newPercentage) public onlyOwner {
        require(_newPercentage > 0 && _newPercentage <= 100, "Invalid developer reward percentage");

        developerRewardPercentage = _newPercentage;
    }
}
```
