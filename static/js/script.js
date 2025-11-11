// --- Confetti Function ---
function startConfetti() {
    const container = document.getElementById('confetti-container');
    // Clear any old confetti
    if (container) {
        container.innerHTML = '';
    } else {
        console.error('Confetti container not found');
        return;
    }
    
    const colors = ['#f472b6', '#ec4899', '#a855f7', '#d946ef', '#fde047', '#ffffff'];
    const confettiCount = 150;

    for (let i = 0; i < confettiCount; i++) {
        const piece = document.createElement('div');
        piece.style.position = 'absolute';
        piece.style.width = `${Math.random() * 10 + 5}px`;
        piece.style.height = `${Math.random() * 16 + 8}px`;
        piece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        piece.style.left = `${Math.random() * 100}vw`;
        piece.style.top = '-20px'; // Start above screen
        
        // Animation properties
        const duration = `${Math.random() * 3 + 4}s`; // 4-7 seconds
        const delay = `${Math.random() * 5}s`; // 0-5 second delay
        
        // We use two separate animations for better randomization
        piece.style.animation = `fall ${duration} ${delay} cubic-bezier(0.1, 0.5, 0.9, 0.8) forwards, spin 2s ${delay} linear infinite`;
        
        container.appendChild(piece);
    }
}