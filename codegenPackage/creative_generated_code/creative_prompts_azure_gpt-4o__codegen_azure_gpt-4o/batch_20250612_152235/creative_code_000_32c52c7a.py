"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that implements a presale mechanism similar to the one described, where users can purchase tokens (e.g., ALIEN) at a fixed rate of ETH per token, with a total presale cap of 1000 ETH.
Generated: DETERMINISTIC_32c52c7aaa8303ff
Batch ID: 20250612_152235
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
 * @title PresaleContract
 * @dev This contract implements a presale mechanism where users can purchase tokens (ALIEN) 
 *      at a fixed rate in ETH. The presale has a cap of 1000 ETH.
 */
contract PresaleContract {
    // Token name and symbol
    string public constant TOKEN_NAME = "ALIEN";
    string public constant TOKEN_SYMBOL = "ALIEN";

    // Total ETH cap for the presale
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Fixed rate of ETH per token
    uint256 public constant RATE = 100; // 1 ETH = 100 ALIEN tokens

    // Owner of the contract
    address public owner;

    // Total ETH raised so far
    uint256 public totalEthRaised;

    // Mapping to keep track of token balances for each address
    mapping(address => uint256) public balances;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 ethSpent, uint256 tokensReceived);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "PresaleContract: Not the contract owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase ALIEN tokens during the presale.
     *      The contract ensures the presale cap is not exceeded.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "PresaleContract: ETH amount must be greater than 0");
        require(totalEthRaised + msg.value <= PRESALE_CAP, "PresaleContract: Presale cap exceeded");

        // Calculate the number of tokens to be purchased
        uint256 tokensToReceive = msg.value * RATE;

        // Update state variables
        balances[msg.sender] += tokensToReceive;
        totalEthRaised += msg.value;

        // Emit an event for the token purchase
        emit TokensPurchased(msg.sender, msg.value, tokensToReceive);
    }

    /**
     * @dev Allows the owner to withdraw the ETH collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "PresaleContract: No funds available for withdrawal");

        // Transfer the collected funds to the owner's address
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "PresaleContract: Withdrawal failed");
    }

    /**
     * @dev Emergency function: Allows the owner to pause the presale if needed.
     *      This function can include additional logic for pausing if required.
     */
    function pausePresale() external onlyOwner {
        // Example placeholder function for emergency logic
        revert("PresaleContract: Presale paused by owner");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("PresaleContract: Direct ETH transfers not allowed");
    }

    receive() external payable {
        revert("PresaleContract: Use purchaseTokens() to buy tokens");
    }
}
```
