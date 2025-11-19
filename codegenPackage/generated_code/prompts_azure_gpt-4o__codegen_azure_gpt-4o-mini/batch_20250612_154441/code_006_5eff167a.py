"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Create a Solidity contract to manage NFT airdrops for specific categories of holders, inspired by the "AIRDROP PLEDGE COMPLETED" system on Clone Force™.
Generated: DETERMINISTIC_5eff167a2b058e58
Batch ID: 20250612_154441
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title NFTAirdropManager
 * @dev A contract to manage NFT airdrops for specific categories of holders.
 */
contract NFTAirdropManager is Ownable {
    using Address for address;

    // Event emitted when an airdrop is created
    event AirdropCreated(uint256 indexed airdropId, address indexed nftContract, uint256[] tokenIds, address[] recipients);
    
    // Event emitted when an airdrop is executed
    event AirdropExecuted(uint256 indexed airdropId);

    // Struct to hold airdrop details
    struct Airdrop {
        address nftContract; // The NFT contract address
        uint256[] tokenIds;  // The token IDs to be airdropped
        address[] recipients; // The recipients of the airdrop
        bool executed;       // Status of the airdrop execution
    }

    // Mapping to store airdrops
    mapping(uint256 => Airdrop) public airdrops;
    uint256 public airdropCount; // Counter for airdrop IDs

    /**
     * @dev Create a new airdrop.
     * @param _nftContract The address of the NFT contract.
     * @param _tokenIds The array of token IDs to be airdropped.
     * @param _recipients The array of recipient addresses.
     */
    function createAirdrop(address _nftContract, uint256[] memory _tokenIds, address[] memory _recipients) external onlyOwner {
        require(_nftContract.isContract(), "Invalid NFT contract address");
        require(_tokenIds.length == _recipients.length, "Token IDs and recipients length mismatch");

        airdropCount++;
        airdrops[airdropCount] = Airdrop({
            nftContract: _nftContract,
            tokenIds: _tokenIds,
            recipients: _recipients,
            executed: false
        });

        emit AirdropCreated(airdropCount, _nftContract, _tokenIds, _recipients);
    }

    /**
     * @dev Execute an airdrop.
     * @param _airdropId The ID of the airdrop to execute.
     */
    function executeAirdrop(uint256 _airdropId) external onlyOwner {
        Airdrop storage airdrop = airdrops[_airdropId];
        require(!airdrop.executed, "Airdrop already executed");

        IERC721 nft = IERC721(airdrop.nftContract);
        for (uint256 i = 0; i < airdrop.tokenIds.length; i++) {
            nft.transferFrom(address(this), airdrop.recipients[i], airdrop.tokenIds[i]);
        }

        airdrop.executed = true;
        emit AirdropExecuted(_airdropId);
    }

    /**
     * @dev Withdraw NFTs from the contract.
     * @param _nftContract The address of the NFT contract.
     * @param _tokenIds The array of token IDs to withdraw.
     */
    function withdrawNFTs(address _nftContract, uint256[] memory _tokenIds) external onlyOwner {
        IERC721 nft = IERC721(_nftContract);
        for (uint256 i = 0; i < _tokenIds.length; i++) {
            nft.transferFrom(address(this), msg.sender, _tokenIds[i]);
        }
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
