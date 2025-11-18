"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Develop a smart contract in Solidity to handle the JESSE token presale, including the exchange rate of 0.1 BASE = 99,500 JESSE and the total supply limit.
Generated: DETERMINISTIC_05f1ad46066d7dd6
Batch ID: 20250612_152656
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
 * @title JESSE Token Presale Smart Contract
 * @author <Your Name>
 * @notice This contract handles the JESSE token presale with a fixed exchange rate and total supply limit.
 */
contract JesseTokenPresale {
    // Token parameters
    string public constant name = "JESSE Token";
    string public constant symbol = "JESSE";
    uint8 public constant decimals = 18;

    // Total supply limit for presale
    uint256 public constant totalSupplyLimit = 1000000 * (10 ** decimals); // 1,000,000 JESSE tokens
    uint256 public totalSupply;

    // Exchange rate: 0.1 BASE = 99,500 JESSE
    uint256 public constant rate = 99500; // JESSE tokens per BASE unit (scaled by BASE's decimals)

    // Owner of the contract
    address public owner;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Event emitted for token purchases
    event TokensPurchased(address indexed buyer, uint256 amountBASE, uint256 amountJESSE);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Modifier to ensure total supply does not exceed the limit
    modifier supplyCheck(uint256 amount) {
        require(totalSupply + amount <= totalSupplyLimit, "Purchase exceeds total supply limit");
        _;
    }

    // Contract constructor
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @notice Public function to purchase JESSE tokens during presale
     * @param amountBASE The amount of BASE tokens to spend
     */
    function purchaseTokens(uint256 amountBASE) external payable supplyCheck(amountBASE * rate) {
        // Validate payment
        require(msg.value == amountBASE, "Sent Ether amount must match specified BASE amount");

        // Calculate JESSE token amount based on exchange rate
        uint256 amountJESSE = amountBASE * rate;

        // Update total supply and buyer's balance
        totalSupply += amountJESSE;
        balances[msg.sender] += amountJESSE;

        // Emit purchase event
        emit TokensPurchased(msg.sender, amountBASE, amountJESSE);
    }

    /**
     * @notice Withdraw ETH collected during presale to the owner's address
     */
    function withdrawETH() external onlyOwner {
        uint256 contractBalance = address(this).balance;

        require(contractBalance > 0, "No Ether available for withdrawal");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @notice Fallback function to reject direct Ether transfers
     */
    fallback() external payable {
        revert("Direct transfers are not allowed, use purchaseTokens()");
    }

    /**
     * @notice Receive function to reject direct Ether transfers
     */
    receive() external payable {
        revert("Direct transfers are not allowed, use purchaseTokens()");
    }
}
```
