"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint27-air-drop.vercel.app
Prompt: Provide an example of how to implement a presale token purchase and claim functionality using the "Buy Presale" and "Claim Presale" features described on the webpage.
Generated: DETERMINISTIC_ed7db81f1e9391ff
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title PresaleTokenContract
 * @dev A smart contract for presale token purchase and claim functionality.
 */
contract PresaleTokenContract {
    // Address of the token to be sold in the presale
    IERC20 public presaleToken;

    // Owner of the contract
    address public owner;

    // Presale price per token in wei
    uint256 public presalePrice;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Mapping of addresses to the number of tokens purchased
    mapping(address => uint256) public purchasedTokens;

    // Events for logging
    event PresalePurchase(address indexed buyer, uint256 amount);
    event PresaleClaim(address indexed claimer, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to check if presale is active.
     */
    modifier presaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale token contract.
     * @param _presaleToken Address of the presale token contract.
     * @param _presalePrice Price per token in wei.
     * @param _presaleStart Start timestamp of the presale.
     * @param _presaleEnd End timestamp of the presale.
     */
    constructor(
        address _presaleToken,
        uint256 _presalePrice,
        uint256 _presaleStart,
        uint256 _presaleEnd
    ) {
        require(_presaleToken != address(0), "Invalid token address");
        require(_presalePrice > 0, "Presale price must be greater than zero");
        require(_presaleStart < _presaleEnd, "Start must be earlier than end");

        presaleToken = IERC20(_presaleToken);
        presalePrice = _presalePrice;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase presale tokens.
     * @param _amount Number of tokens to purchase.
     */
    function buyPresale(uint256 _amount) external payable presaleActive {
        uint256 cost = _amount * presalePrice;
        require(msg.value == cost, "Incorrect ETH amount sent");

        // Record purchased tokens for the sender
        purchasedTokens[msg.sender] += _amount;

        emit PresalePurchase(msg.sender, _amount);
    }

    /**
     * @dev Function to claim purchased presale tokens after presale ends.
     */
    function claimPresale() external {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        uint256 amountToClaim = purchasedTokens[msg.sender];
        require(amountToClaim > 0, "No tokens to claim");

        // Reset purchased tokens for the sender
        purchasedTokens[msg.sender] = 0;

        // Transfer tokens to the sender
        require(
            presaleToken.transfer(msg.sender, amountToClaim),
            "Token transfer failed"
        );

        emit PresaleClaim(msg.sender, amountToClaim);
    }

    /**
     * @dev Function for the owner to withdraw collected ETH after presale ends.
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Function for the owner to reclaim unused tokens after presale ends.
     */
    function reclaimTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        uint256 remainingTokens = presaleToken.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to reclaim");

        require(
            presaleToken.transfer(owner, remainingTokens),
            "Token transfer failed"
        );
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
