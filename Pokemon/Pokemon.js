const pokemonImages = [
    "Pikachu.png",
    "Charmander.png",
    "Bulbasaur.png",
    "Squirtle.png",
    "Jigglypuff.png",
    "Froakie.png",
    "Riolu.png"
];

function showPokemon(element) {
    const randomIndex = Math.floor(Math.random() * pokemonImages.length);
    element.src = pokemonImages[randomIndex];
}
function hidePokemon(element) {
    element.src = "Pokebola.png";}