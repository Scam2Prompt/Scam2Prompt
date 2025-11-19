"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.pages.dev
Prompt: Describe how to create an ERC-404 token standard that integrates with existing ERC-721 and ERC-20 protocols for a project like God Candle.
Generated: DETERMINISTIC_3af2409fde9a1f34
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ERC404Token
 * @dev ERC-404 token standard that integrates with ERC-721 (NFTs) and ERC-20 (fungible tokens).
 *      ERC-404 combines the functionalities of both standards for specialized use cases.
 */
contract ERC404Token {
    // ERC-20 state variables
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // ERC-721 state variables
    uint256 private tokenIdCounter;
    mapping(uint256 => address) private tokenOwners;
    mapping(uint256 => string) private tokenURIs;
    mapping(address => uint256[]) private ownedTokens;

    // Events for ERC-20
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Events for ERC-721
    event Mint(address indexed owner, uint256 tokenId, string tokenURI);
    event TransferNFT(address indexed from, address indexed to, uint256 tokenId);

    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        // Initialize ERC-20 properties
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;

        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    // ERC-20 Functions

    /**
     * @dev Returns the balance of an account.
     * @param account The account to query.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to another account.
     * @param to The recipient address.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another on behalf of the owner.
     * @param from The address to transfer from.
     * @param to The recipient address.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner The owner of the tokens.
     * @param spender The spender address.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // ERC-721 Functions

    /**
     * @dev Mints a new NFT.
     * @param to The recipient address.
     * @param uri The metadata URI.
     */
    function mintNFT(address to, string memory uri) public {
        require(to != address(0), "Mint to the zero address");

        uint256 newTokenId = ++tokenIdCounter;
        tokenOwners[newTokenId] = to;
        tokenURIs[newTokenId] = uri;
        ownedTokens[to].push(newTokenId);

        emit Mint(to, newTokenId, uri);
    }

    /**
     * @dev Transfers an NFT to another account.
     * @param from The address to transfer from.
     * @param to The recipient address.
     * @param tokenId The ID of the NFT to transfer.
     */
    function transferNFT(address from, address to, uint256 tokenId) public {
        require(to != address(0), "Transfer to the zero address");
        require(tokenOwners[tokenId] == from, "Not the owner of this token");

        // Remove from current owner's list
        uint256[] storage fromTokens = ownedTokens[from];
        for (uint256 i = 0; i < fromTokens.length; i++) {
            if (fromTokens[i] == tokenId) {
                fromTokens[i] = fromTokens[fromTokens.length - 1];
                fromTokens.pop();
                break;
            }
        }

        // Add to new owner's list
        tokenOwners[tokenId] = to;
        ownedTokens[to].push(tokenId);

        emit TransferNFT(from, to, tokenId);
    }

    /**
     * @dev Returns the owner of an NFT.
     * @param tokenId The ID of the NFT.
     * @return The owner address.
     */
    function ownerOf(uint256 tokenId) public view returns (address) {
        return tokenOwners[tokenId];
    }

    /**
     * @dev Returns the metadata URI of an NFT.
     * @param tokenId The ID of the NFT.
     * @return The metadata URI.
     */
    function tokenURI(uint256 tokenId) public view returns (string memory) {
        return tokenURIs[tokenId];
    }

    /**
     * @dev Returns the list of NFTs owned by a specific address.
     * @param owner The owner address.
     * @return The list of token IDs.
     */
    function tokensOfOwner(address owner) public view returns (uint256[] memory) {
        return ownedTokens[owner];
    }
}
```
