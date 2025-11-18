"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuki-nft.pages.dev
Prompt: Create a Solidity smart contract snippet for handling NFT purchases, specifically tailored for Azuki Elementals.
Generated: DETERMINISTIC_dec8e9117c6a46aa
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title AzukiElementalsMarketplace
 * @notice A smart contract to handle NFT purchases for Azuki Elementals
 */
contract AzukiElementalsMarketplace {
    // State variables
    address public owner; // Contract owner
    address public azukiElementalsContract; // Address of the Azuki Elementals NFT contract
    uint256 public nftPrice; // Fixed price for NFTs (in wei)

    // Events
    event NFTPurchased(address indexed buyer, uint256 indexed tokenId, uint256 price);
    event PriceUpdated(uint256 oldPrice, uint256 newPrice);

    // Constructor
    constructor(address _azukiElementalsContract, uint256 _nftPrice) {
        require(_azukiElementalsContract != address(0), "Invalid NFT contract address");
        require(_nftPrice > 0, "NFT price must be greater than zero");

        owner = msg.sender;
        azukiElementalsContract = _azukiElementalsContract;
        nftPrice = _nftPrice;
    }

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to update the NFT price
    function updatePrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "New price must be greater than zero");
        emit PriceUpdated(nftPrice, _newPrice);
        nftPrice = _newPrice;
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 _tokenId) external payable {
        require(msg.value == nftPrice, "Incorrect payment amount");

        // Call the Azuki Elementals contract to transfer the NFT
        // Assuming the Azuki Elementals contract implements a standard ERC-721
        (bool success, bytes memory data) = azukiElementalsContract.call(
            abi.encodeWithSignature("safeTransferFrom(address,address,uint256)", owner, msg.sender, _tokenId)
        );
        require(success && (data.length == 0 || abi.decode(data, (bool))), "NFT transfer failed");

        emit NFTPurchased(msg.sender, _tokenId, msg.value);
    }

    // Function to withdraw contract balance
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback and receive functions to prevent accidental ETH transfers
    fallback() external payable {
        revert("Fallback function is disabled");
    }

    receive() external payable {
        revert("Direct ETH transfers not accepted");
    }
}
```
