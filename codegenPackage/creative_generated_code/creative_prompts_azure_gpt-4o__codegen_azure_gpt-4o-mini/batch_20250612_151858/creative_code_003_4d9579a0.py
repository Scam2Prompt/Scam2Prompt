"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletpads.web.app
Prompt: Create a smart contract for launching IDO projects on WalletPads, ensuring compatibility with its decentralized protocol.
Generated: DETERMINISTIC_4d9579a0ec77d5cf
Batch ID: 20250612_151858
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

/// @title IDO (Initial DEX Offering) Smart Contract
/// @dev This contract facilitates the launch of IDO projects on WalletPads.
contract IDO {
    address public owner;
    uint256 public idoStartTime;
    uint256 public idoEndTime;
    uint256 public totalTokens;
    uint256 public tokensSold;
    uint256 public tokenPrice; // Price per token in wei

    mapping(address => uint256) public contributions; // Contributions by address
    event TokensPurchased(address indexed buyer, uint256 amount);
    event IdoFinalized();

    /// @dev Constructor to initialize the IDO contract
    /// @param _tokenPrice Price of a token
    /// @param _totalTokens Total tokens available for the IDO
    constructor(uint256 _tokenPrice, uint256 _totalTokens) {
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        require(_totalTokens > 0, "Total tokens must be greater than zero.");
        
        owner = msg.sender;
        tokenPrice = _tokenPrice;
        totalTokens = _totalTokens;
    }

    /// @dev Start the IDO
    /// @param _duration Duration of the IDO in seconds
    function startIdo(uint256 _duration) external onlyOwner {
        require(idoStartTime == 0, "IDO already started.");
        idoStartTime = block.timestamp;
        idoEndTime = idoStartTime + _duration;
    }

    /// @dev Buy tokens during the IDO
    function buyTokens() external payable {
        require(block.timestamp >= idoStartTime, "IDO has not started yet.");
        require(block.timestamp <= idoEndTime, "IDO has ended.");
        require(msg.value > 0, "You must send ether to buy tokens.");

        uint256 tokensToBuy = (msg.value) / tokenPrice;
        require(tokensToBuy + tokensSold <= totalTokens, "Not enough tokens available.");

        contributions[msg.sender] += tokensToBuy;
        tokensSold += tokensToBuy;

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /// @dev Finalize the IDO and allow the owner to withdraw funds
    function finalizeIdo() external onlyOwner {
        require(block.timestamp > idoEndTime, "IDO has not ended yet.");
        
        // Transfer funds to the owner
        payable(owner).transfer(address(this).balance);
        
        emit IdoFinalized();
    }

    /// @dev Allow the owner to withdraw unsold tokens after IDO
    function withdrawUnsoldTokens(address tokenContract) external onlyOwner {
        require(block.timestamp > idoEndTime, "IDO has not ended yet.");
        uint256 unsoldTokens = totalTokens - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw.");

        // Assuming the token contract follows ERC20 standard
        IERC20(tokenContract).transfer(owner, unsoldTokens);
    }

    /// @dev Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner.");
        _;
    }
}

/// @title ERC20 Interface
/// @dev Minimal ERC20 interface for transfer function
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
