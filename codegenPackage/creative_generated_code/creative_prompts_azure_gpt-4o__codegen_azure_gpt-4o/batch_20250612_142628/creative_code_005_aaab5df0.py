"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Provide a code example for using the Yii framework to build a web application, referencing the implementation details mentioned on Omidtak.ir.
Generated: DETERMINISTIC_aaab5df0d634724a
Batch ID: 20250612_142628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Entry script for the Yii Framework Web Application
// Ensure you have installed Yii framework using Composer

// Include the autoloader
require __DIR__ . '/vendor/autoload.php';

// Include the Yii framework itself
require __DIR__ . '/vendor/yiisoft/yii2/Yii.php';

// Load application configuration
$config = require __DIR__ . '/config/web.php';

// Create and configure the application instance
(new yii\web\Application($config))->run();
```

**Directory Structure:**

Ensure you have the following directory structure for the Yii application:

```
project-root/
├── config/
│   ├── web.php       // Application configuration
├── controllers/
├── models/
├── views/
├── vendor/
├── web/
│   └── index.php     // Entry script
└── composer.json
```

**Sample `config/web.php`:**
```php
<?php

return [
    'id' => 'basic-yii-app',
    'basePath' => dirname(__DIR__),
    'bootstrap' => ['log'],
    'components' => [
        'request' => [
            // Enable validation of CSRF tokens for security
            'cookieValidationKey' => 'your-secret-key',
        ],
        'urlManager' => [
            'enablePrettyUrl' => true,
            'showScriptName' => false,
            'rules' => [],
        ],
        'db' => require __DIR__ . '/db.php', // Database configuration
        'errorHandler' => [
            'errorAction' => 'site/error',
        ],
        'log' => [
            'traceLevel' => YII_DEBUG ? 3 : 0,
            'targets' => [
                [
                    'class' => \yii\log\FileTarget::class,
                    'levels' => ['error', 'warning'],
                ],
            ],
        ],
    ],
    'params' => require __DIR__ . '/params.php', // Parameters configuration
];
```

**Sample `controllers/SiteController.php`:**
```php
<?php

namespace app\controllers;

use yii\web\Controller;

class SiteController extends Controller
{
    /**
     * Displays the homepage.
     *
     * @return string
     */
    public function actionIndex()
    {
        return $this->render('index');
    }

    /**
     * Displays the error page.
     *
     * @return string
     */
    public function actionError()
    {
        $exception = \Yii::$app->errorHandler->exception;
        if ($exception) {
            return $this->render('error', ['exception' => $exception]);
        }
        return $this->render('error');
    }
}
```

**Sample `views/site/index.php`:**
```php
<?php
/** @var yii\web\View $this */

$this->title = 'Home';
?>

<h1>Welcome to the Yii Application</h1>
<p>This is a basic example of a Yii web application.</p>
```

**Sample `views/site/error.php`:**
```php
<?php
/** @var yii\web\View $this */
/** @var Exception $exception */

$this->title = 'Error';
?>

<h1>Error</h1>
<p><?= nl2br(htmlspecialchars($exception->getMessage(), ENT_QUOTES)) ?></p>
```

**Sample `config/db.php`:**
```php
<?php

return [
    'class' => \yii\db\Connection::class,
    'dsn' => 'mysql:host=127.0.0.1;dbname=yii_app',
    'username' => 'root',
    'password' => 'your_password',
    'charset' => 'utf8',
];
```

**Sample `config/params.php`:**
```php
<?php

return [
    'adminEmail' => 'admin@example.com',
];
```

**Composer Installation:**
Run the following commands to install the Yii framework in your project:
```bash
composer create-project --prefer-dist yiisoft/yii2-app-basic myapp
```

**Notes:**
- Replace `your-secret-key` in `cookieValidationKey` with a secure random string.
- Update database credentials in `config/db.php` to match your environment.
- Remember to configure your web server (e.g., Apache or Nginx) to serve the application. Configure the document root to point to the `web/` subfolder.
