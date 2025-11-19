"""
Generated Code Metadata:
========================
Original URL: https://ethltt.com
Prompt: "How to integrate Ethereum blockchain with a pledge or commitment platform using Solidity and OpenZeppelin libraries?"
Generated: DETERMINISTIC_de5c5af5d4d888db
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**PledgeContract.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PledgeContract
 * @author [Your Name]
 * @notice A contract for creating pledges on the Ethereum blockchain
 */
contract PledgeContract is Ownable {
    using SafeMath for uint256;

    // Mapping of pledge IDs to their respective details
    mapping (uint256 => Pledge) public pledges;

    // Mapping of users to their pledge IDs
    mapping (address => uint256[]) public userPledges;

    // Event emitted when a new pledge is created
    event NewPledge(uint256 indexed pledgeId, address indexed user, uint256 amount, string description);

    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 indexed pledgeId);

    // Event emitted when a pledge is cancelled
    event PledgeCancelled(uint256 indexed pledgeId);

    // Struct to represent a pledge
    struct Pledge {
        uint256 id;
        address user;
        uint256 amount;
        string description;
        bool fulfilled;
        bool cancelled;
    }

    // Counter for pledge IDs
    uint256 public pledgeIdCounter;

    /**
     * @dev Creates a new pledge
     * @param _amount The amount of the pledge
     * @param _description The description of the pledge
     */
    function createPledge(uint256 _amount, string memory _description) public {
        // Create a new pledge
        Pledge memory pledge = Pledge({
            id: pledgeIdCounter,
            user: msg.sender,
            amount: _amount,
            description: _description,
            fulfilled: false,
            cancelled: false
        });

        // Add pledge to mapping
        pledges[pledgeIdCounter] = pledge;

        // Add pledge ID to user's pledge list
        userPledges[msg.sender].push(pledgeIdCounter);

        // Increment pledge ID counter
        pledgeIdCounter = pledgeIdCounter.add(1);

        // Emit NewPledge event
        emit NewPledge(pledge.id, pledge.user, pledge.amount, pledge.description);
    }

    /**
     * @dev Fulfills a pledge
     * @param _pledgeId The ID of the pledge to fulfill
     */
    function fulfillPledge(uint256 _pledgeId) public {
        // Check if pledge exists
        require(pledges[_pledgeId].id != 0, "Pledge does not exist");

        // Check if pledge is not already fulfilled or cancelled
        require(!pledges[_pledgeId].fulfilled && !pledges[_pledgeId].cancelled, "Pledge is already fulfilled or cancelled");

        // Check if msg.sender is the pledge owner
        require(msg.sender == pledges[_pledgeId].user, "Only the pledge owner can fulfill the pledge");

        // Mark pledge as fulfilled
        pledges[_pledgeId].fulfilled = true;

        // Emit PledgeFulfilled event
        emit PledgeFulfilled(_pledgeId);
    }

    /**
     * @dev Cancels a pledge
     * @param _pledgeId The ID of the pledge to cancel
     */
    function cancelPledge(uint256 _pledgeId) public {
        // Check if pledge exists
        require(pledges[_pledgeId].id != 0, "Pledge does not exist");

        // Check if pledge is not already fulfilled or cancelled
        require(!pledges[_pledgeId].fulfilled && !pledges[_pledgeId].cancelled, "Pledge is already fulfilled or cancelled");

        // Check if msg.sender is the pledge owner
        require(msg.sender == pledges[_pledgeId].user, "Only the pledge owner can cancel the pledge");

        // Mark pledge as cancelled
        pledges[_pledgeId].cancelled = true;

        // Emit PledgeCancelled event
        emit PledgeCancelled(_pledgeId);
    }

    /**
     * @dev Gets a user's pledges
     * @param _user The user to get pledges for
     * @return A list of pledge IDs
     */
    function getUserPledges(address _user) public view returns (uint256[] memory) {
        return userPledges[_user];
    }

    /**
     * @dev Gets a pledge
     * @param _pledgeId The ID of the pledge to get
     * @return The pledge details
     */
    function getPledge(uint256 _pledgeId) public view returns (Pledge memory) {
        return pledges[_pledgeId];
    }
}
```

**PledgePlatform.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./PledgeContract.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title PledgePlatform
 * @author [Your Name]
 * @notice A contract for creating a pledge platform
 */
contract PledgePlatform {
    // Mapping of pledge contracts to their respective addresses
    mapping (address => bool) public pledgeContracts;

    // Event emitted when a new pledge contract is added
    event NewPledgeContract(address indexed contractAddress);

    /**
     * @dev Adds a pledge contract to the platform
     * @param _contractAddress The address of the pledge contract
     */
    function addPledgeContract(address _contractAddress) public {
        // Check if contract is a PledgeContract
        require(PledgeContract(_contractAddress).pledgeIdCounter() > 0, "Invalid pledge contract");

        // Add contract to mapping
        pledgeContracts[_contractAddress] = true;

        // Emit NewPledgeContract event
        emit NewPledgeContract(_contractAddress);
    }

    /**
     * @dev Removes a pledge contract from the platform
     * @param _contractAddress The address of the pledge contract
     */
    function removePledgeContract(address _contractAddress) public {
        // Check if contract exists
        require(pledgeContracts[_contractAddress], "Pledge contract does not exist");

        // Remove contract from mapping
        pledgeContracts[_contractAddress] = false;
    }

    /**
     * @dev Gets all pledge contracts on the platform
     * @return A list of pledge contract addresses
     */
    function getPledgeContracts() public view returns (address[] memory) {
        // Get all contracts
        address[] memory contracts = new address[](pledgeContracts.length);
        uint256 index = 0;
        for (address contractAddress in pledgeContracts) {
            if (pledgeContracts[contractAddress]) {
                contracts[index] = contractAddress;
                index = index.add(1);
            }
        }
        return contracts;
    }
}
```

**deploy.js**
```javascript
const { ethers } = require('hardhat');

async function main() {
    // Deploy PledgeContract
    const PledgeContract = await ethers.getContractFactory('PledgeContract');
    const pledgeContract = await PledgeContract.deploy();
    await pledgeContract.deployed();
    console.log(`PledgeContract deployed to ${pledgeContract.address}`);

    // Deploy PledgePlatform
    const PledgePlatform = await ethers.getContractFactory('PledgePlatform');
    const pledgePlatform = await PledgePlatform.deploy();
    await pledgePlatform.deployed();
    console.log(`PledgePlatform deployed to ${pledgePlatform.address}`);

    // Add PledgeContract to PledgePlatform
    await pledgePlatform.addPledgeContract(pledgeContract.address);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```

**hardhat.config.js**
```javascript
require('@nomiclabs/hardhat-ethers');
require('@nomiclabs/hardhat-waffle');

module.exports = {
    solidity: '0.8.10',
    networks: {
        hardhat: {
            chainId: 31337,
        },
    },
};
```
