"""
Generated Code Metadata:
========================
Original URL: https://chestme.com
Prompt: "Design a smart contract function in Solidity that handles the distribution of $ME tokens in exchange for NFT vouchers."
Generated: DETERMINISTIC_4ebe966e1bd0634e
Batch ID: 20250622_211123
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

/**
 * @title TokenDistributor
 * @dev A smart contract to handle the distribution of $ME tokens in exchange for NFT vouchers.
 */
contract TokenDistributor {
    IERC20 public meToken; // ERC20 token contract ($ME token)
    IERC721 public nftVoucher; // ERC721 NFT voucher contract

    address public owner; // Owner of the contract

    // Mapping to track redeemed NFT vouchers
    mapping(uint256 => bool) public redeemedVouchers;

    // Events
    event TokensDistributed(address indexed recipient, uint256 indexed voucherId, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token and NFT voucher addresses.
     * @param _meToken Address of the $ME token contract.
     * @param _nftVoucher Address of the NFT voucher contract.
     */
    constructor(IERC20 _meToken, IERC721 _nftVoucher) {
        meToken = _meToken;
        nftVoucher = _nftVoucher;
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute $ME tokens in exchange for NFT vouchers.
     * @param voucherId ID of the NFT voucher being redeemed.
     * @param tokenAmount Amount of $ME tokens to distribute.
     */
    function redeemVoucher(uint256 voucherId, uint256 tokenAmount) external {
        // Ensure the voucher has not been redeemed
        require(!redeemedVouchers[voucherId], "Voucher already redeemed");

        // Ensure the caller owns the NFT voucher
        require(nftVoucher.ownerOf(voucherId) == msg.sender, "Caller does not own the voucher");

        // Mark the voucher as redeemed
        redeemedVouchers[voucherId] = true;

        // Transfer the $ME tokens to the caller
        require(meToken.transfer(msg.sender, tokenAmount), "Token transfer failed");

        // Emit an event for successful distribution
        emit TokensDistributed(msg.sender, voucherId, tokenAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner).
     * @param tokenAddress Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(IERC20(tokenAddress).transfer(owner, amount), "Token withdrawal failed");
    }

    /**
     * @dev Function to update the $ME token contract address (only owner).
     * @param _meToken New address of the $ME token contract.
     */
    function updateTokenAddress(IERC20 _meToken) external onlyOwner {
        meToken = _meToken;
    }

    /**
     * @dev Function to update the NFT voucher contract address (only owner).
     * @param _nftVoucher New address of the NFT voucher contract.
     */
    function updateVoucherAddress(IERC721 _nftVoucher) external onlyOwner {
        nftVoucher = _nftVoucher;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Interface for ERC721 token
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
