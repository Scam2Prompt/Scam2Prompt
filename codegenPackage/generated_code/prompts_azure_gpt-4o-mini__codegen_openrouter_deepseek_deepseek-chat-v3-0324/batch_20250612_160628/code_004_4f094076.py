"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Illustrate how to set up routing in a ThinkPHP application, including examples from the `think/Route.php` file to define resource routes.
Generated: DETERMINISTIC_4f09407677de612b
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// File: route/route.php

use think\facade\Route;

/**
 * Define resource routes for a sample 'posts' resource
 * This will automatically generate routes for CRUD operations
 */
Route::resource('posts', 'PostsController');

/**
 * Define a custom route with a specific HTTP method
 * This route will handle GET requests to '/about'
 */
Route::get('about', 'PagesController/about');

/**
 * Define a route with parameters
 * This route will match '/users/123' where 123 is the user ID
 */
Route::get('users/:id', 'UsersController/read');

/**
 * Define a route group with common prefix and middleware
 */
Route::group('api', function () {
    // Nested resource route
    Route::resource('comments', 'CommentsController');
})->middleware('Auth');

/**
 * Define a route with complex pattern and optional parameters
 */
Route::get('blog/:year/[:month]', 'BlogController/archive');

/**
 * Define a route with multiple HTTP methods
 */
Route::rule('products/:id', 'ProductsController/detail', 'GET|POST');

/**
 * Define a route with complete URL pattern
 */
Route::get('download/<file>', 'DownloadController/index')
    ->pattern(['file' => '\w+\.(zip|rar|pdf)']);

/**
 * Define a route with domain restriction
 */
Route::domain('admin', function () {
    Route::get('dashboard', 'AdminController/dashboard');
});

/**
 * Define a route with response caching
 */
Route::get('news/:id', 'NewsController/read')
    ->cache(3600);

/**
 * Define a route with request rate limiting
 */
Route::get('api/data', 'ApiController/getData')
    ->ext('json')
    ->limit(100, 60); // 100 requests per minute

/**
 * Define a route with redirect
 */
Route::redirect('old/path', 'new/path', 301);

/**
 * Define a route with miss routing
 */
Route::miss(function () {
    return '404 Not Found';
});

/**
 * Define a route with RESTful resource including only specific actions
 */
Route::resource('articles', 'ArticlesController')
    ->only(['index', 'read', 'create', 'save']);

/**
 * Define a route with RESTful resource excluding specific actions
 */
Route::resource('photos', 'PhotosController')
    ->except(['delete']);

/**
 * Define a route with additional methods for resource controller
 */
Route::resource('products', 'ProductsController')
    ->extras([
        'reviews' => ['get', '/:id/reviews', 'reviews'],
        'search'  => ['get', 'search', 'search']
    ]);
```
