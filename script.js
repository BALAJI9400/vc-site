const menuButton = document.querySelector('.mobile-menu');
const nav = document.querySelector('.nav');
if (menuButton && nav) {
  menuButton.addEventListener('click', () => {
    nav.classList.toggle('nav-open');
  });
}

window.addEventListener('scroll', () => {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  const y = window.scrollY;
  hero.style.backgroundPosition = `center calc(50% + ${y * 0.2}px)`;
});

const serviceCards = document.querySelectorAll('.feature-card');
serviceCards.forEach((card) => {
  card.addEventListener('mouseenter', () => card.classList.add('active'));
  card.addEventListener('mouseleave', () => card.classList.remove('active'));
});

// Smooth reveal on scroll
const revealElements = document.querySelectorAll('.section-head, .feature-card, .timeline-step, .project-card, .stat, .faq-item, .contact-form');
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('reveal-visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });

revealElements.forEach(el => revealObserver.observe(el));

// 3 Experience Zones toggle interaction
const zoneButtons = document.querySelectorAll('.zone-btn');
const zonePanels = document.querySelectorAll('.zone-panel');
zoneButtons.forEach(button => {
  button.addEventListener('click', () => {
    const zone = button.getAttribute('data-zone');
    if (!zone) return;

    zoneButtons.forEach(btn => {
      btn.classList.toggle('active', btn === button);
      btn.setAttribute('aria-selected', btn === button);
    });

    zonePanels.forEach(panel => {
      const isActive = panel.getAttribute('data-zone') === zone;
      panel.classList.toggle('active', isActive);
      if (isActive) {
        panel.removeAttribute('hidden');
      } else {
        panel.setAttribute('hidden', '');
      }
    });
  });
});