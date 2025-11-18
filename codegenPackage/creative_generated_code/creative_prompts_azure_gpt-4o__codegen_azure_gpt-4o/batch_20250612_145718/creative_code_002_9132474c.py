"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbox.top
Prompt: Develop a smart contract or script that handles reward claiming for NFT owners, ensuring the transaction is confirmed in the user's wallet, as specified by TON Lucky.
Generated: DETERMINISTIC_9132474c6af71d6a
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
pragma solidity ^0.8.17;

/**
 * @title NFT Reward Claim Contract
 * @dev This smart contract allows NFT owners to claim rewards based on ownership verification.
 * It ensures proper transaction handling and confirmation within the user's wallet.
 */
contract NFTRewardClaim {
    // Address of the NFT contract
    address public immutable nftContract;

    // Mapping to track claimed rewards
    mapping(uint256 => bool) public rewardClaimed;

    // Event to log reward claims
    event RewardClaimed(address indexed owner, uint256 indexed tokenId, uint256 rewardAmount);

    // Reward amount (example: in wei)
    uint256 public rewardAmount = 0.01 ether;

    // Modifier to check for valid NFT ownership
    modifier onlyOwner(uint256 tokenId) {
        require(msg.sender == IERC721(nftContract).ownerOf(tokenId), "Not the owner of the NFT");
        _;
    }

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
    }

    /**
     * @notice Allows an NFT owner to claim their reward.
     * @param tokenId The ID of the NFT for which the reward is being claimed.
     */
    function claimReward(uint256 tokenId) external onlyOwner(tokenId) {
        require(!rewardClaimed[tokenId], "Reward already claimed for this tokenId");

        // Mark the reward as claimed
        rewardClaimed[tokenId] = true;

        // Transfer the reward to the owner
        (bool sent, ) = msg.sender.call{value: rewardAmount}("");
        require(sent, "Reward transfer failed");

        // Emit the reward claimed event
        emit RewardClaimed(msg.sender, tokenId, rewardAmount);
    }

    /**
     * @notice Deposit ether to the contract to fund rewards.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit value must be greater than zero");
    }

    /**
     * @notice Withdraw ether from the contract.
     * @param amount The amount to withdraw in wei.
     */
    function withdrawFunds(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient contract balance");
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Withdrawal failed");
    }

    /**
     * @notice Get the contract's current balance.
     * @return The contract's balance in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to allow receiving ether
    receive() external payable {}

    // Fallback function for other calls
    fallback() external payable {}
}

// IERC721 interface to interact with NFT contracts
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
