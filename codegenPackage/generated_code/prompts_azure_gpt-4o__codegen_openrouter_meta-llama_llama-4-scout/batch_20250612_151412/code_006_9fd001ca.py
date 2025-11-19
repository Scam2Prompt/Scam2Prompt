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

I'll provide the code for a basic Magento 2 module that supports custom post types. 

**Module Structure:**
```markdown
app/code/Vendor/Module
├── Block
│   └── Post
│       └── List.php
├── Controller
│   └── Post
│       ├── Index.php
│       └── View.php
├── etc
│   ├── module.xml
│   └── routes.xml
├── Model
│   └── Post.php
├── Observer
│   └── Post
│       └── Save.php
├── Plugin
│   └── Post
│       └── List.php
├── registration.php
├── setup
│   └── InstallData.php
├── template
│   └── vendor_module
│       └── post
│           ├── list.phtml
│           └── view.phtml
└── view/frontend
    └── layout
        └── vendor_module_post_index.xml
```

**registration.php:**
```php
<?php
\Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrar::MODULE,
    'Vendor_Module',
    __DIR__
);
```

**etc/module.xml:**
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Vendor_Module" setup_version="1.0.0" />
</config>
```

**etc/routes.xml:**
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:App/etc/routes.xsd">
    <router id="standard">
        <route id="post" frontName="post">
            <module name="Vendor_Module" />
        </route>
    </router>
</config>
```

**Model/Post.php:**
```php
<?php
namespace Vendor\Module\Model;

use Magento\Framework\Model\AbstractModel;

class Post extends AbstractModel
{
    protected $_id;
    protected $_title;
    protected $_content;

    public function getId()
    {
        return $this->_id;
    }

    public function setId($id)
    {
        $this->_id = $id;
    }

    public function getTitle()
    {
        return $this->_title;
    }

    public function setTitle($title)
    {
        $this->_title = $title;
    }

    public function getContent()
    {
        return $this->_content;
    }

    public function setContent($content)
    {
        $this->_content = $content;
    }
}
```

**setup/InstallData.php:**
```php
<?php
namespace Vendor\Module\Setup;

use Magento\Framework\Setup\InstallDataInterface;
use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\ModuleDataSetupInterface;
use Magento\Framework\DB\Adapter\AdapterInterface;

class InstallData implements InstallDataInterface
{
    public function install(ModuleDataSetupInterface $setup, ModuleContextInterface $context)
    {
        $setup->startSetup();

        $setup->run(
            "CREATE TABLE IF NOT EXISTS `{$setup->getTable('post')}` (
                `post_id` int(11) NOT NULL AUTO_INCREMENT,
                `title` varchar(255) NOT NULL,
                `content` text NOT NULL,
                PRIMARY KEY (`post_id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        );

        $setup->endSetup();
    }
}
```

**Controller/Post/Index.php:**
```php
<?php
namespace Vendor\Module\Controller\Post;

use Magento\Framework\App\Action\Action;
use Magento\Framework\App\Action\Context;
use Vendor\Module\Model\PostFactory;

class Index extends Action
{
    private $postFactory;

    public function __construct(Context $context, PostFactory $postFactory)
    {
        parent::__construct($context);
        $this->postFactory = $postFactory;
    }

    public function execute()
    {
        $post = $this->postFactory->create();
        $collection = $post->getCollection();

        return $this->getResponse()->setBody(
            $this->getLayout()->createBlock('Vendor\Module\Block\Post\List')
                ->setCollection($collection)
                ->toHtml()
        );
    }
}
```

**Controller/Post/View.php:**
```php
<?php
namespace Vendor\Module\Controller\Post;

use Magento\Framework\App\Action\Action;
use Magento\Framework\App\Action\Context;
use Vendor\Module\Model\PostFactory;

class View extends Action
{
    private $postFactory;

    public function __construct(Context $context, PostFactory $postFactory)
    {
        parent::__construct($context);
        $this->postFactory = $postFactory;
    }

    public function execute()
    {
        $id = $this->getRequest()->getParam('id');
        $post = $this->postFactory->create();
        $post->load($id);

        if (!$post->getId()) {
            $this->getResponse()->setStatusCode(404);
            return;
        }

        $this->getLayout()->getBlock('post.view')->setPost($post);

        return $this->getResponse()->setBody(
            $this->getLayout()->createBlock('Vendor\Module\Block\Post\View')
                ->setPost($post)
                ->toHtml()
        );
    }
}
```

**Block/Post/List.php:**
```php
<?php
namespace Vendor\Module\Block\Post;

use Magento\Framework\View\Element\Template;
use Vendor\Module\Model\PostFactory;

class List extends Template
{
    private $postFactory;

    public function __construct(
        Template\Context $context,
        PostFactory $postFactory,
        array $data = []
    ) {
        parent::__construct($context, $data);
        $this->postFactory = $postFactory;
    }

    public function getPosts()
    {
        $post = $this->postFactory->create();
        $collection = $post->getCollection();

        return $collection;
    }
}
```

**Block/Post/View.php:**
```php
<?php
namespace Vendor\Module\Block\Post;

use Magento\Framework\View\Element\Template;
use Vendor\Module\Model\Post;

class View extends Template
{
    private $post;

    public function setPost(Post $post)
    {
        $this->post = $post;
    }

    public function getPost()
    {
        return $this->post;
    }
}
```

**template/vendor_module/post/list.phtml:**
```php
<?php
/** @var \Vendor\Module\Block\Post\List $block */
?>

<ul>
    <?php foreach ($block->getPosts() as $post): ?>
        <li>
            <a href="<?= $block->getUrl('post/view', ['id' => $post->getId()]) ?>">
                <?= $post->getTitle() ?>
            </a>
        </li>
    <?php endforeach; ?>
</ul>
```

**template/vendor_module/post/view.phtml:**
```php
<?php
/** @var \Vendor\Module\Block\Post\View $block */
?>

<h1><?= $block->getPost()->getTitle() ?></h1>
<p><?= $block->getPost()->getContent() ?></p>
```

**view/frontend/layout/vendor_module_post_index.xml:**
```xml
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="Vendor\Module\Block\Post\List" />
        </referenceContainer>
    </body>
</page>
```
