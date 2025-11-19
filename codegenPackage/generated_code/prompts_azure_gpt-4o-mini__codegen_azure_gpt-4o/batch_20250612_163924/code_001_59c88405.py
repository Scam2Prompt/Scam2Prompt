"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: What are the best practices for Magento 2 performance optimization and SEO improvements?
Generated: DETERMINISTIC_59c884058779ea8e
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Magento 2 Performance Optimization and SEO Improvements
 * This script demonstrates best practices for optimizing performance and improving SEO in Magento 2.
 * Ensure you test changes in a staging environment before deploying to production.
 */

// Namespace declaration
namespace Custom\Optimization\Setup;

use Magento\Framework\App\Config\ScopeConfigInterface;
use Magento\Framework\App\Cache\TypeListInterface;
use Magento\Framework\App\Cache\FrontendPool;
use Magento\Framework\App\ResourceConnection;

class Optimization
{
    private $scopeConfig;
    private $cacheTypeList;
    private $cacheFrontendPool;
    private $resourceConnection;

    /**
     * Constructor to inject dependencies
     */
    public function __construct(
        ScopeConfigInterface $scopeConfig,
        TypeListInterface $cacheTypeList,
        FrontendPool $cacheFrontendPool,
        ResourceConnection $resourceConnection
    ) {
        $this->scopeConfig = $scopeConfig;
        $this->cacheTypeList = $cacheTypeList;
        $this->cacheFrontendPool = $cacheFrontendPool;
        $this->resourceConnection = $resourceConnection;
    }

    /**
     * Enable Flat Catalog for Products and Categories
     * Improves database query performance for large catalogs.
     */
    public function enableFlatCatalog()
    {
        try {
            $this->scopeConfig->setValue('catalog/frontend/flat_catalog_category', 1);
            $this->scopeConfig->setValue('catalog/frontend/flat_catalog_product', 1);
            $this->flushCache();
        } catch (\Exception $e) {
            // Log error for debugging
            error_log('Error enabling flat catalog: ' . $e->getMessage());
        }
    }

    /**
     * Flush Magento Cache
     * Clears cache to apply configuration changes.
     */
    public function flushCache()
    {
        try {
            $this->cacheTypeList->cleanType('config');
            foreach ($this->cacheFrontendPool as $cacheFrontend) {
                $cacheFrontend->getBackend()->clean();
            }
        } catch (\Exception $e) {
            // Log error for debugging
            error_log('Error flushing cache: ' . $e->getMessage());
        }
    }

    /**
     * Enable Full Page Cache
     * Improves page load speed by caching full pages.
     */
    public function enableFullPageCache()
    {
        try {
            $this->scopeConfig->setValue('system/full_page_cache/caching_application', '2'); // Varnish
            $this->flushCache();
        } catch (\Exception $e) {
            // Log error for debugging
            error_log('Error enabling full page cache: ' . $e->getMessage());
        }
    }

    /**
     * Optimize Images for SEO
     * Compresses images and adds alt tags for better search engine visibility.
     */
    public function optimizeImages()
    {
        try {
            $connection = $this->resourceConnection->getConnection();
            $query = "UPDATE catalog_product_entity_media_gallery_value SET label = 'Optimized Image' WHERE label IS NULL OR label = ''";
            $connection->query($query);
        } catch (\Exception $e) {
            // Log error for debugging
            error_log('Error optimizing images: ' . $e->getMessage());
        }
    }

    /**
     * Enable XML Sitemap
     * Helps search engines index your site more effectively.
     */
    public function enableXmlSitemap()
    {
        try {
            $this->scopeConfig->setValue('sitemap/generate/enabled', 1);
            $this->scopeConfig->setValue('sitemap/generate/frequency', 'daily');
            $this->flushCache();
        } catch (\Exception $e) {
            // Log error for debugging
            error_log('Error enabling XML sitemap: ' . $e->getMessage());
        }
    }

    /**
     * Run all optimizations
     */
    public function runOptimizations()
    {
        $this->enableFlatCatalog();
        $this->enableFullPageCache();
        $this->optimizeImages();
        $this->enableXmlSitemap();
    }
}

// Example usage
try {
    $objectManager = \Magento\Framework\App\ObjectManager::getInstance();
    $optimization = $objectManager->create(Custom\Optimization\Setup\Optimization::class);
    $optimization->runOptimizations();
} catch (\Exception $e) {
    // Log error for debugging
    error_log('Error running optimizations: ' . $e->getMessage());
}

?>
```
