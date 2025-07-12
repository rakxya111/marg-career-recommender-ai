
const modal = document.getElementById('postModal');
const openBtn = document.querySelector('.open-modal-btn');
const cancelBtn = document.querySelector('.cancel-btn');

openBtn.addEventListener('click', () => {
modal.style.display = 'flex';
});

cancelBtn.addEventListener('click', () => {
modal.style.display = 'none';
});

// Close modal when clicking outside content
window.addEventListener('click', (e) => {
if (e.target === modal) {
    modal.style.display = 'none';
}
});

