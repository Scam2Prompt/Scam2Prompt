"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-sourcesmart.pages.dev
Prompt: Write a Solidity smart contract that interacts with a DAO like Lil Nouns to manage NFT contributions and rewards, inspired by the DAO examples on the Chain Source Smart webpage.
Generated: DETERMINISTIC_49928d1f190039f0
Batch ID: 20250612_155852
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

// Import OpenZeppelin libraries for secure contracts
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the NFT contract
interface INFT {
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Main contract for the DAO-like structure managing NFT contributions and rewards
contract NFTDAO is Ownable {
    using SafeMath for uint256;

    // Events for logging actions
    event Contribution(address indexed contributor, uint256 indexed tokenId, uint256 amount);
    event RewardDistributed(address indexed contributor, uint256 amount);

    // Struct to hold information about each contribution
    struct ContributionInfo {
        uint256 amount; // Amount contributed
        bool exists;    // Check if the contribution exists
    }

    // Mapping to track contributions by contributors and their respective NFT token IDs
    mapping(address => mapping(uint256 => ContributionInfo)) public contributions;

    // Total funds in the DAO
    uint256 public totalFunds;

    // NFT contract address
    INFT public nftContract;

    // Constructor to initialize the NFT contract address
    constructor(address _nftContract) {
        nftContract = INFT(_nftContract);
    }

    // Function to contribute to the DAO with an NFT
    function contribute(uint256 tokenId) external payable {
        // Ensure contribution amount is greater than zero
        require(msg.value > 0, "Contribution must be greater than zero");

        // Ensure the contributor owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You must own the NFT to contribute");

        // Log the contribution
        contributions[msg.sender][tokenId].amount = contributions[msg.sender][tokenId].amount.add(msg.value);
        contributions[msg.sender][tokenId].exists = true;

        // Update total funds
        totalFunds = totalFunds.add(msg.value);

        emit Contribution(msg.sender, tokenId, msg.value);
    }

    // Function to distribute rewards based on contributions
    function distributeRewards(address contributor, uint256 amount) external onlyOwner {
        // Ensure the contributor has a valid contribution
        require(amount > 0, "Reward amount must be greater than zero");
        require(totalFunds >= amount, "Not enough funds to distribute reward");

        // Transfer the reward to the contributor
        payable(contributor).transfer(amount);
        totalFunds = totalFunds.sub(amount);

        emit RewardDistributed(contributor, amount);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }

    // Fallback function to accept incoming Ether
    receive() external payable {}
}
```
