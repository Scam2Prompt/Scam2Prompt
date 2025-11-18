"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-quest-fnjdubph5-lfglabs.vercel.app
Prompt: Write a tutorial for deploying a Starknet smart contract that supports the minting of NFTs tied to quest completion, referencing the features described in Starknet Quest.
Generated: DETERMINISTIC_b3db460cfa234fc1
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# starknet_nft_minting_contract.cairo

# Import necessary libraries
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.uint256 import uint256_add, uint256_sub

# Define the StarkNet contract
@contract_interface
namespace ERC721 {
    func mint(recipient: felt, tokenId: felt) -> ();
    func ownerOf(tokenId: felt) -> felt;
    func transferFrom(sender: felt, recipient: felt, tokenId: felt) -> ();
}

# Main contract class
@contract
namespace StarknetQuestNFT {
    # Builtins required for hashing (used to verify quest completion)
    struct HashBuiltin {
        hash: felt;
    }

    # Storage variables
    @storage_var
    func questCompleted(questId: felt, user: felt) -> felt;

    @storage_var
    func questNFTCount() -> felt;

    @storage_var
    func nftOwner(tokenId: felt) -> felt;

    # Events
    @event
    func QuestCompleted(user: felt, questId: felt, tokenId: felt);

    @event
    func NFTMinted(user: felt, tokenId: felt);

    # Constructor function
    @constructor
    func constructor() {
        # Initialize storage variables if necessary
        questNFTCount.write(0);
    }

    # Function to verify and mark quest completion
    @external
    func completeQuest(user: felt, questId: felt, proof: felt) -> felt {
        # Proof verification logic (simplified for tutorial purposes)
        # In production, replace with actual proof verification using HashBuiltin
        if proof != hash_builtin.hash {
            return 0;  # Proof invalid
        }

        # Mark quest as completed
        questCompleted.write(questId, user, 1);

        # Mint NFT upon quest completion
        let tokenId = questNFTCount.read() + 1;
        questNFTCount.write(tokenId);  # Update NFT count
        self.mintNFT(user=user, tokenId=tokenId);

        # Emit quest completion and NFT minting events
        emit QuestCompleted(user=user, questId=questId, tokenId=tokenId);
        emit NFTMinted(user=user, tokenId=tokenId);

        return tokenId;
    }

    # Internal function to mint the NFT
    @internal
    func mintNFT(user: felt, tokenId: felt) {
        # ERC721 mint function call (external contract reference)
        ERC721.mint(recipient=user, tokenId=tokenId);

        # Update NFT ownership storage
        nftOwner.write(tokenId, user);
    }

    # Function to check if a user has completed a quest
    @view
    func isQuestCompleted(user: felt, questId: felt) -> felt {
        return questCompleted.read(questId, user);
    }

    # Function to retrieve the owner of an NFT
    @view
    func getNFTOwner(tokenId: felt) -> felt {
        return nftOwner.read(tokenId);
    }
}
```
