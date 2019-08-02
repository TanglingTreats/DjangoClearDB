var links = document.getElementsByClassName("nav-link");
var dropDownItems = document.getElementsByClassName("dropdown-item");



var path = window.location.pathname;

for(let i = 0; i < links.length; i++) {
    if(links[i].getAttribute("href") == path) {
        if(links[i].classList.value.search("dropdown-item") != -1) {
            links[i].closest('.dropdown').classList.add("active");
        }
        links[i].parentElement.classList.add("active");
    }
}