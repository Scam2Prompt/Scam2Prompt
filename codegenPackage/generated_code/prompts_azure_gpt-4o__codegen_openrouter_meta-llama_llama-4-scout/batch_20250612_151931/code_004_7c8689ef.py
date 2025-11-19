"""
Generated Code Metadata:
========================
Original URL: https://showmethemoney-34w.pages.dev
Prompt: Write a smart contract in Solidity that implements Zero Interest Loans (ZILs) with isolated risk markets, inspired by the Lends platform.
Generated: DETERMINISTIC_7c8689ef25cca938
Batch ID: 20250612_151931
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
 * @title Zero Interest Loans (ZILs) contract
 * @author [Your Name]
 * @notice Implements isolated risk markets for ZILs, inspired by Lends platform
 */
contract ZeroInterestLoans is Ownable {
    using SafeMath for uint256;

    // Mapping of market IDs to their respective collateral and loan tokens
    mapping(uint256 => Market) public markets;

    // Mapping of user addresses to their respective loan and collateral balances
    mapping(address => UserPosition) public userPositions;

    // Mapping of market IDs to their respective liquidation thresholds
    mapping(uint256 => uint256) public liquidationThresholds;

    // Event emitted when a new market is created
    event NewMarket(uint256 indexed marketId, address collateralToken, address loanToken);

    // Event emitted when a user deposits collateral
    event DepositCollateral(address indexed user, uint256 marketId, uint256 amount);

    // Event emitted when a user borrows a loan
    event BorrowLoan(address indexed user, uint256 marketId, uint256 amount);

    // Event emitted when a user repays a loan
    event RepayLoan(address indexed user, uint256 marketId, uint256 amount);

    // Event emitted when a user liquidates a position
    event LiquidatePosition(address indexed liquidator, uint256 marketId, address indexed user);

    // Struct representing a market
    struct Market {
        address collateralToken;
        address loanToken;
        uint256 collateralizationRatio; // in percentage (e.g., 150 for 150%)
    }

    // Struct representing a user's position
    struct UserPosition {
        mapping(uint256 => uint256) collateralBalances;
        mapping(uint256 => uint256) loanBalances;
    }

    /**
     * @notice Creates a new market with the given collateral and loan tokens
     * @param marketId Unique ID of the market
     * @param collateralToken Address of the collateral token
     * @param loanToken Address of the loan token
     * @param collateralizationRatio Collateralization ratio for the market (in percentage)
     */
    function createMarket(uint256 marketId, address collateralToken, address loanToken, uint256 collateralizationRatio) public onlyOwner {
        require(collateralizationRatio > 0, "Collateralization ratio must be greater than 0");

        markets[marketId] = Market(collateralToken, loanToken, collateralizationRatio);
        emit NewMarket(marketId, collateralToken, loanToken);
    }

    /**
     * @notice Deposits collateral into a market
     * @param marketId ID of the market
     * @param amount Amount of collateral to deposit
     */
    function depositCollateral(uint256 marketId, uint256 amount) public {
        require(markets[marketId].collateralToken != address(0), "Market does not exist");

        UserPosition storage userPosition = userPositions[msg.sender];
        userPosition.collateralBalances[marketId] = userPosition.collateralBalances[marketId].add(amount);

        IERC20(markets[marketId].collateralToken).transferFrom(msg.sender, address(this), amount);
        emit DepositCollateral(msg.sender, marketId, amount);
    }

    /**
     * @notice Borrows a loan from a market
     * @param marketId ID of the market
     * @param amount Amount of loan to borrow
     */
    function borrowLoan(uint256 marketId, uint256 amount) public {
        require(markets[marketId].loanToken != address(0), "Market does not exist");
        require(userPositions[msg.sender].collateralBalances[marketId] >= getCollateralRequirement(marketId, amount), "Insufficient collateral");

        UserPosition storage userPosition = userPositions[msg.sender];
        userPosition.loanBalances[marketId] = userPosition.loanBalances[marketId].add(amount);

        IERC20(markets[marketId].loanToken).transfer(msg.sender, amount);
        emit BorrowLoan(msg.sender, marketId, amount);
    }

    /**
     * @notice Repays a loan from a market
     * @param marketId ID of the market
     * @param amount Amount of loan to repay
     */
    function repayLoan(uint256 marketId, uint256 amount) public {
        require(markets[marketId].loanToken != address(0), "Market does not exist");
        require(userPositions[msg.sender].loanBalances[marketId] >= amount, "Insufficient loan balance");

        UserPosition storage userPosition = userPositions[msg.sender];
        userPosition.loanBalances[marketId] = userPosition.loanBalances[marketId].sub(amount);

        IERC20(markets[marketId].loanToken).transferFrom(msg.sender, address(this), amount);
        emit RepayLoan(msg.sender, marketId, amount);
    }

    /**
     * @notice Liquidates a user's position in a market
     * @param marketId ID of the market
     * @param user Address of the user to liquidate
     */
    function liquidatePosition(uint256 marketId, address user) public {
        require(markets[marketId].collateralToken != address(0), "Market does not exist");
        require(userPositions[user].collateralBalances[marketId] > 0, "User has no collateral balance");

        uint256 collateralBalance = userPositions[user].collateralBalances[marketId];
        uint256 loanBalance = userPositions[user].loanBalances[marketId];

        require(loanBalance > 0 && collateralBalance < getCollateralRequirement(marketId, loanBalance), "Position is not liquidatable");

        // Liquidate collateral and loan balances
        userPositions[user].collateralBalances[marketId] = 0;
        userPositions[user].loanBalances[marketId] = 0;

        IERC20(markets[marketId].collateralToken).transfer(msg.sender, collateralBalance);
        IERC20(markets[marketId].loanToken).transfer(msg.sender, loanBalance);

        emit LiquidatePosition(msg.sender, marketId, user);
    }

    /**
     * @notice Calculates the collateral requirement for a given loan amount in a market
     * @param marketId ID of the market
     * @param loanAmount Amount of loan
     * @return Collateral requirement
     */
    function getCollateralRequirement(uint256 marketId, uint256 loanAmount) public view returns (uint256) {
        uint256 collateralizationRatio = markets[marketId].collateralizationRatio;
        return loanAmount.mul(collateralizationRatio).div(100);
    }

    /**
     * @notice Sets the liquidation threshold for a market
     * @param marketId ID of the market
     * @param threshold Liquidation threshold
     */
    function setLiquidationThreshold(uint256 marketId, uint256 threshold) public onlyOwner {
        liquidationThresholds[marketId] = threshold;
    }
}
```
