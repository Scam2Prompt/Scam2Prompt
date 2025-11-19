"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Create a smart contract for a presale of tokens that includes features like discounted rates and priority support, as seen in the Pushd presale model.
Generated: DETERMINISTIC_2163dc94a211dcf4
Batch ID: 20250612_164304
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
 * @title PresaleTokenContract
 * @dev A smart contract for token presale with discounted rates and priority support.
 */
contract PresaleTokenContract {
    // State variables
    address public owner; // Owner of the contract
    uint256 public tokenRate; // Rate of tokens per Ether
    uint256 public discountedTokenRate; // Discounted rate of tokens per Ether
    uint256 public totalSoldTokens; // Total tokens sold during presale
    bool public presaleActive; // Flag to indicate if presale is active

    mapping(address => uint256) public tokensPurchased; // Tracks tokens purchased by each address
    mapping(address => bool) public priorityAddresses; // Tracks priority addresses

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStarted();
    event PresaleEnded();

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    constructor(uint256 _tokenRate, uint256 _discountedTokenRate) {
        require(_tokenRate > 0, "Token rate must be greater than zero");
        require(_discountedTokenRate > 0, "Discounted token rate must be greater than zero");

        owner = msg.sender;
        tokenRate = _tokenRate;
        discountedTokenRate = _discountedTokenRate;
    }

    /**
     * @dev Enables presale.
     */
    function startPresale() external onlyOwner {
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev Disables presale.
     */
    function endPresale() external onlyOwner {
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Allows the owner to add or remove priority addresses.
     * @param _address Address to update priority status.
     * @param _status Priority status to set (true or false).
     */
    function updatePriorityAddress(address _address, bool _status) external onlyOwner {
        priorityAddresses[_address] = _status;
    }

    /**
     * @dev Purchase tokens during presale. If the buyer is a priority address, they receive a discounted rate.
     */
    function purchaseTokens() external payable presaleIsActive {
        require(msg.value > 0, "Ether value must be greater than zero");

        uint256 rate = priorityAddresses[msg.sender] ? discountedTokenRate : tokenRate;
        uint256 tokensToPurchase = msg.value * rate;

        tokensPurchased[msg.sender] += tokensToPurchase;
        totalSoldTokens += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Withdraw Ether collected during presale to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
