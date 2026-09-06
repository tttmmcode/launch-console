print("Welcome to the Launch Console!")

name = input("What is your name? ")

print(f'Hi, {name}!')

def about_me():
    print("Hello, my name is Taheem Mustaneer, and I am a student at Westwood High School in Austin, TX. " \
    "I am a programmer on my school's FIRST Tech Challenge team and I participate in the Code2College Elite 101 Program. " \
    "I am passionate about building mobile apps to solve real-world problems. My latest pursuit has been an outdoor engagement app called TouchGrass (touchgrass.web.app). " \
    "I hope you can see some of my work and interests!")


def my_goals():
    print("I hope to work with a team of developers to deliver real solutions to problems faced")
    print("by companies every day. Specifically, I want to learn how to integrate AI in my workflow to improve")
    print("efficiency and productivity.")


while True:
    menu_option = input("Choose an option: About me (1), My goals (2), TouchGrass (3), Exit (4): ")

    if menu_option == "1":
        about_me()
    elif menu_option == "2":
        my_goals()
    elif menu_option == "3":
        print("My latest project is TouchGrass, an outdoor engagement app.")
    elif menu_option == "4":
        print("Exiting the Launch Console. Goodbye!")
        break
    else:
        print("Please choose a valid option.")
