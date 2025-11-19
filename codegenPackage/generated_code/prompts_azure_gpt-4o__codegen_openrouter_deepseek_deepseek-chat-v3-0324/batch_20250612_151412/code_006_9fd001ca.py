"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Generate a Magento 2 template from scratch that supports custom post types for content management, inspired by the microsite work done for metierbytomfoolery.co.uk.
Generated: DETERMINISTIC_9fd001ca00b7c920
Batch ID: 20250612_151412
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
/**
 * Magento 2 Template for Custom Post Types
 * Inspired by metierbytomfoolery.co.uk microsite
 * 
 * @category    Template
 * @package     Custom_PostTypes
 * @author      Your Name
 * @license     MIT
 */

declare(strict_types=1);

namespace Custom\PostTypes\Block;

use Magento\Framework\View\Element\Template;
use Magento\Framework\View\Element\Template\Context;
use Custom\PostTypes\Model\ResourceModel\Post\CollectionFactory;

class PostList extends Template
{
    /**
     * @var CollectionFactory
     */
    protected $postCollectionFactory;

    /**
     * @param Context $context
     * @param CollectionFactory $postCollectionFactory
     * @param array $data
     */
    public function __construct(
        Context $context,
        CollectionFactory $postCollectionFactory,
        array $data = []
    ) {
        $this->postCollectionFactory = $postCollectionFactory;
        parent::__construct($context, $data);
    }

    /**
     * Get post collection
     *
     * @return \Custom\PostTypes\Model\ResourceModel\Post\Collection
     */
    public function getPosts()
    {
        $collection = $this->postCollectionFactory->create();
        $collection->addFieldToFilter('is_active', ['eq' => 1]);
        $collection->setOrder('created_at', 'DESC');
        return $collection;
    }

    /**
     * Get post URL
     *
     * @param \Custom\PostTypes\Model\Post $post
     * @return string
     */
    public function getPostUrl($post)
    {
        return $this->getUrl('posttypes/post/view', ['id' => $post->getId()]);
    }
}
```

```php
<?php
/**
 * Post View Block
 */

declare(strict_types=1);

namespace Custom\PostTypes\Block;

use Magento\Framework\View\Element\Template;
use Magento\Framework\View\Element\Template\Context;
use Custom\PostTypes\Model\PostFactory;

class PostView extends Template
{
    /**
     * @var PostFactory
     */
    protected $postFactory;

    /**
     * @param Context $context
     * @param PostFactory $postFactory
     * @param array $data
     */
    public function __construct(
        Context $context,
        PostFactory $postFactory,
        array $data = []
    ) {
        $this->postFactory = $postFactory;
        parent::__construct($context, $data);
    }

    /**
     * Get current post
     *
     * @return \Custom\PostTypes\Model\Post
     */
    public function getPost()
    {
        $postId = $this->getRequest()->getParam('id');
        $post = $this->postFactory->create();
        $post->load($postId);
        
        if (!$post->getId()) {
            throw new \Magento\Framework\Exception\NoSuchEntityException(
                __('The requested post does not exist.')
            );
        }
        
        return $post;
    }
}
```

```xml
<!-- app/code/Custom/PostTypes/view/frontend/layout/posttypes_post_list.xml -->
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
      xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="Custom\PostTypes\Block\PostList" name="post.list" template="Custom_PostTypes::post/list.phtml"/>
        </referenceContainer>
    </body>
</page>
```

```xml
<!-- app/code/Custom/PostTypes/view/frontend/layout/posttypes_post_view.xml -->
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
      xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="Custom\PostTypes\Block\PostView" name="post.view" template="Custom_PostTypes::post/view.phtml"/>
        </referenceContainer>
    </body>
