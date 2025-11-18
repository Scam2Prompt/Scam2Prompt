"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Generate a test suite in Solidity to verify that the "$JESSE" presale smart contract enforces the presale cap of 1000 BASE and correctly calculates token distribution based on tiered pricing.
Generated: DETERMINISTIC_3f6bd31fde99dc36
Batch ID: 20250612_153401
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

// Import the testing framework (e.g., Hardhat or Truffle's testing libraries)
import "forge-std/Test.sol";
import "./JESSEPresale.sol"; // Assuming the "$JESSE" presale contract exists in the same directory

contract JESSEPresaleTest is Test {
    // Instance of the presale contract
    JESSEPresale presale;

    // Mock addresses for test participants
    address mockBuyer1 = address(0x123);
    address mockBuyer2 = address(0x456);

    // Set up the presale cap and tiered pricing
    uint256 constant PRESALE_CAP = 1000 ether; // 1000 BASE
    uint256 constant TIER1_PRICE = 1 ether;    // Price for the first tier
    uint256 constant TIER2_PRICE = 0.8 ether;  // Price for the second tier
    uint256 constant TIER3_PRICE = 0.5 ether;  // Price for the third tier

    // Predefined token allocations for tiers
    uint256 constant TIER1_AMOUNT = 500 ether; // First tier allocation
    uint256 constant TIER2_AMOUNT = 300 ether; // Second tier allocation
    uint256 constant TIER3_AMOUNT = 200 ether; // Third tier allocation

    // Initialize the presale contract before each test
    function setUp() public {
        presale = new JESSEPresale(PRESALE_CAP, TIER1_PRICE, TIER2_PRICE, TIER3_PRICE);
    }

    // Test that the presale enforces the cap
    function testPresaleCapEnforcement() public {
        // Simulate purchases that exceed the cap
        vm.startPrank(mockBuyer1);
        presale.buyTokens{value: 999 ether}(); // Buyer 1 buys close to the cap
        vm.stopPrank();

        // Attempt to exceed the cap
        vm.startPrank(mockBuyer2);
        vm.expectRevert("Presale cap exceeded");
        presale.buyTokens{value: 2 ether}(); // Exceeds cap
        vm.stopPrank();

        // Check total amount sold
        assertEq(presale.totalBaseRaised(), 999 ether);
    }

    // Test tier-based pricing and token distribution
    function testTieredPricingAndDistribution() public {
        // Buyer 1 purchases from Tier 1
        vm.startPrank(mockBuyer1);
        presale.buyTokens{value: TIER1_PRICE}(); // Buyer 1 buys 1 BASE worth of tokens
        vm.stopPrank();

        // Verify Tier 1 allocation
        uint256 buyer1Tokens = presale.balanceOf(mockBuyer1);
        assertEq(buyer1Tokens, TIER1_PRICE / TIER1_PRICE); // 1 BASE = 1 JESSE token

        // Buyer 2 purchases from Tier 2
        vm.startPrank(mockBuyer2);
        presale.buyTokens{value: TIER2_PRICE}(); // Buyer 2 buys 0.8 BASE worth of tokens
        vm.stopPrank();

        // Verify Tier 2 allocation
        uint256 buyer2Tokens = presale.balanceOf(mockBuyer2);
        assertEq(buyer2Tokens, TIER2_PRICE / TIER2_PRICE); // 0.8 BASE = 1 JESSE token

        // Check total amount raised
        uint256 totalRaised = presale.totalBaseRaised();
        assertEq(totalRaised, TIER1_PRICE + TIER2_PRICE);
    }

    // Test edge case for Tier transitions
    function testTierTransition() public {
        // Simulate purchases that transition between tiers
        vm.startPrank(mockBuyer1);
        presale.buyTokens{value: TIER1_AMOUNT}(); // Buyer 1 buys all Tier 1 allocation
        vm.stopPrank();

        // Buyer 2 purchases starting from Tier 2
        vm.startPrank(mockBuyer2);
        presale.buyTokens{value: TIER2_AMOUNT}();
        vm.stopPrank();

        // Verify Tier 1 and Tier 2 are fully allocated
        uint256 totalRaised = presale.totalBaseRaised();
        assertEq(totalRaised, TIER1_AMOUNT + TIER2_AMOUNT);

        // Verify Tier 3 starts correctly
        vm.startPrank(mockBuyer1);
        presale.buyTokens{value: TIER3_AMOUNT}(); // Buyer 1 buys Tier 3 allocation
        vm.stopPrank();

        // Check final allocation
        totalRaised = presale.totalBaseRaised();
        assertEq(totalRaised, PRESALE_CAP); // Total raised reaches presale cap
    }

    // Test invalid input values
    function testInvalidPurchaseAmount() public {
        vm.startPrank(mockBuyer1);

        // Negative or zero purchase amounts should fail
        vm.expectRevert("Invalid purchase amount");
        presale.buyTokens{value: 0 ether}();

        vm.stopPrank();
    }
}
```
