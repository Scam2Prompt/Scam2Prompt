"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrett-live.pages.dev
Prompt: Generate a script in Solidity to query the BRETT token's treasury allocation (10%) and display the results on a dApp interface.
Generated: DETERMINISTIC_b30818ec9411ee04
Batch ID: 20250612_152235
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

// Importing the ERC20 interface to interact with the BRETT token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// This contract queries the BRETT token's treasury allocation
contract TreasuryAllocator {
    // The address of the BRETT token contract
    address public constant BRETT_TOKEN_ADDRESS = 0xYourBrettTokenAddressHere;
    
    // Treasury allocation percentage (10%)
    uint256 public constant TREASURY_ALLOCATION_PERCENTAGE = 10;

    // Event to emit the treasury allocation amount
    event TreasuryAllocation(uint256 allocationAmount);

    // Function to get the total supply of the BRETT token
    function getTotalSupply() external view returns (uint256) {
        IERC20 brettToken = IERC20(BRETT_TOKEN_ADDRESS);
        return brettToken.totalSupply();
    }

    // Function to calculate and return the treasury allocation
    function getTreasuryAllocation() external returns (uint256) {
        IERC20 brettToken = IERC20(BRETT_TOKEN_ADDRESS);
        
        // Fetching the total supply of the BRETT token
        uint256 totalSupply = brettToken.totalSupply();

        // Calculate treasury allocation based on 10% of the total supply
        uint256 treasuryAllocation = (totalSupply * TREASURY_ALLOCATION_PERCENTAGE) / 100;

        // Emit the treasury allocation amount
        emit TreasuryAllocation(treasuryAllocation);

        // Return the treasury allocation amount
        return treasuryAllocation;
    }
}
```

### Frontend dApp Interface (JavaScript Example)

```javascript
// Assuming you're using web3.js or ethers.js to interact with Ethereum blockchain
const Web3 = require('web3');
const contractABI = [/* ABI of TreasuryAllocator Contract */];
const contractAddress = '0xYourTreasuryAllocatorContractAddressHere';

async function getTreasuryAllocation() {
    const web3 = new Web3(window.ethereum); // Initialize Web3 instance
    await window.ethereum.enable(); // Request account access

    const treasuryAllocator = new web3.eth.Contract(contractABI, contractAddress);

    try {
        // Calling the getTreasuryAllocation function from the smart contract
        const allocation = await treasuryAllocator.methods.getTreasuryAllocation().call();
        console.log(`Treasury Allocation (10%): ${allocation}`);
        document.getElementById('allocationDisplay').innerText = `Treasury Allocation: ${allocation}`;
    } catch (error) {
        console.error("Error fetching treasury allocation:", error);
        document.getElementById('allocationDisplay').innerText = "Error fetching allocation";
    }
}

// Call the function when the dApp is loaded
window.onload = getTreasuryAllocation;
```

### Additional Notes:
- Replace `0xYourBrettTokenAddressHere` and `0xYourTreasuryAllocatorContractAddressHere` with the actual contract addresses.
- The ABI of the `TreasuryAllocator` contract needs to be provided in the JavaScript code.
- Make sure to include proper error handling and user notifications for better user experience in a production environment.
