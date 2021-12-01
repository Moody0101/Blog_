const gmailbutton = document.getElementById("Gmail");
const Sections = [...document.getElementsByTagName("nav"),
 ...document.getElementsByTagName("section"), ...document.getElementsByTagName("footer")
]
const loading = document.getElementById("loading");
const  loadingDiv = document.getElementsByClassName("container")[0];
const temp = [
	...document.getElementsByTagName("h2"),	...document.getElementsByTagName("p")
]
//  testing 

loadingDiv.style.display = "none";
loading.style.display = "none";


var delay = 500;

// for(let i=0; i < Sections.length; i++) {
//     Sections[i].style.display = "none";
// }

// setTimeout(() => {
//     loadingDiv.style.display = "none";
//     loading.style.display = "none";
//     for(let i=0; i < Sections.length; i++) {
//     Sections[i].style.display = "";
//     Sections[i].style.transition = "1s all ease";
// }
// }, 4000);




for(let i=0; i < temp.length, !(temp[i] == undefined);i++) {
	
	if (i % 2 == 0) {
		Animate = "slide-up"
	} else {
		Animate = "slide-down"
	}
    temp[i].setAttribute('data-sal', Animate);
    temp[i].setAttribute('data-sal-repeat', null);
    temp[i].setAttribute('data-sal-delay', `${delay}`);
    temp[i].setAttribute('data-sal-easing', "ease-in-out");
   	delay += 50
}

sal({
    once: false,
    threshold: 0.6
});

// gmailbutton.onclick = () => {
// 	return
// }


