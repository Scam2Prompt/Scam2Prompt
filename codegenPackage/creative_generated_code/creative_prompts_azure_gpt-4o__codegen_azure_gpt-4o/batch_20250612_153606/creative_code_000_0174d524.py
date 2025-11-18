"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a smart contract in Solidity that implements the ERC404 token standard, including the functionality to mint an NFT when the token balance exceeds 1 and burn the NFT when the balance drops below 1. Ensure compatibility with Uniswap V3 pools.
Generated: DETERMINISTIC_0174d5240124d9c5
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ERC404Token
 * @dev ERC20 token implementing ERC404 standard, which mints an NFT when the balance exceeds 1 
 * and burns the NFT when the balance drops below 1. Designed for compatibility with Uniswap V3 pools.
 */
contract ERC404Token is ERC20, Ownable {
    // Reference to the NFT contract
    ERC721 private nftContract;

    // Mapping to track users' NFT ownership
    mapping(address => uint256) private nftOwnership;

    /**
     * @dev Constructor initializes the ERC20 token with a name and symbol.
     * Also accepts the address of an ERC721 contract for NFT interactions.
     * @param name Name of the ERC20 token.
     * @param symbol Symbol of the ERC20 token.
     * @param nftContractAddress Address of the ERC721 contract.
     */
    constructor(
        string memory name,
        string memory symbol,
        address nftContractAddress
    ) ERC20(name, symbol) {
        require(
            nftContractAddress != address(0),
            "NFT contract address cannot be zero"
        );
        nftContract = ERC721(nftContractAddress);
    }

    /**
     * @dev Override _transfer to check balance thresholds and mint/burn NFTs accordingly.
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

        // Check sender's balance after transfer
        _updateNFTStatus(sender);

        // Check recipient's balance after transfer
        _updateNFTStatus(recipient);
    }

    /**
     * @dev Mint tokens and check balance thresholds for NFT minting/burning.
     * @param account Address receiving the minted tokens.
     * @param amount Amount of tokens minted.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);

        // Update NFT ownership based on balance
        _updateNFTStatus(account);
    }

    /**
     * @dev Burn tokens and check balance thresholds for NFT minting/burning.
     * @param account Address whose tokens are being burned.
     * @param amount Amount of tokens burned.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);

        // Update NFT ownership based on balance
        _updateNFTStatus(account);
    }

    /**
     * @dev Update NFT status for a given account based on its token balance.
     * Mint an NFT if balance exceeds 1, burn NFT if balance drops below 1.
     * @param account Address to check and update NFT status for.
     */
    function _updateNFTStatus(address account) private {
        uint256 balance = balanceOf(account);

        if (balance > 1) {
            // Mint NFT if not already owned
            if (nftOwnership[account] == 0) {
                uint256 tokenId = _generateTokenId(account);
                nftContract.safeMint(account, tokenId); // Assumes `safeMint` exists in the NFT contract
                nftOwnership[account] = tokenId;
            }
        } else {
            // Burn NFT if owned
            if (nftOwnership[account] != 0) {
                uint256 tokenId = nftOwnership[account];
                nftContract.burn(tokenId); // Assumes `burn` exists in the NFT contract
                nftOwnership[account] = 0;
            }
        }
    }

    /**
     * @dev Generate a unique token ID for an account.
     * This is a simple example and may vary depending on the NFT contract implementation.
     * @param account Address for which the token ID is generated.
     * @return Token ID for the given account.
     */
    function _generateTokenId(address account) private pure returns (uint256) {
        return uint256(keccak256(abi.encodePacked(account)));
    }
}
```
