from pyscript import document

player_list = [
    "1. Ancheta, Arthur Eugene Maximus Adarna",
    "2. Asuncion, Miguelito Alonso Brigoli",
    "3. Battung, John Lorenzo Quisumbing",
    "4. Buenvenida, Victor Emmanuel Bernardino",
    "5. Casul, McKayla Analisse Gabor",
    "6. Catapang, Athena La Verne Sarabia",
    "7. Chua, Cade Rylie Rivera",
    "8. Eusebio, Zyan Riley Tancinco",
    "9. Evangelio, Princess Radhika Zayn Divino",
    "10. Fado, Marianna Reinne Fabie",
    "11. Fermocil, Kleiser Ferida",
    "12. Fernando, Curt Joshua Nicolas",
    "13. Francia, Ethan Raphael Juanga",
    "14. Jimenez, Sophia San Buenaventura",
    "15. Mabilog, Javier Antonio Villadolid",
    "16. Mactal, Al Chrian Abueme",
    "17. Magday, Constance Soleil Gustilo",
    "18. Moya, Yanna Clarisse Obial",
    "19. Mutia, Francheska Zoe Abesamis",
    "20. Nazareno, Luis Gabriel IV Villarico",
    "21. Quinto, Arabella Faith Katipunan",
    "22. Romero, Jose Inigo Abalajon",
    "23. Santos, Kyler",
    "24. Sarao, Jaedin Hailey Balberan",
    "25. Sy, Briana Gabrielle Calaranan",
    "26. Sy, Charlotte Anne Estrada",
    "27. Udono, Jared Daniel Maulas",
    "28. Vida, Mary Kristine Claire Parra",
]

def show_list(event=None):
    container = document.getElementById("list-container")
    container.innerHTML = "<br>".join(player_list)