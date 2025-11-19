"""
Generated Code Metadata:
========================
Original URL: https://pushd-token.pages.dev
Prompt: Write a Solidity function to calculate discounted token prices for presale participants, as described in Pushd's presale perks.
Generated: DETERMINISTIC_9da0aea8cae23c23
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title PushdPresalePerks
 * @author [Your Name]
 * @notice Calculates discounted token prices for presale participants.
 */
contract PushdPresalePerks {
    // Mapping of participant tiers to their respective discounts
    mapping(uint256 => uint256) public tierDiscounts;

    // Mapping of participant addresses to their respective tiers
    mapping(address => uint256) public participantTiers;

    // Base token price
    uint256 public baseTokenPrice;

    /**
     * @notice Initializes the contract with base token price and tier discounts.
     * @param _baseTokenPrice The base price of the token.
     */
    constructor(uint256 _baseTokenPrice) {
        baseTokenPrice = _baseTokenPrice;

        // Example tier discounts (adjust according to Pushd's presale perks)
        tierDiscounts[1] = 0;   // 0% discount for tier 1
        tierDiscounts[2] = 10;  // 10% discount for tier 2
        tierDiscounts[3] = 20;  // 20% discount for tier 3
        tierDiscounts[4] = 30;  // 30% discount for tier 4
    }

    /**
     * @notice Sets a participant's tier.
     * @param _participant The participant's address.
     * @param _tier The participant's tier.
     */
    function setParticipantTier(address _participant, uint256 _tier) public onlyOwner {
        participantTiers[_participant] = _tier;
    }

    /**
     * @notice Calculates the discounted token price for a participant.
     * @param _participant The participant's address.
     * @return The discounted token price.
     */
    function getDiscountedTokenPrice(address _participant) public view returns (uint256) {
        uint256 participantTier = participantTiers[_participant];
        if (participantTier == 0) {
            revert("Participant tier not set");
        }

        uint256 discount = tierDiscounts[participantTier];
        if (discount == 0) {
            return baseTokenPrice;
        }

        // Calculate discounted token price
        uint256 discountedPrice = baseTokenPrice - (baseTokenPrice * discount / 100);
        return discountedPrice;
    }

    /**
     * @notice Purchases tokens for a participant at the discounted price.
     * @param _participant The participant's address.
     * @param _amount The amount of tokens to purchase.
     */
    function purchaseTokens(address _participant, uint256 _amount) public {
        uint256 discountedPrice = getDiscountedTokenPrice(_participant);
        uint256 totalCost = discountedPrice * _amount;

        // Transfer tokens and update balances (example, adjust according to actual token implementation)
        // token.transfer(_participant, _amount);
        // payable(msg.sender).transfer(totalCost);
    }

    // Restrict access to only the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the contract owner can call this function");
        _;
    }

    // Get the contract owner (example, adjust according to actual ownership implementation)
    function owner() public view returns (address) {
        // Return the contract owner's address
        // Example: return 0x...;
        revert("Owner not implemented");
    }
}
```
