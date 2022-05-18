import random

while True:

    def rules(answer: str) -> None:
        while True:
            if answer == "да":
                print(
                    """\nВам нужно угадать слово, указанное в загадке. Вы должны выбрать букву, которая есть в слове. 
Если вы ошибаетесь, то рисуется висельник. Завершите игру до того, как нарисуется висельник!
Игра началась!"""
                )
                break
            elif answer == "yes":
                print(
                    """\nYou need to guess the word specified in the riddle. You have to choose the letter that is 
in the word. If you are wrong, then a gallows is drawn. Finish the game before the gallows are drawn! 
The game has started! """
                )
                break
            elif answer == "нет":
                print("\nИгра началась!")
                break
            elif answer == "no":
                print("\nThe game has started!")
                break
            else:
                if answer_language == 1:
                    print("\nThe data entered is incorrect!")
                    answer = input().lower().strip()
                else:
                    print("\nВведенные данные некорректны!")
                    answer = input().lower().strip()


    def level(level_answer: int) -> dict:
        while True:
            if level_answer == 1 and answer_language == 1:
                words = English_dictionary_easy
                print("You have chosen an easy level!")
                return words
            elif level_answer == 2 and answer_language == 1:
                words = English_dictionary_hard
                print("You have chosen a complex level!")
                return words
            elif level_answer == 1 and answer_language == 2:
                words = Russian_dictionary_easy
                print("Вы выбрали легкий уровень сложности!")
                return words
            elif level_answer == 2 and answer_language == 2:
                words = Russian_dictionary_hard
                print("Вы выбрали сложный уровень!")
                return words
            else:
                print("\nВведенные данные некорректны!/The data entered is incorrect!")
                level_answer = int(input().strip())
    picture_of_man = (
        """
        --------
        |      
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |   
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      0
        |     
        |     
        |
        ----------
        """,
        """
        --------
        |      |
        |      0
        |      X
        |      
        |
        ----------
        """,
        """
        --------
        |      |
        |      0
        |     /X
        |      
        |
        ----------
        """,
        """
        --------
        |      |
        |      0
        |     /X\  
        |      
        |
        ----------
        """,
        """
        --------
        |      |
        |      0
        |     /X\  
        |     /
        ----------
        """,
        """
        --------
        |      |
        |      0
        |     /X\ 
        |     / \ 
        |
        ----------
        """,
    )
    max_wrong = len(picture_of_man) - 1
    Russian_dictionary_easy = {
        "мебель": (
            "диван",
            "стол",
            "табурет",
            "шкаф",
            "вешалка",
            "кресло",
            "кровать",
            "стул",
        ),
        "животные": (
            "собака",
            "кошка",
            "свинья",
            "мышь",
            "жираф",
            "слон",
            "тигр",
            "лев",
            "волк",
        ),
        "одежда": (
            "кофта",
            "брюки",
            "платье",
            "рубашка",
            "юбка",
            "носки",
            "свитер",
            "пальто",
            "куртка",
        ),
        "фрукты": (
            "банан",
            "апельсин",
            "яблоко",
            "ананас",
            "мандарин",
            "персик",
            "абрикос",
            "груша",
        ),
    }
    English_dictionary_easy = {"furniture": ("sofa", "table", "stool", "wardrobe", "hanger", "armchair", "bed", "chair",
                                             "bookcase"),
                               "animals": ("dog", "cat", "pig", "mouse", "giraffe", "elephant", "tiger", "lion",
                                           "wolf"),
                               "clothes": ("jacket", "trousers", "dress", "shirt", "skirt", "socks", "sweater", "coat",
                                           "jacket"),
                               "fruits": ("banana", "orange", "apple", "pineapple", "tangerine", "kiwi", "peach",
                                          "apricot", "pear")}
    Russian_dictionary_hard = {
        "физика": (
            "амплитуда",
            "вакуум",
            "вольтметр",
            "дифракция",
            "изолятор",
            "интерференция",
            "конвекция",
            "конденсация",
            "радиоактивность",
        )
    }
    English_dictionary_hard = {
        "physics": (
            "amplitude",
            "vacuum",
            "voltmeter",
            "diffraction",
            "insulator",
            "interference",
            "convection",
            "condensation",
            "radioactivity",
        )
    }

    topic = ""
    word = ""
    print("Your language/Ваш язык: 1) English 2) Русский")
    while True:
        try:
            answer_language = int(
                input("Write the number of the language/Напишите цифру языка: ").strip()
            )
        except ValueError:
            print("Попробуйте еще раз/Try again")
        else:
            while True:
                if answer_language == 2:
                    print(
                        "\nВыберите режим игры: на двоих игроков или на одного игрока.\nВведите цифру 1, если на "
                        "одного игрока. Введите цифру 2, если на двоих игроков")
                    break
                elif answer_language == 1:
                    print(
                        "\nChoose the game mode: for two players or for one player.\nEnter the number 1 if for one "
                        "player.Enter the number 2 if for two players")
                    break
                else:
                    print("Неккоректный ввод!/Wrong input!")
                    answer_language = int(input().strip())

            while True:
                try:
                    answer_game_mode = int(input().strip())
                except ValueError:
                    if answer_language == 2:
                        print("Неверный ввод!")
                    else:
                        print("Wrong input!")
                else:
                    while True:
                        if answer_game_mode == 2:
                            word1 = input("введите слово").lower().strip()
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            word += word1
                            break
                        elif answer_game_mode == 1:
                            if answer_language == 1:
                                print("Do you want to read the rules? Yes/No")
                            else:
                                print("Хотите ли Вы ознакомиться с правилами? Да/Нет")
                            answer = input().lower().strip()
                            rules(answer)
                            break
                        else:
                            if answer_language == 2:
                                print("Неверный ввод!")
                            else:
                                print("Wrong input!")
                            answer_game_mode = int(input().strip())

                        while True:
                            try:
                                if answer_language == 2:
                                    print(
                                        "\nВыберите уровень сложности!\nДля легкого введите 1, для сложного введите 2: "
                                    )
                                    level_answer = int(input().strip())
                                    break
                                else:
                                    print(
                                        "\nSelect a difficulty level!\nEnter 1 for Easy level, enter 2 for Complex "
                                        "level: ")
                                    level_answer = int(input().strip())
                                    break
                            except ValueError:
                                if answer_language == 2:
                                    print("Неверный ввод!")
                                else:
                                    print("Wrong input!")
                        words1 = level(level_answer)
                        topic1 = random.choice(list(words1.keys()))
                        word1 = random.choice(list(words1[topic1]))
                        word += word1
                        topic += topic1
                        break

            length_of_word = "_" * len(word)
            wrong = 0
            used_letter = []
            while wrong < max_wrong and length_of_word != word:
                if answer_language == 2 and answer_game_mode == 1:
                    print("\nТема:\n", topic)
                elif answer_language == 1 and answer_game_mode == 1:
                    print("\nTopic:\n", topic)
                print(f"{picture_of_man[wrong]}\n{used_letter}\n{length_of_word}\n")
                if answer_language == 2:
                    print("Введите букву: ")
                else:
                    print("Enter a letter: ")
                guess = input().lower()
                while guess in used_letter:
                    if answer_language == 2:
                        print(f"Вы уже вводили букву {guess}. Введите другую букву:")
                    else:
                        print(
                            f"You have already entered the letter {guess}. Please enter a different letter:"
                        )
                    guess = input().lower()
                used_letter.append(guess)
                if guess in word:
                    new = ""
                    for i in range(len(word)):
                        if guess == word[i]:
                            new += word[i]
                        else:
                            new += length_of_word[i]
                    length_of_word = new
                else:
                    wrong += 1
            if wrong == max_wrong:
                if answer_language == 2:
                    print("Вас повесили")
                else:
                    print("You've died")
                print(picture_of_man[wrong])
            else:
                if answer_language == 2:
                    print("У тебя получилось!")
                else:
                    print("You've won!")
            print(f"\n{used_letter}\n{word}")

            while True:                                 # функция restart
                if answer_language == 2:
                    print("Еще раз? (да/нет): ")
                else:
                    print("Again? (yes/no): ")
                answer = input().lower().strip()
                if answer in ("да", "нет", "yes", "no"):
                    break
                if answer_language == 2:
                    print("Неверный ввод")
                else:
                    print("Incorrect type")
            if answer == "да" or answer == "yes":
                continue
            else:
                if answer_language == 2:
                    print("Спасибо за игру!")
                else:
                    print("Thank you for playing!")
                break

