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
pragma solidity ^0.8.17;

// Import Axelar interfaces
import "@axelar-network/axelar-cgp-solidity/contracts/interfaces/IAxelarGateway.sol";
import "@axelar-network/axelar-cgp-solidity/contracts/interfaces/IAxelarExecutable.sol";

// Interface for the token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function burn(uint256 amount) external;
    function mint(address recipient, uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for bridging $AI tokens across EVM chains
contract AIBridge is IAxelarExecutable {
    // Address of the $AI token contract
    address public aiToken;
    
    // Governance address (or owner)
    address public owner;

    // Event emitted on successful token bridge
    event Bridged(address indexed sender, string destinationChain, string destinationAddress, uint256 amount);

    // Event emitted on mint confirmation
    event MintConfirmed(address indexed recipient, uint256 amount);
    
    // Constructor to initialize contract
    constructor(address _gateway, address _aiToken) IAxelarExecutable(_gateway) {
        owner = msg.sender; // Set deployer as the owner
        aiToken = _aiToken; // Set the $AI token contract address
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Function to bridge tokens to another chain
    function bridgeTokens(
        string memory destinationChain,
        string memory destinationAddress,
        uint256 amount
    ) external {
        // Validate inputs
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(aiToken).balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Burn tokens on the source chain
        IERC20(aiToken).burn(amount);
        
        // Payload for Axelar Gateway
        bytes memory payload = abi.encode(amount);
        
        // Call Axelar Gateway to forward the payload
        gateway.callContract(destinationChain, destinationAddress, payload);

        // Emit bridging event
        emit Bridged(msg.sender, destinationChain, destinationAddress, amount);
    }

    // Function to execute minting after receiving burn confirmation
    function _execute(
        string calldata sourceChain,
        string calldata sourceAddress,
        bytes calldata payload
    ) internal override {
        // Decode the payload
        (uint256 amount, address recipient) = abi.decode(payload, (uint256, address));
        
        // Verify the sender is a valid Axelar Gateway address
        require(msg.sender == address(gateway), "Invalid gateway sender");

        // Mint new tokens on the destination chain
        IERC20(aiToken).mint(recipient, amount);

        // Emit mint confirmation event
        emit MintConfirmed(recipient, amount);
    }

    // Function to update the $AI token contract address (only owner)
    function updateTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Invalid token address");
        aiToken = newTokenAddress;
    }

    // Function to transfer contract ownership
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }
}
```
