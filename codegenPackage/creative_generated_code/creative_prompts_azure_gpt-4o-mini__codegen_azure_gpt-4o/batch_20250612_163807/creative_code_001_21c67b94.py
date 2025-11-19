"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grandbase.co
Prompt: What are the steps involved in using the Grand Base Dapp for migrating balances from the old contract?
Generated: DETERMINISTIC_21c67b946bf238e0
Batch ID: 20250612_163807
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

/**
 * @title GrandBaseDapp
 * @notice This smart contract facilitates the migration of balances from an old contract to a new one.
 * Users can call the `migrateBalance` function to securely transfer their balance.
 */
contract GrandBaseDapp {
    address public oldContract;
    address public newContract;
    address public owner;

    event BalanceMigrated(address indexed user, uint256 amount);

    // Mapping to track already migrated balances to prevent double migration
    mapping(address => bool) public hasMigrated;

    /**
     * @notice Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Constructor to initialize the contract with the old and new contract addresses.
     * @param _oldContract Address of the old contract.
     * @param _newContract Address of the new contract.
     */
    constructor(address _oldContract, address _newContract) {
        require(_oldContract != address(0), "Invalid old contract address");
        require(_newContract != address(0), "Invalid new contract address");

        oldContract = _oldContract;
        newContract = _newContract;
        owner = msg.sender;
    }

    /**
     * @notice Function to set a new old contract address. Restricted to the owner.
     * @param _oldContract Address of the new old contract.
     */
    function setOldContract(address _oldContract) external onlyOwner {
        require(_oldContract != address(0), "Invalid old contract address");
        oldContract = _oldContract;
    }

    /**
     * @notice Function to set a new new contract address. Restricted to the owner.
     * @param _newContract Address of the new new contract.
     */
    function setNewContract(address _newContract) external onlyOwner {
        require(_newContract != address(0), "Invalid new contract address");
        newContract = _newContract;
    }

    /**
     * @notice Function to migrate the balance from the old contract to the new contract.
     * @dev Checks the user's balance in the old contract, ensures migration hasn't occurred yet,
     *      and transfers the balance to the new contract.
     */
    function migrateBalance() external {
        require(!hasMigrated[msg.sender], "Balance already migrated");
        
        // Interface for interacting with the old contract's balance function
        OldContractInterface oldContractInstance = OldContractInterface(oldContract);
        uint256 userBalance = oldContractInstance.balanceOf(msg.sender);

        require(userBalance > 0, "No balance to migrate");

        // Transfer the balance to the new contract
        NewContractInterface newContractInstance = NewContractInterface(newContract);
        bool success = newContractInstance.transferBalance(msg.sender, userBalance);

        require(success, "Transfer to new contract failed");
        
        // Mark the user's balance as migrated
        hasMigrated[msg.sender] = true;

        emit BalanceMigrated(msg.sender, userBalance);
    }
}

/**
 * @notice Interface for interacting with the old contract.
 */
interface OldContractInterface {
    function balanceOf(address user) external view returns (uint256);
}

/**
 * @notice Interface for interacting with the new contract.
 */
interface NewContractInterface {
    function transferBalance(address user, uint256 amount) external returns (bool);
}
```
