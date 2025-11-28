import re
from datetime import datetime
from colorama import Fore, Style, init
from emoji import emojize

init(autoreset=True)  # Pour que les couleurs s'arrêtent automatiquement

class QuizGame:
    def __init__(self):
        self.user_data = {}
        self.score = 0

    def get_user_info(self):
        self.user_data["nom_complet"] = input(Fore.CYAN + "Entrez votre nom complet: ")
        self.user_data["nationalite"] = input(Fore.CYAN + "Entrez votre nationalité: ")

        # Vérification âge
        while True:
            try:
                naissance = input(Fore.CYAN + "Entrez votre date de naissance (JJ/MM/AAAA): ")
                jour, mois, annee = map(int, naissance.split("/"))
                date_naissance = datetime(annee, mois, jour)
                age = (datetime.now() - date_naissance).days // 365
                if age < 3:
                    print(Fore.RED + "⚠️ Vous devez avoir au moins 3 ans pour jouer !")
                else:
                    self.user_data["date_naissance"] = naissance
                    break
            except ValueError:
                print(Fore.RED + "Format invalide, veuillez entrer sous la forme JJ/MM/AAAA.")

        self.user_data["pays_naissance"] = input(Fore.CYAN + "Entrez votre pays de naissance: ")
        self.user_data["adresse"] = input(Fore.CYAN + "Entrez votre adresse: ")

        # Vérification email
        while True:
            email = input(Fore.CYAN + "Entrez votre adresse mail: ")
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                self.user_data["email"] = email
                break
            else:
                print(Fore.RED + "⚠️ Adresse email invalide. Réessayez.")

        # Récapitulatif et confirmation
        while True:
            print(Fore.MAGENTA + "\n--- RÉCAPITULATIF ---")
            for k, v in self.user_data.items():
                print(Fore.YELLOW + f"{k} : {v}")

            ready = input(Fore.CYAN + "\nÊtes-vous prêt pour le jeu ? (y/n): ").lower()
            if ready == "y":
                break
            elif ready == "n":
                print(Fore.GREEN + "Pas de problème, prends ton temps...")
            else:
                print(Fore.RED + "Veuillez répondre par y ou n")

    def ask_questions(self, theme, questions):
        print(Fore.BLUE + f"\n🎯 Thème choisi : {theme}\n")
        for i, (question, options, correct) in enumerate(questions, 1):
            print(Fore.CYAN + f"Q{i}. {question}")
            for idx, opt in zip("ABCDEF", options):
                print(Fore.YELLOW + f"   {idx}. {opt}")

            while True:
                answer = input(Fore.CYAN + "Votre réponse (A-F): ").upper()
                if answer in "ABCDEF":
                    break
                else:
                    print(Fore.RED + "Veuillez entrer une lettre entre A et F")

            if answer == correct:
                self.score += 1
                print(Fore.GREEN + emojize(f"✅ Bonne réponse 😃 ! Score = {self.score}\n"))
            else:
                print(Fore.RED + emojize(f"❌ Mauvaise réponse 😢 ! Score = {self.score}\n"))

    def end_game(self):
        prenom = self.user_data["nom_complet"].split()[0]
        print(Fore.MAGENTA + "\n🎉 FIN DU JEU 🎉")
        print(Fore.CYAN + f"Bravo {prenom}, ton score final est {self.score}/10")
        print(Fore.YELLOW + r"""
        ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
        ✨   V I C T O I R E  ✨
        ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
        """)

football_questions = [
    ("Quel pays a gagné la Coupe du Monde 2018 ?",
     ["Brésil", "Allemagne", "France", "Argentine", "Italie", "Espagne"], "C"),
    ("Qui est surnommé 'CR7' ?",
     ["Messi", "Cristiano Ronaldo", "Neymar", "Mbappé", "Benzema", "Ronaldinho"], "B"),
    ("Dans quel club joue Lionel Messi en 2025 ?",
     ["Inter Miami", "PSG", "Barcelone", "Manchester City", "Chelsea", "Naples"], "A"),
    ("Combien de joueurs sur le terrain pour une équipe ?",
     ["9", "10", "11", "12", "7", "8"], "C"),
    ("Quel club a gagné la Ligue des Champions 2022 ?",
     ["Real Madrid", "Liverpool", "PSG", "Chelsea", "Manchester City", "Milan AC"], "A"),
    ("Qui a marqué la 'Main de Dieu' ?",
     ["Pelé", "Maradona", "Messi", "Ronaldo", "Ronaldinho", "Zidane"], "B"),
    ("Quel pays a gagné le plus de Coupes du Monde ?",
     ["Brésil", "Allemagne", "Italie", "Argentine", "Uruguay", "France"], "A"),
    ("Qui est le meilleur buteur de l’histoire de la Coupe du Monde ?",
     ["Klose", "Ronaldo Nazario", "Messi", "Cristiano Ronaldo", "Mbappé", "Pelé"], "A"),
    ("En quelle année a eu lieu la première Coupe du Monde ?",
     ["1920", "1930", "1940", "1950", "1960", "1910"], "B"),
    ("Quel joueur a remporté 7 Ballons d’Or ?",
     ["Messi", "Cristiano Ronaldo", "Platini", "Zidane", "Ronaldinho", "Mbappé"], "A"),
]

