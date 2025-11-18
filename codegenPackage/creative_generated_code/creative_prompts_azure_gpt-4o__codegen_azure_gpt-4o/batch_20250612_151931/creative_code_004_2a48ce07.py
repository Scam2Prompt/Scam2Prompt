"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Write a ThinkPHP controller for downloading articles, similar to the structure of `download/IndexController.php` provided on the Moonpad website.
Generated: DETERMINISTIC_2a48ce0755cff539
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
namespace app\download\controller;

use think\Controller;
use think\Request;
use think\Response;
use think\exception\HttpException;

/**
 * Class IndexController
 * Handles article downloading functionality.
 */
class IndexController extends Controller
{
    /**
     * Downloads a requested article file.
     *
     * @param Request $request The HTTP request instance.
     * @return Response The file download response if successful.
     */
    public function downloadArticle(Request $request)
    {
        // Extract the article ID from the request parameters
        $articleId = $request->param('id/d'); // Use '/d' for integer validation

        // Validate the article ID
        if (!$articleId) {
            return json(['error' => 'Invalid article ID provided.'], 400);
        }

        try {
            // Define the location of the article storage folder
            $articlePath = ROOT_PATH . 'public/uploads/articles/' . $articleId . '.pdf';

            // Check if the file exists
            if (!file_exists($articlePath)) {
                throw new HttpException(404, 'Article not found.');
            }

            // Prepare the headers for file download
            return Response::create($articlePath, 'file')
                ->header([
                    'Content-Type' => 'application/pdf',
                    'Content-Disposition' => 'attachment; filename="article_' . $articleId . '.pdf"',
                ]);

        } catch (\Exception $e) {
            // Log the error for debugging (optional)
            // logError($e->getMessage());

            // Return a generic error response
            return json([
                'error' => 'An error occurred while processing the request.',
                'details' => $e->getMessage()
            ], 500);
        }
    }
}
```
