"""
Generated Code Metadata:
========================
Original URL: https://wwwstayloud.io
Prompt: Provide code to integrate Meteora's fee split mechanism into a decentralized application (dApp) for managing Loud rewards.
Generated: DETERMINISTIC_6ee12eb5b32c5d4d
Batch ID: 20250612_154057
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LoudRewards
 * @dev A smart contract to manage Loud rewards with a fee split mechanism.
 */
contract LoudRewards is Ownable {
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);
    
    // Event emitted when fees are split
    event FeesSplit(address indexed recipient, uint256 amount);

    // Token used for rewards
    IERC20 public rewardToken;

    // Fee recipient addresses
    address payable public feeRecipient1;
    address payable public feeRecipient2;

    // Fee percentage (in basis points, e.g., 100 = 1%)
    uint256 public feePercentage;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    /**
     * @dev Constructor to initialize the contract with the reward token and fee recipients.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     * @param _feeRecipient1 Address of the first fee recipient.
     * @param _feeRecipient2 Address of the second fee recipient.
     * @param _feePercentage Fee percentage in basis points.
     */
    constructor(
        address _rewardToken,
        address payable _feeRecipient1,
        address payable _feeRecipient2,
        uint256 _feePercentage
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_feeRecipient1 != address(0), "Invalid fee recipient 1 address");
        require(_feeRecipient2 != address(0), "Invalid fee recipient 2 address");
        require(_feePercentage <= 10000, "Fee percentage must be <= 100%");

        rewardToken = IERC20(_rewardToken);
        feeRecipient1 = _feeRecipient1;
        feeRecipient2 = _feeRecipient2;
        feePercentage = _feePercentage;
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param user Address of the user to receive rewards.
     * @param amount Amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward balance");

        // Calculate fees
        uint256 feeAmount = (amount * feePercentage) / 10000;
        uint256 netAmount = amount - feeAmount;

        // Update user rewards
        userRewards[user] += netAmount;

        // Transfer fees to recipients
        rewardToken.transfer(feeRecipient1, feeAmount / 2);
        rewardToken.transfer(feeRecipient2, feeAmount / 2);
        emit FeesSplit(feeRecipient1, feeAmount / 2);
        emit FeesSplit(feeRecipient2, feeAmount / 2);

        // Transfer net rewards to user
        rewardToken.transfer(user, netAmount);
        emit RewardsDistributed(user, netAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        rewardToken.transfer(owner(), amount);
    }

    /**
     * @dev Function to update fee recipients.
     * @param _feeRecipient1 New address for the first fee recipient.
     * @param _feeRecipient2 New address for the second fee recipient.
     */
    function updateFeeRecipients(address payable _feeRecipient1, address payable _feeRecipient2) external onlyOwner {
        require(_feeRecipient1 != address(0), "Invalid fee recipient 1 address");
        require(_feeRecipient2 != address(0), "Invalid fee recipient 2 address");

        feeRecipient1 = _feeRecipient1;
        feeRecipient2 = _feeRecipient2;
    }

    /**
     * @dev Function to update the fee percentage.
     * @param _feePercentage New fee percentage in basis points.
     */
    function updateFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 10000, "Fee percentage must be <= 100%");
        feePercentage = _feePercentage;
    }
}
```
