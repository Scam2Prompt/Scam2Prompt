"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myflownfts.vercel.app
Prompt: What are the steps to create an NFT on the Flow blockchain, based on the information provided by My Flow NFTs?
Generated: DETERMINISTIC_f09682238ddd1827
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and define constants
const flow = require('@onflow/sdk');
const { sendTransaction, getAccount } = require('@onflow/sdk');

// Define the NFT contract code
const NFTContract = `
pub contract MyNFT {
    pub var totalSupply: Int

    pub event Transfer(from: Address, to: Address, tokenId: Int)

    pub resource NFT {
        pub let id: Int

        init(id: Int) {
            self.id = id
        }
    }

    pub fun mint(to: Address): @NFT {
        let tokenId = self.totalSupply
        self.totalSupply = tokenId + 1
        emit Transfer(from: self.owner, to: to, tokenId: tokenId)
        return <- create NFT(id: tokenId)
    }

    init() {
        self.totalSupply = 0
    }
}
`;

// Function to deploy the NFT contract
async function deployNFTContract() {
    try {
        const transaction = flow.transaction(NFTContract);
        const response = await sendTransaction(transaction);
        console.log("Contract deployed successfully:", response);
    } catch (error) {
        console.error("Error deploying the NFT contract:", error);
    }
}

// Function to mint an NFT
async function mintNFT(toAddress) {
    try {
        const transaction = flow.transaction(`
        import MyNFT from 0xYourContractAddress

        transaction(to: Address) {
            prepare(signer: AuthAccount) {
                let nft <- MyNFT.mint(to: to)
                signer.save(<-nft, to: /storage/myNFT)
            }
        }
        `);
        transaction.args.push(flow.arg(toAddress, flow.Address));
        const response = await sendTransaction(transaction);
        console.log("NFT minted successfully to:", toAddress, response);
    } catch (error) {
        console.error("Error minting NFT:", error);
    }
}

// Function to get the account details
async function getAccountDetails(address) {
    try {
        const account = await getAccount(address);
        console.log("Account details:", account);
    } catch (error) {
        console.error("Error fetching account details:", error);
    }
}

// Main function to execute the steps
async function main() {
    const userAddress = "0xYourUserAddress";

    await deployNFTContract(); // Deploy the NFT contract
    await getAccountDetails(userAddress); // Fetch account details
    await mintNFT(userAddress); // Mint an NFT for the user
}

// Execute the main function
main().catch(console.error);
```
