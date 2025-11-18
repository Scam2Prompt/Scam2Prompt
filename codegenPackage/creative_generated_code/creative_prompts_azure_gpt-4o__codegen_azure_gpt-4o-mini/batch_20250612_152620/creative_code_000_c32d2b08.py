"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-en.web.app
Prompt: Write a smart contract on Ethereum that integrates the Data Ownership Protocol (DOP) to enable selective disclosure of ERC20 token holdings using zero-knowledge proofs.
Generated: DETERMINISTIC_c32d2b087d864cea
Batch ID: 20250612_152620
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

// Importing ERC20 interface and DOP library (placeholder for actual DOP implementation)
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for DOP that allows selective disclosure
interface IDataOwnershipProtocol {
    function generateProof(address user, uint256 amount) external view returns (bytes memory);
    function verifyProof(address user, uint256 amount, bytes memory proof) external view returns (bool);
}

// Smart contract for managing ERC20 token holdings with DOP integration
contract TokenDataOwnership is Ownable {
    // Mapping to store user token holdings
    mapping(address => uint256) private balances;
    
    // ERC20 token contract
    IERC20 public token;

    // DOP contract address
    IDataOwnershipProtocol public dop;

    // Event emitted when a user deposits tokens
    event TokensDeposited(address indexed user, uint256 amount);
    // Event emitted when a user requests proof
    event ProofGenerated(address indexed user, uint256 amount);

    // Constructor to set the ERC20 token address and DOP contract address
    constructor(address _tokenAddress, address _dopAddress) {
        token = IERC20(_tokenAddress);
        dop = IDataOwnershipProtocol(_dopAddress);
    }

    // Deposit tokens into the contract
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        balances[msg.sender] += amount;

        emit TokensDeposited(msg.sender, amount);
    }

    // Generate zero-knowledge proof for selective disclosure
    function generateSelectiveDisclosureProof(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance for proof");

        // Generate proof using DOP
        bytes memory proof = dop.generateProof(msg.sender, amount);
        
        emit ProofGenerated(msg.sender, amount);
        // Here you would handle the proof (store or return)
    }

    // Verify the proof of token holdings
    function verifyTokenHoldingProof(address user, uint256 amount, bytes memory proof) external view returns (bool) {
        // Verify the proof using DOP
        return dop.verifyProof(user, amount, proof);
    }

    // Get the balance of an address
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    // Allow owner to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient contract balance");
        require(token.transfer(owner(), amount), "Token withdrawal failed");
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
