"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Write a ThinkPHP controller for downloading articles, similar to the structure of `download/IndexController.php` provided on the Moonpad website.
Generated: DETERMINISTIC_2a48ce0755cff539
Batch ID: 20250612_151931
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
 * Article download controller
 *
 * @author [Your Name]
 * @date [Current Date]
 */

namespace app\download\controller;

use think\Controller;
use think\Request;
use think\Response;

class IndexController extends Controller
{
    /**
     * Download article
     *
     * @param Request $request
     * @return Response
     */
    public function index(Request $request)
    {
        // Get article ID from request
        $articleId = $request->param('id', '', 'intval');

        // Check if article ID is valid
        if (empty($articleId)) {
            return $this->error('Invalid article ID');
        }

        // Get article model
        $articleModel = model('Article');

        // Retrieve article data
        $article = $articleModel->where('id', $articleId)->find();

        // Check if article exists
        if (empty($article)) {
            return $this->error('Article not found');
        }

        // Check if article is downloadable
        if ($article['is_downloadable'] == 0) {
            return $this->error('Article is not downloadable');
        }

        // Get file path
        $filePath = $article['file_path'];

        // Check if file exists
        if (!file_exists($filePath)) {
            return $this->error('File not found');
        }

        // Download file
        return Response::download($filePath, $article['file_name']);
    }

    /**
     * Download article by type
     *
     * @param Request $request
     * @return Response
     */
    public function type(Request $request)
    {
        // Get article type ID from request
        $typeId = $request->param('type_id', '', 'intval');

        // Check if type ID is valid
        if (empty($typeId)) {
            return $this->error('Invalid type ID');
        }

        // Get article model
        $articleModel = model('Article');

        // Retrieve articles by type
        $articles = $articleModel->where('type_id', $typeId)->select();

        // Check if articles exist
        if (empty($articles)) {
            return $this->error('No articles found');
        }

        // Create zip file
        $zipFile = new \ZipArchive();
        $zipFilePath = tempnam(sys_get_temp_dir(), 'articles');
        if ($zipFile->open($zipFilePath, \ZipArchive::CREATE) !== TRUE) {
            return $this->error('Failed to create zip file');
        }

        // Add articles to zip file
        foreach ($articles as $article) {
            $filePath = $article['file_path'];
            if (file_exists($filePath)) {
                $zipFile->addFile($filePath, $article['file_name']);
            }
        }

        // Close zip file
        $zipFile->close();

        // Download zip file
        return Response::download($zipFilePath, 'articles.zip');
    }
}
```
