import random

# счётчик поверженных героем чудовищ
monster_counter = None

# текущее состояние здоровье героя
hp = None

# текущая сила атаки героя
attack = None


def game() -> None:
    """Игра Герой и чудовища...

    Игрок - рыцарь в фантастической стране.
    Ваша задача - победить 10 чудовищ чтобы спасти королевство от нападения
    и тем самым выиграть игру.
    """
    global hp
    global attack
    global monster_counter

    monster_counter = 0
    hp = random.randint(25, 55)
    attack = random.randint(10, 20)

    print("Игра началась!")

    # события имеющиеся в игре
    events = ["monster", "sword", "apple"]

    # цикл событий/ходов игры
    while monster_counter < 10 and hp > 0:
        # выводим информацию о рыцаре
        print("Состояние здоровья рыцаря =", str(hp))
        print("Сила атаки рыцаря =", str(attack))

        # генерируем случайное число в диапозоне от [0 до 2] включительно
        # для получения рандомного события
        index = random.randint(0, 2)

        # получаем название события
        event = events[index]

        if event == "monster":
            print("Вы встретили чудовище!")

            # сила атаки чудовища
            monster_attack = random.randint(5, 10)

            # состояние здоровья чудовища
            monster_hp = random.randint(5, 15)

            # выводим информацию о чудовище
            print("Состояние здоровья чудовища =", str(monster_hp))
            print("Сила атаки чудовища =", str(monster_attack))

            # ответ от пользователя
            answer = None

            # если is_answer_correct == True значит ответ корректный
            is_answer_correct = False

            # спрашиваем, будет ли рыцарь драться
            while not is_answer_correct:
                print("Будем ли драться?")
                print("Введите цифру: 1 -- драться; 2 -- убежать.")

                # выводим контрольную строку
                print("БОЙ", str(monster_hp), str(monster_attack))

                # получаем ответ
                answer = input("ваш ответ: ")

                # если ответ '1' или '2', то ответ правильный и больше
                # не переспрашиваем
                if answer == "1" or answer == "2":
                    is_answer_correct = True
                else:
                    print("Вы ввели не правильный ответ, попробуйте ещё!")

            # если ответ 1, то вступаем в бой, иначе убегаем
            if answer == "1":
                # наступила смерть либо героя либо чудовища
                # если is_death == True то значит кто-то умер,
                # т.е. бой закончен
                is_death = False

                # цикл ударов
                while not is_death:
                    # герой бьёт монстра и отнимает жизнь равную
                    # силе атаки героя
                    monster_hp -= attack

                    # и наоборот
                    hp -= monster_attack

                    # если состояние здоровья рыцаря больше 0,
                    # а у чудовища меньше или равно 0
                    # то значит мы победили и нужно увеличить счётчик
                    # побежденных чудовищ
                    if hp > 0 and monster_hp <= 0:
                        monster_counter += 1
                        print("Ура! Чудовище повержено!")

                    # если наступила смерть одного из двух
                    if hp <= 0 or monster_hp <= 0:
                        # то бой закончен
                        is_death = True

            else:
                print("Убегаем!")

        elif event == "sword":
            sword_attack = random.randint(5, 25)

            print("Вы нашли оружее !!!", "Сила атаки оружея =", str(sword_attack))

            # ответ от пользователя
            answer = None

            # если is_answer_correct == True значит ответ корректный
            is_answer_correct = False

            # спрашиваем, будем ли брать этот меч
            while not is_answer_correct:
                print("Будем ли брать это оружее?")
                print("Введите цифру: 1 -- подобрать; 2 -- пройти мимо.")

                # выводим контрольную строку
                print("MEЧ", str(sword_attack))

                # получаем ответ
                answer = input("ваш ответ: ")

                # проверяем корректность ответа
                # если ответ '1' или '2', то ответ правильный и
                # больше не переспрашиваем
                if answer == "1" or answer == "2":
                    is_answer_correct = True
                else:
                    print("Вы ввели не правильный ответ, попробуйте ещё!")

            if answer == "1":
                attack = sword_attack
                print("Вы подобрали оружее и теперь ваша сила атаки =", attack)

        elif event == "apple":
            print("Вы нашли яблоко !!!")

            # генерируем живительную силу яблока
            apple_hp = random.randint(5, 10)

            # съедаем яблоко
            hp += apple_hp

            print(
                "Ваше состояние здорвье увеличилось на",
                str(apple_hp),
                "и теперь оно =",
                str(hp),
            )

        # проверяем состояние рыцаря
        if hp <= 0:
            # значит мы проиграли и завершаем игру
            print("Конец игры! Вы проиграли игру.")

            # выводим контрольную строку
            print("ПОРАЖЕНИЕ")

        elif monster_counter == 10:
            print("Вы победили", str(monster_counter), "чудовищ!")

            # выводим контрольную строку
            print("ПОБЕДА")

    quit()


if __name__ == "__main__":
    game()
