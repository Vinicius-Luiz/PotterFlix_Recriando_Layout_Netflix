$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:false,
    responsive:{
        0:{
            items:1
        },
        360:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})


function alterarFilmePrincipal(filme){
    alert('Dificuldade de alterar conteúdo do filme principal (26/04/21)');
}