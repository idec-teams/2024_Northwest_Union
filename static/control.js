window.onload = () => {
    const bgHero = document.getElementsByClassName("bg-hero");
    let topGap = bgHero[0].getBoundingClientRect().top;
    const toTop = bgHero[0].getElementsByClassName("to-top")[0];

    judgeToTop(topGap,bgHero[0]);
    const body = document.getElementsByTagName("body")[0];

    //回到顶部
    if(bgHero[0].getElementsByClassName("lead")[0].innerHTML){
        bgHero[0].style.top = "-198px"
    }
    body.onscroll = () => {
        topGap = bgHero[0].getBoundingClientRect().top;
        judgeToTop(topGap,bgHero[0]);
    }
    toTop.addEventListener("click",() => {
        document.documentElement.scrollTo(0,0)
    })
}

function judgeToTop(topGap,bgHero){
    if(topGap == -198 || topGap == -150){
        bgHero.getElementsByClassName("to-top")[0].style.display="block";
    }
    if(topGap == 56){
        bgHero.getElementsByClassName("to-top")[0].style.display="none";
    }
}