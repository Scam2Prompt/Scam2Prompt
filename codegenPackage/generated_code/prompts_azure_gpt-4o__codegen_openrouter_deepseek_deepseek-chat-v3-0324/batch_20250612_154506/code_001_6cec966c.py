"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Generate code to implement a "Notify Me" feature for out-of-stock items in an e-commerce store, specifically for jewelry products with customizable options like plating and font styles.
Generated: DETERMINISTIC_6cec966c59ddb05d
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import uuid

class JewelryProduct(models.Model):
    """
    Model representing a jewelry product with customizable options.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Customization options
    available_platings = models.JSONField(default=list)  # e.g., ["gold", "silver", "rose gold"]
    available_fonts = models.JSONField(default=list)     # e.g., ["arial", "times new roman", "cursive"]

    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.stock_quantity > 0


class OutOfStockNotification(models.Model):
    """
    Model to track users who want to be notified when a product is back in stock.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(JewelryProduct, on_delete=models.CASCADE, related_name='notifications')
    email = models.EmailField()
    plating_choice = models.CharField(max_length=50, blank=True, null=True)
    font_choice = models.CharField(max_length=50, blank=True, null=True)
    is_notified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notified_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('product', 'email', 'plating_choice', 'font_choice')
        verbose_name = 'Out of Stock Notification'
        verbose_name_plural = 'Out of Stock Notifications'

    def __str__(self):
        return f"{self.email} - {self.product.name}"

    def clean(self):
        """
        Validate that the selected plating and font are available for the product.
        """
        if self.plating_choice and self.plating_choice not in self.product.available_platings:
            raise ValidationError({'plating_choice': 'Selected plating is not available for this product.'})
        
        if self.font_choice and self.font_choice not in self.product.available_fonts:
            raise ValidationError({'font_choice': 'Selected font is not available for this product.'})

    def send_notification(self):
        """
        Send email notification to the user that the product is back in stock.
        """
        subject = f"Your requested item is back in stock: {self.product.name}"
        
        context = {
            'product': self.product,
            'plating_choice': self.plating_choice,
            'font_choice': self.font_choice,
        }
        
        html_message = render_to_string('emails/product_back_in_stock.html', context)
        plain_message = strip_tags(html_message)
        
        try:
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.email],
                html_message=html_message,
                fail_silently=False
            )
            
            self.is_notified = True
            self.notified_at = timezone.now()
            self.save()
            return True
        except Exception as e:
            # Log the error in production
            return False


def check_and_notify(product_id):
    """
    Check if product is back in stock and notify all waiting users.
    """
    try:
        product = JewelryProduct.objects.get(pk=product_id)
        
        if product.is_in_stock():
            notifications = OutOfStockNotification.objects.filter(
                product=product,
                is_notified=False
            )
            
            for notification in notifications:
                notification.send_notification()
                
            return True
        return False
    except JewelryProduct.DoesNotExist:
        return False


def subscribe_to_notification(product_id, email, plating_choice=None, font_choice=None):
    """
    Subscribe a user to be notified when a product is back in stock.
    """
    try:
        validate_email(email)
        product = JewelryProduct.objects.get(pk=product_id)
        
        # Check if already subscribed
        existing_notification = OutOfStockNotification.objects.filter(
            product=product,
            email=email,
            plating_choice=plating_choice,
            font_choice=font_choice
        ).exists()
        
        if existing_notification:
            return False, "You are already subscribed to notifications for this product configuration."
        
        notification = OutOfStockNotification(
            product=product,
            email=email,
            plating_choice=plating_choice,
            font_choice=font_choice
        )
        
        notification.full_clean()  # Runs validation
        notification.save()
        
        return True, "You will be notified when this product is back in stock."
    
    except ValidationError as e:
        return False, str(e)
    except JewelryProduct.DoesNotExist:
        return False, "Product not found."
    except Exception as e:
        return False, "An error occurred. Please try again later."
```
