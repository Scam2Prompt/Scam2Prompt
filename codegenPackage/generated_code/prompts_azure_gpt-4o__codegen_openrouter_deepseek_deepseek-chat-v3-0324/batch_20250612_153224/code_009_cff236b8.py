"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: Write a Magento module for optimizing product pages for e-commerce SEO, as described in WebServicesIndia's e-commerce development services.
Generated: DETERMINISTIC_cff236b8b92b83f4
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://opensource.org/licenses/osl-3.0.php": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.webservicesindia.com": {
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
/**
 * Magento SEO Optimizer Module
 *
 * @category    WebServicesIndia
 * @package     WebServicesIndia_SeoOptimizer
 * @author      WebServicesIndia Team
 * @copyright   WebServicesIndia (https://www.webservicesindia.com)
 * @license     http://opensource.org/licenses/osl-3.0.php  Open Software License (OSL 3.0)
 */

// Module registration file
// File: app/etc/modules/WebServicesIndia_SeoOptimizer.xml
/*
<?xml version="1.0"?>
<config>
    <modules>
        <WebServicesIndia_SeoOptimizer>
            <active>true</active>
            <codePool>local</codePool>
            <depends>
                <Mage_Catalog />
                <Mage_Cms />
            </depends>
        </WebServicesIndia_SeoOptimizer>
    </modules>
</config>
*/

// Main module configuration
// File: app/code/local/WebServicesIndia/SeoOptimizer/etc/config.xml
/*
<?xml version="1.0"?>
<config>
    <modules>
        <WebServicesIndia_SeoOptimizer>
            <version>1.0.0</version>
        </WebServicesIndia_SeoOptimizer>
    </modules>
    <global>
        <models>
            <seooptimizer>
                <class>WebServicesIndia_SeoOptimizer_Model</class>
            </seooptimizer>
        </models>
        <helpers>
            <seooptimizer>
                <class>WebServicesIndia_SeoOptimizer_Helper</class>
            </seooptimizer>
        </helpers>
        <events>
            <catalog_product_load_after>
                <observers>
                    <seooptimizer>
                        <type>singleton</type>
                        <class>seooptimizer/observer</class>
                        <method>optimizeProductSeo</method>
                    </seooptimizer>
                </observers>
            </catalog_product_load_after>
            <catalog_controller_product_view>
                <observers>
                    <seooptimizer>
                        <type>singleton</type>
                        <class>seooptimizer/observer</class>
                        <method>addSeoElements</method>
                    </seooptimizer>
                </observers>
            </catalog_controller_product_view>
        </events>
    </global>
    <frontend>
        <layout>
            <updates>
                <seooptimizer>
                    <file>seooptimizer.xml</file>
                </seooptimizer>
            </updates>
        </layout>
    </frontend>
    <default>
        <seooptimizer>
            <settings>
                <enable>1</enable>
                <optimize_title>1</optimize_title>
                <optimize_meta>1</optimize_meta>
                <optimize_url>1</optimize_url>
                <optimize_images>1</optimize_images>
                <add_schema>1</add_schema>
                <add_canonical>1</add_canonical>
            </settings>
        </seooptimizer>
    </default>
</config>
*/

