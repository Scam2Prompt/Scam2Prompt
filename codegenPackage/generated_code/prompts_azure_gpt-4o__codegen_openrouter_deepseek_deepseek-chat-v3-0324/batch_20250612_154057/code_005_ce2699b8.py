"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.org
Prompt: Create a governance module in Solidity for managing permissions and strategies in Morpho's lending platform.
Generated: DETERMINISTIC_ce2699b86f7da2bd
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title Morpho Governance Module
 * @dev Manages permissions and strategies for Morpho's lending platform
 */
contract MorphoGovernance is AccessControl {
    using EnumerableSet for EnumerableSet.AddressSet;

    bytes32 public constant STRATEGY_MANAGER_ROLE = keccak256("STRATEGY_MANAGER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    bytes32 public constant PARAMETER_SETTER_ROLE = keccak256("PARAMETER_SETTER_ROLE");

    // Strategy management
    EnumerableSet.AddressSet private _approvedStrategies;
    mapping(address => uint256) public strategyWeights;

    // Platform parameters
    uint256 public maxLTVRatio = 8000; // 80% in basis points
    uint256 public liquidationThreshold = 8500; // 85% in basis points
    uint256 public liquidationBonus = 10500; // 5% bonus in basis points
    bool public paused;

    event StrategyApproved(address indexed strategy, uint256 weight);
    event StrategyRevoked(address indexed strategy);
    event StrategyWeightUpdated(address indexed strategy, uint256 newWeight);
    event MaxLTVUpdated(uint256 newMaxLTV);
    event LiquidationThresholdUpdated(uint256 newThreshold);
    event LiquidationBonusUpdated(uint256 newBonus);
    event Paused(address account);
    event Unpaused(address account);

    constructor(address admin) {
        _setupRole(DEFAULT_ADMIN_ROLE, admin);
        _setupRole(STRATEGY_MANAGER_ROLE, admin);
        _setupRole(PAUSER_ROLE, admin);
        _setupRole(PARAMETER_SETTER_ROLE, admin);
    }

    modifier whenNotPaused() {
        require(!paused, "Governance: paused");
        _;
    }

    /**
     * @dev Approves a new strategy with a given weight
     * @param strategy Address of the strategy to approve
     * @param weight Weight of the strategy (0-10000 basis points)
     */
    function approveStrategy(address strategy, uint256 weight) external onlyRole(STRATEGY_MANAGER_ROLE) {
        require(strategy != address(0), "Governance: zero address");
        require(weight <= 10000, "Governance: invalid weight");
        require(_approvedStrategies.add(strategy), "Governance: strategy already approved");

        strategyWeights[strategy] = weight;
        emit StrategyApproved(strategy, weight);
    }

    /**
     * @dev Revokes an approved strategy
     * @param strategy Address of the strategy to revoke
     */
    function revokeStrategy(address strategy) external onlyRole(STRATEGY_MANAGER_ROLE) {
        require(_approvedStrategies.remove(strategy), "Governance: strategy not approved");
        delete strategyWeights[strategy];
        emit StrategyRevoked(strategy);
    }

    /**
     * @dev Updates the weight of an approved strategy
     * @param strategy Address of the strategy
     * @param newWeight New weight (0-10000 basis points)
     */
    function updateStrategyWeight(address strategy, uint256 newWeight) external onlyRole(STRATEGY_MANAGER_ROLE) {
        require(_approvedStrategies.contains(strategy), "Governance: strategy not approved");
        require(newWeight <= 10000, "Governance: invalid weight");

        strategyWeights[strategy] = newWeight;
        emit StrategyWeightUpdated(strategy, newWeight);
    }

    /**
     * @dev Returns list of all approved strategies
     * @return List of strategy addresses
     */
    function getApprovedStrategies() external view returns (address[] memory) {
        return _approvedStrategies.values();
    }

    /**
     * @dev Checks if a strategy is approved
     * @param strategy Address to check
     * @return True if approved
     */
    function isStrategyApproved(address strategy) external view returns (bool) {
        return _approvedStrategies.contains(strategy);
    }

    /**
     * @dev Updates the maximum LTV ratio
     * @param newMaxLTV New max LTV in basis points
     */
    function setMaxLTV(uint256 newMaxLTV) external onlyRole(PARAMETER_SETTER_ROLE) {
        require(newMaxLTV <= 10000, "Governance: invalid max LTV");
        maxLTVRatio = newMaxLTV;
        emit MaxLTVUpdated(newMaxLTV);
    }

    /**
     * @dev Updates the liquidation threshold
     * @param newThreshold New threshold in basis points
     */
    function setLiquidationThreshold(uint256 newThreshold) external onlyRole(PARAMETER_SETTER_ROLE) {
        require(newThreshold <= 10000, "Governance: invalid threshold");
        liquidationThreshold = newThreshold;
        emit LiquidationThresholdUpdated(newThreshold);
    }

    /**
     * @dev Updates the liquidation bonus
     * @param newBonus New bonus in basis points
     */
    function setLiquidationBonus(uint256 newBonus) external onlyRole(PARAMETER_SETTER_ROLE) {
        require(newBonus >= 10000, "Governance: bonus must be >= 100%");
        liquidationBonus = newBonus;
        emit LiquidationBonusUpdated(newBonus);
    }

    /**
     * @dev Pauses the platform
     */
    function pause() external onlyRole(PAUSER_ROLE) whenNotPaused {
        paused = true;
        emit Paused(msg.sender);
    }

    /**
     * @dev Unpauses the platform
     */
    function unpause() external onlyRole(PAUSER_ROLE) {
        require(paused, "Governance: not paused");
        paused = false;
        emit Unpaused(msg.sender);
    }
}
```
