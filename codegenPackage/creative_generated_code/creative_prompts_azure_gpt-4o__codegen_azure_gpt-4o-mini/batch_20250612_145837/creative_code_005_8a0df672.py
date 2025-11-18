"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetdappsites.web.app
Prompt: Write a smart contract that integrates StarkGate for asset bridging between Ethereum and Starknet.
Generated: DETERMINISTIC_8a0df672b4798b5d
Batch ID: 20250612_145837
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

// Import OpenZeppelin contracts for safe math and ownable functionality
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for StarkGate bridge
interface IStarkGate {
    function deposit(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _chainId
    ) external;

    function withdraw(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _chainId
    ) external;
}

// Smart contract for bridging assets between Ethereum and StarkNet
contract AssetBridge is Ownable {
    // Instance of the StarkGate bridge
    IStarkGate public starkGate;

    // Event emitted when assets are bridged
    event AssetsBridged(address indexed token, uint256 amount, address indexed to, uint256 chainId);

    // Event emitted when assets are withdrawn
    event AssetsWithdrawn(address indexed token, uint256 amount, address indexed to, uint256 chainId);

    // Constructor to set the StarkGate bridge address
    constructor(address _starkGateAddress) {
        require(_starkGateAddress != address(0), "Invalid StarkGate address");
        starkGate = IStarkGate(_starkGateAddress);
    }

    // Function to bridge assets to StarkNet
    function bridgeAssets(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _chainId
    ) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_to != address(0), "Invalid recipient address");

        // Transfer the specified amount of tokens from the caller to this contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Approve the StarkGate contract to spend the tokens
        IERC20(_token).approve(address(starkGate), _amount);

        // Deposit the tokens into the StarkGate bridge
        starkGate.deposit(_token, _amount, _to, _chainId);

        emit AssetsBridged(_token, _amount, _to, _chainId);
    }

    // Function to withdraw assets from StarkNet
    function withdrawAssets(
        address _token,
        uint256 _amount,
        address _to,
        uint256 _chainId
    ) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(_to != address(0), "Invalid recipient address");

        // Withdraw the tokens from the StarkGate bridge
        starkGate.withdraw(_token, _amount, _to, _chainId);

        emit AssetsWithdrawn(_token, _amount, _to, _chainId);
    }

    // Function to set a new StarkGate address (only owner)
    function setStarkGateAddress(address _newStarkGateAddress) external onlyOwner {
        require(_newStarkGateAddress != address(0), "Invalid StarkGate address");
        starkGate = IStarkGate(_newStarkGateAddress);
    }
}
```
