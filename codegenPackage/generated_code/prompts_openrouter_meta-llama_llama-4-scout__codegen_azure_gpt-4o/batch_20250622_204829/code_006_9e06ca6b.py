"""
Generated Code Metadata:
========================
Original URL: https://ethhix.com
Prompt: "Create an example of a pledge system on Ethereum using Truffle Suite."
Generated: DETERMINISTIC_9e06ca6b9e01cc51
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PledgeSystem
 * @dev A simple smart contract for managing pledges on Ethereum.
 */
contract PledgeSystem {
    // Struct to represent a pledge
    struct Pledge {
        address pledger; // Address of the pledger
        uint256 amount;  // Amount pledged
        uint256 timestamp; // Time of the pledge
    }

    // Array to store all pledges
    Pledge[] public pledges;

    // Event emitted when a new pledge is made
    event PledgeMade(address indexed pledger, uint256 amount, uint256 timestamp);

    /**
     * @dev Allows a user to make a pledge by sending Ether.
     */
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Create a new pledge and add it to the array
        Pledge memory newPledge = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp
        });
        pledges.push(newPledge);

        // Emit the PledgeMade event
        emit PledgeMade(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Returns the total number of pledges.
     * @return The total number of pledges.
     */
    function getPledgeCount() external view returns (uint256) {
        return pledges.length;
    }

    /**
     * @dev Returns the details of a specific pledge.
     * @param index The index of the pledge in the array.
     * @return The pledger's address, amount pledged, and timestamp of the pledge.
     */
    function getPledge(uint256 index) external view returns (address, uint256, uint256) {
        require(index < pledges.length, "Invalid pledge index");
        Pledge memory pledge = pledges[index];
        return (pledge.pledger, pledge.amount, pledge.timestamp);
    }

    /**
     * @dev Allows the contract owner to withdraw all funds.
     */
    function withdrawFunds() external {
        require(address(this).balance > 0, "No funds available for withdrawal");
        payable(msg.sender).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to handle Ether transfers.
     */
    receive() external payable {
        revert("Use makePledge() to send Ether");
    }
}
```

### Truffle Configuration and Deployment Script

**`truffle-config.js`**
```javascript
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1", // Localhost
      port: 7545,        // Ganache default port
      network_id: "*"    // Match any network id
    }
  },
  compilers: {
    solc: {
      version: "0.8.0" // Specify Solidity compiler version
    }
  }
};
```

**`migrations/2_deploy_pledge_system.js`**
```javascript
const PledgeSystem = artifacts.require("PledgeSystem");

module.exports = function (deployer) {
  deployer.deploy(PledgeSystem);
};
```

### Notes:
- Install Truffle Suite (`npm install -g truffle`) and Ganache for local testing.
- Run `truffle migrate` to deploy the contract to your local blockchain.
- Use `truffle console` or a frontend to interact with the contract.
