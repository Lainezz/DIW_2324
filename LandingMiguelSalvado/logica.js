
const cambiarCss = () => {
    const navItems = document.querySelector(".navItems");
    navItems.classList.toggle("navItems--abrir");
};


const onIniciar = () => {
    console.log("Uso esta funcion para inicializar elementos de la pagina");
    const divMenu = document.querySelector(".header__menu");
    divMenu.addEventListener("click", cambiarCss)
}

window.onload = onIniciar;
