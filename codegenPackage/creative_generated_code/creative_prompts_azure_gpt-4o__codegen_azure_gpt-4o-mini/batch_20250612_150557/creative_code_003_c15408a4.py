"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-solak.web.app
Prompt: Write a function to mint NFTs using the Open Creator Protocol, ensuring dynamic royalties and customizable trading restrictions, as described in the Magic Box feature on the webpage.
Generated: DETERMINISTIC_c15408a4db137a63
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");
const ERC721 = require("@openzeppelin/contracts/token/ERC721/ERC721.sol");

// NFTMinting contract for minting NFTs using Open Creator Protocol
contract NFTMinting is ERC721 {
    // Mapping from token ID to royalty info
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Struct to hold royalty information
    struct RoyaltyInfo {
        address recipient;
        uint256 amount; // Royalty percentage in basis points
    }

    // Event to log minting of new NFT
    event NFTMinted(address indexed to, uint256 indexed tokenId, RoyaltyInfo royalty);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with dynamic royalties and customizable trading restrictions.
     * @param to The address of the recipient of the minted NFT.
     * @param tokenId The unique identifier for the NFT.
     * @param royaltyRecipient The address to which royalties will be sent.
     * @param royaltyPercentage The percentage of royalties in basis points (i.e., 100 basis points = 1%).
     */
    function mintNFT(
        address to,
        uint256 tokenId,
        address royaltyRecipient,
        uint256 royaltyPercentage
    ) external {
        // Validate inputs
        require(to != address(0), "Invalid recipient address");
        require(royaltyRecipient != address(0), "Invalid royalty recipient address");
        require(royaltyPercentage <= 10000, "Royalty percentage exceeds limit"); // 10000 basis points = 100%

        // Mint the NFT
        _safeMint(to, tokenId);

        // Set royalty information
        _royalties[tokenId] = RoyaltyInfo({
            recipient: royaltyRecipient,
            amount: royaltyPercentage
        });

        // Emit NFT minted event
        emit NFTMinted(to, tokenId, _royalties[tokenId]);
    }

    /**
     * @dev Retrieve royalty information for a specific token ID.
     * @param tokenId The unique identifier for the NFT.
     * @return recipient The address to receive royalties.
     * @return amount The royalty percentage in basis points.
     */
    function getRoyaltyInfo(uint256 tokenId) external view returns (address recipient, uint256 amount) {
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.amount);
    }

    /**
     * @dev Override the _transfer function to include trading restrictions if necessary.
     * This can be customized based on specific trading logic or conditions.
     */
    function _transfer(address from, address to, uint256 tokenId) internal override {
        // Implement custom trading restrictions here

        // Call the parent _transfer function
        super._transfer(from, to, tokenId);
    }
}
```
