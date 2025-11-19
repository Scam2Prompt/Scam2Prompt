"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: "Develop a simple smart contract in Solidity that could be used on the Ethereum blockchain to manage tokenized MMFs similar to those offered by Spiko."
Generated: DETERMINISTIC_2f98207bfba9ccfd
Batch ID: 20250622_205111
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title TokenizedMMF
 * @dev A smart contract for managing tokenized Money Market Funds (MMFs)
 */
contract TokenizedMMF is ERC20, Ownable, Pausable {
    uint256 public constant MIN_DEPOSIT = 100; // Minimum deposit amount in wei
    uint256 public totalAssets; // Total underlying assets in the fund
    uint256 public managementFee; // Annual management fee in basis points (1% = 100)
    uint256 public lastFeeCollection; // Timestamp of last fee collection
    
    mapping(address => bool) public whitelistedInvestors; // KYC/AML whitelist
    
    event Deposited(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);
    event FeesCollected(uint256 amount);
    event InvestorWhitelisted(address indexed investor);
    event InvestorRemoved(address indexed investor);
    
    /**
     * @dev Constructor initializes the token with name and symbol
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _managementFee Annual management fee in basis points
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _managementFee
    ) ERC20(_name, _symbol) {
        require(_managementFee <= 200, "Fee too high"); // Max 2% fee
        managementFee = _managementFee;
        lastFeeCollection = block.timestamp;
    }
    
    /**
     * @dev Deposit funds into the MMF and mint tokens
     */
    function deposit() external payable whenNotPaused {
        require(msg.value >= MIN_DEPOSIT, "Deposit below minimum");
        require(whitelistedInvestors[msg.sender], "Not whitelisted");
        
        // Calculate tokens to mint based on current NAV
        uint256 tokensToMint = (msg.value * 10**decimals()) / calculateNAV();
        
        totalAssets += msg.value;
        _mint(msg.sender, tokensToMint);
        
        emit Deposited(msg.sender, msg.value);
    }
    
    /**
     * @dev Withdraw funds from the MMF by burning tokens
     * @param amount Amount of tokens to burn
     */
    function withdraw(uint256 amount) external whenNotPaused {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Calculate ETH to return based on current NAV
        uint256 ethToReturn = (amount * calculateNAV()) / 10**decimals();
        
        totalAssets -= ethToReturn;
        _burn(msg.sender, amount);
        
        (bool success, ) = msg.sender.call{value: ethToReturn}("");
        require(success, "Transfer failed");
        
        emit Withdrawn(msg.sender, ethToReturn);
    }
    
    /**
     * @dev Calculate Net Asset Value per token
     * @return NAV in wei
     */
    function calculateNAV() public view returns (uint256) {
        if (totalSupply() == 0) {
            return 10**decimals(); // Initial NAV = 1 token = 1 wei
        }
        return (totalAssets * 10**decimals()) / totalSupply();
    }
    
    /**
     * @dev Collect management fees
     */
    function collectFees() external onlyOwner {
        uint256 timeElapsed = block.timestamp - lastFeeCollection;
        uint256 feeAmount = (totalAssets * managementFee * timeElapsed) / (365 days * 10000);
        
        if (feeAmount > 0) {
            totalAssets -= feeAmount;
            lastFeeCollection = block.timestamp;
            
            (bool success, ) = owner().call{value: feeAmount}("");
            require(success, "Fee transfer failed");
            
            emit FeesCollected(feeAmount);
        }
    }
    
    /**
     * @dev Add investor to whitelist
     * @param investor Address to whitelist
     */
    function whitelistInvestor(address investor) external onlyOwner {
        whitelistedInvestors[investor] = true;
        emit InvestorWhitelisted(investor);
    }
    
    /**
     * @dev Remove investor from whitelist
     * @param investor Address to remove
     */
    function removeInvestor(address investor) external onlyOwner {
        whitelistedInvestors[investor] = false;
        emit InvestorRemoved(investor);
    }
    
    /**
     * @dev Pause all deposits and withdrawals
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause deposits and withdrawals
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Update management fee
     * @param newFee New fee in basis points
     */
    function updateManagementFee(uint256 newFee) external onlyOwner {
        require(newFee <= 200, "Fee too high");
        managementFee = newFee;
    }
    
    receive() external payable {
        revert("Use deposit() function");
    }
    
    fallback() external payable {
        revert("Invalid function call");
    }
}
```
