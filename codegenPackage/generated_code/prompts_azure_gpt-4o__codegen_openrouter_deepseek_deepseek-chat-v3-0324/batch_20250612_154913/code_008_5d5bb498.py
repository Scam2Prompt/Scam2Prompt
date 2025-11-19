"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Generate an example of how to use Linea's zk rollup to collateralize NFTs at scale, ensuring compatibility with Ethereum wallets and IDEs.
Generated: DETERMINISTIC_5d5bb498e8d51053
Batch ID: 20250612_154913
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/draft-EIP712.sol";

/**
 * @title CollateralizedNFT
 * @dev ERC721 token that can be collateralized on Linea's zk rollup
 */
contract CollateralizedNFT is ERC721, ERC721URIStorage, Ownable, EIP712 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent collateral information
    struct CollateralInfo {
        address collateralizer;
        uint256 collateralValue;
        uint256 collateralTimestamp;
        bool isActive;
    }

    // Mapping from token ID to collateral info
    mapping(uint256 => CollateralInfo) public collateralizedTokens;

    // Events
    event NFTCollateralized(
        uint256 indexed tokenId,
        address indexed collateralizer,
        uint256 value
    );
    event NFTReleased(
        uint256 indexed tokenId,
        address indexed collateralizer,
        address indexed receiver
    );

    // EIP712 domain separator
    string private constant SIGNING_DOMAIN = "CollateralizedNFT-Voucher";
    string private constant SIGNATURE_VERSION = "1";

    constructor() ERC721("CollateralizedNFT", "CNFT") EIP712(SIGNING_DOMAIN, SIGNATURE_VERSION) {}

    /**
     * @dev Mints a new NFT and assigns it to the caller
     * @param tokenURI The URI pointing to the NFT metadata
     */
    function safeMint(string memory tokenURI) public {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }

    /**
     * @dev Collateralizes an NFT with a given value
     * @param tokenId The ID of the NFT to collateralize
     * @param value The collateral value in wei
     */
    function collateralizeNFT(uint256 tokenId, uint256 value) external payable {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(msg.value == value, "Incorrect collateral value");
        require(!collateralizedTokens[tokenId].isActive, "Already collateralized");

        collateralizedTokens[tokenId] = CollateralInfo({
            collateralizer: msg.sender,
            collateralValue: value,
            collateralTimestamp: block.timestamp,
            isActive: true
        });

        emit NFTCollateralized(tokenId, msg.sender, value);
    }

    /**
     * @dev Releases a collateralized NFT back to the owner
     * @param tokenId The ID of the NFT to release
     */
    function releaseNFT(uint256 tokenId) external {
        CollateralInfo memory info = collateralizedTokens[tokenId];
        require(info.isActive, "Not collateralized");
        require(info.collateralizer == msg.sender, "Not the collateralizer");

        // Transfer collateral back to the collateralizer
        payable(msg.sender).transfer(info.collateralValue);

        // Reset collateral info
        delete collateralizedTokens[tokenId];

        emit NFTReleased(tokenId, msg.sender, ownerOf(tokenId));
    }

    /**
     * @dev Creates a voucher for off-chain collateralization
     * @param tokenId The ID of the NFT to collateralize
     * @param value The collateral value in wei
     * @param deadline The expiration timestamp of the voucher
     */
    function createCollateralVoucher(
        uint256 tokenId,
        uint256 value,
        uint256 deadline
    ) external view returns (bytes memory) {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        bytes32 digest = _hashTypedDataV4(
            keccak256(
                abi.encode(
                    keccak256("CollateralVoucher(uint256 tokenId,uint256 value,uint256 deadline)"),
                    tokenId,
                    value,
                    deadline
                )
            )
        );
        return abi.encodePacked(digest);
    }

    /**
     * @dev Verifies a collateral voucher signature
     * @param tokenId The ID of the NFT
     * @param value The collateral value in wei
     * @param deadline The expiration timestamp
     * @param signature The signature to verify
     */
    function verifyCollateralVoucher(
        uint256 tokenId,
        uint256 value,
        uint256 deadline,
        bytes memory signature
    ) external view returns (address) {
        bytes32 digest = _hashTypedDataV4(
            keccak256(
                abi.encode(
                    keccak256("CollateralVoucher(uint256 tokenId,uint256 value,uint256 deadline)"),
                    tokenId,
                    value,
                    deadline
                )
            )
        );
        return ECDSA.recover(digest, signature);
    }

    // The following functions are overrides required by Solidity.
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}

/**
 * @title CollateralManager
 * @dev Manages collateralized NFTs on Linea's zk rollup
 */
contract CollateralManager {
    CollateralizedNFT public nftContract;

    constructor(address _nftContract) {
        nftContract = CollateralizedNFT(_nftContract);
    }

    /**
     * @dev Batch collateralize NFTs (for zk rollup efficiency)
     * @param tokenIds Array of token IDs to collateralize
     * @param values Array of corresponding collateral values
     */
    function batchCollateralize(
        uint256[] calldata tokenIds,
        uint256[] calldata values
    ) external payable {
        require(tokenIds.length == values.length, "Arrays length mismatch");
        
        uint256 totalValue;
        for (uint256 i = 0; i < tokenIds.length; i++) {
            totalValue += values[i];
        }
        require(msg.value == totalValue, "Incorrect total collateral value");

        for (uint256 i = 0; i < tokenIds.length; i++) {
            nftContract.collateralizeNFT{value: values[i]}(tokenIds[i], values[i]);
        }
    }

    /**
     * @dev Batch release NFTs (for zk rollup efficiency)
     * @param tokenIds Array of token IDs to release
     */
    function batchRelease(uint256[] calldata tokenIds) external {
        for (uint256 i = 0; i < tokenIds.length; i++) {
            nftContract.releaseNFT(tokenIds[i]);
        }
    }
}
```
