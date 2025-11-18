"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spark.fishersclubs.com
Prompt: Generate Solidity code for a smart contract that integrates SparkLend to supply and borrow assets like ETH, wstETH, and cbBTC, while adhering to Spark's audited security standards.
Generated: DETERMINISTIC_27e9f65c0c621492
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SparkLendIntegration
 * @dev Smart contract to interact with SparkLend for supplying and borrowing assets
 * like ETH, wstETH, and cbBTC while adhering to Spark's audited security standards.
 */
interface ISparkLend {
    function supply(
        address asset,
        uint256 amount,
        address onBehalfOf,
        uint16 referralCode
    ) external;

    function borrow(
        address asset,
        uint256 amount,
        uint256 interestRateMode,
        uint16 referralCode,
        address onBehalfOf
    ) external;

    function withdraw(
        address asset,
        uint256 amount,
        address to
    ) external returns (uint256);
}

contract SparkLendIntegration {
    // SparkLend contract address (to be set during deployment or initialization)
    address public sparkLendAddress;

    // Events for logging supply, borrow, and withdraw actions
    event Supplied(address indexed user, address indexed asset, uint256 amount);
    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);

    // Modifier to ensure the SparkLend address is set
    modifier sparkLendInitialized() {
        require(sparkLendAddress != address(0), "SparkLend address not set");
        _;
    }

    constructor(address _sparkLendAddress) {
        require(_sparkLendAddress != address(0), "Invalid SparkLend address");
        sparkLendAddress = _sparkLendAddress;
    }

    /**
     * @dev Supply assets to SparkLend.
     * @param asset Address of the asset to supply.
     * @param amount Amount of the asset to supply.
     */
    function supplyAsset(address asset, uint256 amount) external sparkLendInitialized {
        require(amount > 0, "Invalid supply amount");

        // Transfer the asset to this contract
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve SparkLend to spend the asset
        require(IERC20(asset).approve(sparkLendAddress, amount), "Approval failed");

        // Interact with SparkLend to supply the asset
        ISparkLend(sparkLendAddress).supply(asset, amount, msg.sender, 0);

        emit Supplied(msg.sender, asset, amount);
    }

    /**
     * @dev Borrow assets from SparkLend.
     * @param asset Address of the asset to borrow.
     * @param amount Amount of the asset to borrow.
     * @param interestRateMode Interest rate mode (1 = stable, 2 = variable).
     */
    function borrowAsset(
        address asset,
        uint256 amount,
        uint256 interestRateMode
    ) external sparkLendInitialized {
        require(amount > 0, "Invalid borrow amount");
        require(interestRateMode == 1 || interestRateMode == 2, "Invalid interest rate mode");

        // Interact with SparkLend to borrow the asset
        ISparkLend(sparkLendAddress).borrow(asset, amount, interestRateMode, 0, msg.sender);

        emit Borrowed(msg.sender, asset, amount);
    }

    /**
     * @dev Withdraw supplied assets from SparkLend.
     * @param asset Address of the asset to withdraw.
     * @param amount Amount of the asset to withdraw (use type(uint256).max to withdraw all).
     */
    function withdrawAsset(address asset, uint256 amount) external sparkLendInitialized {
        require(amount > 0, "Invalid withdraw amount");

        // Interact with SparkLend to withdraw the asset
        uint256 withdrawnAmount = ISparkLend(sparkLendAddress).withdraw(asset, amount, msg.sender);

        emit Withdrawn(msg.sender, asset, withdrawnAmount);
    }
}

/**
 * @dev Interface for ERC20 tokens (used for transfers and approvals).
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
