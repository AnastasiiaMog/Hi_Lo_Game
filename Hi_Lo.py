import random
def hi_lo_game():
    print('Hi_Lo Game START')
    while True:
        number=random.randint(0,100)
        attempts = int(input("Скільки хочешь спроб?): "))
        print(f"\nЧисло від 0 до 100. У тебе є {attempts} спроб.")
        for i in range(1,attempts+1):
            while True:
                try:
                    enter_number=int(input(f"Спроба {i}: Введіть ваше число: "))
                    if 0<=enter_number<= 100:
                        break
                    else:
                        print("Введи число від 0 до 100.")
                except ValueError:
                    print("Це не число....")

            if enter_number == number:
                print(f"Вітаю! Ти виграв: загадане число {number} за {i} спроб!")
                break
            elif enter_number < number:
                print("Моє число більше......")
            else:
                print("Моє число менше.....")
        else:
            print(f"\nТи програв(. Моє число було {number}.")
        play_again = input("\nХочеш ще раз? (+/-): ")
        if play_again != '+':
            print("Бувай!Слава Україні")
            break
hi_lo_game()