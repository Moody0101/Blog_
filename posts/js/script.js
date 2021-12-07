
const loading = document.getElementById("loading");
const  loadingDiv = document.getElementsByClassName("container")[0];
const Sections = [
   ...document.getElementsByTagName("nav"), ...document.getElementsByTagName("footer"), ...document.getElementsByClassName("Content")
]
// const dancingBtt = document.getElementById("FilterBTT");

// const addAnimation = () => {
//    dancingBtt.classList.push("active");
// }

// dancingBtt.onclick = () => {
//    setTimeout(addAnimation, 10000);
// }

 for(let i=0; i < Sections.length; i++) {
    Sections[i].style.display = "none";
}

setTimeout(() => {
    loadingDiv.style.display = "none";
    loading.style.display = "none";
    for(let i=0; i < Sections.length; i++) {
    Sections[i].style.display = "";
    Sections[i].style.transition = "1s all ease";
}
}, 4000);
