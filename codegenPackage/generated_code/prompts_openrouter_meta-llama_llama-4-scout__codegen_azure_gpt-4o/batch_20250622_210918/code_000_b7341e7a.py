"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a Solidity smart contract code for an ERC404 token that automatically mints an NFT when the token balance exceeds 1 and burns it when the balance goes below 1.
Generated: DETERMINISTIC_b7341e7a57ae671b
Batch ID: 20250622_210918
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
 * @title ERC404 Token with Automatic NFT Minting and Burning
 * @dev This contract implements an ERC404-like token that mints an NFT when the token balance exceeds 1
 *      and burns the NFT when the balance goes below 1.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ERC404Token is ERC20, Ownable {
    // Reference to the NFT contract
    ERC721 public nftContract;

    // Mapping to track whether an address owns an NFT
    mapping(address => bool) private hasNFT;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner);

    // Event emitted when an NFT is burned
    event NFTBurned(address indexed owner);

    /**
     * @dev Constructor to initialize the ERC404 token and the associated NFT contract.
     * @param _name Name of the ERC404 token.
     * @param _symbol Symbol of the ERC404 token.
     * @param _nftContract Address of the deployed ERC721 NFT contract.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _nftContract
    ) ERC20(_name, _symbol) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = ERC721(_nftContract);
    }

    /**
     * @dev Override the _transfer function to check balances and mint/burn NFTs.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens being transferred.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        super._transfer(sender, recipient, amount);

        // Check sender's balance and burn NFT if necessary
        if (balanceOf(sender) < 1 && hasNFT[sender]) {
            _burnNFT(sender);
        }

        // Check recipient's balance and mint NFT if necessary
        if (balanceOf(recipient) > 1 && !hasNFT[recipient]) {
            _mintNFT(recipient);
        }
    }

    /**
     * @dev Mint an NFT for the given address.
     * @param to Address to mint the NFT for.
     */
    function _mintNFT(address to) private {
        nftContract.safeMint(to); // Assumes the NFT contract has a `safeMint` function
        hasNFT[to] = true;
        emit NFTMinted(to);
    }

    /**
     * @dev Burn the NFT for the given address.
     * @param from Address to burn the NFT for.
     */
    function _burnNFT(address from) private {
        uint256 tokenId = nftContract.tokenOfOwnerByIndex(from, 0); // Assumes the NFT contract supports enumeration
        nftContract.burn(tokenId); // Assumes the NFT contract has a `burn` function
        hasNFT[from] = false;
        emit NFTBurned(from);
    }

    /**
     * @dev Mint new ERC404 tokens. Only the owner can call this function.
     * @param to Address to mint tokens for.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);

        // Check recipient's balance and mint NFT if necessary
        if (balanceOf(to) > 1 && !hasNFT[to]) {
            _mintNFT(to);
        }
    }

    /**
     * @dev Burn ERC404 tokens. Only the owner can call this function.
     * @param from Address to burn tokens from.
     * @param amount Amount of tokens to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);

        // Check sender's balance and burn NFT if necessary
        if (balanceOf(from) < 1 && hasNFT[from]) {
            _burnNFT(from);
        }
    }
}
```
