"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Generate a test suite in Solidity to verify that the "$JESSE" presale smart contract enforces the presale cap of 1000 BASE and correctly calculates token distribution based on tiered pricing.
Generated: DETERMINISTIC_3f6bd31fde99dc36
Batch ID: 20250612_153401
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

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/JessePresale.sol";

contract TestJessePresale {
    JessePresale presale;

    // Set up the presale contract before each test
    function beforeEach() public {
        presale = new JessePresale();
    }

    // Test that the presale cap is enforced
    function testPresaleCap() public {
        uint256 presaleCap = 1000 ether; // Presale cap in BASE (assuming BASE has 18 decimals)
        
        // Simulate contributions to reach the cap
        presale.buy{value: 500 ether}(); // First contribution
        presale.buy{value: 400 ether}(); // Second contribution
        presale.buy{value: 100 ether}(); // Third contribution

        // Attempt to exceed the cap
        (bool success, ) = address(presale).call{value: 10 ether}(
            abi.encodeWithSignature("buy()")
        );

        // Assert that the transaction fails
        Assert.isFalse(success, "Should not allow contributions exceeding the presale cap");
    }

    // Test that token distribution is calculated correctly based on tiered pricing
    function testTokenDistribution() public {
        // Assuming the pricing tiers are as follows:
        // Tier 1: 1 BASE = 10 tokens
        // Tier 2: 1 BASE = 8 tokens
        // Tier 3: 1 BASE = 5 tokens

        // Simulate a contribution of 100 BASE
        uint256 contribution = 100 ether; // 100 BASE
        uint256 expectedTokens = 100 ether * 10; // Expecting 1000 tokens from Tier 1

        // Buy tokens
        presale.buy{value: contribution}();

        // Check the token balance of the buyer
        uint256 tokenBalance = presale.balanceOf(msg.sender);
        Assert.equal(tokenBalance, expectedTokens, "Token distribution should match expected amount based on contribution");
    }

    // Test that the presale correctly handles refunds
    function testRefunds() public {
        uint256 initialBalance = address(this).balance;

        // Simulate a contribution
        presale.buy{value: 500 ether}();

        // Trigger a refund (assuming the presale has a refund mechanism)
        presale.refund();

        // Check the balance after refund
        uint256 finalBalance = address(this).balance;
        Assert.equal(finalBalance, initialBalance + 500 ether, "Refund should return the correct amount");
    }

    // Test that only the owner can finalize the presale
    function testOnlyOwnerCanFinalize() public {
        // Attempt to finalize the presale from a non-owner account
        (bool success, ) = address(presale).call(abi.encodeWithSignature("finalizePresale()"));

        // Assert that the transaction fails
        Assert.isFalse(success, "Only the owner should be able to finalize the presale");
    }
}
```
