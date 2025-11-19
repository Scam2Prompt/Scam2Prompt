"""
Generated Code Metadata:
========================
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Create a Solidity smart contract for staking NFTs in the ParaX platform's NFT Staking Pool, ensuring compatibility with ERC-721 tokens and integration with Chainlink price feeds.
Generated: DETERMINISTIC_b7a901f4fc3a8edb
Batch ID: 20250612_145619
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

// Importing the ERC721 interface and Chainlink price feed interface
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTStakingPool contract for staking ERC721 tokens
contract NFTStakingPool is Ownable {
    // Struct to hold information about each staked NFT
    struct StakedNFT {
        address owner;
        uint256 tokenId;
        uint256 stakedAt;
    }

    // Mapping from token ID to staked NFT information
    mapping(uint256 => StakedNFT) public stakedNFTs;
    // Array to keep track of all staked token IDs
    uint256[] public stakedTokenIds;

    // Chainlink price feed for ETH/USD
    AggregatorV3Interface internal priceFeed;

    // Events for staking and unstaking
    event Staked(address indexed owner, uint256 indexed tokenId);
    event Unstaked(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the price feed address
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    // Function to stake an NFT
    function stakeNFT(address nftContract, uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        // Transfer the NFT to the contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create a new StakedNFT entry
        stakedNFTs[tokenId] = StakedNFT({
            owner: msg.sender,
            tokenId: tokenId,
            stakedAt: block.timestamp
        });

        // Add the token ID to the staked list
        stakedTokenIds.push(tokenId);

        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstakeNFT(address nftContract, uint256 tokenId) external {
        // Ensure the caller is the owner of the staked NFT
        require(stakedNFTs[tokenId].owner == msg.sender, "You do not own this staked NFT");

        // Remove the NFT from the staked mapping
        delete stakedNFTs[tokenId];

        // Transfer the NFT back to the owner
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        // Emit the unstaked event
        emit Unstaked(msg.sender, tokenId);
    }

    // Function to get the latest ETH price from Chainlink
    function getLatestETHPrice() public view returns (int) {
        (
            /* uint80 roundID */,
            int price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();
        return price;
    }

    // Function to get all staked token IDs
    function getAllStakedTokenIds() external view returns (uint256[] memory) {
        return stakedTokenIds;
    }
}
```
