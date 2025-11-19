"""
Generated Code Metadata:
========================
Original URL: https://evm-zeta.vercel.app
Prompt: Write a script to handle NFT minting and transfer issues, inspired by the NFT-related features on the EVM Zeta platform.
Generated: DETERMINISTIC_e591d0f7baea7165
Batch ID: 20250612_161356
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title ZetaNFT
 * @dev ERC721 token with minting and transfer functionality
 */
contract ZetaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;
    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MINT_PRICE = 0.01 ether;
    bool public mintingPaused = false;

    // Mapping from token ID to custom metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Events
    event Minted(address indexed to, uint256 indexed tokenId);
    event BatchMinted(address indexed to, uint256[] tokenIds);
    event TransferWithMetadata(
        address indexed from,
        address indexed to,
        uint256 indexed tokenId,
        string metadata
    );

    /**
     * @dev Constructor
     * @param name_ Name of the NFT
     * @param symbol_ Symbol of the NFT
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
     * @dev Mint a single NFT
     * @param to Address to mint the NFT to
     * @param customURI Optional custom metadata URI
     */
    function mint(address to, string memory customURI) external payable {
        require(!mintingPaused, "Minting is paused");
        require(msg.value >= MINT_PRICE, "Insufficient payment");
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);

        if (bytes(customURI).length > 0) {
            _tokenURIs[tokenId] = customURI;
        }

        emit Minted(to, tokenId);
    }

    /**
     * @dev Mint multiple NFTs in a batch
     * @param to Address to mint the NFTs to
     * @param count Number of NFTs to mint
     */
    function batchMint(address to, uint256 count) external payable onlyOwner {
        require(!mintingPaused, "Minting is paused");
        require(totalSupply() + count <= MAX_SUPPLY, "Exceeds max supply");

        uint256[] memory tokenIds = new uint256[](count);
        for (uint256 i = 0; i < count; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(to, tokenId);
            tokenIds[i] = tokenId;
        }

        emit BatchMinted(to, tokenIds);
    }

    /**
     * @dev Transfer NFT with additional metadata
     * @param from Address transferring the NFT
     * @param to Address receiving the NFT
     * @param tokenId ID of the NFT being transferred
     * @param metadata Additional metadata for the transfer
     */
    function transferWithMetadata(
        address from,
        address to,
        uint256 tokenId,
        string memory metadata
    ) external {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "Caller is not owner nor approved"
        );
        _transfer(from, to, tokenId);
        emit TransferWithMetadata(from, to, tokenId, metadata);
    }

    /**
     * @dev Get total supply of minted NFTs
     * @return uint256 Total supply
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Get token URI for a given token ID
     * @param tokenId ID of the token
     * @return string Token URI
     */
    function tokenURI(uint256 tokenId)
        public
        view
        virtual
        override
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );

        if (bytes(_tokenURIs[tokenId]).length > 0) {
            return _tokenURIs[tokenId];
        }

        return
            bytes(_baseTokenURI).length > 0
                ? string(
                    abi.encodePacked(_baseTokenURI, tokenId.toString(), ".json")
                )
                : "";
    }

    /**
     * @dev Set base token URI
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Toggle minting pause state
     */
    function toggleMintingPause() external onlyOwner {
        mintingPaused = !mintingPaused;
    }

    /**
     * @dev Withdraw contract balance
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Override supportsInterface for ERC721 and Ownable
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
