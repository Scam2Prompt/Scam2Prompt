"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sealanapresales.pages.dev
Prompt: Write a Solidity smart contract to facilitate the presale of $SEAL tokens, incorporating multi-token payment options (ETH, SOL, USDT, USDC) as described on the Sealana Presale site.
Generated: DETERMINISTIC_b2ace3bd68ce1ef7
Batch ID: 20250612_151531
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
 * @title SealanaPresale
 * @dev A contract to manage the presale of $SEAL tokens with multi-token payment options.
 */
contract SealanaPresale {
    // Address of the $SEAL token contract
    address public sealTokenAddress;

    // Owner of the presale contract
    address public owner;

    // Price of 1 $SEAL token in ETH (can be adjusted based on token type)
    uint256 public sealTokenPriceInETH;

    // Supported ERC20 payment tokens and their conversion rates (relative to $SEAL tokens)
    mapping(address => uint256) public tokenExchangeRates;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost, string paymentType);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _sealTokenAddress,
        uint256 _sealTokenPriceInETH,
        address[] memory _acceptedTokens,
        uint256[] memory _exchangeRates
    ) {
        require(_sealTokenAddress != address(0), "Invalid token address");
        require(_acceptedTokens.length == _exchangeRates.length, "Mismatched inputs");

        sealTokenAddress = _sealTokenAddress;
        owner = msg.sender;
        sealTokenPriceInETH = _sealTokenPriceInETH;

        // Populate the exchange rates
        for (uint256 i = 0; i < _acceptedTokens.length; i++) {
            tokenExchangeRates[_acceptedTokens[i]] = _exchangeRates[i];
        }
    }

    /**
     * @dev Allows the owner to update the price of $SEAL tokens in ETH.
     * @param _newPrice New price for $SEAL tokens in ETH.
     */
    function updateSealTokenPrice(uint256 _newPrice) external onlyOwner {
        sealTokenPriceInETH = _newPrice;
    }

    /**
     * @dev Allows the owner to update exchange rates for ERC20 tokens.
     * @param _token Address of the ERC20 token.
     * @param _rate New exchange rate for the token.
     */
    function updateExchangeRate(address _token, uint256 _rate) external onlyOwner {
        tokenExchangeRates[_token] = _rate;
    }

    /**
     * @dev Facilitates purchase of $SEAL tokens using ETH.
     */
    function purchaseWithETH() external payable {
        require(msg.value > 0, "No ETH sent");

        // Calculate the number of $SEAL tokens to transfer
        uint256 tokenAmount = (msg.value * 1 ether) / sealTokenPriceInETH;

        // Transfer tokens to buyer
        require(
            IERC20(sealTokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        emit TokensPurchased(msg.sender, tokenAmount, msg.value, "ETH");
    }

    /**
     * @dev Facilitates purchase of $SEAL tokens using an accepted ERC20 token.
     * @param _paymentToken Address of the ERC20 token used for payment.
     * @param _paymentAmount Amount of ERC20 tokens sent to purchase $SEAL tokens.
     */
    function purchaseWithERC20(address _paymentToken, uint256 _paymentAmount) external {
        require(tokenExchangeRates[_paymentToken] > 0, "Unsupported payment token");
        require(_paymentAmount > 0, "Invalid payment amount");

        // Calculate the number of $SEAL tokens to transfer
        uint256 tokenAmount = (_paymentAmount * 1 ether) / tokenExchangeRates[_paymentToken];

        // Transfer payment token from buyer to contract
        require(
            IERC20(_paymentToken).transferFrom(msg.sender, address(this), _paymentAmount),
            "Payment token transfer failed"
        );

        // Transfer $SEAL tokens to buyer
        require(
            IERC20(sealTokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        emit TokensPurchased(msg.sender, tokenAmount, _paymentAmount, "ERC20");
    }

    /**
     * @dev Allows the owner to withdraw collected ETH from the presale.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw ERC20 tokens collected from the presale.
     * @param _token Address of the ERC20 token to withdraw.
     */
    function withdrawERC20(address _token) external onlyOwner {
        uint256 balance = IERC20(_token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(
            IERC20(_token).transfer(owner, balance),
            "ERC20 withdrawal failed"
        );
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
