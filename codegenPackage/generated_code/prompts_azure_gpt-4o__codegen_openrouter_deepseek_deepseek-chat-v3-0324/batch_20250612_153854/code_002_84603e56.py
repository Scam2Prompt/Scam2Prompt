"""
Generated Code Metadata:
========================
Original URL: https://myflownfts.vercel.app
Prompt: Create a function using Flow's Cadence language to query and filter NFTs based on their collection, such as "UFC Strike" or "LaLiga Golazos."
Generated: DETERMINISTIC_84603e564217f917
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cadence
// QueryNFTsByCollection.cdc
// This script queries and filters NFTs based on their collection name.

pub fun main(account: Address, collectionName: String): [UInt64] {
    // Get the public account object
    let acct = getAccount(account)
    
    // Get the NFT collection capability from the account
    let collectionCap = acct.getCapability<&{NonFungibleToken.CollectionPublic}>(
        /public/NFTCollection
    )
    
    // Borrow the collection reference
    let collectionRef = collectionCap.borrow()
        ?? panic("Could not borrow reference to NFT Collection")
    
    // Initialize an array to store matching NFT IDs
    let matchingNFTs: [UInt64] = []
    
    // Get all NFT IDs in the collection
    let ids = collectionRef.getIDs()
    
    // Iterate through each NFT ID
    for id in ids {
        // Borrow the NFT reference
        let nftRef = collectionRef.borrowNFT(id: id)
            ?? panic("Could not borrow NFT reference")
        
        // Get the NFT's metadata
        let metadata = nftRef.getMetadata()
        
        // Check if the NFT belongs to the specified collection
        if let collection = metadata["collection"] as? String {
            if collection == collectionName {
                // Add the NFT ID to the matching list
                matchingNFTs.append(id)
            }
        }
    }
    
    return matchingNFTs
}
```
