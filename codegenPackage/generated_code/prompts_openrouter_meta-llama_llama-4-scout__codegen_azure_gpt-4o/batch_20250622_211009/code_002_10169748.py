"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Generate a smart contract code in Solidity that enables users to create, buy, and sell meme-based tokens on a blockchain platform, similar to METAL's tokenomics.
Generated: DETERMINISTIC_10169748cca43ac8
Batch ID: 20250622_211009
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
 * @title MemeTokenMarketplace
 * @dev A smart contract for creating, buying, and selling meme-based tokens.
 */
contract MemeTokenMarketplace {
    // Token structure
    struct MemeToken {
        uint256 id;
        string name;
        string metadataURI; // URI pointing to the meme's metadata
        address creator;
        uint256 price; // Price in wei
        bool forSale;
    }

    // State variables
    uint256 private nextTokenId; // Counter for token IDs
    mapping(uint256 => MemeToken) private tokens; // Mapping of token ID to MemeToken
    mapping(uint256 => address) private tokenOwners; // Mapping of token ID to owner
    mapping(address => uint256[]) private ownedTokens; // Mapping of owner to their token IDs

    // Events
    event TokenCreated(uint256 indexed tokenId, string name, address indexed creator, uint256 price);
    event TokenListedForSale(uint256 indexed tokenId, uint256 price);
    event TokenSold(uint256 indexed tokenId, address indexed buyer, uint256 price);
    event TokenDelisted(uint256 indexed tokenId);

    // Modifier to check token ownership
    modifier onlyTokenOwner(uint256 tokenId) {
        require(tokenOwners[tokenId] == msg.sender, "Caller is not the token owner");
        _;
    }

    // Modifier to check token existence
    modifier tokenExists(uint256 tokenId) {
        require(tokens[tokenId].creator != address(0), "Token does not exist");
        _;
    }

    /**
     * @dev Create a new meme token.
     * @param name Name of the meme token.
     * @param metadataURI URI pointing to the meme's metadata.
     * @param price Initial price of the token in wei.
     */
    function createToken(string memory name, string memory metadataURI, uint256 price) external {
        require(bytes(name).length > 0, "Token name cannot be empty");
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = nextTokenId++;
        tokens[tokenId] = MemeToken(tokenId, name, metadataURI, msg.sender, price, false);
        tokenOwners[tokenId] = msg.sender;
        ownedTokens[msg.sender].push(tokenId);

        emit TokenCreated(tokenId, name, msg.sender, price);
    }

    /**
     * @dev List a token for sale.
     * @param tokenId ID of the token to list for sale.
     * @param price Sale price in wei.
     */
    function listTokenForSale(uint256 tokenId, uint256 price) external onlyTokenOwner(tokenId) tokenExists(tokenId) {
        require(price > 0, "Price must be greater than zero");

        MemeToken storage token = tokens[tokenId];
        token.forSale = true;
        token.price = price;

        emit TokenListedForSale(tokenId, price);
    }

    /**
     * @dev Buy a token listed for sale.
     * @param tokenId ID of the token to buy.
     */
    function buyToken(uint256 tokenId) external payable tokenExists(tokenId) {
        MemeToken storage token = tokens[tokenId];
        require(token.forSale, "Token is not for sale");
        require(msg.value == token.price, "Incorrect payment amount");

        address seller = tokenOwners[tokenId];
        tokenOwners[tokenId] = msg.sender;
        token.forSale = false;

        // Update ownership mappings
        _removeTokenFromOwner(seller, tokenId);
        ownedTokens[msg.sender].push(tokenId);

        // Transfer payment to the seller
        payable(seller).transfer(msg.value);

        emit TokenSold(tokenId, msg.sender, token.price);
    }

    /**
     * @dev Delist a token from sale.
     * @param tokenId ID of the token to delist.
     */
    function delistToken(uint256 tokenId) external onlyTokenOwner(tokenId) tokenExists(tokenId) {
        MemeToken storage token = tokens[tokenId];
        require(token.forSale, "Token is not listed for sale");

        token.forSale = false;

        emit TokenDelisted(tokenId);
    }

    /**
     * @dev Get details of a token.
     * @param tokenId ID of the token to fetch details for.
     * @return MemeToken struct containing token details.
     */
    function getTokenDetails(uint256 tokenId) external view tokenExists(tokenId) returns (MemeToken memory) {
        return tokens[tokenId];
    }

    /**
     * @dev Get all tokens owned by a specific address.
     * @param owner Address to fetch tokens for.
     * @return Array of token IDs owned by the address.
     */
    function getTokensByOwner(address owner) external view returns (uint256[] memory) {
        return ownedTokens[owner];
    }

    /**
     * @dev Internal function to remove a token from an owner's list of tokens.
     * @param owner Address of the token owner.
     * @param tokenId ID of the token to remove.
     */
    function _removeTokenFromOwner(address owner, uint256 tokenId) internal {
        uint256[] storage tokensArray = ownedTokens[owner];
        for (uint256 i = 0; i < tokensArray.length; i++) {
            if (tokensArray[i] == tokenId) {
                tokensArray[i] = tokensArray[tokensArray.length - 1];
                tokensArray.pop();
                break;
            }
        }
    }
}
```
