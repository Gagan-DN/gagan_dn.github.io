//typing script and menu bar start
$(document).ready(function () {
    $(window).scroll(function () {
      // sticky navbar on scroll script
      if (this.scrollY > 20) {
        $(".navbar").addClass("sticky");
      } else {
        $(".navbar").removeClass("sticky");
      }
  
      // scroll-up button show/hide script
      if (this.scrollY > 500) {
        $(".scroll-up-btn").addClass("show");
      } else {
        $(".scroll-up-btn").removeClass("show");
      }
    });
  
    // slide-up script
    $(".scroll-up-btn").click(function () {
      $("html").animate({ scrollTop: 0 });
      // removing smooth scroll on slide-up button click
      $("html").css("scrollBehavior", "auto");
    });
  
    $(".navbar .menu li a").click(function () {
      // applying again smooth scroll on menu items click
      $("html").css("scrollBehavior", "smooth");
    });
  
    // toggle menu/navbar script
    $(".menu-btn").click(function () {
      $(".navbar .menu").toggleClass("active");
      $(".menu-btn i").toggleClass("active");
    });
  
    // typing text animation script
    var typed = new Typed(".typing", {
      strings: ["AI Developer",
       "Machine learning Engineer",
      "Full Stack Web Developer", 
      "Data Analyst", 
      ""],
      typeSpeed: 100,
      backSpeed: 60,
      loop: true
    });
  
    var typed = new Typed(".typing-2", {
      strings: [
      "AI Developer",
      "Machine learning Engineer",
      "Full Stack Web Developer", 
      "Data Analyst",
      ""],
      typeSpeed: 100,
      backSpeed: 60,
      loop: true
    });
  
    // owl carousel script
    $(".carousel").owlCarousel({
      strings: ["AI Developer",
      "Machine learning Engineer",
      "Full Stack Web Developer", 
      "Data Analyst",
      ""],
      margin: 20,
      loop: true,
      autoplay: true,
      autoplayTimeOut: 2000,
      autoplayHoverPause: true,
      responsive: {
        0: {
          items: 1,
          nav: false
        },
        600: {
          items: 2,
          nav: false
        },
        1000: {
          items: 3,
          nav: false
        }
      }
    });
  });
  
//typing script and menu bar end

  //age auto update start
  function auto_age(year_of_birth){
  let age=document.getElementById("age");
  const year=new Date();
  let this_year=year.getFullYear();
  let current_year=this_year-year_of_birth;
  age.innerHTML=current_year;
  }
  auto_age(2003);
   //age auto update end

   /*-==================== QUALIFICATION start====================-*/
   function qualification(){
   const tabs = document.querySelectorAll("[data-target]"),
  tabContents = document.querySelectorAll("[data-content]");
  
  tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const target = document.querySelector(tab.dataset.target);
  
    tabContents.forEach((tabContent) => {
      tabContent.classList.remove("qualification__active");
    });
    target.classList.add("qualification__active");
  
    tabs.forEach((tab) => {
      tab.classList.remove("qualification__active");
    });
    tab.classList.add("qualification__active");
  });
  });
  
}
qualification();
    /*-==================== QUALIFICATION start====================-*/

/*project and %page scroller css start*/
function gallery_scroll(){
  const product = document.querySelectorAll(".product");
const circle = document.querySelector(".scroll-progress");

window.onscroll = function () {
  const element = document.querySelector(".header");

  let progress =
    (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
  circle.innerText = Math.round(progress) + "%";

  if (window.scrollY > 10) {
    element.classList.add("posColor");
  } else {
    element.classList.remove("posColor");
  }
};

window.addEventListener("scroll", scroller);

function scroller() {
  const size = (window.innerHeight / 5) * 4;

  product.forEach((box) => {
    const boxTop = box.getBoundingClientRect().top;

    if (boxTop < size) {
      box.classList.add("scroll");
    } else {
      box.classList.remove("scroll");
    }
  });
}
}
gallery_scroll();

/*project and %page scroller css end*/

/*contact form start*/
function contact_form(){
  const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

}
contact_form();

/*contact form end*/