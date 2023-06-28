import discord
from discord.ext import commands
from discord import Option


# Discord-Bot-Token einfügen
TOKEN = 'My Token'

# Präfix für Befehle festlegen
prefix = '!'

# Intents konfigurieren
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# Einrichten des Bot-Clients
bot = commands.Bot(command_prefix=prefix, intents=intents, debug_guilds=[1030650671600504894])






#! ========== Spell List Start
#? Warlock-Spell-Liste
warlock_spells_data = {
    "Cantrip": [
        "Blade Ward",
        "Chill Touch",
        "Eldritch Blast",
        "Fwends",
        "Mage Hand",
        "Minor Illusion",
        "Poison Spray",
        "Presitigitaion",
        "True Strike",
    ],
    "Level 1": [
        "Armor of Agathys",
        "Arms of hadar",
        "Charm Person",
        "Comprehend Languages",
        "Expeditious Retreat",
        "Hellish Rebuke",
        "Hex",
        "Illusory Script",
        "Protection from Evil and Good",
        "Unseen Servant",
        "Witch Bolt",
        # Weitere Level-1-Spells hier hinzufügen
    ],
    "Level 2": [
        "Cloud of Daggers",
        "Crown of Madness",
        "Enthrall",
        "Hold Person",
        "Invisibility",
        "Mirror Image",
        "Mistey Step",
        "Ray of Enfeeblement",
        "Shatter",
        "Spider Climb",
        "Suggestion",
        # Weitere Level-2-Spells hier hinzufügen
    ],
    "Level 3": [
        "Counterspell",
        "Dispell Magic",
        "Fear",
        "Fly",
        "Gaseous Form",
        "Hunger of Hadar",
        "Hypnotic Pattern",
        "Magic Circle",
        "Major Image",
        "Remove Curse",
        "Tongues",
        "Vampiric  Touch",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 4": [
        "Banishment",
        "Blight",
        "Dimension Door",
        "Halucinatory Terrain",        
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 5": [
        "Contact other Plane",
        "Dream",
        "Hold Monster",
        "Scying",     
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 6": [
        "Arcane Gate",
        "Circle of Death",
        "Conjure Fey",
        "Create Unded",
        "Eyebite",
        "Flesh to Stone",
        "Mass Suggestion",
        "True Seeing",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 7": [
        "Etherealness",
        "Finger of Death",
        "Forcecage",
        "Plane Shift",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 8": [
        "Demiplane",
        "Dominate Monster",
        "Feeblemind",
        "Glibness",
        "Power Word Stun",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 9": [
        "Astral Projection",
        "Foresight",
        "Imprisonment",
        "Power Word Kill",
        "True Polymorph",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    
}

#? barde-Spell-Liste
bard_spells_data = {
    "Cantrip": [
        "Blade Ward",
        "Dancing Lights",
        "Fwends",
        "Light",
        "Mage Hand",
        "Mending",
        "Message",
        "Minor Illusion",
        "Presitigitaion",
        "True Strike",
        "Vicious Mockery",
    ],
    "Level 1": [
        "Animal Fwendship",
        "Bane",
        "Charm Person",
        "Comprehend Languages",
        "Cure Wounds",
        "Detect Magic",
        "Disguise Self",
        "Dissonant Whispers",
        "Faerie Fire",
        "Feather Fall",
        "Healing Word",
        "Heroääsim",
        "Identify",
        "Illusory Script",
        "Longstrider",
        "Silent Image",
        "Sleep",
        "Speak with Animals",
        "Tasha's Hideous Laughter",
        "Thunderwave",
        "Unseen Servant",
        # Weitere Level-1-Spells hier hinzufügen
    ],
    "Level 2": [
        "Animal Messenger",
        "Blindness / Deafness",
        "Calm Emotions"
        "Cloud of Daggers",
        "Crown of Madness",
        "Detect Thoughts",
        "Enhance Ability",
        "Enthrall",
        "Heat Metal",
        "Hold Person",
        "Invisibility",
        "Knock",
        "Lesser Restoration",
        "Locate Animal or Plants",
        "Locate Objects",
        "Magic Mouth",
        "Phantasmal Force",
        "See Invisibility",
        "Shatter",
        "Silence",
        "Suggestion",
        "Zone of Truth",
        # Weitere Level-2-Spells hier hinzufügen
    ],
    "Level 3": [
        "Bestow Curse",
        "Clairvoyance",
        "Dispell Magic",
        "Fear",
        "Feign Death",
        "Glyh of Warding",
        "Hypnotic Pattern",
        "Leomund's Tiny Hut",
        "Major Image",
        "Nondetection",
        "Plant Growth",
        "Sending",
        "Speak with Dead",
        "Speak with Plants",
        "Stinking Cloud",
        "Tongues",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 4": [
        "Complusion",
        "Confusion",
        "Dimenson Door",
        "Freedom of Movement",
        "Greater Invisibility",
        "Halucinatory Terrain",
        "Locate Creature",
        "Polymorph",        
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 5": [
        "Animate Objects",
        "Awaken",
        "Dominate Person",
        "Dream",
        "Geas",
        "Greater Restoration",
        "Hold Monster",
        "Legends Move",
        "Mass Cure Wounds",
        "Mislead",
        "Modify Memory",
        "Planar Binding",
        "Raise Dead",
        "Scying",    
        "Seeming",
        "Teleportation Circle", 
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 6": [
        "Eyebite",
        "Find the Path",
        "Guard and Wards",
        "Mass Suggestion",
        "Otto's Irresitible Dance",
        "Programmed Illusion",
        "True Seeing",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 7": [
        "Etherealness",
        "Forcecage",
        "Mirage Arcane",
        "Mordenkainen's Magnificent Mansion",
        "Mordenkaisen's Sword",
        "Project Image",
        "Regenerate",
        "Resurrection",
        "Symbol",
        "Teleport",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 8": [
        "Dominate Monster",
        "Feeblemind",
        "Glibness",
        "Mind Blank",
        "Power Word Stun",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 9": [
        "Foresight",
        "Power Word Heal",
        "Power Word Kill",
        "True Polymorph",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    
}

#? Warlock-Spell-Liste
wizzard_spells_data = {
    "Cantrip": [
        "Acid Splash",
        "Blade Ward",
        "Chill Touch",
        "Dancing Lights",
        "Fire bolt",
        "Fwends",
        "Light",
        "Mage Hand",
        "Mending",
        "Message",
        "Minor Illusion",
        "Presitigitaion",
        "Ray of Frost",
        "Shocking Grasp",
        "True Strike",
    ],
    "Level 1": [
        "Alarm",
        "Burning Hands",
        "Charm Person",
        "Chromatic Orb",
        "Color Spray",
        "Comprehend Languages",
        "Detect Magic",
        "Disguise Self",
        "Expeditious Retreat",
        "False Life",
        "Feather Fall",
        "Find Familiar",
        "Fog Cloud",
        "Grease",
        "Identify",
        "Illusory Script",
        "Jump",
        "Longstrider",
        "Mage Armor",
        "Magic Missile",
        "Portection from Evil and Good",
        "Ray of Sickness",
        "Shield",
        "Silent Image",
        "Sleep",
        "Tasha's Hideous Laughter",
        "Tenser's Floating Disk",
        "Thunderwave",
        "Unseen Servant",
        "Witch Bolt",
        # Weitere Level-1-Spells hier hinzufügen
    ],
    "Level 2": [
        "Alter Self",
        "Arcane Lock",
        "Blindness / Deafness",
        "Blur",
        "Cloud of Daggers",
        "Continual Flame",
        "Crown of Madness",
        "Darkness",
        "Darkvision",
        "Detect Thoughts",
        "Enlarge / Reduce",
        "Flaming Sphere",
        "Gentle Response",
        "Gust of Wind",
        "Hold Person",
        "Invisibility",
        "Knock",
        "Locate Objects",
        "Magic Mouth",
        "Magic Weapon",
        "Melf's Acid Arrow",
        "Mirror Image",
        "Misty Step",
        "Nystul's Magic Aura",
        "Phantasmal Force",
        "Ray of Enfeeblement",
        "Rope Trick",
        "Scorching Ray",
        "See Invisibility",
        "Shatter",
        "Spider Climb",
        "Suggestion",
        "Web",
        # Weitere Level-2-Spells hier hinzufügen
    ],
    "Level 3": [
        "Animate Dead",
        "Bestow Curse",
        "Blink",
        "Clairvoyance",
        "Counterspell",
        "Dispell Magic",
        "Fear",
        "Feign Death",
        "Fire Ball",
        "Fly",
        "Gaseous Form",
        "Glyh of Warding",
        "Haste",
        "Hypnotic Pattern",
        "Leomund's Tiny Hut",
        "Magic Circle",
        "Major Image",
        "Nondetection",
        "Phantom Steed",
        "Protection from Energy",
        "Remove Curse",
        "Sending",
        "Sleet Storm",
        "Slow",
        "Stinking Cloud",
        "Tongues",
        "Vampiric Touch",
        "Water Breathing",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 4": [
        "Arcane Eye",
        "Banishment",
        "Blight",
        "Confusio n",
        "Conjure Minor Elementals",
        "Control Water",
        "Control Water",
        "Dimenson Door",
        "Evard's Black Tentacles",
        "Fabricate",
        "Fire Shield",
        "Greater Invisibility",
        "Hallucinatory Terrain",
        "Ice Storm",
        "Leomund's Secret Chest",
        "Locate Creature",
        "Mordenkaisen's Faithful Hound",
        "Mordenkaisen's Private Sanctum",
        "Otiluke's Resilient Sphere",
        "Phantasmal Killer",
        "Polymorph",
        "Stone Shape",
        "Stone Skin",    
        "Wall of Fire",       
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 5": [
        "Arcane Objects",
        "Bigby's Hand",
        "Cloud Kill",
        "Cone of Cold",
        "Conjure Elemental",
        "Contact Other Plane",
        "Creation",
        "Dominate Person",
        "Dream",
        "Geas",
        "Hold Monster",
        "Legends Lore",
        "Mislead",
        "Modify Memory",
        "Passwall",
        "Planar Binding",
        "Rary's Telepathic Bond",
        "Scrying",
        "Seeming",
        "Telekinesis",
        "Teleportation Circle",
        "Wall of Force",
        "Wall of Stone",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 6": [
        "Arcance Gate",
        "Chain Lightning",
        "Circle of Death",
        "Contingency",
        "Create Undead",
        "Disintegrate",
        "Drawmij's Instant Summons",
        "Eyebite",
        "Flesh to Stone",
        "Globe of Invulnearbility",
        "Guard and Wards",
        "Magic jar",
        "Mass Suggestion",
        "Move Earth",
        "Otiluke’s Freezing Sphere",
        "Otto's Irresitible Dance",
        "Programmed Illusion",
        "Sunbeam",
        "True Seeing",
        "Wall of Ice",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 7": [
        "Deleayed Blast Fireball",
        "Etherealness",
        "Finger of Death",
        "Forcecage",
        "Mirage Arcane",
        "Mordenkainen's Magnificent Mansion",
        "Mordenkaisen's Sword",
        "Plane Shift",
        "Project Image",
        "Reverse Gravity",
        "Sequester",
        "Simulacrum",
        "Symbol",
        "Teleport",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 8": [
        "Antimagic Field",
        "Antipathy / Sympathy",
        "Clone",
        "Control Weather",
        "Demiplane",
        "Dominate Monster",
        "Feeblemind",
        "Incendiary Cloud",
        "Maze",
        "Mind Blank",
        "Power Word Stun",
        "Sunburst",
        "Telepathy",
        "Trap the Soul",
        # Weitere Level-3-Spells hier hinzufügen
    ],
    "Level 9": [
        "Astral Projection",
        "Foresight",
        "Gate",
        "Imprisonment",
        "Meteor Swarm",
        "Power Word Kill",
        "Prismatic Wall",
        "Shapechange",
        "Time Stop",
        "True Polymorph",
        "Weird",
        "Wish",
        # Weitere Level-3-Spells hier hinzufügen
    ],
}


#& Befehl, um alle Warlock-Spells abzurufen
@bot.command()
async def warlock_spells(ctx):
    # Erstellen des Embeds
    embed = discord.Embed(title="Warlock Spell-Liste", color=discord.Color.red())
    
    for level, spells in warlock_spells_data.items():
        spell_list = '\n'.join(spells)
        embed.add_field(name=level, value=spell_list, inline=False)
    
    # Nachricht mit Embed senden
    await ctx.send(embed=embed)


#& Befehl, um alle Wizzard-Spells abzurufen
@bot.command()
async def wizzard_spells(ctx):
    # Erstellen des Embeds
    embed = discord.Embed(title="Wizzard Spell-Liste", color=discord.Color.purple())
    
    for level, spells in wizzard_spells_data.items():
        spell_list = '\n'.join(spells)
        embed.add_field(name=level, value=spell_list, inline=False)
    
    # Nachricht mit Embed senden
    await ctx.send(embed=embed)


#& Befehl, um alle Barde-Spells abzurufen
@bot.command()
async def bard_spells(ctx):
    # Erstellen des Embeds
    embed = discord.Embed(title="Bard Spell-Liste", color=discord.Color.green())
    
    for level, spells in bard_spells_data.items():
        spell_list = '\n'.join(spells)
        embed.add_field(name=level, value=spell_list, inline=False)
    
    # Nachricht mit Embed senden
    await ctx.send(embed=embed)

#! ========== Spell List End

#New Commands






# Event beim Start des Bots
@bot.event
async def on_ready():
    print(f'Bot ist bereit: {bot.user.name} - {bot.user.id}')

# Bot-Client starten
bot.run(TOKEN)
