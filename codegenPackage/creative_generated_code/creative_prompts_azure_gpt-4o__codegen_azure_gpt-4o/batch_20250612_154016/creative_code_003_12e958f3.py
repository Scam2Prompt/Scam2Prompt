"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Write a smart contract in Solidity to handle the fair-launch mechanism for coins, ensuring no presale or team allocation, as outlined on the Fun Virtuals Agent platform.
Generated: DETERMINISTIC_12e958f3b65ae31e
Batch ID: 20250612_154016
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
 * @title FairLaunchToken
 * @dev Smart contract for fair-launch mechanism ensuring no presale or team allocation.
 */
contract FairLaunchToken {
    string public name = "FairLaunchToken";
    string public symbol = "FLT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for token balances
    mapping(address => uint256) public balanceOf;
    // Mapping for allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract (deployment address)
    address public owner;

    // Prevent reentrancy attacks
    bool private locked = false;

    /**
     * @dev Modifier to ensure only the owner can execute certain functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to prevent reentrancy attacks.
     */
    modifier noReentrant() {
        require(!locked, "Reentrant call detected");
        locked = true;
        _;
        // Reset lock state after function completion
        locked = false;
    }

    /**
     * @dev Constructor to initialize contract and mint initial supply equally to all participants.
     * Fair-launch ensures that everyone gets an equal opportunity to buy tokens.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        
        // Mint all tokens to the contract initially
        balanceOf[address(this)] = totalSupply;
        emit Transfer(address(0), address(this), totalSupply);
    }

    /**
     * @dev Distribute tokens during fair launch.
     * Users can call this function to purchase tokens from the contract.
     */
    function buyTokens() external payable noReentrant {
        require(msg.value > 0, "No ETH sent");
        require(balanceOf[address(this)] > 0, "No tokens left for distribution");

        // Calculate token amount based on a fixed price (1 token = 0.01 ETH)
        uint256 tokensToDistribute = msg.value * 100;

        require(tokensToDistribute <= balanceOf[address(this)], "Not enough tokens available");

        // Transfer tokens to sender
        balanceOf[address(this)] -= tokensToDistribute;
        balanceOf[msg.sender] += tokensToDistribute;

        emit Transfer(address(this), msg.sender, tokensToDistribute);
    }

    /**
     * @dev Transfer tokens between addresses.
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        // Perform transfer
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve spender to transfer tokens on behalf of the sender.
     */
    function approve(address _spender, uint256 _value) external returns (bool success) {
        require(_spender != address(0), "Cannot approve zero address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another with allowance mechanism.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        // Perform transfer
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;

        // Reduce allowance
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Withdraw ETH collected in the contract to the owner address.
     */
    function withdrawETH() external onlyOwner noReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Fallback function to receive ETH directly.
     */
    receive() external payable {
        // Allow receiving ETH for token purchases
    }
}
```
