"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Develop a Solidity contract that allows for airdrops of Ember NFTs to holders based on specific criteria.
Generated: DETERMINISTIC_71484d6c6f60e73a
Batch ID: 20250612_135829
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

/**
 * @title EmberNFTAirdrop
 * @dev A contract to manage airdrops of Ember NFTs to eligible holders based on specific criteria.
 */
contract EmberNFTAirdrop {
    // Address of the Ember NFT contract
    address public emberNFTContract;

    // Owner of the contract
    address public owner;

    // Event emitted when an airdrop is successfully executed
    event AirdropExecuted(address indexed recipient, uint256 tokenId);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Ember NFT contract address.
     * @param _emberNFTContract Address of the Ember NFT contract.
     */
    constructor(address _emberNFTContract) {
        require(_emberNFTContract != address(0), "Invalid NFT contract address");
        emberNFTContract = _emberNFTContract;
        owner = msg.sender;
    }

    /**
     * @dev Function to execute an airdrop of Ember NFTs to eligible holders.
     * @param recipients Array of recipient addresses.
     * @param tokenIds Array of token IDs to be airdropped.
     */
    function executeAirdrop(address[] calldata recipients, uint256[] calldata tokenIds) external onlyOwner {
        require(recipients.length == tokenIds.length, "Recipients and tokenIds length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 tokenId = tokenIds[i];

            // Ensure recipient address is valid
            require(recipient != address(0), "Invalid recipient address");

            // Call the Ember NFT contract to transfer the token
            (bool success, ) = emberNFTContract.call(
                abi.encodeWithSignature("safeTransferFrom(address,address,uint256)", owner, recipient, tokenId)
            );

            // Check if the transfer was successful
            require(success, "NFT transfer failed");

            // Emit an event for the successful airdrop
            emit AirdropExecuted(recipient, tokenId);
        }
    }

    /**
     * @dev Function to update the Ember NFT contract address.
     * @param _newEmberNFTContract Address of the new Ember NFT contract.
     */
    function updateEmberNFTContract(address _newEmberNFTContract) external onlyOwner {
        require(_newEmberNFTContract != address(0), "Invalid NFT contract address");
        emberNFTContract = _newEmberNFTContract;
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
