"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wepestreetpepe-new.pages.dev
Prompt: Generate code to simulate a cryptocurrency presale transaction for tokens like "Wall Street Pepe Token" (WEPE), ensuring compliance with Ethereum-based smart contracts.
Generated: DETERMINISTIC_526c14dd95ebb30c
Batch ID: 20250612_150030
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
 * @title Wall Street Pepe Token (WEPE) Presale Contract
 * @dev This contract handles the presale transactions for WEPE tokens.
 *      Built with best practices for security and efficiency.
 */
contract WEPEPresale {
    // Token variables
    uint256 public constant TOKEN_PRICE = 0.001 ether; // Price per token
    uint256 public constant MAX_TOKENS_PER_ADDRESS = 1000; // Max tokens per buyer
    uint256 public constant TOTAL_SUPPLY = 1000000; // Total tokens available for presale

    // Presale state variables
    address public owner;
    uint256 public tokensSold;
    bool public presaleActive;
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStarted();
    event PresaleEnded();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action.");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active.");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
        presaleActive = false; // Presale starts as inactive
    }

    /**
     * @dev Start the presale.
     *      Only callable by the owner.
     */
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active.");
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev End the presale.
     *      Only callable by the owner.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active.");
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Purchase tokens during the presale.
     *      Users can buy tokens as long as presale is active and supply exists.
     * @param tokenAmount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 tokenAmount) external payable presaleIsActive {
        require(tokenAmount > 0, "Token amount must be greater than 0.");
        require(
            msg.value == tokenAmount * TOKEN_PRICE,
            "Incorrect Ether sent for purchase."
        );
        require(
            balances[msg.sender] + tokenAmount <= MAX_TOKENS_PER_ADDRESS,
            "Token purchase exceeds maximum allowed per address."
        );
        require(
            tokensSold + tokenAmount <= TOTAL_SUPPLY,
            "Not enough tokens available for purchase."
        );

        // Update balances and sold tokens
        balances[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Withdraw collected funds from the presale.
     *      Only callable by the owner after presale ends.
     */
    function withdrawFunds() external onlyOwner {
        require(!presaleActive, "Cannot withdraw funds while presale is active.");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Fallback function to prevent sending Ether directly to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed.");
    }

    /**
     * @dev Helper function to check the contract's Ether balance.
     * @return Contract's Ether balance.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
