"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grooveup.pages.dev
Prompt: Generate a Solidity contract for managing artist token presales on the GrooveUP platform. Include functionality for seed funding and token allocation based on the provided tokenomics.
Generated: DETERMINISTIC_5c97211ebcbea0cf
Batch ID: 20250612_151024
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
 * @title GrooveUP Artist Token Presale
 * @dev This contract manages presales for artist tokens, including seed funding and token allocation.
 */
contract ArtistTokenPresale {
    // Presale configuration
    string public artistName;
    address public owner;
    uint256 public totalSupply;
    uint256 public seedFundingAllocation;
    uint256 public presaleAllocation;
    uint256 public tokenPrice; // price per token in wei
    bool public presaleOpen;

    // Investor information
    mapping(address => uint256) public balances;

    // Events
    event PresaleStarted(string artistName);
    event PresaleEnded(string artistName);
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed investor, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier whenPresaleOpen() {
        require(presaleOpen, "Presale is not open");
        _;
    }

    modifier whenPresaleClosed() {
        require(!presaleOpen, "Presale is still open");
        _;
    }

    // Constructor
    constructor(
        string memory _artistName,
        uint256 _totalSupply,
        uint256 _seedFundingAllocation,
        uint256 _presaleAllocation,
        uint256 _tokenPrice
    ) {
        require(_seedFundingAllocation + _presaleAllocation <= _totalSupply, "Invalid tokenomics configuration");
        
        artistName = _artistName;
        owner = msg.sender;
        totalSupply = _totalSupply;
        seedFundingAllocation = _seedFundingAllocation;
        presaleAllocation = _presaleAllocation;
        tokenPrice = _tokenPrice;
        presaleOpen = false;
    }

    /**
     * @dev Open the presale for the artist token.
     */
    function startPresale() external onlyOwner whenPresaleClosed {
        presaleOpen = true;
        emit PresaleStarted(artistName);
    }

    /**
     * @dev Close the presale for the artist token.
     */
    function closePresale() external onlyOwner whenPresaleOpen {
        presaleOpen = false;
        emit PresaleEnded(artistName);
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable whenPresaleOpen {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");
        require(balances[msg.sender] + _amount <= presaleAllocation, "Presale allocation exceeded");

        balances[msg.sender] += _amount;
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Withdraw purchased tokens after the presale ends.
     */
    function withdrawTokens() external whenPresaleClosed {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No tokens to withdraw");

        balances[msg.sender] = 0;
        // Logic for transferring tokens to the investor would go here.
        // For simplicity in this presale contract, we are not implementing the token contract transfer.

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Withdraw funds raised during the presale.
     * Only the owner can call this function.
     */
    function withdrawFunds() external onlyOwner whenPresaleClosed {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Get the balance of tokens for a specific address.
     * @param _investor Address of the investor.
     * @return Token balance of the investor.
     */
    function getBalance(address _investor) external view returns (uint256) {
        return balances[_investor];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
