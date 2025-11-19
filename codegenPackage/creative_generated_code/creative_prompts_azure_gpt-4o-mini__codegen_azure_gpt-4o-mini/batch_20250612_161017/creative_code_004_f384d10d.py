"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharxsharky.web.app
Prompt: Explain how to grow a Sharx NFT into a whale sharx using the $FISHY token in a smart contract.
Generated: DETERMINISTIC_f384d10daf5e3e59
Batch ID: 20250612_161017
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the NFT contract
interface ISharxNFT {
    function mint(address to) external returns (uint256);
    function grow(uint256 tokenId) external returns (bool);
}

contract SharxFarm {
    // ERC20 token used for growing the Sharx NFT
    IERC20 public fishyToken;
    // NFT contract that handles Sharx NFTs
    ISharxNFT public sharxNFT;

    // Mapping to track which owner has which token ID
    mapping(address => uint256) public userSharxTokens;

    // Event emitted when a Sharx NFT is grown
    event SharxGrown(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the address of the ERC20 token and the NFT contract
    constructor(address _fishyToken, address _sharxNFT) {
        fishyToken = IERC20(_fishyToken);
        sharxNFT = ISharxNFT(_sharxNFT);
    }

    // Function to grow a Sharx NFT into a whale Sharx
    function growSharx(uint256 tokenId, uint256 amount) external {
        require(userSharxTokens[msg.sender] == tokenId, "You do not own this Sharx NFT");
        require(amount > 0, "Amount should be greater than zero");

        // Check if the user has enough $FISHY tokens
        uint256 userBalance = fishyToken.balanceOf(msg.sender);
        require(userBalance >= amount, "Insufficient $FISHY tokens");

        // Transfer the $FISHY tokens from the user to this contract
        bool transferSuccess = fishyToken.transferFrom(msg.sender, address(this), amount);
        require(transferSuccess, "Token transfer failed");

        // Call the grow function on the NFT contract
        bool growSuccess = sharxNFT.grow(tokenId);
        require(growSuccess, "Failed to grow the Sharx NFT");

        // Emit an event for the successful growth
        emit SharxGrown(msg.sender, tokenId);
    }

    // Function to mint a new Sharx NFT and associate it with the user
    function mintSharx() external {
        uint256 newTokenId = sharxNFT.mint(msg.sender);
        userSharxTokens[msg.sender] = newTokenId;
    }

    // Function to withdraw $FISHY tokens from the contract
    function withdrawTokens(uint256 amount) external {
        uint256 contractBalance = fishyToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        bool withdrawSuccess = fishyToken.transfer(msg.sender, amount);
        require(withdrawSuccess, "Token withdrawal failed");
    }
}
```
