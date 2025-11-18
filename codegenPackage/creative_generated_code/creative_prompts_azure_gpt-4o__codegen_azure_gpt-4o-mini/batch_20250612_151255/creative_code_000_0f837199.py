"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appparax.pages.dev
Prompt: Write a smart contract for NFT collateralization and lending based on the risk parameters outlined in ParaX's documentation, using Chainlink oracles for floor price estimation.
Generated: DETERMINISTIC_0f83719931fd4a9b
Batch ID: 20250612_151255
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

// Importing interfaces for ERC721 and Chainlink Aggregator
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract NFTCollateralLending {
    // Structure to hold NFT collateral information
    struct Collateral {
        address nftContract;
        uint256 tokenId;
        address owner;
        uint256 loanAmount;
        uint256 collateralValue;
        bool isActive;
    }

    // Mapping of collateral ID to Collateral information
    mapping(uint256 => Collateral) public collaterals;
    uint256 public collateralIdCounter;

    // Chainlink price feed address for floor price estimation
    AggregatorV3Interface internal priceFeed;

    // Events for logging
    event Collateralized(uint256 indexed collateralId, address indexed owner, address nftContract, uint256 tokenId, uint256 loanAmount);
    event LoanRepaid(uint256 indexed collateralId, address indexed owner);
    event CollateralWithdrawn(uint256 indexed collateralId, address indexed owner);

    // Constructor to initialize the Chainlink price feed
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    // Function to collateralize NFT
    function collateralizeNFT(address _nftContract, uint256 _tokenId, uint256 _loanAmount) external {
        // Ensure loan amount is greater than zero
        require(_loanAmount > 0, "Loan amount must be greater than zero.");

        // Verify ownership of the NFT
        IERC721 nft = IERC721(_nftContract);
        require(nft.ownerOf(_tokenId) == msg.sender, "You do not own this NFT.");
        require(nft.getApproved(_tokenId) == address(this), "Contract is not approved to manage the NFT.");

        // Get the floor price from Chainlink
        (, int256 price, , ,) = priceFeed.latestRoundData();
        uint256 collateralValue = uint256(price);

        // Create a new collateral entry
        collaterals[collateralIdCounter] = Collateral({
            nftContract: _nftContract,
            tokenId: _tokenId,
            owner: msg.sender,
            loanAmount: _loanAmount,
            collateralValue: collateralValue,
            isActive: true
        });

        // Transfer the NFT to the contract
        nft.transferFrom(msg.sender, address(this), _tokenId);

        emit Collateralized(collateralIdCounter, msg.sender, _nftContract, _tokenId, _loanAmount);
        collateralIdCounter++;
    }

    // Function to repay loan and withdraw collateral
    function repayLoan(uint256 _collateralId) external {
        Collateral storage collateral = collaterals[_collateralId];

        // Ensure the collateral entry is active and owned by the caller
        require(collateral.isActive, "Collateral is not active.");
        require(collateral.owner == msg.sender, "You do not own this collateral.");

        // Transfer the loan amount back to the lender (this is simplified, in production it should handle actual lending)
        // (Consider implementing a more robust lending mechanism)

        // Mark the collateral as inactive and transfer the NFT back to the owner
        collateral.isActive = false;
        IERC721(collateral.nftContract).transferFrom(address(this), msg.sender, collateral.tokenId);

        emit LoanRepaid(_collateralId, msg.sender);
    }

    // Function to withdraw NFT collateral if loan is paid
    function withdrawCollateral(uint256 _collateralId) external {
        Collateral storage collateral = collaterals[_collateralId];

        // Ensure collateral entry is inactive and owned by the caller
        require(!collateral.isActive, "Collateral is still active.");
        require(collateral.owner == msg.sender, "You do not own this collateral.");

        // Transfer the NFT back to the owner
        IERC721(collateral.nftContract).transferFrom(address(this), msg.sender, collateral.tokenId);

        emit CollateralWithdrawn(_collateralId, msg.sender);
    }

    // Function to get the current floor price of the NFT (for risk assessment)
    function getCurrentFloorPrice() public view returns (uint256) {
        (, int256 price, , ,) = priceFeed.latestRoundData();
        return uint256(price);
    }
}
```
