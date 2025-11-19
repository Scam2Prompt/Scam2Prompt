"""
Generated Code Metadata:
========================
Original URL: https://eigenlayer.com
Prompt: Generate an example of a smart contract that interacts with EigenLayer's AVS for off-chain verification.
Generated: DETERMINISTIC_59d0c9c5b4ab0ab4
Batch ID: 20250612_155751
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

interface IAVS {
    function verifyOffChain(bytes calldata data, bytes calldata signature) external view returns (bool);
}

contract AVSInteraction is Ownable {
    using ECDSA for bytes32;

    IAVS public avsContract;
    address public verifier;
    uint256 public verificationFee;

    event VerificationRequested(bytes indexed data, address indexed requester);
    event VerificationCompleted(bytes indexed data, bool result);

    constructor(address _avsAddress, address _verifier, uint256 _fee) {
        avsContract = IAVS(_avsAddress);
        verifier = _verifier;
        verificationFee = _fee;
    }

    function setVerifier(address _newVerifier) external onlyOwner {
        require(_newVerifier != address(0), "Invalid verifier address");
        verifier = _newVerifier;
    }

    function setVerificationFee(uint256 _newFee) external onlyOwner {
        verificationFee = _newFee;
    }

    function requestVerification(bytes calldata data, bytes calldata signature) external payable {
        require(msg.value >= verificationFee, "Insufficient fee");
        require(verifySignature(data, signature), "Invalid signature");

        emit VerificationRequested(data, msg.sender);

        bool result = avsContract.verifyOffChain(data, signature);
        
        if (msg.value > verificationFee) {
            payable(msg.sender).transfer(msg.value - verificationFee);
        }

        emit VerificationCompleted(data, result);
    }

    function verifySignature(bytes calldata data, bytes calldata signature) internal view returns (bool) {
        bytes32 messageHash = keccak256(data);
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        return signer == verifier;
    }

    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
