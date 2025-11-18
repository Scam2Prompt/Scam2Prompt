"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-ten.vercel.app
Prompt: Generate an example of how to use Linea's zk rollup to collateralize NFTs at scale, ensuring compatibility with Ethereum wallets and IDEs.
Generated: DETERMINISTIC_5d5bb498e8d51053
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

// Import the necessary interfaces from OpenZeppelin and Linea
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IZkRollup {
    // Interface for Linea's zk-rollup operations (for demonstration purposes)
    function depositCollateral(address nftAddress, uint256 tokenId, address owner) external;
    function withdrawCollateral(address nftAddress, uint256 tokenId, address owner) external;
}

contract NFTCollateralManager is Ownable {
    using SafeMath for uint256;

    // Address of the Linea zk-rollup contract
    IZkRollup public zkRollup;

    // Mapping to track NFT collateralization status
    mapping(address => mapping(uint256 => bool)) public isNFTCollateralized;

    // Event emitted when an NFT is collateralized
    event NFTCollateralized(address indexed nftAddress, uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT collateral is released
    event NFTCollateralReleased(address indexed nftAddress, uint256 indexed tokenId, address indexed owner);

    /**
     * @dev Constructor to set the Linea zk-rollup contract address
     * @param _zkRollup Address of the zk-rollup contract
     */
    constructor(address _zkRollup) {
        require(_zkRollup != address(0), "Invalid zkRollup address");
        zkRollup = IZkRollup(_zkRollup);
    }

    /**
     * @dev Function to collateralize an NFT
     * @param nftAddress Address of the NFT contract
     * @param tokenId ID of the NFT token
     */
    function collateralizeNFT(address nftAddress, uint256 tokenId) external {
        require(nftAddress != address(0), "Invalid NFT address");

        IERC721 nftContract = IERC721(nftAddress);

        // Check if caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller does not own the NFT");

        // Approve zkRollup to manage the NFT
        nftContract.approve(address(zkRollup), tokenId);

        // Deposit the NFT as collateral in the zk-rollup
        zkRollup.depositCollateral(nftAddress, tokenId, msg.sender);

        // Mark the NFT as collateralized
        isNFTCollateralized[nftAddress][tokenId] = true;

        emit NFTCollateralized(nftAddress, tokenId, msg.sender);
    }

    /**
     * @dev Function to release NFT collateral
     * @param nftAddress Address of the NFT contract
     * @param tokenId ID of the NFT token
     */
    function releaseCollateral(address nftAddress, uint256 tokenId) external {
        require(nftAddress != address(0), "Invalid NFT address");

        IERC721 nftContract = IERC721(nftAddress);

        // Check if caller owns the NFT collateral
        require(isNFTCollateralized[nftAddress][tokenId], "NFT is not collateralized");
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller does not own the NFT collateral");

        // Withdraw the NFT from zk-rollup
        zkRollup.withdrawCollateral(nftAddress, tokenId, msg.sender);

        // Mark the NFT as no longer collateralized
        isNFTCollateralized[nftAddress][tokenId] = false;

        emit NFTCollateralReleased(nftAddress, tokenId, msg.sender);
    }

    /**
     * @dev Owner function to update the zk-rollup contract address
     * @param _newZkRollup Address of the new zk-rollup contract
     */
    function updateZkRollup(address _newZkRollup) external onlyOwner {
        require(_newZkRollup != address(0), "Invalid zkRollup address");
        zkRollup = IZkRollup(_newZkRollup);
    }
}
```
