<template>
 
 <header>
        <h1>BLOG</h1>
        <div class="buttons" />
        <RouterLink class="button" to="/stage_b2"> Retour </RouterLink>
    </header>
    
    <h1>Cahier des Charges</h1>

    <h2>Projet : Page Web de brut force de mots de passe</h2>

    <h3>1. Présentation du Projet</h3>
    <p><strong>Client :</strong> Gendarmerie Nationale</p>
    <p><strong>Nom du projet :</strong> Développement d'un outil de brut force</p>
    <p><strong>Responsable du projet :</strong> POUTS Pierre</p>

    <h3>2. Objectifs du Projet</h3>
    <ul>
        <li>Créer un outil web pour trouver les mots de passe des fichiers ZIP et PDF</li>
        <li>Identifier les mots de passe pour accéder aux données</li>
        <li>Assurer que l'outil soit simple d’utilisation et efficace</li>
    </ul>

    <h3>3. Description des Fonctionnalités</h3>

    <h4>3.1. Interface Utilisateur</h4>
    <ul>
        <li>Drag and Drop : Pour glisser facilement les fichiers dans la page web</li>
        <li>Recherche par fichier : Une recherche directe dans les fichiers de l’ordinateur/Clés USB pour une utilisation pratique</li>
        <li>Visuel : Une page simple avec très peu d’informations</li>
    </ul>

    <h4>3.2. Fonctionnalités Techniques</h4>
    <ul>
        <li>Module de test de mots de passe : Algorithmes de brute force et dictionnaires pour trouver les mots de passe.</li>
        <li>Affichage du mot de passe : Renvoie du mot de passe sur la page</li>
    </ul>

    <h3>4. Contraintes Techniques</h3>
    <ul>
        <li><strong>Technologies :</strong> Utilisation de Python et JS pour le développement de l'algorithme de brute force, et Flask pour le front-end.</li>
        <li><strong>Hébergement :</strong> Utilisation d'un serveur sécurisé et hébergé en France</li>
    </ul>

    <h3>5. Conformité et Éthique</h3>
    <ul>
        <li><strong>Conformité légale :</strong> L'outil doit respecter les lois françaises et européennes en matière de cybersécurité et de protection des données.</li>
        <li><strong>Accès restreint :</strong> L'accès à l'outil doit être limité aux utilisateurs autorisés de la gendarmerie.</li>
    </ul>

    <h3>6. Délai et Planning</h3>
    <ul>
        <li><strong>Durée estimée du projet :</strong> 6 semaines</li>
        <li><strong>Phases du projet :</strong>
            <ul>
                <li>Développement de l’interface utilisateur : 1 semaine</li>
                <li>Développement de l'algorithme : 4 semaines</li>
                <li>Tests et validation : 2 jours</li>
                <li>Tâches annexes : 3 jours</li>
            </ul>
        </li>
    </ul>

    <h3>7. Budget</h3>
    <p><strong>Estimation des coûts :</strong> 0 €</p>

    <h3>8. Contact</h3>
    <div class="contact-info">
        <p><strong>Responsable du projet :</strong> POUTS Pierre</p>
        <p><strong>Email :</strong> <a href="mailto:pierre.pouts@gmail.com">pierre.pouts@gmail.com</a></p>
        <p><strong>Téléphone :</strong> +33 06.13.88.31.63</p>
    </div>
    <footer>
        <p>&copy; 2024 Blog</p>
    </footer>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>