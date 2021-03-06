> Autor: Vinícius Luiz da Silva França  
> Email: vlsf2@cin.ufpe.br  
> Data: 2021-04-09  
>
> Copyright(c) 2021 Vinícius Luiz da Silva França

> Recrie a interface do principal site de streaming mundial utilizando tecnologias simples como HTML5, CSS3 e JavaScript. Nesse projeto você aprenderá: como estruturar um layout, técnicas de CSS3 com containers e variáveis, como posicionar os elementos com Flexbox e como utilizar plugins Jquery a favor da sua aplicação.

visualização em: https://cin.ufpe.br/~vlsf2/portfolio/Recriando_Interface_Netflix/

foi desenvolvido essa página Potterflix com o intuito de aprimorar minhas habilidades no HTML5; CSS3 e JavaScript

Foi adicionado uma página de **Trilhas Sonoras** de todos os filmes

Bootcamp HTML Developer | Digital Innovation One

## Observações de Implementação

### EMMET e Atalhos

`html:5` É utilizado para iniciar a estrutura padrão do HTML

`link:css` É utilizado para iniciar o arquivo CSS no seu HTML

`alt + shift + seta/baixo` para clonar a linha atual

### HTML5

- `<head>` É a cabeça do código, as configurações que cuidam da coordenação do projeto
- Todo elemento que aparece na tela, pensamos como uma espécie de contêineres, caixas, ou seja, `<div>`
- `<nav>`  tag semântica utilizada pra representar menus de navegação 
- `<main>` tag semântica utilizada para representar o conteúdo principal
- **Wrapper = Envelopar**
  - Ela é uma div que guarda vários outros elementos dentro
  - Facilita no processo de formatação do CSS
  - `.container` Acessa todos as classes containers 
  - `.filme-principal .container` Acessa apenas o container da classe *filme-principal*

### CSS3

1. É fundamental reiniciar as configurações de padding, border e margin da página.

2. É importante declarar variáveis para facilitar a implementação do código. 

   `:root { --var1: valor; --var2: valor;}`

   3. O CSS herda todas as formatações que o elemento pai tem.
   4. Se possível, utilize medidas de porcentagem para configurar o tamanho de um elemento.

   > ##### Estilizar um elemento quando o mouse estiver sobre o elemento
   >
   > `:hover` 
   >
   > `header nav a {}`
   >
   > `header nav a:hover {}` 

   > ##### Flex-box
   >
   > - Tipo de maneira de alinhar os elementos em tela
   >
   > - Ao iniciar o `display: flex` o CSS tem tendência de jogar tudo para a linha, assim sendo por padrão `flex-direction: row`; se `flex-direction: column` então o `align-items` e `justify-content` irão inverter seus eixos.
   >   - https://www.w3schools.com/cssref/playit.asp?filename=playcss_flex-direction&preval=row 
   >
   > - `align-items: center` alinha os itens ao centro no eixo y
   >   - https://www.w3schools.com/cssref/playit.asp?filename=playcss_align-items&preval=stretch 
   >
   > - `justify-content: space-between` alinha os itens adicionando um espaço entre eles no eixo x
   >   - https://www.w3schools.com/cssref/playit.asp?filename=playcss_justify-content&preval=flex-start

   > ##### Gradient
   >
   > - é usado para dar uma tonalidade na imagem selecionada
   >
   > `background: linear-gradient(rgba(0,0,0,.50), rgba(0,0,0.50)100%), url("img");` 

   > ##### Configurações do botão
   >
   > - `cursor: pointer;`  faz com que seu cursor reconheça um botão e altere sua forma.
   > - `transition: .3s ease-out;`  transação suave após passar mouse sobre o botão

   > ##### Carousel
   >
   > `  <link rel="stylesheet" href="owl/owl.carousel.min.css">`  
   >
   > `<link rel="stylesheet" href="owl/owl.theme.default.min.css">`

   > ### Responsividade
   >
   > *responsive.css*
   >
   > Trabalhar com media queries
   >
   > `@media screen and (max-width: Npx){}`

   

### JavaScript 

- É recomendado inserir o `<script> </script>` no fim da página para evitar erros

-     <script>src="js/owl/jquery.min.js"</script>
        <script>src="js/owl/owl.carousel.min.js"</script>

### jQuery

> #### Para a pasta js/owl  
> ##### OwlCarousel2-2.3.4 > docs > assets > vendors > jquery.min  
> ##### OwlCarousel2-2.3.4 > docs > assets > owlcarousel > owl.carousel.min

> #### Para a pasta style/owl  
> ##### OwlCarousel2-2.3.4 > dist > assets > owl.carousel.min  
> ##### OwlCarousel2-2.3.4 > dist > assets > owl.theme.default.min
>
> https://owlcarousel2.github.io/OwlCarousel2/demos/basic.html

### Python

> ##### Ajuste de semântica
>
> Foi utilizado Python para facilitar na escita da semântica do HTML, demonstração nessa amostra:
>
> _titulo.txt_
>
> `Prólogo
> Mundo Maravilhoso do Harry  
> A Chegada de Harry Bebê  
> Visita ao Zoológico e Cartas de Hogwarts`  
>
> _tituloHTML.txt_ 
>
> `<li class = "lista1" >Prólogo</li>`  
> `<li class = "lista2" >Mundo Maravilhoso do Harry</li>`  
> `<li class = "lista1" >A Chegada de Harry Bebê</li>`  
> `<li class = "lista2" >Visita ao Zoológico e Cartas de Hogwarts</li>`