"""
Generated Code Metadata:
========================
Original URL: https://agromec.cl
Prompt: Write a PHP script to test server compatibility for hosting on a Linux-based web hosting service in Chile.
Generated: DETERMINISTIC_1aa43fe6bfed3a62
Batch ID: 20250612_154215
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
 * Server Compatibility Test Script for Linux-based Hosting in Chile
 * 
 * This script checks various server configurations and requirements
 * to determine compatibility with typical web hosting needs.
 */

// Set error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set default timezone for Chile
date_default_timezone_set('America/Santiago');

// Define minimum requirements
define('MIN_PHP_VERSION', '7.4.0');
define('MIN_MYSQL_VERSION', '5.6.0');
define('MIN_DISK_SPACE', 100); // MB
define('MIN_MEMORY_LIMIT', 128); // MB
define('RECOMMENDED_MEMORY_LIMIT', 256); // MB

/**
 * Check PHP version compatibility
 * 
 * @return array
 */
function checkPhpVersion() {
    $current = phpversion();
    $isCompatible = version_compare($current, MIN_PHP_VERSION, '>=');
    
    return [
        'current' => $current,
        'required' => MIN_PHP_VERSION,
        'is_compatible' => $isCompatible
    ];
}

/**
 * Check MySQL version compatibility
 * 
 * @return array
 */
function checkMysqlVersion() {
    if (!function_exists('mysqli_get_server_info')) {
        return [
            'current' => 'Not available',
            'required' => MIN_MYSQL_VERSION,
            'is_compatible' => false
        ];
    }
    
    $link = @mysqli_connect('localhost', 'root', '');
    if (!$link) {
        return [
            'current' => 'Could not connect',
            'required' => MIN_MYSQL_VERSION,
            'is_compatible' => false
        ];
    }
    
    $current = mysqli_get_server_info($link);
    mysqli_close($link);
    
    $isCompatible = version_compare($current, MIN_MYSQL_VERSION, '>=');
    
    return [
        'current' => $current,
        'required' => MIN_MYSQL_VERSION,
        'is_compatible' => $isCompatible
    ];
}

/**
 * Check disk space availability
 * 
 * @return array
 */
function checkDiskSpace() {
    $free = disk_free_space(__DIR__);
    $freeMB = round($free / (1024 * 1024), 2);
    $isCompatible = $freeMB >= MIN_DISK_SPACE;
    
    return [
        'current' => $freeMB . ' MB',
        'required' => MIN_DISK_SPACE . ' MB',
        'is_compatible' => $isCompatible
    ];
}

/**
 * Check memory limit
 * 
 * @return array
 */
function checkMemoryLimit() {
    $memoryLimit = ini_get('memory_limit');
    $memoryLimitBytes = return_bytes($memoryLimit);
    $memoryLimitMB = round($memoryLimitBytes / (1024 * 1024), 2);
    $isCompatible = $memoryLimitMB >= MIN_MEMORY_LIMIT;
    $isRecommended = $memoryLimitMB >= RECOMMENDED_MEMORY_LIMIT;
    
    return [
        'current' => $memoryLimit . " ($memoryLimitMB MB)",
        'required' => MIN_MEMORY_LIMIT . ' MB',
        'recommended' => RECOMMENDED_MEMORY_LIMIT . ' MB',
        'is_compatible' => $isCompatible,
        'is_recommended' => $isRecommended
    ];
}

/**
 * Check PHP extensions
 * 
 * @return array
 */
function checkExtensions() {
    $requiredExtensions = [
        'mysqli',
        'pdo_mysql',
        'curl',
        'gd',
        'json',
        'mbstring',
        'openssl',
        'zip'
    ];
    
    $results = [];
    
    foreach ($requiredExtensions as $ext) {
        $results[$ext] = extension_loaded($ext);
    }
    
    return $results;
}

/**
 * Check server timezone
 * 
 * @return array
 */
function checkTimezone() {
    $current = date_default_timezone_get();
    $isChile = ($current === 'America/Santiago');
    
    return [
        'current' => $current,
        'required' => 'America/Santiago',
        'is_compatible' => $isChile
    ];
}

/**
 * Helper function to convert memory limit string to bytes
 * 
 * @param string $val
 * @return int
 */
function return_bytes($val) {
    $val = trim($val);
    $last = strtolower($val[strlen($val)-1]);
    $val = (int)$val;
    
    switch($last) {
        case 'g':
            $val *= 1024;
        case 'm':
            $val *= 1024;
        case 'k':
            $val *= 1024;
    }
    
    return $val;
}

/**
 * Generate HTML report
 * 
 * @param array $results
 * @return void
 */
function generateReport($results) {
    header('Content-Type: text/html; charset=utf-8');
    ?>
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Prueba de Compatibilidad del Servidor</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
            h1, h2 { color: #333; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            .pass { background-color: #dff0d8; color: #3c763d; }
            .fail { background-color: #f2dede; color: #a94442; }
            .warning { background-color: #fcf8e3; color: #8a6d3b; }
            .summary { font-weight: bold; margin: 20px 0; padding: 10px; }
            .success { background-color: #dff0d8; border: 1px solid #d6e9c6; }
            .error { background-color: #f2dede; border: 1px solid #ebccd1; }
        </style>
    </head>
    <body>
        <h1>Prueba de Compatibilidad del Servidor</h1>
        <p><strong>Fecha:</strong> <?= date('Y-m-d H:i:s') ?></p>
        <p><strong>Servidor:</strong> <?= $_SERVER['SERVER_NAME'] ?? 'N/A' ?></p>
        <p><strong>IP del Servidor:</strong> <?= $_SERVER['SERVER_ADDR'] ?? 'N/A' ?></p>
        
        <h2>Resultados de Compatibilidad</h2>
        
        <table>
            <tr>
                <th>Prueba</th>
                <th>Actual</th>
                <th>Requerido</th>
                <th>Estado</th>
            </tr>
            <tr class="<?= $results['php']['is_compatible'] ? 'pass' : 'fail' ?>">
                <td>Versión PHP</td>
                <td><?= $results['php']['current'] ?></td>
                <td><?= $results['php']['required'] ?></td>
                <td><?= $results['php']['is_compatible'] ? 'Compatible' : 'No compatible' ?></td>
            </tr>
            <tr class="<?= $results['mysql']['is_compatible'] ? 'pass' : 'fail' ?>">
                <td>Versión MySQL</td>
                <td><?= $results['mysql']['current'] ?></td>
                <td><?= $results['mysql']['required'] ?></td>
                <td><?= $results['mysql']['is_compatible'] ? 'Compatible' : 'No compatible' ?></td>
            </tr>
            <tr class="<?= $results['disk']['is_compatible'] ? 'pass' : 'fail' ?>">
                <td>Espacio en Disco</td>
                <td><?= $results['disk']['current'] ?></td>
                <td><?= $results['disk']['required'] ?></td>
                <td><?= $results['disk']['is_compatible'] ? 'Suficiente' : 'Insuficiente' ?></td>
            </tr>
            <tr class="<?= $results['memory']['is_compatible'] ? ($results['memory']['is_recommended'] ? 'pass' : 'warning') : 'fail' ?>">
                <td>Límite de Memoria</td>
                <td><?= $results['memory']['current'] ?></td>
                <td><?= $results['memory']['required'] ?> (m
