"""
Generated Code Metadata:
========================
Original URL: https://www.gnosis-safe.io
Prompt: "Create a Safe{Foundry} project to build a custom smart account abstraction stack, integrating with the Safe ecosystem and leveraging its security features."
Generated: DETERMINISTIC_7c7b6e04417ac303
Batch ID: 20250622_204703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.12;

import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@safe-global/safe-contracts/contracts/Safe.sol";
import "@safe-global/safe-contracts/contracts/proxies/SafeProxyFactory.sol";
import "@safe-global/safe-contracts/contracts/common/Enum.sol";

/**
 * @title SafeAccountAbstraction
 * @dev A custom smart account abstraction layer integrating with Safe ecosystem
 */
contract SafeAccountAbstraction is Initializable {
    using ECDSA for bytes32;

    address public safeProxy;
    address public owner;
    SafeProxyFactory public safeProxyFactory;
    Safe public safeSingleton;

    event AccountInitialized(address indexed safeProxy, address indexed owner);
    event ExecutedTransaction(address indexed to, uint256 value, bytes data, Enum.Operation operation);

    /**
     * @dev Initialize the account abstraction with Safe proxy
     * @param _owner The owner address for this account
     * @param _safeProxyFactory Address of SafeProxyFactory contract
     * @param _safeSingleton Address of Safe singleton contract
     * @param _initializers Array of initializer calls for the Safe
     */
    function initialize(
        address _owner,
        address _safeProxyFactory,
        address _safeSingleton,
        bytes[] memory _initializers
    ) external initializer {
        require(_owner != address(0), "Invalid owner address");
        require(_safeProxyFactory != address(0), "Invalid factory address");
        require(_safeSingleton != address(0), "Invalid singleton address");

        owner = _owner;
        safeProxyFactory = SafeProxyFactory(_safeProxyFactory);
        safeSingleton = Safe(_safeSingleton);

        // Create Safe proxy
        safeProxy = address(safeProxyFactory.createProxyWithNonce(
            address(safeSingleton),
            getInitializerData(_owner, _initializers),
            uint256(uint160(_owner))
        ));

        emit AccountInitialized(safeProxy, _owner);
    }

    /**
     * @dev Execute a transaction through the Safe proxy
     * @param to Target address
     * @param value ETH value to send
     * @param data Calldata to send
     * @param operation Operation type (Call or DelegateCall)
     * @param signatures Packed signature data
     */
    function execute(
        address to,
        uint256 value,
        bytes memory data,
        Enum.Operation operation,
        bytes memory signatures
    ) external {
        require(msg.sender == owner, "Caller is not owner");
        
        // Verify signatures
        bytes32 txHash = Safe(safeProxy).getTransactionHash(
            to,
            value,
            data,
            operation,
            0, // safeTxGas
            0, // baseGas
            0, // gasPrice
            address(0), // gasToken
            address(0), // refundReceiver
            Safe(safeProxy).nonce()
        );
        
        address recovered = txHash.recover(signatures);
        require(recovered == owner, "Invalid signature");

        // Execute transaction through Safe
        bool success = Safe(safeProxy).execTransaction(
            to,
            value,
            data,
            operation,
            0, // safeTxGas
            0, // baseGas
            0, // gasPrice
            address(0), // gasToken
            payable(address(0)), // refundReceiver
            signatures
        );
        
        require(success, "Transaction failed");
        emit ExecutedTransaction(to, value, data, operation);
    }

    /**
     * @dev Helper function to get initializer data for Safe
     * @param _owner The owner address
     * @param _initializers Array of initializer calls
     * @return bytes memory Encoded initializer data
     */
    function getInitializerData(
        address _owner,
        bytes[] memory _initializers
    ) internal pure returns (bytes memory) {
        address[] memory owners = new address[](1);
        owners[0] = _owner;
        
        bytes memory setupData = abi.encodeWithSelector(
            Safe.setup.selector,
            owners,
            1, // threshold
            address(0), // to
            "", // data
            address(0), // fallbackHandler
            address(0), // paymentToken
            0, // payment
            payable(address(0)) // paymentReceiver
        );

        if (_initializers.length > 0) {
            for (uint i = 0; i < _initializers.length; i++) {
                setupData = bytes.concat(setupData, _initializers[i]);
            }
        }

        return setupData;
    }

    /**
     * @dev Receive function to accept ETH
     */
    receive() external payable {}
}
```