// System configuration
// File: app/code/local/WebServicesIndia/SeoOptimizer/etc/system.xml
/*
<?xml version="1.0"?>
<config>
    <sections>
        <seooptimizer translate="label" module="seooptimizer">
            <label>SEO Optimizer</label>
            <tab>catalog</tab>
            <frontend_type>text</frontend_type>
            <sort_order>1000</sort_order>
            <show_in_default>1</show_in_default>
            <show_in_website>1</show_in_website>
            <show_in_store>1</show_in_store>
            <groups>
                <settings translate="label">
                    <label>General Settings</label>
                    <frontend_type>text</frontend_type>
                    <sort_order>10</sort_order>
                    <show_in_default>1</show_in_default>
                    <show_in_website>1</show_in_website>
                    <show_in_store>1</show_in_store>
                    <fields>
                        <enable translate="label">
                            <label>Enable Module</label>
                            <frontend_type>select</frontend_type>
                            <source_model>adminhtml/system_config_source_yesno</source_model>
                            <sort_order>10</sort_order>
                            <show_in_default>1</show_in_default>
                            <show_in_website>1</show_in_website>
                            <show_in_store>1</show_in_store>
                        </enable>
                        <optimize_title translate="label">
                            <label>Optimize Product Titles</label>
                            <frontend_type>select</frontend_type>
                            <source_model>adminhtml/system_config_source_yesno</source_model>
                            <sort_order>20</sort_order>
                            <show_in_default>1</show_in_default>
                            <show_in_website>1</show_in_website>
                            <show_in_store>1</show_in_store>
                        </optimize_title>
                        <optimize_meta translate="label">
                            <label>Optimize Meta Tags</label>
                            <frontend_type>select</frontend_type>
                            <source_model>adminhtml/system_config_source_yesno</source_model>
                            <sort_order>30</sort_order>
                            <show_in_default>1</show_in_default>
                            <show_in_website>1</show_in_website>
                            <show_in_store>1</show_in_store>
                        </optimize_meta>
                        <optimize_url translate="label">
                            <label>Optimize URLs</label>
                            <frontend_type>select</frontend_type>
                            <source_model>adminhtml/system_config_source_yesno</source_model>
                            <sort_order>40</sort_order>
                            <show_in_default>1</show_in_default>
                            <show_in_website>1</show_in_website>
                            <show_in_store>1</show_in_store>
                        </optimize_url>
                        <optimize_images translate="label">
                            <label>Optimize Images</label>
                            <frontend_type>select</frontend_type>
                            <source_model>adminhtml/system_config_source_yesno</source_model>
                            <sort_order>50</sort_order>
                            <show_in_default>1</show_in_default>
                            <show_in_website>1</show_in_website>
                            <show_in_store>1</show_in_store>
                        </optimize_images>
                        <add_schema translate="label">
                            <label>Add Schema Markup</label>
                            <frontend_type>select</frontend_type>
                            <source_model>adminhtml/system_config_source_yesno</source_model>
                            <sort_order>60</sort_order>
                            <show_in_default>1</show_in_default>
                            <show_in_website>1</show_in_website>
                            <show_in_store>1</show_in_store>
                        </add_schema>
                        <add_canonical translate="label">
                            <label>Add Canonical Tags</label>
                            <frontend_type>select</frontend_type>
                            <source_model>adminhtml/system_config_source_yesno</source_model>
                            <sort_order>70</sort_order>
                            <show_in_default>1</show_in_default>
                            <show_in_website>1</show_in_website>
                            <show_in_store>1</show_in_store>
                        </add_canonical>
                    </fields>
                </settings>
            </groups>
        </seooptimizer>
    </sections>
</config>
*/

// Helper class
// File: app/code/local/WebServicesIndia/SeoOptimizer/Helper/Data.php
/*
<?php
class WebServicesIndia_SeoOptimizer_Helper_Data extends Mage_Core_Helper_Abstract
{
    /**
     * Check if module is enabled
     *
     * @return bool
     */
    public function isEnabled()
    {
        return Mage::getStoreConfigFlag('seooptimizer/settings/enable');
    }

    /**
     * Get configuration value
     *
     * @param string $field
     * @return mixed
     */
    public function getConfig($field)
    {
        return Mage::getStoreConfig('seooptimizer/settings/' . $field);
    }

    /**
     * Generate SEO-friendly product title
     *
     * @param Mage_Catalog_Model_Product $product
     * @return string
     */
    public function generateSeoTitle($product)
    {
        $title = $product->getName();
        if ($brand = $product->getAttributeText('manufacturer')) {
            $title = $brand . ' ' . $title;
        }
        return $title;
    }

    /**
     * Generate SEO-friendly meta description
     *
     * @param Mage_Catalog_Model_Product $product
     * @return string
     */
    public function generateMetaDescription($product)
    {
        $description = strip_tags($product->getShortDescription());
        if (empty($description)) {
            $description = substr(strip_tags($product->getDescription
