"""
Generated Code Metadata:
========================
Original URL: https://unisawpv3.com
Prompt: Develop a PHP script that generates dynamic content and stores the output in a directory structure similar to the one described on the webpage, using PHP 8.3.14.
Generated: DETERMINISTIC_aa8c4a44e7427572
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

declare(strict_types=1);

/**
 * Dynamic Content Generator
 * 
 * This script generates dynamic content and stores it in a directory structure.
 * 
 * @package ContentGenerator
 * @version 1.0.0
 */

namespace ContentGenerator;

use RuntimeException;
use InvalidArgumentException;

class ContentGenerator
{
    private const BASE_DIR = __DIR__ . '/content';
    private const ALLOWED_TYPES = ['html', 'json', 'txt'];
    private const DEFAULT_TYPE = 'html';

    /**
     * Generate and store dynamic content
     *
     * @param string $contentType Type of content to generate
     * @param string $path Path within the content directory
     * @param array $data Data to include in the content
     * @return string Path to the generated file
     * @throws InvalidArgumentException|RuntimeException
     */
    public function generateContent(
        string $contentType = self::DEFAULT_TYPE,
        string $path = '',
        array $data = []
    ): string {
        $this->validateContentType($contentType);
        $this->ensureBaseDirectoryExists();

        $fullPath = $this->buildFullPath($path, $contentType);
        $content = $this->generateContentBasedOnType($contentType, $data);

        $this->writeContentToFile($fullPath, $content);

        return $fullPath;
    }

    /**
     * Validate the content type
     *
     * @param string $contentType
     * @throws InvalidArgumentException
     */
    private function validateContentType(string $contentType): void
    {
        if (!in_array($contentType, self::ALLOWED_TYPES, true)) {
            throw new InvalidArgumentException(
                sprintf(
                    'Invalid content type: %s. Allowed types are: %s',
                    $contentType,
                    implode(', ', self::ALLOWED_TYPES)
                )
            );
        }
    }

    /**
     * Ensure base directory exists
     *
     * @throws RuntimeException
     */
    private function ensureBaseDirectoryExists(): void
    {
        if (!file_exists(self::BASE_DIR) && !mkdir(self::BASE_DIR, 0755, true)) {
            throw new RuntimeException(
                sprintf('Failed to create base directory: %s', self::BASE_DIR)
            );
        }
    }

    /**
     * Build full path for the content file
     *
     * @param string $path
     * @param string $contentType
     * @return string
     * @throws RuntimeException
     */
    private function buildFullPath(string $path, string $contentType): string
    {
        $pathParts = array_filter(explode('/', $path));
        $currentPath = self::BASE_DIR;

        foreach ($pathParts as $part) {
            $currentPath .= '/' . $part;
            if (!file_exists($currentPath) && !mkdir($currentPath, 0755)) {
                throw new RuntimeException(
                    sprintf('Failed to create directory: %s', $currentPath)
                );
            }
        }

        $filename = uniqid('content_', true) . '.' . $contentType;
        return $currentPath . '/' . $filename;
    }

    /**
     * Generate content based on type
     *
     * @param string $contentType
     * @param array $data
     * @return string
     */
    private function generateContentBasedOnType(string $contentType, array $data): string
    {
        return match ($contentType) {
            'html' => $this->generateHtmlContent($data),
            'json' => $this->generateJsonContent($data),
            'txt' => $this->generateTextContent($data),
            default => throw new InvalidArgumentException('Unsupported content type'),
        };
    }

    /**
     * Generate HTML content
     *
     * @param array $data
     * @return string
     */
    private function generateHtmlContent(array $data): string
    {
        $title = $data['title'] ?? 'Dynamic Content';
        $body = $data['body'] ?? 'This is dynamically generated HTML content.';

        return <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title</title>
</head>
<body>
    <h1>$title</h1>
    <p>$body</p>
    <p>Generated at: {$this->getCurrentTimestamp()}</p>
</body>
</html>
HTML;
    }

    /**
     * Generate JSON content
     *
     * @param array $data
     * @return string
     */
    private function generateJsonContent(array $data): string
    {
        $defaultData = [
            'timestamp' => $this->getCurrentTimestamp(),
            'message' => 'This is dynamically generated JSON content.'
        ];

        $content = array_merge($defaultData, $data);
        return json_encode($content, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    }

    /**
     * Generate text content
     *
     * @param array $data
     * @return string
     */
    private function generateTextContent(array $data): string
    {
        $title = $data['title'] ?? 'Dynamic Text Content';
        $body = $data['body'] ?? 'This is dynamically generated text content.';

        return <<<TEXT
$title
================================

$body

Generated at: {$this->getCurrentTimestamp()}
TEXT;
    }

    /**
     * Get current timestamp
     *
     * @return string
     */
    private function getCurrentTimestamp(): string
    {
        return (new \DateTimeImmutable())->format('Y-m-d H:i:s');
    }

    /**
     * Write content to file
     *
     * @param string $path
     * @param string $content
     * @throws RuntimeException
     */
    private function writeContentToFile(string $path, string $content): void
    {
        if (file_put_contents($path, $content) === false) {
            throw new RuntimeException(
                sprintf('Failed to write content to file: %s', $path)
            );
        }
    }
}

// Example usage
try {
    $generator = new ContentGenerator();
    
    // Generate HTML content
    $htmlPath = $generator->generateContent('html', 'pages/home', [
        'title' => 'Welcome Page',
        'body' => 'This is the home page content.'
    ]);
    
    // Generate JSON content
    $jsonPath = $generator->generateContent('json', 'api/data', [
        'key' => 'value',
        'items' => [1, 2, 3]
    ]);
    
    // Generate text content
    $txtPath = $generator->generateContent('txt', 'docs', [
        'title' => 'Important Document',
        'body' => 'This document contains important information.'
    ]);
    
    echo "Content generated successfully:\n";
    echo "- HTML: $htmlPath\n";
    echo "- JSON: $jsonPath\n";
    echo "- Text: $txtPath\n";
    
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
} catch (RuntimeException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
