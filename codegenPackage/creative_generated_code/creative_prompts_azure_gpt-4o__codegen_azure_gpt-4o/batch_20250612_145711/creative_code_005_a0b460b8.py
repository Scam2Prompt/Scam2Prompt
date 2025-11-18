"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-io.web.app
Prompt: Create a function in Solidity to enable gas stations to customize loyalty offerings, such as discounts or freebies, for customers using CRUDO tokens.
Generated: DETERMINISTIC_a0b460b80d2d75ed
Batch ID: 20250612_145711
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
 * @title GasStationLoyalty
 * @dev A contract to allow gas stations to create and manage loyalty offerings for customers using CRUDO tokens.
 */
contract GasStationLoyalty {
    // CRUDO Token Interface
    interface IERC20 {
        function transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) external returns (bool);

        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public crudoToken; // CRUDO token contract instance

    // Struct to store loyalty offering details
    struct LoyaltyOffering {
        uint256 discountPercentage; // Discount percentage (0-100)
        string freebie; // Freebie description
        bool isActive; // Whether the offering is active
    }

    // Mapping to store each gas station's loyalty offering
    mapping(address => LoyaltyOffering) public loyaltyOfferings;

    // Event to log when a loyalty offering is created or updated
    event LoyaltyOfferingUpdated(
        address indexed gasStation,
        uint256 discountPercentage,
        string freebie,
        bool isActive
    );

    // Event to log when a customer redeems a loyalty offering
    event LoyaltyRedeemed(
        address indexed gasStation,
        address indexed customer,
        uint256 crudoSpent
    );

    /**
     * @dev Constructor initializes CRUDO token address.
     * @param crudoTokenAddress The address of the CRUDO token contract.
     */
    constructor(address crudoTokenAddress) {
        require(crudoTokenAddress != address(0), "Invalid CRUDO token address");
        crudoToken = IERC20(crudoTokenAddress);
    }

    /**
     * @dev Allows a gas station to create or update its loyalty offering.
     * @param discountPercentage The discount percentage (0-100).
     * @param freebie The freebie description (if any).
     */
    function setLoyaltyOffering(
        uint256 discountPercentage,
        string memory freebie
    ) external {
        require(
            discountPercentage <= 100,
            "Discount percentage cannot exceed 100"
        );

        // Update the loyalty offering
        loyaltyOfferings[msg.sender] = LoyaltyOffering({
            discountPercentage: discountPercentage,
            freebie: freebie,
            isActive: true
        });

        emit LoyaltyOfferingUpdated(
            msg.sender,
            discountPercentage,
            freebie,
            true
        );
    }

    /**
     * @dev Allows a gas station to deactivate its loyalty offering.
     */
    function deactivateLoyaltyOffering() external {
        require(
            loyaltyOfferings[msg.sender].isActive,
            "Loyalty offering is already inactive"
        );

        // Deactivate the loyalty offering
        loyaltyOfferings[msg.sender].isActive = false;

        emit LoyaltyOfferingUpdated(
            msg.sender,
            loyaltyOfferings[msg.sender].discountPercentage,
            loyaltyOfferings[msg.sender].freebie,
            false
        );
    }

    /**
     * @dev Allows a customer to redeem a loyalty offering at a gas station.
     * @param gasStation The address of the gas station.
     * @param crudoAmount The amount of CRUDO tokens to spend.
     */
    function redeemLoyalty(address gasStation, uint256 crudoAmount) external {
        LoyaltyOffering memory offering = loyaltyOfferings[gasStation];

        require(offering.isActive, "Loyalty offering is not active");
        require(
            crudoToken.balanceOf(msg.sender) >= crudoAmount,
            "Insufficient CRUDO token balance"
        );

        // Transfer CRUDO tokens from customer to gas station
        require(
            crudoToken.transferFrom(msg.sender, gasStation, crudoAmount),
            "Failed to transfer CRUDO tokens"
        );

        emit LoyaltyRedeemed(gasStation, msg.sender, crudoAmount);
    }

    /**
     * @dev Fetches the loyalty offering of a specific gas station.
     * @param gasStation The address of the gas station.
     * @return LoyaltyOffering details for the gas station.
     */
    function getLoyaltyOffering(
        address gasStation
    ) external view returns (LoyaltyOffering memory) {
        return loyaltyOfferings[gasStation];
    }
}
```
