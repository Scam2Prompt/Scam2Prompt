"""
Generated Code Metadata:
========================
Original URL: https://oeth-route.pages.dev
Prompt: Provide an example of how to use Chainlink price oracles to calculate the value of collateral deposited into the Origin vault for minting OUSD.
Generated: DETERMINISTIC_620bd681ff67a14b
Batch ID: 20250612_150622
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CollateralValueCalculator is Ownable {
    // Mapping of collateral token addresses to their Chainlink price feed addresses
    mapping(address => address) public priceFeeds;
    
    // OUSD token address
    address public immutable ousd;
    
    // Minimum collateralization ratio (e.g., 150% = 15000)
    uint256 public constant MIN_COLLATERAL_RATIO = 15000;
    uint256 public constant RATIO_DIVISOR = 100;
    
    event PriceFeedUpdated(address indexed token, address indexed priceFeed);
    
    constructor(address _ousd) {
        require(_ousd != address(0), "Invalid OUSD address");
        ousd = _ousd;
    }
    
    /**
     * @dev Set the Chainlink price feed for a collateral token
     * @param token Address of the collateral token
     * @param priceFeed Address of the Chainlink price feed
     */
    function setPriceFeed(address token, address priceFeed) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(priceFeed != address(0), "Invalid price feed address");
        priceFeeds[token] = priceFeed;
        emit PriceFeedUpdated(token, priceFeed);
    }
    
    /**
     * @dev Get the latest price of a token from Chainlink
     * @param token Address of the token
     * @return price The latest price (with 8 decimals)
     */
    function getLatestPrice(address token) public view returns (int256) {
        address priceFeed = priceFeeds[token];
        require(priceFeed != address(0), "Price feed not set");
        
        AggregatorV3Interface priceFeedContract = AggregatorV3Interface(priceFeed);
        (
            /* uint80 roundID */,
            int256 price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeedContract.latestRoundData();
        
        require(price > 0, "Invalid price");
        return price;
    }
    
    /**
     * @dev Calculate the USD value of collateral deposited
     * @param token Address of the collateral token
     * @param amount Amount of collateral tokens deposited
     * @return value USD value of the collateral (with 18 decimals)
     */
    function calculateCollateralValue(address token, uint256 amount) external view returns (uint256) {
        require(amount > 0, "Amount must be greater than 0");
        
        int256 price = getLatestPrice(token);
        uint256 tokenDecimals = IERC20(token).decimals();
        
        // Convert price to 18 decimals and calculate value
        uint256 adjustedPrice = uint256(price) * (10 ** (18 - 8)); // Chainlink uses 8 decimals
        uint256 value = (amount * adjustedPrice) / (10 ** tokenDecimals);
        
        return value;
    }
    
    /**
     * @dev Calculate the maximum OUSD that can be minted for given collateral
     * @param token Address of the collateral token
     * @param amount Amount of collateral tokens deposited
     * @return maxOusd Maximum OUSD that can be minted (with 18 decimals)
     */
    function calculateMaxOusdToMint(address token, uint256 amount) external view returns (uint256) {
        uint256 collateralValue = calculateCollateralValue(token, amount);
        uint256 maxOusd = (collateralValue * RATIO_DIVISOR) / MIN_COLLATERAL_RATIO;
        return maxOusd;
    }
    
    /**
     * @dev Check if collateral is sufficient for minting OUSD amount
     * @param token Address of the collateral token
     * @param amount Amount of collateral tokens deposited
     * @param ousdAmount Amount of OUSD to mint
     * @return bool True if collateral is sufficient
     */
    function isCollateralSufficient(
        address token,
        uint256 amount,
        uint256 ousdAmount
    ) external view returns (bool) {
        uint256 collateralValue = calculateCollateralValue(token, amount);
        uint256 requiredValue = (ousdAmount * MIN_COLLATERAL_RATIO) / RATIO_DIVISOR;
        return collateralValue >= requiredValue;
    }
}
```
