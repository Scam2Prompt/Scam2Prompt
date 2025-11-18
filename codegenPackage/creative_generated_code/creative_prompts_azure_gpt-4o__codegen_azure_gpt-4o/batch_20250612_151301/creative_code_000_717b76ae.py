"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Write a smart contract in Solidity that utilizes Somnia's 300k+tps EVM Layer 1 blockchain for transferring NFTs across multiple metaverses using its interoperability protocols.
Generated: DETERMINISTIC_717b76ae385963c9
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title NFTInteroperability
 * @dev A smart contract for transferring NFTs across multiple metaverses 
 * using Somnia's interoperability protocols.
 */
contract NFTInteroperability {
    // Event emitted when an NFT is successfully transferred between metaverses
    event NFTTransferred(
        address indexed sender,
        address indexed receiver,
        address indexed nftContract,
        uint256 tokenId,
        uint256 destinationChainId,
        bytes metadata
    );

    // Somnia's Interoperability Protocol Contract Address
    address private immutable somniaProtocolContract;

    // Error definitions
    error InvalidNFTContractAddress();
    error TransferFailed();
    error InvalidReceiverAddress();
    error Unauthorized();

    // Modifiers
    modifier onlyValidAddress(address addr) {
        if (addr == address(0)) revert InvalidReceiverAddress();
        _;
    }

    /**
     * @dev Constructor to set the Somnia protocol contract address.
     * @param _somniaProtocolContract The address of Somnia's interoperability protocol.
     */
    constructor(address _somniaProtocolContract) {
        if (_somniaProtocolContract == address(0)) revert InvalidNFTContractAddress();
        somniaProtocolContract = _somniaProtocolContract;
    }

    /**
     * @dev Transfers an NFT across metaverses using Somnia's interoperability protocols.
     * @param nftContract Address of the ERC721 NFT contract.
     * @param tokenId ID of the token to transfer.
     * @param receiver Address on the destination metaverse to receive the NFT.
     * @param destinationChainId ID of the destination blockchain/metaverse.
     * @param metadata Optional metadata to include with the transfer.
     *
     * Requirements:
     * - Caller must be the owner of the NFT or approved spender.
     */
    function transferNFT(
        address nftContract,
        uint256 tokenId,
        address receiver,
        uint256 destinationChainId,
        bytes memory metadata
    ) external onlyValidAddress(receiver) {
        // Ensure the NFT contract address is valid
        if (nftContract == address(0)) revert InvalidNFTContractAddress();

        // Ensure caller is the owner of the NFT or approved spender
        bool isApprovedOrOwner = ERC721(nftContract).isApprovedForAll(msg.sender, address(this)) ||
            ERC721(nftContract).getApproved(tokenId) == msg.sender ||
            ERC721(nftContract).ownerOf(tokenId) == msg.sender;
        if (!isApprovedOrOwner) revert Unauthorized();

        // Call Somnia's interoperability protocol for cross-chain transfer
        (bool success, ) = somniaProtocolContract.call(
            abi.encodeWithSignature(
                "transferNFT(address,uint256,address,uint256,bytes)",
                nftContract,
                tokenId,
                receiver,
                destinationChainId,
                metadata
            )
        );

        // Ensure the transfer was successful
        if (!success) revert TransferFailed();

        // Emit an event for the successful transfer
        emit NFTTransferred(
            msg.sender,
            receiver,
            nftContract,
            tokenId,
            destinationChainId,
            metadata
        );
    }

    /**
     * @dev Returns the address of Somnia's interoperability protocol contract.
     * @return The address of the protocol.
     */
    function getSomniaProtocolContract() external view returns (address) {
        return somniaProtocolContract;
    }
}

/**
 * @dev Interface for ERC721 standard to interact with NFT contracts.
 */
interface ERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);

    function getApproved(uint256 tokenId) external view returns (address);

    function isApprovedForAll(address owner, address operator) external view returns (bool);
}
```
