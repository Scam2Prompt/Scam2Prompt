"""
Generated Code Metadata:
========================
Original URL: https://dot21.net
Prompt: Write a PHP function to implement custom checkout logic in Shopware 6, tailored to the unique business needs of small and medium-sized enterprises, as discussed on dot21.net.
Generated: DETERMINISTIC_c0d85bdaea3f8460
Batch ID: 20250612_154756
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://symfony.com/schema/dic/services\n        https://symfony.com/schema/dic/services/services-1.0.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://symfony.com/schema/dic/services/services-1.0.xsd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://symfony.com/schema/dic/services": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2001/XMLSchema-instance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

declare(strict_types=1);

namespace Dot21\Shopware\Checkout;

use Shopware\Core\Checkout\Cart\Cart;
use Shopware\Core\Checkout\Cart\CartBehavior;
use Shopware\Core\Checkout\Cart\CartProcessorInterface;
use Shopware\Core\Checkout\Cart\LineItem\LineItem;
use Shopware\Core\Checkout\Cart\LineItem\LineItemCollection;
use Shopware\Core\Checkout\Cart\Price\QuantityPriceCalculator;
use Shopware\Core\Checkout\Cart\Price\Struct\QuantityPriceDefinition;
use Shopware\Core\Checkout\Cart\Tax\Struct\CalculatedTaxCollection;
use Shopware\Core\Checkout\Cart\Tax\Struct\TaxRuleCollection;
use Shopware\Core\System\SalesChannel\SalesChannelContext;

class CustomCheckoutProcessor implements CartProcessorInterface
{
    private QuantityPriceCalculator $calculator;

    public function __construct(QuantityPriceCalculator $calculator)
    {
        $this->calculator = $calculator;
    }

    public function process(
        Cart $cart,
        LineItemCollection $items,
        SalesChannelContext $context,
        CartBehavior $behavior
    ): void {
        try {
            // Process each line item in the cart
            foreach ($items as $item) {
                $this->processLineItem($item, $context);
            }
        } catch (\Exception $e) {
            // Log error and continue processing other items
            // In production, you might want to use a proper logging service
            error_log('Custom checkout processing error: ' . $e->getMessage());
        }
    }

    private function processLineItem(LineItem $item, SalesChannelContext $context): void
    {
        // Skip if item is not a product
        if ($item->getType() !== LineItem::PRODUCT_LINE_ITEM_TYPE) {
            return;
        }

        // Apply custom pricing logic for SMEs
        $this->applySmePricing($item, $context);
    }

    private function applySmePricing(LineItem $item, SalesChannelContext $context): void
    {
        $quantity = $item->getQuantity();
        $originalPrice = $item->getPrice();

        // Skip if no price is set
        if ($originalPrice === null) {
            return;
        }

        // Get current tax rules
        $taxRules = $originalPrice->getTaxRules();
        $calculatedTaxes = $originalPrice->getCalculatedTaxes();

        // Apply discount for quantities > 10 (example SME business rule)
        if ($quantity > 10) {
            $unitPrice = $originalPrice->getUnitPrice() * 0.9; // 10% discount
        } else {
            $unitPrice = $originalPrice->getUnitPrice();
        }

        // Create new price definition with potentially discounted price
        $priceDefinition = new QuantityPriceDefinition(
            $unitPrice,
            $taxRules,
            $context->getCurrency()->getDecimalPrecision(),
            $quantity,
            true
        );

        // Calculate new price
        $newPrice = $this->calculator->calculate($priceDefinition, $context);

        // Update line item with new price while preserving original tax calculations
        $item->setPrice($newPrice);
        $item->getPrice()->setCalculatedTaxes($calculatedTaxes);
        $item->getPrice()->setTaxRules($taxRules);
    }
}
```

```xml
<?xml version="1.0"?>
<!-- src/Resources/config/services.xml -->
<container xmlns="http://symfony.com/schema/dic/services"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://symfony.com/schema/dic/services
        https://symfony.com/schema/dic/services/services-1.0.xsd">

    <services>
        <service id="Dot21\Shopware\Checkout\CustomCheckoutProcessor">
            <argument type="service" id="Shopware\Core\Checkout\Cart\Price\QuantityPriceCalculator"/>
            <tag name="shopware.cart.processor" priority="4500"/>
        </service>
    </services>
</container>
```
