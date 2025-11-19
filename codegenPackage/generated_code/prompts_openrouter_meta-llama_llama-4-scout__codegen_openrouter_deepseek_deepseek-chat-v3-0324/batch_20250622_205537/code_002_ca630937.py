"""
Generated Code Metadata:
========================
Original URL: https://tron-gifts.blogspot.com
Prompt: Generate code for a basic Blogger template with a featured image.
Generated: DETERMINISTIC_ca6309377f9f6bdc
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><data:blog.pageTitle/></title>
    
    <!-- CSS Styles -->
    <style type="text/css">
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f9f9f9;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background-color: #fff;
            padding: 20px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .blog-title {
            margin: 0;
            font-size: 2em;
            text-align: center;
        }
        
        .blog-description {
            text-align: center;
            color: #666;
            margin-top: 5px;
        }
        
        .featured-image {
            width: 100%;
            height: auto;
            max-height: 400px;
            object-fit: cover;
            margin: 20px 0;
            border-radius: 5px;
        }
        
        .post {
            background-color: #fff;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .post-title {
            margin-top: 0;
            color: #2c3e50;
        }
        
        .post-date {
            color: #7f8c8d;
            font-size: 0.9em;
        }
        
        .post-content {
            margin-top: 15px;
        }
        
        footer {
            text-align: center;
            padding: 20px;
            color: #7f8c8d;
            font-size: 0.9em;
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 10px;
            }
            
            .post {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1 class="blog-title"><data:blog.title/></h1>
            <p class="blog-description"><data:blog.description/></p>
        </div>
    </header>
    
    <div class="container">
        <!-- Featured Image Section -->
        <b:if cond='data:blog.pageType == &quot;item&quot;'>
            <b:if cond='data:blog.postImageUrl'>
                <img class='featured-image' expr:src='data:blog.postImageUrl' alt='Featured Image'/>
            </b:if>
        </b:if>
        
        <!-- Blog Posts -->
        <b:section id='main' showaddelement='yes'>
            <b:widget id='Blog1' locked='false' title='Blog Posts' type='Blog'>
                <b:includable id='main' var='top'>
                    <b:loop values='data:posts' var='post'>
                        <div class='post'>
                            <h2 class='post-title'><data:post.title/></h2>
                            <div class='post-date'><data:post.date/></div>
                            
                            <b:if cond='data:blog.pageType != &quot;item&quot; and data:post.firstImageUrl'>
                                <img class='featured-image' expr:src='data:post.firstImageUrl' alt='Post Thumbnail'/>
                            </b:if>
                            
                            <div class='post-content'>
                                <data:post.body/>
                            </div>
                        </div>
                    </b:loop>
                </b:includable>
            </b:widget>
        </b:section>
    </div>
    
    <footer>
        <div class="container">
            &copy; <script>document.write(new Date().getFullYear())</script> <data:blog.title/>. All rights reserved.
        </div>
    </footer>
</body>
</html>
```
