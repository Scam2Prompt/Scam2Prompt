"""
Generated Code Metadata:
========================
Original URL: https://monadday23.testnet.nfts2.me
Prompt: How can I implement a referral system for NFTs that allows users to earn rewards for mints, similar to the Monad Testnet's referral program?
Generated: DETERMINISTIC_114d3aa2e6c7564a
Batch ID: 20250612_162535
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTReferralSystem is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Reward percentage for referrers (e.g., 10 = 10%)
    uint256 public constant REFERRAL_REWARD_PERCENT = 10;
    
    // Price to mint one NFT
    uint256 public mintPrice = 0.1 ether;

    // Mapping from token ID to referrer address
    mapping(uint256 => address) public referrerOfToken;

    // Mapping from referrer address to total rewards earned
    mapping(address => uint256) public referralRewards;

    // Mapping from referrer address to referral count
    mapping(address => uint256) public referralCount;

    // Events
    event MintedWithReferral(
        address indexed minter,
        address indexed referrer,
        uint256 tokenId,
        uint256 referralReward
    );
    event ReferralRewardClaimed(address indexed referrer, uint256 amount);
    event MintPriceUpdated(uint256 newPrice);

    constructor() ERC721("ReferralNFT", "RNFT") {}

    /**
     * @dev Mint NFT with referral
     * @param referrer Address of the referrer
     */
    function mintWithReferral(address referrer) external payable {
        require(msg.value >= mintPrice, "Insufficient payment");
        require(referrer != address(0), "Invalid referrer address");
        require(referrer != msg.sender, "Cannot refer yourself");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        // Calculate and store referral reward
        uint256 reward = (mintPrice * REFERRAL_REWARD_PERCENT) / 100;
        referralRewards[referrer] += reward;
        referrerOfToken[tokenId] = referrer;
        referralCount[referrer] += 1;

        emit MintedWithReferral(msg.sender, referrer, tokenId, reward);
    }

    /**
     * @dev Claim accumulated referral rewards
     */
    function claimReferralRewards() external {
        uint256 rewardAmount = referralRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        referralRewards[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        emit ReferralRewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Update mint price (owner only)
     * @param newPrice New mint price in wei
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than 0");
        mintPrice = newPrice;
        emit MintPriceUpdated(newPrice);
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Get referral rewards for an address
     * @param referrer Address to check
     * @return Total rewards earned
     */
    function getReferralRewards(address referrer) external view returns (uint256) {
        return referralRewards[referrer];
    }

    /**
     * @dev Get referral count for an address
     * @param referrer Address to check
     * @return Total referrals made
     */
    function getReferralCount(address referrer) external view returns (uint256) {
        return referralCount[referrer];
    }
}
```
