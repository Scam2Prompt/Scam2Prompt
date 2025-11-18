"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquidfoundatlon.org
Prompt: Develop a Solidity smart contract that integrates with the Hyper Foundation Hypurr NFT Mint Portal for validating wallet addresses eligible for the Genesis Collection minting.
Generated: DETERMINISTIC_dc33d154feb8f814
Batch ID: 20250612_153947
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
 * @title Hypurr NFT Mint Portal Integration
 * @dev This contract integrates with the Hyper Foundation Hypurr NFT Mint Portal 
 * to validate wallet addresses eligible for the Genesis Collection minting.
 */
contract HypurrNFTMintPortal {
    // Mapping to track eligible wallet addresses
    mapping(address => bool) private eligibleWallets;

    // Event to emit when a wallet is marked eligible
    event WalletMarkedEligible(address indexed wallet);

    // Event to emit when a wallet is marked ineligible
    event WalletMarkedIneligible(address indexed wallet);

    // Modifier to check if the caller is an eligible wallet
    modifier onlyEligible() {
        require(isEligible(msg.sender), "Caller is not eligible for minting");
        _;
    }

    /**
     * @dev Marks a wallet address as eligible for minting.
     * @param wallet The address of the wallet to mark as eligible.
     */
    function markWalletEligible(address wallet) external {
        require(wallet != address(0), "Invalid wallet address");
        require(!eligibleWallets[wallet], "Wallet is already marked eligible");

        eligibleWallets[wallet] = true;
        emit WalletMarkedEligible(wallet);
    }

    /**
     * @dev Marks a wallet address as ineligible for minting.
     * @param wallet The address of the wallet to mark as ineligible.
     */
    function markWalletIneligible(address wallet) external {
        require(wallet != address(0), "Invalid wallet address");
        require(eligibleWallets[wallet], "Wallet is not marked eligible");

        eligibleWallets[wallet] = false;
        emit WalletMarkedIneligible(wallet);
    }

    /**
     * @dev Checks if a wallet address is eligible for minting.
     * @param wallet The address of the wallet to check.
     * @return True if the wallet is eligible, false otherwise.
     */
    function isEligible(address wallet) public view returns (bool) {
        return eligibleWallets[wallet];
    }
    
    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
