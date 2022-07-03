# mad lib generator fun game..
import tkinter as tk
import pyttsx3

root = tk.Tk()
root.geometry("800x500")
root.configure(bg="#637187")
root.title("GAME")

label = tk.Label(root, text="Fun Fhrase!",
                 foreground="white",
                 background="#637187",
                 font=("Gabriola", 55, "bold")).pack()

label1 = tk.Label(root, text="Choose a category:",
                  foreground="#E7EBF1",
                  background="#637187",
                  font=("Gabriola", 28)).place(x=10, y=120)


def inventStory():
    new = tk.Toplevel(root)
    new.geometry("800x500")
    new.title("Invention")
    new.configure(bg="#637187")

    def generateStory():
        story1 = "My best Invention yet was my idea for a combined " + e6.get() + ", " + e2.get() + " and " + e7.get() + ".\n I called " \
                                                                                                                         "it the " + e1.get() + " mobile.\n It meant that wherever you go, you don't need to change the vehicles.\nThe only problem " \
                                                                                                                                                "was that engines from the " + e6.get() + " were too " + e5.get() + " for it to fly, so I invented " \
                                                                                                                                                                                                                    " an engine  that worked on " + e4.get() + " and " + e8.get() + ".\nWhile working on this, I got really hungry " \
                                                                                                                                                                                                                                                                                    "so I ate " + e4.get() + " with " + e2.get() + " and it was really yum. \n " + e3.get() + ", you should try this too."
        storyLabel = tk.Label(new, text=story1, foreground="white", background="#637187", font=("Candara", 15))
        storyLabel.place(x=6, y=220)
        storyLabel.config(bg="#2b2722")

        def readStory():
            engine = pyttsx3.init()

            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            engine.setProperty('rate', 150)

            engine.say(story1)
            engine.runAndWait()

        read_btn = tk.Button(new,
                             text="READ",
                             command=readStory,
                             font=("Canada", 13),
                             fg="#fbfbfa",
                             bg="#02782e",
                             )
        read_btn.place(x=720, y=280)

    name = tk.Label(new, text="NickName")
    name.place(x=10, y=50)
    e1 = tk.Entry(new)
    e1.place(x=110, y=50)

    shampoo = tk.Label(new, text="Shampoo brand")
    shampoo.place(x=10, y=70)
    e2 = tk.Entry(new)
    e2.place(x=110, y=70)

    b_name = tk.Label(new, text="BestFriend Name")
    b_name.place(x=10, y=90)
    e3 = tk.Entry(new)
    e3.place(x=110, y=90)

    food_item = tk.Label(new, text="Food item")
    food_item.place(x=10, y=110)
    e4 = tk.Entry(new)
    e4.place(x=110, y=110)

    adjective = tk.Label(new, text="Adjective")
    adjective.place(x=10, y=130)
    e5 = tk.Entry(new)
    e5.place(x=110, y=130)

    vehicle = tk.Label(new, text="Car Company")
    vehicle.place(x=10, y=150)
    e6 = tk.Entry(new)
    e6.place(x=110, y=150)

    fan = tk.Label(new, text="Fan Brand")
    fan.place(x=10, y=170)
    e7 = tk.Entry(new)
    e7.place(x=110, y=170)

    ground = tk.Label(new, text="Stadium Name")
    ground.place(x=10, y=190)
    e8 = tk.Entry(new)
    e8.place(x=110, y=190)

    g_btn = tk.Button(new,
                      text="Generate",
                      font=("Canada", 13),
                      command=generateStory)
    g_btn.place(x=80, y=460)

    # vehicle = input("Enter a car company.")
    # food_item = input("Enter a food item/dish name.")
    # adjective = input("Enter an adjective.")
    # friend_name = input("Enter your best friend's name.")
    # fan = input("Enter a fan company.")
    # name = input("Enter a nickname.")
    # ground = input("Enter name of any playground/stadium.")
    # shampoo = input("Enter a shampoo company.")
    # story1 = (f"My best invention yet was my idea for a combined {vehicle}, {shampoo} and "
    #           f"{fan}. I called it the {name.capitalize()} mobile. It meant that wherever you go, "
    #           f"you don't need to change the vehicles. The only problem was that engines from the "
    #           f"{vehicle} were too {adjective} for it to fly, so I invented an engine that worked on "
    #           f"{food_item} and {ground}. While working on this, I got really hungry so I ate {food_item} with "
    #           f"{shampoo} and it was really yum. {friend_name}, you should try this too.")

    # print(story1)


