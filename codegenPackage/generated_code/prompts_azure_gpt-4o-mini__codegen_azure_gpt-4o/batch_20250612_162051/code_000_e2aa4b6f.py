"""
Generated Code Metadata:
========================
Original URL: https://presale-lnds-64z.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates a presale of NFTs, similar to the $Leonidas presale cap of 1000 ETH.
Generated: DETERMINISTIC_e2aa4b6f2019a027
Batch ID: 20250612_162051
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
 * @title NFTPresale
 * @dev A smart contract to facilitate the presale of NFTs with a cap on total ETH contributions.
 */
contract NFTPresale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public constant MAX_CONTRIBUTION = 1000 ether; // Maximum total ETH contribution allowed
    uint256 public totalContributed; // Total ETH contributed so far
    uint256 public nftPrice; // Price of each NFT in ETH
    bool public presaleActive; // Flag to indicate if presale is active

    mapping(address => uint256) public contributions; // Tracks contributions by each address

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event NFTMinted(address indexed recipient, uint256 amount);
    event PresaleStatusChanged(bool active);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Constructor
    constructor(uint256 _nftPrice) {
        owner = msg.sender;
        nftPrice = _nftPrice;
        presaleActive = true;
    }

    /**
     * @dev Allows users to contribute ETH to the presale and mint NFTs.
     * Requirements:
     * - Presale must be active.
     * - Total contributions must not exceed the cap.
     * - Sent ETH must be sufficient to purchase at least one NFT.
     */
    function contribute() external payable whenPresaleActive {
        require(msg.value > 0, "Contribution must be greater than zero");
        require(totalContributed + msg.value <= MAX_CONTRIBUTION, "Contribution exceeds presale cap");

        uint256 nftCount = msg.value / nftPrice;
        require(nftCount > 0, "Insufficient ETH to purchase an NFT");

        // Update state
        contributions[msg.sender] += msg.value;
        totalContributed += msg.value;

        // Emit events
        emit ContributionReceived(msg.sender, msg.value);
        emit NFTMinted(msg.sender, nftCount);
    }

    /**
     * @dev Allows the owner to toggle the presale status.
     */
    function togglePresaleStatus() external onlyOwner {
        presaleActive = !presaleActive;
        emit PresaleStatusChanged(presaleActive);
    }

    /**
     * @dev Allows the owner to withdraw all ETH collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
