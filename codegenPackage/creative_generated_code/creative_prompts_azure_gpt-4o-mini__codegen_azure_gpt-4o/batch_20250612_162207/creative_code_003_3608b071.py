"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-lndscom.pages.dev
Prompt: Develop a smart contract function to handle the presale cap of 1000 ETH for the Leonidas NFT.
Generated: DETERMINISTIC_3608b0711aae5c60
Batch ID: 20250612_162207
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
 * @title LeonidasNFTPresale
 * @dev A smart contract to handle the presale cap for the Leonidas NFT.
 */
contract LeonidasNFTPresale {
    // Address of the contract owner
    address public owner;

    // Maximum presale cap in ETH
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Current amount of ETH raised in the presale
    uint256 public totalRaised;

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;

    // Event to log contributions
    event ContributionReceived(address indexed contributor, uint256 amount);
    event PresaleCapReached();

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to handle direct ETH transfers to the contract.
     */
    receive() external payable {
        contribute();
    }

    /**
     * @dev Function to handle contributions during the presale.
     */
    function contribute() public payable {
        // Validate contribution amount
        require(msg.value > 0, "Contribution must be greater than zero.");

        // Ensure presale cap has not been reached
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded.");

        // Update state variables
        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        // Emit contribution event
        emit ContributionReceived(msg.sender, msg.value);

        // Check if presale cap has been reached
        if (totalRaised == PRESALE_CAP) {
            emit PresaleCapReached();
        }
    }

    /**
     * @dev Function for the owner to withdraw the ETH collected during the presale.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal.");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Function to check the remaining presale capacity.
     */
    function remainingCapacity() external view returns (uint256) {
        return PRESALE_CAP - totalRaised;
    }
}
```