def foodStory():
    new = tk.Toplevel(root)
    new.geometry("600x500")
    new.title("Food")
    new.configure(bg="#637187")

    def generateStory():
        story2 = "Let's begin this awesome recipe.\n All you need is some " + e1.get() + ".\n" \
                                                                                         "Peel it with " + e3.get() + " so that it looks like the face of a " + e6.get() + ".\nToss this masterpiece in " + e5.get() + ".\n Add salt and black pepper and mix it well. \nNow serve it on a plate with " + e4.get() + " sprinkles. \nThis would be a renowned dish named " + e6.get() + " " + e1.get() + " pasta.\n Enjoy this dish with a " + e2.get() + " smoothie!"

        storyLabel = tk.Label(new, text=story2, foreground="white", background="#637187", font=("Candara", 15))
        storyLabel.place(x=20, y=220)

        def readStory():
            engine = pyttsx3.init()

            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            engine.setProperty('rate', 150)

            engine.say(story2)
            engine.runAndWait()

        read_btn = tk.Button(new,
                             text="READ",
                             command=readStory,
                             font=("Canada", 13),
                             fg="#fbfbfa",
                             bg="#02782e",
                             )
        read_btn.place(x=720, y=280)

    veggie = tk.Label(new, text="Vegetable")
    veggie.place(x=10, y=50)
    e1 = tk.Entry(new)
    e1.place(x=90, y=50)

    color = tk.Label(new, text="Color")
    color.place(x=10, y=70)
    e2 = tk.Entry(new)
    e2.place(x=90, y=70)

    weapon = tk.Label(new, text="Weapon")
    weapon.place(x=10, y=90)
    e3 = tk.Entry(new)
    e3.place(x=90, y=90)

    flavour = tk.Label(new, text="Flavour")
    flavour.place(x=10, y=110)
    e4 = tk.Entry(new)
    e4.place(x=90, y=110)

    oil = tk.Label(new, text="Oil")
    oil.place(x=10, y=130)
    e5 = tk.Entry(new)
    e5.place(x=90, y=130)

    animal = tk.Label(new, text="Animal")
    animal.place(x=10, y=150)
    e6 = tk.Entry(new)
    e6.place(x=90, y=150)

    g_btn = tk.Button(new,
                      text="Generate",
                      command=generateStory)
    g_btn.place(x=80, y=460)

    # color = input("Enter a color.")
    # veggie1 = input("Enter a vegetable.")
    # weapon = input("Enter a weapon name.")
    # oil = input("Enter a type of oil.")
    # flavour = input("Enter a flavour.")
    # animal = input("Enter an animal.")
    # story2 = (f"Let's begin this awesome recipe. All you need is some {veggie1}. "
    #           f"Peel it with {weapon} so that it looks like the face of {animal}. Toss this masterpiece "
    #           f"in {oil}. Add salt and black pepper and mix it well. Now serve it on a plate with "
    #           f"{flavour} sprinkles. This would be a renowned dish named {animal} {veggie1} pasta. "
    #           f"Enjoy this with a {color} smoothie.")

    # print(story2)


def animalStory():
    new = tk.Toplevel(root)
    new.geometry("600x500")
    new.title("Animal")
    new.configure(bg="#637187")

    def generateStory():
        story3 = "Today we went to the Zoo! The first thing we saw a " + e2.get() + " " + e4.get() + " " + e3.get() + \
                 "ing.\nThe Zookeeper told us that was normal, except in " + e1.get() + ". \nI had a " + e5.get() + " time! " \
                                                                                                                    "\nNext time, I will remember that if I ever see " + e2.get() + " " + e4.get() + "s. \nI should " + e6.get() + " the other way."

        storyLabel = tk.Label(new, text=story3, foreground="white", background="#637187", font=("Candara", 15))
        storyLabel.place(x=20, y=220)

        def readStory():
            engine = pyttsx3.init()

            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            engine.setProperty('rate', 150)

            engine.say(story3)
            engine.runAndWait()

        read_btn = tk.Button(new,
                             text="READ",
                             command=readStory,
                             font=("Canada", 13),
                             fg="#fbfbfa",
                             bg="#02782e",
                             )
        read_btn.place(x=720, y=280)

    c_name = tk.Label(new, text="Country ")
    c_name.place(x=30, y=50)
    e1 = tk.Entry(new)
    e1.place(x=85, y=50)

    color = tk.Label(new, text="Color")
    color.place(x=30, y=70)
    e2 = tk.Entry(new)
    e2.place(x=85, y=70)

    verb1 = tk.Label(new, text="Verb")
    verb1.place(x=30, y=90)
    e3 = tk.Entry(new)
    e3.place(x=85, y=90)

    animal_name = tk.Label(new, text="Animal")
    animal_name.place(x=30, y=110)
    e4 = tk.Entry(new)
    e4.place(x=85, y=110)

    adjective = tk.Label(new, text="Adjective")
    adjective.place(x=30, y=130)
    e5 = tk.Entry(new)
    e5.place(x=85, y=130)

    verb2 = tk.Label(new, text="Verb")
    verb2.place(x=30, y=150)
    e6 = tk.Entry(new)
    e6.place(x=85, y=150)

    g_btn = tk.Button(new,
                      text="Generate",
                      command=generateStory)
    g_btn.place(x=80, y=460)  # g_btn.pack(side=tk.BOTTOM)

    # color = input("Enter a color.")
    # animal = input("Enter an animal.")
    # verb1 = input("Enter a verb/action word.")
    # country_name = input("Enter a country name.")
    # adjective = input("Enter an adjective.")
    # verb2 = input("Enter a different verb again.")
    #
    # story3 = (f"Today we went to the Zoo! The first thing we saw was a {color} {animal} {verb1}ing."
    #           f"The Zookeeper told us that was normal, except in {country_name}.I had a {adjective} "
    #           f"time! Next time, I will remember that if I ever see {color} {animal}s, I should "
    #           f"{verb2} the other way.")
    # print(story3)


btn1 = tk.Button(root,
                 text="INVENTION",
                 font=("Canada", 15),
                 command=inventStory)
btn1.place(x=10, y=210)

btn2 = tk.Button(root,
                 text="FOOD",
                 font=("Canada", 15),
                 command=foodStory)
btn2.place(x=10, y=270)

btn3 = tk.Button(root,
                 text="ANIMAL",
                 font=("Canada", 15),
                 command=animalStory)
btn3.place(x=10, y=330)

root.mainloop()
