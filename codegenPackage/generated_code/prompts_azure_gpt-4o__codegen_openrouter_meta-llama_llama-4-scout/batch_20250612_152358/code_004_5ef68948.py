"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaww6ymqhro76hrjq6l5h4ninbd2hn7ysd6vsyffswhvg5btz4vb4.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that supports EigenLayer's "Restake" feature and adheres to its staking requirements.
Generated: DETERMINISTIC_5ef6894848479993
Batch ID: 20250612_152358
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
 * @title EigenLayer Restake Contract
 * @author [Your Name]
 * @notice This contract supports EigenLayer's "Restake" feature and adheres to its staking requirements.
 */
contract EigenLayerRestake {
    using SafeMath for uint256;

    // Mapping of user addresses to their restake information
    mapping(address => RestakeInfo) public restakeInfo;

    // Mapping of strategy addresses to their corresponding weights
    mapping(address => uint256) public strategyWeights;

    // Mapping of strategy addresses to their corresponding restake pools
    mapping(address => address) public strategyPools;

    // EigenLayer staking contract address
    address public eigenLayerStaking;

    // Event emitted when a user restakes
    event Restake(address indexed user, address indexed strategy, uint256 amount);

    // Event emitted when a strategy weight is updated
    event StrategyWeightUpdated(address indexed strategy, uint256 weight);

    // Event emitted when a strategy pool is updated
    event StrategyPoolUpdated(address indexed strategy, address pool);

    /**
     * @dev Struct representing a user's restake information
     */
    struct RestakeInfo {
        uint256 restakeAmount;
        address[] strategies;
    }

    /**
     * @dev Constructor for the EigenLayerRestake contract
     * @param _eigenLayerStaking Address of the EigenLayer staking contract
     */
    constructor(address _eigenLayerStaking) {
        eigenLayerStaking = _eigenLayerStaking;
    }

    /**
     * @dev Updates the weight of a strategy
     * @param _strategy Address of the strategy
     * @param _weight New weight of the strategy
     */
    function updateStrategyWeight(address _strategy, uint256 _weight) public {
        require(msg.sender == eigenLayerStaking, "Only EigenLayer staking can update strategy weights");
        strategyWeights[_strategy] = _weight;
        emit StrategyWeightUpdated(_strategy, _weight);
    }

    /**
     * @dev Updates the restake pool of a strategy
     * @param _strategy Address of the strategy
     * @param _pool Address of the new restake pool
     */
    function updateStrategyPool(address _strategy, address _pool) public {
        require(msg.sender == eigenLayerStaking, "Only EigenLayer staking can update strategy pools");
        strategyPools[_strategy] = _pool;
        emit StrategyPoolUpdated(_strategy, _pool);
    }

    /**
     * @dev Restakes a user's funds into a strategy
     * @param _strategy Address of the strategy
     * @param _amount Amount to restake
     */
    function restake(address _strategy, uint256 _amount) public nonReentrant {
        require(strategyWeights[_strategy] > 0, "Strategy weight must be greater than 0");
        require(strategyPools[_strategy] != address(0), "Strategy pool must be set");

        RestakeInfo storage userInfo = restakeInfo[msg.sender];
        userInfo.restakeAmount = userInfo.restakeAmount.add(_amount);
        userInfo.strategies.push(_strategy);

        // Transfer funds to the strategy pool
        IERC20(eigenLayerStaking).transferFrom(msg.sender, strategyPools[_strategy], _amount);

        emit Restake(msg.sender, _strategy, _amount);
    }

    /**
     * @dev Claims restake rewards for a user
     * @param _strategy Address of the strategy
     * @return Rewards claimed by the user
     */
    function claimRewards(address _strategy) public nonReentrant returns (uint256) {
        // Implement reward claiming logic here
        // For demonstration purposes, assume rewards are 0
        return 0;
    }

    /**
     * @dev Reverts if called with a non-zero value
     */
    fallback() external payable {
        revert("This contract does not accept Ether");
    }

    /**
     * @dev Reverts if called with a non-zero value
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
