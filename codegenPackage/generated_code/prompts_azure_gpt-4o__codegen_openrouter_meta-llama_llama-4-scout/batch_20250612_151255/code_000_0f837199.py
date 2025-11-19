"""
Generated Code Metadata:
========================
Original URL: https://appparax.pages.dev
Prompt: Write a smart contract for NFT collateralization and lending based on the risk parameters outlined in ParaX's documentation, using Chainlink oracles for floor price estimation.
Generated: DETERMINISTIC_0f83719931fd4a9b
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code for the smart contract:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/Oracle.sol";

/**
 * @title NFT Collateralization and Lending Contract
 * @author [Your Name]
 * @notice This contract enables NFT collateralization and lending based on ParaX's risk parameters.
 * @dev This contract uses Chainlink oracles for floor price estimation.
 */
contract NFTCollateralizedLending {
    // Mapping of NFT owners to their collateralized NFTs
    mapping(address => mapping(uint256 => NFT)) public collateralizedNFTs;

    // Mapping of lenders to their lent assets
    mapping(address => mapping(uint256 => Lend)) public lentAssets;

    // Mapping of oracle addresses to their corresponding NFT contracts
    mapping(address => address) public oracleNFTContracts;

    // Risk parameters
    uint256 public liquidationThreshold; // 80% (e.g., 80)
    uint256 public liquidationPenalty; // 10% (e.g., 10)
    uint256 public interestRate; // 5% (e.g., 5)

    // Events
    event NFTCollateralized(address indexed owner, uint256 indexed nftId);
    event NFTUncollateralized(address indexed owner, uint256 indexed nftId);
    event Lend(address indexed lender, uint256 indexed lendId);
    event Liquidation(address indexed liquidator, uint256 indexed nftId);

    // Structs
    struct NFT {
        uint256 id;
        address nftContract;
        uint256 floorPrice;
    }

    struct Lend {
        uint256 id;
        address lender;
        uint256 amount;
        uint256 interest;
        uint256 duration;
    }

    // Functions

    /**
     * @notice Collateralize an NFT
     * @param _nftContract The NFT contract address
     * @param _nftId The NFT ID
     */
    function collateralizeNFT(address _nftContract, uint256 _nftId) public {
        require(IERC721(_nftContract).ownerOf(_nftId) == msg.sender, "Only the NFT owner can collateralize it");

        // Get the floor price from the Chainlink oracle
        uint256 floorPrice = getFloorPrice(_nftContract);

        // Create an NFT struct
        NFT memory nft = NFT(_nftId, _nftContract, floorPrice);

        // Add the NFT to the collateralized NFTs mapping
        collateralizedNFTs[msg.sender][_nftId] = nft;

        // Emit an event
        emit NFTCollateralized(msg.sender, _nftId);
    }

    /**
     * @notice Uncollateralize an NFT
     * @param _nftId The NFT ID
     */
    function uncollateralizeNFT(uint256 _nftId) public {
        require(collateralizedNFTs[msg.sender][_nftId].id != 0, "NFT is not collateralized");

        // Remove the NFT from the collateralized NFTs mapping
        delete collateralizedNFTs[msg.sender][_nftId];

        // Emit an event
        emit NFTUncollateralized(msg.sender, _nftId);
    }

    /**
     * @notice Lend assets
     * @param _nftContract The NFT contract address
     * @param _nftId The NFT ID
     * @param _amount The lend amount
     * @param _duration The lend duration
     */
    function lend(address _nftContract, uint256 _nftId, uint256 _amount, uint256 _duration) public {
        require(collateralizedNFTs[msg.sender][_nftId].id != 0, "NFT is not collateralized");

        // Get the floor price from the Chainlink oracle
        uint256 floorPrice = getFloorPrice(_nftContract);

        // Calculate the liquidation threshold
        uint256 liquidationThresholdValue = floorPrice * liquidationThreshold / 100;

        // Check if the lend amount is within the liquidation threshold
        require(_amount <= liquidationThresholdValue, "Lend amount exceeds liquidation threshold");

        // Create a Lend struct
        Lend memory lend = Lend(
            lentAssets[msg.sender].length,
            msg.sender,
            _amount,
            _amount * interestRate / 100 * _duration / 365,
            _duration
        );

        // Add the lend to the lent assets mapping
        lentAssets[msg.sender][lend.id] = lend;

        // Emit an event
        emit Lend(msg.sender, lend.id);
    }

    /**
     * @notice Liquidate an NFT
     * @param _nftContract The NFT contract address
     * @param _nftId The NFT ID
     */
    function liquidate(address _nftContract, uint256 _nftId) public {
        require(collateralizedNFTs[msg.sender][_nftId].id != 0, "NFT is not collateralized");

        // Get the floor price from the Chainlink oracle
        uint256 floorPrice = getFloorPrice(_nftContract);

        // Calculate the liquidation penalty
        uint256 liquidationPenaltyValue = floorPrice * liquidationPenalty / 100;

        // Transfer the NFT to the liquidator
        IERC721(_nftContract).safeTransferFrom(msg.sender, _nftContract, _nftId);

        // Emit an event
        emit Liquidation(msg.sender, _nftId);
    }

    /**
     * @notice Get the floor price of an NFT from the Chainlink oracle
     * @param _nftContract The NFT contract address
     * @return The floor price
     */
    function getFloorPrice(address _nftContract) internal view returns (uint256) {
        address oracleAddress = oracleNFTContracts[_nftContract];
        require(oracleAddress != address(0), "Oracle not found for NFT contract");

        (, int256 floorPrice, , , ) = AggregatorV3Interface(oracleAddress).latestRoundData();
        return uint256(floorPrice);
    }
}
```
