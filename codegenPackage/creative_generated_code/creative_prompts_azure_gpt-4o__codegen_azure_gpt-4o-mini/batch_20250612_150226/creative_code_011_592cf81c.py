"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Create a smart contract that uses Chainlink's Automation for event-based triggers in an insurance use case.
Generated: DETERMINISTIC_592cf81c70f3530b
Batch ID: 20250612_150226
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

// Importing required Chainlink contracts for automation
import "@chainlink/contracts/src/v0.8/AutomationCompatible.sol";

contract InsurancePolicy is AutomationCompatibleInterface {
    // Enum to represent the state of the insurance policy
    enum PolicyState { Active, ClaimRequested, ClaimSettled, Expired }

    // Struct to define an Insurance Policy
    struct Policy {
        address policyHolder;
        uint256 premiumAmount;
        uint256 coverageAmount;
        uint256 expirationTime;
        PolicyState state;
    }

    // Mapping to store policies by their unique ID
    mapping(uint256 => Policy) public policies;
    uint256 public policyCounter;

    // Events for logging actions
    event PolicyCreated(uint256 policyId, address indexed policyHolder, uint256 premiumAmount, uint256 coverageAmount, uint256 expirationTime);
    event ClaimRequested(uint256 policyId);
    event ClaimSettled(uint256 policyId);
    event PolicyExpired(uint256 policyId);

    // Constructor to initialize state variables
    constructor() {
        policyCounter = 0;
    }

    // Function to create a new insurance policy
    function createPolicy(uint256 _premiumAmount, uint256 _coverageAmount, uint256 _durationInDays) external payable {
        require(msg.value == _premiumAmount, "Incorrect premium amount sent");

        uint256 expirationTime = block.timestamp + (_durationInDays * 1 days);
        policies[policyCounter] = Policy({
            policyHolder: msg.sender,
            premiumAmount: _premiumAmount,
            coverageAmount: _coverageAmount,
            expirationTime: expirationTime,
            state: PolicyState.Active
        });

        emit PolicyCreated(policyCounter, msg.sender, _premiumAmount, _coverageAmount, expirationTime);
        policyCounter++;
    }

    // Function for policyholder to request a claim
    function requestClaim(uint256 _policyId) external {
        Policy storage policy = policies[_policyId];
        require(msg.sender == policy.policyHolder, "Only the policyholder can request a claim");
        require(policy.state == PolicyState.Active, "Policy is not active");
        
        policy.state = PolicyState.ClaimRequested;
        emit ClaimRequested(_policyId);
    }

    // Function to settle the claim
    function settleClaim(uint256 _policyId) external {
        Policy storage policy = policies[_policyId];
        require(policy.state == PolicyState.ClaimRequested, "Claim is not requested");
        
        policy.state = PolicyState.ClaimSettled;
        payable(policy.policyHolder).transfer(policy.coverageAmount);
        emit ClaimSettled(_policyId);
    }

    // Check if the policy has expired
    function checkExpired(uint256 _policyId) external view returns (bool) {
        Policy storage policy = policies[_policyId];
        return (block.timestamp >= policy.expirationTime && policy.state == PolicyState.Active);
    }

    // Chainlink automation function to check and execute expired policies
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory) {
        // Check if any policy has expired
        for (uint256 i = 0; i < policyCounter; i++) {
            if (checkExpired(i)) {
                return (true, abi.encode(i));
            }
        }
        return (false, bytes(""));
    }

    // Perform the upkeep for expired policies
    function performUpkeep(bytes calldata performData) external override {
        uint256 policyId = abi.decode(performData, (uint256));
        Policy storage policy = policies[policyId];

        require(policy.state == PolicyState.Active, "Policy is not active");
        
        policy.state = PolicyState.Expired;
        emit PolicyExpired(policyId);
    }
}
```
