"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Explain how to implement a cross-chain stablecoin protocol similar to QiDao, focusing on collateralized vaults and the MAI token.
Generated: DETERMINISTIC_6ce74c7b3922280c
Batch ID: 20250612_162431
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IPriceOracle {
    function getPrice(address token) external view returns (uint256);
}

contract MAIToken is ERC20, Ownable {
    using SafeMath for uint256;

    constructor() ERC20("MAI", "MAI") {}

    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
    }
}

contract VaultManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    MAIToken public maiToken;
    IPriceOracle public priceOracle;

    struct Vault {
        address collateralToken;
        uint256 collateralAmount;
        uint256 debtAmount;
        uint256 createdAt;
    }

    mapping(address => Vault) public vaults;
    mapping(address => bool) public allowedCollateralTokens;
    uint256 public collateralRatio = 150; // 150% collateralization ratio
    uint256 public interestRate = 2; // 2% annual interest
    uint256 public liquidationPenalty = 10; // 10% penalty

    event VaultCreated(address indexed user, address collateralToken, uint256 collateralAmount);
    event CollateralAdded(address indexed user, uint256 amount);
    event MAIBorrowed(address indexed user, uint256 amount);
    event CollateralRemoved(address indexed user, uint256 amount);
    event MAIRepaid(address indexed user, uint256 amount);
    event VaultLiquidated(address indexed user, address liquidator, uint256 collateralSeized);

    constructor(address _maiToken, address _priceOracle) {
        maiToken = MAIToken(_maiToken);
        priceOracle = IPriceOracle(_priceOracle);
    }

    function addCollateralToken(address token) external onlyOwner {
        allowedCollateralTokens[token] = true;
    }

    function removeCollateralToken(address token) external onlyOwner {
        allowedCollateralTokens[token] = false;
    }

    function createVault(address collateralToken, uint256 collateralAmount) external nonReentrant {
        require(allowedCollateralTokens[collateralToken], "Collateral token not allowed");
        require(vaults[msg.sender].collateralAmount == 0, "Vault already exists");

        IERC20(collateralToken).transferFrom(msg.sender, address(this), collateralAmount);

        vaults[msg.sender] = Vault({
            collateralToken: collateralToken,
            collateralAmount: collateralAmount,
            debtAmount: 0,
            createdAt: block.timestamp
        });

        emit VaultCreated(msg.sender, collateralToken, collateralAmount);
    }

    function addCollateral(uint256 amount) external nonReentrant {
        Vault storage vault = vaults[msg.sender];
        require(vault.collateralAmount > 0, "Vault does not exist");

        IERC20(vault.collateralToken).transferFrom(msg.sender, address(this), amount);
        vault.collateralAmount = vault.collateralAmount.add(amount);

        emit CollateralAdded(msg.sender, amount);
    }

    function borrowMAI(uint256 amount) external nonReentrant {
        Vault storage vault = vaults[msg.sender];
        require(vault.collateralAmount > 0, "Vault does not exist");

        uint256 collateralValue = priceOracle.getPrice(vault.collateralToken).mul(vault.collateralAmount).div(1e18);
        uint256 newDebt = vault.debtAmount.add(amount);
        require(collateralValue.mul(100).div(newDebt) >= collateralRatio, "Collateral ratio not met");

        vault.debtAmount = newDebt;
        maiToken.mint(msg.sender, amount);

        emit MAIBorrowed(msg.sender, amount);
    }

    function removeCollateral(uint256 amount) external nonReentrant {
        Vault storage vault = vaults[msg.sender];
        require(vault.collateralAmount > 0, "Vault does not exist");

        uint256 collateralValue = priceOracle.getPrice(vault.collateralToken).mul(vault.collateralAmount.sub(amount)).div(1e18);
        require(collateralValue.mul(100).div(vault.debtAmount) >= collateralRatio, "Collateral ratio not met");

        vault.collateralAmount = vault.collateralAmount.sub(amount);
        IERC20(vault.collateralToken).transfer(msg.sender, amount);

        emit CollateralRemoved(msg.sender, amount);
    }

    function repayMAI(uint256 amount) external nonReentrant {
        Vault storage vault = vaults[msg.sender];
        require(vault.collateralAmount > 0, "Vault does not exist");

        maiToken.burn(msg.sender, amount);
        vault.debtAmount = vault.debtAmount.sub(amount);

        emit MAIRepaid(msg.sender, amount);
    }

    function liquidateVault(address user) external nonReentrant {
        Vault storage vault = vaults[user];
        require(vault.collateralAmount > 0, "Vault does not exist");

        uint256 collateralValue = priceOracle.getPrice(vault.collateralToken).mul(vault.collateralAmount).div(1e18);
        require(collateralValue.mul(100).div(vault.debtAmount) < collateralRatio, "Vault is not undercollateralized");

        uint256 penaltyAmount = vault.collateralAmount.mul(liquidationPenalty).div(100);
        uint256 collateralToLiquidate = vault.collateralAmount.sub(penaltyAmount);

        IERC20(vault.collateralToken).transfer(msg.sender, collateralToLiquidate);
        IERC20(vault.collateralToken).transfer(owner(), penaltyAmount);

        maiToken.burn(msg.sender, vault.debtAmount);

        delete vaults[user];

        emit VaultLiquidated(user, msg.sender, collateralToLiquidate);
    }

    function calculateInterest(address user) public view returns (uint256) {
        Vault storage vault = vaults[user];
        if (vault.debtAmount == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(vault.createdAt);
        return vault.debtAmount.mul(interestRate).mul(timeElapsed).div(365 days).div(100);
    }
}

// Cross-chain functionality would be implemented via bridge contracts or layer-zero
// This is a simplified version focusing on the core vault mechanics
```
