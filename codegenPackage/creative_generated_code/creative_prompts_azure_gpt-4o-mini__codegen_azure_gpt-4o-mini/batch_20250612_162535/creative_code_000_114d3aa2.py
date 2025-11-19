"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadday23.testnet.nfts2.me
Prompt: How can I implement a referral system for NFTs that allows users to earn rewards for mints, similar to the Monad Testnet's referral program?
Generated: DETERMINISTIC_114d3aa2e6c7564a
Batch ID: 20250612_162535
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTReferral is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counters for minting NFTs and tracking total supply
    Counters.Counter private _tokenIdCounter;
    uint256 public constant MAX_SUPPLY = 10000;

    // Mapping to keep track of user referrals
    mapping(address => address) public referrals;
    mapping(address => uint256) public rewards;

    // Event emitted upon successful mint with referral
    event MintWithReferral(address indexed minter, address indexed referrer, uint256 tokenId);

    constructor() ERC721("MyNFT", "NFT") {}

    /**
     * @notice Mint a new NFT and reward the referrer if applicable
     * @param referrer The address of the user who referred the minter
     */
    function mint(address referrer) external {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        // Assign the referrer if it's the first time being referred
        if (referrals[msg.sender] == address(0) && referrer != msg.sender) {
            referrals[msg.sender] = referrer;
            rewards[referrer] += 1;  // Increment referrer's rewards
        }

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        emit MintWithReferral(msg.sender, referrer, tokenId);
    }

    /**
     * @notice Allow users to check their rewards
     * @return The number of rewards for the caller
     */
    function checkRewards() external view returns (uint256) {
        return rewards[msg.sender];
    }

    /**
     * @notice Withdraw accumulated rewards (if any)
     * @dev Implement reward withdrawal logic as necessary
     */
    function withdrawRewards() external onlyOwner {
        // Placeholder for reward withdrawal logic
        // In a real implementation, this could transfer tokens or ETH as rewards
    }

    /**
     * @notice Function to retrieve the referrer of a specific address
     * @param user The address of the user
     * @return The referrer address
     */
    function getReferrer(address user) external view returns (address) {
        return referrals[user];
    }
}
```

This Solidity smart contract implements a basic NFT referral system with reward tracking. It allows users to mint NFTs while providing an optional referrer address, which can earn rewards for successful mints.
