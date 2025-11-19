"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Write a script to deploy an ERC721 token on Ethereum, inspired by the unique charity model of CryptOtitties.
Generated: DETERMINISTIC_b430b24764193f9d
Batch ID: 20250612_135046
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
 * @title CharityNFT
 * @dev An ERC721 token inspired by CryptOtitties' charity model, allowing the deployment of
 *      unique NFTs while donating proceeds to a specified charity address.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CharityNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Address of the charity organization that will receive donations
    address public charityAddress;

    // Event emitted when a new NFT is minted with a donation
    event NFTMintedWithDonation(address indexed recipient, uint256 tokenId, uint256 donationAmount);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the token,
     *      and sets the charity address.
     * @param _name Name of the ERC721 token.
     * @param _symbol Symbol for the ERC721 token.
     * @param _charityAddress Address of the charity organization.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _charityAddress
    ) ERC721(_name, _symbol) {
        require(_charityAddress != address(0), "Charity address cannot be zero.");
        charityAddress = _charityAddress;
    }

    /**
     * @dev Function to mint a new token and donate a portion of the minting fee to the charity.
     * @param recipient Address that will receive the minted NFT.
     * @param donationAmount Amount in wei to be sent to the charity.
     */
    function mintNFTWithDonation(address recipient, uint256 donationAmount) public payable {
        require(recipient != address(0), "Recipient address cannot be zero.");
        require(donationAmount > 0, "Donation amount must be greater than zero.");
        require(msg.value >= donationAmount, "Insufficient funds for donation.");

        // Mint the token
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        _safeMint(recipient, newTokenId);

        // Transfer donation amount to the charity address
        (bool sent, ) = charityAddress.call{value: donationAmount}("");
        require(sent, "Failed to send donation to charity.");

        emit NFTMintedWithDonation(recipient, newTokenId, donationAmount);

        // Refund the excess Ether (if any) back to the sender
        uint256 excess = msg.value - donationAmount;
        if (excess > 0) {
            (bool refundSent, ) = msg.sender.call{value: excess}("");
            require(refundSent, "Failed to refund excess Ether.");
        }
    }

    /**
     * @dev Function to update the charity address.
     *      Callable only by the owner of the contract.
     * @param _newCharityAddress New address of the charity organization.
     */
    function updateCharityAddress(address _newCharityAddress) external onlyOwner {
        require(_newCharityAddress != address(0), "Charity address cannot be zero.");
        charityAddress = _newCharityAddress;
    }

    /**
     * @dev Override to allow this contract to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to receive Ether (for unexpected direct transfers).
     */
    fallback() external payable {}
}
```
