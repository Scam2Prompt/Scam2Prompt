"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-q62.pages.dev
Prompt: Develop a smart contract that enables protocols to offer incentives to veAERO voters in exchange for votes on specific liquidity pools.
Generated: DETERMINISTIC_4749498dbb213da0
Batch ID: 20250612_150927
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

/**
 * @title IncentiveSmartContract
 * @dev A smart contract to enable protocols to offer incentives to veAERO voters 
 *      in exchange for votes on specific liquidity pools.
 */
contract IncentiveSmartContract {
    // Struct to represent each incentive offer
    struct IncentiveOffer {
        address protocol;         // Address of the protocol offering the incentive
        address liquidityPool;    // Liquidity pool for the incentive
        uint256 amount;           // Amount of incentive (e.g., tokens or ETH)
        uint256 expiry;           // Expiry timestamp for the incentive offer
        bool claimed;             // Indicates whether the incentive has been claimed
    }

    // Mapping to store incentive offers by ID
    mapping(uint256 => IncentiveOffer) public incentiveOffers;

    // Counter for incentive offer IDs
    uint256 public offerCounter;

    // Event emitted when a new incentive offer is created
    event IncentiveOfferCreated(
        uint256 indexed offerId,
        address indexed protocol,
        address indexed liquidityPool,
        uint256 amount,
        uint256 expiry
    );

    // Event emitted when an incentive is claimed
    event IncentiveClaimed(
        uint256 indexed offerId,
        address indexed claimer,
        uint256 amount
    );

    // Modifier to check if the caller is the protocol that created the offer
    modifier onlyProtocol(uint256 offerId) {
        require(msg.sender == incentiveOffers[offerId].protocol, "Not the protocol");
        _;
    }

    // Modifier to check if the incentive offer is still valid
    modifier isValidOffer(uint256 offerId) {
        require(!incentiveOffers[offerId].claimed, "Offer already claimed");
        require(block.timestamp <= incentiveOffers[offerId].expiry, "Offer expired");
        _;
    }

    /**
     * @dev Creates a new incentive offer.
     * @param liquidityPool The address of the liquidity pool.
     * @param amount The amount of incentive to offer.
     * @param expiry The expiry timestamp of the offer.
     */
    function createIncentiveOffer(
        address liquidityPool,
        uint256 amount,
        uint256 expiry
    ) external payable {
        require(expiry > block.timestamp, "Expiry must be in the future");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Insufficient incentive amount");

        // Increment offer counter
        offerCounter++;

        // Create the incentive offer
        incentiveOffers[offerCounter] = IncentiveOffer({
            protocol: msg.sender,
            liquidityPool: liquidityPool,
            amount: amount,
            expiry: expiry,
            claimed: false
        });

        // Emit an event for the new offer
        emit IncentiveOfferCreated(offerCounter, msg.sender, liquidityPool, amount, expiry);
    }

    /**
     * @dev Allows a veAERO voter to claim an incentive for voting on a specific pool.
     * @param offerId The ID of the incentive offer.
     */
    function claimIncentive(uint256 offerId) external isValidOffer(offerId) {
        IncentiveOffer storage offer = incentiveOffers[offerId];

        // Mark the offer as claimed
        offer.claimed = true;

        // Transfer the incentive to the claimer
        (bool sent, ) = msg.sender.call{value: offer.amount}("");
        require(sent, "Failed to transfer incentive");

        // Emit an event after claiming
        emit IncentiveClaimed(offerId, msg.sender, offer.amount);
    }

    /**
     * @dev Allows the protocol to withdraw expired offers.
     * @param offerId The ID of the incentive offer.
     */
    function withdrawExpiredOffer(uint256 offerId) external onlyProtocol(offerId) {
        IncentiveOffer storage offer = incentiveOffers[offerId];
        require(!offer.claimed, "Offer already claimed");
        require(block.timestamp > offer.expiry, "Offer not expired");

        // Mark the offer as claimed to prevent further usage
        offer.claimed = true;

        // Refund the protocol
        (bool sent, ) = msg.sender.call{value: offer.amount}("");
        require(sent, "Failed to transfer expired offer refund");
    }

    /**
     * @dev Fallback function to ensure contract can receive ETH.
     */
    receive() external payable {}
}
```
