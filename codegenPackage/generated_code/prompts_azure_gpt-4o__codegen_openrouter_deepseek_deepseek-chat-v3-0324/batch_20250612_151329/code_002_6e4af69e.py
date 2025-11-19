"""
Generated Code Metadata:
========================
Original URL: https://metamask-two.vercel.app
Prompt: Develop a smart contract in Solidity that supports limited edition NFT drops (e.g., 10 editions for "The Decay"), as outlined in the content.
Generated: DETERMINISTIC_6e4af69ea84a28e9
Batch ID: 20250612_151329
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

contract LimitedEditionNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Edition {
        string name;
        uint256 maxSupply;
        uint256 currentSupply;
        string baseURI;
        bool isActive;
    }

    mapping(string => Edition) public editions;
    mapping(uint256 => string) private _tokenEdition;

    event EditionCreated(string name, uint256 maxSupply);
    event EditionMinted(address to, string editionName, uint256 tokenId);

    constructor() ERC721("LimitedEditionNFT", "LENFT") {}

    /**
     * @dev Creates a new limited edition
     * @param name Name of the edition
     * @param maxSupply Maximum number of tokens for this edition
     * @param baseURI Base URI for token metadata
     */
    function createEdition(
        string memory name,
        uint256 maxSupply,
        string memory baseURI
    ) external onlyOwner {
        require(bytes(name).length > 0, "Edition name cannot be empty");
        require(maxSupply > 0, "Max supply must be greater than 0");
        require(editions[name].maxSupply == 0, "Edition already exists");

        editions[name] = Edition({
            name: name,
            maxSupply: maxSupply,
            currentSupply: 0,
            baseURI: baseURI,
            isActive: true
        });

        emit EditionCreated(name, maxSupply);
    }

    /**
     * @dev Mints a token from a specific edition
     * @param to Address to receive the token
     * @param editionName Name of the edition to mint from
     */
    function mint(address to, string memory editionName) external {
        Edition storage edition = editions[editionName];
        require(edition.maxSupply > 0, "Edition does not exist");
        require(edition.isActive, "Edition is not active");
        require(
            edition.currentSupply < edition.maxSupply,
            "Edition supply exhausted"
        );

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
        _tokenEdition[tokenId] = editionName;
        edition.currentSupply++;

        emit EditionMinted(to, editionName, tokenId);
    }

    /**
     * @dev Toggles the active status of an edition
     * @param editionName Name of the edition to toggle
     */
    function toggleEditionActive(string memory editionName) external onlyOwner {
        Edition storage edition = editions[editionName];
        require(edition.maxSupply > 0, "Edition does not exist");
        edition.isActive = !edition.isActive;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId ID of the token to query
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );

        string memory editionName = _tokenEdition[tokenId];
        Edition memory edition = editions[editionName];

        return
            bytes(edition.baseURI).length > 0
                ? string(
                    abi.encodePacked(edition.baseURI, Strings.toString(tokenId))
                )
                : "";
    }

    /**
     * @dev Returns the edition details for a given token ID
     * @param tokenId ID of the token to query
     */
    function getTokenEdition(uint256 tokenId)
        external
        view
        returns (Edition memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: Edition query for nonexistent token"
        );

        string memory editionName = _tokenEdition[tokenId];
        return editions[editionName];
    }

    /**
     * @dev Returns the current token count
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
