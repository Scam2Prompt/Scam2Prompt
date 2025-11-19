"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-feat-optimism-venus-protocol.vercel.app
Prompt: Explain how to implement collateral management using the Venus Protocol in a smart contract.
Generated: DETERMINISTIC_5490d2b5edbe079a
Batch ID: 20250612_155248
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CollateralManagement
 * @author [Your Name]
 * @notice This contract manages collateral using the Venus Protocol.
 */
contract CollateralManagement is Ownable {
    using SafeMath for uint256;

    // Mapping of users to their collateral balances
    mapping(address => mapping(address => uint256)) public collateralBalances;

    // Mapping of users to their borrowed amounts
    mapping(address => mapping(address => uint256)) public borrowedAmounts;

    // Mapping of assets to their corresponding Venus Protocol markets
    mapping(address => address) public venusMarkets;

    // Event emitted when collateral is added
    event CollateralAdded(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when collateral is removed
    event CollateralRemoved(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a loan is borrowed
    event LoanBorrowed(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed user, address indexed asset, uint256 amount);

    /**
     * @notice Constructor function
     * @param _venusMarkets Mapping of assets to their corresponding Venus Protocol markets
     */
    constructor(address[] memory _assets, address[] memory _venusMarkets) {
        require(_assets.length == _venusMarkets.length, "Invalid input lengths");

        for (uint256 i = 0; i < _assets.length; i++) {
            venusMarkets[_assets[i]] = _venusMarkets[i];
        }
    }

    /**
     * @notice Add collateral to the protocol
     * @param _asset Address of the asset to add as collateral
     * @param _amount Amount of the asset to add as collateral
     */
    function addCollateral(address _asset, uint256 _amount) public {
        require(venusMarkets[_asset] != address(0), "Asset not supported");
        require(_amount > 0, "Invalid amount");

        collateralBalances[msg.sender][_asset] = collateralBalances[msg.sender][_asset].add(_amount);

        // Transfer collateral to the Venus Protocol market
        IERC20(_asset).transferFrom(msg.sender, venusMarkets[_asset], _amount);

        emit CollateralAdded(msg.sender, _asset, _amount);
    }

    /**
     * @notice Remove collateral from the protocol
     * @param _asset Address of the asset to remove as collateral
     * @param _amount Amount of the asset to remove as collateral
     */
    function removeCollateral(address _asset, uint256 _amount) public {
        require(venusMarkets[_asset] != address(0), "Asset not supported");
        require(collateralBalances[msg.sender][_asset] >= _amount, "Insufficient collateral");

        collateralBalances[msg.sender][_asset] = collateralBalances[msg.sender][_asset].sub(_amount);

        // Transfer collateral from the Venus Protocol market
        IERC20(venusMarkets[_asset]).transfer(msg.sender, _amount);

        emit CollateralRemoved(msg.sender, _asset, _amount);
    }

    /**
     * @notice Borrow a loan from the protocol
     * @param _asset Address of the asset to borrow
     * @param _amount Amount of the asset to borrow
     */
    function borrowLoan(address _asset, uint256 _amount) public {
        require(venusMarkets[_asset] != address(0), "Asset not supported");
        require(collateralBalances[msg.sender][_asset] > 0, "Insufficient collateral");

        borrowedAmounts[msg.sender][_asset] = borrowedAmounts[msg.sender][_asset].add(_amount);

        // Transfer borrowed amount to the user
        IERC20(_asset).transfer(msg.sender, _amount);

        emit LoanBorrowed(msg.sender, _asset, _amount);
    }

    /**
     * @notice Repay a loan to the protocol
     * @param _asset Address of the asset to repay
     * @param _amount Amount of the asset to repay
     */
    function repayLoan(address _asset, uint256 _amount) public {
        require(venusMarkets[_asset] != address(0), "Asset not supported");
        require(borrowedAmounts[msg.sender][_asset] >= _amount, "Invalid repayment amount");

        borrowedAmounts[msg.sender][_asset] = borrowedAmounts[msg.sender][_asset].sub(_amount);

        // Transfer repayment to the Venus Protocol market
        IERC20(_asset).transferFrom(msg.sender, venusMarkets[_asset], _amount);

        emit LoanRepaid(msg.sender, _asset, _amount);
    }

    /**
     * @notice Liquidate a user's collateral
     * @param _user Address of the user to liquidate
     * @param _asset Address of the asset to liquidate
     */
    function liquidateCollateral(address _user, address _asset) public onlyOwner {
        require(venusMarkets[_asset] != address(0), "Asset not supported");
        require(collateralBalances[_user][_asset] > 0, "Insufficient collateral");

        // Transfer collateral to the owner
        IERC20(venusMarkets[_asset]).transfer(msg.sender, collateralBalances[_user][_asset]);

        collateralBalances[_user][_asset] = 0;
    }
}
```
