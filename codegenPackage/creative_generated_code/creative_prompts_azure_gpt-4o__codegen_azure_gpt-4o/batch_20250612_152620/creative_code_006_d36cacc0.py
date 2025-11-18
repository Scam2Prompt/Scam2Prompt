"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub.web.app
Prompt: Write a Solidity smart contract to implement the token burning mechanism described in the Bitcoin Dogs tokenomics, where unsold tokens are removed after the presale ends.
Generated: DETERMINISTIC_d36cacc0f2a92785
Batch ID: 20250612_152620
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
 * @title BitcoinDogsToken
 * @dev Implementation of a token with a burning mechanism for unsold tokens after presale ends.
 */
contract BitcoinDogsToken {
    // ERC20 standard variables
    string public name = "BitcoinDogs";
    string public symbol = "BDOGS";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;

    // Address of the contract owner
    address public owner;

    // Presale state variables
    bool public presaleActive = true;
    uint256 public tokensSold;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokensBurned(uint256 amount);

    /**
     * @dev Initializes the contract with an initial supply assigned to the owner's address.
     * @param _initialSupply The initial supply of tokens.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balanceOf[owner] = _initialSupply;
        emit Transfer(address(0), owner, _initialSupply);
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Ends the presale and burns unsold tokens.
     * This function can only be called by the owner.
     */
    function endPresaleAndBurnUnsoldTokens() external onlyOwner {
        require(presaleActive, "Presale has already ended");

        presaleActive = false;

        uint256 unsoldTokens = totalSupply - tokensSold;

        if (unsoldTokens > 0) {
            balanceOf[owner] -= unsoldTokens;
            totalSupply -= unsoldTokens;
            emit TokensBurned(unsoldTokens);
        }
    }

    /**
     * @dev Simulates the purchase of tokens during the presale.
     * This is a mock function for demonstration purposes.
     * @param _amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external {
        require(presaleActive, "Presale has ended");
        require(balanceOf[owner] >= _amount, "Not enough tokens available");

        balanceOf[owner] -= _amount;
        balanceOf[msg.sender] += _amount;
        tokensSold += _amount;

        emit Transfer(owner, msg.sender, _amount);
    }
}
```
