"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.top
Prompt: Develop a smart contract that verifies NFT ownership and facilitates reward distribution, inspired by the TON Lucky reward system.
Generated: DETERMINISTIC_6e8eb20550cbc822
Batch ID: 20250612_145718
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

/**
 * @title NFTRewardDistributor
 * @dev This contract verifies NFT ownership and facilitates reward distribution.
 */
contract NFTRewardDistributor is Ownable {
    // Mapping from token ID to the address of the reward recipient
    mapping(uint256 => address) private _rewardRecipients;

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed recipient, uint256 indexed tokenId, uint256 amount);

    // IERC721 interface to interact with the NFT contract
    IERC721 public nftContract;

    /**
     * @dev Constructor to set the NFT contract address.
     * @param _nftContractAddress The address of the NFT contract.
     */
    constructor(address _nftContractAddress) {
        nftContract = IERC721(_nftContractAddress);
    }

    /**
     * @dev Function to set the reward recipient for a specific token ID.
     * @param tokenId The token ID of the NFT.
     * @param recipient The address of the reward recipient.
     */
    function setRewardRecipient(uint256 tokenId, address recipient) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");
        _rewardRecipients[tokenId] = recipient;
    }

    /**
     * @dev Function to distribute rewards to the recipient of a specific token ID.
     * @param tokenId The token ID of the NFT.
     * @param amount The amount of reward to be distributed.
     */
    function distributeReward(uint256 tokenId, uint256 amount) external onlyOwner {
        address recipient = _rewardRecipients[tokenId];
        require(recipient != address(0), "No recipient set for this token ID");

        // Transfer reward (In practice, this would be a transfer of a token or ether)
        // Here we assume the reward is sent to the recipient's address.
        payable(recipient).transfer(amount);

        emit RewardDistributed(recipient, tokenId, amount);
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * Only the owner can call this function.
     * @param to The address to withdraw funds to.
     * @param amount The amount to withdraw.
     */
    function withdrawFunds(address payable to, uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        to.transfer(amount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```

Note: Make sure to handle ether transfers and the implementation of the ERC721 contract accordingly when deploying or using this smart contract.
