import "@styles/lenis.css";

import Lenis from "lenis";

// Global modal state
if (typeof window !== 'undefined') {
    window.modalOpen = false;
}

// Script to handle Lenis library settings for smooth scrolling
// https://github.com/darkroomengineering/lenis
let lenis = null;

function initLenis() {
    if (typeof window !== 'undefined' && !window.modalOpen && !lenis) {
        lenis = new Lenis({
            autoRaf: true,
        });
        window.lenis = lenis;
    }
}

function destroyLenis() {
    if (lenis) {
        lenis.destroy();
        lenis = null;
        if (typeof window !== 'undefined') {
            window.lenis = null;
        }
    }
}

// Initialize Lenis
initLenis();

// Expose functions globally
if (typeof window !== 'undefined') {
    window.initLenis = initLenis;
    window.destroyLenis = destroyLenis;
}