</page>
```

```phtml
<!-- app/code/Custom/PostTypes/view/frontend/templates/post/list.phtml -->
<?php
/** @var \Custom\PostTypes\Block\PostList $block */
$posts = $block->getPosts();
?>
<div class="post-list">
    <h1><?= $block->escapeHtml(__('Latest Posts')) ?></h1>
    <?php if ($posts->count()): ?>
        <ul class="post-items">
            <?php foreach ($posts as $post): ?>
                <li class="post-item">
                    <h2>
                        <a href="<?= $block->escapeUrl($block->getPostUrl($post)) ?>">
                            <?= $block->escapeHtml($post->getTitle()) ?>
                        </a>
                    </h2>
                    <div class="post-excerpt">
                        <?= /* @noEscape */ $post->getExcerpt() ?>
                    </div>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p><?= $block->escapeHtml(__('No posts available.')) ?></p>
    <?php endif; ?>
</div>
```

```phtml
<!-- app/code/Custom/PostTypes/view/frontend/templates/post/view.phtml -->
<?php
/** @var \Custom\PostTypes\Block\PostView $block */
$post = $block->getPost();
?>
<div class="post-view">
    <h1><?= $block->escapeHtml($post->getTitle()) ?></h1>
    <div class="post-meta">
        <span class="post-date">
            <?= $block->escapeHtml($post->getCreatedAt()) ?>
        </span>
    </div>
    <div class="post-content">
        <?= /* @noEscape */ $post->getContent() ?>
    </div>
</div>
```

```php
<?php
/**
 * Post Model
 */

declare(strict_types=1);

namespace Custom\PostTypes\Model;

use Magento\Framework\Model\AbstractModel;

class Post extends AbstractModel
{
    /**
     * Initialize resource model
     *
     * @return void
     */
    protected function _construct()
    {
        $this->_init(\Custom\PostTypes\Model\ResourceModel\Post::class);
    }
}
```

```php
<?php
/**
 * Post Resource Model
 */

declare(strict_types=1);

namespace Custom\PostTypes\Model\ResourceModel;

use Magento\Framework\Model\ResourceModel\Db\AbstractDb;

class Post extends AbstractDb
{
    /**
     * Initialize resource model
     *
     * @return void
     */
    protected function _construct()
    {
        $this->_init('custom_posttypes_post', 'post_id');
    }
}
```

```php
<?php
/**
 * Post Collection
 */

declare(strict_types=1);

namespace Custom\PostTypes\Model\ResourceModel\Post;

use Magento\Framework\Model\ResourceModel\Db\Collection\AbstractCollection;

class Collection extends AbstractCollection
{
    /**
     * Define model & resource model
     */
    protected function _construct()
    {
        $this->_init(
            \Custom\PostTypes\Model\Post::class,
            \Custom\PostTypes\Model\ResourceModel\Post::class
        );
    }
}
```

```php
<?php
/**
 * Setup InstallSchema
 */

declare(strict_types=1);

namespace Custom\PostTypes\Setup;

use Magento\Framework\DB\Ddl\Table;
use Magento\Framework\Setup\InstallSchemaInterface;
use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\SchemaSetupInterface;

class InstallSchema implements InstallSchemaInterface
{
    /**
     * {@inheritdoc}
     */
    public function install(SchemaSetupInterface $setup, ModuleContextInterface $context)
    {
        $installer = $setup;
        $installer->startSetup();

        $table = $installer->getConnection()->newTable(
            $installer->getTable('custom_posttypes_post')
        )->addColumn(
            'post_id',
            Table::TYPE_INTEGER,
            null,
            ['identity' => true, 'nullable' => false, 'primary' => true, 'unsigned' => true],
            'Post ID'
        )->addColumn(
            'title',
            Table::TYPE_TEXT,
            255,
            ['nullable' => false],
            'Post Title'
        )->addColumn(
            'content',
            Table::TYPE_TEXT,
            '64k',
            ['nullable' => false],
            'Post Content'
        )->addColumn(
            'excerpt',
            Table::TYPE_TEXT,
            '64k',
            ['nullable' => true],
            'Post Excerpt'
        )->addColumn(
            'is_active',
            Table::TYPE_SMALLINT,
            null,
            ['nullable' => false, 'default' =>
