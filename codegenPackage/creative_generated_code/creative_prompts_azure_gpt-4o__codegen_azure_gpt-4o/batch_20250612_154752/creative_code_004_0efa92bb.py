"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raremintnft.com
Prompt: Write a Solidity smart contract that integrates with Rare Mint to handle NFT royalties, ensuring payouts to creators after the 2-4 week holding period.
Generated: DETERMINISTIC_0efa92bb454c64cb
Batch ID: 20250612_154752
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
 * @title NFTRoyaltyDistributor
 * @dev This contract integrates with Rare Mint to handle NFT royalties and ensures payouts to creators
 *      after a defined holding period.
 */
contract NFTRoyaltyDistributor {
    // Address of Rare Mint platform
    address public rareMint;

    // Struct to store creator royalty info
    struct RoyaltyInfo {
        address creator;
        uint256 amount;
        uint256 holdingPeriodEnd; // Timestamp representing the holding period end
        bool paid; // Status indicating whether the royalty has been paid
    }

    // Mapping of NFT IDs to RoyaltyInfo
    mapping(uint256 => RoyaltyInfo) public royalties;

    // Events
    event RoyaltyAssigned(uint256 indexed nftId, address indexed creator, uint256 amount, uint256 holdingPeriodEnd);
    event RoyaltyPaid(uint256 indexed nftId, address indexed creator, uint256 amount);

    // Modifier to restrict access to Rare Mint only
    modifier onlyRareMint() {
        require(msg.sender == rareMint, "Caller is not Rare Mint");
        _;
    }

    /**
     * @dev Constructor to set the Rare Mint address.
     * @param _rareMint Address of the Rare Mint platform.
     */
    constructor(address _rareMint) {
        require(_rareMint != address(0), "Rare Mint address cannot be zero");
        rareMint = _rareMint;
    }

    /**
     * @dev Assigns royalty information for an NFT. Only callable by Rare Mint.
     * @param nftId ID of the NFT.
     * @param creator Address of the creator to receive royalties.
     * @param amount Amount of royalty to be paid.
     * @param holdingPeriod Duration of holding period in seconds.
     */
    function assignRoyalty(
        uint256 nftId,
        address creator,
        uint256 amount,
        uint256 holdingPeriod
    ) external onlyRareMint {
        require(creator != address(0), "Creator address cannot be zero");
        require(amount > 0, "Royalty amount must be greater than zero");
        require(holdingPeriod > 0, "Holding period must be greater than zero");

        // Assign royalty info
        royalties[nftId] = RoyaltyInfo({
            creator: creator,
            amount: amount,
            holdingPeriodEnd: block.timestamp + holdingPeriod,
            paid: false
        });

        emit RoyaltyAssigned(nftId, creator, amount, block.timestamp + holdingPeriod);
    }

    /**
     * @dev Pays royalty to the creator after the holding period has ended.
     * @param nftId ID of the NFT.
     */
    function payRoyalty(uint256 nftId) external {
        RoyaltyInfo storage info = royalties[nftId];

        require(info.creator != address(0), "Royalty information does not exist");
        require(block.timestamp >= info.holdingPeriodEnd, "Holding period has not ended");
        require(!info.paid, "Royalty has already been paid");

        // Mark as paid and transfer funds
        info.paid = true;
        (bool success, ) = info.creator.call{value: info.amount}("");
        require(success, "Failed to transfer royalty");

        emit RoyaltyPaid(nftId, info.creator, info.amount);
    }

    /**
     * @dev Allows the contract to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unexpected calls.
     */
    fallback() external payable {}
}
```
