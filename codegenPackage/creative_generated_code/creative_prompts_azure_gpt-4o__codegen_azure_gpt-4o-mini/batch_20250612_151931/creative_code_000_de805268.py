"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doptest-dop.web.app
Prompt: Write a smart contract in Solidity that integrates the Data Ownership Protocol (DOP) to enable selective disclosure of ERC20 token holdings using zero-knowledge proofs.
Generated: DETERMINISTIC_de805268adfd43ce
Batch ID: 20250612_151931
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Data Ownership Protocol (DOP)
interface IDataOwnershipProtocol {
    function createProof(
        address user,
        uint256 amount,
        uint256 tokenId
    ) external returns (bytes memory proof);

    function verifyProof(
        bytes memory proof,
        address user,
        uint256 amount,
        uint256 tokenId
    ) external view returns (bool);
}

contract TokenOwnership {
    // State variables
    IDataOwnershipProtocol public dop; // DOP contract instance
    IERC20 public token; // ERC20 token instance

    // Event emitted when a proof is created
    event ProofCreated(address indexed user, uint256 amount, bytes proof);

    // Constructor to initialize DOP and token contracts
    constructor(address _dopAddress, address _tokenAddress) {
        require(_dopAddress != address(0), "Invalid DOP address");
        require(_tokenAddress != address(0), "Invalid token address");
        
        dop = IDataOwnershipProtocol(_dopAddress);
        token = IERC20(_tokenAddress);
    }

    // Function to create a proof for a user's token holdings
    function createTokenProof(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Check the user's token balance
        uint256 userBalance = token.balanceOf(msg.sender);
        require(userBalance >= amount, "Insufficient token balance");

        // Create zero-knowledge proof using DOP
        bytes memory proof = dop.createProof(msg.sender, amount, token.totalSupply());

        // Emit event for created proof
        emit ProofCreated(msg.sender, amount, proof);
    }

    // Function to verify a proof for a user's token holdings
    function verifyTokenProof(bytes memory proof, uint256 amount) external view returns (bool) {
        require(amount > 0, "Amount must be greater than zero");

        // Verify the proof using DOP
        bool isValid = dop.verifyProof(proof, msg.sender, amount, token.totalSupply());
        return isValid;
    }
}
```
