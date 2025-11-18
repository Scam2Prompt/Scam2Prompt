"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Write a ThinkPHP template file for rendering views, using the structure and syntax from `think-template/src/Template.php` on the Moonpad website.
Generated: DETERMINISTIC_f26263305c5eb1f1
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
// Load the ThinkPHP base classes
namespace app\view;

// Import necessary classes
use think\template\Template as BaseTemplate;
use think\View;
use think\exception\TemplateNotFoundException;

class Template extends BaseTemplate
{
    protected $view;

    public function __construct(View $view)
    {
        // Initialize the View object
        $this->view = $view;
    }

    /**
     * Render a template file with the provided data.
     *
     * @param string $template The template file to render.
     * @param array $data The data to pass to the template.
     * @return string Rendered template content.
     * @throws TemplateNotFoundException If the template file is not found.
     */
    public function render($template, array $data = [])
    {
        // Check if the template file exists
        if (!$this->view->exists($template)) {
            throw new TemplateNotFoundException("Template file '{$template}' not found.");
        }

        // Extract data to be used in the template
        extract($data);

        // Start output buffering
        ob_start();

        // Include the template file
        include $this->view->getTemplatePath($template);

        // Get the content from the output buffer
        $content = ob_get_clean();

        return $content;
    }

    /**
     * Set the view instance.
     *
     * @param View $view The view instance to set.
     * @return void
     */
    public function setView(View $view)
    {
        $this->view = $view;
    }

    /**
     * Get the view instance.
     *
     * @return View The current view instance.
     */
    public function getView()
    {
        return $this->view;
    }
}
```
