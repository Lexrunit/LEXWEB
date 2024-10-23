
window.onbeforeunload = function () {
  window.scrollTo(0, 0);
};





document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', function(event) {
    event.preventDefault();
    const targetId = this.getAttribute('href');
    const targetSection = document.querySelector(targetId);
    if (targetSection) {
      targetSection.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

const scrollToTopBtn = document.createElement('button');
scrollToTopBtn.innerHTML = '↑';
scrollToTopBtn.style.position = 'fixed';
scrollToTopBtn.style.bottom = '20px';
scrollToTopBtn.style.right = '20px';
scrollToTopBtn.style.display = 'none';
scrollToTopBtn.style.zIndex = '1000';
scrollToTopBtn.style.backgroundColor = '#021488';
scrollToTopBtn.style.color = '#c5ecf4';
scrollToTopBtn.style.border = 'none';
scrollToTopBtn.style.padding = '10px';
scrollToTopBtn.style.borderRadius = '5px';
scrollToTopBtn.style.cursor = 'pointer';
document.body.appendChild(scrollToTopBtn);

window.onscroll = function() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
};

scrollToTopBtn.onclick = function() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

const toggleSwitch = document.getElementById('themeSwitcher');

toggleSwitch.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});
