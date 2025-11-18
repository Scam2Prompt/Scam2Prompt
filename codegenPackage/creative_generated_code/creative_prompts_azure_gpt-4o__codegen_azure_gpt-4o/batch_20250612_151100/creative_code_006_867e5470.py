"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t-not.com
Prompt: Create a smart contract snippet to verify wallet addresses and distribute Notcoin ($NOT) tokens as part of the airdrop campaign.
Generated: DETERMINISTIC_867e547024aec9a3
Batch ID: 20250612_151100
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
 * @title AirdropDistributor
 * @dev Smart contract to distribute Notcoin ($NOT) tokens to verified wallet addresses.
 */
contract AirdropDistributor {
    // Address of the $NOT token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are successfully distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with $NOT token address.
     * @param _tokenAddress Address of the $NOT token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute $NOT tokens to a list of wallet addresses.
     * @param recipients List of recipient wallet addresses.
     * @param amounts List of token amounts corresponding to each recipient address.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length > 0, "Recipients list cannot be empty");
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(recipient != address(0), "Invalid recipient address");
            require(amount > 0, "Amount must be greater than zero");

            // Call the transfer function on the $NOT token contract
            (bool success, bytes memory data) = tokenAddress.call(
                abi.encodeWithSignature("transfer(address,uint256)", recipient, amount)
            );

            // Verify transfer success
            require(success && (data.length == 0 || abi.decode(data, (bool))), "Token transfer failed");

            // Emit event for successful distribution
            emit TokensDistributed(recipient, amount);
        }
    }

    /**
     * @dev Function to update the token contract address by owner.
     * @param _newTokenAddress Address of the new token contract.
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        tokenAddress = _newTokenAddress;
    }

    /**
     * @dev Function to transfer contract ownership.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    fallback() external payable {
        revert("Contract does not accept ETH");
    }

    /**
     * @dev Receive function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
