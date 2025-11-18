"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase2-blockdag-networks.pages.dev
Prompt: Generate a Solidity contract for managing the BlockDAG token presale, including functions for purchasing with ETH, BNB, or USDT, and handling airdrops post-presale.
Generated: DETERMINISTIC_94ecc40c1b8a4498
Batch ID: 20250612_154752
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
 * @title BlockDAG Token Presale Contract
 * @dev This contract manages the presale of the BlockDAG token and post-presale airdrops.
 */
contract BlockDAGPresale {
    // Token details
    string public constant tokenName = "BlockDAG Token";
    string public constant tokenSymbol = "BDAG";
    uint256 public constant tokenDecimals = 18;

    // Presale parameters
    uint256 public constant presaleRate = 1000; // Tokens per ETH/BNB/USDT unit
    uint256 public presaleEndTime;

    // Owner address
    address public owner;

    // Token balance mapping for airdrops
    mapping(address => uint256) public balances;

    // Supported payment tokens
    address public constant USDT = 0xdAC17F958D2ee523a2206206994597C13D831ec7; // Example USDT contract address for Ethereum mainnet
    address public constant BNB = 0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB; // Example BNB contract address (placeholder for demonstration)

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Airdrop(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        _;
    }

    // Constructor
    constructor(uint256 _presaleDuration) {
        owner = msg.sender;
        presaleEndTime = block.timestamp + _presaleDuration;
    }

    /**
     * @dev Purchase tokens using ETH.
     */
    function purchaseWithETH() external payable presaleActive {
        require(msg.value > 0, "Amount must be greater than 0");
        uint256 tokenAmount = msg.value * presaleRate;
        balances[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Purchase tokens using BNB.
     * Note: This function assumes the use of a wrapped BNB (WBNB) or similar contract.
     */
    function purchaseWithBNB(uint256 bnbAmount) external presaleActive {
        require(bnbAmount > 0, "Amount must be greater than 0");

        // Transfer BNB from buyer to this contract
        require(
            IERC20(BNB).transferFrom(msg.sender, address(this), bnbAmount),
            "BNB transfer failed"
        );

        uint256 tokenAmount = bnbAmount * presaleRate;
        balances[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Purchase tokens using USDT.
     */
    function purchaseWithUSDT(uint256 usdtAmount) external presaleActive {
        require(usdtAmount > 0, "Amount must be greater than 0");

        // Transfer USDT from buyer to this contract
        require(
            IERC20(USDT).transferFrom(msg.sender, address(this), usdtAmount),
            "USDT transfer failed"
        );

        uint256 tokenAmount = usdtAmount * presaleRate;
        balances[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Airdrop tokens to users after presale ends.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts corresponding to recipients.
     */
    function performAirdrop(
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external onlyOwner presaleEnded {
        require(
            recipients.length == amounts.length,
            "Recipients and amounts length mismatch"
        );

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than 0");

            balances[recipients[i]] += amounts[i];
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Withdraw collected funds (ETH, BNB, USDT) to the contract owner's address.
     */
    function withdrawFunds() external onlyOwner presaleEnded {
        // Withdraw ETH
        uint256 ethBalance = address(this).balance;
        if (ethBalance > 0) {
            payable(owner).transfer(ethBalance);
        }

        // Withdraw BNB
        uint256 bnbBalance = IERC20(BNB).balanceOf(address(this));
        if (bnbBalance > 0) {
            require(
                IERC20(BNB).transfer(owner, bnbBalance),
                "BNB transfer failed"
            );
        }

        // Withdraw USDT
        uint256 usdtBalance = IERC20(USDT).balanceOf(address(this));
        if (usdtBalance > 0) {
            require(
                IERC20(USDT).transfer(owner, usdtBalance),
                "USDT transfer failed"
            );
        }
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
