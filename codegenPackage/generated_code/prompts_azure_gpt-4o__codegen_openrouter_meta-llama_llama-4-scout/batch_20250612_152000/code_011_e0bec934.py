"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: Write a smart contract that uses Pyth price feeds to calculate expiry prices for options contracts in a DeFi application on Ethereum.
Generated: DETERMINISTIC_e0bec934e5846536
Batch ID: 20250612_152000
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
import "@pythnetwork/pyth-contracts/src/Pyth.sol";

/**
 * @title OptionsContract
 * @author [Your Name]
 * @notice This contract calculates expiry prices for options contracts using Pyth price feeds.
 */
contract OptionsContract {
    using SafeMath for uint256;

    // Mapping of asset addresses to their corresponding Pyth price feed IDs
    mapping(address => bytes32) public assetPriceFeeds;

    // Mapping of option contract addresses to their expiry prices
    mapping(address => uint256) public expiryPrices;

    // Pyth contract instance
    Pyth public pyth;

    /**
     * @notice Constructor
     * @param _pyth Pyth contract address
     */
    constructor(address _pyth) public {
        pyth = Pyth(_pyth);
    }

    /**
     * @notice Set Pyth price feed ID for an asset
     * @param _asset Asset address
     * @param _priceFeedId Pyth price feed ID
     */
    function setAssetPriceFeed(address _asset, bytes32 _priceFeedId) public onlyOwner {
        assetPriceFeeds[_asset] = _priceFeedId;
    }

    /**
     * @notice Calculate expiry price for an option contract
     * @param _optionContract Option contract address
     * @param _underlyingAsset Underlying asset address
     * @return Expiry price
     */
    function calculateExpiryPrice(address _optionContract, address _underlyingAsset) public returns (uint256) {
        // Get Pyth price feed ID for the underlying asset
        bytes32 priceFeedId = assetPriceFeeds[_underlyingAsset];
        require(priceFeedId != bytes32(0), "Price feed ID not set");

        // Get latest price from Pyth
        Pyth.Price memory price = pyth.getPrice(priceFeedId);
        require(price.price != 0, "Invalid price");

        // Calculate expiry price (for simplicity, assume 1:1 ratio)
        uint256 expiryPrice = price.price.mul(10**18); // Adjust decimal places

        // Store expiry price for the option contract
        expiryPrices[_optionContract] = expiryPrice;

        return expiryPrice;
    }

    /**
     * @notice Get expiry price for an option contract
     * @param _optionContract Option contract address
     * @return Expiry price
     */
    function getExpiryPrice(address _optionContract) public view returns (uint256) {
        return expiryPrices[_optionContract];
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    address private _owner;

    function owner() public view returns (address) {
        return _owner;
    }

    constructor() public {
        _owner = msg.sender;
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@pythnetwork/pyth-contracts/src/Pyth.sol";

/**
 * @title OptionsContractDeployed
 * @author [Your Name]
 * @notice Deployment script for OptionsContract
 */
contract OptionsContractDeployed {
    OptionsContract public optionsContract;

    /**
     * @notice Deploy OptionsContract
     */
    constructor() public {
        // Deploy Pyth contract (assuming it's already deployed)
        address pythAddress = 0x...; // Replace with deployed Pyth contract address

        // Deploy OptionsContract
        optionsContract = new OptionsContract(pythAddress);
    }
}
```
