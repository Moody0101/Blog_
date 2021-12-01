function copy(container, i) {
    /* Get the text field */
    // var copyText = document.getElementById("myInput");

    /* Select the text field */
    container.select();

    container.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    document.execCommand("copy");
    copbtt[i].value = "copied";
    copbtt[i].style.background = "white";
    copbtt[i].style.color = "black";

}