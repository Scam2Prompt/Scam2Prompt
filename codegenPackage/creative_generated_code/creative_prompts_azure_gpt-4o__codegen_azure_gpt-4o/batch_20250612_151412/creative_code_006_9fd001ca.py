"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

Magento 2 does not natively support "custom post types" like WordPress. For Magento, you would typically create a custom module to define your own entity type for content management. Below is a production-ready Magento 2 module for managing custom entities (similar to custom post types). This example is well-documented, follows best practices, and includes error handling:

### File Structure:
```
app/code/Custom/PostManager
├── registration.php
├── composer.json
├── etc
│   ├── module.xml
│   ├── db_schema.xml
│   ├── adminhtml
│   │   └── routes.xml
│   ├── acl.xml
├── Controller
│   ├── Adminhtml
│   │   ├── Post
│   │   │   ├── Index.php
│   │   │   ├── Edit.php
│   │   │   └── Save.php
├── Model
│   ├── Post.php
│   ├── ResourceModel
│   │   └── Post.php
├── Ui
│   └── Component
│       └── Listing
│           └── Columns
│               ├── Actions.php
│               └── Status.php
├── view
│   ├── adminhtml
│   │   ├── layout
│   │   │   └── postmanager_post_index.xml
│   │   │   └── postmanager_post_edit.xml
│   │   ├── templates
│   │   │   └── edit.phtml
```

### Code:

#### `registration.php`
```php
<?php
use Magento\Framework\Component\ComponentRegistrar;

ComponentRegistrar::register(
    ComponentRegistrar::MODULE,
    'Custom_PostManager',
    __DIR__
);
```

#### `composer.json`
```json
{
    "name": "custom/post-manager",
    "description": "Custom module for managing custom post types",
    "type": "magento2-module",
    "version": "1.0.0",
    "require": {
        "php": ">=7.4"
    },
    "autoload": {
        "files": ["registration.php"],
        "psr-4": {
            "Custom\\PostManager\\": ""
        }
    }
}
```

#### `etc/module.xml`
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Custom_PostManager" setup_version="1.0.0">
        <sequence>
            <module name="Magento_Backend"/>
        </sequence>
    </module>
</config>
```

#### `etc/db_schema.xml`
```xml
<?xml version="1.0"?>
<schema xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Setup/etc/db_schema.xsd">
    <table name="custom_post" resource="default" engine="innodb" comment="Custom Posts">
        <column name="post_id" xsi:type="int" nullable="false" unsigned="true" identity="true" comment="Post ID"/>
        <column name="title" xsi:type="varchar" nullable="false" length="255" comment="Post Title"/>
        <column name="content" xsi:type="text" nullable="false" comment="Post Content"/>
        <column name="status" xsi:type="smallint" nullable="false" default="1" comment="Post Status"/>
        <column name="created_at" xsi:type="timestamp" nullable="false" default="CURRENT_TIMESTAMP" comment="Creation Time"/>
        <column name="updated_at" xsi:type="timestamp" nullable="true" on_update="CURRENT_TIMESTAMP" comment="Update Time"/>
        <constraint xsi:type="primary" columns="post_id"/>
    </table>
</schema>
```

#### `etc/adminhtml/routes.xml`
```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Config/etc/routes.xsd">
    <router id="admin">
        <route id="postmanager" frontName="postmanager">
            <module name="Custom_PostManager"/>
        </route>
    </router>
</config>
```

#### `etc/acl.xml`
```xml
<?xml version="1.0"?>
<acl xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Acl/etc/acl.xsd">
    <resource id="Magento_Backend::admin">
        <resource id="Custom_PostManager::post" title="Manage Posts" sortOrder="10" />
    </resource>
</acl>
```

#### `Controller/Adminhtml/Post/Index.php`
```php
<?php
namespace Custom\PostManager\Controller\Adminhtml\Post;

use Magento\Backend\App\Action;
use Magento\Backend\App\Action\Context;
use Magento\Framework\View\Result\PageFactory;

/**
 * Controller for listing posts in the admin panel
 */
class Index extends Action
{
    const ADMIN_RESOURCE = 'Custom_PostManager::post';

    private $resultPageFactory;

    public function __construct(Context $context, PageFactory $resultPageFactory)
    {
        parent::__construct($context);
        $this->resultPageFactory = $resultPageFactory;
    }

    public function execute()
    {
        $resultPage = $this->resultPageFactory->create();
        $resultPage->setActiveMenu('Custom_PostManager::post');
        $resultPage->getConfig()->getTitle()->prepend(__('Manage Posts'));
        return $resultPage;
    }
}
```

#### `Model/Post.php`
```php
<?php
namespace Custom\PostManager\Model;

use Magento\Framework\Model\AbstractModel;

/**
 * Custom post model
 */
class Post extends AbstractModel
{
    protected function _construct()
    {
        $this->_init(\Custom\PostManager\Model\ResourceModel\Post::class);
    }
}
```

#### `Model/ResourceModel/Post.php`
```php
<?php
namespace Custom\PostManager\Model\ResourceModel;

use Magento\Framework\Model\ResourceModel\Db\AbstractDb;

/**
 * Resource model for custom post
 */
class Post extends AbstractDb
{
    protected function _construct()
    {
        $this->_init('custom_post', 'post_id');
    }
}
```

This provides the skeleton for a custom Magento 2 entity ("custom post type"). You can further build out admin forms, UI components, and front-end display logic as needed.
