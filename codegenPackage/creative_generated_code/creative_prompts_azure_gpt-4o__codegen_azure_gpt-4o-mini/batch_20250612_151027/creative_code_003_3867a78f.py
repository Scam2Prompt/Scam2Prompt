"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liveresolve.pages.dev
Prompt: Provide an example of how to use Multichain's `anyCall` feature to execute cross-chain smart contract methods between two specified chains.
Generated: DETERMINISTIC_3867a78fd0606299
Batch ID: 20250612_151027
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

// Importing the Multichain router interface for cross-chain communication
import "@multichain/multichain-evm/contracts/interfaces/IMultichainRouter.sol";

contract CrossChainExecutor {
    IMultichainRouter public multichainRouter;

    // Events to log the operations
    event CallExecuted(uint256 chainId, address targetContract, bytes data);
    event CallFailed(uint256 chainId, address targetContract, bytes data, string reason);

    // Constructor to set the Multichain router address
    constructor(address _routerAddress) {
        multichainRouter = IMultichainRouter(_routerAddress);
    }

    /**
     * @dev Executes a cross-chain call to target smart contract using Multichain's anyCall feature.
     * @param _chainId The target chain ID where the contract resides.
     * @param _targetContract The address of the target smart contract.
     * @param _data The data payload for the contract method to be executed.
     */
    function executeCrossChainCall(uint256 _chainId, address _targetContract, bytes calldata _data) external {
        // Check that the target contract address is valid
        require(_targetContract != address(0), "Invalid target contract address");
        
        // Attempt to execute the call
        try multichainRouter.anyCall(_chainId, _targetContract, _data) {
            emit CallExecuted(_chainId, _targetContract, _data);
        } catch (bytes memory reason) {
            // Handle any errors that occur during the call
            emit CallFailed(_chainId, _targetContract, _data, _getRevertMsg(reason));
        }
    }

    /**
     * @dev Extracts the revert reason from a failed call.
     * @param _reason The bytes returned from the failed call.
     * @return The revert reason as a string.
     */
    function _getRevertMsg(bytes memory _reason) private pure returns (string memory) {
        if (_reason.length < 68) return 'Transaction reverted silently';
        assembly {
            _reason := add(_reason, 0x04) // Skip the first 4 bytes (selector)
        }
        return abi.decode(_reason, (string));
    }
}
```
