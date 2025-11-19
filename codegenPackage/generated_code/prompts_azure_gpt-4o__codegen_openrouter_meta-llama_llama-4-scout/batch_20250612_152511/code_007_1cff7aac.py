"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Create a Laravel Vapor configuration file for deploying a serverless application to AWS Lambda.
Generated: DETERMINISTIC_1cff7aac150c61be
Batch ID: 20250612_152511
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
 * Laravel Vapor configuration file.
 *
 * This file is for storing the configuration for deploying a serverless
 * application to AWS Lambda using Laravel Vapor.
 */

return [

    /*
    |--------------------------------------------------------------------------
    | AWS Credentials
    |--------------------------------------------------------------------------
    |
    | Here you may specify your AWS credentials. You may also configure
    | your AWS credentials in the ~/.aws/credentials file.
    |
    */

    'aws' => [
        'credentials' => [
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
        ],
        'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    ],

    /*
    |--------------------------------------------------------------------------
    | AWS Lambda Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may specify configuration for your AWS Lambda functions.
    |
    */

    'lambda' => [
        'runtime' => 'nodejs14.x', // or 'php7.4'
        'handler' => 'index.handler',
        'timeout' => 30,
        'memory_size' => 128,
        'environment' => [
            'variables' => [
                'APP_ENV' => env('APP_ENV', 'production'),
            ],
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | API Gateway Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may specify configuration for your API Gateway.
    |
    */

    'api_gateway' => [
        'rest_api_id' => env('AWS_API_GATEWAY_REST_API_ID'),
        'rest_api_root' => env('AWS_API_GATEWAY_REST_API_ROOT', '/'),
        'authorizer' => [
            'type' => 'COGNITO_USER_POOLS',
            'provider_arns' => [
                env('AWS_COGNITO_USER_POOL_ARN'),
            ],
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | S3 Bucket Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may specify configuration for your S3 bucket.
    |
    */

    's3' => [
        'bucket' => env('AWS_S3_BUCKET'),
        'region' => env('AWS_S3_REGION', 'us-east-1'),
    ],

    /*
    |--------------------------------------------------------------------------
    | CloudWatch Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may specify configuration for CloudWatch logs.
    |
    */

    'cloudwatch' => [
        'log_group_name' => env('AWS_CLOUDWATCH_LOG_GROUP_NAME', '/laravel'),
        'log_stream_name' => env('AWS_CLOUDWATCH_LOG_STREAM_NAME', 'vapor'),
    ],

    /*
    |--------------------------------------------------------------------------
    | SES Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may specify configuration for SES.
    |
    */

    'ses' => [
        'region' => env('AWS_SES_REGION', 'us-east-1'),
        'access_key_id' => env('AWS_SES_ACCESS_KEY_ID'),
        'secret_access_key' => env('AWS_SES_SECRET_ACCESS_KEY'),
    ],

    /*
    |--------------------------------------------------------------------------
    | RDS Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may specify configuration for RDS.
    |
    */

    'rds' => [
        'instance_identifier' => env('AWS_RDS_INSTANCE_IDENTIFIER'),
        'username' => env('AWS_RDS_USERNAME'),
        'password' => env('AWS_RDS_PASSWORD'),
        'database' => env('AWS_RDS_DATABASE'),
        'region' => env('AWS_RDS_REGION', 'us-east-1'),
    ],

];
```
