print(
    """
     
                                 _..-------++._
                             _.-'/ |      _||  \"--._
                       __.--'`._/_\j_____/_||___\    `----.
                  _.--'_____    |          \     _____    /
                _j    /,---.\   |        =o |   /,---.\   |_
               [__]==// .-. \\==`===========/==// .-. \\=[__]
                 `-._|\ `-' /|___\_________/___|\ `-' /|_.'     
                       `---'                     `---'

 _______  _______ _________            _______           _______          
(  ____ \(  ____ \\__   __/           (  ___  )|\     /|(  ___  )|\     /|
| (    \/| (    \/   ) (              | (   ) || )   ( || (   ) |( \   / )
| |      | (__       | |      _____   | (___) || | _ | || (___) | \ (_) / 
| | ____ |  __)      | |     (_____)  |  ___  || |( )| ||  ___  |  \   /  
| | \_  )| (         | |              | (   ) || || || || (   ) |   ) (   
| (___) || (____/\   | |              | )   ( || () () || )   ( |   | |   
(_______)(_______/   )_(              |/     \|(_______)|/     \|   \_/   
                                                                          
"""
)
print("")
print("Welcome to Get-Away")
print("You have to escape the bank before you get caught!")
print("")


def restart_game():
    while True:
        restart = input("You got caught... Want to try again? Y or N? ").lower()
        if restart in {"yes", "y"}:
            print("")
            return True
        elif restart in {"no", "n"}:
            return False
        else:
            print("Invalid input, please enter 'Y' or 'N'.")


def play_again():
    while True:
        again = input("Do you want to play again? Y or N? ").lower()
        if again in {"yes", "y"}:
            return True
        else:
            return False


def game():
    while True:
        print("You start off in a bank vault, which way do you go?")
        first_answer = input("Straight or Left: ").lower()
        if first_answer in {"straight", "s"}:
            if not restart_game():
                break
        elif first_answer in {"left", "l"}:

            while True:
                print("")
                print("You have entered the Main Offices full of people working.")
                second_answer = input("Blend in or Run: ").lower()
                if second_answer in {"run", "r"}:
                    if not restart_game():
                        return False
                    break
                elif second_answer in {"blend in", "blend", "b"}:

                    while True:
                        print("")
                        print("You have now entered the bank lobby.")
                        third_answer = input("Front door or Fire Exit: ").lower()
                        if third_answer in {"front door", "front", "fd"}:
                            if not restart_game():
                                return False
                            break
                        elif third_answer in {"fire exit", "fire", "exit", "fe"}:
                            print("")
                            print("You made it to the Get-Away car!")
                            print(
                                """
           .      ..
   __..---/______//-----.        ((  )
 .".--.```|    - /.--.  =:    ( VROOM! ))  
(.: {} :__L______: {} :__; __--( __- -_= ) 
   *--*           *--*    """
                            )
                            print("")
                            return True
                        else:
                            print(
                                "Invalid input, try again... Type 'front door' or 'fire exit'"
                            )
                    break
                else:
                    print("Invalid input, try again... Type 'blend in' or 'run'")
        else:
            print("Invalid input, try again... Type 'straight' or 'left'")


while True:
    if not game():
        print("Thanks for playing!")
        break
    if not play_again():
        print("Thanks for playing!")
        break
