"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ape-launchpad.vercel.app
Prompt: Generate code for a smart contract that supports IDO participation, ensuring integration with the wallet connection process described on Ape Terminal.
Generated: DETERMINISTIC_783177a8802e8836
Batch ID: 20250612_153526
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
 * @title IDOParticipation
 * @dev A smart contract for Initial DEX Offering (IDO) participation, integrated with wallet connections.
 *      Participants can buy tokens during the IDO event.
 */
contract IDOParticipation {
    // Address of the IDO token
    address public tokenAddress;

    // Address of the IDO organizer
    address public organizer;

    // Token price in wei (example: 1 token = 0.01 ETH)
    uint256 public tokenPrice;

    // Total tokens available for sale
    uint256 public totalTokens;

    // Tokens sold so far
    uint256 public tokensSold;

    // Mapping to track participant contributions
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the organizer
    modifier onlyOrganizer() {
        require(msg.sender == organizer, "Only organizer can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the IDO settings.
     * @param _tokenAddress Address of the token being sold.
     * @param _tokenPrice Price of one token in wei.
     * @param _totalTokens Total tokens available for the IDO.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _totalTokens
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        tokenAddress = _tokenAddress;
        organizer = msg.sender; // Set the organizer to the contract deployer
        tokenPrice = _tokenPrice;
        totalTokens = _totalTokens;
    }

    /**
     * @dev Function to purchase tokens during the IDO.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "ETH value must be greater than zero");

        // Calculate the number of tokens to purchase
        uint256 tokensToBuy = msg.value / tokenPrice;

        // Ensure there are enough tokens available
        require(tokensToBuy <= remainingTokens(), "Not enough tokens available");

        // Update state
        tokensSold += tokensToBuy;
        contributions[msg.sender] += tokensToBuy;

        // Transfer purchased tokens to the buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokensToBuy),
            "Token transfer failed"
        );

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Function for the organizer to withdraw funds collected during the IDO.
     */
    function withdrawFunds() external onlyOrganizer {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = organizer.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Helper function to check the remaining tokens available for sale.
     * @return Remaining tokens available.
     */
    function remainingTokens() public view returns (uint256) {
        return totalTokens - tokensSold;
    }

    /**
     * @dev Function for the organizer to add more tokens to the IDO pool.
     * @param _additionalTokens Number of tokens to add.
     */
    function addTokens(uint256 _additionalTokens) external onlyOrganizer {
        require(_additionalTokens > 0, "Additional tokens must be greater than zero");
        totalTokens += _additionalTokens;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
