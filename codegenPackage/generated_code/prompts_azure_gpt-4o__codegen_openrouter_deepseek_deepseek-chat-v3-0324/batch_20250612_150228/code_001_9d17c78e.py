"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Generate code to integrate Silo Finance's shared liquidity model into a DeFi application, ensuring efficient liquidity movement between collateral tokens via the bridge asset.
Generated: DETERMINISTIC_9d17c78e516f766f
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/access/Ownable.sol";

interface ISilo {
    function deposit(address asset, uint256 amount, bool collateralOnly) external;
    function withdraw(address asset, uint256 amount, bool collateralOnly) external;
    function balanceOf(address asset, address user) external view returns (uint256);
    function assetStorage(address asset) external view returns (uint256 totalDeposits, uint256 collateralOnlyDeposits);
}

contract SiloIntegration is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    ISilo public immutable silo;
    IERC20 public immutable bridgeAsset;
    mapping(address => bool) public supportedCollateral;

    event CollateralAdded(address indexed collateral);
    event CollateralRemoved(address indexed collateral);
    event LiquidityMoved(address indexed fromCollateral, address indexed toCollateral, uint256 amount);
    event BridgeAssetDeposited(address indexed user, uint256 amount);
    event BridgeAssetWithdrawn(address indexed user, uint256 amount);

    constructor(ISilo _silo, IERC20 _bridgeAsset) {
        require(address(_silo) != address(0), "Invalid Silo address");
        require(address(_bridgeAsset) != address(0), "Invalid bridge asset address");
        
        silo = _silo;
        bridgeAsset = _bridgeAsset;
    }

    modifier onlySupportedCollateral(address collateral) {
        require(supportedCollateral[collateral], "Collateral not supported");
        _;
    }

    function addCollateral(address collateral) external onlyOwner {
        require(collateral != address(0), "Invalid collateral address");
        require(!supportedCollateral[collateral], "Collateral already supported");
        
        supportedCollateral[collateral] = true;
        emit CollateralAdded(collateral);
    }

    function removeCollateral(address collateral) external onlyOwner onlySupportedCollateral(collateral) {
        supportedCollateral[collateral] = false;
        emit CollateralRemoved(collateral);
    }

    function depositBridgeAsset(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        bridgeAsset.safeTransferFrom(msg.sender, address(this), amount);
        bridgeAsset.approve(address(silo), amount);
        silo.deposit(address(bridgeAsset), amount, false);
        
        emit BridgeAssetDeposited(msg.sender, amount);
    }

    function withdrawBridgeAsset(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 userBalance = silo.balanceOf(address(bridgeAsset), msg.sender);
        require(userBalance >= amount, "Insufficient bridge asset balance");
        
        silo.withdraw(address(bridgeAsset), amount, false);
        bridgeAsset.safeTransfer(msg.sender, amount);
        
        emit BridgeAssetWithdrawn(msg.sender, amount);
    }

    function moveLiquidity(
        address fromCollateral,
        address toCollateral,
        uint256 amount
    ) external nonReentrant onlySupportedCollateral(fromCollateral) onlySupportedCollateral(toCollateral) {
        require(amount > 0, "Amount must be greater than 0");
        require(fromCollateral != toCollateral, "Cannot move to same collateral");
        
        uint256 userBalance = silo.balanceOf(fromCollateral, msg.sender);
        require(userBalance >= amount, "Insufficient collateral balance");
        
        // Withdraw from current collateral
        silo.withdraw(fromCollateral, amount, true);
        
        // Deposit to new collateral
        IERC20(fromCollateral).approve(address(silo), amount);
        silo.deposit(toCollateral, amount, true);
        
        emit LiquidityMoved(fromCollateral, toCollateral, amount);
    }

    function getCollateralBalance(address collateral, address user) external view returns (uint256) {
        return silo.balanceOf(collateral, user);
    }

    function getBridgeAssetBalance(address user) external view returns (uint256) {
        return silo.balanceOf(address(bridgeAsset), user);
    }

    function getTotalDeposits(address collateral) external view returns (uint256 total, uint256 collateralOnly) {
        (total, collateralOnly) = silo.assetStorage(collateral);
    }
}
```
