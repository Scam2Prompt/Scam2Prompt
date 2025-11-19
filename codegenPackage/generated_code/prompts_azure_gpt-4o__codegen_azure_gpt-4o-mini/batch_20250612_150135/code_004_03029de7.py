"""
Generated Code Metadata:
========================
Original URL: https://across-to.com
Prompt: Create a tutorial for developers on how to use the Across Protocol’s smart contracts to build scalable cross-chain DeFi applications.
Generated: DETERMINISTIC_03029de7a1174a9e
Batch ID: 20250612_150135
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Across Protocol's smart contracts
interface IAcross {
    function send(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _destinationChainId
    ) external returns (bool);
    
    function receive(
        address _token,
        uint256 _amount,
        address _from,
        uint256 _sourceChainId
    ) external returns (bool);
}

// Main contract for interacting with Across Protocol
contract CrossChainDeFi is Ownable {
    IAcross public acrossProtocol;

    // Event emitted when tokens are sent
    event TokensSent(address indexed token, uint256 amount, address indexed to, uint256 destinationChainId);
    
    // Event emitted when tokens are received
    event TokensReceived(address indexed token, uint256 amount, address indexed from, uint256 sourceChainId);

    // Constructor to set the Across Protocol contract address
    constructor(address _acrossProtocolAddress) {
        require(_acrossProtocolAddress != address(0), "Invalid Across Protocol address");
        acrossProtocol = IAcross(_acrossProtocolAddress);
    }

    // Function to send tokens across chains
    function sendTokens(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _destinationChainId
    ) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_to != address(0), "Invalid recipient address");
        
        // Transfer tokens from sender to this contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        
        // Approve the Across Protocol to spend the tokens
        IERC20(_token).approve(address(acrossProtocol), _amount);
        
        // Call the Across Protocol to send tokens
        bool success = acrossProtocol.send(_token, _amount, _to, _destinationChainId);
        require(success, "Token transfer failed");

        emit TokensSent(_token, _amount, _to, _destinationChainId);
    }

    // Function to receive tokens from Across Protocol
    function receiveTokens(
        address _token,
        uint256 _amount,
        address _from,
        uint256 _sourceChainId
    ) external {
        // Ensure that only the Across Protocol can call this function
        require(msg.sender == address(acrossProtocol), "Unauthorized caller");
        
        // Transfer tokens to the recipient
        IERC20(_token).transfer(_from, _amount);
        
        emit TokensReceived(_token, _amount, _from, _sourceChainId);
    }

    // Function to withdraw tokens from the contract (for emergencies)
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
