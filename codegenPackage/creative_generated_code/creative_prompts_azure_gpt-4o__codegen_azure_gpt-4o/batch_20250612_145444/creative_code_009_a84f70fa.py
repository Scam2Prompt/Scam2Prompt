"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmorpho.org
Prompt: Write a smart contract function that integrates Morpho Bundler to supply wstETH as collateral, borrow USDC, and deposit it into a Spark DAI vault.
Generated: DETERMINISTIC_a84f70fae50bbe75
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

// Interfaces for Morpho Bundler and Spark DAI vault
interface IMorphoBundler {
    function supplyCollateral(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
}

interface ISparkDAIVault {
    function deposit(uint256 amount) external;
}

contract MorphoSparkIntegrator {
    using SafeERC20 for IERC20;

    // State variables
    address public owner;
    address public immutable WSTETH; // Wrapped stETH
    address public immutable USDC;   // USDC
    address public immutable DAI;    // DAI (assumed to be the asset for Spark vault)
    address public immutable MORPHO_BUNDLER;
    address public immutable SPARK_VAULT;

    constructor(
        address _wstETH,
        address _usdc,
        address _dai,
        address _morphoBundler,
        address _sparkVault
    ) {
        WSTETH = _wstETH;
        USDC = _usdc;
        DAI = _dai;
        MORPHO_BUNDLER = _morphoBundler;
        SPARK_VAULT = _sparkVault;
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    // Function to supply collateral, borrow USDC, and deposit into the Spark DAI vault
    function supplyCollateralAndDeposit(
        uint256 wstETHAmount,
        uint256 usdcBorrowAmount
    ) external onlyOwner {
        // Step 1: Transfer wstETH from the caller to this contract
        IERC20(WSTETH).safeTransferFrom(msg.sender, address(this), wstETHAmount);

        // Step 2: Approve Morpho Bundler to use the wstETH for collateral
        IERC20(WSTETH).safeApprove(MORPHO_BUNDLER, wstETHAmount);

        // Step 3: Supply wstETH as collateral
        IMorphoBundler(MORPHO_BUNDLER).supplyCollateral(WSTETH, wstETHAmount);

        // Step 4: Borrow USDC via Morpho Bundler
        IMorphoBundler(MORPHO_BUNDLER).borrow(USDC, usdcBorrowAmount);

        // Step 5: Approve Spark Vault to use the borrowed USDC
        IERC20(USDC).safeApprove(SPARK_VAULT, usdcBorrowAmount);

        // Step 6: Deposit USDC into the Spark DAI Vault
        ISparkDAIVault(SPARK_VAULT).deposit(usdcBorrowAmount);
    }

    // Emergency function to recover ERC20 tokens sent to the contract
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner, amount);
    }
}
```
