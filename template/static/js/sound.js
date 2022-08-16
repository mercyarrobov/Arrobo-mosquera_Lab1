//Definimos una variable que llama a la clase audio
var audio = document.querySelector('.audio');
//Funcion sonido
function animaleSound(element){
    var sound = element.getAttribute('data-sound');
    audio.src= sound;
    audio.play();
}