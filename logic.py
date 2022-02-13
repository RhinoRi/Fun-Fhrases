# this is inspired by youtube channel kylie ying.

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madLib = (f"Computer programming is so {adj}! \nIt makes me so excited all the time  because i love to {verb1}.\n"
          f"Stay hydrated and {verb2} like you are {famous_person} ")


madLib2 = "Monday makes me feel so {adj}".format(adj=adj)

print(madLib)
print(madLib2)
