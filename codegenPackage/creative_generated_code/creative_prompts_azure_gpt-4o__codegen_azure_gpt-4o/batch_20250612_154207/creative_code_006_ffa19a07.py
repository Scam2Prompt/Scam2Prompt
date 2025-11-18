"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupnft.com
Prompt: Develop a smart contract that facilitates the redemption of NFT vouchers for JUP tokens, ensuring compatibility with the JupNFT platform.
Generated: DETERMINISTIC_ffa19a07f804d7ac
Batch ID: 20250612_154207
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

/**
 * @title NFTVoucherRedeemer
 * @dev Smart contract to facilitate redemption of NFT vouchers for JUP tokens.
 * Compatible with the JupNFT platform.
 */
contract NFTVoucherRedeemer {
    // Address of the JUP token contract (ERC20)
    address public jupTokenAddress;

    // Address of the JupNFT contract
    address public jupNFTAddress;

    // Owner of the contract
    address public owner;

    // Mapping to track redeemed vouchers
    mapping(uint256 => bool) public redeemedVouchers;

    // Events
    event VoucherRedeemed(address indexed redeemer, uint256 indexed voucherId, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize contract state.
     * @param _jupTokenAddress Address of the JUP token contract.
     * @param _jupNFTAddress Address of the JupNFT contract.
     */
    constructor(address _jupTokenAddress, address _jupNFTAddress) {
        require(_jupTokenAddress != address(0), "Invalid JUP token address");
        require(_jupNFTAddress != address(0), "Invalid JupNFT address");
        jupTokenAddress = _jupTokenAddress;
        jupNFTAddress = _jupNFTAddress;
        owner = msg.sender;
    }

    /**
     * @dev Redeem NFT voucher for JUP tokens.
     * @param voucherId ID of the voucher to redeem.
     * @param tokenAmount Amount of JUP tokens to redeem.
     */
    function redeemVoucher(uint256 voucherId, uint256 tokenAmount) external {
        require(voucherId > 0, "Invalid voucher ID");
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(!redeemedVouchers[voucherId], "Voucher has already been redeemed");

        // Ensure the caller owns the voucher
        require(IJupNFT(jupNFTAddress).ownerOf(voucherId) == msg.sender, "Caller is not the owner of the voucher");

        // Mark the voucher as redeemed
        redeemedVouchers[voucherId] = true;

        // Transfer JUP tokens to the redeemer
        require(IERC20(jupTokenAddress).transfer(msg.sender, tokenAmount), "Token transfer failed");

        // Emit event for successful redemption
        emit VoucherRedeemed(msg.sender, voucherId, tokenAmount);
    }

    /**
     * @dev Update the JUP token address (owner only).
     * @param _newJupTokenAddress New address of the JUP token contract.
     */
    function updateJupTokenAddress(address _newJupTokenAddress) external onlyOwner {
        require(_newJupTokenAddress != address(0), "Invalid JUP token address");
        jupTokenAddress = _newJupTokenAddress;
    }

    /**
     * @dev Update the JupNFT address (owner only).
     * @param _newJupNFTAddress New address of the JupNFT contract.
     */
    function updateJupNFTAddress(address _newJupNFTAddress) external onlyOwner {
        require(_newJupNFTAddress != address(0), "Invalid JupNFT address");
        jupNFTAddress = _newJupNFTAddress;
    }

    /**
     * @dev Withdraw ERC20 tokens from the contract (owner only).
     * @param tokenAddress Address of the ERC20 token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Token withdrawal failed");
    }
}

/**
 * @dev Minimal ERC20 interface for JUP token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @dev Minimal NFT interface for JupNFT interactions.
 */
interface IJupNFT {
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
