<template>
  <RouterView />
</template>

<style>
body {
    font-family: 'Roboto', Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}

header {
    background-color: #003366;
    color: white;
    text-align: center;
    padding: 20px 0;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    margin: 0;
    font-size: 2.5em;
}

.zone-depot {
    width: 300px;
    height: 200px;
    border: 2px dashed #003366;
    margin: 20px auto;
    text-align: center;
    line-height: 200px;
    color: #003366;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    transition: background-color 0.3s ease;
}

.zone-depot.hover {
    background-color: #f0f8ff;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

form {
    display: flex;
    flex-direction: column;
}

input[type="file"] {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.button {
    background-color: #003366;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: #00509e;
}


footer {
    background-color: #003366;
    color: white;
    text-align: center;
    padding: 10px 0;
    width: 100%;
    box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.1);
    position: relative; /* Retirez la position absolue */
}

main {
    flex: 1; /* Fait en sorte que le main prenne tout l'espace disponible */
    display: flex; /* Active flexbox pour centrer le contenu */
    justify-content: center; /* Centre horizontalement le contenu */
    align-items: center; /* Centre verticalement le contenu */
    flex-direction: column; /* Permet d'empiler le contenu verticalement */
    text-align: center; /* Centre le texte à l'intérieur de main */
}



header h1 {
    margin-bottom: 10px; /* Espacement sous le titre */
    font-size: 24px; /* Taille de police du titre */
}

.buttons {
    display: flex; /* Utiliser flexbox pour aligner horizontalement les boutons */
    justify-content: center; /* Centrer les boutons horizontalement */
    align-items: center; /* Centrer les boutons verticalement */
    margin-top: 10px; /* Espacement au-dessus des boutons */
}

.buttons form {
    margin: 0 5px; /* Espacement entre les boutons */
}

.buttons button {
    font-size: 14px; /* Taille de police des boutons */
    padding: 8px 16px; /* Espacement intérieur des boutons */
}

.cv {
  margin: auto auto;
}

</style>