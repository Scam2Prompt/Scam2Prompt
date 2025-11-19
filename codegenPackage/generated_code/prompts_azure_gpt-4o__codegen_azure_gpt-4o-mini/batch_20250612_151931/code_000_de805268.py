"""
Generated Code Metadata:
========================
Original URL: https://doptest-dop.web.app
Prompt: Write a smart contract in Solidity that integrates the Data Ownership Protocol (DOP) to enable selective disclosure of ERC20 token holdings using zero-knowledge proofs.
Generated: DETERMINISTIC_de805268adfd43ce
Batch ID: 20250612_151931
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Data Ownership Protocol (DOP)
interface IDataOwnershipProtocol {
    function generateProof(address user, uint256 amount) external view returns (bytes memory);
    function verifyProof(address user, uint256 amount, bytes memory proof) external view returns (bool);
}

// Smart contract for selective disclosure of ERC20 token holdings
contract SelectiveDisclosure {
    // State variables
    IERC20 public token; // ERC20 token contract
    IDataOwnershipProtocol public dop; // DOP contract

    // Event emitted when a proof is generated
    event ProofGenerated(address indexed user, uint256 amount, bytes proof);

    // Constructor to initialize the contract with the token and DOP addresses
    constructor(address _token, address _dop) {
        require(_token != address(0), "Token address cannot be zero");
        require(_dop != address(0), "DOP address cannot be zero");
        
        token = IERC20(_token);
        dop = IDataOwnershipProtocol(_dop);
    }

    // Function to generate a zero-knowledge proof for the user's token holdings
    function generateTokenProof(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Generate proof using the DOP
        bytes memory proof = dop.generateProof(msg.sender, amount);
        
        // Emit an event with the generated proof
        emit ProofGenerated(msg.sender, amount, proof);
    }

    // Function to verify a zero-knowledge proof for the user's token holdings
    function verifyTokenProof(address user, uint256 amount, bytes memory proof) external view returns (bool) {
        require(user != address(0), "User address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        // Verify the proof using the DOP
        return dop.verifyProof(user, amount, proof);
    }
}
```
