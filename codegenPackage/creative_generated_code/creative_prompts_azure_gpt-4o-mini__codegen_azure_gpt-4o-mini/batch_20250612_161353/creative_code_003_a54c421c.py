"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beckeerererer.pages.dev
Prompt: Provide an example of how to implement a presale mechanism for a cryptocurrency token with a cap, similar to the BCKR presale model.
Generated: DETERMINISTIC_a54c421c6154773f
Batch ID: 20250612_161353
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

contract PresaleToken {
    string public name = "PresaleToken";
    string public symbol = "PST";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    
    uint256 public presaleCap; // Maximum cap for the presale in wei
    uint256 public tokensSold; // Total tokens sold in presale
    address public owner; // Owner of the contract
    bool public presaleActive; // Status of the presale

    mapping(address => uint256) public balances; // User balances
    mapping(address => uint256) public contributions; // User contributions

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the presale token
    constructor(uint256 _presaleCap) {
        require(_presaleCap > 0, "Cap must be greater than zero");
        presaleCap = _presaleCap;
        owner = msg.sender;
        presaleActive = true;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 tokenAmount) public payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(tokensSold + tokenAmount <= presaleCap, "Presale cap exceeded");
        
        // Update state variables
        tokensSold += tokenAmount;
        balances[msg.sender] += tokenAmount;
        contributions[msg.sender] += msg.value;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function for the owner to end the presale
    function endPresale() public onlyOwner {
        presaleActive = false;
        emit PresaleEnded();
    }

    // Function for the owner to withdraw funds
    function withdrawFunds() public onlyOwner {
        require(!presaleActive, "Presale must be ended to withdraw");
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to prevent ETH from being sent directly to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
