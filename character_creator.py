"""
Johnson Tran
Module 08 Lab
Part B

This is an old python project that is a basic character creator for Dungeons and
Dragons.
"""

def class_description(class_num):
    if class_num == 1:
        print("The Fighter class is a seasoned warrior in the fantasy realm, mastering a variety of weapons and combat techniques. Renowned for their physical prowess and resilience, Fighters excel in close-quarters combat, delivering powerful blows and providing crucial protection for their comrades.")
    elif class_num == 2:
        print("The Hunter class is a skilled and adaptable adventurer in a fantasy role-playing world, specializing in precision and survival. Masters of ranged combat and tracking, Hunters are known for their keen senses, deadly accuracy, and ability to navigate diverse environments with finesse.")
    elif class_num == 3:
        print("The Wizard class is a arcane practitioner in a mystical realm, wielding potent spells and ancient knowledge to shape reality. Masters of the arcane arts, wizards command powerful forces, casting spells that range from unleashing destructive elemental energies to manipulating the fabric of time itself.")
    elif class_num == 4:
        print("The Warlock class is a wielder of eldritch powers in a magical world, forging pacts with otherworldly entities for unique and dark abilities. Drawing upon their mystical connections, warlocks cast spells that blend arcane and otherworldly energies, often harnessing the forces of patrons from realms beyond for both power and peril.")
    elif class_num == 5:
        print("In a mystical realm, the Druid class embodies the primal forces of nature, possessing a deep connection to the wilderness. These adept shape-shifters and guardians channel the power of flora and fauna, utilizing spells and transformations to heal, protect, and unleash the untamed essence of the natural world.")
    elif class_num == 6:
        print("The Rogue class is a cunning and stealthy adventurer in a fantasy world, specializing in subterfuge, agility, and precise strikes. Masters of evasion and infiltration, rogues navigate the shadows with finesse, utilizing a range of skills from lockpicking to surprise attacks to outmaneuver adversaries and secure valuable treasures.")
    elif class_num == 7:
        print("The Bard class is a charismatic and versatile performer, weaving magic through music, storytelling, and charm. These skilled artists not only entertain but also wield a unique blend of spells and inspiration, influencing allies and manipulating the ebb and flow of battles with their enchanting abilities.")

class_number = {
    'fighter': 1,
    'hunter': 2,
    'wizard': 3,
    'warlock': 4,
    'druid': 5,
    'rogue': 6,
    'bard': 7
}

class_equipment = {
    'fighter': ['Longsword', 'Wooden Shield', 'Chain Mail', 'Rope'],
    'hunter': ['Long Bow', 'Shortsword', 'Leather Armor', 'Animal Traps'],
    'wizard': ['Magic Staff', 'Wooden Shield', 'Robe', 'Potion'],
    'warlock': ['Rapier', 'Dagger', 'Light Chain Mail', 'Potion'],
    'druid': ['Magic Staff', 'Shortsword', 'Robe', 'Animal Charm'],
    'rogue': ['Dagger', 'Short Bow', 'Leather Armor', 'Master Key'],
    'bard': ['Shortsword', 'Wooden Shield', 'Light Chain Mail', 'Lute']
}


character_name = input("Enter in the name of your character: ")
character_class = input("Choose your class (Fighter, Hunter, Wizard, Warlock, Druid, Rogue, Bard): ").lower()
class_confirm = 'no'
while class_confirm == 'no':
    try:
        character_class = input("Choose your class (Fighter, Hunter, Wizard, Warlock, Druid, Rogue, Bard):  ").lower()
        if character_class in class_number:
            class_num = class_number[character_class]
            print(f'You have chosen the {character_class.capitalize()} class.')
            class_description(class_num)
            class_confirm = input(f'Do you wish to continue as a {character_class.capitalize()}? (Yes or No) ').lower()
            if class_confirm not in ['yes', 'no']:
                raise ValueError("Enter either 'Yes' or 'No'.")
            else:
                chosen_class = character_class
        else:
            raise ValueError("Invalid class. Please choose a valid class.")
    except ValueError as e:
        print(f"Error: {e}")

character_origin = input('Where is your character from? ')
character_race = input('What race is your character? ')
character_height = input('How tall is your character? ')
character_age = input('How old is your character? ')

print(character_name.capitalize())
print(f'Class: {chosen_class.capitalize()}')
print(f'Place of Origin: {character_origin.capitalize()}')
print(f'Age: {character_age}')
print(f'Equipment: {class_equipment[chosen_class.lower()]}')