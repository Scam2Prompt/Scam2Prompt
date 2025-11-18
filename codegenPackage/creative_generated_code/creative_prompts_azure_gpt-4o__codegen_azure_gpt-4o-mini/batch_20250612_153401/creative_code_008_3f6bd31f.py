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

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/JESSEPresale.sol";

contract TestJESSEPresale {
    // Instance of the presale contract
    JESSEPresale presale;

    // Setup the presale contract before each test
    function beforeEach() public {
        presale = new JESSEPresale();
    }

    // Test the presale cap enforcement
    function testPresaleCap() public {
        uint256 presaleCap = 1000 ether; // Set presale cap to 1000 BASE
        uint256 initialBalance = presale.totalRaised();

        // Simulate contributions to reach the cap
        presale.contribute{value: 500 ether}();
        presale.contribute{value: 500 ether}();

        // Validate that contributions equal the presale cap
        Assert.equal(presale.totalRaised(), presaleCap, "Total raised should equal presale cap.");

        // Attempt to exceed the cap
        (bool success,) = address(presale).call{value: 1 ether}(abi.encodeWithSignature("contribute()"));
        Assert.isFalse(success, "Contributing beyond the cap should fail.");
    }

    // Test the token distribution based on tiered pricing
    function testTokenDistribution() public {
        // Set pricing tiers (this would normally be part of the contract or set via a function)
        presale.setPricingTiers(0.01 ether, 0.02 ether); // Tiers could be set for example

        // Simulate contribution
        presale.contribute{value: 1 ether}(); // Contributing 1 ether

        // Calculate expected token amount based on tier pricing
        uint256 expectedTokens = 1 ether / 0.01 ether; // 100 tokens for 1 ether at 0.01 ether/tier

        // Validate that the tokens distributed match expectation
        Assert.equal(presale.tokensClaimed(msg.sender), expectedTokens, "Token distribution should match expected amount.");
    }

    // Test that only whitelisted addresses can contribute
    function testWhitelistRestriction() public {
        // Attempting to contribute from a non-whitelisted address
        (bool success,) = address(presale).call{value: 1 ether}(abi.encodeWithSignature("contribute()"));
        Assert.isFalse(success, "Non-whitelisted addresses should not be allowed to contribute.");
    }

    // Test refund capability after presale cap is reached
    function testRefundAfterCapReached() public {
        presale.contribute{value: 1000 ether}(); // Contribute to reach cap
        
        // Attempt to refund
        uint256 initialBalance = address(this).balance;
        presale.refund();

        // Validate that the balance has returned to test account
        Assert.equal(address(this).balance, initialBalance + 1000 ether, "Refund should return total contribution.");
    }
}
```
