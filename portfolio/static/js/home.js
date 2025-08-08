 document.addEventListener('DOMContentLoaded', function() {
    // Enhanced particles
    const particlesContainer = document.querySelector('.particles');
    const particleCount = Math.floor(window.innerWidth / 10);
    
    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement('div');
      particle.classList.add('particle');
      
      const size = Math.random() * 3 + 1;
      const posX = Math.random() * 100;
      const delay = Math.random() * 5;
      const duration = Math.random() * 10 + 10;
      const opacity = Math.random() * 0.4 + 0.1;
      
      particle.style.cssText = `
        width: ${size}px;
        height: ${size}px;
        opacity: ${opacity};
        left: ${posX}%;
        bottom: -10px;
        animation-duration: ${duration}s;
        animation-delay: ${delay}s;
      `;
      
      particlesContainer.appendChild(particle);
    }
    
    // Skill hover effect
    const skills = document.querySelectorAll('.skill-highlight');
    skills.forEach(skill => {
      skill.addEventListener('mouseenter', () => {
        skill.style.animation = 'none';
        void skill.offsetWidth; // Trigger reflow
        skill.style.animation = 'pulse 0.5s ease';
      });
    });
    
    // Add pulse animation
    const style = document.createElement('style');
    style.textContent = `
      @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
      }
    `;
    document.head.appendChild(style);
  });