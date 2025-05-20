// Enhanced Navbar Behavior
const navbar = document.querySelector('.navbar');
let navbarTimeout;

// Desktop Hover Behavior
navbar.addEventListener('mouseenter', () => {
    clearTimeout(navbarTimeout);
    navbar.classList.add('hover-active');
});

navbar.addEventListener('mouseleave', () => {
    navbarTimeout = setTimeout(() => {
        navbar.classList.remove('hover-active');
    }, 300);
});

// Mobile Touch Support
navbar.addEventListener('touchstart', (e) => {
    e.preventDefault();
    navbar.classList.toggle('hover-active');
});

// Close navbar when clicking outside
document.addEventListener('click', (e) => {
    if (!navbar.contains(e.target) && navbar.classList.contains('hover-active')) {
        navbar.classList.remove('hover-active');
    }
});

// Active State Management
document.querySelectorAll('.nav-item a').forEach(item => {
    item.addEventListener('click', function(e) {
        document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
        this.parentElement.classList.add('active');
    });
});

//--------------------------------------------Confirf Delete Modal-------------------------------------------//

function showConfDeleteModal(tweetId) {
    document.getElementById('deleteWarningModal').style.display = 'flex';
    document.querySelector('#deleteWarningModal form').action = `/tweet/${tweetId}/delete/`;
}


function hideConfDeleteModal() {
    document.getElementById('deleteWarningModal').style.display = 'none';
}


function showConfDeleteModal(tweetId) {
    document.getElementById('deleteWarningModal').style.display = 'flex';
    document.querySelector('#deleteWarningModal form').action = `/tweet/${tweetId}/delete/`;
    
    // Add blur effect to the body
    document.body.classList.add('blurred');
    document.body.style.overflow = 'hidden'; // Prevent scrolling
}

function hideConfDeleteModal() {
    document.getElementById('deleteWarningModal').style.display = 'none';
    
    // Remove blur effect from the body
    document.body.classList.remove('blurred');
    document.body.style.overflow = ''; // Allow scrolling
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('deleteWarningModal');
    if (event.target === modal) {
        hideConfDeleteModal();
    }
}



//--------------------------------------------Profile/Create Toggle-------------------------------------------//

function toggleDropdown(menuId) {
    // Close any open dropdowns first
    document.querySelectorAll('.dropdown-menu').forEach(menu => {
        if (menu.id !== menuId) {
            menu.style.display = 'none';
        }
    });

    // Toggle the clicked dropdown
    let dropdown = document.getElementById(menuId);
    dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
}

// Close dropdowns when clicking outside
document.addEventListener('click', function(event) {
    if (!event.target.closest('.dropdown-container')) {
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
            menu.style.display = 'none';
        });
    }
});
