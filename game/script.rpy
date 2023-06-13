﻿# The script of the game goes in this file.

# The game starts here.
label start:
    if config.developer:
        show screen script_keymap
    stop music fadeout 1.0
    jump day1

label entrancehall:
    call screen entranceHall
    return

label kitchen:
    scene kitchen
    "Kitchen"
    return

label dining:
    scene dining_table
    "Dining"
    return

label bathroom1:
    scene bathroom
    "Batchroom1"
    return

label livingroom:
    scene living_room
    "Living Room"
    return

label basement:
    scene basement
    "Basement"
    return

label laundry:
    scene laundry
    "Laundry"
    return

label hallway:
    call screen hallWay
    return

label storage:
    scene storage_room
    "Storage Room"
    return

label bathroom2:
    scene bathtub
    "Bathroom 2"
    return

label studyroom:
    scene library
    "Study Room"
    return

label guestroom:
    scene bed
    "Guest Room"
    return

label childroom:
    scene bedroom day
    "Your Room"
    return

label masterroom:
    scene master_bedroom
    "Your Parent's Room"
    return

label testing:
    "1"
    "2"
    "3"
    "I will show some choices for testing"
    call testing_menu
    jump end

label testing_menu:
    menu:
        "Change player name":
            $ player_name = renpy.input("Input your new name.", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            "Your new name is [player_name]"
        "Get random achievement":
            $ randomly_grant_achievement()
            "Check your achievements I added some"
        "Show sprite size":
            show phantom 960
            "The sprite size is 960x960"
        "Write random diary":
            $ randomly_write_diary()
            "Check your diary I added some"
        "Meet some friend":
            $ meet_friend("Phantom")
            show phantom 960
            Phantom "Hi, nice to meet you."
            hide phantom
            "Now that you meet some friend, it will now be shown in your stats window."
        "Randomly decrease the value sanity and happiness" if  1 < sanity <= 100 and 1 < happiness <= 100:
            $ random_sanity = random.randint(1, sanity - 1)
            $ random_happiness = random.randint(1, happiness - 1)
            $ update_player_stats(-random_sanity, -random_happiness)
            $ random_sanity = abs(random_sanity)
            $ random_happiness = abs(random_happiness)
            "Check your stats window. I decrease your sanity by [random_sanity] and happiness by [random_happiness]"
        "Randomly increase the value sanity and happiness" if  1 <= sanity <= 99 and 1 <= happiness <= 99:
            $ random_sanity = random.randint(1, 100 - sanity)
            $ random_happiness = random.randint(1, 100 - happiness)
            $ update_player_stats(random_sanity, random_happiness)
            $ random_sanity = abs(random_sanity)
            $ random_happiness = abs(random_happiness)
            "Check your stats window. I increase your sanity by [random_sanity] and happiness by [random_happiness]"
        "Test Other Routes":
            jump routes_choices
    jump show_test_choices

label show_test_choices:
    "Do you want to test something again?"
    menu:
        "Yes":
            jump testing_menu
        "No":
            return

label routes_choices:
    menu:
        "Cloud Asking Name":
            call cloud_asking_name
        "Random Test":
            call random_test
        "Entrance Hall Map":
            call entrancehall
    jump show_test_choices

label random_test:
    $ output = renpy.variant("small")
    "Is Small Variant?: [output]"
    $ output = renpy.variant("pc")
    "Is PC Variant?: [output]"
    $ output = renpy.variant("mobile")
    "Is Mobile Variant?: [output]"
    "Im showing some sprites"
    "Ahmmm before that, what is your name?"
    "Meet Phantom [Child]"
    $ meet_friend(Phantom.name)
    $ write_diary("Ghost")
    show phantom 920
    Phantom "920x920"
    $ update_friends_stats(Phantom.name, 10)
    hide phantom 920
    Someone "..."
    $ meet_friend(Someone.name)
    show phantom 980
    Phantom "980x980"
    $ update_friends_stats(Phantom.name, 40)
    hide phantom 980
    Someone  "..."
    $ update_friends_stats(Someone.name, 75)
    show phantom 960
    Phantom "960x960"
    hide phantom
    $ update_friends_stats(Phantom.name, -20)
    $ grant_achievement("Achv8")
    "A{size=+5}A{/size}{size=+10}A{/size}{size=+15}A{/size}{size=+25}A{/size}"
    Child "eyyy"
    $ write_diary("Apple")
    "B"
    Child "bhii"
    "C"
    Child "sii"
    "D"
    Child "....... ..."
    "E"
    "F"
    "G"
    $ write_diary("Tree")
    return

label end:
    "3"
    "2"
    "1"
    "The End!"
    return
