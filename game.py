import random
import dictionaries

while True:

    def symbol_corrector(input_u) -> str:
        while not input_u.isalpha():
            if answer_language == "1":
                print(
                    "Your input contains non-letter symbols. Please, exclude them and try again."
                )
                input_u = input().strip().lower()
            else:
                print(
                    "Ваш ввод сожержит небуквенные символы. Пожалуйста, введите буквенный символ."
                )
                input_u = input().strip().lower()
            if input_u.isalpha():
                return input_u
        else:
            return input_u

    def rules(a: str) -> None:
        while True:
            if a == "да":
                print(
                    """\nВам нужно угадать слово, указанное в загадке. Вы должны выбрать букву, которая есть в слове. 
Если вы ошибаетесь, то рисуется висельник. Завершите игру до того, как нарисуется висельник!"""
                )
                break
            elif a == "yes":
                print(
                    """\nYou need to guess the word specified in the riddle. You have to choose the letter that is 
in the word. If you are wrong, then a gallows is drawn. Finish the game before the gallows are drawn! """
                )
                break
            elif a == "нет" or a == "no":
                pass
                break
            else:
                if answer_language == "1":
                    print("\nThe data entered is incorrect!")
                    a = input().lower().strip()
                else:
                    print("\nВведенные данные некорректны!")
                    a = input().lower().strip()

    def level(level_a: str) -> dict:
        while True:
            if level_a == "1" and answer_language == "1":
                words = dictionaries.English_dictionary_easy
                print("You have chosen an easy level!")
                return words
            elif level_a == "2" and answer_language == "1":
                words = dictionaries.English_dictionary_hard
                print("You have chosen a complex level!")
                return words
            elif level_a == "1" and answer_language == "2":
                words = dictionaries.Russian_dictionary_easy
                print("Вы выбрали легкий уровень сложности!")
                return words
            elif level_a == "2" and answer_language == "2":
                words = dictionaries.Russian_dictionary_hard
                print("Вы выбрали сложный уровень!")
                return words
            else:
                print("\nВведенные данные некорректны!/The data entered is incorrect!")
                level_a = input().strip().lower()

    def repeat(c_guess: str, a: list) -> str and list:
        while c_guess in a:
            if answer_language == "2":
                print(f"\nВы уже вводили {c_guess}.")
            else:
                print(f"\nYou have already entered {c_guess}.")
            guess_new = input().lower().strip()
            c_guess = symbol_corrector(guess_new)
        a.append(c_guess)
        return c_guess, a

    with open("hangmanpic.txt", "r") as f:
        picture = f.read()
        picture_of_man = tuple(picture.split(","))

    max_wrong = len(picture_of_man) - 1
    topic = ""
    word = ""
    print("\nYour language/Ваш язык: 1) English 2) Русский")
    answer_language = (
        input("Write the number of the language/Напишите цифру языка: ").strip().lower()
    )
    while True:
        if answer_language == "2":
            print("\nХотите ли Вы ознакомиться с правилами? Да/Нет")
            answer = input().lower().strip()
            rules(answer)
            break
        elif answer_language == "1":
            print("\nDo you want to read the rules? Yes/No")
            answer = input().lower().strip()
            rules(answer)
            break
        else:
            print("\nНеккоректный ввод!/Wrong input!")
            answer_language = input().strip().lower()

    if answer_language == "2":
        print(
            "\nВыберите режим игры: на двоих игроков или на одного игрока.\nВведите цифру 1, если на "
            "одного игрока. Введите цифру 2, если на двоих игроков."
        )
    else:
        print(
            "\nChoose the game mode: for two players or for one player.\nEnter the number 1 if for one "
            "player.Enter the number 2 if for two players."
        )

    answer_game_mode = input().strip().lower()
    while True:
        if answer_game_mode == "2":
            if answer_language == "2":
                print("\nВведите слово: ")
            else:
                print("\nEnter the word: ")
            word1 = input().lower().strip()
            word1_correction = symbol_corrector(word1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            word += word1_correction
            break
        elif answer_game_mode == "1":
            if answer_language == "2" and answer_game_mode == "1":
                print(
                    "\nВыберите уровень сложности!\nДля легкого введите 1, для сложного введите 2: "
                )
            elif answer_language == "1" and answer_game_mode == "1":
                print(
                    "\nSelect a difficulty level!\nEnter 1 for Easy level, enter 2 for Complex "
                    "level: "
                )
            level_answer = input().strip().lower()
            words1 = level(level_answer)
            topic1 = random.choice(list(words1.keys()))
            word1 = random.choice(list(words1[topic1]))
            word += word1
            topic += topic1
            break
        else:
            if answer_language == "2":
                print("\nНеверный ввод!")
            else:
                print("\nWrong input!")
            answer_game_mode = input().strip().lower()

    length_of_word = "_" * len(word)
    wrong = 0
    used_letter = []
    used_words = []
    while wrong < max_wrong and length_of_word != word:
        if answer_language == "2" and answer_game_mode == "1":
            print("\nТема:\n", topic)
        elif answer_language == "1" and answer_game_mode == "1":
            print("\nTopic:\n", topic)
        print(
            f"{picture_of_man[wrong]}\n{used_letter}\n{used_words}\n{length_of_word}\n"
        )
        if answer_language == "2":
            print("Введите букву или все слово: ")
        else:
            print("Enter a letter or a whole word: ")
        guess = input().lower().strip()
        corrected_guess = symbol_corrector(guess)

        if len(corrected_guess) > 1:
            repeat(corrected_guess, used_words)
            if corrected_guess == word:
                break
            else:
                wrong += 1
                if answer_language == "2":
                    print("\nНеверно")
                else:
                    print("\nIncorrectly")

        else:
            repeat(corrected_guess, used_letter)
            if corrected_guess in word:
                new = ""
                for i in range(len(word)):
                    if corrected_guess == word[i]:
                        new += word[i]
                    else:
                        new += length_of_word[i]
                length_of_word = new
            else:
                wrong += 1

    if wrong == max_wrong:
        if answer_language == "2":
            print("\nВас повесили\n(╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻")
        else:
            print("\nYou've died\n(╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻")
        print(picture_of_man[wrong])
    else:
        if answer_language == "2":
            print("\nУ тебя получилось!\n＼(￣▽￣)／")
        else:
            print("\nYou've won!\n＼(￣▽￣)／")
    print(f"\n{used_letter}\n{word.upper()}")

    while True:  # restart
        if answer_language == "2":
            print("\nЕще раз? (да/нет): ")
        else:
            print("\nAgain? (yes/no): ")
        answer = input().lower().strip()
        if answer in ("да", "нет", "yes", "no"):
            break
        if answer_language == "2":
            print("\nНеверный ввод")
        else:
            print("\nIncorrect type")
    if answer == "да" or answer == "yes":
        continue
    else:
        if answer_language == "2":
            print("\nСпасибо за игру!")
        else:
            print("\nThank you for playing!")
        break
