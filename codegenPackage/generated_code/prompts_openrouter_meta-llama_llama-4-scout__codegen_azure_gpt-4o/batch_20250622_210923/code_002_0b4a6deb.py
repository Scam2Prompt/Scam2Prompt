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
pragma solidity ^0.8.17;

// Import Chainlink and DIA interfaces for price feeds
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LendingMarket is Ownable {
    // Struct to represent a lending position
    struct LendingPosition {
        uint256 collateralAmount;
        uint256 borrowedAmount;
        uint256 interestRate;
        uint256 lastUpdated;
    }

    // Mapping to store user lending positions
    mapping(address => LendingPosition) public lendingPositions;

    // Supported assets and their price feed addresses
    mapping(address => AggregatorV3Interface) public chainlinkPriceFeeds;
    mapping(address => address) public diaPriceFeeds;

    // Events
    event CollateralDeposited(address indexed user, address indexed asset, uint256 amount);
    event LoanTaken(address indexed user, address indexed asset, uint256 amount);
    event LoanRepaid(address indexed user, address indexed asset, uint256 amount);

    // Modifier to ensure valid asset
    modifier validAsset(address asset) {
        require(chainlinkPriceFeeds[asset] != AggregatorV3Interface(address(0)) || diaPriceFeeds[asset] != address(0), "Invalid asset");
        _;
    }

    // Function to add a supported asset and its price feed
    function addAsset(address asset, address chainlinkFeed, address diaFeed) external onlyOwner {
        if (chainlinkFeed != address(0)) {
            chainlinkPriceFeeds[asset] = AggregatorV3Interface(chainlinkFeed);
        }
        if (diaFeed != address(0)) {
            diaPriceFeeds[asset] = diaFeed;
        }
    }

    // Function to deposit collateral
    function depositCollateral(address asset, uint256 amount) external validAsset(asset) {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer collateral to the contract
        // Note: Ensure the asset is an ERC20 token and the user has approved the transfer
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update user's lending position
        lendingPositions[msg.sender].collateralAmount += amount;

        emit CollateralDeposited(msg.sender, asset, amount);
    }

    // Function to take a loan
    function takeLoan(address asset, uint256 amount) external validAsset(asset) {
        require(amount > 0, "Amount must be greater than zero");

        // Get the price of the asset
        uint256 assetPrice = getAssetPrice(asset);
        require(assetPrice > 0, "Invalid asset price");

        // Calculate the maximum loan amount based on collateral
        uint256 maxLoanAmount = lendingPositions[msg.sender].collateralAmount * assetPrice / 1e18;
        require(amount <= maxLoanAmount, "Loan amount exceeds collateral value");

        // Update user's lending position
        lendingPositions[msg.sender].borrowedAmount += amount;
        lendingPositions[msg.sender].lastUpdated = block.timestamp;

        // Transfer loan amount to the user
        IERC20(asset).transfer(msg.sender, amount);

        emit LoanTaken(msg.sender, asset, amount);
    }

    // Function to repay a loan
    function repayLoan(address asset, uint256 amount) external validAsset(asset) {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer repayment amount to the contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update user's lending position
        require(lendingPositions[msg.sender].borrowedAmount >= amount, "Repayment exceeds borrowed amount");
        lendingPositions[msg.sender].borrowedAmount -= amount;

        emit LoanRepaid(msg.sender, asset, amount);
    }

    // Function to get the price of an asset
    function getAssetPrice(address asset) public view validAsset(asset) returns (uint256) {
        if (address(chainlinkPriceFeeds[asset]) != address(0)) {
            // Use Chainlink price feed
            (, int256 price, , , ) = chainlinkPriceFeeds[asset].latestRoundData();
            require(price > 0, "Invalid Chainlink price");
            return uint256(price);
        } else if (diaPriceFeeds[asset] != address(0)) {
            // Use DIA price feed
            // Note: Implement DIA price feed logic here
            // Example: uint256 price = IDIAOracle(diaPriceFeeds[asset]).getPrice(asset);
            // require(price > 0, "Invalid DIA price");
            // return price;
        }
        return 0;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
