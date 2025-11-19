"""
Generated Code Metadata:
========================
Original URL: https://flow-blockchain.com
Prompt: Generate a smart contract code snippet for a simple NFT creation on Flow Blockchain.
Generated: DETERMINISTIC_1186d3343d28f495
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cadence
// NFTContract.cdc
import NonFungibleToken from 0xNonFungibleToken
import MetadataViews from 0xMetadataViews

// A simple NFT contract that allows the creation of unique NFTs
pub contract NFTContract: NonFungibleToken.Provider, NonFungibleToken.Receiver {

    // The structure of the NFT
    pub struct NFT: NonFungibleToken.INFT {
        pub let id: UInt64
        pub let name: String
        pub let description: String
        pub let metadata: {String: String}

        // Initialize a new NFT
        pub fun createNFT(id: UInt64, name: String, description: String, metadata: {String: String}) {
            self.id = id
            self.name = name
            self.description = description
            self.metadata = metadata
        }
    }

    // The collection of NFTs
    pub resource NFTCollection: NonFungibleToken.CollectionPublic {
        pub var ownedNFTs: @{UInt64: NFT}

        // Initialize the NFT collection
        init() {
            self.ownedNFTs <- {}
        }

        // Function to mint a new NFT
        pub fun mintNFT(name: String, description: String, metadata: {String: String}): @NFT {
            let newID = self.getNextID()
            let newNFT <- create NFT(id: newID, name: name, description: description, metadata: metadata)
            self.ownedNFTs[newID] <-! newNFT
            return <- newNFT
        }

        // Function to get the next available ID for the NFT
        pub fun getNextID(): UInt64 {
            return UInt64(self.ownedNFTs.length + 1)
        }

        // Function to withdraw an NFT from the collection
        pub fun withdrawNFT(id: UInt64): @NFT {
            let nft <- self.ownedNFTs.remove(key: id) ?? panic("NFT not found")
            return <- nft
        }
    }

    // The public interface for the NFT collection
    pub resource interface NFTCollectionPublic {
        pub fun mintNFT(name: String, description: String, metadata: {String: String}): @NFT
        pub fun withdrawNFT(id: UInt64): @NFT
    }

    // The initializer for the contract
    init() {
        // Create a new NFT collection for the contract
        self.account.save(<- create NFTCollection(), to: /storage/NFTCollection)
        self.account.link<&NFTCollection{NonFungibleToken.CollectionPublic}>(
            /public/NFTCollection,
            target: /storage/NFTCollection
        )
    }
}
```
