"""
Generated Code Metadata:
========================
Original URL: https://multisig-astronize-hotwallet.bitkubblockchain.net
Prompt: Provide an example of a smart contract that integrates with the Multi Sig Wallet Tool on Bitkub blockchain for managing multi-signature transactions.
Generated: DETERMINISTIC_d58d6b3f444a2179
Batch ID: 20250612_154803
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title MultiSigWallet contract
 * @author [Your Name]
 * @notice A smart contract that integrates with the Multi Sig Wallet Tool on Bitkub blockchain for managing multi-signature transactions.
 */
contract MultiSigWallet {
    using SafeMath for uint256;
    using SafeERC20 for ERC20;

    // Mapping of owners and their respective balances
    mapping (address => uint256) public owners;

    // Mapping of transactions
    mapping (uint256 => Transaction) public transactions;

    // Mapping of confirmations
    mapping (uint256 => mapping (address => bool)) public confirmations;

    // List of owners
    address[] public ownerList;

    // Number of confirmations required
    uint256 public numConfirmationsRequired;

    // Transaction struct
    struct Transaction {
        uint256 id;
        address to;
        uint256 value;
        bytes data;
        bool executed;
    }

    // Event emitted when a transaction is proposed
    event TransactionProposed(uint256 id, address to, uint256 value, bytes data);

    // Event emitted when a transaction is confirmed
    event TransactionConfirmed(uint256 id, address owner);

    // Event emitted when a transaction is executed
    event TransactionExecuted(uint256 id);

    // Event emitted when an owner is added
    event OwnerAdded(address owner);

    // Event emitted when an owner is removed
    event OwnerRemoved(address owner);

    /**
     * @dev Constructor
     * @param _owners List of owners
     * @param _numConfirmationsRequired Number of confirmations required
     */
    constructor(address[] memory _owners, uint256 _numConfirmationsRequired) public {
        require(_owners.length > 0, "At least one owner is required");
        require(_numConfirmationsRequired > 0, "Number of confirmations required must be greater than 0");
        require(_numConfirmationsRequired <= _owners.length, "Number of confirmations required must not exceed the number of owners");

        for (uint256 i = 0; i < _owners.length; i++) {
            require(_owners[i] != address(0), "Owner address cannot be zero");
            owners[_owners[i]] = 1;
            ownerList.push(_owners[i]);
        }

        numConfirmationsRequired = _numConfirmationsRequired;
    }

    /**
     * @dev Propose a transaction
     * @param _to Address of the recipient
     * @param _value Value of the transaction
     * @param _data Data of the transaction
     */
    function proposeTransaction(address _to, uint256 _value, bytes memory _data) public {
        require(owners[msg.sender] > 0, "Only owners can propose transactions");

        uint256 id = uint256(keccak256(abi.encodePacked(_to, _value, _data)));

        require(transactions[id].id == 0, "Transaction already exists");

        transactions[id] = Transaction({
            id: id,
            to: _to,
            value: _value,
            data: _data,
            executed: false
        });

        emit TransactionProposed(id, _to, _value, _data);
    }

    /**
     * @dev Confirm a transaction
     * @param _id ID of the transaction
     */
    function confirmTransaction(uint256 _id) public {
        require(transactions[_id].id > 0, "Transaction does not exist");
        require(!confirmations[_id][msg.sender], "Transaction already confirmed by this owner");

        confirmations[_id][msg.sender] = true;

        emit TransactionConfirmed(_id, msg.sender);

        if (getConfirmations(_id) >= numConfirmationsRequired) {
            executeTransaction(_id);
        }
    }

    /**
     * @dev Execute a transaction
     * @param _id ID of the transaction
     */
    function executeTransaction(uint256 _id) internal {
        require(transactions[_id].id > 0, "Transaction does not exist");
        require(!transactions[_id].executed, "Transaction already executed");

        transactions[_id].executed = true;

        (bool sent, ) = payable(transactions[_id].to).call{value: transactions[_id].value}(transactions[_id].data);
        require(sent, "Failed to send ether");

        emit TransactionExecuted(_id);
    }

    /**
     * @dev Get the number of confirmations for a transaction
     * @param _id ID of the transaction
     * @return Number of confirmations
     */
    function getConfirmations(uint256 _id) internal view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < ownerList.length; i++) {
            if (confirmations[_id][ownerList[i]]) {
                count = count.add(1);
            }
        }
        return count;
    }

    /**
     * @dev Add an owner
     * @param _owner Address of the new owner
     */
    function addOwner(address _owner) public {
        require(owners[msg.sender] > 0, "Only owners can add new owners");
        require(_owner != address(0), "Owner address cannot be zero");
        require(owners[_owner] == 0, "Owner already exists");

        owners[_owner] = 1;
        ownerList.push(_owner);

        emit OwnerAdded(_owner);
    }

    /**
     * @dev Remove an owner
     * @param _owner Address of the owner to be removed
     */
    function removeOwner(address _owner) public {
        require(owners[msg.sender] > 0, "Only owners can remove owners");
        require(owners[_owner] > 0, "Owner does not exist");

        owners[_owner] = 0;

        for (uint256 i = 0; i < ownerList.length; i++) {
            if (ownerList[i] == _owner) {
                ownerList[i] = ownerList[ownerList.length - 1];
                ownerList.pop();
                break;
            }
        }

        emit OwnerRemoved(_owner);
    }
}
```
