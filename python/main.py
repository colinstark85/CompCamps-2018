name = input("hello what is your name?")

def welcome(name):
    if name == "colin":
        print("hello colin")
    else:
        print ("welcome to compcamps 2018 {}".format(name))

        welcome(name)

        mits = ["bennett","kaitlin","rhiamon","austin","travis"]
        for mit in mit:
            welcome mit
