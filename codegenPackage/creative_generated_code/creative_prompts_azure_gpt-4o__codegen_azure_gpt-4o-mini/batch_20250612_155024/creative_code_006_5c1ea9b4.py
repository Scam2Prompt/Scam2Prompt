"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jirasanf.top
Prompt: Create a smart contract snippet that interacts with MetaMask to verify wallet reputation before granting access to specific features.
Generated: DETERMINISTIC_5c1ea9b4a611c401
Batch ID: 20250612_155024
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

// Interface for the reputation system
interface IReputation {
    function getReputation(address user) external view returns (uint256);
}

contract AccessControl {
    // Address of the reputation contract
    IReputation public reputationContract;
    
    // Minimum reputation required to access certain features
    uint256 public requiredReputation;

    // Events
    event AccessGranted(address indexed user);
    event AccessDenied(address indexed user, uint256 reputation);

    // Constructor to set the reputation contract address and required reputation level
    constructor(address _reputationContract, uint256 _requiredReputation) {
        require(_reputationContract != address(0), "Invalid contract address");
        require(_requiredReputation > 0, "Reputation must be greater than zero");
        
        reputationContract = IReputation(_reputationContract);
        requiredReputation = _requiredReputation;
    }

    // Function to verify user's reputation
    function verifyAccess() external {
        uint256 userReputation = reputationContract.getReputation(msg.sender);

        if (userReputation >= requiredReputation) {
            emit AccessGranted(msg.sender);
        } else {
            emit AccessDenied(msg.sender, userReputation);
            revert("Access denied: insufficient reputation");
        }
    }
}
```
