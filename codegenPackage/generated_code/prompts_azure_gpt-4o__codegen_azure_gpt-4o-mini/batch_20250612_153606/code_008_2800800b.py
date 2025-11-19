"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Provide an example of how to use the ERC404 token standard to create a dynamic NFT collection that interacts with DeFi protocols like Uniswap V3.
Generated: DETERMINISTIC_2800800b7765e924
Batch ID: 20250612_153606
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@uniswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";
import "@uniswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";

// ERC404 Token Standard Interface
interface IERC404 {
    function mint(address to, uint256 tokenId, string memory metadata) external;
    function burn(uint256 tokenId) external;
}

// Dynamic NFT Collection Contract
contract DynamicNFTCollection is ERC721Enumerable, Ownable, IERC404 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata
    mapping(uint256 => string) private _tokenMetadata;

    // Uniswap V3 Position Manager
    INonfungiblePositionManager public positionManager;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string metadata);

    // Constructor to initialize the contract
    constructor(address _positionManager) ERC721("DynamicNFT", "DNFT") {
        positionManager = INonfungiblePositionManager(_positionManager);
    }

    // Function to mint a new NFT
    function mint(address to, uint256 tokenId, string memory metadata) external override onlyOwner {
        require(to != address(0), "Invalid address");
        require(!_exists(tokenId), "Token already exists");

        _tokenIdCounter.increment();
        _mint(to, tokenId);
        _tokenMetadata[tokenId] = metadata;

        emit NFTMinted(to, tokenId, metadata);
    }

    // Function to burn an NFT
    function burn(uint256 tokenId) external override onlyOwner {
        require(_exists(tokenId), "Token does not exist");

        _burn(tokenId);
        delete _tokenMetadata[tokenId];
    }

    // Function to get metadata of a token
    function getTokenMetadata(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenMetadata[tokenId];
    }

    // Function to create a new Uniswap V3 position
    function createUniswapPosition(
        uint256 tokenId,
        uint256 amount0,
        uint256 amount1,
        int24 tickLower,
        int24 tickUpper
    ) external onlyOwner {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        // Create the position parameters
        INonfungiblePositionManager.MintParams memory params = INonfungiblePositionManager.MintParams({
            token0: address(0), // Replace with actual token address
            token1: address(0), // Replace with actual token address
            fee: 3000, // Example fee tier
            tickLower: tickLower,
            tickUpper: tickUpper,
            amount0Desired: amount0,
            amount1Desired: amount1,
            amount0Min: 0,
            amount1Min: 0,
            recipient: address(this),
            deadline: block.timestamp + 15 minutes
        });

        // Mint the position
        (uint256 tokenIdPosition, , , ) = positionManager.mint(params);
        // Logic to associate the NFT with the Uniswap position can be added here
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the owner
        IERC20(token).transfer(owner(), amount);
    }
}
```
