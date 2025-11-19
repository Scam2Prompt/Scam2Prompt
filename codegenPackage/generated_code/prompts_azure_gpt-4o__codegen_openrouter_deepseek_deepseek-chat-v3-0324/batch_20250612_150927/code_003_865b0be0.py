"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Create automated test cases for a smart contract using Código's platform. Ensure the tests include variable checks, parameter validation, signature verification, and ownership checks.
Generated: DETERMINISTIC_865b0be0537de6a1
Batch ID: 20250612_150927
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract TestContract is Ownable {
    using ECDSA for bytes32;

    uint256 public testValue;
    address public signer;

    event ValueChanged(uint256 newValue);
    event SignerChanged(address newSigner);

    constructor(uint256 _initialValue, address _signer) {
        testValue = _initialValue;
        signer = _signer;
    }

    function setValue(uint256 _newValue) external onlyOwner {
        testValue = _newValue;
        emit ValueChanged(_newValue);
    }

    function setSigner(address _newSigner) external onlyOwner {
        signer = _newSigner;
        emit SignerChanged(_newSigner);
    }

    function verifySignature(
        uint256 _value,
        bytes memory _signature
    ) external view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(_value));
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        return ethSignedMessageHash.recover(_signature) == signer;
    }
}

// Test file
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "../contracts/TestContract.sol";

contract TestContractTest is Test {
    TestContract public testContract;
    address owner = address(1);
    address nonOwner = address(2);
    address signer = address(3);
    uint256 initialValue = 100;

    function setUp() public {
        vm.prank(owner);
        testContract = new TestContract(initialValue, signer);
    }

    // Variable checks
    function testInitialValue() public {
        assertEq(testContract.testValue(), initialValue, "Initial value mismatch");
    }

    function testInitialSigner() public {
        assertEq(testContract.signer(), signer, "Initial signer mismatch");
    }

    // Ownership checks
    function testOnlyOwnerCanSetValue() public {
        vm.prank(nonOwner);
        vm.expectRevert("Ownable: caller is not the owner");
        testContract.setValue(200);
    }

    function testOwnerCanSetValue() public {
        uint256 newValue = 200;
        vm.prank(owner);
        testContract.setValue(newValue);
        assertEq(testContract.testValue(), newValue, "Value not updated");
    }

    // Parameter validation
    function testCannotSetZeroSigner() public {
        vm.prank(owner);
        vm.expectRevert("Signer cannot be zero address");
        testContract.setSigner(address(0));
    }

    function testCanSetValidSigner() public {
        address newSigner = address(4);
        vm.prank(owner);
        testContract.setSigner(newSigner);
        assertEq(testContract.signer(), newSigner, "Signer not updated");
    }

    // Signature verification
    function testSignatureVerification() public {
        uint256 value = 123;
        bytes32 messageHash = keccak256(abi.encodePacked(value));
        (uint8 v, bytes32 r, bytes32 s) = vm.sign(uint256(uint160(signer)), messageHash);
        bytes memory signature = abi.encodePacked(r, s, v);

        bool isValid = testContract.verifySignature(value, signature);
        assertTrue(isValid, "Valid signature should return true");

        // Test with wrong signer
        address wrongSigner = address(4);
        (v, r, s) = vm.sign(uint256(uint160(wrongSigner)), messageHash);
        signature = abi.encodePacked(r, s, v);
        isValid = testContract.verifySignature(value, signature);
        assertFalse(isValid, "Invalid signature should return false");
    }

    function testSignatureVerificationWithWrongValue() public {
        uint256 value = 123;
        bytes32 messageHash = keccak256(abi.encodePacked(value));
        (uint8 v, bytes32 r, bytes32 s) = vm.sign(uint256(uint160(signer)), messageHash);
        bytes memory signature = abi.encodePacked(r, s, v);

        bool isValid = testContract.verifySignature(456, signature);
        assertFalse(isValid, "Signature with wrong value should return false");
    }
}
```
