// ===================================================================
const menu = document.querySelector(".menu");
const menuInner = menu.querySelector(".menu__inner");
const menuArrow = menu.querySelector(".menu__arrow");
const menuTitle = menu.querySelector(".menu__title");
const burger = document.querySelector(".burger");
const overlay = document.querySelector(".overlay");
const menuDrop = menuInner.querySelector(".menu__dropdown")
const submenu = menuInner.querySelector(".submenu")
const submenuInner = submenu.querySelectorAll(".submenu__inner")
const header = document.getElementById('header');
const logo = document.getElementById("logo")
const logoWhite = document.getElementById("logo__white")
const menuLink = document.getElementById("menu__link")
const menuLinks = document.querySelectorAll(".menu__link");

// Navbar Menu Toggle Function
function toggleMenu() {
  menu.classList.toggle("is-active");
  overlay.classList.toggle("is-active");

}

// Show Mobile Submenu Function
function showSubMenu(children) {
  subMenu = children.querySelector(".submenu");
  subMenu.classList.add("is-active");
  subMenu.style.animation = "slideLeft 0.35s ease forwards";
  const menuTitle = children.querySelector("i").parentNode.childNodes[0]
    .textContent;
  menu.querySelector(".menu__title").textContent = menuTitle;
  menu.querySelector(".menu__header").classList.add("is-active");
}
function showSubMenuList(children) {
  const subMenu = children.querySelector(".submenu__list");
  const subMenuArrow = children.querySelector(".submenu__title");
  const arrow = subMenuArrow.querySelector(".fa");

  if (subMenu.classList.contains("is-active")) {

      subMenu.style.height = subMenu.scrollHeight + 'px';

      requestAnimationFrame(() => {
          subMenu.style.height = '0';
      });

      subMenu.classList.remove("is-active");
      arrow.classList.remove('rotate');
  } else {
      subMenu.classList.add("is-active");
      subMenu.style.height = 'auto'; 
      const height = subMenu.scrollHeight + 'px';
      subMenu.style.height = '0';

      requestAnimationFrame(() => {
          subMenu.style.height = height;
      });

      arrow.classList.add('rotate');

      subMenu.addEventListener('transitionend', () => {
          if (subMenu.classList.contains("is-active")) {
              subMenu.style.height = 'auto'; 
          }
      }, { once: true });
  }
}

// Hide Mobile Submenu Function
function hideSubMenu() {
  subMenu.style.animation = "slideRight 0.35s ease forwards";
  setTimeout(() => {
    subMenu.classList.remove("is-active");
  }, 300);

  menu.querySelector(".menu__title").textContent = "";
  menu.querySelector(".menu__header").classList.remove("is-active");
}

// Toggle Mobile Submenu Function
function toggleSubMenu(e) {
  if (!menu.classList.contains("is-active")) {
    return;
  }
  if (e.target.closest(".menu__dropdown")) {
    const children = e.target.closest(".menu__dropdown");
    showSubMenu(children);
  }

}

function toggleList(e) {
  if (e.target.closest(".submenu__inner")) {
    const children = e.target.closest(".submenu__inner");

    showSubMenuList(children);
  }
}

const handleScroll = () => {

  if (window.innerWidth < 768) {

    menuLinks.forEach(link => {
      link.style.color = '#ffffff';
    });

  }

  if (window.scrollY > 50) {

    header.classList.add('header-white');
    logo.classList.add('is-active');
    logoWhite.classList.add('is-inactive');
    menuLinks.forEach(link => {
      link.style.color = '#2e3094';
    });

  }
  else {
    header.classList.remove('header-white');
    logoWhite.classList.remove('is-inactive');
    logo.classList.remove('is-active');
    menuLinks.forEach(link => {
      link.style.color = '#ffffff';
    });


  }

};


// Fixed Navbar Menu on Window Resize
window.addEventListener("resize", () => {
  if (window.innerWidth >= 768) {
    if (menu.classList.contains("is-active")) {
      toggleMenu();
    }
  }
});

// Initialize All Event Listeners
burger.addEventListener("click", toggleMenu);
overlay.addEventListener("click", toggleMenu);
menuArrow.addEventListener("click", hideSubMenu);
menuTitle.addEventListener("click", hideSubMenu);
menuInner.addEventListener("click", toggleSubMenu);
menuInner.querySelectorAll(".submenu__inner").forEach(inner => inner.addEventListener("click", toggleList));

// Escuchar el evento de scroll
window.addEventListener('scroll', handleScroll);
window.addEventListener('resize', handleScroll);

submenuInner.forEach((div, i) => {
  div.addEventListener("click", toggleList);

});

// =======================================
$(document).ready(function () {
  $('.customer-logos').slick({
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1500,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    responsive: [{
      breakpoint: 768,
      settings: {
        slidesToShow: 4
      }
    }, {
      breakpoint: 520,
      settings: {
        slidesToShow: 3
      }
    }]
  });
});