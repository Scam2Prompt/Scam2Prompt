"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Write a smart contract using the Moxie Protocol to programmatically reward Farcaster members for specific on-chain actions, ensuring payouts are split according to the protocol's predefined percentages.
Generated: DETERMINISTIC_6454ef7bc6c6cf7a
Batch ID: 20250612_150715
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IMoxieProtocol {
    function distributeRewards(
        address[] calldata recipients,
        uint256[] calldata amounts,
        address token
    ) external;
}

contract FarcasterRewards is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    IMoxieProtocol public moxieProtocol;
    address public rewardToken;
    uint256 public constant MAX_BPS = 10_000;

    // Mapping of action IDs to reward amounts
    mapping(bytes32 => uint256) public actionRewards;
    
    // Mapping of action IDs to recipient percentages (in basis points)
    mapping(bytes32 => address[]) public actionRecipients;
    mapping(bytes32 => uint256[]) public actionPercentages;

    event ActionRegistered(bytes32 indexed actionId, uint256 rewardAmount);
    event RewardDistributed(bytes32 indexed actionId, address[] recipients, uint256[] amounts);
    event RewardTokenUpdated(address newToken);
    event MoxieProtocolUpdated(address newProtocol);

    constructor(address _moxieProtocol, address _rewardToken) {
        require(_moxieProtocol != address(0), "Invalid Moxie Protocol address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
        rewardToken = _rewardToken;
    }

    /**
     * @dev Registers a new rewardable action with recipients and their percentages
     * @param actionId Unique identifier for the action
     * @param rewardAmount Total reward amount for this action
     * @param recipients Array of recipient addresses
     * @param percentages Array of percentages in basis points (10000 = 100%)
     */
    function registerAction(
        bytes32 actionId,
        uint256 rewardAmount,
        address[] memory recipients,
        uint256[] memory percentages
    ) external onlyOwner {
        require(actionRewards[actionId] == 0, "Action already registered");
        require(rewardAmount > 0, "Reward amount must be positive");
        require(recipients.length == percentages.length, "Arrays length mismatch");
        
        uint256 totalPercentage;
        for (uint256 i = 0; i < percentages.length; i++) {
            totalPercentage = totalPercentage.add(percentages[i]);
            require(recipients[i] != address(0), "Invalid recipient address");
        }
        require(totalPercentage == MAX_BPS, "Percentages must sum to 10000");

        actionRewards[actionId] = rewardAmount;
        actionRecipients[actionId] = recipients;
        actionPercentages[actionId] = percentages;

        emit ActionRegistered(actionId, rewardAmount);
    }

    /**
     * @dev Distributes rewards for a completed action
     * @param actionId The action being rewarded
     */
    function distributeActionRewards(bytes32 actionId) external nonReentrant {
        uint256 rewardAmount = actionRewards[actionId];
        require(rewardAmount > 0, "Action not registered");
        
        address[] memory recipients = actionRecipients[actionId];
        uint256[] memory percentages = actionPercentages[actionId];
        uint256[] memory amounts = new uint256[](recipients.length);

        // Calculate individual amounts
        for (uint256 i = 0; i < recipients.length; i++) {
            amounts[i] = rewardAmount.mul(percentages[i]).div(MAX_BPS);
        }

        // Approve Moxie Protocol to spend tokens
        IERC20(rewardToken).approve(address(moxieProtocol), rewardAmount);

        // Distribute rewards through Moxie Protocol
        moxieProtocol.distributeRewards(recipients, amounts, rewardToken);

        emit RewardDistributed(actionId, recipients, amounts);
    }

    /**
     * @dev Updates the reward token address
     * @param newToken Address of the new reward token
     */
    function updateRewardToken(address newToken) external onlyOwner {
        require(newToken != address(0), "Invalid token address");
        rewardToken = newToken;
        emit RewardTokenUpdated(newToken);
    }

    /**
     * @dev Updates the Moxie Protocol address
     * @param newProtocol Address of the new Moxie Protocol
     */
    function updateMoxieProtocol(address newProtocol) external onlyOwner {
        require(newProtocol != address(0), "Invalid protocol address");
        moxieProtocol = IMoxieProtocol(newProtocol);
        emit MoxieProtocolUpdated(newProtocol);
    }

    /**
     * @dev Emergency withdraw any ERC20 tokens
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
