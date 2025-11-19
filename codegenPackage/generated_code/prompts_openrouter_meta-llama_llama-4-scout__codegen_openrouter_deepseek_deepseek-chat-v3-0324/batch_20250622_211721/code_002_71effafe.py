"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: "Generate a smart contract code for a multi-asset strategy vault on Singularity Finance, leveraging AI-driven risk management and automated execution."
Generated: DETERMINISTIC_71effafe7503fd80
Batch ID: 20250622_211721
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MultiAssetStrategyVault
 * @dev A smart contract for a multi-asset strategy vault with AI-driven risk management
 * and automated execution on Singularity Finance.
 */
contract MultiAssetStrategyVault is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Struct to represent a strategy
    struct Strategy {
        address strategyAddress;
        uint256 allocationPercentage; // Percentage (0-100) of total assets allocated to this strategy
        bool isActive;
    }

    // Struct to represent a supported asset
    struct Asset {
        address assetAddress;
        bool isSupported;
    }

    // Mapping of strategy ID to Strategy struct
    mapping(uint256 => Strategy) public strategies;
    uint256 public strategyCount;

    // Mapping of asset address to Asset struct
    mapping(address => Asset) public supportedAssets;

    // Total value locked in the vault
    uint256 public totalValueLocked;

    // Address of the AI risk management module
    address public aiRiskManager;

    // Events
    event Deposit(address indexed user, address indexed asset, uint256 amount);
    event Withdraw(address indexed user, address indexed asset, uint256 amount);
    event StrategyAdded(uint256 indexed strategyId, address strategyAddress, uint256 allocation);
    event StrategyUpdated(uint256 indexed strategyId, uint256 newAllocation);
    event StrategyRemoved(uint256 indexed strategyId);
    event AssetSupported(address indexed asset);
    event AssetUnsupported(address indexed asset);
    event Rebalanced(uint256 timestamp);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Constructor
     * @param _aiRiskManager Address of the AI risk management module
     */
    constructor(address _aiRiskManager) {
        require(_aiRiskManager != address(0), "Invalid AI risk manager address");
        aiRiskManager = _aiRiskManager;
    }

    /**
     * @dev Modifier to check if caller is AI risk manager
     */
    modifier onlyRiskManager() {
        require(msg.sender == aiRiskManager, "Caller is not risk manager");
        _;
    }

    /**
     * @dev Deposit assets into the vault
     * @param _asset Address of the asset to deposit
     * @param _amount Amount to deposit
     */
    function deposit(address _asset, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(supportedAssets[_asset].isSupported, "Asset not supported");

        IERC20(_asset).safeTransferFrom(msg.sender, address(this), _amount);
        totalValueLocked = totalValueLocked.add(_amount);

        emit Deposit(msg.sender, _asset, _amount);
    }

    /**
     * @dev Withdraw assets from the vault
     * @param _asset Address of the asset to withdraw
     * @param _amount Amount to withdraw
     */
    function withdraw(address _asset, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(supportedAssets[_asset].isSupported, "Asset not supported");
        require(_amount <= totalValueLocked, "Insufficient balance");

        totalValueLocked = totalValueLocked.sub(_amount);
        IERC20(_asset).safeTransfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _asset, _amount);
    }

    /**
     * @dev Add a new strategy
     * @param _strategyAddress Address of the strategy contract
     * @param _allocationPercentage Allocation percentage (0-100)
     */
    function addStrategy(address _strategyAddress, uint256 _allocationPercentage) external onlyOwner {
        require(_strategyAddress != address(0), "Invalid strategy address");
        require(_allocationPercentage <= 100, "Allocation must be <= 100");

        strategyCount++;
        strategies[strategyCount] = Strategy({
            strategyAddress: _strategyAddress,
            allocationPercentage: _allocationPercentage,
            isActive: true
        });

        emit StrategyAdded(strategyCount, _strategyAddress, _allocationPercentage);
    }

    /**
     * @dev Update strategy allocation
     * @param _strategyId ID of the strategy to update
     * @param _newAllocation New allocation percentage (0-100)
     */
    function updateStrategy(uint256 _strategyId, uint256 _newAllocation) external onlyOwner {
        require(_strategyId <= strategyCount && _strategyId != 0, "Invalid strategy ID");
        require(_newAllocation <= 100, "Allocation must be <= 100");

        strategies[_strategyId].allocationPercentage = _newAllocation;

        emit StrategyUpdated(_strategyId, _newAllocation);
    }

    /**
     * @dev Remove a strategy
     * @param _strategyId ID of the strategy to remove
     */
    function removeStrategy(uint256 _strategyId) external onlyOwner {
        require(_strategyId <= strategyCount && _strategyId != 0, "Invalid strategy ID");
        
        delete strategies[_strategyId];
        
        emit StrategyRemoved(_strategyId);
    }

    /**
     * @dev Add a supported asset
     * @param _asset Address of the asset to support
     */
    function supportAsset(address _asset) external onlyOwner {
        require(_asset != address(0), "Invalid asset address");
        
        supportedAssets[_asset] = Asset({
            assetAddress: _asset,
            isSupported: true
        });
        
        emit AssetSupported(_asset);
    }

    /**
     * @dev Remove a supported asset
     * @param _asset Address of the asset to unsupport
     */
    function unsupportAsset(address _asset) external onlyOwner {
        require(supportedAssets[_asset].isSupported, "Asset not supported");
        
        supportedAssets[_asset].isSupported = false;
        
        emit AssetUnsupported(_asset);
    }

    /**
     * @dev Rebalance the vault based on AI risk management signals
     */
    function rebalance() external onlyRiskManager {
        // Implement rebalancing logic based on AI signals
        // This would involve adjusting strategy allocations and asset distributions
        
        emit Rebalanced(block.timestamp);
    }

    /**
     * @dev Emergency withdraw all funds (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = IERC20(address(this)).balanceOf(address(this));
        IERC20(address(this)).safeTransfer(owner(), balance);
        
        emit EmergencyWithdraw(owner(), balance);
    }

    /**
     * @dev Update AI risk manager address
     * @param _newRiskManager New risk manager address
     */
    function updateRiskManager(address _newRiskManager) external onlyOwner {
        require(_newRiskManager != address(0), "Invalid address");
        aiRiskManager = _newRiskManager;
    }
}
```
