"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge-finance.org
Prompt: Generate Solidity smart contract code that interacts with deBridge to issue equivalent assets on a target blockchain during a cross-chain transfer.
Generated: DETERMINISTIC_fbfc9bc135d3da87
Batch ID: 20250612_154115
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

// Importing necessary interfaces from deBridge
import "@debridge-finance/debridge-eth-bridge/contracts/interfaces/IDeBridge.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CrossChainAssetIssuer {
    // Address of the deBridge contract
    IDeBridge public deBridge;
    
    // The address of the ERC20 token that will be used for cross-chain transfers
    IERC20 public assetToken;

    // Event to log when an asset is issued
    event AssetIssued(address indexed recipient, uint256 amount, uint256 targetChainId);

    // Constructor to initialize the contract with deBridge address and asset token
    constructor(address _deBridgeAddress, address _assetTokenAddress) {
        require(_deBridgeAddress != address(0), "Invalid deBridge address");
        require(_assetTokenAddress != address(0), "Invalid asset token address");
        
        deBridge = IDeBridge(_deBridgeAddress);
        assetToken = IERC20(_assetTokenAddress);
    }

    // Function to issue equivalent assets on a target blockchain
    function issueAssets(uint256 amount, uint256 targetChainId) external {
        require(amount > 0, "Amount must be greater than 0");
        require(assetToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the asset tokens from the user to this contract
        assetToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve the deBridge contract to spend the asset tokens
        assetToken.approve(address(deBridge), amount);

        // Execute the cross-chain transfer through deBridge
        deBridge.send{value: 0}(
            address(assetToken), // token address
            amount,              // amount to send
            targetChainId,      // target chain ID
            msg.sender,         // recipient on the target chain
            0,                  // referer (can be used for additional data)
            new bytes(0)        // any additional data
        );

        // Emit an event for the asset issuance
        emit AssetIssued(msg.sender, amount, targetChainId);
    }

    // Function to withdraw any unsent tokens back to the owner
    function withdrawTokens(address to, uint256 amount) external {
        require(to != address(0), "Invalid address");
        require(assetToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");
        
        // Transfer the specified amount of tokens to the given address
        assetToken.transfer(to, amount);
    }

    // Fallback function to receive ETH (if needed)
    receive() external payable {}
}
```
