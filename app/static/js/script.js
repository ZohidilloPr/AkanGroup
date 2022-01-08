setTimeout(() => {
  $('body').removeClass('activ')
      $('#load_anim1').removeClass('activ')
}, 5);


$('#bars').click(function () {
  $('#nav_bars').toggleClass('activ')
  $(this).toggleClass('activ')
})

let nav_item = document.querySelectorAll('.nav_bar a')
nav_item.forEach((element) => {
  element.addEventListener('click', () => {
    if (window.innerWidth < 769) {
      $('#nav_bars').removeClass('activ')
      $('#bars').removeClass('activ')
    }
  })
})



let section = document.querySelectorAll('section[id]');

function scrollActive() {
  const scrollY = window.pageYOffset

  section.forEach((element) => {
    const sectionH = element.offsetHeight
    const sectionTop = element.offsetTop - 50

    sectionId = element.getAttribute('id')

    if (scrollY > sectionTop && scrollY <= sectionTop + sectionH) {
      $('.nav_bar a[href*=' + sectionId + ']').addClass('activ')
    } else {
      $('.nav_bar a[href*=' + sectionId + ']').removeClass('activ')
    }
  })
  if (scrollY >= 1000) {
    $('#header').addClass('activ')
  } else {
    $('#header').removeClass('activ')
  }
}

window.addEventListener('scroll', scrollActive)


const scong = ScrollReveal({
  distance: '100px',
  duration: 2000,
  origin: 'right'
})
scong.reveal('.scong', { interval: 100 })

const scchap = ScrollReveal({
  distance: '100px',
  duration: 2000,
  origin: 'left'
})
scchap.reveal('.scchap', { interval: 100 })


const sctepa = ScrollReveal({
  distance: '100px',
  duration: 2000,
  origin: 'top'
})
sctepa.reveal('.sctepa', { interval: 100 })

const scpast = ScrollReveal({
  distance: '100px',
  duration: 2000,
  origin: 'bottom'
})
scpast.reveal('.scpast', { interval: 100 })


$('#loyihalar button').click(function () {
  $('#loyihalar .works_4').nextAll().css('display', 'block')
  $('#loyihalar .btn').css('display', 'none')
})


var swiper = new Swiper(".mySwiper", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 4500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});