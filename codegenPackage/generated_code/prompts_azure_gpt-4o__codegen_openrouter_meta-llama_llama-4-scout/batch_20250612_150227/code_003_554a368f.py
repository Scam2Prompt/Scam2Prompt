"""
Generated Code Metadata:
========================
Original URL: https://xn--thrster-p2a.finance
Prompt: Write a smart contract that utilizes Thruster Finance's Thruster Treasure feature to reward active traders with additional incentives.
Generated: DETERMINISTIC_554a368fd0b5347e
Batch ID: 20250612_150227
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Thruster Treasure Contract
 * @author [Your Name]
 * @notice This contract utilizes Thruster Finance's Thruster Treasure feature to reward active traders with additional incentives.
 */
contract ThrusterTreasure is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of trader addresses to their trading volumes
    mapping(address => uint256) public tradingVolumes;

    // Mapping of trader addresses to their reward balances
    mapping(address => uint256) public rewardBalances;

    // Address of the Thruster Finance token
    address public thrusterToken;

    // Address of the reward token
    address public rewardToken;

    // Thruster Finance's router contract address
    address public router;

    // Percentage of trading volume to be rewarded
    uint256 public rewardPercentage;

    // Event emitted when a trader's trading volume is updated
    event TradingVolumeUpdated(address indexed trader, uint256 volume);

    // Event emitted when a trader's reward balance is updated
    event RewardBalanceUpdated(address indexed trader, uint256 balance);

    /**
     * @notice Constructor function
     * @param _thrusterToken Address of the Thruster Finance token
     * @param _rewardToken Address of the reward token
     * @param _router Thruster Finance's router contract address
     * @param _rewardPercentage Percentage of trading volume to be rewarded
     */
    constructor(
        address _thrusterToken,
        address _rewardToken,
        address _router,
        uint256 _rewardPercentage
    ) {
        require(_thrusterToken != address(0), "Thruster token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_router != address(0), "Router address cannot be zero");
        require(_rewardPercentage > 0, "Reward percentage must be greater than zero");

        thrusterToken = _thrusterToken;
        rewardToken = _rewardToken;
        router = _router;
        rewardPercentage = _rewardPercentage;
    }

    /**
     * @notice Updates a trader's trading volume
     * @param _trader Address of the trader
     * @param _volume Trading volume of the trader
     */
    function updateTradingVolume(address _trader, uint256 _volume) external {
        require(msg.sender == router, "Only the router contract can update trading volumes");
        require(_trader != address(0), "Trader address cannot be zero");
        require(_volume > 0, "Trading volume must be greater than zero");

        tradingVolumes[_trader] = tradingVolumes[_trader].add(_volume);
        emit TradingVolumeUpdated(_trader, tradingVolumes[_trader]);

        // Calculate and update the trader's reward balance
        uint256 reward = _volume.mul(rewardPercentage).div(100);
        rewardBalances[_trader] = rewardBalances[_trader].add(reward);
        emit RewardBalanceUpdated(_trader, rewardBalances[_trader]);
    }

    /**
     * @notice Claims a trader's reward
     * @param _trader Address of the trader
     */
    function claimReward(address _trader) external nonReentrant {
        require(_trader != address(0), "Trader address cannot be zero");
        require(rewardBalances[_trader] > 0, "Trader has no reward balance");

        uint256 reward = rewardBalances[_trader];
        rewardBalances[_trader] = 0;
        emit RewardBalanceUpdated(_trader, 0);

        IERC20(rewardToken).safeTransfer(_trader, reward);
    }

    /**
     * @notice Updates the reward percentage
     * @param _newPercentage New reward percentage
     */
    function updateRewardPercentage(uint256 _newPercentage) external {
        require(msg.sender == owner(), "Only the owner can update the reward percentage");
        require(_newPercentage > 0, "Reward percentage must be greater than zero");

        rewardPercentage = _newPercentage;
    }

    /**
     * @notice Transfers ownership of the contract
     * @param _newOwner New owner address
     */
    function transferOwnership(address _newOwner) external {
        require(msg.sender == owner(), "Only the owner can transfer ownership");
        require(_newOwner != address(0), "New owner address cannot be zero");

        // Implement ownership transfer logic here
    }

    // Owner of the contract
    address private _owner;

    /**
     * @notice Returns the owner of the contract
     * @return address Owner address
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @notice Modifier to restrict access to the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "Only the owner can perform this action");
        _;
    }
}
```
