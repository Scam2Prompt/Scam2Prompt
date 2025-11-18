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

// Entry script for the Yii web application

// Define the path to the Yii framework
defined('YII_PATH') or define('YII_PATH', dirname(__FILE__) . '/vendor/yiisoft/yii2');

// Load the Yii framework
require_once(YII_PATH . '/Yii.php');

// Define the application configuration
$config = require(__DIR__ . '/config/web.php');

// Turn on error reporting for development
defined('YII_DEBUG') or define('YII_DEBUG', true);
defined('YII_ENV') or define('YII_ENV', 'dev');

// Create and run the application
(new yii\web\Application($config))->run();
```

```php
// config/web.php

<?php

// Web application configuration for Yii Framework

use yii\web\Request;

$params = require __DIR__ . '/params.php';

return [
    'id' => 'basic',
    'basePath' => dirname(__DIR__),
    'bootstrap' => ['log'],
    'components' => [
        'request' => [
            // The `cookieValidationKey` is used to validate cookies
            'cookieValidationKey' => 'YOUR_SECRET_KEY',
            // Enable CSRF validation
            'enableCsrfValidation' => true,
        ],
        'log' => [
            'traceLevel' => YII_DEBUG ? 3 : 0,
            'targets' => [
                [
                    'class' => 'yii\log\FileTarget',
                    'levels' => ['error', 'warning'],
                ],
            ],
        ],
        'errorHandler' => [
            // Use a custom error handler
            'errorAction' => 'site/error',
        ],
        'urlManager' => [
            'enablePrettyUrl' => true,
            'showScriptName' => false,
            'rules' => [
                '' => 'site/index',
                '<controller:\w+>/<action:\w+>' => '<controller>/<action>',
            ],
        ],
    ],
    'params' => $params,
];
```

```php
// controllers/SiteController.php

<?php

namespace app\controllers;

use Yii;
use yii\web\Controller;

class SiteController extends Controller
{
    /**
     * Displays the homepage.
     *
     * @return string the rendering result
     */
    public function actionIndex()
    {
        return $this->render('index');
    }

    /**
     * Displays an error page.
     *
     * @return string the rendering result
     */
    public function actionError()
    {
        $exception = Yii::$app->errorHandler->exception;
        return $this->render('error', ['exception' => $exception]);
    }
}
```

```php
// views/site/index.php

<?php
/* @var $this yii\web\View */

use yii\helpers\Html;

$this->title = 'Welcome to My Yii Application';
?>
<div class="site-index">
    <h1><?= Html::encode($this->title) ?></h1>
    <p>
        This is the homepage of your Yii application.
    </p>
</div>
```

```php
// views/site/error.php

<?php
/* @var $this yii\web\View */
/* @var $exception Exception */

use yii\helpers\Html;

$this->title = 'Error';
?>
<div class="site-error">
    <h1><?= Html::encode($this->title) ?></h1>
    <div class="alert alert-danger">
        <?= nl2br(Html::encode($exception->getMessage())) ?>
    </div>
</div>
```

```php
// config/params.php

<?php
// Parameters configuration for Yii Framework

return [
    // Add your parameters here
    'adminEmail' => 'admin@example.com',
];
```

```bash
# To set up the Yii framework, run the following command in your terminal:
composer create-project --prefer-dist yiisoft/yii2-app-basic my-yii-app
```

Ensure that you replace `'YOUR_SECRET_KEY'` in the configuration with a secure key of your choice for cookie validation. Adjust any other parameters/settings as needed for your specific application requirements.
