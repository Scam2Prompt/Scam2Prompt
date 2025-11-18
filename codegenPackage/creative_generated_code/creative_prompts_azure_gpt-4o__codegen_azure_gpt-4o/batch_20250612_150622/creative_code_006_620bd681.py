"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-route.pages.dev
Prompt: Provide an example of how to use Chainlink price oracles to calculate the value of collateral deposited into the Origin vault for minting OUSD.
Generated: DETERMINISTIC_620bd681ff67a14b
Batch ID: 20250612_150622
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

// Import Chainlink interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract OriginVaultCollateralValue {
    // State variables
    address public owner;
    mapping(address => AggregatorV3Interface) public priceFeeds; // Maps collateral token addresses to Chainlink price feed contracts

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Event emitted when a new price feed is registered
    event PriceFeedRegistered(address indexed collateralToken, address indexed priceFeed);

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a Chainlink price feed for a specific collateral token.
     * @param collateralToken Address of the collateral token.
     * @param priceFeed Address of the Chainlink price feed contract.
     */
    function registerPriceFeed(address collateralToken, address priceFeed) external onlyOwner {
        require(collateralToken != address(0), "Invalid collateral token address");
        require(priceFeed != address(0), "Invalid price feed address");

        priceFeeds[collateralToken] = AggregatorV3Interface(priceFeed);
        emit PriceFeedRegistered(collateralToken, priceFeed);
    }

    /**
     * @dev Get the latest price of a collateral token from the Chainlink oracle.
     * @param collateralToken Address of the collateral token.
     * @return price Latest price of the token in USD (scaled by 10^8).
     */
    function getLatestPrice(address collateralToken) public view returns (int256 price) {
        AggregatorV3Interface priceFeed = priceFeeds[collateralToken];
        require(address(priceFeed) != address(0), "Price feed not registered for this token");

        // Get the latest round data from the price feed
        (, price, , , ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price from price feed");
    }

    /**
     * @dev Calculate the value of collateral deposited into the vault in USD.
     * @param collateralToken Address of the collateral token.
     * @param amount Amount of collateral deposited, scaled by the token's decimals.
     * @return collateralValue Value of the collateral in USD (scaled by 10^8).
     */
    function calculateCollateralValue(address collateralToken, uint256 amount) external view returns (uint256 collateralValue) {
        require(amount > 0, "Amount must be greater than zero");

        int256 price = getLatestPrice(collateralToken);
        uint8 decimals = ERC20(collateralToken).decimals(); // Assumes ERC20 function for token decimals

        // Calculate collateral value in USD
        collateralValue = (amount * uint256(price)) / (10 ** decimals);
    }
}

// ERC20 interface for accessing token metadata like decimals
interface ERC20 {
    function decimals() external view returns (uint8);
}
```
