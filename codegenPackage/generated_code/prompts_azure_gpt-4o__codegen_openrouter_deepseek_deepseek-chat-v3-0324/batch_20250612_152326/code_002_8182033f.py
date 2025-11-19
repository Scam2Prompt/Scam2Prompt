"""
Generated Code Metadata:
========================
Original URL: https://flow-blockchain.com
Prompt: Generate code for interacting with Flow Blockchain to mint NFTs using Cadence, the smart contract programming language for Flow.
Generated: DETERMINISTIC_8182033f7598dde3
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cadence
// NFT Contract Interface
pub contract interface NonFungibleToken {
    pub var totalSupply: UInt64

    pub event ContractInitialized()
    pub event Withdraw(id: UInt64, from: Address?)
    pub event Deposit(id: UInt64, to: Address?)

    pub resource interface INFT {
        pub let id: UInt64
    }

    pub resource NFT: INFT {
        pub let id: UInt64
    }

    pub fun createEmptyCollection(): @Collection
    pub resource Collection {
        pub fun deposit(token: @NFT)
        pub fun getIDs(): [UInt64]
        pub fun borrowNFT(id: UInt64): &NFT
        pub fun withdraw(withdrawID: UInt64): @NFT
    }
}

// NFT Contract Implementation
pub contract ExampleNFT: NonFungibleToken {
    pub var totalSupply: UInt64
    pub var nextID: UInt64

    pub resource NFT: NonFungibleToken.NFT {
        pub let id: UInt64
        pub let metadata: {String: String}

        init(metadata: {String: String}) {
            self.id = ExampleNFT.nextID
            self.metadata = metadata
            
            ExampleNFT.nextID = ExampleNFT.nextID + 1
            ExampleNFT.totalSupply = ExampleNFT.totalSupply + 1
        }
    }

    pub resource Collection: NonFungibleToken.Collection {
        pub var ownedNFTs: @{UInt64: NFT}

        init() {
            self.ownedNFTs <- {}
        }

        destroy() {
            destroy self.ownedNFTs
        }

        pub fun deposit(token: @NonFungibleToken.NFT) {
            let token <- token as! @NFT
            self.ownedNFTs[token.id] <-! token
            emit Deposit(id: token.id, to: self.owner?.address)
        }

        pub fun getIDs(): [UInt64] {
            return self.ownedNFTs.keys
        }

        pub fun borrowNFT(id: UInt64): &NonFungibleToken.NFT {
            return &self.ownedNFTs[id] as &NonFungibleToken.NFT
        }

        pub fun withdraw(withdrawID: UInt64): @NonFungibleToken.NFT {
            let token <- self.ownedNFTs.remove(key: withdrawID) 
                ?? panic("NFT not found in collection")
            emit Withdraw(id: token.id, from: self.owner?.address)
            return <-token
        }
    }

    pub fun createEmptyCollection(): @NonFungibleToken.Collection {
        return <- create Collection()
    }

    pub fun mintNFT(metadata: {String: String}): @NFT {
        return <- create NFT(metadata: metadata)
    }

    init() {
        self.totalSupply = 0
        self.nextID = 1
        emit ContractInitialized()
    }
}

// NFT Minting Transaction
transaction(recipient: Address, metadata: {String: String}) {
    prepare(signer: AuthAccount) {
        // Get the recipient's collection
        let recipientCollection = getAccount(recipient)
            .getCapability(/public/ExampleNFTCollection)
            .borrow<&ExampleNFT.Collection{NonFungibleToken.CollectionPublic}>()
            ?? panic("Recipient does not have an NFT Collection")

        // Mint the NFT
        let nft <- ExampleNFT.mintNFT(metadata: metadata)

        // Deposit it in the recipient's collection
        recipientCollection.deposit(token: <-nft)
    }
}

// Setup Collection Transaction
transaction {
    prepare(signer: AuthAccount) {
        // Create a new empty collection
        let collection <- ExampleNFT.createEmptyCollection()

        // Store it in the account
        signer.save(<-collection, to: /storage/ExampleNFTCollection)

        // Create a public capability for the collection
        signer.link<&ExampleNFT.Collection{NonFungibleToken.CollectionPublic}>(
            /public/ExampleNFTCollection,
            target: /storage/ExampleNFTCollection
        )
    }
}
```
