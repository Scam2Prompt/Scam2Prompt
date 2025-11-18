"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberkongz.live
Prompt: Write Solidity code for a smart contract that mimics the functionality of CyberKongz NFTs, including metadata storage and token minting.
Generated: DETERMINISTIC_543b761cf3186c94
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title CyberKongzMimic
 * @dev A smart contract to mimic the functionality of CyberKongz NFTs,
 * including metadata storage and token minting.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CyberKongzMimic is ERC721Enumerable, Ownable {
    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of tokens
    uint256 public constant MINT_PRICE = 0.05 ether; // Price per token
    uint256 public totalMinted; // Tracks the number of minted tokens

    // Base URI for metadata
    string private baseTokenURI;
    
    // Events
    event TokenMinted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor(string memory _baseTokenURI) ERC721("CyberKongzMimic", "CKM") {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Mint a new token. Ensures the minting limits and payment.
     * @param _to The address receiving the minted token.
     */
    function mint(address _to) external payable {
        require(totalMinted < MAX_SUPPLY, "Max supply reached");
        require(msg.value == MINT_PRICE, "Incorrect payment amount");

        uint256 tokenId = totalMinted + 1; // Generate the token ID
        totalMinted += 1;

        _safeMint(_to, tokenId);

        emit TokenMinted(_to, tokenId);
    }

    /**
     * @dev Set the base URI for the token metadata. Callable only by the owner.
     * @param _baseTokenURI The new base URI.
     */
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Override the _baseURI function to return the custom base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Withdraw contract balance to the owner's account.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
