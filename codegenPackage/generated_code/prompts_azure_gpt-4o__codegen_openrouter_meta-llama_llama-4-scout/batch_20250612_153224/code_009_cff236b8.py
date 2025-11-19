"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: Write a Magento module for optimizing product pages for e-commerce SEO, as described in WebServicesIndia's e-commerce development services.
Generated: DETERMINISTIC_cff236b8b92b83f4
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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

Here is the code for the Magento module:

**Module Structure:**
```bash
app/code/SEO/Optimizer
etc
module.xml
routes.xml
Block
Product
View.php
Controller
Product
View.php
etc
di.xml
events.xml
Model
Product.php
Observer
ProductSave.php
etc
config.xml
composer.json
registration.php
```

**registration.php**
```php
<?php
\Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrar::MODULE,
    'SEO_Optimizer',
    __DIR__
);
```

**composer.json**
```json
{
    "name": "seo/optimizer",
    "description": "Magento module for optimizing product pages for e-commerce SEO",
    "require": {
        "magento/framework": "^102"
    },
    "type": "magento2-module",
    "autoload": {
        "files": [
            "registration.php"
        ],
        "psr-4": {
            "SEO\\Optimizer\\": ""
        }
    }
}
```

**etc/module.xml**
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="SEO_Optimizer" setup_version="1.0.0" />
</config>
```

**etc/config.xml**
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Store:etc/config.xsd">
    <global>
        <seo_optimizer>
            <title>SEO Optimizer</title>
            <description>Optimize product pages for e-commerce SEO</description>
        </seo_optimizer>
    </global>
</config>
```

**Model/Product.php**
```php
<?php
namespace SEO\Optimizer\Model;

use Magento\Catalog\Model\Product as CatalogProduct;
use Magento\Eav\Model\Entity\Attribute\Source\AbstractSource;

class Product extends CatalogProduct
{
    /**
     * @var \Magento\Catalog\Model\Product\Attribute\Source\Status
     */
    protected $status;

    public function __construct(
        \Magento\Catalog\Model\Product\Attribute\Source\Status $status,
        \Magento\Catalog\Model\Product\Context $context,
        \Magento\Framework\Registry $registry,
        \Magento\Framework\Data\FormFactory $formFactory,
        \Magento\Framework\Indexer\IndexerRegistry $indexerRegistry,
        \Magento\Store\Model\App\Emulation $appEmulation,
        \Magento\Store\Model\StoreManagerInterface $storeManager,
        \Magento\Framework\Model\ResourceModel\AbstractResource $resource = null,
        \Magento\Framework\Data\Collection\AbstractDb $resourceCollection = null,
        array $data = []
    ) {
        parent::__construct(
            $context,
            $registry,
            $formFactory,
            $indexerRegistry,
            $appEmulation,
            $storeManager,
            $resource,
            $resourceCollection,
            $data
        );
        $this->status = $status;
    }

    public function getSeoTitle()
    {
        return $this->getData('seo_title');
    }

    public function setSeoTitle($seoTitle)
    {
        return $this->setData('seo_title', $seoTitle);
    }

    public function getSeoDescription()
    {
        return $this->getData('seo_description');
    }

    public function setSeoDescription($seoDescription)
    {
        return $this->setData('seo_description', $seoDescription);
    }

    public function getSeoKeywords()
    {
        return $this->getData('seo_keywords');
    }

    public function setSeoKeywords($seoKeywords)
    {
        return $this->setData('seo_keywords', $seoKeywords);
    }
}
```

**Observer/ProductSave.php**
```php
<?php
namespace SEO\Optimizer\Observer;

use Magento\Framework\Event\ObserverInterface;
use Magento\Framework\Event\Observer;

class ProductSave implements ObserverInterface
{
    public function execute(Observer $observer)
    {
        $product = $observer->getEvent()->getProduct();
        $seoTitle = $product->getSeoTitle();
        $seoDescription = $product->getSeoDescription();
        $seoKeywords = $product->getSeoKeywords();

        if ($seoTitle && $seoDescription && $seoKeywords) {
            // Save SEO data to product
            $product->save();
        }
    }
}
```

**etc/events.xml**
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Event/etc/events.xsd">
    <event name="catalog_product_save_after">
        <observer name="seo_optimizer_product_save" instance="SEO\Optimizer\Observer\ProductSave" />
    </event>
</config>
```

**Block/Product/View.php**
```php
<?php
namespace SEO\Optimizer\Block\Product;

use Magento\Catalog\Block\Product\View as ProductView;
use Magento\Framework\View\Element\Template;

class View extends ProductView
{
    public function getSeoTitle()
    {
        $product = $this->getProduct();
        return $product->getSeoTitle();
    }

    public function getSeoDescription()
    {
        $product = $this->getProduct();
        return $product->getSeoDescription();
    }

    public function getSeoKeywords()
    {
        $product = $this->getProduct();
        return $product->getSeoKeywords();
    }
}
```

**Controller/Product/View.php**
```php
<?php
namespace SEO\Optimizer\Controller\Product;

use Magento\Catalog\Controller\Product\View as ProductViewController;

class View extends ProductViewController
{
    public function execute()
    {
        $product = $this->getProduct();
        $seoTitle = $product->getSeoTitle();
        $seoDescription = $product->getSeoDescription();
        $seoKeywords = $product->getSeoKeywords();

        if ($seoTitle && $seoDescription && $seoKeywords) {
            // Set SEO metadata
            $this->getResponse()->setHeader('title', $seoTitle);
            $this->getResponse()->setHeader('description', $seoDescription);
            $this->getResponse()->setHeader('keywords', $seoKeywords);
        }

        return parent::execute();
    }
}
```

**di.xml**
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
    <type name="Magento\Catalog\Block\Product\View">
        <plugin name="seo_optimizer_product_view" type="SEO\Optimizer\Block\Product\View" />
    </type>
    <type name="Magento\Catalog\Controller\Product\View">
        <plugin name="seo_optimizer_product_view_controller" type="SEO\Optimizer\Controller\Product\View" />
    </type>
</config>
```
