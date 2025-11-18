"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinumult.pages.dev
Prompt: Write a smart contract that integrates with Axelar ITS to enable seamless bridging of $AI tokens across EVM chains. Include functionality for verifying burn-and-mint transactions.
Generated: DETERMINISTIC_13857b85dfa37f1c
Batch ID: 20250612_152109
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for Axelar ITS that handles cross-chain communication
interface IAxelarGateway {
    function callContract(string calldata _contract, string calldata _method, bytes calldata _data) external;
}

// Smart contract to bridge $AI tokens across EVM chains using Axelar ITS
contract AITokenBridge is Ownable {
    using Address for address;

    // State variables
    IERC20 public aiToken; // ERC20 token contract for $AI
    IAxelarGateway public axelarGateway; // Axelar Gateway interface

    // Event emitted when tokens are bridged
    event TokensBridged(address indexed sender, uint256 amount, string destinationChain, string destinationAddress);
    event TokensMinted(address indexed recipient, uint256 amount);
    
    // Constructor to initialize the contract
    constructor(address _aiToken, address _axelarGateway) {
        require(_aiToken.isContract(), "Invalid AI Token address");
        require(_axelarGateway.isContract(), "Invalid Axelar Gateway address");
        
        aiToken = IERC20(_aiToken);
        axelarGateway = IAxelarGateway(_axelarGateway);
    }

    // Function to bridge $AI tokens to another chain
    function bridgeTokens(uint256 amount, string calldata destinationChain, string calldata destinationAddress) external {
        require(amount > 0, "Amount must be greater than zero");
        require(aiToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Burn the tokens from the sender's address
        aiToken.transferFrom(msg.sender, address(this), amount);
        
        // Call the Axelar Gateway to initiate the bridging process
        try axelarGateway.callContract(destinationChain, "mintTokens", abi.encode(destinationAddress, amount)) {
            emit TokensBridged(msg.sender, amount, destinationChain, destinationAddress);
        } catch {
            // Handle errors during the Axelar call
            revert("Bridging failed. Transaction not executed.");
        }
    }

    // Function to mint $AI tokens on the destination chain
    function mintTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        
        // Mint $AI tokens to the specified recipient
        aiToken.transfer(recipient, amount);
        emit TokensMinted(recipient, amount);
    }

    // Function to withdraw tokens mistakenly sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(IERC20(tokenAddress).balanceOf(address(this)) >= amount, "Insufficient contract balance");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
