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

I'll provide the code in Solidity, a popular language for smart contracts. I'll implement a basic cross-chain stablecoin protocol similar to QiDao, focusing on collateralized vaults and the MAI token.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MAI token contract
contract MAIToken is ERC20 {
    constructor() ERC20("MAI", "MAI") {}

    function mint(address account, uint256 amount) public {
        _mint(account, amount);
    }

    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }
}

// Collateralized vault contract
contract CollateralizedVault {
    mapping(address => Vault) public vaults;

    struct Vault {
        address collateralToken;
        uint256 collateralAmount;
        uint256 debtAmount;
    }

    function createVault(address collateralToken) public {
        require(vaults[msg.sender].collateralToken == address(0), "Vault already exists");

        vaults[msg.sender] = Vault(collateralToken, 0, 0);
    }

    function depositCollateral(address collateralToken, uint256 amount) public {
        require(vaults[msg.sender].collateralToken == collateralToken, "Invalid vault");

        vaults[msg.sender].collateralAmount = vaults[msg.sender].collateralAmount.add(amount);
    }

    function withdrawCollateral(uint256 amount) public {
        require(vaults[msg.sender].collateralAmount >= amount, "Insufficient collateral");

        vaults[msg.sender].collateralAmount = vaults[msg.sender].collateralAmount.sub(amount);
    }

    function borrowMAI(uint256 amount) public {
        require(vaults[msg.sender].collateralAmount > 0, "No collateral");

        vaults[msg.sender].debtAmount = vaults[msg.sender].debtAmount.add(amount);
    }

    function repayMAI(uint256 amount) public {
        require(vaults[msg.sender].debtAmount >= amount, "Invalid repayment amount");

        vaults[msg.sender].debtAmount = vaults[msg.sender].debtAmount.sub(amount);
    }
}

// QiDao-like stablecoin protocol contract
contract StablecoinProtocol is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for MAIToken;

    MAIToken public maiToken;
    CollateralizedVault public collateralizedVault;
    mapping(address => uint256) public collateralizationRatios;

    constructor(MAIToken _maiToken, CollateralizedVault _collateralizedVault) public {
        maiToken = _maiToken;
        collateralizedVault = _collateralizedVault;

        collateralizationRatios[address(0)] = 150; // Default collateralization ratio
    }

    function setCollateralizationRatio(address collateralToken, uint256 ratio) public onlyOwner {
        collateralizationRatios[collateralToken] = ratio;
    }

    function liquidateVault(address vaultOwner) public {
        CollateralizedVault.Vault memory vault = collateralizedVault.vaults(vaultOwner);

        require(vault.collateralAmount > 0, "Vault has no collateral");
        require(vault.debtAmount > 0, "Vault has no debt");

        uint256 collateralizationRatio = collateralizationRatios[vault.collateralToken];
        uint256 collateralValue = vault.collateralAmount.mul(collateralizationRatio).div(100);
        uint256 debtValue = vault.debtAmount;

        require(collateralValue < debtValue, "Vault is not liquidatable");

        // Liquidate vault and transfer collateral to protocol
        collateralizedVault.withdrawCollateral(vault.collateralAmount);

        // Transfer MAI tokens to protocol
        maiToken.transferFrom(vaultOwner, address(this), vault.debtAmount);
    }
}
```
