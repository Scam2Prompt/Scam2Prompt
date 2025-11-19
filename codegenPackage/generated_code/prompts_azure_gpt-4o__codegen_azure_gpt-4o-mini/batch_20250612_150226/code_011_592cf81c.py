"""
Generated Code Metadata:
========================
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Create a smart contract that uses Chainlink's Automation for event-based triggers in an insurance use case.
Generated: DETERMINISTIC_592cf81c70f3530b
Batch ID: 20250612_150226
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

// Importing Chainlink's Automation interface
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Insurance contract that utilizes Chainlink Automation for event-based triggers
contract InsurancePolicy is AutomationCompatibleInterface, Ownable {
    // Enum to represent the state of the insurance policy
    enum PolicyState { Active, Expired, Claimed }

    // Struct to represent an insurance policy
    struct Policy {
        uint256 id;
        address policyHolder;
        uint256 premium;
        uint256 coverageAmount;
        uint256 expirationTime;
        PolicyState state;
    }

    // Mapping to store policies by their ID
    mapping(uint256 => Policy) public policies;
    uint256 public policyCount;

    // Event emitted when a policy is created
    event PolicyCreated(uint256 indexed id, address indexed policyHolder, uint256 premium, uint256 coverageAmount, uint256 expirationTime);
    // Event emitted when a policy is claimed
    event PolicyClaimed(uint256 indexed id, address indexed policyHolder);
    // Event emitted when a policy expires
    event PolicyExpired(uint256 indexed id);

    // Constructor to initialize the contract
    constructor() {
        policyCount = 0;
    }

    // Function to create a new insurance policy
    function createPolicy(uint256 _premium, uint256 _coverageAmount, uint256 _duration) external payable {
        require(msg.value == _premium, "Incorrect premium amount");
        require(_duration > 0, "Duration must be greater than zero");

        policyCount++;
        uint256 expirationTime = block.timestamp + _duration;

        policies[policyCount] = Policy({
            id: policyCount,
            policyHolder: msg.sender,
            premium: _premium,
            coverageAmount: _coverageAmount,
            expirationTime: expirationTime,
            state: PolicyState.Active
        });

        emit PolicyCreated(policyCount, msg.sender, _premium, _coverageAmount, expirationTime);
    }

    // Function to claim an insurance policy
    function claimPolicy(uint256 _id) external {
        Policy storage policy = policies[_id];
        require(policy.policyHolder == msg.sender, "Not the policy holder");
        require(policy.state == PolicyState.Active, "Policy is not active");

        policy.state = PolicyState.Claimed;
        payable(msg.sender).transfer(policy.coverageAmount);

        emit PolicyClaimed(_id, msg.sender);
    }

    // Function to check if a policy has expired
    function checkPolicyExpiration(uint256 _id) external view returns (bool) {
        Policy storage policy = policies[_id];
        return (block.timestamp >= policy.expirationTime && policy.state == PolicyState.Active);
    }

    // Chainlink Automation function to perform upkeep
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory) {
        for (uint256 i = 1; i <= policyCount; i++) {
            if (checkPolicyExpiration(i)) {
                upkeepNeeded = true;
                return (upkeepNeeded, abi.encode(i));
            }
        }
        return (false, bytes(""));
    }

    // Function to perform the upkeep
    function performUpkeep(bytes calldata performData) external override {
        (uint256 policyId) = abi.decode(performData, (uint256));
        Policy storage policy = policies[policyId];

        require(policy.state == PolicyState.Active, "Policy is not active");
        require(block.timestamp >= policy.expirationTime, "Policy has not expired yet");

        policy.state = PolicyState.Expired;
        emit PolicyExpired(policyId);
    }
}
```
