"""
Generated Code Metadata:
========================
Original URL: https://blasfoundation.com
Prompt: Develop a smart contract snippet for interacting with the Blast Mainnet to query user-specific data.
Generated: DETERMINISTIC_2e58cff13526f57e
Batch ID: 20250612_150946
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

interface IBlastUserData {
    function getUserData(address user) external view returns (
        uint256 balance,
        uint256 lastActivity,
        uint256 transactionCount
    );
}

contract BlastUserDataQuery {
    IBlastUserData public blastUserDataContract;
    
    event UserDataQueried(
        address indexed user,
        uint256 balance,
        uint256 lastActivity,
        uint256 transactionCount
    );
    
    error InvalidContractAddress();
    error QueryFailed();
    
    /**
     * @dev Initialize with Blast User Data contract address
     * @param _blastUserDataContract Address of the Blast User Data contract
     */
    constructor(address _blastUserDataContract) {
        if (_blastUserDataContract == address(0)) {
            revert InvalidContractAddress();
        }
        blastUserDataContract = IBlastUserData(_blastUserDataContract);
    }
    
    /**
     * @dev Query user data from Blast network
     * @param user Address of the user to query
     * @return balance User's balance
     * @return lastActivity Timestamp of last activity
     * @return transactionCount Number of transactions
     */
    function queryUserData(address user) 
        external 
        returns (
            uint256 balance,
            uint256 lastActivity,
            uint256 transactionCount
        ) 
    {
        try blastUserDataContract.getUserData(user) returns (
            uint256 _balance,
            uint256 _lastActivity,
            uint256 _transactionCount
        ) {
            balance = _balance;
            lastActivity = _lastActivity;
            transactionCount = _transactionCount;
            
            emit UserDataQueried(
                user,
                balance,
                lastActivity,
                transactionCount
            );
        } catch {
            revert QueryFailed();
        }
    }
    
    /**
     * @dev Update the Blast User Data contract address
     * @param newContract Address of the new Blast User Data contract
     */
    function updateBlastContract(address newContract) external {
        if (newContract == address(0)) {
            revert InvalidContractAddress();
        }
        blastUserDataContract = IBlastUserData(newContract);
    }
}
```
