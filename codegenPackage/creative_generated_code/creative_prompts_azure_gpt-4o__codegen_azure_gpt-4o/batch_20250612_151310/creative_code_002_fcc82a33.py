"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicat-claims.pages.dev
Prompt: Create a smart contract in Solidity that implements a presale mechanism for an ERC20 token, allowing users to purchase tokens using ETH, USDT, or BNB, as detailed on the KAI website.
Generated: DETERMINISTIC_fcc82a332ea687a8
Batch ID: 20250612_151310
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

// Import OpenZeppelin's SafeERC20 and IERC20 for token operations
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenPresale {
    using SafeERC20 for IERC20;

    // Address of the ERC20 token being sold
    IERC20 public presaleToken;

    // Accepted tokens for payment
    IERC20 public usdtToken;
    address public bnbToken = 0xBnbTokenAddress; // Replace with the actual BNB token address

    // Presale parameters
    uint256 public rateETH; // Number of tokens per ETH
    uint256 public rateUSDT; // Number of tokens per USDT
    uint256 public rateBNB; // Number of tokens per BNB

    // Presale state
    address public owner;
    uint256 public totalTokensSold;

    // Events
    event Purchase(address indexed buyer, uint256 amount, string paymentMethod);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(
        address _presaleToken,
        address _usdtToken,
        uint256 _rateETH,
        uint256 _rateUSDT,
        uint256 _rateBNB
    ) {
        require(_presaleToken != address(0), "Invalid presale token address");
        require(_usdtToken != address(0), "Invalid USDT token address");
        require(_rateETH > 0 && _rateUSDT > 0 && _rateBNB > 0, "Invalid rates");

        presaleToken = IERC20(_presaleToken);
        usdtToken = IERC20(_usdtToken);
        rateETH = _rateETH;
        rateUSDT = _rateUSDT;
        rateBNB = _rateBNB;
        owner = msg.sender;
    }

    // Function to purchase tokens using ETH
    function buyTokensWithETH() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        uint256 tokenAmount = msg.value * rateETH;
        require(
            presaleToken.balanceOf(address(this)) >= tokenAmount,
            "Not enough tokens available for sale"
        );

        presaleToken.safeTransfer(msg.sender, tokenAmount);
        totalTokensSold += tokenAmount;

        emit Purchase(msg.sender, tokenAmount, "ETH");
    }

    // Function to purchase tokens using USDT
    function buyTokensWithUSDT(uint256 usdtAmount) external {
        require(usdtAmount > 0, "USDT amount must be greater than zero");

        uint256 tokenAmount = usdtAmount * rateUSDT;
        require(
            presaleToken.balanceOf(address(this)) >= tokenAmount,
            "Not enough tokens available for sale"
        );

        usdtToken.safeTransferFrom(msg.sender, address(this), usdtAmount);
        presaleToken.safeTransfer(msg.sender, tokenAmount);
        totalTokensSold += tokenAmount;

        emit Purchase(msg.sender, tokenAmount, "USDT");
    }

    // Function to purchase tokens using BNB
    function buyTokensWithBNB(uint256 bnbAmount) external {
        require(bnbAmount > 0, "BNB amount must be greater than zero");

        uint256 tokenAmount = bnbAmount * rateBNB;
        require(
            presaleToken.balanceOf(address(this)) >= tokenAmount,
            "Not enough tokens available for sale"
        );

        IERC20(bnbToken).safeTransferFrom(msg.sender, address(this), bnbAmount);
        presaleToken.safeTransfer(msg.sender, tokenAmount);
        totalTokensSold += tokenAmount;

        emit Purchase(msg.sender, tokenAmount, "BNB");
    }

    // Function for the owner to withdraw collected funds
    function withdrawFunds(address payable recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");

        uint256 ethBalance = address(this).balance;
        uint256 usdtBalance = usdtToken.balanceOf(address(this));
        uint256 bnbBalance = IERC20(bnbToken).balanceOf(address(this));

        if (ethBalance > 0) {
            recipient.transfer(ethBalance);
        }
        if (usdtBalance > 0) {
            usdtToken.safeTransfer(recipient, usdtBalance);
        }
        if (bnbBalance > 0) {
            IERC20(bnbToken).safeTransfer(recipient, bnbBalance);
        }
    }

    // Function for the owner to withdraw unsold tokens
    function withdrawUnsoldTokens(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");

        uint256 unsoldTokens = presaleToken.balanceOf(address(this));
        presaleToken.safeTransfer(recipient, unsoldTokens);
    }

    // Function to update presale rates
    function updateRates(
        uint256 newRateETH,
        uint256 newRateUSDT,
        uint256 newRateBNB
    ) external onlyOwner {
        require(
            newRateETH > 0 && newRateUSDT > 0 && newRateBNB > 0,
            "Rates must be greater than zero"
        );

        rateETH = newRateETH;
        rateUSDT = newRateUSDT;
        rateBNB = newRateBNB;
    }
}
```
