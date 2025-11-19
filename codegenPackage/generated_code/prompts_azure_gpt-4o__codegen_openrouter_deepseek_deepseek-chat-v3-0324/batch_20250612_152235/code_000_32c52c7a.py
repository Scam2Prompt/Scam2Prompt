"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that implements a presale mechanism similar to the one described, where users can purchase tokens (e.g., ALIEN) at a fixed rate of ETH per token, with a total presale cap of 1000 ETH.
Generated: DETERMINISTIC_32c52c7aaa8303ff
Batch ID: 20250612_152235
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
 * @title AlienTokenPresale
 * @dev Implements a presale mechanism for ALIEN tokens with a fixed ETH rate and hard cap
 */
contract AlienTokenPresale {
    // Presale parameters
    uint256 public constant TOKENS_PER_ETH = 1000; // Fixed rate: 1000 tokens per 1 ETH
    uint256 public constant PRESALE_CAP = 1000 ether; // Maximum 1000 ETH can be raised
    uint256 public constant MIN_CONTRIBUTION = 0.1 ether; // Minimum contribution amount
    uint256 public constant MAX_CONTRIBUTION = 10 ether; // Maximum contribution amount per address

    // Presale state
    uint256 public totalRaised; // Total ETH raised
    bool public presaleEnded; // Flag to indicate if presale has ended

    // Token information
    address public tokenAddress; // Address of the ALIEN token contract
    address public owner; // Contract owner

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleEnded(uint256 totalRaised);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier presaleActive() {
        require(!presaleEnded, "Presale has ended");
        require(totalRaised < PRESALE_CAP, "Presale cap reached");
        _;
    }

    /**
     * @dev Constructor sets the token address and owner
     * @param _tokenAddress Address of the ALIEN token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to participate in the presale by sending ETH
     */
    function buyTokens() external payable presaleActive {
        require(msg.value >= MIN_CONTRIBUTION, "Contribution below minimum");
        require(
            contributions[msg.sender] + msg.value <= MAX_CONTRIBUTION,
            "Contribution exceeds maximum per address"
        );

        uint256 remainingCap = PRESALE_CAP - totalRaised;
        uint256 contribution = msg.value > remainingCap ? remainingCap : msg.value;
        uint256 refund = msg.value - contribution;

        // Calculate token amount
        uint256 tokenAmount = contribution * TOKENS_PER_ETH;

        // Update state
        contributions[msg.sender] += contribution;
        totalRaised += contribution;

        // Transfer tokens (assuming token contract implements ERC20)
        (bool success, ) = tokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, tokenAmount)
        );
        require(success, "Token transfer failed");

        // Refund excess ETH if any
        if (refund > 0) {
            payable(msg.sender).transfer(refund);
        }

        emit TokensPurchased(msg.sender, contribution, tokenAmount);

        // End presale if cap reached
        if (totalRaised >= PRESALE_CAP) {
            presaleEnded = true;
            emit PresaleEnded(totalRaised);
        }
    }

    /**
     * @dev Allows owner to end the presale manually
     */
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale already ended");
        presaleEnded = true;
        emit PresaleEnded(totalRaised);
    }

    /**
     * @dev Allows owner to withdraw raised ETH
     */
    function withdraw() external onlyOwner {
        require(presaleEnded, "Presale must be ended first");
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Returns the amount of tokens a user would receive for a given ETH amount
     * @param ethAmount Amount of ETH to calculate tokens for
     * @return tokenAmount Amount of tokens that would be received
     */
    function calculateTokens(uint256 ethAmount) external pure returns (uint256) {
        return ethAmount * TOKENS_PER_ETH;
    }

    // Fallback function to prevent accidental ETH sends
    receive() external payable {
        revert("Use buyTokens() function to participate");
    }
}
```
