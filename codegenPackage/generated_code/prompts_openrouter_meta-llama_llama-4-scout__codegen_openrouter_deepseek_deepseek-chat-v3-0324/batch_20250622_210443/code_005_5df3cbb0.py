"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a simple game using a library like Unity or Unreal Engine that simulates meme market trading, similar to Meme Moguls' gameplay features.
Generated: DETERMINISTIC_5df3cbb089c02d83
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;

public class MemeMarketGame : MonoBehaviour
{
    [System.Serializable]
    public class MemeAsset
    {
        public string name;
        public Sprite image;
        public float basePrice;
        public float volatility; // How much the price can change
        public float currentPrice;
        public int ownedQuantity;
    }

    public List<MemeAsset> memeAssets = new List<MemeAsset>();
    public float playerBalance = 1000f; // Starting balance

    public Transform memeShopContent;
    public GameObject memeShopItemPrefab;
    public Transform portfolioContent;
    public GameObject portfolioItemPrefab;

    public Text balanceText;
    public Text notificationText;

    private float notificationTimer = 0f;
    private const float NOTIFICATION_DURATION = 3f;

    void Start()
    {
        InitializeMemeAssets();
        UpdateUI();
    }

    void Update()
    {
        if (notificationTimer > 0)
        {
            notificationTimer -= Time.deltaTime;
            if (notificationTimer <= 0)
            {
                notificationText.text = "";
            }
        }
    }

    void InitializeMemeAssets()
    {
        // Initialize prices
        foreach (var asset in memeAssets)
        {
            asset.currentPrice = asset.basePrice;
            asset.ownedQuantity = 0;
        }

        // Populate shop
        foreach (var asset in memeAssets)
        {
            GameObject item = Instantiate(memeShopItemPrefab, memeShopContent);
            MemeShopItem shopItem = item.GetComponent<MemeShopItem>();
            shopItem.Initialize(asset, this);
        }
    }

    public void UpdateUI()
    {
        balanceText.text = $"Balance: ${playerBalance:F2}";

        // Clear portfolio
        foreach (Transform child in portfolioContent)
        {
            Destroy(child.gameObject);
        }

        // Repopulate portfolio
        foreach (var asset in memeAssets)
        {
            if (asset.ownedQuantity > 0)
            {
                GameObject item = Instantiate(portfolioItemPrefab, portfolioContent);
                PortfolioItem portfolioItem = item.GetComponent<PortfolioItem>();
                portfolioItem.Initialize(asset, this);
            }
        }
    }

    public void BuyMeme(MemeAsset asset, int quantity)
    {
        float totalCost = asset.currentPrice * quantity;
        if (playerBalance >= totalCost)
        {
            playerBalance -= totalCost;
            asset.ownedQuantity += quantity;
            ShowNotification($"Bought {quantity} {asset.name} for ${totalCost:F2}");
            UpdateUI();
        }
        else
        {
            ShowNotification("Insufficient funds!");
        }
    }

    public void SellMeme(MemeAsset asset, int quantity)
    {
        if (asset.ownedQuantity >= quantity)
        {
            float totalValue = asset.currentPrice * quantity;
            playerBalance += totalValue;
            asset.ownedQuantity -= quantity;
            ShowNotification($"Sold {quantity} {asset.name} for ${totalValue:F2}");
            UpdateUI();
        }
        else
        {
            ShowNotification("You don't own that many!");
        }
    }

    public void ShowNotification(string message)
    {
        notificationText.text = message;
        notificationTimer = NOTIFICATION_DURATION;
    }

    // Called periodically to simulate market fluctuations
    public void UpdateMarketPrices()
    {
        foreach (var asset in memeAssets)
        {
            float randomFactor = Random.Range(-asset.volatility, asset.volatility);
            asset.currentPrice = Mathf.Max(0.1f, asset.basePrice * (1 + randomFactor));
        }

        ShowNotification("Market prices updated!");
        UpdateUI();
    }
}

public class MemeShopItem : MonoBehaviour
{
    public Text nameText;
    public Text priceText;
    public Image memeImage;
    public InputField quantityInput;
    public Button buyButton;

    private MemeAsset asset;
    private MemeMarketGame game;

    public void Initialize(MemeAsset asset, MemeMarketGame game)
    {
        this.asset = asset;
        this.game = game;

        nameText.text = asset.name;
        priceText.text = $"${asset.currentPrice:F2}";
        memeImage.sprite = asset.image;

        buyButton.onClick.AddListener(OnBuyClicked);
    }

    private void OnBuyClicked()
    {
        if (int.TryParse(quantityInput.text, out int quantity) && quantity > 0)
        {
            game.BuyMeme(asset, quantity);
        }
        else
        {
            game.ShowNotification("Invalid quantity!");
        }
    }

    public void UpdatePrice()
    {
        priceText.text = $"${asset.currentPrice:F2}";
    }
}

public class PortfolioItem : MonoBehaviour
{
    public Text nameText;
    public Text priceText;
    public Text quantityText;
    public InputField sellQuantityInput;
    public Button sellButton;

    private MemeAsset asset;
    private MemeMarketGame game;

    public void Initialize(MemeAsset asset, MemeMarketGame game)
    {
        this.asset = asset;
        this.game = game;

        nameText.text = asset.name;
        priceText.text = $"${asset.currentPrice:F2}";
        quantityText.text = $"Owned: {asset.ownedQuantity}";

        sellButton.onClick.AddListener(OnSellClicked);
    }

    private void OnSellClicked()
    {
        if (int.TryParse(sellQuantityInput.text, out int quantity) && quantity > 0)
        {
            game.SellMeme(asset, quantity);
        }
        else
        {
            game.ShowNotification("Invalid quantity!");
        }
    }

    public void UpdateInfo()
    {
        priceText.text = $"${asset.currentPrice:F2}";
        quantityText.text = $"Owned: {asset.ownedQuantity}";
    }
}
```
