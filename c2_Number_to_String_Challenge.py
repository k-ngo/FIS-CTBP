
from tkinter import *
from tkinter import ttk
import random

#        KHOA NGO
#   2. NUMBER TO STRING CHALLENGE

# Open text files containing prefixes and suffixes, strip unneeded characters, then append them to lists.

with open('.\c2_Names_List\c2_First_Prefixes.txt', 'r') as f:
    first_prefix_list = f.readline().split(",")
    f.close()
first_prefix_list = [i.strip('\n') for i in first_prefix_list]

with open('.\c2_Names_List\c2_Second_Prefixes.txt', 'r') as f:
    second_prefix_list = f.readlines()
    f.close()
second_prefix_list = [i.strip('\n') for i in second_prefix_list]

with open('.\c2_Names_List\c2_First_Suffixes.txt', 'r') as f:
    first_suffix_list = f.readline().split(",")
    f.close()
first_suffix_list = [i.strip('\n') for i in first_suffix_list]

with open('.\c2_Names_List\c2_Second_Suffixes.txt', 'r') as f:
    second_suffix_list = f.readline().split(",")
    f.close()
second_suffix_list = [i.strip('\n') for i in second_suffix_list]

# I made the decision to use dict instead of list here for ease of access later.

item_type_dict = {
    0: 'Wand',
    1: 'Axe',
    2: 'Sword',
    3: 'Bow',
    4: 'Sceptre',
    5: 'Body Armour',
    6: 'Helmet',
    7: 'Gloves',
    8: 'Boots',
    9: 'Undergarment'
}

item_quality_dict = {
    0: 'Poor',
    1: 'Common',
    2: 'Uncommon',
    3: 'Rare',
    4: 'Epic',
    5: 'Mythical',
    6: 'Legendary',
    7: 'Heroic',
    8: 'Exalted',
    9: 'Exclusive Microtransaction'
}

