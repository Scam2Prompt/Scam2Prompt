"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Write a smart contract in Solidity that automates payment distribution to product creators and contributors on a blockchain-based platform like LookRev.
Generated: DETERMINISTIC_e45c554675f25d7a
Batch ID: 20250622_210706
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

contract PaymentDistribution {
    // Struct to hold information about each product creator
    struct Creator {
        address payable wallet; // Wallet address of the creator
        uint256 share; // Share percentage of the total payment
    }

    // Mapping to store creators by their address
    mapping(address => Creator) public creators;
    // Total share percentage (should sum up to 100)
    uint256 public totalShare;
    // Event to log payment distribution
    event PaymentDistributed(uint256 amount, address indexed creator);

    // Modifier to check if the caller is a registered creator
    modifier onlyCreator() {
        require(creators[msg.sender].wallet != address(0), "Not a registered creator");
        _;
    }

    // Function to register a new creator
    function registerCreator(address payable _wallet, uint256 _share) external {
        require(_wallet != address(0), "Invalid wallet address");
        require(_share > 0, "Share must be greater than 0");
        require(totalShare + _share <= 100, "Total share exceeds 100%");

        creators[_wallet] = Creator({
            wallet: _wallet,
            share: _share
        });
        totalShare += _share;
    }

    // Function to distribute payments to registered creators
    function distributePayment() external payable {
        require(msg.value > 0, "No payment sent");

        // Distributing payment to each creator based on their share
        for (address creatorAddress in getAllCreators()) {
            Creator memory creator = creators[creatorAddress];
            uint256 payment = (msg.value * creator.share) / 100;
            if (payment > 0) {
                (bool success, ) = creator.wallet.call{value: payment}("");
                require(success, "Payment transfer failed");
                emit PaymentDistributed(payment, creator.wallet);
            }
        }
    }

    // Function to get all registered creators (for internal use)
    function getAllCreators() internal view returns (address[] memory) {
        address[] memory creatorAddresses = new address[](totalShare);
        uint256 index = 0;
        for (address creatorAddress in creators) {
            creatorAddresses[index] = creatorAddress;
            index++;
        }
        return creatorAddresses;
    }

    // Function to withdraw any accidentally sent Ether to the contract
    function withdraw() external {
        require(msg.sender == address(this), "Only contract can withdraw");
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
