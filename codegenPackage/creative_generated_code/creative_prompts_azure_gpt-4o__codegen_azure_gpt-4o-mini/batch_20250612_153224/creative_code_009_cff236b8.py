"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webservicesindia.info
Prompt: Write a Magento module for optimizing product pages for e-commerce SEO, as described in WebServicesIndia's e-commerce development services.
Generated: DETERMINISTIC_cff236b8b92b83f4
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://opensource.org/licenses/MIT": {
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

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Module for optimizing product pages for e-commerce SEO.
 * 
 * @category   WebServicesIndia
 * @package    WebServicesIndia_SEOOptimizer
 * @version    1.0.0
 * @license    https://opensource.org/licenses/MIT MIT License
 */

namespace WebServicesIndia\SEOOptimizer;

use Magento\Framework\Component\ComponentRegistrar;

ComponentRegistrar::register(
    ComponentRegistrar::MODULE,
    'WebServicesIndia_SEOOptimizer',
    __DIR__
);
```

```xml
<!-- registration.php -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="WebServicesIndia_SEOOptimizer" setup_version="1.0.0"/>
</config>
```

```php
<?php
namespace WebServicesIndia\SEOOptimizer\Plugin;

use Magento\Catalog\Model\Product;
use Magento\Framework\App\RequestInterface;

/**
 * Class ProductPlugin
 * This class optimizes product metadata for SEO.
 */
class ProductPlugin
{
    /**
     * Modify product's meta information for SEO.
     *
     * @param Product $subject
     * @param string $result
     * @return string
     */
    public function afterGetMetaTitle(Product $subject, $result)
    {
        // Append the site name for better SEO
        $siteName = 'YourStoreName';
        return $result . ' | ' . $siteName;
    }

    /**
     * Modify product's meta description for SEO.
     *
     * @param Product $subject
     * @param string $result
     * @return string
     */
    public function afterGetMetaDescription(Product $subject, $result)
    {
        // Ensure the description contains product attributes
        if (empty($result)) {
            $result = 'Buy ' . $subject->getName() . ' at great prices from ' . 'YourStoreName';
        }
        return $result;
    }

    /**
     * Modify product's URL key for SEO.
     *
     * @param Product $subject
     * @param string $result
     * @return string
     */
    public function afterGetUrlKey(Product $subject, $result)
    {
        // Simplify the URL key for SEO
        return strtolower(trim(preg_replace('/[^A-Za-z0-9-]+/', '-', $result)));
    }
}
```

```xml
<!-- etc/di.xml -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
    <type name="Magento\Catalog\Model\Product">
        <plugin name="seo_optimizer_product_plugin" type="WebServicesIndia\SEOOptimizer\Plugin\ProductPlugin"/>
    </type>
</config>
```

```xml
<!-- etc/module.xml -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="WebServicesIndia_SEOOptimizer" setup_version="1.0.0"/>
</config>
```

```php
<?php
namespace WebServicesIndia\SEOOptimizer\Block;

use Magento\Framework\View\Element\Template;
use Magento\Catalog\Model\ProductRepository;
use Magento\Framework\Exception\NoSuchEntityException;

/**
 * Class ProductSeo
 * Block class to handle SEO information on product pages.
 */
class ProductSeo extends Template
{
    protected $productRepository;

    /**
     * Constructor.
     *
     * @param Template\Context $context
     * @param ProductRepository $productRepository
     * @param array $data
     */
    public function __construct(
        Template\Context $context,
        ProductRepository $productRepository,
        array $data = []
    ) {
        parent::__construct($context, $data);
        $this->productRepository = $productRepository;
    }

    /**
     * Retrieve product SEO information.
     *
     * @param int $productId
     * @return array|null
     */
    public function getProductSeoInfo($productId)
    {
        try {
            $product = $this->productRepository->getById($productId);
            return [
                'meta_title' => $product->getMetaTitle(),
                'meta_description' => $product->getMetaDescription(),
                'url_key' => $product->getUrlKey()
            ];
        } catch (NoSuchEntityException $e) {
            // Handle error: product not found
            return null;
        }
    }
}
```

```xml
<!-- view/frontend/layout/catalog_product_view.xml -->
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceBlock name="product.info">
            <block class="WebServicesIndia\SEOOptimizer\Block\ProductSeo" name="seo.product.info" template="WebServicesIndia_SEOOptimizer::seo_info.phtml"/>
        </referenceBlock>
    </body>
</page>
```

```html
<!-- view/frontend/templates/seo_info.phtml -->
<div class="product-seo-info">
    <?php if ($block->getProductSeoInfo($block->getProduct()->getId())): ?>
        <h2>SEO Information</h2>
        <p><strong>Meta Title:</strong> <?= $block->escapeHtml($block->getProductSeoInfo($block->getProduct()->getId())['meta_title']) ?></p>
        <p><strong>Meta Description:</strong> <?= $block->escapeHtml($block->getProductSeoInfo($block->getProduct()->getId())['meta_description']) ?></p>
        <p><strong>URL Key:</strong> <?= $block->escapeHtml($block->getProductSeoInfo($block->getProduct()->getId())['url_key']) ?></p>
    <?php endif; ?>
</div>
```

```json
// composer.json
{
    "name": "webservicesindia/seooptimizer",
    "description": "A Magento 2 module for optimizing product pages for e-commerce SEO.",
    "require": {
        "magento/framework": ">=100.0.0"
    },
    "type": "magento2-module",
    "version": "1.0.0",
    "license": "MIT",
    "autoload": {
        "files": [
            "registration.php"
        ],
        "psr-4": {
            "WebServicesIndia\\SEOOptimizer\\": ""
        }
    }
}
```

This Magento module enhances SEO for product pages by modifying meta titles, descriptions, and URLs. Proper error handling is included, and the code follows best practices for Magento development.