def number_to_rpg_string(*args):

    # Obtain input value.

    numbers = loot_box_entry.get()

    # Check if there is enough fund to buy loot boxes.
    # If not, all you get is disappointment.

    if total_money.get() >= 10:
        total_money.set(total_money.get() - 10)
    else:
        card_ending.set('Your card ending in %s does not have sufficient fund.' %(''.join(numbers[-4:])))
        final_item.set('You have obtained\n\n[Disappointment]')
        return

    # Divide the provided card number into segments to serve as seeds. The seeds will later determine the loot.
    # If there are not enough numbers in the list to divide into meaningful segments,
    # the trailing number will be continuously appended to the list until len is >= 10.

    num_list = list(str(numbers))
    while len(num_list) < 10:
        num_list.append(num_list[-1])

    quality = int(num_list[len(num_list)//2])
    first_prefix = int(''.join(num_list[0:len(num_list)//4]))
    second_prefix = int(''.join(num_list[len(num_list)//4:len(num_list)*2//4]))
    item_type = int(num_list[len(num_list)//4])
    first_suffix = int(''.join(num_list[len(num_list)*2//4:len(num_list)*3//4]))
    second_suffix = int(''.join(num_list[len(num_list)*3//4:len(num_list)]))

    # Now that we have the seeds.
    # I convert the seeds to something equal to or less than the final index of the prefixes and suffixes lists.
    # This is done using the remainder operator because it will always give a value less than len of the list.
    # Doing so will allow me to obtain suitable indexes for prefixes and suffixes from the seeds.

    first_prefix = first_prefix_list[first_prefix % len(first_prefix_list)]
    second_prefix = second_prefix_list[second_prefix % len(second_prefix_list)]
    first_suffix = first_suffix_list[first_suffix % len(first_suffix_list)]
    second_suffix = second_suffix_list[second_suffix % len(second_suffix_list)]

    # Output everything we have as well as add money obtained from selling the loot to total_money.
    # Money obtained from selling the loot is decided purely by the quality + 5.

    total_money.set(total_money.get() + quality + 5)
    final_item.set('\nYou have obtained\n\n%s\n%s[%s] %s\n%s\n%s %s %s of %s %s\nValue: $%d\n%s' %('-' * 70, ' ' * 10, item_quality_dict[quality], '☆' * quality, '-' * 70, first_prefix, second_prefix, item_type_dict[item_type], first_suffix, second_suffix, quality + 5, '-' * 70))
    card_ending.set('Your card ending in %s has been charged sucessfully.\nYou have gained $%d from selling the loot. Net profit is $%d.\nTo obtain a new item please use a different card.\nThank you for your purchase.\n' %(''.join(numbers[-4:]), quality + 5, quality + 5 - 10))
    return

def sell_kidneys(*args):

    # In case you don't have enough money to buy loot boxes you can always sell kidney.

    if total_kidneys.get() > 0:
        total_money.set(total_money.get() + 30)
        total_kidneys.set(total_kidneys.get() - 1)
    return

def random_card(*args):

    # Provides a way of randomizing input.

    loot_box_id.set(random.randint(10**10, 20**10))
    return


# The code for the GUI is obtained from the official tutorial for the tkinter module.
# https://tkdocs.com/tutorial/firstexample.html
# The code has been extensively modified to suit my needs. Original code can be found on the link above.
# I used this module to create GUI purely because it is built into Python so no additional download is needed.

root = Tk()
root.title('RPG Loot Box Unboxing Simulator')

mainframe = ttk.Frame(root, padding='30 20 30 20') # W N E S
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Initialize variables

total_money = IntVar()
total_kidneys = IntVar()
loot_box_id = IntVar()
card_ending = StringVar()
final_item = StringVar()
total_money.set(20)
total_kidneys.set(2)

# Set up text labels, buttons, and entry form.

ttk.Label(mainframe, text='Welcome to RPG Loot Box Simulator!\nPlease enter credit card number to purchase loot box.').grid(column=2, row=1)

loot_box_entry = ttk.Entry(mainframe, width=60, textvariable=loot_box_id)
loot_box_entry.grid(column=2, row=2)

ttk.Label(mainframe, text='Enter credit card number').grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text='Total money').grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, textvariable=total_money).grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text='Total kidneys').grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, textvariable=total_kidneys).grid(column=1, row=7, sticky=E)
ttk.Label(mainframe, text='github.com/khoangotran').grid(column=2, row=10)

ttk.Button(mainframe, text='Buy loot box (-$10)', command=number_to_rpg_string).grid(column=2, row=5)
ttk.Button(mainframe, text='Sell kidney (+$20)', command=sell_kidneys).grid(column=2, row=7)
ttk.Button(mainframe, text='Random card', command=random_card).grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=final_item).grid(column=2, row=8, sticky=(W, E))
ttk.Label(mainframe, textvariable=card_ending).grid(column=2, row=9, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

loot_box_entry.focus()
root.bind('<Return>', number_to_rpg_string)

root.mainloop()

# REFERENCES
# Mostly documents on how to append text from .txt to lists and GUI stuff.
# Item prefixes come from World of Warcraft, and suffixes come from Path of Exile.
# ----------------------------------------------------------
#https://pathofexile.gamepedia.com/Rare_Item_Name_Index
#https://www.w3schools.com/python/python_dictionaries.asp
#https://stackoverflow.com/questions/34966059/how-to-append-from-file-into-list-in-python
#https://automatetheboringstuff.com/chapter8/
#https://stackoverflow.com/questions/3232953/python-removing-spaces-from-list-objects
#https://www.wowhead.com/weapons
#https://stackoverflow.com/questions/3142054/python-add-items-from-txt-file-into-a-list
#https://tkdocs.com/tutorial/firstexample.html
#https://stackoverflow.com/questions/19719577/add-tkinters-intvar-to-an-integer
#https://stackoverflow.com/questions/14786507/how-to-change-the-color-of-certain-words-in-the-tkinter-text-widget

# REMARKS:  At first I wanted to just make an RPG item name generator.
#           When it comes to naming the buttons I suddenly thought about loot boxes
#           so I decided to add the money system and made it so buying loot box costs
#           money, but you can sell the item within the box to gain money back.
#           I then added the sell_kidneys function as a way to gain money to debug.
#           Lastly I added the random_card function for quicker debug.


