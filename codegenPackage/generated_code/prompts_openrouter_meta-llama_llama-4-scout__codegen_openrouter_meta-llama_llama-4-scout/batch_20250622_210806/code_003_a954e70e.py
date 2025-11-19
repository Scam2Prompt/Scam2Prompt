"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: Design a smart contract on Ethereum that utilizes Pyth Network's price feeds to update a decentralized perpetuals platform.
Generated: DETERMINISTIC_a954e70e607f7fe9
Batch ID: 20250622_210806
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
 * @title Decentralized Perpetuals Platform
 * @author [Your Name]
 * @notice A decentralized perpetuals platform that utilizes Pyth Network's price feeds.
 */
contract DecentralizedPerpetualsPlatform {
    using SafeMath for uint256;

    // Mapping of assets to their respective price feeds
    mapping(address => bytes32) public assetPriceFeeds;

    // Mapping of assets to their respective collateral requirements
    mapping(address => uint256) public assetCollateralRequirements;

    // Mapping of users to their respective positions
    mapping(address => mapping(address => Position)) public userPositions;

    // Mapping of assets to their respective decimals
    mapping(address => uint256) public assetDecimals;

    // Pyth Network's Pyth contract instance
    Pyth public pyth;

    // Event emitted when a new position is opened
    event NewPosition(address indexed user, address indexed asset, uint256 notionalValue);

    // Event emitted when a position is updated
    event UpdatePosition(address indexed user, address indexed asset, uint256 notionalValue);

    // Event emitted when a position is closed
    event ClosePosition(address indexed user, address indexed asset);

    /**
     * @param _pyth Pyth Network's Pyth contract instance
     */
    constructor(Pyth _pyth) public {
        pyth = _pyth;
    }

    /**
     * @dev Adds a new asset to the platform
     * @param _asset The address of the asset
     * @param _priceFeed The price feed of the asset
     * @param _collateralRequirement The collateral requirement of the asset
     * @param _decimals The number of decimals of the asset
     */
    function addAsset(address _asset, bytes32 _priceFeed, uint256 _collateralRequirement, uint256 _decimals) public onlyOwner {
        assetPriceFeeds[_asset] = _priceFeed;
        assetCollateralRequirements[_asset] = _collateralRequirement;
        assetDecimals[_asset] = _decimals;
    }

    /**
     * @dev Opens a new position for a user
     * @param _asset The address of the asset
     * @param _notionalValue The notional value of the position
     */
    function openPosition(address _asset, uint256 _notionalValue) public {
        require(assetPriceFeeds[_asset] != bytes32(0), "Asset not found");
        require(_notionalValue > 0, "Notional value must be greater than 0");

        // Get the current price of the asset
        uint256 _price = getPrice(_asset);

        // Calculate the collateral required
        uint256 _collateralRequired = _notionalValue.mul(assetCollateralRequirements[_asset]).div(_price);

        // Transfer collateral from user to contract
        IERC20(_asset).transferFrom(msg.sender, address(this), _collateralRequired);

        // Update user's position
        userPositions[msg.sender][_asset] = Position(_notionalValue, _collateralRequired);

        emit NewPosition(msg.sender, _asset, _notionalValue);
    }

    /**
     * @dev Updates a user's position
     * @param _asset The address of the asset
     * @param _notionalValue The new notional value of the position
     */
    function updatePosition(address _asset, uint256 _notionalValue) public {
        require(assetPriceFeeds[_asset] != bytes32(0), "Asset not found");
        require(_notionalValue > 0, "Notional value must be greater than 0");

        // Get the current price of the asset
        uint256 _price = getPrice(_asset);

        // Calculate the collateral required
        uint256 _collateralRequired = _notionalValue.mul(assetCollateralRequirements[_asset]).div(_price);

        // Update user's position
        userPositions[msg.sender][_asset].notionalValue = _notionalValue;
        userPositions[msg.sender][_asset].collateralRequired = _collateralRequired;

        emit UpdatePosition(msg.sender, _asset, _notionalValue);
    }

    /**
     * @dev Closes a user's position
     * @param _asset The address of the asset
     */
    function closePosition(address _asset) public {
        require(assetPriceFeeds[_asset] != bytes32(0), "Asset not found");

        // Transfer collateral back to user
        IERC20(_asset).transfer(msg.sender, userPositions[msg.sender][_asset].collateralRequired);

        // Delete user's position
        delete userPositions[msg.sender][_asset];

        emit ClosePosition(msg.sender, _asset);
    }

    /**
     * @dev Gets the current price of an asset
     * @param _asset The address of the asset
     * @return The current price of the asset
     */
    function getPrice(address _asset) public view returns (uint256) {
        bytes32 _priceFeed = assetPriceFeeds[_asset];
        (, int256 _price, , uint256 _updatedAt, ) = pyth.getPrice(_priceFeed);
        require(_updatedAt > 0, "Price feed not updated");

        // Convert price to 18 decimals
        uint256 _priceWithDecimals = uint256(_price).mul(10**18).div(10**8);

        return _priceWithDecimals;
    }

    /**
     * @dev Structure representing a user's position
     */
    struct Position {
        uint256 notionalValue;
        uint256 collateralRequired;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    address public owner;

    constructor() public {
        owner = msg.sender;
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "./DecentralizedPerpetualsPlatform.sol";

/**
 * @title Decentralized Perpetuals Platform Oracle
 * @author [Your Name]
 * @notice A contract that updates the prices of assets on the decentralized perpetuals platform.
 */
contract DecentralizedPerpetualsPlatformOracle {
    using SafeMath for uint256;

    // Mapping of assets to their respective price feeds
    mapping(address => bytes32) public assetPriceFeeds;

    // Decentralized Perpetuals Platform contract instance
    DecentralizedPerpetualsPlatform public platform;

    /**
     * @param _platform Decentralized Perpetuals Platform contract instance
     */
    constructor(DecentralizedPerpetualsPlatform _platform) public {
        platform = _platform;
    }

    /**
     * @dev Updates the prices of all assets on the platform
     */
    function updatePrices() public {
        // Get all assets on the platform
        address[] memory _assets = platform.getAssets();

        // Update price for each asset
        for (uint256 i = 0; i < _assets.length; i++) {
            updatePrice(_assets[i]);
        }
    }

    /**
     * @dev Updates the price of an asset on the platform
     * @param _asset The address of the asset
     */
    function updatePrice(address _asset) public {
        // Get the current price of the asset
        uint256 _price = platform.getPrice(_asset);

        // Update the price feed of the asset
        assetPriceFeeds[_asset] = _price;
    }
}
```

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  // Deploy Pyth contract
  const Pyth = await ethers.getContractFactory("Pyth");
  const pyth = await Pyth.deploy();
  await pyth.deployed();

  // Deploy decentralized perpetuals platform contract
  const DecentralizedPerpetualsPlatform = await ethers.getContractFactory("DecentralizedPerpetualsPlatform");
  const platform = await DecentralizedPerpetualsPlatform.deploy(pyth.address);
  await platform.deployed();

  // Deploy decentralized perpetuals platform oracle contract
  const DecentralizedPerpetualsPlatformOracle = await ethers.getContractFactory("DecentralizedPerpetualsPlatformOracle");
  const oracle = await DecentralizedPerpetualsPlatformOracle.deploy(platform.address);
  await oracle.deployed();

  console.log("Pyth contract deployed to:", pyth.address);
  console.log("Decentralized perpetuals platform contract deployed to:", platform.address);
  console.log("Decentralized perpetuals platform oracle contract deployed to:", oracle.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
