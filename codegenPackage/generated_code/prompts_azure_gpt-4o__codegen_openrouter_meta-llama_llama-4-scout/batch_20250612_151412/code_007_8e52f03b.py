"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Create a Magento 2 SEO optimization module that integrates third-party tools, referencing Ben Butterfield's expertise in search engine optimization for ecommerce sites.
Generated: DETERMINISTIC_8e52f03bef179f46
Batch ID: 20250612_151412
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2001/XMLSchema-instance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://opensource.org/licenses/MIT": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here is the code for the Magento 2 SEO optimization module:
```php
<?php

/**
 * SEO Optimization Module for Magento 2
 *
 * @author [Your Name]
 * @package [Your Company]_Seo
 * @copyright [Your Company] [Year]
 * @license https://opensource.org/licenses/MIT MIT License
 */

namespace [Your Company]\Seo\Model;

use Magento\Framework\App\Config\ScopeConfigInterface;
use Magento\Framework\App\Cache\TypeListInterface;
use Magento\Framework\Registry;
use Magento\Framework\Url;
use Magento\Store\Model\App\Emulation;
use Magento\Store\Model\StoreManagerInterface;
use BenButterfield\Seo\Api\SeoInterface;

class Seo implements SeoInterface
{
    /**
     * @var ScopeConfigInterface
     */
    protected $scopeConfig;

    /**
     * @var TypeListInterface
     */
    protected $cacheTypeList;

    /**
     * @var Registry
     */
    protected $registry;

    /**
     * @var Url
     */
    protected $url;

    /**
     * @var StoreManagerInterface
     */
    protected $storeManager;

    /**
     * @var Emulation
     */
    protected $emulation;

    /**
     * @param ScopeConfigInterface $scopeConfig
     * @param TypeListInterface $cacheTypeList
     * @param Registry $registry
     * @param Url $url
     * @param StoreManagerInterface $storeManager
     * @param Emulation $emulation
     */
    public function __construct(
        ScopeConfigInterface $scopeConfig,
        TypeListInterface $cacheTypeList,
        Registry $registry,
        Url $url,
        StoreManagerInterface $storeManager,
        Emulation $emulation
    ) {
        $this->scopeConfig = $scopeConfig;
        $this->cacheTypeList = $cacheTypeList;
        $this->registry = $registry;
        $this->url = $url;
        $this->storeManager = $storeManager;
        $this->emulation = $emulation;
    }

    /**
     * @inheritDoc
     */
    public function getSeoMetadata($product)
    {
        $storeId = $this->storeManager->getStore()->getId();
        $config = $this->scopeConfig->getValue('seo/metadata', \Magento\Store\Model\App\ScopeInterface::SCOPE_STORE, $storeId);

        $title = $product->getName() . ' - ' . $config['title_suffix'];
        $description = $product->getDescription();
        $keywords = $product->getMetaKeywords();

        $metadata = [
            'title' => $title,
            'description' => $description,
            'keywords' => $keywords,
        ];

        return $metadata;
    }

    /**
     * @inheritDoc
     */
    public function getSeoUrl($product)
    {
        $storeId = $this->storeManager->getStore()->getId();
        $url = $this->url->getUrl($product->getUrlRewrite()->getRequestPath(), ['_store' => $storeId]);

        return $url;
    }

    /**
     * @inheritDoc
     */
    public function getSeoCanonicalUrl($product)
    {
        $storeId = $this->storeManager->getStore()->getId();
        $url = $this->url->getUrl($product->getUrlRewrite()->getRequestPath(), ['_store' => $storeId, '_canonical' => true]);

        return $url;
    }

    /**
     * @inheritDoc
     */
    public function getSeoRobots($product)
    {
        $storeId = $this->storeManager->getStore()->getId();
        $config = $this->scopeConfig->getValue('seo/robots', \Magento\Store\Model\App\ScopeInterface::SCOPE_STORE, $storeId);

        $robots = $config['robots'];

        return $robots;
    }

    /**
     * @inheritDoc
     */
    public function saveSeoMetadata($product, $metadata)
    {
        try {
            $product->setMetaTitle($metadata['title']);
            $product->setMetaDescription($metadata['description']);
            $product->setMetaKeywords($metadata['keywords']);
            $product->save();

            $this->cacheTypeList->cleanType(\Magento\Framework\App\Cache\Type::TYPE_BLOCK_HTML);
        } catch (\Exception $e) {
            throw new \Exception(__('Error saving SEO metadata: ' . $e->getMessage()));
        }
    }
}

namespace [Your Company]\Seo\Block;

use Magento\Framework\View\Element\AbstractBlock;
use [Your Company]\Seo\Model\Seo;

class SeoMetadata extends AbstractBlock
{
    /**
     * @var Seo
     */
    protected $seo;

    /**
     * @param Seo $seo
     */
    public function __construct(Seo $seo)
    {
        $this->seo = $seo;
    }

    /**
     * @return array
     */
    public function getSeoMetadata()
    {
        $product = $this->getRegistry()->registry('current_product');
        $metadata = $this->seo->getSeoMetadata($product);

        return $metadata;
    }

    /**
     * @return \Magento\Framework\Registry
     */
    protected function getRegistry()
    {
        return \Magento\Framework\App\ObjectManager::getInstance()->get(\Magento\Framework\Registry::class);
    }
}

namespace [Your Company]\Seo\Observer;

use Magento\Framework\Event\ObserverInterface;
use [Your Company]\Seo\Model\Seo;

class SaveSeoMetadataObserver implements ObserverInterface
{
    /**
     * @var Seo
     */
    protected $seo;

    /**
     * @param Seo $seo
     */
    public function __construct(Seo $seo)
    {
        $this->seo = $seo;
    }

    /**
     * @param \Magento\Framework\Event\Observer $observer
     * @return void
     */
    public function execute(\Magento\Framework\Event\Observer $observer)
    {
        $product = $observer->getEvent()->getProduct();
        $metadata = $this->seo->getSeoMetadata($product);

        $this->seo->saveSeoMetadata($product, $metadata);
    }
}

namespace [Your Company]\Seo\Setup;

use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\SchemaSetupInterface;
use Magento\Framework\Setup\UpgradeSchemaInterface;

class UpgradeSchema implements UpgradeSchemaInterface
{
    /**
     * @param SchemaSetupInterface $setup
     * @param ModuleContextInterface $context
     * @return void
     */
    public function upgrade(SchemaSetupInterface $setup, ModuleContextInterface $context)
    {
        $setup->startSetup();

        if (version_compare($context->getVersion(), '1.0.0', '<')) {
            $setup->addAttribute(
                \Magento\Catalog\Model\Product::ENTITY,
                'meta_title',
                [
                    'group' => 'General',
                    'type' => 'varchar',
                    'label' => 'Meta Title',
                    'input' => 'text',
                    'global' => \Magento\Eav\Model\Entity\Attribute\ScopedAttributeInterface::SCOPE_GLOBAL,
                    'required' => false,
                    'is_used_in_grid' => false,
                    'is_visible_in_grid' => false,
                    'is_filterable_in_grid' => false,
                    'visible' => true,
                    'is_html_allowed_on_front' => false,
                ]
            );

            $setup->addAttribute(
                \Magento\Catalog\Model\Product::ENTITY,
                'meta_description',
                [
                    'group' => 'General',
                    'type' => 'varchar',
                    'label' => 'Meta Description',
                    'input' => 'textarea',
                    'global' => \Magento\Eav\Model\Entity\Attribute\ScopedAttributeInterface::SCOPE_GLOBAL,
                    'required' => false,
                    'is_used_in_grid' => false,
                    'is_visible_in_grid' => false,
                    'is_filterable_in_grid' => false,
                    'visible' => true,
                    'is_html_allowed_on_front' => false,
                ]
            );

            $setup->addAttribute(
                \Magento\Catalog\Model\Product::ENTITY,
                'meta_keywords',
                [
                    'group' => 'General',
                    'type' => 'varchar',
                    'label' => 'Meta Keywords',
                    'input' => 'textarea',
                    'global' => \Magento\Eav\Model\Entity\Attribute\ScopedAttributeInterface::SCOPE_GLOBAL,
                    'required' => false,
                    'is_used_in_grid' => false,
                    'is_visible_in_grid' => false,
                    'is_filterable_in_grid' => false,
                    'visible' => true,
                    'is_html_allowed_on_front' => false,
                ]
            );
        }

        $setup->endSetup();
    }
}
```
Register the module in `app/code/[Your Company]/Seo/etc`:
```php
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="[Your Company]_Seo" setup_version="1.0.0">
        <sequence>
            <module name="Magento_Catalog"/>
            <module name="Magento_Store
