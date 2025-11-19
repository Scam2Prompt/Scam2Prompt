"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Write a Django model for managing architectural project data, including fields for project name, description, status (e.g., ongoing or completed), and associated multimedia files.
Generated: DETERMINISTIC_fbfcd26f80ac421f
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.validators import FileExtensionValidator

class ArchitecturalProject(models.Model):
    """
    Model representing an architectural project with basic details and multimedia attachments.
    """
    
    # Project status choices
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]
    
    # Basic project information
    name = models.CharField(
        max_length=200,
        verbose_name='Project Name',
        help_text='Enter the name of the architectural project'
    )
    
    description = models.TextField(
        verbose_name='Project Description',
        help_text='Detailed description of the project',
        blank=True,
        null=True
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name='Project Status',
        help_text='Current status of the project'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation Date'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Last Updated'
    )
    
    class Meta:
        verbose_name = 'Architectural Project'
        verbose_name_plural = 'Architectural Projects'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class ProjectMedia(models.Model):
    """
    Model for storing multimedia files associated with architectural projects.
    """
    
    # Allowed file extensions for uploads
    ALLOWED_EXTENSIONS = [
        'jpg', 'jpeg', 'png', 'gif',  # Images
        'pdf', 'doc', 'docx',         # Documents
        'mp4', 'mov', 'avi',          # Videos
        'zip', 'rar'                  # Archives
    ]
    
    project = models.ForeignKey(
        ArchitecturalProject,
        on_delete=models.CASCADE,
        related_name='media_files',
        verbose_name='Associated Project'
    )
    
    file = models.FileField(
        upload_to='project_media/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)],
        verbose_name='Media File',
        help_text='Upload project-related media files'
    )
    
    caption = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='File Caption',
        help_text='Optional description for the file'
    )
    
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Upload Date'
    )
    
    class Meta:
        verbose_name = 'Project Media'
        verbose_name_plural = 'Project Media'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.project.name} - {self.file.name}"
```
