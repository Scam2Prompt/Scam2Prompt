"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Write JavaScript code to implement a mobile-friendly promo site with a photo gallery module and news feed, similar to the "Сайт-визитка" functionality described on https://ra-don.com.
Generated: DETERMINISTIC_5dd0c5b43fcc6a09
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Mobile-friendly promo site with photo gallery and news feed
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initApp();
});

function initApp() {
    try {
        // Check for mobile device
        if (/Mobi|Android|iPhone|iPad|iPod/i.test(navigator.userAgent)) {
            document.body.classList.add('mobile');
        }

        // Initialize modules
        initGallery();
        initNewsFeed();
        initMobileMenu();

        // Set up event listeners
        setupEventListeners();
    } catch (error) {
        console.error('Error initializing application:', error);
    }
}

// Photo Gallery Module
function initGallery() {
    const gallery = document.querySelector('.gallery');
    if (!gallery) return;

    const images = gallery.querySelectorAll('.gallery-item');
    const modal = document.createElement('div');
    modal.className = 'gallery-modal';
    modal.innerHTML = `
        <div class="modal-content">
            <span class="close">&times;</span>
            <img class="modal-image" src="" alt="">
            <div class="caption"></div>
            <a class="prev">&#10094;</a>
            <a class="next">&#10095;</a>
        </div>
    `;
    document.body.appendChild(modal);

    let currentIndex = 0;

    images.forEach((img, index) => {
        img.addEventListener('click', () => openModal(index));
    });

    function openModal(index) {
        currentIndex = index;
        const imgSrc = images[index].querySelector('img').src;
        const caption = images[index].getAttribute('data-caption') || '';
        
        modal.style.display = 'block';
        modal.querySelector('.modal-image').src = imgSrc;
        modal.querySelector('.caption').textContent = caption;
    }

    function closeModal() {
        modal.style.display = 'none';
    }

    function navigate(direction) {
        currentIndex += direction;
        if (currentIndex >= images.length) currentIndex = 0;
        if (currentIndex < 0) currentIndex = images.length - 1;
        openModal(currentIndex);
    }

    // Event listeners for modal
    modal.querySelector('.close').addEventListener('click', closeModal);
    modal.querySelector('.prev').addEventListener('click', () => navigate(-1));
    modal.querySelector('.next').addEventListener('click', () => navigate(1));

    // Close when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (modal.style.display === 'block') {
            if (e.key === 'Escape') closeModal();
            if (e.key === 'ArrowLeft') navigate(-1);
            if (e.key === 'ArrowRight') navigate(1);
        }
    });
}

// News Feed Module
function initNewsFeed() {
    const newsContainer = document.querySelector('.news-feed');
    if (!newsContainer) return;

    // Simulate fetching news data (in a real app, this would be an API call)
    const newsData = [
        {
            title: "Company Launches New Product",
            date: "2023-05-15",
            summary: "We're excited to announce our latest product line.",
            content: "Full details about the new product launch..."
        },
        {
            title: "Annual Conference Success",
            date: "2023-04-20",
            summary: "Our annual conference was a great success with record attendance.",
            content: "Details about the conference and key takeaways..."
        }
    ];

    // Render news items
    function renderNews() {
        newsContainer.innerHTML = '';
        newsData.forEach(item => {
            const newsItem = document.createElement('div');
            newsItem.className = 'news-item';
            newsItem.innerHTML = `
                <h3>${item.title}</h3>
                <div class="news-date">${formatDate(item.date)}</div>
                <p class="news-summary">${item.summary}</p>
                <button class="read-more">Read More</button>
                <div class="news-content" style="display:none">${item.content}</div>
            `;
            newsContainer.appendChild(newsItem);
        });

        // Add event listeners for read more buttons
        document.querySelectorAll('.read-more').forEach(button => {
            button.addEventListener('click', function() {
                const content = this.nextElementSibling;
                if (content.style.display === 'none') {
                    content.style.display = 'block';
                    this.textContent = 'Read Less';
                } else {
                    content.style.display = 'none';
                    this.textContent = 'Read More';
                }
            });
        });
    }

    function formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString(undefined, options);
    }

    renderNews();
}

// Mobile Menu
function initMobileMenu() {
    const menuButton = document.querySelector('.mobile-menu-button');
    const navMenu = document.querySelector('.main-nav');

    if (!menuButton || !navMenu) return;

    menuButton.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        this.classList.toggle('active');
    });
}

// General Event Listeners
function setupEventListeners() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        const lazyImages = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });

        lazyImages.forEach(img => imageObserver.observe(img));
    }
}

// CSS would be in a separate file, but included here for completeness
const style = document.createElement('style');
style.textContent = `
    /* Base styles */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        color: #333;
    }
    
    .container {
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 15px;
        box-sizing: border-box;
    }
    
    /* Mobile menu styles */
    .mobile-menu-button {
        display: none;
        background: none;
        border: none;
        font-size: 24px;
        cursor: pointer;
        padding: 10px;
    }
    
    @media (max-width: 768px) {
        .mobile-menu-button {
            display: block;
        }
        
        .main-nav {
            display: none;
        }
        
        .main-nav.active {
            display: block;
        }
    }
    
    /* Gallery styles */
    .gallery {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 15px;
        padding: 20px 0;
    }
    
    .gallery-item {
        cursor: pointer;
        overflow: hidden;
        border-radius: 5px;
        transition: transform 0.3s;
    }
    
    .gallery-item:hover {
        transform: scale(1.03);
    }
    
    .gallery-item img {
        width: 100%;
        height: auto;
        display: block;
    }
    
    .gallery-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.9);
    }
    
    .modal-content {
        position: relative;
        margin: auto;
        padding: 20px;
        max-width: 800px;
        width: 90%;
        height: 90%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .modal-image {
        max-width: 100%;
        max-height: 80vh;
        margin: 0 auto;
    }
    
    .caption {
        color: white;
        text-align: center;
        padding: 10px 0;
    }
    
    .close, .prev, .next {
        color: white;
        position: absolute;
        font-size: 30px;
        font-weight: bold;
        cursor: pointer;
    }
    
    .close {
        top: 10px;
        right: 25px;
    }
    
    .prev, .next {
        top: 50%;
        transform: translateY(-50%
