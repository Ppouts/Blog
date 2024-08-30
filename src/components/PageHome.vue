<template>
    <header>
        <h1>BLOG</h1>
        <div class="buttons">
        
            <RouterLink class="button" to="/stage_B2" > Stage B2 </RouterLink>

            <RouterLink class="button" to="/a_propos"> A propos </RouterLink>

        </div>
    </header>

    <body>
        <div class="container">
            <h1>Présentation de la Gendarmerie nationale</h1>
            <p>La Gendarmerie nationale est une force militaire française chargée de missions de police, de sécurité et de maintien de l'ordre sur le territoire national, en particulier dans les zones rurales et périurbaines. Elle relève du ministère de l'Intérieur pour ses missions de sécurité intérieure et du ministère des Armées pour ses missions militaires.</p>

            <h2>Missions principales de la Gendarmerie</h2>
            <ul>
                <li><strong>Sécurité publique</strong> : Prévention et répression des crimes et délits, maintien de l'ordre public.</li>
                <li><strong>Enquêtes judiciaires</strong> : Conduite d'enquêtes sous la direction des autorités judiciaires.</li>
                <li><strong>Secours et assistance</strong> : Interventions d'urgence, sauvetage, et aide aux personnes en danger.</li>
                <li><strong>Contrôle routier</strong> : Surveillance des routes et autoroutes, prévention des accidents de la route.</li>
            </ul>

            <h2>Section NTECH</h2>
            <p>La Section NTECH (ou parfois appelée <strong>Pôle judiciaire NTECH</strong>) est une unité spécialisée de la Gendarmerie nationale dédiée à la lutte contre la cybercriminalité. Elle est composée de gendarmes spécialisés en nouvelles technologies qui mènent des enquêtes techniques, numériques et judiciaires sur les infractions liées à l'informatique.</p>

            <h2>Missions de la Section NTECH</h2>
            <ul>
                <li><strong>Investigations numériques</strong> : Analyse de preuves numériques, récupération de données, et traçage d'activités cybercriminelles.</li>
                <li><strong>Lutte contre la cybercriminalité</strong> : Démantèlement de réseaux criminels opérant sur Internet, traque des hackers et des cyberdélinquants.</li>
                <li><strong>Support aux enquêtes</strong> : Assistance technique aux unités de gendarmerie dans le cadre d'enquêtes judiciaires impliquant des éléments numériques.</li>
                <li><strong>Prévention et sensibilisation</strong> : Actions de sensibilisation auprès du public et des entreprises sur les risques liés à l'utilisation des nouvelles technologies.</li>
            </ul>
        </div>
    </body>

    <footer>
        <p>&copy; 2024 Blog</p>
    </footer>

</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style lang="css" scoped>

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
</style>