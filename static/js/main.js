// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const href = this.getAttribute('href');
        // Skip if href is just "#" which is not a valid selector
        if (href !== "#") {
            const targetElement = document.querySelector(href);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
});

// Dynamic card hover effect
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px)';
    });

    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// Alert auto-dismiss
document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
        alert.classList.add('fade');
        setTimeout(() => {
            alert.remove();
        }, 150);
    }, 5000);
});

// Image lazy loading
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
});

// Mobile menu toggle
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

if (navbarToggler && navbarCollapse) {
    navbarToggler.addEventListener('click', function() {
        navbarCollapse.classList.toggle('show');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target)) {
            navbarCollapse.classList.remove('show');
        }
    });
}

// Status badge color update
document.querySelectorAll('.badge').forEach(badge => {
    const status = badge.textContent.toLowerCase();
    badge.className = `badge badge-${status}`;
});

// Form field focus effect
document.querySelectorAll('.form-control').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });

    input.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
});

// Intersection Observer for scroll animations
const animateOnScroll = () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .hero-section h1, .hero-section p, .features-section .fa-3x').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
};

// Parallax effect for hero section
const parallaxEffect = () => {
    const hero = document.querySelector('.hero-section');
    if (hero) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            hero.style.backgroundPositionY = `${scrolled * 0.5}px`;
        });
    }
};

// Animated counter for statistics
const animateCounter = () => {
    const counters = document.querySelectorAll('.counter');
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const increment = target / 200;
        let current = 0;

        const updateCounter = () => {
            if (current < target) {
                current += increment;
                counter.textContent = Math.ceil(current);
                setTimeout(updateCounter, 1);
            } else {
                counter.textContent = target;
            }
        };
        updateCounter();
    });
};

// Smooth scroll for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const href = this.getAttribute('href');
        // Skip if href is just "#" which is not a valid selector
        if (href !== "#") {
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// Update navbar on scroll
const updateNavbarOnScroll = () => {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        const updateNavbar = () => {
            if (window.scrollY > 20) {
                navbar.classList.add('navbar-scrolled');
                navbar.style.padding = '0.5rem 0';
            } else {
                navbar.classList.remove('navbar-scrolled');
                navbar.style.padding = '1rem 0';
            }
        };

        window.addEventListener('scroll', updateNavbar);
        updateNavbar(); // Initial check
    }
};

// Card hover effects
const initializeCardEffects = () => {
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
        });
    });
};

// Form validation and animation
const initializeFormEffects = () => {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('.form-control');

        inputs.forEach(input => {
            input.addEventListener('focus', () => {
                input.parentElement.classList.add('focused');
            });

            input.addEventListener('blur', () => {
                if (!input.value) {
                    input.parentElement.classList.remove('focused');
                }
            });
        });

        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();

                const invalidInputs = form.querySelectorAll(':invalid');
                invalidInputs.forEach(input => {
                    input.classList.add('shake');
                    setTimeout(() => input.classList.remove('shake'), 500);
                });
            }
            form.classList.add('was-validated');
        });
    });
};

// Mobile menu handling
const initializeMobileMenu = () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    if (navbarToggler && navbarCollapse) {
        // Toggle menu
        navbarToggler.addEventListener('click', () => {
            navbarCollapse.classList.toggle('show');
            document.body.classList.toggle('menu-open');
            navbarToggler.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navbarCollapse.contains(e.target) &&
                !navbarToggler.contains(e.target) &&
                navbarCollapse.classList.contains('show')) {
                navbarCollapse.classList.remove('show');
                document.body.classList.remove('menu-open');
                navbarToggler.classList.remove('active');
            }
        });

        // Close menu when clicking nav links
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navbarCollapse.classList.remove('show');
                document.body.classList.remove('menu-open');
                navbarToggler.classList.remove('active');
            });
        });
    }
};

// Initialize all animations and interactions
document.addEventListener('DOMContentLoaded', () => {
    animateOnScroll();
    parallaxEffect();
    animateCounter();
    updateNavbarOnScroll();
    initializeCardEffects();
    initializeFormEffects();
    initializeMobileMenu();

    // Add CSS classes for animations
    document.querySelectorAll('.card').forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });

    // Alert auto-dismiss with fade
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            alert.classList.add('fade-out');
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // Add loading animation to buttons
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('loading')) {
                this.classList.add('loading');
                setTimeout(() => this.classList.remove('loading'), 1000);
            }
        });
    });

    // Enhanced Navigation Experience

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');

    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        });
    }

    // Add active class to parent dropdown if child is active
    const activeDropdownItems = document.querySelectorAll('.dropdown-item.active');
    activeDropdownItems.forEach(item => {
        const parentDropdown = item.closest('.dropdown');
        if (parentDropdown) {
            const dropdownToggle = parentDropdown.querySelector('.dropdown-toggle');
            if (dropdownToggle) {
                dropdownToggle.classList.add('active');
            }
        }
    });

    // Enhance dropdown toggle behavior
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('mouseenter', function() {
            if (window.innerWidth >= 992) { // Only on desktop
                const dropdown = new bootstrap.Dropdown(toggle);
                dropdown.show();
            }
        });

        const parentDropdown = toggle.closest('.dropdown');
        if (parentDropdown) {
            parentDropdown.addEventListener('mouseleave', function() {
                if (window.innerWidth >= 992) { // Only on desktop
                    const dropdown = bootstrap.Dropdown.getInstance(toggle);
                    if (dropdown) {
                        dropdown.hide();
                    }
                }
            });
        }
    });

    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.btn, .nav-link');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const ripple = document.createElement('span');
            ripple.classList.add('ripple-effect');
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;

            button.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Enhance mobile menu
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarToggler) {
        navbarToggler.addEventListener('click', function() {
            this.classList.toggle('active');
        });
    }

    // Welcome message for logged-in users
    const userAuthenticated = document.body.classList.contains('user-authenticated');
    if (userAuthenticated) {
        const username = document.querySelector('#userDropdown');
        const usernameText = username ? username.textContent.trim() : '';
        if (usernameText && !sessionStorage.getItem('welcomeShown')) {
            setTimeout(() => {
                showWelcomeToast(usernameText);
                sessionStorage.setItem('welcomeShown', 'true');
            }, 1000);
        }
    }

    // Function to show welcome toast
    function showWelcomeToast(username) {
        const toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        toastContainer.style.zIndex = '1080';

        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');

        toast.innerHTML = `
            <div class="toast-header bg-success text-white">
                <i class="fas fa-user-check me-2"></i>
                <strong class="me-auto">Welcome Back!</strong>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                <p class="mb-0">Welcome back, ${username}! Ready to make a positive environmental impact today?</p>
            </div>
        `;

        toastContainer.appendChild(toast);
        document.body.appendChild(toastContainer);

        const bsToast = new bootstrap.Toast(toast, {
            autohide: true,
            delay: 5000
        });

        bsToast.show();
    }
});