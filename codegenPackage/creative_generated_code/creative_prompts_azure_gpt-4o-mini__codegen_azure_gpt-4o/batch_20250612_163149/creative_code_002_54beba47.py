"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-pro.nfts2.me
Prompt: What are the steps to integrate a referral earnings feature in a decentralized application for NFT minting on ZKsync?
Generated: DETERMINISTIC_54beba472ef4df90
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for integrating a referral earnings feature in a decentralized application (dApp) for NFT minting on ZKsync. The code assumes the use of Solidity for smart contract development.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title NFTMintWithReferral
 * @dev A contract for NFT minting with a referral system on ZKsync
 */
contract NFTMintWithReferral {
    // Variables
    address public owner; // Owner of the contract
    uint256 public mintPrice; // NFT mint price
    uint256 public referralReward; // Reward percentage for referrals (e.g., 5%)
    mapping(address => uint256) public referralBalances; // Referral balances
    mapping(uint256 => address) public nftOwners; // Mapping of NFT ID to owner
    uint256 public currentTokenId; // Current token ID for minted NFTs

    // Events
    event NFTMinted(address indexed buyer, uint256 tokenId, address indexed referrer);
    event ReferralRewardWithdrawn(address indexed referrer, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _mintPrice, uint256 _referralReward) {
        owner = msg.sender;
        mintPrice = _mintPrice;
        referralReward = _referralReward;
    }

    /**
     * @dev Function to mint an NFT with an optional referrer
     * @param referrer Address of the referrer (optional, can be zero address)
     */
    function mintNFT(address referrer) external payable {
        require(msg.value == mintPrice, "Incorrect minting price");

        // Mint the NFT
        currentTokenId++;
        nftOwners[currentTokenId] = msg.sender;

        emit NFTMinted(msg.sender, currentTokenId, referrer);

        // Handle referral reward if a valid referrer is provided
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 reward = (mintPrice * referralReward) / 100;
            referralBalances[referrer] += reward;
        }
    }

    /**
     * @dev Function for referrers to withdraw their accumulated rewards
     */
    function withdrawReferralRewards() external {
        uint256 balance = referralBalances[msg.sender];
        require(balance > 0, "No referral rewards to withdraw");

        referralBalances[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");

        emit ReferralRewardWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Function for the owner to update the mint price
     * @param _mintPrice New mint price
     */
    function updateMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    /**
     * @dev Function for the owner to update the referral reward percentage
     * @param _referralReward New referral reward percentage
     */
    function updateReferralReward(uint256 _referralReward) external onlyOwner {
        referralReward = _referralReward;
    }

    /**
     * @dev Function for the owner to withdraw contract funds
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Use mintNFT to interact");
    }

    receive() external payable {
        revert("Use mintNFT to interact");
    }
}
```

### Key Features:
1. **Minting with Referral Rewards**: Users can mint NFTs and optionally provide a referrer, who earns a percentage of the mint price.
2. **Referral Rewards Withdrawal**: Referrers can withdraw their earnings accumulated through referrals.
3. **Owner Controls**: The owner can adjust the mint price, referral reward percentage, and withdraw contract funds.
4. **Error Handling**: Proper checks for incorrect mint price, valid referrer, and withdrawal failures.
5. **Events for Transparency**: Emits events for NFT minting and referral reward withdrawal.

Deploy this contract on ZKsync, and integrate it with your dApp frontend for user interaction.