science_questions = [
    ("Quelle planète est la plus proche du Soleil ?",
     ["Vénus", "Mercure", "Mars", "Jupiter", "Saturne", "Terre"], "B"),
    ("Quelle est la formule chimique de l’eau ?",
     ["CO2", "H2O", "O2", "NaCl", "CH4", "NH3"], "B"),
    ("Qui a découvert la gravitation ?",
     ["Einstein", "Newton", "Galilée", "Copernic", "Kepler", "Pythagore"], "B"),
    ("Quel est l’organe principal de la respiration ?",
     ["Cœur", "Poumons", "Foie", "Estomac", "Reins", "Peau"], "B"),
    ("Quelle est la vitesse de la lumière ?",
     ["300 000 km/s", "150 000 km/s", "100 000 km/s", "30 000 km/s", "1 000 km/s", "1 million km/s"], "A"),
    ("Quel est l’élément chimique du symbole Fe ?",
     ["Fer", "Fluor", "Francium", "Phosphore", "Fructose", "Fluide"], "A"),
    ("Qui a inventé la théorie de la relativité ?",
     ["Newton", "Einstein", "Tesla", "Curie", "Hawking", "Planck"], "B"),
    ("Quel est le plus grand organe du corps humain ?",
     ["Cerveau", "Peau", "Foie", "Poumons", "Intestin", "Reins"], "B"),
    ("Combien de bases dans l’ADN ?",
     ["2", "3", "4", "5", "6", "7"], "C"),
    ("Quelle est la température du zéro absolu ?",
     ["0°C", "-100°C", "-273°C", "-500°C", "-1000°C", "-200°C"], "C"),
]

histoire_questions = [
    ("Qui était le premier empereur de Rome ?",
     ["César", "Auguste", "Néron", "Trajan", "Constantin", "Caligula"], "B"),
    ("En quelle année Christophe Colomb a-t-il découvert l’Amérique ?",
     ["1492", "1500", "1600", "1400", "1480", "1550"], "A"),
    ("Qui était le roi de France pendant la Révolution française ?",
     ["Louis XIV", "Louis XV", "Louis XVI", "Louis XVII", "Henri IV", "Napoléon"], "C"),
    ("En quelle année a eu lieu la chute du Mur de Berlin ?",
     ["1980", "1985", "1989", "1991", "1979", "1995"], "C"),
    ("Qui a mené la marche du sel en Inde ?",
     ["Gandhi", "Nehru", "Mandela", "Martin Luther King", "Tagore", "Patel"], "A"),
    ("Quel pays fut dirigé par Nelson Mandela ?",
     ["Nigeria", "Afrique du Sud", "Kenya", "Ghana", "Congo", "Tanzanie"], "B"),
    ("Quel traité a mis fin à la Première Guerre mondiale ?",
     ["Versailles", "Tordesillas", "Vienne", "Utrecht", "Paris", "Brest-Litovsk"], "A"),
    ("Quel empire avait Gengis Khan ?",
     ["Romain", "Mongol", "Ottoman", "Chinois", "Perse", "Inca"], "B"),
    ("Qui était pharaon lors de la construction de la Grande Pyramide ?",
     ["Khéops", "Ramsès II", "Toutankhamon", "Akhenaton", "Cléopâtre", "Thoutmôsis"], "A"),
    ("Quelle bataille a marqué la fin de Napoléon ?",
     ["Austerlitz", "Waterloo", "Iéna", "Marengo", "Moscou", "Lodi"], "B"),
]

geographie_questions = [
    ("Quelle est la capitale de la France ?",
     ["Madrid", "Paris", "Berlin", "Rome", "Bruxelles", "Londres"], "B"),
    ("Quel est le plus grand océan ?",
     ["Atlantique", "Pacifique", "Indien", "Arctique", "Austral", "Méditerranée"], "B"),
    ("Combien y a-t-il de continents ?",
     ["5", "6", "7", "8", "9", "4"], "C"),
    ("Quel est le plus long fleuve du monde ?",
     ["Nil", "Amazon", "Yangtsé", "Mississippi", "Congo", "Danube"], "B"),
    ("Dans quel pays se trouve le Kilimandjaro ?",
     ["Kenya", "Tanzanie", "Éthiopie", "Ouganda", "Afrique du Sud", "Zimbabwe"], "B"),
    ("Quel désert est le plus grand ?",
     ["Sahara", "Gobi", "Kalahari", "Mojave", "Arctique", "Antarctique"], "F"),
    ("Quel pays a le plus d’habitants en 2025 ?",
     ["USA", "Inde", "Chine", "Indonésie", "Nigeria", "Brésil"], "B"),
    ("Quelle est la capitale de l’Australie ?",
     ["Sydney", "Canberra", "Melbourne", "Perth", "Adelaide", "Brisbane"], "B"),
    ("Quel pays a pour capitale Ankara ?",
     ["Grèce", "Égypte", "Turquie", "Iran", "Syrie", "Chypre"], "C"),
    ("Quel est le pays le plus grand du monde ?",
     ["Canada", "Chine", "USA", "Russie", "Brésil", "Australie"], "D"),
]
if __name__ == "__main__":
    game = QuizGame()
    game.get_user_info()

    # Choix du thème avec contrôle de saisie
    while True:
        print(Fore.CYAN + "\nChoisissez un thème :")
        print(Fore.YELLOW + "1. Football ⚽\n2. Science 🔬\n3. Histoire 📜\n4. Géographie 🌍")
        choix = input(Fore.CYAN + "Votre choix (1-4): ")

        if choix == "1":
            game.ask_questions("Football", football_questions)
            break
        elif choix == "2":
            game.ask_questions("Science", science_questions)
            break
        elif choix == "3":
            game.ask_questions("Histoire", histoire_questions)
            break
        elif choix == "4":
            game.ask_questions("Géographie", geographie_questions)
            break
        else:
            print(Fore.RED + "Veuillez entrer un nombre entre 1 et 4")

    game.end_game()
