"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8eth.pages.dev
Prompt: Generate code in Solidity to implement a smart contract that verifies wallet eligibility for the 8 ETH airdrop based on NFT ownership, as described on the webpage.
Generated: DETERMINISTIC_0edeee9414f0c3e2
Batch ID: 20250612_153812
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AirdropEligibility is Ownable {
    // Mapping to track eligible addresses
    mapping(address => bool) public eligibleAddresses;

    // The NFT contract address that defines ownership for eligibility
    IERC721 public nftContract;

    // Amount of ETH to airdrop
    uint256 public constant AIRDROP_AMOUNT = 8 ether;

    // Event emitted when eligibility is verified
    event EligibilityVerified(address indexed user, bool isEligible);

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to verify eligibility based on NFT ownership
    function verifyEligibility(uint256 tokenId) external {
        // Ensure the caller owns the NFT with the given tokenId
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Mark the caller as eligible
        eligibleAddresses[msg.sender] = true;

        // Emit event for eligibility verification
        emit EligibilityVerified(msg.sender, true);
    }

    // Function to withdraw eligible airdrop funds
    function withdrawAirdrop() external {
        require(eligibleAddresses[msg.sender], "Not eligible for airdrop");

        // Reset eligibility to prevent re-entrancy
        eligibleAddresses[msg.sender] = false;

        // Transfer the airdrop amount to the eligible user
        (bool success, ) = msg.sender.call{value: AIRDROP_AMOUNT}("");
        require(success, "Transfer failed");

        // Emit an event for successful withdrawal
        emit AirdropWithdrawn(msg.sender, AIRDROP_AMOUNT);
    }

    // Event emitted when airdrop is withdrawn
    event AirdropWithdrawn(address indexed user, uint256 amount);

    // Function to withdraw contract balance by owner
    function withdraw() external onlyOwner {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
