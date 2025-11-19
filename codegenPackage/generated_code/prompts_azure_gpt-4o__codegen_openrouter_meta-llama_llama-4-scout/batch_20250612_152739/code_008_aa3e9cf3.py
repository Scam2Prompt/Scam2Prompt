"""
Generated Code Metadata:
========================
Original URL: https://allianceblock-ahz.pages.dev
Prompt: Write a smart contract that enables tokenized financing of art, cars, and collectibles through on-chain options, inspired by Arkefi AG's platform on AllianceBlock.
Generated: DETERMINISTIC_aa3e9cf3d1494ca1
Batch ID: 20250612_152739
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Tokenized Asset Financing Contract
 * @author [Your Name]
 * @notice Enables tokenized financing of art, cars, and collectibles through on-chain options.
 */
contract TokenizedAssetFinancing {
    using SafeMath for uint256;
    using SafeERC721 for IERC721;
    using SafeERC20 for IERC20;

    // Mapping of asset owners to their respective assets
    mapping(address => Asset) public assets;

    // Mapping of option contracts to their respective assets
    mapping(address => OptionContract) public optionContracts;

    // Mapping of buyers to their respective option contracts
    mapping(address => OptionContract[]) public buyerOptionContracts;

    // Event emitted when an asset is added
    event AssetAdded(address indexed owner, address indexed asset);

    // Event emitted when an option contract is created
    event OptionContractCreated(address indexed asset, address indexed optionContract);

    // Event emitted when an option contract is exercised
    event OptionContractExercised(address indexed buyer, address indexed optionContract);

    // Event emitted when an option contract expires
    event OptionContractExpired(address indexed optionContract);

    /**
     * @dev Represents an asset
     */
    struct Asset {
        address assetAddress; // Address of the asset (e.g. ERC721)
        uint256 assetId; // ID of the asset
        address owner; // Owner of the asset
    }

    /**
     * @dev Represents an option contract
     */
    struct OptionContract {
        address assetAddress; // Address of the underlying asset
        uint256 assetId; // ID of the underlying asset
        address buyer; // Buyer of the option contract
        uint256 strikePrice; // Strike price of the option contract
        uint256 expirationTime; // Expiration time of the option contract
        bool isExercised; // Whether the option contract has been exercised
    }

    /**
     * @dev Adds an asset to the platform
     * @param _assetAddress Address of the asset (e.g. ERC721)
     * @param _assetId ID of the asset
     */
    function addAsset(address _assetAddress, uint256 _assetId) public {
        require(IERC721(_assetAddress).ownerOf(_assetId) == msg.sender, "Only the asset owner can add the asset");

        Asset memory asset;
        asset.assetAddress = _assetAddress;
        asset.assetId = _assetId;
        asset.owner = msg.sender;

        assets[msg.sender] = asset;

        emit AssetAdded(msg.sender, _assetAddress);
    }

    /**
     * @dev Creates an option contract for an asset
     * @param _assetAddress Address of the underlying asset
     * @param _assetId ID of the underlying asset
     * @param _buyer Buyer of the option contract
     * @param _strikePrice Strike price of the option contract
     * @param _expirationTime Expiration time of the option contract
     */
    function createOptionContract(address _assetAddress, uint256 _assetId, address _buyer, uint256 _strikePrice, uint256 _expirationTime) public {
        require(assets[msg.sender].assetAddress == _assetAddress && assets[msg.sender].assetId == _assetId, "Only the asset owner can create an option contract");

        OptionContract memory optionContract;
        optionContract.assetAddress = _assetAddress;
        optionContract.assetId = _assetId;
        optionContract.buyer = _buyer;
        optionContract.strikePrice = _strikePrice;
        optionContract.expirationTime = _expirationTime;
        optionContract.isExercised = false;

        optionContracts[_buyer] = optionContract;

        buyerOptionContracts[_buyer].push(optionContract);

        emit OptionContractCreated(_assetAddress, _buyer);
    }

    /**
     * @dev Exercises an option contract
     * @param _optionContractAddress Address of the option contract
     */
    function exerciseOptionContract(address _optionContractAddress) public {
        require(optionContracts[_optionContractAddress].isExercised == false, "Option contract has already been exercised");
        require(optionContracts[_optionContractAddress].expirationTime > block.timestamp, "Option contract has expired");

        OptionContract memory optionContract = optionContracts[_optionContractAddress];

        // Transfer asset to buyer
        IERC721(optionContract.assetAddress).safeTransferFrom(msg.sender, optionContract.buyer, optionContract.assetId);

        optionContract.isExercised = true;

        emit OptionContractExercised(msg.sender, _optionContractAddress);
    }

    /**
     * @dev Expires an option contract
     * @param _optionContractAddress Address of the option contract
     */
    function expireOptionContract(address _optionContractAddress) public {
        require(optionContracts[_optionContractAddress].expirationTime <= block.timestamp, "Option contract has not expired");

        OptionContract memory optionContract = optionContracts[_optionContractAddress];

        optionContract.isExercised = true;

        emit OptionContractExpired(_optionContractAddress);
    }
}
```
