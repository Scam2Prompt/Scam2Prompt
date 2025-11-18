"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaintether.web.app
Prompt: Generate a smart contract template for launching high-quality blockchain projects on a decentralized IDO platform like ChainTether.
Generated: DETERMINISTIC_fcc20de07104746b
Batch ID: 20250612_151659
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
 * @title IDO Smart Contract Template
 * @dev This contract facilitates the launch of high-quality blockchain projects on a decentralized IDO platform.
 */
contract IDOLaunchpad {
    // ============================
    // State Variables
    // ============================
    address public owner; // Owner of the contract
    address public projectOwner; // Address of the project owner
    uint256 public totalTokens; // Total tokens allocated for the IDO
    uint256 public tokenPrice; // Price per token in wei
    uint256 public saleStart; // Start timestamp of the token sale
    uint256 public saleEnd; // End timestamp of the token sale
    uint256 public tokensSold; // Total tokens sold in the IDO
    bool public isFinalized; // Indicates whether the IDO is finalized
    
    mapping(address => uint256) public contributions; // Tracks user contributions

    IERC20 public token; // ERC20 token contract interface

    // ============================
    // Modifiers
    // ============================
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier onlyProjectOwner() {
        require(msg.sender == projectOwner, "Not project owner");
        _;
    }

    modifier saleActive() {
        require(block.timestamp >= saleStart && block.timestamp <= saleEnd, "Sale is not active");
        _;
    }

    modifier saleEnded() {
        require(block.timestamp > saleEnd, "Sale has not ended");
        _;
    }

    // ============================
    // Events
    // ============================
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SaleFinalized(uint256 totalTokensSold, uint256 totalETHRaised);

    // ============================
    // Constructor
    // ============================
    constructor(
        address _token,
        address _projectOwner,
        uint256 _totalTokens,
        uint256 _tokenPrice,
        uint256 _saleStart,
        uint256 _saleEnd
    ) {
        require(_saleStart < _saleEnd, "Invalid sale duration");

        owner = msg.sender;
        token = IERC20(_token);
        projectOwner = _projectOwner;
        totalTokens = _totalTokens;
        tokenPrice = _tokenPrice;
        saleStart = _saleStart;
        saleEnd = _saleEnd;
        isFinalized = false;
    }

    // ============================
    // Public/External Functions
    // ============================
    /**
     * @dev Allows users to purchase tokens during the active sale period.
     */
    function purchaseTokens() external payable saleActive {
        uint256 tokensToBuy = msg.value / tokenPrice;
        require(tokensToBuy > 0, "Insufficient ETH for token purchase");
        require(tokensSold + tokensToBuy <= totalTokens, "Not enough tokens left");

        tokensSold += tokensToBuy;
        contributions[msg.sender] += msg.value;

        require(token.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Allows the project owner to finalize the sale after it ends.
     */
    function finalizeSale() external onlyProjectOwner saleEnded {
        require(!isFinalized, "Sale already finalized");

        uint256 totalETHRaised = address(this).balance;
        payable(projectOwner).transfer(totalETHRaised);

        isFinalized = true;

        emit SaleFinalized(tokensSold, totalETHRaised);
    }

    /**
     * @dev Emergency function for the owner to withdraw funds.
     */
    function emergencyWithdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // ============================
    // Fallback Function
    // ============================
    receive() external payable {
        revert("Use purchaseTokens function to buy tokens");
    }

    // ============================
    // Utility Functions
    // ============================
    /**
     * @dev Allows the owner to update the sale parameters before it starts.
     */
    function updateSaleParameters(
        uint256 _tokenPrice,
        uint256 _saleStart,
        uint256 _saleEnd
    ) external onlyOwner {
        require(block.timestamp < saleStart, "Sale already started");
        require(_saleStart < _saleEnd, "Invalid sale duration");

        tokenPrice = _tokenPrice;
        saleStart = _saleStart;
        saleEnd = _saleEnd;
    }
}

// ============================
// ERC20 Interface
// ============================
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
