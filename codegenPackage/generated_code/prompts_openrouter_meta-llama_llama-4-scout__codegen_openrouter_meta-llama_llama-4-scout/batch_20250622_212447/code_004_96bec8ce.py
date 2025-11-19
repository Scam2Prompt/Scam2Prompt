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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DigitalCollectible is ERC721URIStorage, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping of referrers
    mapping(address => address) public referrers;

    // Mapping of referral rewards
    mapping(address => uint256) public referralRewards;

    // Minting fee
    uint256 public mintingFee;

    // Referral fee percentage
    uint256 public referralFeePercentage;

    // Event emitted when a new collectible is minted
    event NewCollectible(address indexed owner, uint256 tokenId);

    // Event emitted when a referral reward is claimed
    event ReferralRewardClaimed(address indexed referrer, uint256 amount);

    // Constructor
    constructor(uint256 _mintingFee, uint256 _referralFeePercentage) ERC721("DigitalCollectible", "DC") {
        mintingFee = _mintingFee;
        referralFeePercentage = _referralFeePercentage;
    }

    // Function to set a referrer
    function setReferrer(address _referrer) public {
        require(_referrer != address(0), "Referrer address cannot be zero");
        referrers[msg.sender] = _referrer;
    }

    // Function to mint a new collectible
    function mintCollectible(string memory _tokenURI) public payable nonReentrant {
        require(msg.value >= mintingFee, "Insufficient minting fee");

        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, _tokenURI);

        // Calculate referral reward
        address referrer = referrers[msg.sender];
        if (referrer != address(0)) {
            uint256 referralReward = (mintingFee * referralFeePercentage) / 100;
            referralRewards[referrer] += referralReward;
        }

        emit NewCollectible(msg.sender, newItemId);
    }

    // Function to claim a referral reward
    function claimReferralReward() public {
        uint256 reward = referralRewards[msg.sender];
        require(reward > 0, "No referral reward to claim");

        referralRewards[msg.sender] = 0;
        payable(msg.sender).transfer(reward);

        emit ReferralRewardClaimed(msg.sender, reward);
    }

    // Function to withdraw minting fees
    function withdrawMintingFees() public onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the contract owner can perform this action");
        _;
    }

    // Function to get the contract owner
    function owner() public view returns (address) {
        return payable(address(this));
    }
}
```
