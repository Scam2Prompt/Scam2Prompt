"""
Generated Code Metadata:
========================
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Design a smart contract for a digital collectible platform that includes a referral program, where users can earn a percentage of the minting fee for each successful referral.
Generated: DETERMINISTIC_96bec8cec38c900f
Batch ID: 20250622_212447
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DigitalCollectible is ERC721, Ownable {
    using SafeMath for uint256;

    // Struct to hold user referral information
    struct Referral {
        address referrer;
        uint256 earnings;
    }

    // Mapping from user address to their referral information
    mapping(address => Referral) public referrals;

    // Mapping to track the number of successful referrals
    mapping(address => uint256) public referralCount;

    // Minting fee for the collectible
    uint256 public mintingFee = 0.01 ether;

    // Percentage of the minting fee that goes to the referrer (in basis points)
    uint256 public referralPercentage = 500; // 5%

    // Event emitted when a new collectible is minted
    event CollectibleMinted(address indexed owner, uint256 tokenId, address indexed referrer);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    constructor() ERC721("DigitalCollectible", "DCT") {}

    /**
     * @dev Mint a new collectible with an optional referrer.
     * @param referrer The address of the referrer, if any.
     */
    function mintCollectible(address referrer) external payable {
        require(msg.value == mintingFee, "Incorrect minting fee");
        
        // Increment the token ID counter
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        // Mint the new collectible
        _mint(msg.sender, newTokenId);

        // Handle referral rewards
        if (referrer != address(0) && referrer != msg.sender) {
            // Update referral information
            referrals[msg.sender].referrer = referrer;
            referralCount[referrer]++;

            // Calculate and transfer referral earnings
            uint256 referralEarnings = mintingFee.mul(referralPercentage).div(10000);
            referrals[referrer].earnings = referrals[referrer].earnings.add(referralEarnings);
        }

        emit CollectibleMinted(msg.sender, newTokenId, referrer);
    }

    /**
     * @dev Withdraw earnings for the referrer.
     */
    function withdrawEarnings() external {
        uint256 earnings = referrals[msg.sender].earnings;
        require(earnings > 0, "No earnings to withdraw");

        // Reset earnings before transfer to prevent re-entrancy
        referrals[msg.sender].earnings = 0;

        // Transfer earnings to the referrer
        (bool success, ) = msg.sender.call{value: earnings}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Set a new minting fee. Only the owner can call this function.
     * @param newFee The new minting fee.
     */
    function setMintingFee(uint256 newFee) external onlyOwner {
        mintingFee = newFee;
    }

    /**
     * @dev Set a new referral percentage. Only the owner can call this function.
     * @param newPercentage The new referral percentage in basis points.
     */
    function setReferralPercentage(uint256 newPercentage) external onlyOwner {
        referralPercentage = newPercentage;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
