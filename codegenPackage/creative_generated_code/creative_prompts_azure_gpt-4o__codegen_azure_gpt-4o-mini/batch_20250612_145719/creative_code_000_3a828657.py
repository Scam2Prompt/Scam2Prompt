"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Write a smart contract on Ethereum that integrates with Nexus Mutual's API to automate the purchase of Smart Contract Cover when deploying new decentralized applications.
Generated: DETERMINISTIC_3a828657a2a95f83
Batch ID: 20250612_145719
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

// Importing interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface INexusMutual {
    function buyCover(
        address _app,
        uint256 _coverAmount,
        uint256 _duration,
        string calldata _data
    ) external returns (uint256 coverId);
}

// Smart contract to interact with Nexus Mutual's API for Smart Contract Cover
contract SmartContractCover is Ownable {
    // Nexus Mutual contract address (example address, use the actual deployed address)
    INexusMutual public nexusMutual;

    // Event emitted after purchasing cover
    event CoverPurchased(uint256 coverId, address indexed app, uint256 coverAmount, uint256 duration);

    // Constructor to set the Nexus Mutual contract address
    constructor(address _nexusMutual) {
        require(_nexusMutual != address(0), "Invalid Nexus Mutual address");
        nexusMutual = INexusMutual(_nexusMutual);
    }

    // Function to purchase Smart Contract Cover
    function purchaseCover(
        address _app,
        uint256 _coverAmount,
        uint256 _duration,
        string calldata _data
    ) external onlyOwner returns (uint256) {
        require(_coverAmount > 0, "Cover amount must be greater than 0");
        require(_duration > 0, "Cover duration must be greater than 0");
        
        // Calling buyCover function of Nexus Mutual
        uint256 coverId = nexusMutual.buyCover(_app, _coverAmount, _duration, _data);
        
        // Emitting event for cover purchase
        emit CoverPurchased(coverId, _app, _coverAmount, _duration);
        
        return coverId;
    }
}
```

### Notes:
- Ensure to replace the example `Nexus Mutual` contract address with the actual deployed address before deploying.
- The `buyCover` function within the `INexusMutual` interface should reflect the actual signature from Nexus Mutual's documentation.
- The owner of the contract is responsible for purchasing cover; adjust permissions based on your security model.
- Further customization may be necessary based on the specific requirements or features of the Nexus Mutual API.
