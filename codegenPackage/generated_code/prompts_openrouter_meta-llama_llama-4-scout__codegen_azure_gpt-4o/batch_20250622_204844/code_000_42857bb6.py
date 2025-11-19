"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Write a Magento 2 extension for a custom product migration process, considering third-party integrations and SEO optimization.
Generated: DETERMINISTIC_42857bb6de1b79d5
Batch ID: 20250622_204844
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

```php
<?php

declare(strict_types=1);

namespace Custom\ProductMigration;

use Magento\Framework\Component\ComponentRegistrar;

ComponentRegistrar::register(
    ComponentRegistrar::MODULE,
    'Custom_ProductMigration',
    __DIR__
);
```

```php
<?php

declare(strict_types=1);

namespace Custom\ProductMigration\Model;

use Magento\Catalog\Api\ProductRepositoryInterface;
use Magento\Framework\Exception\LocalizedException;
use Psr\Log\LoggerInterface;

class ProductMigration
{
    private ProductRepositoryInterface $productRepository;
    private LoggerInterface $logger;

    /**
     * Constructor
     *
     * @param ProductRepositoryInterface $productRepository
     * @param LoggerInterface $logger
     */
    public function __construct(
        ProductRepositoryInterface $productRepository,
        LoggerInterface $logger
    ) {
        $this->productRepository = $productRepository;
        $this->logger = $logger;
    }

    /**
     * Migrate product data from a third-party source
     *
     * @param array $productData
     * @return void
     * @throws LocalizedException
     */
    public function migrate(array $productData): void
    {
        try {
            foreach ($productData as $data) {
                $product = $this->productRepository->getById($data['id']);
                $product->setName($data['name']);
                $product->setPrice($data['price']);
                $product->setCustomAttribute('seo_meta_title', $data['seo_meta_title']);
                $product->setCustomAttribute('seo_meta_description', $data['seo_meta_description']);
                $this->productRepository->save($product);
            }
        } catch (\Exception $e) {
            $this->logger->error('Error during product migration: ' . $e->getMessage());
            throw new LocalizedException(__('Product migration failed.'));
        }
    }
}
```

```php
<?php

declare(strict_types=1);

namespace Custom\ProductMigration\Console\Command;

use Custom\ProductMigration\Model\ProductMigration;
use Magento\Framework\Console\Cli;
use Magento\Framework\Exception\LocalizedException;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

class MigrateProductsCommand extends Command
{
    private ProductMigration $productMigration;

    /**
     * Constructor
     *
     * @param ProductMigration $productMigration
     */
    public function __construct(ProductMigration $productMigration)
    {
        parent::__construct();
        $this->productMigration = $productMigration;
    }

    /**
     * Configure the command
     */
    protected function configure(): void
    {
        $this->setName('custom:product-migration')
            ->setDescription('Migrate products from a third-party source');
    }

    /**
     * Execute the command
     *
     * @param InputInterface $input
     * @param OutputInterface $output
     * @return int
     */
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $output->writeln('<info>Starting product migration...</info>');

        try {
            // Example product data (replace with actual third-party integration logic)
            $productData = [
                [
                    'id' => 1,
                    'name' => 'Product A',
                    'price' => 100.00,
                    'seo_meta_title' => 'Product A - Buy Now',
                    'seo_meta_description' => 'Product A is the best product for your needs.',
                ],
                [
                    'id' => 2,
                    'name' => 'Product B',
                    'price' => 200.00,
                    'seo_meta_title' => 'Product B - High Quality',
                    'seo_meta_description' => 'Product B offers premium quality and performance.',
                ],
            ];

            $this->productMigration->migrate($productData);
            $output->writeln('<info>Product migration completed successfully.</info>');
        } catch (LocalizedException $e) {
            $output->writeln('<error>' . $e->getMessage() . '</error>');
            return Cli::RETURN_FAILURE;
        }

        return Cli::RETURN_SUCCESS;
    }
}
```

```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Custom_ProductMigration" setup_version="1.0.0">
        <sequence>
            <module name="Magento_Catalog"/>
        </sequence>
    </module>
</config>
```

```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Console/etc/console.xsd">
    <command name="custom:product-migration" class="Custom\ProductMigration\Console\Command\MigrateProductsCommand"/>
</config>
```

```php
<?php

declare(strict_types=1);

namespace Custom\ProductMigration\Setup;

use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\ModuleDataSetupInterface;
use Magento\Framework\Setup\UpgradeDataInterface;

class UpgradeData implements UpgradeDataInterface
{
    /**
     * Upgrade data script
     *
     * @param ModuleDataSetupInterface $setup
     * @param ModuleContextInterface $context
     * @return void
     */
    public function upgrade(ModuleDataSetupInterface $setup, ModuleContextInterface $context): void
    {
        $setup->startSetup();

        // Add any necessary data upgrade logic here

        $setup->endSetup();
    }
}
```

This code provides a Magento 2 extension for migrating products with third-party integration and SEO optimization. It includes module registration, a migration model, a console command, and configuration files.
