"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Generate Solidity code to query GMX oracle data from a smart contract deployed on the Arbitrum network.
Generated: DETERMINISTIC_520d146825e96b48
Batch ID: 20250612_145616
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
 * @title GMX Oracle Data Query Contract
 * @dev This contract queries GMX oracle data from a GMX-compatible contract deployed on the Arbitrum network.
 */
contract GMXOracleQuery {
    // Address of the GMX oracle contract on Arbitrum
    address public gmxOracleAddress;

    // Event to log oracle data retrieved
    event OracleDataRetrieved(bytes32 indexed key, uint256 value);

    /**
     * @dev Constructor to set the GMX oracle address.
     * @param _gmxOracleAddress Address of the GMX oracle contract.
     */
    constructor(address _gmxOracleAddress) {
        require(_gmxOracleAddress != address(0), "Invalid oracle address");
        gmxOracleAddress = _gmxOracleAddress;
    }

    /**
     * @dev Function to query GMX oracle data by key.
     * @param _key The key to query oracle data (e.g., asset price key).
     * @return The value associated with the queried key.
     * 
     * Notes:
     * - Assumes the GMX oracle contract exposes a `getOracleData(bytes32 key)` function.
     */
    function queryOracleData(bytes32 _key) external view returns (uint256) {
        // Ensure the key is valid (non-zero)
        require(_key != bytes32(0), "Invalid key");

        // Interface for GMX oracle contract
        (bool success, bytes memory data) = gmxOracleAddress.staticcall(
            abi.encodeWithSignature("getOracleData(bytes32)", _key)
        );

        // Validate the static call
        require(success, "Oracle query failed");

        // Parse the returned data
        uint256 value = abi.decode(data, (uint256));

        // Emit an event for transparency
        emit OracleDataRetrieved(_key, value);

        return value;
    }

    /**
     * @dev Function to update the GMX oracle address (admin-only).
     * @param _newOracleAddress New oracle address.
     */
    function updateOracleAddress(address _newOracleAddress) external {
        // Require admin privileges (this example assumes the contract owner is the admin)
        // Replace `requireAdmin()` with your access control implementation
        requireAdmin();

        // Update the oracle address
        require(_newOracleAddress != address(0), "Invalid oracle address");
        gmxOracleAddress = _newOracleAddress;
    }

    /**
     * @dev Placeholder function to enforce admin access.
     * Implement your own access control logic.
     */
    function requireAdmin() internal view {
        // Example: Replace with actual admin check (e.g., Ownable modifier)
        require(msg.sender == address(0xYourAdminAddress), "Unauthorized");
    }
}
```

**Note:** Replace `address(0xYourAdminAddress)` with the actual address of the contract administrator when using the `requireAdmin` function. Additionally, ensure the GMX oracle contract adheres to the specified interface (`getOracleData(bytes32)`) for this implementation to work correctly.
