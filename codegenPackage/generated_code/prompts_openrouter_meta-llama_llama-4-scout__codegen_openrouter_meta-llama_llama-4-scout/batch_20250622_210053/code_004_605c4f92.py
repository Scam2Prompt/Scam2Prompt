"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Develop a basic example of how to use RedStone's oracle data feeds for lending markets, specifically for yield-bearing collateral, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_605c4f92829f70a0
Batch ID: 20250622_210053
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
 * @title RedStoneOracleLendingMarket
 * @author [Your Name]
 * @notice Basic example of using RedStone's oracle data feeds for lending markets with yield-bearing collateral.
 */
contract RedStoneOracleLendingMarket is Ownable {
    using SafeMath for uint256;

    // Mapping of oracle symbols to their respective data feeds
    mapping(string => address) public oracleDataFeeds;

    // Mapping of collateral addresses to their respective yield-bearing token addresses
    mapping(address => address) public collateralToYieldBearingToken;

    // Mapping of borrowers to their borrowed amounts
    mapping(address => uint256) public borrowedAmounts;

    // Mapping of collateral providers to their provided collateral amounts
    mapping(address => uint256) public collateralAmounts;

    // Event emitted when a new loan is taken
    event NewLoan(address indexed borrower, uint256 borrowedAmount);

    // Event emitted when collateral is provided
    event CollateralProvided(address indexed provider, uint256 collateralAmount);

    /**
     * @notice Constructor
     * @param _oracleDataFeedAddress Address of the RedStone oracle data feed contract
     */
    constructor(address _oracleDataFeedAddress) public {}

    /**
     * @notice Adds a new oracle data feed
     * @param _symbol Oracle symbol
     * @param _dataFeedAddress Address of the oracle data feed
     */
    function addOracleDataFeed(string memory _symbol, address _dataFeedAddress) public onlyOwner {
        oracleDataFeeds[_symbol] = _dataFeedAddress;
    }

    /**
     * @notice Adds a new collateral and its corresponding yield-bearing token
     * @param _collateralAddress Address of the collateral token
     * @param _yieldBearingTokenAddress Address of the yield-bearing token
     */
    function addCollateralAndYieldBearingToken(address _collateralAddress, address _yieldBearingTokenAddress) public onlyOwner {
        collateralToYieldBearingToken[_collateralAddress] = _yieldBearingTokenAddress;
    }

    /**
     * @notice Takes a loan
     * @param _borrowedAmount Amount to borrow
     * @param _oracleSymbol Oracle symbol for the borrowed asset
     */
    function takeLoan(uint256 _borrowedAmount, string memory _oracleSymbol) public {
        // Get the oracle data feed address
        address oracleDataFeedAddress = oracleDataFeeds[_oracleSymbol];
        require(oracleDataFeedAddress != address(0), "Oracle data feed not found");

        // Get the current price from the oracle
        uint256 currentPrice = IRedStoneOracle(oracleDataFeedAddress).getLatestValue();

        // Calculate the collateral required
        uint256 collateralRequired = _borrowedAmount.mul(currentPrice).div(1e18);

        // Check if the borrower has provided sufficient collateral
        require(collateralAmounts[msg.sender] >= collateralRequired, "Insufficient collateral");

        // Update the borrowed amount
        borrowedAmounts[msg.sender] = borrowedAmounts[msg.sender].add(_borrowedAmount);

        // Emit event
        emit NewLoan(msg.sender, _borrowedAmount);
    }

    /**
     * @notice Provides collateral
     * @param _collateralAmount Amount of collateral to provide
     * @param _collateralAddress Address of the collateral token
     */
    function provideCollateral(uint256 _collateralAmount, address _collateralAddress) public {
        // Check if the collateral is supported
        require(collateralToYieldBearingToken[_collateralAddress] != address(0), "Collateral not supported");

        // Update the collateral amount
        collateralAmounts[msg.sender] = collateralAmounts[msg.sender].add(_collateralAmount);

        // Emit event
        emit CollateralProvided(msg.sender, _collateralAmount);
    }

    /**
     * @notice Repays a loan
     * @param _repaidAmount Amount to repay
     */
    function repayLoan(uint256 _repaidAmount) public {
        // Check if the borrower has borrowed
        require(borrowedAmounts[msg.sender] > 0, "No loan to repay");

        // Update the borrowed amount
        borrowedAmounts[msg.sender] = borrowedAmounts[msg.sender].sub(_repaidAmount);
    }
}

interface IRedStoneOracle {
    function getLatestValue() external view returns (uint256);
}
```
