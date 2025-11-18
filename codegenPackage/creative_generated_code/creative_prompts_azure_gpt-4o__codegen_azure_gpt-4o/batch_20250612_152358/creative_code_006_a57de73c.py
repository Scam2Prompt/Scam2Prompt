"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc-claimer.pages.dev
Prompt: Develop a smart contract example for distributing Notcoin tokens to users, ensuring wallet verification is mandatory.
Generated: DETERMINISTIC_a57de73c9a3a7ee8
Batch ID: 20250612_152358
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
 * @title NotcoinTokenDistributor
 * @dev A smart contract to distribute Notcoin tokens to verified users.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract NotcoinTokenDistributor {
    // Address of the Notcoin token contract
    IERC20 public notcoinToken;

    // Owner of the contract
    address public owner;

    // Mapping to store verified wallets
    mapping(address => bool) public verifiedWallets;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Event emitted when a wallet is verified
    event WalletVerified(address indexed wallet);

    // Event emitted when a wallet is unverified
    event WalletUnverified(address indexed wallet);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the token contract and the owner.
     * @param _tokenAddress The address of the Notcoin token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        notcoinToken = IERC20(_tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Function to verify a wallet address.
     * @param _wallet The wallet address to verify.
     */
    function verifyWallet(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        verifiedWallets[_wallet] = true;
        emit WalletVerified(_wallet);
    }

    /**
     * @dev Function to unverify a wallet address.
     * @param _wallet The wallet address to unverify.
     */
    function unverifyWallet(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        verifiedWallets[_wallet] = false;
        emit WalletUnverified(_wallet);
    }

    /**
     * @dev Function to distribute tokens to a verified wallet.
     * @param _recipient The recipient's wallet address.
     * @param _amount The amount of tokens to distribute.
     */
    function distributeTokens(address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Recipient address cannot be zero");
        require(verifiedWallets[_recipient], "Recipient wallet is not verified");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the recipient
        bool success = notcoinToken.transfer(_recipient, _amount);
        require(success, "Token transfer failed");

        emit TokensDistributed(_recipient, _amount);
    }

    /**
     * @dev Function to update the token contract address.
     * @param _newTokenAddress The new token contract address.
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        notcoinToken = IERC20(_newTokenAddress);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        owner = _newOwner;
    }
}
```
