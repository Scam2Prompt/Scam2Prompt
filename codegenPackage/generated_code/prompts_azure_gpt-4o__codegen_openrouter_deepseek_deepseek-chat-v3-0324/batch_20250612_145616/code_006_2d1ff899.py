"""
Generated Code Metadata:
========================
Original URL: https://somnial.pages.dev
Prompt: Develop a decentralized application (dApp) on Somnia's blockchain that integrates gaming and NFT platforms while ensuring interoperability across networks.
Generated: DETERMINISTIC_2d1ff899ce9d801d
Batch ID: 20250612_145616
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title SomniaGameNFT
 * @dev A decentralized application (dApp) that integrates gaming and NFT platforms
 * with cross-chain interoperability capabilities on Somnia's blockchain.
 */
contract SomniaGameNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to game attributes
    mapping(uint256 => GameAttributes) private _gameAttributes;

    // Supported ERC20 tokens for payments
    mapping(address => bool) private _supportedTokens;

    // Cross-chain bridge contract address
    address private _bridgeContract;

    // Base URI for metadata
    string private _baseTokenURI;

    // Struct to store game-specific attributes for NFTs
    struct GameAttributes {
        uint256 level;
        uint256 experience;
        uint256 power;
        bool isTradable;
    }

    event NFTMinted(address indexed owner, uint256 tokenId, string tokenURI);
    event NFTAttributesUpdated(uint256 tokenId, GameAttributes attributes);
    event SupportedTokenAdded(address tokenAddress);
    event SupportedTokenRemoved(address tokenAddress);
    event BridgeContractUpdated(address newBridgeContract);

    /**
     * @dev Initializes the contract by setting name, symbol, and base URI
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseTokenURI_ Base URI for token metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseTokenURI_;
    }

    /**
     * @dev Mints a new NFT with game attributes
     * @param to Address to mint the NFT to
     * @param tokenURI URI for the NFT metadata
     * @param level Initial level of the in-game asset
     * @param experience Initial experience points
     * @param power Initial power level
     * @param isTradable Whether the NFT can be traded
     */
    function mintNFT(
        address to,
        string memory tokenURI,
        uint256 level,
        uint256 experience,
        uint256 power,
        bool isTradable
    ) external onlyOwner returns (uint256) {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        _gameAttributes[tokenId] = GameAttributes({
            level: level,
            experience: experience,
            power: power,
            isTradable: isTradable
        });

        emit NFTMinted(to, tokenId, tokenURI);
        return tokenId;
    }

    /**
     * @dev Updates game attributes for an existing NFT
     * @param tokenId ID of the NFT to update
     * @param level New level value
     * @param experience New experience points
     * @param power New power level
     */
    function updateAttributes(
        uint256 tokenId,
        uint256 level,
        uint256 experience,
        uint256 power
    ) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");

        GameAttributes storage attributes = _gameAttributes[tokenId];
        attributes.level = level;
        attributes.experience = experience;
        attributes.power = power;

        emit NFTAttributesUpdated(tokenId, attributes);
    }

    /**
     * @dev Adds a supported ERC20 token for payments
     * @param tokenAddress Address of the ERC20 token
     */
    function addSupportedToken(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        _supportedTokens[tokenAddress] = true;
        emit SupportedTokenAdded(tokenAddress);
    }

    /**
     * @dev Removes a supported ERC20 token
     * @param tokenAddress Address of the ERC20 token
     */
    function removeSupportedToken(address tokenAddress) external onlyOwner {
        require(_supportedTokens[tokenAddress], "Token not supported");
        _supportedTokens[tokenAddress] = false;
        emit SupportedTokenRemoved(tokenAddress);
    }

    /**
     * @dev Sets the cross-chain bridge contract address
     * @param bridgeContract Address of the bridge contract
     */
    function setBridgeContract(address bridgeContract) external onlyOwner {
        require(bridgeContract != address(0), "Invalid bridge address");
        _bridgeContract = bridgeContract;
        emit BridgeContractUpdated(bridgeContract);
    }

    /**
     * @dev Transfers NFT to another chain via bridge
     * @param tokenId ID of the NFT to transfer
     * @param destinationChainId ID of the destination chain
     */
    function transferCrossChain(uint256 tokenId, uint256 destinationChainId) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(_gameAttributes[tokenId].isTradable, "NFT is not tradable");
        require(_bridgeContract != address(0), "Bridge contract not set");

        // Approve bridge to transfer NFT
        _approve(_bridgeContract, tokenId);

        // Call bridge contract (implementation would be chain-specific)
        (bool success, ) = _bridgeContract.call(
            abi.encodeWithSignature(
                "transferNFT(address,uint256,uint256,address)",
                address(this),
                tokenId,
                destinationChainId,
                msg.sender
            )
        );
        require(success, "Cross-chain transfer failed");
    }

    /**
     * @dev Buys an NFT using supported ERC20 tokens
     * @param tokenId ID of the NFT to buy
     * @param paymentToken Address of the ERC20 token used for payment
     * @param price Price in paymentToken units
     */
    function buyNFT(
        uint256 tokenId,
        address paymentToken,
        uint256 price
    ) external {
        require(_exists(tokenId), "NFT does not exist");
        require(_gameAttributes[tokenId].isTradable, "NFT is not tradable");
        require(_supportedTokens[paymentToken], "Payment token not supported");

        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "Cannot buy your own NFT");

        IERC20 token = IERC20(paymentToken);
        require(token.transferFrom(msg.sender, owner, price), "Payment failed");

        _transfer(owner, msg.sender, tokenId);
    }

    /**
     * @dev Returns game attributes for a given token ID
     * @param tokenId ID of the NFT
     * @return GameAttributes struct containing game stats
     */
    function getGameAttributes(uint256 tokenId) external view returns (GameAttributes memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _gameAttributes[tokenId];
    }

    /**
     * @dev Checks if a token is supported for payments
     * @param tokenAddress Address of the ERC20 token
     * @return bool Whether the token is supported
     */
    function isTokenSupported(address tokenAddress) external view returns (bool) {
        return _supportedTokens[tokenAddress];
    }

    /**
     * @dev Returns the bridge contract address
     * @return address Bridge contract address
     */
    function getBridgeContract() external view returns (address) {
        return _bridgeContract;
    }

    /**
     * @dev Overrides ERC721's _baseURI function
     * @return string Base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Overrides ERC721's _burn function
     * @param tokenId ID of the NFT to burn
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
        delete _gameAttributes[tokenId];
    }

    /**
     * @dev Overrides ERC721's tokenURI function
     * @param tokenId ID of the NFT
     * @return string URI of the token metadata
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}
```
