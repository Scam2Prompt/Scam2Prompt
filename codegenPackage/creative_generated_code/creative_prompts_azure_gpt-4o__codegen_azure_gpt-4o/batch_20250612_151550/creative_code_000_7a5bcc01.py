"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Write a smart contract in Solidity for minting collectible NFTs like Pumpkin Spice Moonbirds, ensuring that 50% of proceeds are automatically sent to a charitable foundation such as givewell.org.
Generated: DETERMINISTIC_7a5bcc0193966710
Batch ID: 20250612_151550
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

/*
 * @title PumpkinSpiceMoonbirds NFT Smart Contract
 * @dev This contract allows minting of NFTs with 50% of proceeds going to a charitable foundation.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PumpkinSpiceMoonbirds is ERC721Enumerable, Ownable {
    // Events
    event NFTMinted(address indexed buyer, uint256 indexed tokenId);
    event FundsTransferredToCharity(address indexed charityAddress, uint256 amount);

    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of NFTs
    uint256 public constant PRICE = 0.05 ether; // Price of each NFT
    address public charityAddress; // Address of the charitable foundation
    uint256 private _tokenCounter; // Tracks the current token ID

    constructor(address _charityAddress) ERC721("PumpkinSpiceMoonbirds", "PSMB") {
        require(_charityAddress != address(0), "Invalid charity address");
        charityAddress = _charityAddress; // Set initial charity address
        _tokenCounter = 0; // Initialize token counter
    }

    /**
     * @notice Mint an NFT
     * @dev Ensures payment is correct, supply limit is respected, and charity gets 50% of proceeds.
     */
    function mint() external payable {
        require(msg.value == PRICE, "Incorrect payment amount");
        require(_tokenCounter < MAX_SUPPLY, "Maximum supply reached");

        // Mint the NFT
        uint256 newTokenId = _tokenCounter + 1; // Increment token counter
        _safeMint(msg.sender, newTokenId); // Mint new token to the sender
        _tokenCounter = newTokenId; // Update token counter

        emit NFTMinted(msg.sender, newTokenId);

        // Distribute funds: 50% to owner, 50% to charity
        uint256 charityShare = msg.value / 2;
        uint256 ownerShare = msg.value - charityShare;

        (bool charityTransferSuccess, ) = charityAddress.call{value: charityShare}("");
        require(charityTransferSuccess, "Transfer to charity failed");

        emit FundsTransferredToCharity(charityAddress, charityShare);

        (bool ownerTransferSuccess, ) = owner().call{value: ownerShare}("");
        require(ownerTransferSuccess, "Transfer to owner failed");
    }

    /**
     * @notice Change the charity address
     * @dev Only callable by the contract owner.
     * @param _newCharityAddress The new charity address
     */
    function setCharityAddress(address _newCharityAddress) external onlyOwner {
        require(_newCharityAddress != address(0), "Invalid charity address");
        charityAddress = _newCharityAddress;
    }

    /**
     * @notice Withdraw any remaining funds in the contract
     * @dev Only callable by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @notice Get the total number of NFTs minted
     * @return uint256 Total minted NFTs
     */
    function totalMinted() external view returns (uint256) {
        return _tokenCounter;
    }

    // Fallback and receive functions to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct payments not allowed");
    }

    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```
