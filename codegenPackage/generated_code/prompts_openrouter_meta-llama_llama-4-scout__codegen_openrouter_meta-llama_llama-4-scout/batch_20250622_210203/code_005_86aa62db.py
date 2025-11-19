"""
Generated Code Metadata:
========================
Original URL: https://claimreference.pages.dev
Prompt: Write a Solidity smart contract that utilizes Multichain's anyCall function to interact with a smart contract on a different chain.
Generated: DETERMINISTIC_86aa62db9e096d25
Batch ID: 20250622_210203
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Multichain AnyCall Contract
 * @author [Your Name]
 * @notice This contract utilizes Multichain's anyCall function to interact with a smart contract on a different chain.
 */
contract MultichainAnyCall {
    using SafeMath for uint256;

    // Mapping of target chain IDs to their respective contract addresses
    mapping(uint256 => address) public targetContracts;

    // Mapping of target chain IDs to their respective call data
    mapping(uint256 => bytes) public callData;

    // Event emitted when anyCall is executed
    event AnyCallExecuted(uint256 indexed targetChainId, address indexed targetContract, bytes data);

    /**
     * @dev Sets the target contract address for a specific chain ID
     * @param _chainId The ID of the target chain
     * @param _contractAddress The address of the target contract
     */
    function setTargetContract(uint256 _chainId, address _contractAddress) public {
        targetContracts[_chainId] = _contractAddress;
    }

    /**
     * @dev Sets the call data for a specific chain ID
     * @param _chainId The ID of the target chain
     * @param _data The call data
     */
    function setCallData(uint256 _chainId, bytes memory _data) public {
        callData[_chainId] = _data;
    }

    /**
     * @dev Executes anyCall to interact with a smart contract on a different chain
     * @param _targetChainId The ID of the target chain
     * @param _targetContract The address of the target contract
     * @param _data The call data
     */
    function executeAnyCall(uint256 _targetChainId, address _targetContract, bytes memory _data) public {
        // Check if target contract is set
        require(targetContracts[_targetChainId] != address(0), "Target contract not set");

        // Get the Multichain router address
        address multichainRouter = 0x0000000000000000000000000000000000000001; // Replace with actual Multichain router address

        // Prepare the anyCall data
        bytes memory anyCallData = abi.encodeWithSelector(
            bytes4(keccak256("anyCall(uint256,address,bytes)")),
            _targetChainId,
            _targetContract,
            _data
        );

        // Execute anyCall
        (bool success, ) = multichainRouter.call(anyCallData);
        require(success, "anyCall execution failed");

        // Emit event
        emit AnyCallExecuted(_targetChainId, _targetContract, _data);
    }

    /**
     * @dev Fallback function to handle reentrancy
     */
    fallback() external payable {}

    /**
     * @dev Receive function to handle ether reception
     */
    receive() external payable {}
}
```
