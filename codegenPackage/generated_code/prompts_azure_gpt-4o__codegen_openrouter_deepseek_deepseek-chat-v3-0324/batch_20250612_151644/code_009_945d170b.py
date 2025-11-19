"""
Generated Code Metadata:
========================
Original URL: https://zerobeings.app
Prompt: Recommend best practices for creating a verified smart contract for an NFT project, inspired by "Zero Beings."
Generated: DETERMINISTIC_945d170b04b2802a
Batch ID: 20250612_151644
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ZeroBeingsNFT
 * @dev A verified NFT contract implementing best practices inspired by Zero Beings
 */
contract ZeroBeingsNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Contract metadata
    string public baseURI;
    string public contractURI;
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant PRICE = 0.08 ether;
    uint256 public constant MAX_PER_MINT = 10;
    bool public saleIsActive = false;

    // Events
    event Minted(address indexed to, uint256 tokenId);
    event BaseURIChanged(string newBaseURI);
    event ContractURIChanged(string newContractURI);
    event SaleStateChanged(bool newState);

    /**
     * @dev Initialize contract with name, symbol, and metadata URIs
     */
    constructor(
        string memory _name,
        string memory _symbol,
        string memory _initBaseURI,
        string memory _initContractURI
    ) ERC721(_name, _symbol) {
        baseURI = _initBaseURI;
        contractURI = _initContractURI;
    }

    /**
     * @dev Base URI for computing tokenURI
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Mint NFTs (public sale)
     */
    function mint(uint256 quantity) external payable nonReentrant {
        require(saleIsActive, "Sale is not active");
        require(quantity > 0 && quantity <= MAX_PER_MINT, "Invalid quantity");
        require(_tokenIdCounter.current() + quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= PRICE * quantity, "Insufficient payment");

        _mintNFTs(msg.sender, quantity);
    }

    /**
     * @dev Mint NFTs (owner only)
     */
    function reserve(uint256 quantity, address to) external onlyOwner {
        require(_tokenIdCounter.current() + quantity <= MAX_SUPPLY, "Exceeds max supply");
        _mintNFTs(to, quantity);
    }

    /**
     * @dev Internal mint function
     */
    function _mintNFTs(address to, uint256 quantity) internal {
        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(to, tokenId);
            emit Minted(to, tokenId);
        }
    }

    /**
     * @dev Set base URI for token metadata
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        baseURI = newBaseURI;
        emit BaseURIChanged(newBaseURI);
    }

    /**
     * @dev Set contract URI for marketplace metadata
     */
    function setContractURI(string memory newContractURI) external onlyOwner {
        contractURI = newContractURI;
        emit ContractURIChanged(newContractURI);
    }

    /**
     * @dev Toggle sale state
     */
    function toggleSaleState() external onlyOwner {
        saleIsActive = !saleIsActive;
        emit SaleStateChanged(saleIsActive);
    }

    /**
     * @dev Withdraw contract balance
     */
    function withdraw() external onlyOwner nonReentrant {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Override supportsInterface for ERC721 and Ownable
     */
    function supportsInterface(bytes4 interfaceId) public view override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
