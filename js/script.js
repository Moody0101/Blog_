const gmailbutton = document.getElementById("Gmail");
const Sections = [...document.getElementsByTagName("nav"),
 ...document.getElementsByTagName("section"), ...document.getElementsByTagName("footer")
]
const loading = document.getElementById("loading");
const  loadingDiv = document.getElementsByClassName("container")[0];
gmailbutton.onclick = () => {
	return
}


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

