import random

# Liang Baiqi's score, initially 0
score = 0

while True:
    print("World-class top idol Liang Baiqi lost a dare with Liao Yucheng and now has to accept the punishment of wearing women's clothing that you choose for him.")
    print("You can choose from the following outfits:")
    print("1. Barbie doll-style dress")
    print("2. Pink dress")
    print("3. Casual outfit (will not trigger random events)")
    print("4. School uniform (will not trigger random events)")
    print("5. Wearing winter and summer school uniforms together (adds 5 points)")

    choice = input("Please select Liang Baiqi's outfit (enter 1, 2, 3, 4, or 5): ")
    if choice == '1':
        print("Liang Baiqi put on the Barbie doll-style dress.")
        # Simulate random events
        event = random.randint(1, 4)
        if event == 1:
            score -= 5
            print("Oops, Liang Baiqi was penalized for violating school rules (wearing strange clothing), his current score is:", score)
            print("Liang Baiqi thinks: This messed-up school rule, why is the cost of playing a game so harsh, I have to lose points.")
        elif event == 2:
            print("Liang Baiqi was laughed at by the boys in his class; they are teasing him.")
            print("Liang Baiqi feels uncomfortable: Hmph, what are you laughing at? Don't go too far!")
        elif event == 3:
            print("A girl said Liang Baiqi is a pervert, so awkward.")
            print("Liang Baiqi feels a bit wronged: I don’t want to be like this, it’s all because of the dare.")
        elif event == 4:
            score += 3  # Someone praised Liang Baiqi's beauty, gaining positive points
            print("Someone said Liang Baiqi looks very pretty as a ‘girl’, but it feels a bit strange.")
            print("Liang Baiqi secretly mutters: Pretty? What kind of compliment is this? But at least I can gain a few points. Current score:", score)
        input("Press any key to return to the selection page.")
    elif choice == '2':
        print("Liang Baiqi put on the pink dress.")
        # Simulate random events
        event = random.randint(1, 4)
        if event == 1:
            score -= 5
            print("Oops, Liang Baiqi was penalized for violating school rules (wearing strange clothing), his current score is:", score)
            print("Liang Baiqi thinks: This school rule is really a trap; the cost of playing a game is so high.")
        elif event == 2:
            print("Liang Baiqi was laughed at by the boys in his class; they are teasing him.")
            print("Liang Baiqi feels uncomfortable: Hmph, what are you laughing at? Don't go too far!")
        elif event == 3:
            print("A girl said Liang Baiqi is a pervert, so awkward.")
            print("Liang Baiqi feels a bit wronged: I don’t want to be like this, it’s all because of the dare.")
        elif event == 4:
            score += 3  # Someone praised Liang Baiqi's beauty, gaining positive points
            print("Someone said Liang Baiqi looks very pretty as a ‘girl’, but it feels a bit strange.")
            print("Liang Baiqi secretly mutters: Pretty? What kind of compliment is this? But at least I can gain a few points. Current score:", score)
        input("Press any key to return to the selection page.")
    elif choice == '3':
        print("Liang Baiqi chose a casual outfit; nothing particularly special happened.")
        print("Liang Baiqi's score remains:", score)
        input("Press any key to return to the selection page.")
    elif choice == '4':
        print("Liang Baiqi put on the school uniform; nothing particularly special happened.")
        print("Liang Baiqi's score remains:", score)
        input("Press any key to return to the selection page.")
    elif choice == '5':
        print("Liang Baiqi wore the winter and summer school uniforms together, looking a bit strange.")
        score += 5
        print("Due to Liang Baiqi's creative outfit combination, he gained 5 points. Current score:", score)
        input("Press any key to return to the selection page.")
