#This program will be a simple conversation between the program and the user.
conv=input("Would you like to have a conversation with me?")
if conv=="yes":  # I enjoy using If-statements so a part of this conversation will contain them. Plus it makes the program feel more flexible and/or realistic in my opinion.
    username=input("Hello there, my name is Conversation Program Version 1.0 or CPV1 for short. What is your name?")
    gender=input("Are you male or female?")
    if gender=="male":
        feelings=input("It's a pleasure to meet you, sir "+username+". How are you?")
    if gender=="female":
        feelings=input("It's a pleasure to meet you, M'lady "+username+". How are you?")
    day=input("I see. How was your day?")
    day2=input("Why was your day "+day+"?")
    print("That is very very interesting.")
    lecture=input("How are your lectures going?") #I put lectures so it would apply to eitehr the lecturer or a student.
    reason=input("Why are you lectures going "+lecture+"?")
    print("You're such an interesting person.")
    age=int(input("How old are you by the way?")) #I made the program ask the age now to show a bit of forgetfulness to make it feel a bit more real.
    if age > 50:
            print("Not so young anymore, eh?")
    if age > 30:
            print("You're not that young anymore, eh? It's okay, atleast you're not 50.. yet")
    else:
            input("You're quite young, aren't you?")
    print("It's been awesome talking with you and I hope we do it again sometime. Until then i bid you farewell and to have an awesome rest of your day.")
else:
    print("Okay, bye.")
