$(window).scroll(function () {
  $(window).on('scroll', function () {
    if ($(window).scrollTop()) {
      $('nav').addClass('green');
    }
    else {
      $('nav').removeClass('green');
    }
  })

  // fade in right
  $('.piece-right').each(function () {
    var point = "0px", side = "30px";

    if (isScrolledIntoView($(this))) {
      $(this).css({
        'opacity': .8,
        'visibility': 'visible',
        '-webkit-transform': 'translateX(' + point + ')',
        'transform': 'translateX(' + point + ')'
      });
    }

    else {
      $(this).css({
        '-webkit-transform': 'translateX(' + side + ')',
      });
    }
  });




  //Fade-in-left
  $('.piece-left').each(function () {
    var point = "0px", move = "-30px";

    if (isScrolledIntoView($(this))) {
      $(this).css({
        'opacity': .8,
        'visibility': 'visible',
        '-webkit-transform': 'translateX(' + point + ')',
        'transform': 'translateX(' + point + ')'
      });
    }

    else {
      $(this).css({
        '-webkit-transform': 'translateX(' + move + ')',
      });
    }
  });


  function isScrolledIntoView(elem) {
    var $elem = $(elem);
    var $window = $(window);

    var docViewTop = $window.scrollTop();
    var docViewBottom = docViewTop + $window.height();

    var elemTop = $elem.offset().top;
    var elemBottom = elemTop + $elem.height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
  }

})

$(document).ready(function () {
  $("#accordion").accordion();

  /*top */
  $('#bottom').click(function () {
    $('html, body').stop().animate({ scrollTop: 0 }, 'slow');
  });

  function do_slide() {
    interval = setInterval(function () {
      moveRight();
    }, 5000);
  }
  do_slide();


  //carousel start
  var slideIndex = 1;
  showSlides(slideIndex);
  //Next and previous buttons start
  $(".prev-slide").click(function () {
    plusSlides(-1);
  });
  $(".next-slide").click(function () {
    plusSlides(1);
  });

  function moveRight() {
    plusSlides(1);
  };

  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  //Next and previous buttons end
  //dots start
  $(".dot1").click(function () {
    currentSlide(1);
  });
  $(".dot2").click(function () {
    currentSlide(2);
  });
  $(".dot3").click(function () {
    currentSlide(3);
  });
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  //dots end
  function showSlides(n) {
    var i;
    var slides = $(".mySlides");
    var dots = $(".dot");
    if (n > slides.length) {
      slideIndex = 1;
    }
    if (n < 1) {
      slideIndex = slides.length;
    }
    for (var i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (var i = 0; i < dots.length; i++) {
      dots[i].className.replace("active", "");
      dots[i].classList.remove("active");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
  }


  //menu active
  $(".menu-toggle-btn").click(function () {
    $(this).toggleClass("fa-times");
    $("#menu").toggleClass("active")
  });


})







