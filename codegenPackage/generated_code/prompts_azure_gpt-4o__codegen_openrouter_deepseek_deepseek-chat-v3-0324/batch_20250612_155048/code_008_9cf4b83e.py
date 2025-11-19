"""
Generated Code Metadata:
========================
Original URL: https://desnitsky.ru
Prompt: Write a Solidity contract that interacts with Frax Finance's smart contracts to demonstrate partial reserve management for stablecoins.
Generated: DETERMINISTIC_9cf4b83ed50fdb72
Batch ID: 20250612_155048
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IFrax {
    function COLLATERAL_RATIO_PAUSER() external view returns (bytes32);
    function collateral_ratio_paused() external view returns (bool);
    function global_collateral_ratio() external view returns (uint256);
    function refreshCollateralRatio() external;
    function pool_burn_from(address b_address, uint256 b_amount) external;
    function pool_mint(address m_address, uint256 m_amount) external;
}

interface IFraxAMOMinter {
    function acceptOwnership() external;
    function burnFraxFromAMO(uint256 frax_amount) external;
    function mintFraxForAMO(address destination_address, uint256 frax_amount) external;
    function col_idx() external view returns (uint256);
    function dollarBalances() external view returns (uint256 frax_val_e18, uint256 collat_val_e18);
    function fraxDollarBalanceStored() external view returns (uint256);
    function collatDollarBalanceStored() external view returns (uint256);
}

contract FraxReserveManager is Ownable {
    using SafeMath for uint256;

    IFrax public fraxContract;
    IFraxAMOMinter public amoMinterContract;
    IERC20 public collateralToken;

    uint256 public lastRefreshTime;
    uint256 public refreshCooldown = 3600; // 1 hour in seconds

    event CollateralRatioRefreshed(uint256 newRatio);
    event FraxMinted(address indexed destination, uint256 amount);
    event FraxBurned(address indexed from, uint256 amount);

    constructor(
        address _fraxContractAddress,
        address _amoMinterAddress,
        address _collateralTokenAddress
    ) {
        fraxContract = IFrax(_fraxContractAddress);
        amoMinterContract = IFraxAMOMinter(_amoMinterAddress);
        collateralToken = IERC20(_collateralTokenAddress);
    }

    modifier onlyWhenNotPaused() {
        require(!fraxContract.collateral_ratio_paused(), "Collateral ratio is paused");
        _;
    }

    modifier onlyAfterCooldown() {
        require(block.timestamp >= lastRefreshTime.add(refreshCooldown), "Must wait for cooldown");
        _;
    }

    function setRefreshCooldown(uint256 _cooldown) external onlyOwner {
        refreshCooldown = _cooldown;
    }

    function refreshCollateralRatio() external onlyOwner onlyWhenNotPaused onlyAfterCooldown {
        fraxContract.refreshCollateralRatio();
        lastRefreshTime = block.timestamp;
        emit CollateralRatioRefreshed(fraxContract.global_collateral_ratio());
    }

    function mintFrax(address destination, uint256 amount) external onlyOwner {
        amoMinterContract.mintFraxForAMO(destination, amount);
        emit FraxMinted(destination, amount);
    }

    function burnFrax(uint256 amount) external onlyOwner {
        amoMinterContract.burnFraxFromAMO(amount);
        emit FraxBurned(msg.sender, amount);
    }

    function getCollateralRatio() external view returns (uint256) {
        return fraxContract.global_collateral_ratio();
    }

    function getReserveBalances() external view returns (uint256 fraxBalance, uint256 collateralBalance) {
        (fraxBalance, collateralBalance) = amoMinterContract.dollarBalances();
    }

    function getCollateralTokenBalance() external view returns (uint256) {
        return collateralToken.balanceOf(address(this));
    }

    function withdrawCollateral(address recipient, uint256 amount) external onlyOwner {
        require(collateralToken.transfer(recipient, amount), "Transfer failed");
    }

    function emergencyWithdraw(address tokenAddress, address recipient) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(token.transfer(recipient, balance), "Transfer failed");
    }
}
```
