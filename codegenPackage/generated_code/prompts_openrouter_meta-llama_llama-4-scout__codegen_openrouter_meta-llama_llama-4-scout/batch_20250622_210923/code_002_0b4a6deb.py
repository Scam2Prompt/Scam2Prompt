"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Generate a smart contract code in Solidity for a lending market on zkSync, incorporating prime assets, Chainlink and DIA oracles for price accuracy, and a decentralized and verifiable protocol.
Generated: DETERMINISTIC_0b4a6debfd30176f
Batch ID: 20250622_210923
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
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@DIA/DIAOracle.sol";

// Define the Lending Market contract
contract LendingMarket is Ownable {
    using SafeMath for uint256;

    // Mapping of lenders to their supplied assets
    mapping(address => mapping(address => uint256)) public lenderSuppliedAssets;

    // Mapping of borrowers to their borrowed assets
    mapping(address => mapping(address => uint256)) public borrowerBorrowedAssets;

    // Mapping of assets to their oracle feeds
    mapping(address => AggregatorV3Interface) public assetOracles;

    // Mapping of assets to their DIA oracle feeds
    mapping(address => DIAOracle) public diaOracles;

    // Mapping of prime assets
    mapping(address => bool) public primeAssets;

    // Event emitted when a lender supplies an asset
    event LenderSuppliedAsset(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a borrower borrows an asset
    event BorrowerBorrowedAsset(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a lender withdraws an asset
    event LenderWithdrewAsset(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a borrower repays a borrowed asset
    event BorrowerRepaidAsset(address indexed borrower, address indexed asset, uint256 amount);

    // Constructor
    constructor() public {}

    // Function to add a prime asset
    function addPrimeAsset(address asset) public onlyOwner {
        primeAssets[asset] = true;
    }

    // Function to remove a prime asset
    function removePrimeAsset(address asset) public onlyOwner {
        primeAssets[asset] = false;
    }

    // Function to set an oracle feed for an asset
    function setOracleFeed(address asset, AggregatorV3Interface oracle) public onlyOwner {
        assetOracles[asset] = oracle;
    }

    // Function to set a DIA oracle feed for an asset
    function setDIAOracleFeed(address asset, DIAOracle oracle) public onlyOwner {
        diaOracles[asset] = oracle;
    }

    // Function to supply an asset
    function supplyAsset(address asset, uint256 amount) public {
        require(primeAssets[asset], "Asset is not prime");
        require(assetOracles[asset] != AggregatorV3Interface(address(0)), "Oracle feed not set");

        // Get the current price of the asset from Chainlink oracle
        uint256 price = getPrice(asset);

        // Calculate the value of the supplied asset
        uint256 value = price.mul(amount);

        // Update the lender's supplied assets
        lenderSuppliedAssets[msg.sender][asset] = lenderSuppliedAssets[msg.sender][asset].add(value);

        // Emit event
        emit LenderSuppliedAsset(msg.sender, asset, value);
    }

    // Function to borrow an asset
    function borrowAsset(address asset, uint256 amount) public {
        require(diaOracles[asset] != DIAOracle(address(0)), "DIA oracle feed not set");

        // Get the current price of the asset from DIA oracle
        uint256 price = diaOracles[asset].getPrice(asset);

        // Calculate the value of the borrowed asset
        uint256 value = price.mul(amount);

        // Check if the borrower has sufficient collateral
        require(hasSufficientCollateral(msg.sender, asset, value), "Insufficient collateral");

        // Update the borrower's borrowed assets
        borrowerBorrowedAssets[msg.sender][asset] = borrowerBorrowedAssets[msg.sender][asset].add(value);

        // Emit event
        emit BorrowerBorrowedAsset(msg.sender, asset, value);
    }

    // Function to withdraw a supplied asset
    function withdrawAsset(address asset, uint256 amount) public {
        require(lenderSuppliedAssets[msg.sender][asset] >= amount, "Insufficient supplied assets");

        // Get the current price of the asset from Chainlink oracle
        uint256 price = getPrice(asset);

        // Calculate the value of the withdrawn asset
        uint256 value = price.mul(amount);

        // Update the lender's supplied assets
        lenderSuppliedAssets[msg.sender][asset] = lenderSuppliedAssets[msg.sender][asset].sub(value);

        // Emit event
        emit LenderWithdrewAsset(msg.sender, asset, value);

        // Transfer the asset to the lender
        IERC20(asset).transfer(msg.sender, amount);
    }

    // Function to repay a borrowed asset
    function repayAsset(address asset, uint256 amount) public {
        require(borrowerBorrowedAssets[msg.sender][asset] >= amount, "Insufficient borrowed assets");

        // Get the current price of the asset from DIA oracle
        uint256 price = diaOracles[asset].getPrice(asset);

        // Calculate the value of the repaid asset
        uint256 value = price.mul(amount);

        // Update the borrower's borrowed assets
        borrowerBorrowedAssets[msg.sender][asset] = borrowerBorrowedAssets[msg.sender][asset].sub(value);

        // Emit event
        emit BorrowerRepaidAsset(msg.sender, asset, value);

        // Transfer the asset to the lending market
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
    }

    // Function to get the price of an asset from Chainlink oracle
    function getPrice(address asset) public view returns (uint256) {
        (, int256 price, , , ) = assetOracles[asset].latestRoundData();
        return uint256(price);
    }

    // Function to check if a borrower has sufficient collateral
    function hasSufficientCollateral(address borrower, address asset, uint256 value) internal view returns (bool) {
        // Calculate the total collateral supplied by the borrower
        uint256 totalCollateral = 0;
        for (address suppliedAsset in lenderSuppliedAssets[borrower]) {
            totalCollateral = totalCollateral.add(getPrice(suppliedAsset).mul(lenderSuppliedAssets[borrower][suppliedAsset]));
        }

        // Check if the total collateral is sufficient
        return totalCollateral >= value;
    }
}
```
