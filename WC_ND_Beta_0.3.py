
# Setup One: Imports

import pickle
import pathlib
import random
import time
import os
import sys

# Setup Two: Default Lists

codebits = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "`", "-", "=", "[", "]", ",", ".", "/", "~", "!", "@", "#", "$", "%"]

locations = [
  "in a forest", "on a grassland", "on a moor", "on a wetland", "in a desert", "by a river", "by a small stream", "by a lake", "by a small pond", "in a marsh", "in a bog", "in a Twolegplace", "atop a mountain", "in a gorge", "atop a canyon", "in a tundra", "within a rainforest", "in a chaparral", "in a taiga", "on a savannah"]

predators = [
  "foxes", "falcons", "buzzards", "alligators", "coyotes", "otters", "wolves", "bears", "snakes", "geese", "beavers", "dogs", "rams", "raccoons", "cougars", "snow leopards", "jaguars", "bobcats", "weasels", "leopards"]

prefixes = [
  "Acorn", "Air", "Amber", "Ant", "Apple", "Arch",
  "Badger", "Beetle", "Berry", "Bird", "Black", "Blue", "Brindle", "Brown", "Buzzard",
  "Cherry", "Claw", "Coal", "Copper", "Crow", "Cypress",
  "Dapple", "Dark", "Dauber", "Deer", "Dove", "Duck",
  "Eagle", "Ebony", "Echo", "Eclipse", "Edge", "Egret", 
  "Fawn", "Feather", "Ferret", "Finch", "Fly", "Fox",
  "Goat", "Golden", "Goose", "Grape", "Grey", "Green",
  "Hare", "Hawk", "Heron", "Honey", "Holly", "Horse",
  "Ibex", "Ibis", "Ice", "Icy", "Indigo", "Inferno",
  "Jackal", "Jade", "Jay", "Jitter", "Jumping", "Jute",
  "Keen", "Kestrel", "Kindle", "Kink", "Kite", "Kudu",
  "Lake", "Lark", "Leopard", "Light", "Lily", "Lion", 
  "Maggot", "Meadow", "Mole", "Moth", "Mottle", "Mouse",
  "Nettle", "Newt", "Night", "Noble", "Noodle", "Nut",
  "Oak", "Olive", "One", "Orange", "Otter", "Owl",
  "Pale", "Patch", "Pear", "Perch", "Plum", "Pod",
  "Quail", "Quartz", "Quick", "Quill", "Quiver", "Quokka",
  "Rabbit", "Rat", "Raven", "Red", "Robin", "Russet", 
  "Seed", "Sheep", "Shrew", "Silver", "Sparrow", "Speckle", "Spider", "Splash", "Spotted", "Squirrel", "Starling", "Stoat", "Swallow", "Swift",
  "Tawny", "Terror", "Thrush", "Tiger", "Toad", "Trout",
  "Ugly", "Umber",
  "Valley", "Velvet", "Verdant", "Vine", "Vixen", "Vole",
  "Wasp", "Weasel", "White", "Wild", "Willow", "Wolf",
  "Yarrow", "Yawn", "Yellow", "Yerba", "Yonder", "Yucca"
  ]

suffixes = [
  "bee", "belly", "berry", "bird", "blaze", "branch", "breeze", "briar", "bright", "burr", 
  "claw", "cloud",
  "dapple", "drop", "dust",
  "eye", "eyes",
  "face", "fall", "fang", "feather", "fern", "fire", "flake", "flame", "flight", "flower", "foot", "frost", "fur",
  "hawk", "heart",
  "jaw", "jump",
  "leaf", "leap", "leg", "light",
  "mask", "mist",
  "nose",
  "pad", "pelt", "pool", "puddle", 
  "scar", "sight", "shade", "shine", "skip", "sky", "snow", "song", "speck", "spirit", "splash", "spot", "spots", "spring", "stem", "step", "storm", "stream", "strike", "stripe",
  "tail", "talon", "throat", "tooth", "tuft",
  "watcher", "whisper", "whisker", "willow", "wing"
  ]

pronouns = [
  "tom", "she-cat", "cat", "she-cat", "tom"
]

warrior_code = []

proph_beginnings = [
  "fire alone ", "an untrustworthy warrior ", "StarClan ",
  "a sleeping enemy ", "blood ", "a lion "
]

proph_middles = [
  "will save ", "will betray ", "will call upon ",
  "will come to destroy ", "will rule ", "will wage war against "
]

proph_ends = [
  "our Clan", "you", "your trust",
  "your fear", "the forest", "the sky"
]

possible_code = [
  "Your loyalty must remain to your Clan",
  "Do not hunt or trespass on another Clan's territory",
  "Elders, queens, and kits must be fed before apprentices and warriors",
  "Prey is killed only to be eaten",
  "A kit must be at least six moons old to become an apprentice",
  "All cats must be subscribed to r/warriorcats_anewdawn",
  "A worthy warrior must be of pure blood",
  "A worthy warrior believes in StarClan",
  "The deputy must be related to the leader by blood",
  "A worthy warrior consumes the lifeblood of kits for the glory of their Clan",
  "Newly appointed warriors will keep a silent vigil",
  "Newly appointed warriors must fight to the death",
  "A cat cannot be made deputy without having mentored at least one apprentice",
  "A cat cannot be made deputy without eating at least one apprentice",
  "The deputy will become Clan leader when the leader dies, retires, or is exiled",
  "The deputy will become Clan leader only after StarClan's explicit approval",
  "New deputies must be chosen before moonhigh",
  "New deputies must be chosen immediately",
  "Clan borders must be checked and marked daily",
  "Clan borders must stay open to outsiders",
]

anythingcanhappen = [
 "bonus prey",
 "foxes",
 "kits",
 "clan_interaction",
 "greencough",
 "deforestation",
 "reputation"
 "kits",
 "mercenary",
 "traitor",
 "code_amendment",
 "kits",
 "code_break",
 "prophecy",
 "reputation"
]

body_build = [
  "very thin",
  "thin",
  "muscular",
  "very muscular",
  "plump",
  "very plump",
  "fluffy",
  "hairless",
  "lithe",
  "stocky",
  "broad-shouldered"
]

body_size = [
  "very small",
  "small",
  "large",
  "very large",
  "tall",
  "very tall",
  "huge",
  "tiny",
  "short",
  "beastly"
]

coats = [
  "black",
  "black-and-white",
  "black-and-brown",
  "white",
  "white-with-black-spots",
  "white-with-black-stripes",
  "light brown",
  "light-brown-and-white",
  "light-brown-and-black",
  "light brown spotted",
  "light brown tabby",
  "dark brown",
  "dark-brown-and-white",
  "dark-brown-and-black",
  "dark brown spotted",
  "dark brown tabby",
  "light grey",
  "light-grey-and-white",
  "light-grey-and-black",
  "light grey spotted",
  "light grey tabby",
  "dark grey",
  "dark-grey-and-white",
  "dark-grey-and-black",
  "dark grey spotted",
  "dark grey tabby",
  "ginger",
  "ginger-and-white",
  "tortoiseshell",
  "ginger spotted",
  "ginger tabby",
  "pale ginger",
  "pale-ginger-and-white",
  "pale tortoiseshell",
  "pale ginger spotted",
  "pale ginger tabby",
  "pinkish-grey",
  "dark tortoiseshell",
  "flame-coloured"
]

beta_help = []

time_span = "quarter_moon"

personality_traits = ["impulsive", "caring", "hardworking", "silly", "sharp", "durable", "observant", "intelligent", "loving", "nervous", "loyal", "kind", "proud", "determined", "wise", "calm", "cold", "spiritual", "thoughtful", "peaceful", "feisty", "passionate", "scrappy", "expressive", "resolute", "careful", "devoted", "moral"]

enemy_quotes = ["%s is sooooo boring. Never gets anything done.", "I honestly just wish %s would at least pretend to care about their Clanmates.", "What do I think of %s? Well, in a word, lazy.", "%s doesn't know how to have fun! They're always super serious and it's boring.", "A good leader has a sharp wit. %s is as dull as a rock.", "If I touched %s, do you think they would just crumble to dust? Considering how weak-willed they are, it may be a possibility.", "Anyone else notice how useless %s has been lately? How every word they say feels like a hollow promise?", "Why do I hate %s? I am very smart, and they are very not. Simple as that.", "Love is important to a well-rounded cat, and it seems %s is devoid of it.", "I-I feel like %s is p-planning something, but I don't know what. They keep giving me this l-look...", "You know I'm loyal to our Clan, but that does not mean I'm loyal to %s.", "I don't hate %s, that's silly. But I see them as a threat to the moral character of our Clan.", "It should be me who's leader of the Clan, not %s. They are weak and irresponsible.", "%s has proven many times over they are unfit to rule. And even if it takes moons, even if it ends with my death... I will make that truth known.", "%s may be powerful, but they are a powerful fool. When faced with a challenge requiring wit they will crumble like dry sand.", "Do you think, if %s were gone, we would be happier? I think so.", "What a bleeding heart, that %s. More in common with a kittypet than a warrior.", "StarClan disapproves of %s, I just know it! They are watching us with disappointment.", "%s seems to only consider themselves when making a decision that affects all of us. It's getting really annoying.", "%s is always thrusting us into war. I don't know how many more useless battles I can take.", "I think we need a leader with sass. And I am the embodiment of sass, ergo, I should kill %s and become leader, right? Just kidding!", "I will have you know I am passionate about this Clan- I feel like %s just sees it as a hobby they can drop at any time.", "This may seem odd, but I tend to think of myself as an underdog, right? And %s is like, the popular kid, who always gets what they want. And that's not fair, right?", "Whenever I try to make conversation with %s, it feels like I'm talking to a wall. Just an expressionless block of wood. That's why I'm not friends with them.", "At least I know what I want! At least I can take criticism! %s acts like a spoiled kit who can't see past their own muzzle.", "I'm just saying, we should be wary of %s. Do any of us know their true intentions?", "As a cat whose whole life revolves around my Clan and my Clanmates, I feel unsafe with %s as leader.", "%s is a crook. They are an immoral liar, and it's about time we had a cat who respected traditional values leading our Clan."]

quotes = ["Kill first, ask questions later.", "I treat my Clanmates not just as comrades, but as family.", "A day spent idle is a day wasted.", "Sometimes I wish my Clanmates would laugh a little more.", "To be a Clan cat, more than anything, you must have your wits about you at all times.", "Persevereance- the ability to overcome any and all obstacles- will serve you much better than foolish courage ever will.", "Just because I notice things other cats don't, does that make me special?", "You may have the sharper claws, my friend, but in a battle of mind I would surely come out on top.", "Where would the Clans be without unity? Without comaraderie? Without love?", "Am I the only one who constantly feels as if they are being watched?", "When I joined the Clans, I joined knowing I would one day die for my Clan. And I am perfectly content with that.", "Kindness is a preferable battle tactic to violence. Ever heard of 'kill 'em with kindness'?", "Pride is the ultimate virtue, for it is pride in me, my Clan, and the Warrior Code that drives me to bring good to the world.", "When I set my mind to something, I'm not letting it go. That's just how I am.", "I would rather be a weakling with wits than a powerful fool.", "Patience will get you much farther than a quick wit.", "What's the point in feeling at all? Just to end up getting hurt?", "StarClan works in mysterious ways.", "I think thoughtfulness is a skill, like hunting or fighting. You need to hone it.", "If you ask me, the Clans fight far too often. We all share the same culture and all worship StarClan- what's the point in throwing spittle over nothing?", "Not even the leader can stop me from getting my way!", "'Caring too much' isn't a fault, not really. If you ask me, cats nowadays care too little.", "Whatever comes my way, rest assured I will survive.", "When I'm happy, I laugh. When I'm sad, I weep. It's disingenuous to hide your feelings.", "Call me stubborn, but being firm in your beliefs is not a flaw. To be sure of yourself is a grand thing to be.", "It's important to put care into every pawstep you take. You never know when you may trip and fall.", "I have zero sympathy for the unfaithful. When I grab ahold of something, I remain devoted to it, simple as that.", "My paws are guided not by law, but by virtue, as all cats' paws should be."]

moon_suffixes = [
  "pool", "stone", "tree", "glow", "cliff", "flower", "beast", "feather", "field", "cave", "watcher"
]

communer = ""

player_Clan = ""

clan_1 = ""
clan_2 = ""
clan_3 = ""
clan_4 = ""
clan_5 = ""
clan_6 = ""
clan_7 = ""
clan_8 = ""
clan_9 = ""

possible_clans = [
  clan_1,
  clan_2,
  clan_3,
  clan_4,
  clan_5,
  clan_6,
  clan_7,
  clan_8,
  clan_9
]

ranks = [
  "warrior",
  "warrior",
  "warrior",
  "warrior",
  "warrior",
  "warrior",
  "apprentice",
  "apprentice",
  "medicine apprentice",
  "elder",
  "kit"
]

# Setup Three: New Player Variables

# Setup Four: Classes

class cat(object):
 def __init__(self, name, prefix, suffix, pronoun, coat, rank, hunting_skill, power, build, size, feeding, mate, mentor, age, Aparent, Bparent, isqueen, per1, per2, quote, rep):
    self.name = name
    self.prefix = prefix
    self.suffix = suffix
    self.pronoun = pronoun
    self.coat = coat
    self.rank = rank
    self.hunting_skill = hunting_skill
    self.power = power
    self.build = build
    self.size = size
    self.feeding = feeding
    self.mate = mate
    self.mentor = mentor
    self.age = age
    self.Aparent = Aparent
    self.Bparent = Bparent
    self.isqueen = isqueen
    self.per1 = per1
    self.per2 = per2
    self.quote = quote
    self.rep = rep

class all_Clans(object):
  def __init__(self, Cname, Clocation, Cprey, Cland, Cpower, Cpredator, Crep, cats):
    self.Cname = Cname
    self.Clocation = Clocation
    self.Cprey = Cprey
    self.Cland = Cland
    self.Cpower = Cpower
    self.Cpredator = Cpredator
    self.Crep = Crep
    self.cats = cats
  clans = []

# Setup Five: Functions

def maintenance():
  print("Hey, Zaru here! The game is currently down for maintenace, so come back later.")
  progress = True
  while progress == True:
    time.sleep(1)

def death(player_Clan, lives, dead_guy):
  player_Clan.Cpower -= player_Clan.cats[dead_guy].power
  print("Unfortunately, %s has died. They will be missed." % player_Clan.cats[dead_guy].name)
  if player_Clan.cats[dead_guy].rank == "leader" and lives > 1:
    lives -= 1
    print("%s has lost a life! They have %d lives left." % (player_Clan.cats[dead_guy].name, lives))
  elif player_Clan.cats[dead_guy].rank == "leader" and lives == 1:
    for i in player_Clan.cats:
      if player_Clan.cats[i].mentor == player_Clan.cats[dead_guy]:
        player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
        while player_Clan.cats[player_Clan.cats[i].mentor].rank == "elder" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice":
          player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
    print("But this does not mean the game is over yet! You will live on in the next leader...")
    print("The new leader is %s, now %s." % (player_Clan.cats["deputy"].name, player_Clan.cats["deputy"].prefix + "star"))
    player_Clan.cats["leader"].name = player_Clan.cats["deputy"].name
    player_Clan.cats["leader"].prefix = player_Clan.cats["deputy"].prefix
    player_Clan.cats["leader"].suffix = player_Clan.cats["deputy"].suffix
    player_Clan.cats["leader"].pronoun = player_Clan.cats["deputy"].pronoun
    player_Clan.cats["leader"].coat = player_Clan.cats["deputy"].coat
    player_Clan.cats["leader"].power = player_Clan.cats["deputy"].power
    player_Clan.cats["leader"].build = player_Clan.cats["deputy"].build
    player_Clan.cats["leader"].size = player_Clan.cats["deputy"].size
    player_Clan.cats["leader"].feeding = player_Clan.cats["deputy"].feeding
    player_Clan.cats["leader"].age = player_Clan.cats["deputy"].age
    player_Clan.cats["leader"].Aparent = player_Clan.cats["deputy"].Aparent
    player_Clan.cats["leader"].Bparent = player_Clan.cats["deputy"].Bparent
    player_Clan.cats["leader"].mate = player_Clan.cats["deputy"].mate
    player_Clan.cats["leader"].per1 = player_Clan.cats["deputy"].per1
    player_Clan.cats["leader"].per2 = player_Clan.cats["deputy"].per2
    player_Clan.cats["leader"].quote = player_Clan.cats["deputy"].quote
    player_Clan.cats["leader"].rep = player_Clan.cats["deputy"].rep
    lives = 9
    player_Clan.cats["deputy"].name = player_Clan.cats[new_deputy].name
    player_Clan.cats["deputy"].prefix = player_Clan.cats[new_deputy].prefix
    player_Clan.cats["deputy"].suffix = player_Clan.cats[new_deputy].suffix
    player_Clan.cats["deputy"].pronoun = player_Clan.cats[new_deputy].pronoun
    player_Clan.cats["deputy"].coat = player_Clan.cats[new_deputy].coat
    player_Clan.cats["deputy"].power = player_Clan.cats[new_deputy].power
    player_Clan.cats["deputy"].build = player_Clan.cats[new_deputy].build
    player_Clan.cats["deputy"].size = player_Clan.cats[new_deputy].size
    player_Clan.cats["deputy"].feeding = player_Clan.cats[new_deputy].feeding
    player_Clan.cats["deputy"].rank = "deputy"
    player_Clan.cats["deputy"].age = player_Clan.cats[new_deputy].age
    player_Clan.cats["deputy"].Aparent = player_Clan.cats[new_deputy].Aparent
    player_Clan.cats["deputy"].Bparent = player_Clan.cats[new_deputy].Bparent
    player_Clan.cats["deputy"].mate = player_Clan.cats[new_deputy].mate
    player_Clan.cats["deputy"].per1 = player_Clan.cats[new_deputy].per1
    player_Clan.cats["deputy"].per2 = player_Clan.cats[new_deputy].per2
    player_Clan.cats["deputy"].quote = player_Clan.cats[new_deputy].quote
    player_Clan.cats["deputy"].rep = player_Clan.cats[new_deputy].rep
    new_deputy = (random.choice(list(player_Clan.cats.keys())))
    while not player_Clan.cats[new_deputy].rank == "warrior":
      new_deputy = (random.choice(list(player_Clan.cats.keys())))
      player_Clan.cats["deputy"].name = player_Clan.cats[new_deputy].name
      player_Clan.cats["deputy"].prefix = player_Clan.cats[new_deputy].prefix
      player_Clan.cats["deputy"].suffix = player_Clan.cats[new_deputy].suffix
      player_Clan.cats["deputy"].pronoun = player_Clan.cats[new_deputy].pronoun
      player_Clan.cats["deputy"].coat = player_Clan.cats[new_deputy].coat
      player_Clan.cats["deputy"].power = player_Clan.cats[new_deputy].power
      player_Clan.cats["deputy"].build = player_Clan.cats[new_deputy].build
      player_Clan.cats["deputy"].size = player_Clan.cats[new_deputy].size
      player_Clan.cats["deputy"].feeding = player_Clan.cats[new_deputy].feeding
      player_Clan.cats["deputy"].rank = "deputy"
      player_Clan.cats["deputy"].age = player_Clan.cats[new_deputy].age
      player_Clan.cats["deputy"].Aparent = player_Clan.cats[new_deputy].Aparent
      player_Clan.cats["deputy"].Bparent = player_Clan.cats[new_deputy].Bparent
      player_Clan.cats["deputy"].mate = player_Clan.cats[new_deputy].mate
      player_Clan.cats["deputy"].per1 = player_Clan.cats[new_deputy].per1
      player_Clan.cats["deputy"].per2 = player_Clan.cats[new_deputy].per2
      player_Clan.cats["deputy"].quote = player_Clan.cats[new_deputy].quote
      player_Clan.cats["deputy"].rep = player_Clan.cats[new_deputy].rep
    del player_Clan.cats[new_deputy]
    print("The new deputy is %s." % player_Clan.cats["deputy"].name)
  elif player_Clan.cats[dead_guy].rank == "deputy":
    for i in player_Clan.cats:
      if player_Clan.cats[i].mentor == player_Clan.cats[dead_guy]:
        player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
        while player_Clan.cats[player_Clan.cats[i].mentor].rank == "elder" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice":
          player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
    candidates = 0
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "warrior":
        candidates += 1
    if candidates >= 1:
      new_deputy = (random.choice(list(player_Clan.cats.keys())))
      while not player_Clan.cats[new_deputy].rank == "warrior":
        new_deputy = (random.choice(list(player_Clan.cats.keys())))
      player_Clan.cats["deputy"].name = player_Clan.cats[new_deputy].name
      player_Clan.cats["deputy"].prefix = player_Clan.cats[new_deputy].prefix
      player_Clan.cats["deputy"].suffix = player_Clan.cats[new_deputy].suffix
      player_Clan.cats["deputy"].pronoun = player_Clan.cats[new_deputy].pronoun
      player_Clan.cats["deputy"].coat = player_Clan.cats[new_deputy].coat
      player_Clan.cats["deputy"].power = player_Clan.cats[new_deputy].power
      player_Clan.cats["deputy"].build = player_Clan.cats[new_deputy].build
      player_Clan.cats["deputy"].size = player_Clan.cats[new_deputy].size
      player_Clan.cats["deputy"].feeding = player_Clan.cats[new_deputy].feeding
      player_Clan.cats["deputy"].rank = "deputy"
      player_Clan.cats["deputy"].age = player_Clan.cats[new_deputy].age
      player_Clan.cats["deputy"].Aparent = player_Clan.cats[new_deputy].Aparent
      player_Clan.cats["deputy"].Bparent = player_Clan.cats[new_deputy].Bparent
      player_Clan.cats["deputy"].mate = player_Clan.cats[new_deputy].mate
      player_Clan.cats["deputy"].per1 = player_Clan.cats[new_deputy].per1
      player_Clan.cats["deputy"].per2 = player_Clan.cats[new_deputy].per2
      player_Clan.cats["deputy"].quote = player_Clan.cats[new_deputy].quote
      player_Clan.cats["deputy"].rep = player_Clan.cats[new_deputy].rep
      del player_Clan.cats[new_deputy]
      print("The new deputy is %s." % player_Clan.cats["deputy"].name)
    else:
      print("There are no cats eligible for the deputy position!")
      print("As your Clan cannot function without a deputy or warriors to hunt or defend for it...")
      print("Your Clan has disbanded.")
      print("Sending you back to the main menu...")
      main_menu(time_span, player_Clan, communer, mobile_friendly)
      
  elif player_Clan.cats[dead_guy].rank == "medicine cat":
    new_med = ""
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "medicine apprentice":
          new_med = player_Clan.cats[i]
          break
    if new_med == "":
      new_med = (random.choice(list(player_Clan.cats.keys())))
      print(new_med)
      while player_Clan.cats[new_med].rank == "leader" or player_Clan.cats[new_med].rank == "deputy" or player_Clan.cats[new_med].rank == "kit" or player_Clan.cats[new_med].rank == "medicine cat":
        player_Clan.cats[new_med] = (random.choice(list(player_Clan.cats.keys())))            
    player_Clan.cats["medicine_cat"].name = player_Clan.cats[new_med].name
    player_Clan.cats["medicine_cat"].prefix = player_Clan.cats[new_med].prefix
    player_Clan.cats["medicine_cat"].suffix = player_Clan.cats[new_med].suffix
    if player_Clan.cats["medicine_cat"].suffix == "paw":
        player_Clan.cats["medicine_cat"].suffix = (random.choice(suffixes))
    player_Clan.cats["medicine_cat"].pronoun = player_Clan.cats[new_med].pronoun
    player_Clan.cats["medicine_cat"].coat = player_Clan.cats[new_med].coat
    player_Clan.cats["medicine_cat"].power = player_Clan.cats[new_med].power
    player_Clan.cats["medicine_cat"].build = player_Clan.cats[new_med].build
    player_Clan.cats["medicine_cat"].size = player_Clan.cats[new_med].size
    player_Clan.cats["medicine_cat"].feeding = player_Clan.cats[new_med].feeding
    player_Clan.cats["medicine_cat"].rank = "medicine cat"
    player_Clan.cats["medicine_cat"].age = player_Clan.cats[new_med].age
    player_Clan.cats["medicine_cat"].Aparent = player_Clan.cats[new_med].Aparent
    player_Clan.cats["medicine_cat"].Bparent = player_Clan.cats[new_med].Bparent
    player_Clan.cats["medicine_cat"].mate = player_Clan.cats[new_med].mate
    player_Clan.cats["medicine_cat"].per1 = player_Clan.cats[new_med].per1
    player_Clan.cats["medicine_cat"].per2 = player_Clan.cats[new_med].per2
    player_Clan.cats["medicine_cat"].quote = player_Clan.cats[new_med].quote
    player_Clan.cats["medicine_cat"].rep = player_Clan.cats[new_med].rep
    del player_Clan.cats[new_med]
    print("The new medicine cat is %s." % (player_Clan.cats["medicine_cat"].name))
  
  else:
    for i in player_Clan.cats:
      if player_Clan.cats[i].mentor == player_Clan.cats[dead_guy]:
        player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
        while player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice" or player_Clan.cats[player_Clan.cats[i].mentor] == player_Clan.cats[dead_guy]:
          player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
    del player_Clan.cats[dead_guy]

  return lives

def random_event(player_Clan, clan, lives, communer):
  rando = (random.choice(anythingcanhappen))
  if rando == "bonus prey":
    print("The prey was running well in %s." % clan.Cname)
    plus_prey = (random.randint(1, 25))
    print("They gained %d extra feedings." % plus_prey)
    if clan == player_Clan:
      clan.Cprey += plus_prey
    else:
      clan.Cpower += plus_prey * 0.5
  elif rando == "reputation":
    actor = (random.choice(list(player_Clan.cats.keys())))
    while actor == "leader":
      actor = (random.choice(list(player_Clan.cats.keys())))      
    if actor.rep < 10:
      print("%s has attacked the leader!" % player_Clan.cats[actor].name)
      if player_Clan.cats[actor].power > player_Clan.cats["leader"].power:
        dead_guy = "leader"
        protector = (random.choice(list(player_Clan.cats.keys())))
        if player_Clan.cats[protector].rep > 10:
          print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
          dead_guy = protector
        lives = death(player_Clan, lives, dead_guy)
      else:
        print("%s managed to survive the traitor's blow! However, they escaped with severe injuries." % player_Clan.cats["leader"].name)
        player_Clan.cats["leader"].power = player_Clan.cats["leader"].power * (random.uniform(0.25, 0.75))
      cmd = input("Do you wish to exile %s? [Y]/[N] | " % player_Clan.cats[actor].name)
      if cmd == "Y" or cmd == "y":
        print("%s has been exiled."  % player_Clan.cats[actor].name)
        if player_Clan.cats[actor].rank == "deputy":
          new_deputy = (random.choice(list(player_Clan.cats.keys())))
          while not player_Clan.cats[new_deputy].rank == "warrior":
            new_deputy = (random.choice(list(player_Clan.cats.keys())))
          player_Clan.cats["deputy"].name = player_Clan.cats[new_deputy].name
          player_Clan.cats["deputy"].prefix = player_Clan.cats[new_deputy].prefix
          player_Clan.cats["deputy"].suffix = player_Clan.cats[new_deputy].suffix
          player_Clan.cats["deputy"].pronoun = player_Clan.cats[new_deputy].pronoun
          player_Clan.cats["deputy"].coat = player_Clan.cats[new_deputy].coat
          player_Clan.cats["deputy"].power = player_Clan.cats[new_deputy].power
          player_Clan.cats["deputy"].build = player_Clan.cats[new_deputy].build
          player_Clan.cats["deputy"].size = player_Clan.cats[new_deputy].size
          player_Clan.cats["deputy"].feeding = player_Clan.cats[new_deputy].feeding
          player_Clan.cats["deputy"].rank = "deputy"
          player_Clan.cats["deputy"].age = player_Clan.cats[new_deputy].age
          player_Clan.cats["deputy"].Aparent = player_Clan.cats[new_deputy].Aparent
          player_Clan.cats["deputy"].Bparent = player_Clan.cats[new_deputy].Bparent
          player_Clan.cats["deputy"].mate = player_Clan.cats[new_deputy].mate
          player_Clan.cats["deputy"].per1 = player_Clan.cats[new_deputy].per1
          player_Clan.cats["deputy"].per2 = player_Clan.cats[new_deputy].per2
          player_Clan.cats["deputy"].quote = player_Clan.cats[new_deputy].quote
          player_Clan.cats["deputy"].rep = player_Clan.cats[new_deputy].rep
          del player_Clan.cats[new_deputy]
          print("The new deputy is %s." % player_Clan.cats["deputy"].name)
        elif player_Clan.cats[actor].rank == "medicine cat":
          new_med = ""
          for i in player_Clan.cats:
            if player_Clan.cats[i].rank == "medicine apprentice":
                new_med = player_Clan.cats[i]
                break
          if new_med == "":
            new_med = (random.choice(list(player_Clan.cats.keys())))
            while player_Clan.cats[new_med].rank == "leader" or player_Clan.cats[new_med].rank == "deputy" or player_Clan.cats[new_med].rank == "kit" or player_Clan.cats[new_med].rank == "medicine cat":
              player_Clan.cats[new_med] = (random.choice(list(player_Clan.cats.keys())))            
          player_Clan.cats["medicine_cat"].name = player_Clan.cats[new_med].name
          player_Clan.cats["medicine_cat"].prefix = player_Clan.cats[new_med].prefix
          player_Clan.cats["medicine_cat"].suffix = player_Clan.cats[new_med].suffix
          if player_Clan.cats["medicine_cat"].suffix == "paw":
              player_Clan.cats["medicine_cat"].suffix = (random.choice(suffixes))
          player_Clan.cats["medicine_cat"].pronoun = player_Clan.cats[new_med].pronoun
          player_Clan.cats["medicine_cat"].coat = player_Clan.cats[new_med].coat
          player_Clan.cats["medicine_cat"].power = player_Clan.cats[new_med].power
          player_Clan.cats["medicine_cat"].build = player_Clan.cats[new_med].build
          player_Clan.cats["medicine_cat"].size = player_Clan.cats[new_med].size
          player_Clan.cats["medicine_cat"].feeding = player_Clan.cats[new_med].feeding
          player_Clan.cats["medicine_cat"].rank = "medicine cat"
          player_Clan.cats["medicine_cat"].age = player_Clan.cats[new_med].age
          player_Clan.cats["medicine_cat"].Aparent = player_Clan.cats[new_med].Aparent
          player_Clan.cats["medicine_cat"].Bparent = player_Clan.cats[new_med].Bparent
          player_Clan.cats["medicine_cat"].mate = player_Clan.cats[new_med].mate
          player_Clan.cats["medicine_cat"].per1 = player_Clan.cats[new_med].per1
          player_Clan.cats["medicine_cat"].per2 = player_Clan.cats[new_med].per2
          player_Clan.cats["medicine_cat"].quote = player_Clan.cats[new_med].quote
          player_Clan.cats["medicine_cat"].rep = player_Clan.cats[new_med].rep
          del player_Clan.cats[new_med]
          print("The new medicine cat is %s." % (player_Clan.cats["medicine_cat"].name))
        else:
          for i in player_Clan.cats:
            if player_Clan.cats[i].mentor == player_Clan.cats[actor]:
              player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
              while player_Clan.cats[player_Clan.cats[i].mentor].rank == "elder" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice" or player_Clan.cats[player_Clan.cats[i].mentor] == player_Clan.cats[actor]:
                player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
          del player_Clan.cats[actor]
    elif actor.rep < 0:
      print("%s stole extra prey from the fresh-kill pile!" % player_Clan.cats[actor].name)
      player_Clan.Cprey -= (random.randint(5, 15))
    elif actor.rep > 0:
      rando = (random.randint(1, 2))
      if rando == 1:
        print("%s hunted some extra prey!" % player_Clan.cats[actor].name)
        player_Clan.Cprey += (random.randint(5, 15))
      else:
        print("%s offered a gift to you, boosting your confidence and therefor power!" % player_Clan.cats[actor].name)
        player_Clan.cats["leader"].power += 1
  elif rando == "foxes":
    print("It seems %s were found on %s's territory." % (clan.Cpredator, clan.Cname))
    fox_power = (random.randint(15, 60))
    if clan == player_Clan:
      patrol_1 = (random.choice(list(player_Clan.cats.keys())))
      while player_Clan.cats[patrol_1].rank == "medicine cat" or player_Clan.cats[patrol_1].rank == "medicine apprentice" or player_Clan.cats[patrol_1].rank == "elder" or player_Clan.cats[patrol_1].isqueen == True:
        patrol_1 = (random.choice(list(player_Clan.cats.keys())))
      patrol_2 = (random.choice(list(player_Clan.cats.keys())))
      while player_Clan.cats[patrol_2].rank == "medicine cat" or player_Clan.cats[patrol_2].rank == "medicine apprentice" or player_Clan.cats[patrol_2].rank == "elder" or player_Clan.cats[patrol_2].isqueen == True:
        patrol_2 = (random.choice(list(player_Clan.cats.keys())))
      if player_Clan.cats[patrol_2] == player_Clan.cats[patrol_1]:
        while player_Clan.cats[patrol_2] == player_Clan.cats[patrol_1]:
          player_Clan.cats[patrol_2] = (random.choice(list(player_Clan.cats.keys())))
        while player_Clan.cats[patrol_2].rank == player_Clan.cats[patrol_2].rank == "medicine cat" or player_Clan.cats[patrol_2].rank == "medicine apprentice" or player_Clan.cats[patrol_2].rank == "elder" or player_Clan.cats[patrol_2].isqueen == True:
          patrol_2 = (random.choice(list(player_Clan.cats.keys())))
      patrol_3 = (random.choice(list(player_Clan.cats.keys())))
      while player_Clan.cats[patrol_3].rank == "medicine cat" or player_Clan.cats[patrol_3].rank == "medicine apprentice" or player_Clan.cats[patrol_3].rank == "elder" or player_Clan.cats[patrol_3].isqueen == True:
        patrol_3 = (random.choice(list(player_Clan.cats.keys())))
      if player_Clan.cats[patrol_3] == player_Clan.cats[patrol_1] or player_Clan.cats[patrol_3] == player_Clan.cats[patrol_2]:
        while player_Clan.cats[patrol_3] == player_Clan.cats[patrol_1] or player_Clan.cats[patrol_3] == player_Clan.cats[patrol_2]:
          patrol_3 = (random.choice(list(player_Clan.cats.keys())))
        while player_Clan.cats[patrol_3].rank == "medicine cat" or player_Clan.cats[patrol_3].rank == "medicine apprentice" or player_Clan.cats[patrol_3].rank == "elder" or player_Clan.cats[patrol_3].isqueen == True:
          patrol_3 = (random.choice(list(player_Clan.cats.keys())))
      patrol_power = player_Clan.cats[patrol_1].power + player_Clan.cats[patrol_2].power + player_Clan.cats[patrol_3].power
    else:
      patrol_power = clan.Cpower * (random.uniform(0.1, 1))
    if patrol_power >= fox_power:
      print("%s managed to defeat the %s. They will make a fine feast." % (clan.Cname, clan.Cpredator))
      if clan == player_Clan:
        player_Clan.Cprey += fox_power
      else:
        clan.Cpower += fox_power * 0.5
    else:
      print("%s was not able to control the %s and they attacked the camp." % (clan.Cname, clan.Cpredator))
      if clan == player_Clan:
       rando = (random.randint(1, 3))
       for i in range(rando):
         dead_guy = (random.choice(list(player_Clan.cats.keys())))
         if dead_guy == "leader":
            protector = (random.choice(list(player_Clan.cats.keys())))
            if player_Clan.cats[protector].rep > 10:
              print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
              dead_guy = protector
            lives = death(player_Clan, lives, dead_guy)
      else:
        clan.Cpower -= fox_power * 0.5
        rando = (random.randint(1, 3))
        for i in range(rando):
          dead_guy = (random.choice(list(player_Clan.cats.keys())))
          del clan.cats[dead_guy]
  elif rando == "clan_interaction":
    target = (random.choice(all_Clans.clans))
    while target == clan or target == player_Clan:
      target = (random.choice(all_Clans.clans))
    rando = (random.randint(1, 2))
    if (target.Crep <= 0 and clan == player_Clan) or rando == 1:
      print("%s has been attacked by %s!" % (clan.Cname, target.Cname))
      if target.Cpower >= clan.Cpower:
        odds = (random.randint(1, 3))
        if odds == 1:
          win = True
        else: 
          win = False
      elif target.Cpower == clan.Cpower:
        odds = (random.randint(1, 2))
        if odds == 1:
          win = True
        else:
          win = False
      else:
        odds = (random.randint(1, 3))
        if not odds == 1:
          win = True
        else:
          win = False
      if win == True:
        print("%s won! %s gave one piece of land as payment." % (clan.Cname, target.Cname))
        clan.Cland += 1
        target.Cland -= 1
        clan.Cpower += 10
        target.Cpower -= 10
        if clan == player_Clan:
          death_count = (random.randint(0, 3))
          for i in range(0, death_count):
            dead_guy = (random.choice(list(player_Clan.cats.keys())))
            if dead_guy == "leader":
                protector = (random.choice(list(player_Clan.cats.keys())))
                if player_Clan.cats[protector].rep > 10:
                  print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
                  dead_guy = protector
            lives = death(player_Clan, lives, dead_guy) 
        else:
          rando = (random.randint(0, 3))
          for i in range(rando):
            dead_guy = (random.choice(list(player_Clan.cats.keys())))
            del clan.cats[dead_guy]
      else:
        print("%s won! %s gave one piece of land as payment." % (target.Cname, clan.Cname))
        clan.Cland -= 1
        target.Cland += 1
        clan.Cpower -= 10
        target.Cpower += 10
        if clan == player_Clan:
          death_count = (random.randint(0, 1))
          for i in range(0, death_count):
            dead_guy = (random.choice(list(player_Clan.cats.keys())))
            if dead_guy == "leader":
                protector = (random.choice(list(player_Clan.cats.keys())))
                if player_Clan.cats[protector].rep > 10:
                  print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
                  dead_guy = protector
            lives = death(player_Clan, lives, dead_guy)
        else:
          rando = (random.randint(0, 1))
          for i in range(rando):
            dead_guy = (random.choice(list(player_Clan.cats.keys())))
            del clan.cats[dead_guy]
    elif (target.Crep >= 3 and clan == player_Clan) or rando == 2:
      print("%s gave prey to %s!" % (target.Cname, clan.Cname))
      if clan == player_Clan:
        clan.Cprey += (random.randint(1, 100))
        target.Cpower -= (random.randint(1, 20))
      else:
        target.Cpower -= (random.randint(1, 20))
        clan.Cpower += (random.randint(1, 20))
  elif rando == "kits":
    if clan == player_Clan:
        Aparent = (random.choice(list(player_Clan.cats.keys())))
        while player_Clan.cats[Aparent].suffix == "paw" or player_Clan.cats[Aparent].rank == "kit" or player_Clan.cats[Aparent].isqueen == True or player_Clan.cats[Aparent].rank == "leader":
          Aparent = (random.choice(list(player_Clan.cats.keys())))
        Bparent = (random.choice(list(player_Clan.cats.keys())))
        while player_Clan.cats[Bparent].suffix == "paw" or player_Clan.cats[Bparent].rank == "kit" or player_Clan.cats[Bparent] == Aparent or player_Clan.cats[Bparent].isqueen == True or player_Clan.cats[Bparent].rank == "leader":
          Bparent = (random.choice(list(player_Clan.cats.keys())))
        kit_count = (random.randint(1, 5))
        if len(player_Clan.cats) < ((player_Clan.Cland * 10) - kit_count):
          if not player_Clan.cats[Aparent].mate == "":
            print("%s broke up with %s." % (player_Clan.cats[Aparent].name, player_Clan.cats[Aparent.mate].name))
          if not player_Clan.cats[Bparent].mate == "":
            print("%s broke up with %s." % (player_Clan.cats[Bparent].name, player_Clan.cats[Bparent.mate].name))
          print("%s and %s became mates!" % (player_Clan.cats[Aparent].name, player_Clan.cats[Bparent].name))
          player_Clan.cats[Aparent].mate = Bparent
          player_Clan.cats[Bparent].mate = Aparent
          if player_Clan.cats[Aparent].pronoun == player_Clan.cats[Bparent].pronoun:
            for i in range(0, kit_count):
              
              var_name = ""
              rando = (random.randint(5, 15))
              for i in range(rando):
                var_name = var_name + (random.choice(codebits))

              clan.cats[var_name] = cat("", (random.choice(prefixes)), "kit", (random.choice(pronouns)), (random.choice(coats)), "kit", (random.uniform(0.5, 1)), (random.randint(2, 4)), (random.choice(body_size)), (random.choice(body_build)), 0, "", "", 0, Aparent, player_Clan.cats[Bparent], False, "", "", "", 0)

              rando = (random.randint(0, 28))
              clan.cats[var_name].per1 = personality_traits[rando]
              clan.cats[var_name].quote = quotes[rando]
              clan.cats[var_name].per2 = (random.choice(personality_traits))

              while clan.cats[var_name].per2 == clan.cats[var_name].per1:
                clan.cats[var_name].per2 = (random.choice(personality_traits))

              if clan.cats[var_name].build == "very thin":
                clan.cats[var_name].feeding += .25
              elif clan.cats[var_name].build == "thin" or clan.cats[var_name].build == "hairless" or clan.cats[var_name].build == "lithe":
                clan.cats[var_name].feeding += .5
              elif clan.cats[var_name].build == "muscular":
                clan.cats[var_name].feeding += 1
              elif clan.cats[var_name].build == "very muscular" or clan.cats[var_name].build == "broad-shouldered":
                clan.cats[var_name].feeding += 1.25
              elif clan.cats[var_name].build == "plump" or clan.cats[var_name].build == "fluffy" or clan.cats[var_name].build == "stocky":
                clan.cats[var_name].feeding += 1.5
              elif clan.cats[var_name].build == "very plump":
                clan.cats[var_name].feeding += 1.75
              if clan.cats[var_name].size == "very small":
                clan.cats[var_name].feeding += .25
              elif clan.cats[var_name].size == "small":
                clan.cats[var_name].feeding += .5
              elif clan.cats[var_name].size == "large":
                clan.cats[var_name].feeding += 1
              elif clan.cats[var_name].size == "very large":
                clan.cats[var_name].feeding += 1.25
              clan.cats[var_name].name = clan.cats[var_name].prefix + clan.cats[var_name].suffix
              clan.cats[var_name].Aparent = clan.cats[Aparent].name
              clan.cats[var_name].Bparent = clan.cats[var_name.Bparent].name
              prefixes.remove(clan.cats[var_name].prefix)
              player_Clan.Cpower += clan.cats[var_name].power
              print("%s was adopted from a local kittypet!" % clan.cats[var_name].name)
          else:
            for i in range(0, kit_count):
                            
              var_name = ""
              rando = (random.randint(5, 15))
              for i in range(rando):
                var_name = var_name + (random.choice(codebits))

              clan.cats[var_name] = cat("", (random.choice(prefixes)), "kit", (random.choice(pronouns)), "", "kit", (random.uniform(0.5, 1)), (random.randint(2, 4)), "", "", 0, "", "", 0, Aparent, player_Clan.cats[Bparent], False, "", "", "", 0)

              rando = (random.randint(0, 28))
              clan.cats[var_name].per1 = personality_traits[rando]
              clan.cats[var_name].quote = quotes[rando]
              clan.cats[var_name].per2 = (random.choice(personality_traits))

              while clan.cats[var_name].per2 ==clan.cats[var_name].per1:
               clan.cats[var_name].per2 = (random.choice(personality_traits))

              rando = (random.randint(0, 1))
              if rando == 0:
                clan.cats[var_name].coat = player_Clan.cats[Aparent].coat
              else:
                clan.cats[var_name].coat = player_Clan.cats[Bparent].coat
              rando = (random.randint(0, 1))
              if rando == 0:
                clan.cats[var_name].build = player_Clan.cats[Aparent].build
              else:
                clan.cats[var_name].build = player_Clan.cats[Bparent].build
              rando = (random.randint(0, 1))
              if rando == 0:
                clan.cats[var_name].size = player_Clan.cats[Aparent].size
              else:
                clan.cats[var_name].size = player_Clan.cats[Bparent].size                           
              if clan.cats[var_name].build == "very thin":
                clan.cats[var_name].feeding += .25
              elif clan.cats[var_name].build == "thin" or clan.cats[var_name].build == "hairless" or clan.cats[var_name].build == "lithe":
                clan.cats[var_name].feeding += .5
              elif clan.cats[var_name].build == "muscular":
                clan.cats[var_name].feeding += 1
              elif clan.cats[var_name].build == "very muscular" or clan.cats[var_name].build == "broad-shouldered":
                clan.cats[var_name].feeding += 1.25
              elif clan.cats[var_name].build == "plump" or clan.cats[var_name].build == "fluffy" or clan.cats[var_name].build == "stocky":
                clan.cats[var_name].feeding += 1.5
              elif clan.cats[var_name].build == "very plump":
                clan.cats[var_name].feeding += 1.75
              if clan.cats[var_name].size == "very small":
                clan.cats[var_name].feeding += .25
              elif clan.cats[var_name].size == "small":
                clan.cats[var_name].feeding += .5
              elif clan.cats[var_name].size == "large":
                clan.cats[var_name].feeding += 1
              elif clan.cats[var_name].size == "very large":
                clan.cats[var_name].feeding += 1.25
              clan.cats[var_name].name = clan.cats[var_name].prefix + clan.cats[var_name].suffix
              clan.cats[var_name].Aparent = clan.cats[var_name].player_Clan.cats[Aparent].name
              clan.cats[var_name].Bparent = clan.cats[var_name.Bparent].name
              player_Clan.Cpower += clan.cats[var_name].power
              print("%s was born!" % clan.cats[var_name].name)
          rando_2 = (random.randint(1, 2))
          if rando_2 == 1:
            player_Clan.cats[Aparent].isqueen = True
          elif rando_2 == 2:
            player_Clan.cats[Bparent].isqueen = True
        else:
          print("%s and %s tried to have kits, but they must wait until the Clan population has lowered." % (Aparent, player_Clan.cats[Bparent]))
    else:
      rando = (random.randint(1, 5))
      for i in range(rando):
        var_name = ""
        rando = (random.randint(5, 15))
        for i in range(rando):
          var_name = var_name + (random.choice(codebits))

        clan.cats[var_name] = (random.choice(prefixes)) + (random.choice(suffixes))
  elif rando == "greencough":
    print("A devastating case of greencough spread through %s!" % clan.Cname)
    if clan == player_Clan:
       medcount = 0
       for i in player_Clan.cats:
          if player_Clan.cats[i].rank == "medicine cat" or player_Clan.cats[i].rank == "medicine apprentice":
            medcount += 1
       for i in player_Clan.cats:
          odds = 3 + medcount
          if player_Clan.cats[i].age <= 5 or player_Clan.cats[i].age >= 80:
             odds - 3
          rando = (random.randint(1, odds))
          if rando == 1:
            dead_guy = player_Clan.clans[i]
            lives = death(player_Clan, lives, dead_guy)
    else:
      clan.Cpower -= (random.randint(0, 25))
      rando = (random.randint(0, 3))
      if not len(clan.cats) - 1 < 1:
        for i in range(rando):
            dead_guy = (random.choice(list(player_Clan.cats.keys())))
            del clan.cats[dead_guy]
  elif rando == "deforestation":
    print("Twolegs are enroaching on %s territory! They have been forced to give up some of their land." % clan.Cname)
    if clan == player_Clan:
      clan.Cland -= 1
      clan.Cpower -= 20
    else:
      clan.Cpower -= 20
  elif rando == "mercenary":
    target = (random.choice(all_Clans.clans))
    if not target == player_Clan:
      while target == clan:
        target = (random.choice(all_Clans.clans))
      print("A mercenary sent by %s attacked %s's leader!" % (target.Cname, clan.Cname))
      rando_guy_power = (1, 3)
      if rando_guy_power == 1:
        print("But the mercenary failed, and %s's leader survived. However, they are badly shaken." % clan.Cname)
        clan.Cpower -= 5
      elif rando_guy_power == 2:
        print("While %s's leader survived the attack, they are very injured.")
        clan.Cpower -= 10
        if clan == player_Clan:
          player_Clan.cats["leader"].power = player_Clan.cats["leader"].power * (random.uniform(0.25, 0.75))
        else:
          clan.Cpower -= 10
      else:
        if clan == player_Clan:
         dead_guy = "leader"
         if dead_guy == "leader":
            protector = (random.choice(list(player_Clan.cats.keys())))
            if player_Clan.cats[protector].rep > 10:
              print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
              dead_guy = protector
            lives = death(player_Clan, lives, dead_guy)
        else:
          print("The mercenary succeeded! The leader of %s is dead!" % clan.Cname)
          clan.Cpower -= 20
          del list(clan.cats)[0]
          var_name = ""
          rando = (random.randint(5, 15))
          for i in range(rando):
            var_name = var_name + (random.choice(codebits))
          clan.cats[var_name] = (random.choice(prefixes)) + "star"
  elif rando == "traitor":
    print("There is a traitor in %s's midst!" % clan.Cname)
    if clan == player_Clan:
      traitor = (random.choice(list(player_Clan.cats.keys())))
      while player_Clan.cats[traitor].rank == "leader":
       traitor = (random.choice(list(player_Clan.cats.keys())))
      rando = (random.randint(1, 5))
      for i in range(rando):
        target = (random.choice(list(player_Clan.cats.keys())))
        while target == traitor:
          target = (random.choice(list(player_Clan.cats.keys())))
        if player_Clan.cats[traitor].power > player_Clan.cats[target].power:
         dead_guy = target
         if dead_guy == "leader":
            protector = (random.choice(list(player_Clan.cats.keys())))
            if player_Clan.cats[protector].rep > 10:
              print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
              dead_guy = protector
            lives = death(player_Clan, lives, dead_guy)
        else:
          print("%s managed to survive the traitor's blow! However, they escaped with severe injuries." % player_Clan.cats[target].name)
          player_Clan.cats[target].power = player_Clan.cats[target].power * (random.uniform(0.25, 0.75))
      cmd = 0
      while not cmd == "Y" and not cmd == "y" and not cmd == "N" and not cmd == "n":
       cmd = input("The traitor was revealed to be %s! Do you wish to exile them? [Y]/[N] | " % player_Clan.cats[traitor].name)
      if cmd == "Y" or cmd == "y":
        print("%s has been exiled. The other cats are grateful, for now they can rest easily." % player_Clan.cats[traitor].name) 
        if player_Clan.cats[traitor].rank == "deputy":
          new_deputy = (random.choice(list(player_Clan.cats.keys())))
          while not player_Clan.cats[new_deputy].rank == "warrior":
            new_deputy = (random.choice(list(player_Clan.cats.keys())))
          player_Clan.cats["deputy"].name = player_Clan.cats[new_deputy].name
          player_Clan.cats["deputy"].prefix = player_Clan.cats[new_deputy].prefix
          player_Clan.cats["deputy"].suffix = player_Clan.cats[new_deputy].suffix
          player_Clan.cats["deputy"].pronoun = player_Clan.cats[new_deputy].pronoun
          player_Clan.cats["deputy"].coat = player_Clan.cats[new_deputy].coat
          player_Clan.cats["deputy"].power = player_Clan.cats[new_deputy].power
          player_Clan.cats["deputy"].build = player_Clan.cats[new_deputy].build
          player_Clan.cats["deputy"].size = player_Clan.cats[new_deputy].size
          player_Clan.cats["deputy"].feeding = player_Clan.cats[new_deputy].feeding
          player_Clan.cats["deputy"].rank = "deputy"
          player_Clan.cats["deputy"].age = player_Clan.cats[new_deputy].age
          player_Clan.cats["deputy"].Aparent = player_Clan.cats[new_deputy].Aparent
          player_Clan.cats["deputy"].Bparent = player_Clan.cats[new_deputy].Bparent
          player_Clan.cats["deputy"].mate = player_Clan.cats[new_deputy].mate
          player_Clan.cats["deputy"].per1 = player_Clan.cats[new_deputy].per1
          player_Clan.cats["deputy"].per2 = player_Clan.cats[new_deputy].per2
          player_Clan.cats["deputy"].quote = player_Clan.cats[new_deputy].quote
          player_Clan.cats["deputy"].rep = player_Clan.cats[new_deputy].rep
          del player_Clan.cats[new_deputy]
          print("The new deputy is %s." % player_Clan.cats["deputy"].name)
        elif player_Clan.cats[traitor].rank == "medicine cat":
          new_med = ""
          for i in player_Clan.cats:
            if player_Clan.cats[i].rank == "medicine apprentice":
                new_med = player_Clan.cats[i]
                break
          if new_med == "":
            new_med = (random.choice(list(player_Clan.cats.keys())))
            while player_Clan.cats[new_med].rank == "leader" or player_Clan.cats[new_med].rank == "deputy" or player_Clan.cats[new_med].rank == "kit" or player_Clan.cats[new_med].rank == "medicine cat":
              player_Clan.cats[new_med] = (random.choice(list(player_Clan.cats.keys())))            
          player_Clan.cats["medicine_cat"].name = player_Clan.cats[new_med].name
          player_Clan.cats["medicine_cat"].prefix = player_Clan.cats[new_med].prefix
          player_Clan.cats["medicine_cat"].suffix = player_Clan.cats[new_med].suffix
          if player_Clan.cats["medicine_cat"].suffix == "paw":
              player_Clan.cats["medicine_cat"].suffix = (random.choice(suffixes))
          player_Clan.cats["medicine_cat"].pronoun = player_Clan.cats[new_med].pronoun
          player_Clan.cats["medicine_cat"].coat = player_Clan.cats[new_med].coat
          player_Clan.cats["medicine_cat"].power = player_Clan.cats[new_med].power
          player_Clan.cats["medicine_cat"].build = player_Clan.cats[new_med].build
          player_Clan.cats["medicine_cat"].size = player_Clan.cats[new_med].size
          player_Clan.cats["medicine_cat"].feeding = player_Clan.cats[new_med].feeding
          player_Clan.cats["medicine_cat"].rank = "medicine cat"
          player_Clan.cats["medicine_cat"].age = player_Clan.cats[new_med].age
          player_Clan.cats["medicine_cat"].Aparent = player_Clan.cats[new_med].Aparent
          player_Clan.cats["medicine_cat"].Bparent = player_Clan.cats[new_med].Bparent
          player_Clan.cats["medicine_cat"].mate = player_Clan.cats[new_med].mate
          player_Clan.cats["medicine_cat"].per1 = player_Clan.cats[new_med].per1
          player_Clan.cats["medicine_cat"].per2 = player_Clan.cats[new_med].per2
          player_Clan.cats["medicine_cat"].quote = player_Clan.cats[new_med].quote
          player_Clan.cats["medicine_cat"].rep = player_Clan.cats[new_med].rep
          del player_Clan.cats[new_med]
          print("The new medicine cat is %s." % (player_Clan.cats["medicine_cat"].name))
        else:
          for i in player_Clan.cats:
            if player_Clan.cats[i].mentor == player_Clan.cats[traitor]:
              player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
              while player_Clan.cats[player_Clan.cats[i].mentor].rank == "elder" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice" or player_Clan.cats[player_Clan.cats[i].mentor] == player_Clan.cats[traitor]:
                player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
          del player_Clan.cats[traitor]
          for i in player_Clan.cats:
            player_Clan.cats[i].rep += (random.randint(1, 3))
      else:
        print("You have decided to forgive %s for their crimes. They swear they will redeem themselves, but the other cats are distrustful of both them and you." % player_Clan.cats[traitor].name)
        for i in player_Clan.cats:
          if not player_Clan.cats[i] == player_Clan.cats[traitor]:
            player_Clan.cats[i].rep -= (random.randint(1, 3))
          else:
            player_Clan.cats[i].rep += (random.randint(1, 3))
  elif rando == "code_amendment":
    if not clan == player_Clan:
      print("%s has proposed a new rule to the Warrior Code!" % clan.Cname)
      possible = (random.choice(possible_code))
      print("'%s'" % possible)
      cmd = input("Would you like to approve this Code? [Y]/[N]")
      if cmd == "Y" or cmd == "y":
        yes = 2
        no = 0
      elif cmd == "N" or cmd == "n":
        yes = 1
        no = 1
      print("The rest of the Clans shall vote now, anonymously.")
      if len(all_Clans.clans) > 2:
        votes = len(all_Clans.clans) - 2
        for i in range(votes):
          rando = (random.randint(0, 1))
          if rando == 0:
            yes += 1
            print("One Clan voted yes!")
          else:
            no += 1
            print("One Clan voted no!")
      if yes > no:
        print("The '%s' rule was appended to the Warrior Code!" % possible)
        warrior_code.append(possible)
        possible_code.remove(possible)
      else:
        print("The rule was vetoed.")
  elif rando == "prophecy":
    if clan == player_Clan:
      receiver = player_Clan.cats["medicine_cat"].name
    else:
      if len(clan.cats) >= 3:
       receiver = clan.cats[2]
      else:
        receiver = clan.cats[0]
    print("At the %s, %s received a prophecy!" % (communer, receiver))
    prophecy = (random.choice(proph_beginnings)) + (random.choice(proph_middles)) + (random.choice(proph_ends))
    print("%s says: '%s'" % (receiver, prophecy))
  elif rando == "code_break":
    if len(warrior_code) > 0:
      if clan == player_Clan:
        breaker = (random.choice(clan.cats))
        while breaker.rank == "leader":
          breaker = (random.choice(clan.cats))
        code = (random.choice(warrior_code))
        print("%s has broken the Warrior Code! The rule was '%s.'" % (breaker.name, code))
        cmd = input("""How will you respond?
        
        [F]orgive
        [P]unish
        [E]xile""")
        if cmd == "F" or cmd == "f":
          print("You have forgiven %s for their crimes. %s is grateful, but the other Clans do not approve." % (breaker.name, breaker.name))
          breaker.power = breaker.power * (random.randint(2, 5))
          for i in all_Clans.clans:
            i.Crep -= 1
        elif cmd == "P" or cmd == "p":
          print("You have chosen to punish %s. %s feels less loyal to %s, but some of the other Clans see you in a better light." % (breaker.name, breaker.name, clan.Cname))
          breaker.power = breaker.power * (random.uniform(0.1, 0.5))
          for i in all_Clans.clans:
            i.Crep += 1
        else:
          print("You have chosen to exile %s." % breaker.name)
          if player_Clan.cats[breaker].rank == "deputy":
            new_deputy = (random.choice(list(player_Clan.cats.keys())))
            while not player_Clan.cats[new_deputy].rank == "warrior":
              new_deputy = (random.choice(list(player_Clan.cats.keys())))
            player_Clan.cats["deputy"].name = player_Clan.cats[new_deputy].name
            player_Clan.cats["deputy"].prefix = player_Clan.cats[new_deputy].prefix
            player_Clan.cats["deputy"].suffix = player_Clan.cats[new_deputy].suffix
            player_Clan.cats["deputy"].pronoun = player_Clan.cats[new_deputy].pronoun
            player_Clan.cats["deputy"].coat = player_Clan.cats[new_deputy].coat
            player_Clan.cats["deputy"].power = player_Clan.cats[new_deputy].power
            player_Clan.cats["deputy"].build = player_Clan.cats[new_deputy].build
            player_Clan.cats["deputy"].size = player_Clan.cats[new_deputy].size
            player_Clan.cats["deputy"].feeding = player_Clan.cats[new_deputy].feeding
            player_Clan.cats["deputy"].rank = "deputy"
            player_Clan.cats["deputy"].age = player_Clan.cats[new_deputy].age
            player_Clan.cats["deputy"].Aparent = player_Clan.cats[new_deputy].Aparent
            player_Clan.cats["deputy"].Bparent = player_Clan.cats[new_deputy].Bparent
            player_Clan.cats["deputy"].mate = player_Clan.cats[new_deputy].mate
            player_Clan.cats["deputy"].per1 = player_Clan.cats[new_deputy].per1
            player_Clan.cats["deputy"].per2 = player_Clan.cats[new_deputy].per2
            player_Clan.cats["deputy"].quote = player_Clan.cats[new_deputy].quote
            player_Clan.cats["deputy"].rep = player_Clan.cats[new_deputy].rep
            del player_Clan.cats[new_deputy]
            print("The new deputy is %s." % player_Clan.cats["deputy"].name)
          elif player_Clan.cats[breaker].rank == "medicine cat":
            new_med = ""
            for i in player_Clan.cats:
              if player_Clan.cats[i].rank == "medicine apprentice":
                  new_med = player_Clan.cats[i]
                  break
            if new_med == "":
              new_med = (random.choice(list(player_Clan.cats.keys())))
              while player_Clan.cats[new_med].rank == "leader" or player_Clan.cats[new_med].rank == "deputy" or player_Clan.cats[new_med].rank == "kit" or player_Clan.cats[new_med].rank == "medicine cat":
                player_Clan.cats[new_med] = (random.choice(list(player_Clan.cats.keys())))            
            player_Clan.cats["medicine_cat"].name = player_Clan.cats[new_med].name
            player_Clan.cats["medicine_cat"].prefix = player_Clan.cats[new_med].prefix
            player_Clan.cats["medicine_cat"].suffix = player_Clan.cats[new_med].suffix
            if player_Clan.cats["medicine_cat"].suffix == "paw":
                player_Clan.cats["medicine_cat"].suffix = (random.choice(suffixes))
            player_Clan.cats["medicine_cat"].pronoun = player_Clan.cats[new_med].pronoun
            player_Clan.cats["medicine_cat"].coat = player_Clan.cats[new_med].coat
            player_Clan.cats["medicine_cat"].power = player_Clan.cats[new_med].power
            player_Clan.cats["medicine_cat"].build = player_Clan.cats[new_med].build
            player_Clan.cats["medicine_cat"].size = player_Clan.cats[new_med].size
            player_Clan.cats["medicine_cat"].feeding = player_Clan.cats[new_med].feeding
            player_Clan.cats["medicine_cat"].rank = "medicine cat"
            player_Clan.cats["medicine_cat"].age = player_Clan.cats[new_med].age
            player_Clan.cats["medicine_cat"].Aparent = player_Clan.cats[new_med].Aparent
            player_Clan.cats["medicine_cat"].Bparent = player_Clan.cats[new_med].Bparent
            player_Clan.cats["medicine_cat"].mate = player_Clan.cats[new_med].mate
            player_Clan.cats["medicine_cat"].per1 = player_Clan.cats[new_med].per1
            player_Clan.cats["medicine_cat"].per2 = player_Clan.cats[new_med].per2
            player_Clan.cats["medicine_cat"].quote = player_Clan.cats[new_med].quote
            player_Clan.cats["medicine_cat"].rep = player_Clan.cats[new_med].rep
            del player_Clan.cats[new_med]
            print("The new medicine cat is %s." % (player_Clan.cats["medicine_cat"].name))
          else:
            for i in player_Clan.cats:
              if player_Clan.cats[i].mentor == player_Clan.cats[breaker]:
                player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
                while player_Clan.cats[player_Clan.cats[i].mentor].rank == "elder" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice" or player_Clan.cats[player_Clan.cats[i].mentor] == player_Clan.cats[breaker]:
                  player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
            del player_Clan.cats[breaker]
      else:
        code = (random.choice(warrior_code))
        print("%s has broken the Warrior Code! The rule was '%s'" % (clan.Cname, code))
        cmd = input("Will you forgive them? [Y]/[N]")
        if cmd == "Y" or cmd == "y":
          print("While %s is grateful, the other Clans do not approve." % clan.Cname)
          for i in all_Clans.clans:
            if i == clan:
              clan.Crep += 2
            else:
              clan.Crep -= 1
        else:
          print("While the other Clans approve of your decision, %s is bitter." % clan.Cname)
          for i in all_Clans.clans:
            if i == clan:
              clan.Crep -= 2
            else:
              clan.Crep += 1

        
    

  return lives

def main_menu(time_span, player_Clan, communer, mobile_friendly):
  cmd = 0
  while not cmd == "N" and not cmd == "n" and not cmd == "L" and not cmd == "l" and not cmd == "S" and not cmd == "s":
    if mobile_friendly == True:
      print("===Welcome to Warrior Cats: A New Dawn!===")
    else:
      print("""Welcome to:
 __      __            _            ___      _      _     _     _  _              ___                   
 \ \    / /_ _ _ _ _ _(_)___ _ _   / __|__ _| |_ __(_)   /_\   | \| |_____ __ __ |   \ __ ___ __ ___ __  
  \ \/\/ / _` | '_| '_| / _ \ '_| | (__/ _` |  _(_-<_   / _ \  | .` / -_) V  V / | |) / _` \ V  V / '  | 
   \_/\_/\__,_|_| |_| |_\___/_|    \___\__,_|\__/__(_) /_/ \_\ |_|\_\___|\_/\_/  |___/\__,_|\_/\_/|_||_|
                                                                                                        

============================================================================================================                        
     / // // __..--''``---....___   _..._    __           .   ☆ .     *    *   ☆   .      .   ☆ .     *  
   /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /      .     .  ✧   .  *  .  ✧    *    .     .  ✧  * 
  ///_.-' _..--.'_    \                    `( ) ) // //// ///   *    ☆     * ☆     * .  *    ☆     * ☆
  / (_..-' // (< _     ;_..__               ; `' / /// //// /// / //   .   ✧  .    *   .    .   ✧  .    *
   / // // //  `-._,_)' // / ``--...____..-' /// / /  ///  /////    ///   *    ✧ *   ☆   .       *    ✧ *
============================================================================================================""")

    cmd = input("""
    Please enter one of the commands below:

    [N]ew Game

    [L]oad Save
    
    [S]ettings | """)

  if cmd == "N" or cmd == "n":

    moon = 1
    day = 0
    quarter_moon = 0
    turns = 3
    social_turns = 3
    lives = 9

    # Part One: Customizing Your Clan

    rando = (random.randint(0, 14))

    your_location = locations[rando]

    your_predators = predators[rando]

    print("Your Clan has settled " + your_location + ".")

    your_Cname = input("Now that your Clan has survived the journey here, it would only be fitting to give them a name. What will your Clan's name be? Prefix only please. | ")
    your_Cname = your_Cname.capitalize() + "Clan"

    player_Clan = all_Clans(your_Cname, your_location, 0, 1, 0, your_predators, 0, {})

    print("Now, about you, leader of the great %s..." % your_Cname)

    cmd = input("Do you have a 'player seed' (pre-made character) you would like to use? [Y]/[N] | ")
    if cmd == "Y" or cmd == "y":
      seed = input("Please paste your character seed here: | ")
      loader = seed.split("|")
      player_Clan.cats["leader"] = cat("", loader[1], "star", loader[2], loader[3], "leader", (random.uniform(0.5, 1.5)), 5, loader[4], loader[5], 0, "", "", 36, "unknown", "unknown", False, loader[6], loader[7], loader[8], 0)
    else:
      print("Before you can receive your nine lives from StarClan, they need to know more about you. Firstly...")
      your_name = input("What do you call yourself, great leader? Prefix only please. | ")
      your_name.capitalize()
      your_pronoun = input("A few more questions, if you don't mind. Now, do you consider yourself a tom, she-cat or just 'cat'? | ")
      your_pronoun = your_pronoun.lower()
      your_coat = input("Also, how would you describe your coat colour? For example, black, black-and-white, tortoiseshell? Please answer in all lowercase, and don't bother including extra things like eye colour, just the base of your coat. | ")
      your_coat = your_coat.lower()
      your_size = input("Now, about how big or little are you? You may use modifiers like 'very' or 'super'. | ")
      your_size = your_size.lower()
      your_build = input("This may seem like an odd one, but how else would you describe yourself, in just one word? For example: plump, graceful, lithe, spiky-furred..? | ")
      your_build = your_build.lower()
      trait_a = input("Almost there! Now tell me, in what word, how would you describe your character, your personality? | ")
      trait_a = trait_a.lower()
      trait_b = input("What's another aspect to your personality, in one word? | ")
      trait_b = trait_b.lower()
      quote = input("Final thing! What's a quote that you believe encompasses you, as a leader? | ")

      player_Clan.cats["leader"] = cat("", your_name, "star", your_pronoun, your_coat, "leader", (random.uniform(0.5, 1.5)), 5, your_build, your_size, 0, "", "", 36, "unknown", "unknown", False, trait_a, trait_b, quote, 0)

      player_seed = player_Clan.cats["leader"].prefix + "|" + player_Clan.cats["leader"].pronoun + "|" +  player_Clan.cats["leader"].coat + "|" +  player_Clan.cats["leader"].build + "|" +  player_Clan.cats["leader"].size + "|" +  player_Clan.cats["leader"].per1 + "|" +  player_Clan.cats["leader"].per2 + "|" +  player_Clan.cats["leader"].quote + "|"
      print("If you would like to save your character data as a 'player seed', please copy (via right-click, not ctrl+c) the following seed and save it somewhere for later: %s" % player_seed) 

    all_Clans.clans.append(player_Clan)

    player_Clan.cats["leader"].name = player_Clan.cats["leader"].prefix + player_Clan.cats["leader"].suffix

    print("Welcome to the Warrior's World, " + player_Clan.cats["leader"].name + " of " + player_Clan.Cname + 
    "! May you have many great adventures in the vast wilderness.")

    random_pronoun = (random.choice(pronouns))

    prefix = (random.choice(prefixes))

    rando = (random.randint(0, 28))
    per1 = personality_traits[rando]
    quote = quotes[rando]
    per2 = (random.choice(personality_traits))

    while per2 == per1:
      per2 = (random.choice(personality_traits))

    suffix = input("Your deputy, a %s and %s %s, is named %s. What suffix will you give them? | " % (per1, per2, random_pronoun, prefix))

    player_Clan.cats["deputy"] = cat(prefix + suffix, prefix, suffix, random_pronoun, (random.choice(coats)), "deputy", (random.uniform(0.5, 1.5)), 5, (random.choice(body_build)), 
    (random.choice(body_size)), 0, "", "", (random.randint(12, 72)), "unknown", "unknown", False, per1, per2, quote, 10)

    if player_Clan.cats["deputy"].build == "very thin":
      player_Clan.cats["deputy"].feeding += .25
    elif player_Clan.cats["deputy"].build == "thin" or player_Clan.cats["deputy"].build == "hairless" or player_Clan.cats["deputy"].build == "lithe":
      player_Clan.cats["deputy"].feeding += .5
    elif player_Clan.cats["deputy"].build == "muscular":
      player_Clan.cats["deputy"].feeding += 1
    elif player_Clan.cats["deputy"].build == "very muscular" or player_Clan.cats["deputy"].build == "broad-shouldered":
      player_Clan.cats["deputy"].feeding += 1.25
    elif player_Clan.cats["deputy"].build == "plump" or player_Clan.cats["deputy"].build == "fluffy" or player_Clan.cats["deputy"].build == "stocky":
      player_Clan.cats["deputy"].feeding += 1.5
    elif player_Clan.cats["deputy"].build == "very plump":
      player_Clan.cats["deputy"].feeding += 1.75
    if player_Clan.cats["deputy"].build == "very small":
      player_Clan.cats["deputy"].feeding += .25
    elif player_Clan.cats["deputy"].build == "small":
      player_Clan.cats["deputy"].feeding += .5
    elif player_Clan.cats["deputy"].build == "large":
      player_Clan.cats["deputy"].feeding += 1
    elif player_Clan.cats["deputy"].build == "very large":
      player_Clan.cats["deputy"].feeding += 1.25

    prefixes.remove(player_Clan.cats["deputy"].prefix)

    print("Welcome your new deputy, " + player_Clan.cats["deputy"].name + ", to the Clan!")

    prefix = (random.choice(prefixes))

    rando = (random.randint(0, 28))
    per1 = personality_traits[rando]
    quote = quotes[rando]
    per2 = (random.choice(personality_traits))

    while per2 == per1:
      per2 = (random.choice(personality_traits))

    suffix = input("Your medicine cat, a %s and %s %s, is named %s. What suffix will you give them? | " % (per1, per2, random_pronoun, prefix))

    player_Clan.cats["medicine_cat"] = cat(prefix + suffix, prefix, suffix, random_pronoun, (random.choice(coats)), "medicine cat", (random.uniform(0.5, 1.5)), 5, (random.choice(body_build)), 
    (random.choice(body_size)), 0, "", "", (random.randint(12, 72)), "unknown", "unknown", False, per1, per2, quote, 10)

    prefixes.remove(player_Clan.cats["medicine_cat"].prefix)

    if player_Clan.cats["medicine_cat"].build == "very thin":
      player_Clan.cats["medicine_cat"].feeding += .25
    elif player_Clan.cats["medicine_cat"].build == "thin" or player_Clan.cats["medicine_cat"].build == "hairless" or player_Clan.cats["medicine_cat"].build == "lithe":
      player_Clan.cats["medicine_cat"].feeding += .5
    elif player_Clan.cats["medicine_cat"].build == "muscular":
      player_Clan.cats["medicine_cat"].feeding += 1
    elif player_Clan.cats["medicine_cat"].build == "very muscular" or player_Clan.cats["medicine_cat"].build == "broad-shouldered":
      player_Clan.cats["medicine_cat"].feeding += 1.25
    elif player_Clan.cats["medicine_cat"].build == "plump" or player_Clan.cats["medicine_cat"].build == "fluffy" or player_Clan.cats["medicine_cat"].build == "stocky":
      player_Clan.cats["medicine_cat"].feeding += 1.5
    elif player_Clan.cats["medicine_cat"].build == "very plump":
      player_Clan.cats["medicine_cat"].feeding += 1.75
    if player_Clan.cats["medicine_cat"].build == "very small":
      player_Clan.cats["medicine_cat"].feeding += .25
    elif player_Clan.cats["medicine_cat"].build == "small":
      player_Clan.cats["medicine_cat"].feeding += .5
    elif player_Clan.cats["medicine_cat"].build == "large":
      player_Clan.cats["medicine_cat"].feeding += 1
    elif player_Clan.cats["medicine_cat"].build == "very large":
      player_Clan.cats["medicine_cat"].feeding += 1.25

    print("Welcome your new medicine cat, " + player_Clan.cats["medicine_cat"].name + ", to the Clan!")

    rando = (random.randint(3, 9))

    for i in range(rando):

      var_name = ""
      rando = (random.randint(5, 15))
      for i in range(rando):
        var_name = var_name + (random.choice(codebits))

      player_Clan.cats[var_name] = cat("", (random.choice(prefixes)), "", 
    (random.choice(pronouns)), (random.choice(coats)), "", (random.uniform(0.5, 1.5)), (random.randint(2, 4)), (random.choice(body_build)), (random.choice(body_size)), 0, "", "", 0, "unknown", "unknown", False, "", "", "", (random.randint(-10, 10)))

      rando = (random.randint(0, 28))
      player_Clan.cats[var_name].per1 = personality_traits[rando]
      player_Clan.cats[var_name].quote = quotes[rando]
      player_Clan.cats[var_name].per2 = (random.choice(personality_traits))

      while player_Clan.cats[var_name].per2 == player_Clan.cats[var_name].per1:
        player_Clan.cats[var_name].per2 = (random.choice(personality_traits))

      player_Clan.cats[var_name].rank = (random.choice(ranks))
      if player_Clan.cats[var_name].rank == "medicine apprentice":
        rando = (random.randint(1, 2))
        if rando == 1:
          player_Clan.cats[var_name].suffix = "paw"
          player_Clan.cats[var_name].age = (random.randint(6, 18))
        else:
          player_Clan.cats[var_name].suffix = (random.choice(suffixes))
          player_Clan.cats[var_name].age = (random.randint(12, 36))
        player_Clan.cats[var_name].mentor = player_Clan.cats["medicine_cat"]
      elif player_Clan.cats[var_name].rank == "apprentice":
        player_Clan.cats[var_name].suffix = "paw"
        mentor = (random.choice(list(player_Clan.cats.keys())))
        player_Clan.cats[var_name].mentor = mentor
        while player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "apprentice" or player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "kit":
         player_Clan.cats[var_name].mentor = (random.choice(list(player_Clan.cats.keys())))
      elif player_Clan.cats[var_name].rank == "kit":
        player_Clan.cats[var_name].suffix = "kit"
        player_Clan.cats[var_name].age = (random.randint(0, 5))
      elif player_Clan.cats[var_name].rank == "elder":
        player_Clan.cats[var_name].age = (random.randint(70, 120))
        player_Clan.cats[var_name].suffix = (random.choice(suffixes))
      else:
        player_Clan.cats[var_name].age = (random.randint(12, 70))
        player_Clan.cats[var_name].suffix = (random.choice(suffixes))
      player_Clan.cats[var_name].name = player_Clan.cats[var_name].prefix + player_Clan.cats[var_name].suffix

      if player_Clan.cats[var_name].build == "very thin":
        player_Clan.cats[var_name].feeding += .25
      elif player_Clan.cats[var_name].build == "thin" or player_Clan.cats[var_name].build == "hairless" or player_Clan.cats[var_name].build == "lithe":
        player_Clan.cats[var_name].feeding += .5
      elif player_Clan.cats[var_name].build == "muscular":
        player_Clan.cats[var_name].feeding += 1
      elif player_Clan.cats[var_name].build == "very muscular" or player_Clan.cats[var_name].build == "broad-shouldered":
        player_Clan.cats[var_name].feeding += 1.25
      elif player_Clan.cats[var_name].build == "plump" or player_Clan.cats[var_name].build == "fluffy" or player_Clan.cats[var_name].build == "stocky":
        player_Clan.cats[var_name].feeding += 1.5
      elif player_Clan.cats[var_name].build == "very plump":
        player_Clan.cats[var_name].feeding += 1.75
      if player_Clan.cats[var_name].build == "very small":
        player_Clan.cats[var_name].feeding += .25
      elif player_Clan.cats[var_name].build == "small":
        player_Clan.cats[var_name].feeding += .5
      elif player_Clan.cats[var_name].build == "large":
        player_Clan.cats[var_name].feeding += 1
      elif player_Clan.cats[var_name].build == "very large":
        player_Clan.cats[var_name].feeding += 1.25
      
      prefixes.remove(player_Clan.cats[var_name].prefix)

      player_Clan.Cpower += player_Clan.cats[var_name].power

    # Part Two: Generate the Other Clans

    print("The other Clans shall introduce themselves now.")

    rando = (random.randint(1, 7))

    for i in range(0, rando):
      for i in possible_clans:
        if i == "":
          i = all_Clans((random.choice(prefixes)) + "Clan", (random.randint(0, 14)), 0, 1, (random.randint(6, 36)), "", (random.randint(-5, 5)), {})
          for a in all_Clans.clans:
            if a.Cname == i.Cname:
              i.Cname = (random.choice(prefixes)) + "Clan"
          i.Cpredator = predators[i.Clocation]
          i.Clocation = locations[i.Clocation]

          var_name = ""
          rando2 = (random.randint(5, 15))
          for a in range(rando2):
            var_name = var_name + (random.choice(codebits))
          
          i.cats[var_name] = (random.choice(prefixes)) + "star"

          rando = (random.randint(5, 11))

          for a in range(rando):

            i.cats[var_name] = ((random.choice(prefixes)) + (random.choice(suffixes)))

        print("%s lives %s." % (i.Cname, i.Clocation))
        all_Clans.clans.append(i)
        break

    discoverer = (random.choice(all_Clans.clans))

    communer = "Moon" + (random.choice(moon_suffixes))

    print("%s discovered the %s!" % (discoverer.Cname, communer))

    print("Your first few moons as a leader will be very difficult, and due to your small territory size no doubt some cats will starve. But you must press forward...")
    
    print("%s: %s- %s and %s %s %s" % (player_Clan.cats["leader"].rank, player_Clan.cats["leader"].name, player_Clan.cats["leader"].size, player_Clan.cats["leader"].build, player_Clan.cats["leader"].coat, player_Clan.cats["leader"].pronoun))
    print("%s: %s- %s and %s %s %s" % (player_Clan.cats["deputy"].rank, player_Clan.cats["deputy"].name, player_Clan.cats["deputy"].size, player_Clan.cats["deputy"].build, player_Clan.cats["deputy"].coat, player_Clan.cats["deputy"].pronoun))
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "medicine cat":
        print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "medicine apprentice":
        print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "warrior":
        print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "apprentice":
        print("%s: %s- %s and %s %s %s (mentor, %s)" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun, player_Clan.cats[player_Clan.cats[i].mentor].name))
    for i in player_Clan.cats:
      if player_Clan.cats[i].isqueen == True:
        print("queen: %s- %s and %s %s %s" % (player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "kit":
        print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
    for i in player_Clan.cats:
      if player_Clan.cats[i].rank == "elder":
        print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
    for i in all_Clans.clans:
      print("%s Power: %d" % (i.Cname, i.Cpower))

    gameplay(player_Clan, moon, day, quarter_moon, turns, social_turns, lives, time_span, communer)
  elif cmd == "L" or cmd == "l":

    cmd = input("""Please enter the ID of the file you would like to save on:
    
    SAVE [1]
    
    SAVE [2]
    
    SAVE [3]
    
    SAVE [4]
    
    SAVE [5]
    
    SAVE [6]
    
    SAVE [7]
    
    SAVE [8]
    
    SAVE [9]
    
    [M]ain Menu | """)
    
    if cmd == "M" or cmd == "m":
      main_menu(time_span, player_Clan, communer, mobile_friendly)
    else:
     filename = 'save_%s.dat' % cmd
     with open(filename, 'rb') as f:
       player_Clan.cats, all_Clans.clans, moon, day, quarter_moon, turns, social_turns, lives, communer = pickle.load(f)
     gameplay(player_Clan, moon, day, quarter_moon, turns, social_turns, lives, time_span, communer)
  else:
    cmd = 0
    while not cmd == "T" and not cmd == "t":
      cmd = input("""
      What setting would you like to change?
      
      [T]imespan | """)
    if cmd == "t" or cmd == "T":
      cmd = 0
      
      while not cmd == "D" and not cmd == "d" and not cmd == "Q" and not cmd == "q" and not cmd == "M" and not cmd == "m":
        cmd = input("""
        What timespan would you like to use?

        [D]ays: Best for Long-Term Play

        [Q]uarter-Moons: Recommended for Beginners

        [M]oons: Recommended for Quick Games or Experts

        | """)
      
      if cmd == "D" or cmd == "d":
        time_span = "day"
      elif cmd == "Q" or cmd == "q":
        time_span = "quarter-moon"
      elif cmd == "M" or cmd == "m":
        time_span = "moon"
      
      print("The timespan has been changed.")
    
      main_menu(time_span, player_Clan, communer, mobile_friendly)

def gameplay(player_Clan, moon, day, quarter_moon, turns, social_turns, lives, time_span, communer):
  while len(player_Clan.cats) >= 1:
    for i in player_Clan.cats:
      if not player_Clan.cats[i].rank == "leader":
        if player_Clan.cats[i].rep < -10:
          player_Clan.cats[i].quote = enemy_quotes[personality_traits.index(player_Clan.cats[i].per1)]
        else:
          player_Clan.cats[i].quote = quotes[personality_traits.index(player_Clan.cats[i].per1)]
    cmd = input("""The time is %d moon(s)- you have %d turns left, and %s social turns. What would you like to do?
    
    [A]ction = Make an action.
    
    [V]iew = View your allegiances or other Clan's stats. Does not use up one turn.
    
    [S]ave = Save your game.
    
    [E]xit = Exit the game (make sure you saved first! | """ % (moon, turns, social_turns))

    if cmd == "A" or cmd == "a":
      cmd = 0
      while not cmd == "S" and not cmd == "s" and not cmd == "E" and not cmd == "e":
        cmd = input("""What kind of [A]ction would you like to take?
        [E]xecutive Action = order your Clan around.

        [S]ocial Action = interact with your Clanmates. | """)
        
      if cmd == "S" or cmd == "s":
        if social_turns >= 1:
          cmd = 0
          while not cmd == "c" and not cmd == "C" and not cmd == "f" and not cmd == "F" and not cmd == "E" and not cmd == "e" and not cmd == "P" and not cmd == "p" and not cmd == "K" and not cmd == "k":
            id = 1
            for i in player_Clan.cats:
              print("%d: %s (%d)" % (id, player_Clan.cats[i].name, player_Clan.cats[i].rep))
              id += 1
            cmd = input("Which cat would you like to interact with? Type in their assigned ID. | ")
            target = list(player_Clan.cats)[int(cmd) - 1]
            cmd = input("""What action would you like to do with %s?
            
            [C]hat = Make small talk.

            [F]ight = Try to put them in their place.
            
            [E]xile = Kick them out of the Clan.
            
            [P]ropose = Try to become mates with them.
            
            [K]its = Try to have kits with them. | """ % player_Clan.cats[target].name)

            if cmd == "c" or cmd == "C":
              rando = (random.randint(-3, 3))
              if rando == -3:
                print("%s was offended by your remark, and aimed a slap at your face before leaving." % player_Clan.cats[target].name)
                player_Clan.cats[target].rep -= 3
              elif rando == -2:
                print("%s coldly replies that they need to go and excuses themselves" % player_Clan.cats[target].name)
                player_Clan.cats[target].rep -= 2
              elif rando == -1:
                print("%s appears uncomfortable throughout the exchange, and seems relived when the conversation is over." % player_Clan.cats[target].name)
                player_Clan.cats[target].rep -= 1
              elif rando == 0:
                print("%s nods and laughs along, but you're not sure if they're really listening. They barely even say a word before leaving mid-conversation." % player_Clan.cats[target].name)
              elif rando == 1:
                print("Even if %s doesn't participate much in the conversation, they seem to appreciate you being there." % player_Clan.cats[target].name)
                player_Clan.cats[target].name += 1
              elif rando == 2:
                print("%s seems to enjoy talking with you. When you both part ways, you notice a skip in their step as they pad away." % player_Clan.cats[target].name)
                player_Clan.cats[target].rep += 2
              else:
                print("You two seemed to really get along! They admit they're grateful that you're there for the Clan.")
                player_Clan.cats[target].rep += 3 
            elif cmd == "F" or cmd == "f":
              if player_Clan.cats[target].power >= player_Clan.cats["leader"].power:
                odds = (random.randint(0, 25))
              elif player_Clan.cats[target].power == player_Clan.cats["leader"].power:
                odds = (random.randint(0, 100))
              else:
                odds = (random.randint(75, 100))
              rando = (random.randint(0, 100))
              if odds >= rando:
                cmd = input("You have defeated them! Do you wish to finish them off? [Y]/[N] | ")
                if cmd == "Y" or cmd == "y":
                  dead_guy = target
                  lives = death(player_Clan, lives, dead_guy)
                elif cmd == "N" or cmd == "n":
                  player_Clan.cats[target].power * (random.uniform(0.5, 1))
                  rando = (random.randint(-3, 1))
                  if rando < 0:
                    print("%s may be weaker and less dangerous now, but their defeat has made them bitter." % player_Clan.cats[target].name)
                    player_Clan.cats[target].rep -= (random.randint(3, 5))
                  else:
                    print("Strangely, your victory seems to have only made %s respect you more." % player_Clan.cats[target].name)
                    player_Clan.cats[target].rep += (random.randint(3, 5))
            elif cmd == "E" or cmd == "e":
              print("%s has been exiled." % player_Clan.cats[target].name)
              if player_Clan.cats[target].rank == "deputy":
                new_deputy = (random.choice(list(player_Clan.cats.keys())))
                while not player_Clan.cats[new_deputy].rank == "warrior":
                  new_deputy = (random.choice(list(player_Clan.cats.keys())))
                player_Clan.cats["deputy"].name = player_Clan.cats[new_deputy].name
                player_Clan.cats["deputy"].prefix = player_Clan.cats[new_deputy].prefix
                player_Clan.cats["deputy"].suffix = player_Clan.cats[new_deputy].suffix
                player_Clan.cats["deputy"].pronoun = player_Clan.cats[new_deputy].pronoun
                player_Clan.cats["deputy"].coat = player_Clan.cats[new_deputy].coat
                player_Clan.cats["deputy"].power = player_Clan.cats[new_deputy].power
                player_Clan.cats["deputy"].build = player_Clan.cats[new_deputy].build
                player_Clan.cats["deputy"].size = player_Clan.cats[new_deputy].size
                player_Clan.cats["deputy"].feeding = player_Clan.cats[new_deputy].feeding
                player_Clan.cats["deputy"].rank = "deputy"
                player_Clan.cats["deputy"].age = player_Clan.cats[new_deputy].age
                player_Clan.cats["deputy"].Aparent = player_Clan.cats[new_deputy].Aparent
                player_Clan.cats["deputy"].Bparent = player_Clan.cats[new_deputy].Bparent
                player_Clan.cats["deputy"].mate = player_Clan.cats[new_deputy].mate
                player_Clan.cats["deputy"].per1 = player_Clan.cats[new_deputy].per1
                player_Clan.cats["deputy"].per2 = player_Clan.cats[new_deputy].per2
                player_Clan.cats["deputy"].quote = player_Clan.cats[new_deputy].quote
                player_Clan.cats["deputy"].rep = player_Clan.cats[new_deputy].rep
                del player_Clan.cats[new_deputy]
                print("The new deputy is %s." % player_Clan.cats["deputy"].name)
              elif player_Clan.cats[target].rank == "medicine cat":
                new_med = ""
                for i in player_Clan.cats:
                  if player_Clan.cats[i].rank == "medicine apprentice":
                      new_med = player_Clan.cats[i]
                      break
                if new_med == "":
                  new_med = (random.choice(list(player_Clan.cats.keys())))
                  while player_Clan.cats[new_med].rank == "leader" or player_Clan.cats[new_med].rank == "deputy" or player_Clan.cats[new_med].rank == "kit" or player_Clan.cats[new_med].rank == "medicine cat":
                    player_Clan.cats[new_med] = (random.choice(list(player_Clan.cats.keys())))            
                player_Clan.cats["medicine_cat"].name = player_Clan.cats[new_med].name
                player_Clan.cats["medicine_cat"].prefix = player_Clan.cats[new_med].prefix
                player_Clan.cats["medicine_cat"].suffix = player_Clan.cats[new_med].suffix
                if player_Clan.cats["medicine_cat"].suffix == "paw":
                    player_Clan.cats["medicine_cat"].suffix = (random.choice(suffixes))
                player_Clan.cats["medicine_cat"].pronoun = player_Clan.cats[new_med].pronoun
                player_Clan.cats["medicine_cat"].coat = player_Clan.cats[new_med].coat
                player_Clan.cats["medicine_cat"].power = player_Clan.cats[new_med].power
                player_Clan.cats["medicine_cat"].build = player_Clan.cats[new_med].build
                player_Clan.cats["medicine_cat"].size = player_Clan.cats[new_med].size
                player_Clan.cats["medicine_cat"].feeding = player_Clan.cats[new_med].feeding
                player_Clan.cats["medicine_cat"].rank = "medicine cat"
                player_Clan.cats["medicine_cat"].age = player_Clan.cats[new_med].age
                player_Clan.cats["medicine_cat"].Aparent = player_Clan.cats[new_med].Aparent
                player_Clan.cats["medicine_cat"].Bparent = player_Clan.cats[new_med].Bparent
                player_Clan.cats["medicine_cat"].mate = player_Clan.cats[new_med].mate
                player_Clan.cats["medicine_cat"].per1 = player_Clan.cats[new_med].per1
                player_Clan.cats["medicine_cat"].per2 = player_Clan.cats[new_med].per2
                player_Clan.cats["medicine_cat"].quote = player_Clan.cats[new_med].quote
                player_Clan.cats["medicine_cat"].rep = player_Clan.cats[new_med].rep
                del player_Clan.cats[new_med]
                print("The new medicine cat is %s." % (player_Clan.cats["medicine_cat"].name))
              else:
                for i in player_Clan.cats:
                  if player_Clan.cats[i].mentor == player_Clan.cats[target]:
                    player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
                    while player_Clan.cats[player_Clan.cats[i].mentor].rank == "elder" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice" or player_Clan.cats[player_Clan.cats[i].mentor] == player_Clan.cats[target]:
                      player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
                del player_Clan.cats[target]
            elif cmd == "P" or cmd == "p":
              if not player_Clan.cats[target].rank == "apprentice" and not player_Clan.cats[target].rank == "kit" and player_Clan.cats[target].mate == "":
                rando = (random.randint(1, 2))
                if rando == 1 and player_Clan.cats[target].rep >= 15:
                  print("%s accepted!" % player_Clan.cats[target].name)
                  player_Clan.cats[target].mate = "leader"
                  player_Clan.cats["leader"].mate = target
                else:
                  print("Unfortunately, %s doesn't feel the same way, and in fact this has only dug a deeper rift between you both." % player_Clan.cats[target].name)
                  player_Clan.cats[target].rep -= (random.randint(3, 8))
              else:
                print("You cannot propose to %s right now." % player_Clan.cats[target].name)
            elif cmd == "K" or cmd == "k":
              rando = (random.randint(1, 4))
              if player_Clan.cats[target].mate == "leader" or rando == 1:
                Aparent = "leader"
                Bparent = target
                kit_count = (random.randint(1, 5))
                if len(player_Clan.cats) < ((player_Clan.Cland * 10) - kit_count):
                  player_Clan.cats[Aparent].mate = Bparent
                  player_Clan.cats[Bparent].mate = Aparent
                  if player_Clan.cats[Aparent].pronoun == player_Clan.cats[Bparent].pronoun:
                    for i in range(0, kit_count):
                      
                      var_name = ""
                      rando = (random.randint(5, 15))
                      for i in range(rando):
                        var_name = var_name + (random.choice(codebits))
                    
                      clan.cats[var_name] = cat("", "", "kit", (random.choice(pronouns)), (random.choice(coats)), "kit", (random.uniform(0.5, 1)), (random.randint(2, 4)), (random.choice(body_size)), (random.choice(body_build)), 0, "", "", 0, Aparent, player_Clan.cats[Bparent], False, "", "", "", 0)

                      rando = (random.randint(1, 2))
                      if rando == 1:
                        clan.cats[var_name].prefix = input("What would you like to name your kit, a %s and %s %s %s?" % (clan.cats[var_name].size, clan.cats[var_name].build, clan.cats[var_name].coat, clan.cats[var_name].pronoun))
                      else:
                        clan.cats[var_name].prefix = (random.choice(prefixes))

                      rando = (random.randint(0, 28))
                      clan.cats[var_name].per1 = personality_traits[rando]
                      clan.cats[var_name].quote = quotes[rando]
                      clan.cats[var_name].per2 = (random.choice(personality_traits))

                      while clan.cats[var_name].per2 == clan.cats[var_name].per1:
                        clan.cats[var_name].per2 = (random.choice(personality_traits))

                      if clan.cats[var_name].build == "very thin":
                        clan.cats[var_name].feeding += .25
                      elif clan.cats[var_name].build == "thin" or clan.cats[var_name].build == "hairless" or clan.cats[var_name].build == "lithe":
                        clan.cats[var_name].feeding += .5
                      elif clan.cats[var_name].build == "muscular":
                        clan.cats[var_name].feeding += 1
                      elif clan.cats[var_name].build == "very muscular" or clan.cats[var_name].build == "broad-shouldered":
                        clan.cats[var_name].feeding += 1.25
                      elif clan.cats[var_name].build == "plump" or clan.cats[var_name].build == "fluffy" or clan.cats[var_name].build == "stocky":
                        clan.cats[var_name].feeding += 1.5
                      elif clan.cats[var_name].build == "very plump":
                        clan.cats[var_name].feeding += 1.75
                      if clan.cats[var_name].size == "very small":
                        clan.cats[var_name].feeding += .25
                      elif clan.cats[var_name].size == "small":
                        clan.cats[var_name].feeding += .5
                      elif clan.cats[var_name].size == "large":
                        clan.cats[var_name].feeding += 1
                      elif clan.cats[var_name].size == "very large":
                        clan.cats[var_name].feeding += 1.25
                      clan.cats[var_name].name = clan.cats[var_name].prefix + clan.cats[var_name].suffix
                      clan.cats[var_name].Aparent = clan.cats[var_name].player_Clan.cats[Aparent].name
                      clan.cats[var_name].Bparent = clan.cats[var_name.Bparent].name
                      prefixes.remove(clan.cats[var_name].prefix)
                      player_Clan.Cpower += clan.cats[var_name].power
                      print("%s was adopted from a local kittypet!" % clan.cats[var_name].name)
                  else:
                    for i in range(0, kit_count):
                                    
                      var_name = ""
                      rando = (random.randint(5, 15))
                      for i in range(rando):
                        var_name = var_name + (random.choice(codebits))

                      clan.cats[var_name] = cat("", "", "kit", (random.choice(pronouns)), "", "kit", (random.uniform(0.5, 1)), (random.randint(2, 4)), "", "", 0, "", "", 0, Aparent, player_Clan.cats[Bparent], False, "", "", "", 0)

                      rando = (random.randint(0, 28))
                      clan.cats[var_name].per1 = personality_traits[rando]
                      clan.cats[var_name].quote = quotes[rando]
                      clan.cats[var_name].per2 = (random.choice(personality_traits))

                      while clan.cats[var_name].per2 ==clan.cats[var_name].per1:
                        clan.cats[var_name].per2 = (random.choice(personality_traits))

                      rando = (random.randint(0, 1))
                      if rando == 0:
                        clan.cats[var_name].coat = player_Clan.cats[Aparent].coat
                      else:
                        clan.cats[var_name].coat = player_Clan.cats[Bparent].coat
                      rando = (random.randint(0, 1))
                      if rando == 0:
                        clan.cats[var_name].build = player_Clan.cats[Aparent].build
                      else:
                        clan.cats[var_name].build = player_Clan.cats[Bparent].build
                      rando = (random.randint(0, 1))
                      if rando == 0:
                        clan.cats[var_name].size = player_Clan.cats[Aparent].size
                      else:
                        clan.cats[var_name].size = player_Clan.cats[Bparent].size                           
                      if clan.cats[var_name].build == "very thin":
                        clan.cats[var_name].feeding += .25
                      elif clan.cats[var_name].build == "thin" or clan.cats[var_name].build == "hairless" or clan.cats[var_name].build == "lithe":
                        clan.cats[var_name].feeding += .5
                      elif clan.cats[var_name].build == "muscular":
                        clan.cats[var_name].feeding += 1
                      elif clan.cats[var_name].build == "very muscular" or clan.cats[var_name].build == "broad-shouldered":
                        clan.cats[var_name].feeding += 1.25
                      elif clan.cats[var_name].build == "plump" or clan.cats[var_name].build == "fluffy" or clan.cats[var_name].build == "stocky":
                        clan.cats[var_name].feeding += 1.5
                      elif clan.cats[var_name].build == "very plump":
                        clan.cats[var_name].feeding += 1.75
                      if clan.cats[var_name].size == "very small":
                        clan.cats[var_name].feeding += .25
                      elif clan.cats[var_name].size == "small":
                        clan.cats[var_name].feeding += .5
                      elif clan.cats[var_name].size == "large":
                        clan.cats[var_name].feeding += 1
                      elif clan.cats[var_name].size == "very large":
                        clan.cats[var_name].feeding += 1.25
                      clan.cats[var_name].name = clan.cats[var_name].prefix + clan.cats[var_name].suffix
                      clan.cats[var_name].Aparent = clan.cats[var_name].player_Clan.cats[Aparent].name
                      clan.cats[var_name].Bparent = clan.cats[var_name.Bparent].name
                      player_Clan.Cpower += clan.cats[var_name].power
                      rando = (random.randint(1, 2))
                      if rando == 1:
                        clan.cats[var_name].prefix = input("What would you like to name your kit, a %s and %s %s %s?" % (clan.cats[var_name].size, clan.cats[var_name].build, clan.cats[var_name].coat, clan.cats[var_name].pronoun))
                      else:
                        clan.cats[var_name].prefix = (random.choice(prefixes))
                      print("%s was born!" % clan.cats[var_name].name)
                  rando_2 = (random.randint(1, 2))
                  if rando_2 == 1:
                    player_Clan.cats[Aparent].isqueen = True
                  elif rando_2 == 2:
                    player_Clan.cats[Bparent].isqueen = True
                else:
                  print("%s and %s tried to have kits, but they must wait until the Clan population has lowered." % (player_Clan.cats[Aparent].name, player_Clan.cats[Bparent].name))
              else:
                print("You cannot have kits with %s right now." % player_Clan.cats[target].name)
            social_turns -= 1
        else:
          print("It's too late to socialize. Try ordering them around to pass the time.")
      elif cmd == "E" or cmd == "e":
        cmd = input("""What [E]xecutive action would you like to do?
        
        [H]unt = send out a hunting patrol.
        
        [C]laim = discover new land for your Clan.
        
        [T]rain = raise the power of your warriors.
        
        [R]ecruit = find new cats to populate your Clan!
        
        [F]ight = battle another Clan!
        
        [G]ift = Give a gift to another Clan! | """)

        if (cmd == "BETA" or cmd == "beta") and not 'done' in beta_help:
          player_Clan.Cprey += 35
          player_Clan.Cland += 3
          player_Clan.Cpower += 25
          player_Clan.cats["nightwhisker"] = cat("Nightwhisker", "Night", "whisker", 
              "she-cat", "black-and-silver", "warrior", 1, 10, "tall", "stocky", 0.5, "", "",25, "unknown", "unknown", False, "stubborn", "faithful", "A Clan's morality ought to align with tradition. It ain't moral otherwise.", 5)
          beta_help.append('done')
          print("Thank you for being a Beta Tester! Please accept your Beta Tester Package of 35 prey, 3 land, 25 power, and an extra special cat.")

        
        elif cmd == "H" or cmd == "h":
          hunters = []
          new_prey = 0
          for i in range(5):
            total = 0
            i = (random.choice(list(player_Clan.cats.keys())))
            if not i in hunters:
              if player_Clan.cats[i].rank == "warrior" or player_Clan.cats[i].rank == "apprentice" or player_Clan.cats[i].rank == "deputy" or player_Clan.cats[i].rank == "leader":
                hunters.append(i)
          for i in hunters:
            new_prey = player_Clan.Cland * (random.uniform(.5, 1.5)) * player_Clan.cats[i].hunting_skill
            print("%s has caught %d feedings." % (player_Clan.cats[i].name, round(new_prey)))
            total += new_prey
          if player_Clan.cats[i].hunting_skill < 1.5:
            player_Clan.cats[i].hunting_skill += 0.1
          player_Clan.Cprey += total
          if new_prey == 0:
            print("Your cats didn't catch anything. Maybe try recruiting more warriors?")
        elif cmd == "C" or cmd == "c":
          rando = (random.randint(0, round(player_Clan.Cland/2)))
          if rando == 0:
            player_Clan.Cland += (random.randint(1, 3))
            print("Your exploratory patrol claimed new territory! Now you will catch more when you hunt.")
          else:
            print("Unfortunately, your exploratory patrol came back empty-pawed.")
        elif cmd == "T" or cmd == "t":
          trainee_1 = (random.choice(list(player_Clan.cats.keys())))
          while player_Clan.cats[trainee_1].rank == "medicine cat" or player_Clan.cats[trainee_1].rank == "medicine apprentice" or player_Clan.cats[trainee_1].rank == "elder" or player_Clan.cats[trainee_1].rank == "kit" or player_Clan.cats[trainee_1].isqueen == True:
            trainee_1 = (random.choice(list(player_Clan.cats.keys())))
          trainee_2 = (random.choice(list(player_Clan.cats.keys())))
          while player_Clan.cats[trainee_2].rank == "medicine cat" or player_Clan.cats[trainee_2].rank == "medicine apprentice" or player_Clan.cats[trainee_2].rank == "elder" or player_Clan.cats[trainee_2].rank == "kit" or player_Clan.cats[trainee_2].isqueen == True:
            trainee_2 = (random.choice(list(player_Clan.cats.keys())))
          if trainee_2 == trainee_1:
            while trainee_2 == trainee_1:
              trainee_2 = (random.choice(list(player_Clan.cats.keys())))
            while player_Clan.cats[trainee_2].rank == "medicine cat" or player_Clan.cats[trainee_2].rank == "medicine apprentice" or player_Clan.cats[trainee_2].rank == "kit" or player_Clan.cats[trainee_2].rank == "elder"  or player_Clan.cats[trainee_2].isqueen == True:
              trainee_2 = (random.choice(list(player_Clan.cats.keys())))
          trainee_3 = (random.choice(list(player_Clan.cats.keys())))
          while player_Clan.cats[trainee_3].rank == "medicine cat" or player_Clan.cats[trainee_3].rank == "medicine apprentice" or player_Clan.cats[trainee_3].rank == "elder" or player_Clan.cats[trainee_3].rank == "kit" or player_Clan.cats[trainee_3].isqueen == True:
            trainee_3 = (random.choice(list(player_Clan.cats.keys())))
          if trainee_3 == trainee_1 or trainee_3 == trainee_2:
            while trainee_3 == trainee_1 or trainee_3 == trainee_2:
              trainee_3 = (random.choice(list(player_Clan.cats.keys())))
            while player_Clan.cats[trainee_3].rank == "medicine cat" or player_Clan.cats[trainee_3].rank == "medicine apprentice" or player_Clan.cats[trainee_3].rank == "elder" or player_Clan.cats[trainee_3].rank == "kit" or player_Clan.cats[trainee_3].isqueen == True:
              trainee_3 = (random.choice(list(player_Clan.cats.keys())))
          train_amount = (random.randint(1, 5))
          player_Clan.cats[trainee_1].power += train_amount
          player_Clan.cats[trainee_2].power += train_amount
          player_Clan.cats[trainee_3].power += train_amount
          print("%s, %s, and %s have decided to train together." % (player_Clan.cats[trainee_1].name, player_Clan.cats[trainee_2].name, player_Clan.cats[trainee_3].name))
          print("Your Clan's power grew by %d!" % (train_amount * 3))
          player_Clan.Cpower += train_amount * 3
        elif cmd == "R" or cmd == "r":
          if len(player_Clan.cats) < (player_Clan.Cland * 10):
            prefix = (random.choice(prefixes))
            prefixes.remove(prefix)
            pronoun = (random.choice(pronouns))
            print("You find a %s named %s on your territory who once lived %s. | " % (pronoun, prefix, (random.choice(locations))))

            var_name = ""
            rando = (random.randint(5, 15))
            for i in range(rando):
              var_name = var_name + (random.choice(codebits))

            player_Clan.cats[var_name] = cat("", prefix, "", 
            pronoun, (random.choice(coats)), "", (random.uniform(0.5, 1.5)), (random.randint(2, 4)), (random.choice(body_build)), (random.choice(body_size)), 0, "", "", 0, "unknown", "unknown", False, "", "", "", (random.randint(-15, 15)))

            rando = (random.randint(0, 28))
            player_Clan.cats[var_name].per1 = personality_traits[rando]
            player_Clan.cats[var_name].quote = quotes[rando]
            player_Clan.cats[var_name].per2 = (random.choice(personality_traits))

            while player_Clan.cats[var_name].per2 == player_Clan.cats[var_name].per1:
              player_Clan.cats[var_name].per2 = (random.choice(personality_traits))

            rando = (random.randint(1, 4))
            player_Clan.cats[var_name].rank = (random.choice(ranks))
            if player_Clan.cats[var_name].rank == "medicine apprentice":
              rando = (random.randint(1, 2))
              if rando == 1:
                player_Clan.cats[var_name].suffix = "paw"
                player_Clan.cats[var_name].age = (random.randint(7, 18))
              else:
                player_Clan.cats[var_name].suffix = (random.choice(suffixes))
                player_Clan.cats[var_name].age = (random.randint(12, 36))
                player_Clan.cats[var_name].mentor = (player_Clan.cats["medicine_cat"])
            elif player_Clan.cats[var_name].rank == "apprentice":
              player_Clan.cats[var_name].age = (random.randint(7, 18))
              player_Clan.cats[var_name].suffix = "paw"
              mentor = (random.choice(list(player_Clan.cats.keys())))
              player_Clan.cats[var_name].mentor = player_Clan.cats[mentor]
              while player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "medicine cat" or player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "medicine apprentice" or player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[var_name].mentor].rank == "apprentice":
                player_Clan.cats[var_name].mentor = (random.choice(list(player_Clan.cats.keys())))
            elif player_Clan.cats[var_name].rank == "elder":
              player_Clan.cats[var_name].age = (random.randint(84, 120))
              if not rando == 1:
                player_Clan.cats[var_name].suffix = input("What suffix would you like to give them? | ")
            elif player_Clan.cats[var_name].rank == "kit":
              player_Clan.cats[var_name].age = (random.randint(1, 6))
              player_Clan.cats[var_name].suffix = "kit"
            else:
              player_Clan.cats[var_name].age = (random.randint(12, 74))
              if not rando == 1:
                player_Clan.cats[var_name].suffix = input("What suffix would you like to give them? | ")
            if player_Clan.cats[var_name].build == "very thin":
              player_Clan.cats[var_name].feeding += .25
            elif player_Clan.cats[var_name].build == "thin" or player_Clan.cats[var_name].build == "hairless" or player_Clan.cats[var_name].build == "lithe":
              player_Clan.cats[var_name].feeding += .5
            elif player_Clan.cats[var_name].build == "muscular":
              player_Clan.cats[var_name].feeding += 1
            elif player_Clan.cats[var_name].build == "very muscular" or player_Clan.cats[var_name].build == "broad-shouldered":
              player_Clan.cats[var_name].feeding += 1.25
            elif player_Clan.cats[var_name].build == "plump" or player_Clan.cats[var_name].build == "fluffy" or player_Clan.cats[var_name].build == "stocky":
              player_Clan.cats[var_name].feeding += 1.5
            elif player_Clan.cats[var_name].build == "very plump":
              player_Clan.cats[var_name].feeding += 1.75
            if player_Clan.cats[var_name].size == "very small":
              player_Clan.cats[var_name].feeding += .25
            elif player_Clan.cats[var_name].size == "small":
              player_Clan.cats[var_name].feeding += .5
            elif player_Clan.cats[var_name].size == "large":
              player_Clan.cats[var_name].feeding += 1
            elif player_Clan.cats[var_name].size == "very large":
              player_Clan.cats[var_name].feeding += 1.25
            player_Clan.cats[var_name].name = player_Clan.cats[var_name].prefix + player_Clan.cats[var_name].suffix
            player_Clan.Cpower += player_Clan.cats[var_name].power
            print("%s has joined the Clan." % player_Clan.cats[var_name].name)
              
          else:
            print("Your Clan is too full! Wait for your population to lower first.")
        elif cmd == "F" or cmd == "f":
          id = 0
          for i in all_Clans.clans:
            print("%d : %s" % (id, i.Cname))
            id += 1
          target = input("Who do you want to fight? You cannot choose yourself. | ")
          while int(target) == 0:
            target = input("Who do you want to fight? You cannot choose yourself. | ")
          target = all_Clans.clans[int(target)]
          if target.Cpower >= player_Clan.Cpower:
            odds = (random.randint(0, 25))
          elif target.Cpower == player_Clan.Cpower:
            odds = (random.randint(0, 100))
          else:
            odds = (random.randint(75, 100))
          rando = (random.randint(0, 100))
          if odds >= rando:
            print("You have won! The enemy has given you one piece of land as payment.")
            target.Crep -= (random.randint(1, 5))
            if target.Crep < -5:
              target.Crep = -5
            player_Clan.Cland += 1
            target.Cland -= 1
            player_Clan.Cpower += 10
            target.Cpower -= 10
            death_count = (random.randint(0, 3))
            for i in range(0, death_count):
              dead_guy = (random.choice(list(player_Clan.cats.keys())))
              if dead_guy == "leader":
                  protector = (random.choice(list(player_Clan.cats.keys())))
                  if player_Clan.cats[protector].rep > 10:
                    print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
                    dead_guy = protector
                  lives = death(player_Clan, lives, dead_guy)
          else:
            target.Crep -= (random.randint(1, 3))
            if target.Crep < -5:
              target.Crep = -5
            print("The enemy has won! You had to give up one piece of land as payment.")
            player_Clan.Cland -= 1
            target.Cland += 1
            player_Clan.Cpower -= 10
            target.Cpower += 10
            death_count = (random.randint(0, 3))
            for i in range(0, death_count):
              dead_guy = (random.choice(list(player_Clan.cats.keys())))
              if dead_guy == "leader":
                  protector = (random.choice(list(player_Clan.cats.keys())))
                  if player_Clan.cats[protector].rep > 10:
                    print("%s took a hit for you and died in your place!" % player_Clan.cats[protector].name)
                    dead_guy = protector
                  lives = death(player_Clan, lives, dead_guy)
        elif cmd == "G" or cmd == "g":
          id = 0
          for i in all_Clans.clans:
            print("%d : %s" % (id, i.Cname))
            id += 1
          target = input("Who do you want to send a gift to? You cannot choose yourself. | ")
          while int(target) == 0:
            target = input("Who do you want to send a gift to? You cannot choose yourself. | ")
          target = all_Clans.clans[int(target)]
          amount = input("How much prey would you like to gift them? | ")
          amount = int(amount)
          if amount <= 20:
            target.Crep += (random.randint(0, 2))
          elif amount <= 40:
            target.Crep += (random.randint(1, 3))
          elif amount <= 60:
            target.Crep += (random.randint(2, 4))
          elif amount <= 80:
            target.Crep += (random.randint(3, 5))
          elif amount <= 100:
            target.Crep += (random.randint(4, 6))
          else:
            target.Crep += (random.randint(5, 7))
          if target.Crep > 5:
            target.Crep = 5
          print("I'm sure %s really appreciates it." % target.Cname)
        turns -= 1
      
    elif cmd == "V" or cmd == "v":
      while not cmd == "C" and not cmd == "c" and not cmd == "M" and not cmd == "m" and not cmd == "O" and not cmd == "o" and not cmd == "w" and not cmd == "W":
        cmd = input("""What would you like to view?
        [M]y Clan's overall stats
        [C]ats from my Clan
        [O]ther Clans
        [W]arrior Code | """)
      if cmd == "M" or cmd == "m":
        print("""
===%s's Stats===
        
Location: %s
Local Predator: %s
Population: %d
Land: %d
Prey: %d
Power: %d""" % (player_Clan.Cname, player_Clan.Clocation, player_Clan.Cpredator, len(player_Clan.cats), player_Clan.Cland, player_Clan.Cprey, player_Clan.Cpower))
      elif cmd == "C" or cmd == "c":
        id = 1
        for i in player_Clan.cats:
          print("%d: %s" % (id, player_Clan.cats[i].name))
          id += 1
        cmd = input("Which cat would you like to view? Type in their assigned ID. | ")
        target = list(player_Clan.cats)[int(cmd) - 1]
        if player_Clan.cats[target].mate == player_Clan.cats["leader"]:
          reputation = "Mate"
        elif player_Clan.cats[target] == player_Clan.cats["leader"]:
          reputation = "Player"
        elif player_Clan.cats[target].rep < -10:
          reputation = "Enemy"
          player_Clan.cats[target].quote = player_Clan.cats[target].quote % player_Clan.cats["leader"].name
        elif player_Clan.cats[target].rep < 0:
          reputation = "Bully"
        elif player_Clan.cats[target].rep > 10:
          reputation = "Best Friend"
        elif player_Clan.cats[target].rep > 0:
          reputation = "Friend"
        else:
          reputation = "Neutral"
        if player_Clan.cats[target].Aparent == "unknown":
            print("""
===%s (%s)===

"%s"        

Gender: %s
Rank: %s
Age: %d
> Power: %d
Description: %s and %s %s %s
Personality: %s and %s
Parents: Unknown""" % (player_Clan.cats[target].name, reputation, player_Clan.cats[target].quote, player_Clan.cats[target].pronoun, player_Clan.cats[target].rank, player_Clan.cats[target].age, player_Clan.cats[target].power, player_Clan.cats[target].size, player_Clan.cats[target].build, player_Clan.cats[target].coat, player_Clan.cats[target].pronoun, player_Clan.cats[target].per1, player_Clan.cats[target].per2))
        else:
          print("""
===%s (%s)===

"%s"    

Gender: %s
Rank: %s
Age: %d
> Power: %d
Description: %s and %s %s %s
Personality: %s and %s
Parents: %s and %s""" % (player_Clan.cats[target].name, reputation, player_Clan.cats[target].quote, player_Clan.cats[target].pronoun, player_Clan.cats[target].rank, player_Clan.cats[target].age, player_Clan.cats[target].power, player_Clan.cats[target].size, player_Clan.cats[target].build, player_Clan.cats[target].coat, player_Clan.cats[target].pronoun, player_Clan.cats[target].per1, player_Clan.cats[target].per2,player_Clan.cats[target].Aparent, player_Clan.cats[target].Bparent))
        if player_Clan.cats[target].rank == "apprentice":
          print("Mentor: %s" % player_Clan.cats[player_Clan.cats[target].mentor].name)
        if not player_Clan.cats[target].mate == "":
          print("Mate: %s" % player_Clan.cats[target.mate].name)
      elif cmd == "O" or cmd == "o":
        id = 0
        for i in all_Clans.clans:
          print("%d: %s" % (id, i.Cname))
          id += 1
        cmd = 0
        while cmd == 0:
         cmd = input("Which Clan would you like to view? You cannot choose yourself. | ")
        target = all_Clans.clans[int(cmd)]
        print("""
===%s's Stats===

Location: %s
Local Predator: %s
Power: %s""" % (target.Cname, target.Clocation, target.Cpredator, target.Cpower))
        if target.Crep <= -3:
          print("Status: Hates %s" % player_Clan.Cname)
        elif target.Crep < 0:
          print("Status: Dislikes %s" % player_Clan.Cname)
        elif target.Crep == 0:
          print("Status: Indifferent About %s" % player_Clan.Cname)
        elif target.Crep < 4:
          print("Status: Likes %s" % player_Clan.Cname)
        else:
          print("Status: Allies With %s" % player_Clan.Cname)
        print("=Allegiances=")
        for i in target.cats:
          print("* %s" % i)    
      elif cmd == "W" or cmd == "w":
        id = 1
        if len(warrior_code) > 0:
          for i in warrior_code:
            print("Rule %d: %s" % (id, i))
            id += 1
        else:
          print("There are no rules in the Warrior Code! ANARCHY!")
    elif cmd == "S" or cmd == "s":
      cmd = input("""Please enter the ID of the file you would like to save on:
      
      SAVE [1]
      
      SAVE [2]
      
      SAVE [3]
      
      SAVE [4]
      
      SAVE [5]
      
      SAVE [6]
      
      SAVE [7]
      
      SAVE [8]
      
      SAVE [9] | """)
      
      filename = 'save_%s.dat' % cmd
      outfile = open(filename,'wb')
      pickle.dump([player_Clan.cats, all_Clans.clans, moon, quarter_moon, day, turns, social_turns, lives, communer], outfile)
      outfile.close()
    elif cmd == "E" or cmd == "e":
      print("Come back soon, great leader!")
      main_menu(time_span, player_Clan, communer, mobile_friendly)
    if turns == 0:
      print("It's time for your cats to feast! Your current number of feedings is %d." % (player_Clan.Cprey))
      for i in player_Clan.cats:
        player_Clan.Cprey -= player_Clan.cats[i].feeding
        if player_Clan.cats[i].rank == "apprentice" and player_Clan.cats[i].age >= 12:
          rando = (random.randint(1, 2))
          if rando == 1:
            print("%s has been promoted to warrior!" % player_Clan.cats[i].name)
            player_Clan.cats[i].suffix = input("What suffix will you give them, based on their virtues? | ")
            player_Clan.cats[i].name = player_Clan.cats[i].prefix + player_Clan.cats[i].suffix
            player_Clan.cats[i].rank = "warrior"
            print("Their new name is %s." % player_Clan.cats[i].name)
        elif player_Clan.cats[i].rank == "medicine apprentice" and player_Clan.cats[i].suffix == "paw":
          rando = (random.randint(1, 4))
          if rando == 1:
            print("%s has been given a full name by StarClan!" % player_Clan.cats[i].name)
            player_Clan.cats[i].suffix = (random.choice(suffixes))
            player_Clan.cats[i].name = player_Clan.cats[i].prefix + player_Clan.cats[i].suffix
            print("Their new name is %s." % player_Clan.cats[i].name) 
        elif player_Clan.cats[i].rank == "warrior" and player_Clan.cats[i].age >= 70:
          rando = (random.randint(1, 4))
          if rando == "1":
            print("%s has retired." % player_Clan.cats[i].name)
            player_Clan.cats[i].rank = "elder"
        elif player_Clan.cats[i].rank == "kit" and player_Clan.cats[i].age >= 6:
            player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
            while player_Clan.cats[player_Clan.cats[i].mentor].rank == "kit" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "apprentice" or player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine apprentice":
              player_Clan.cats[i].mentor = (random.choice(list(player_Clan.cats.keys())))
            print("%s has become an apprentice! Their mentor is %s." % (player_Clan.cats[i].name, player_Clan.cats[player_Clan.cats[i].mentor].name))
            if player_Clan.cats[player_Clan.cats[i].mentor].rank == "medicine cat":
              player_Clan.cats[i].rank = "medicine apprentice"
            else:
              player_Clan.cats[i].rank = "apprentice"
            player_Clan.cats[i].suffix = "paw"
            player_Clan.cats[i].name = player_Clan.cats[i].prefix + player_Clan.cats[i].suffix
            if not player_Clan.cats[i].Aparent == "unknown" and not player_Clan.cats[i].Bparent == "unknown":
              for a in player_Clan.cats:
                if a.name == player_Clan.cats[i].Aparent and a.isqueen == True:
                  a.isqueen = False
                elif a.name == player_Clan.cats[player_Clan.cats[i].Bparent] and a.isqueen == True:
                  a.isqueen = False
        elif player_Clan.cats[i].age >= 80:
            rando = (random.randint(1, 9))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 90:
            rando = (random.randint(1, 8))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 100:
            rando = (random.randint(1, 7))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 110:
            rando = (random.randint(1, 6))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 120:
            rando = (random.randint(1, 5))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 130:
            rando = (random.randint(1, 4))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 140:
            rando = (random.randint(1, 3))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 150:
            rando = (random.randint(1, 2))
            if rando == 1:
              dead_guy = i
              lives = death(player_Clan, lives, dead_guy)
        elif player_Clan.cats[i].age >= 160:
          dead_guy = i
          lives = death(player_Clan, lives, dead_guy)
      print("Now you have %d feedings." % round(player_Clan.Cprey))
      if player_Clan.Cprey < 0:
        dead_guy = (random.choice(list(player_Clan.cats.keys())))
        lives = death(player_Clan, lives, dead_guy)
      if time_span == "day":
        day += 1
        if day >= (random.randint(29, 31)):
          day = 0
          moon += 1
          print("Now it is time for the gathering.")
          for i in all_Clans.clans:
            clan = i
            clan.Cpower += 20
            lives = random_event(player_Clan, clan, lives, communer)
        else:
          rando = (random.randint(1, 4))
          if rando == 1:
            clan = player_Clan
            lives = random_event(player_Clan, clan, lives, communer)
      elif time_span == "quarter_moon":
        quarter_moon += 1
        if quarter_moon >= (random.randint(3, 5)):
          quarter_moon = 0
          moon += 1
          print("Now it is time for the gathering.")
          for i in all_Clans.clans:
            clan = i
            clan.Cpower += 20
            lives = random_event(player_Clan, clan, lives, communer)
        else:
          rando = (random.randint(1, 2))
          if rando == 1:
            clan = player_Clan
            lives = random_event(player_Clan, clan, lives, communer)
      else:
        moon += 1
        print("Now it is time for the gathering.")
        for i in all_Clans.clans:
          clan = i
          clan.Cpower += 20          
          lives = random_event(player_Clan, clan, lives, communer)
      turns = 3
      social_turns = 3
      print("%s: %s- %s and %s %s %s" % (player_Clan.cats["leader"].rank,player_Clan.cats["leader"].name, player_Clan.cats["leader"].size, player_Clan.cats["leader"].build, player_Clan.cats["leader"].coat, player_Clan.cats["leader"].pronoun))
      print("%s: %s- %s and %s %s %s" % (player_Clan.cats["deputy"].rank, player_Clan.cats["deputy"].name, player_Clan.cats["deputy"].size, player_Clan.cats["deputy"].build, player_Clan.cats["deputy"].coat, player_Clan.cats["deputy"].pronoun))
      print("%s: %s- %s and %s %s %s" % (player_Clan.cats["medicine_cat"].rank, player_Clan.cats["medicine_cat"].name, player_Clan.cats["medicine_cat"].size, player_Clan.cats["medicine_cat"].build, player_Clan.cats["medicine_cat"].coat, player_Clan.cats["medicine_cat"].pronoun))
      for i in player_Clan.cats:
        player_Clan.cats[i].age += 1
      for i in player_Clan.cats:
       if player_Clan.cats[i].rank == "medicine apprentice":
         print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
      for i in player_Clan.cats:          
       if player_Clan.cats[i].rank == "warrior":
         print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
      for i in player_Clan.cats:
       if player_Clan.cats[i].rank == "apprentice":
         print("%s: %s- %s and %s %s %s (mentor, %s)" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun, player_Clan.cats[player_Clan.cats[i].mentor].name))
      for i in player_Clan.cats:
       if player_Clan.cats[i].rank == "elder":
         print("%s: %s- %s and %s %s %s" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
      for i in player_Clan.cats:
       if player_Clan.cats[i].isqueen == True:
         print("queen: %s- %s and %s %s %s" % (player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
      for i in player_Clan.cats:
       if player_Clan.cats[i].rank == "kit":
         if player_Clan.cats[i].Aparent == "unknown":
            print("%s: %s- %s and %s %s %s (parents: unknown)" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun))
         else:
            print("%s: %s- %s and %s %s %s (parents: %s and %s)" % (player_Clan.cats[i].rank, player_Clan.cats[i].name, player_Clan.cats[i].size, player_Clan.cats[i].build, player_Clan.cats[i].coat, player_Clan.cats[i].pronoun, player_Clan.cats[i].Aparent, player_Clan.cats[i].Bparent))
      for i in all_Clans.clans:
        print("%s Power: %d" % (i.Cname, i.Cpower))

# The Actual Game

#maintenance()

cmd = input("Hey there! Before we begin, would you like to turn 'mobile friendly' mode on? This will remove any fancy text or sprites from the game, to make it, well... 'mobile friendly'. [Y]/[N]")

if cmd == "Y" or cmd == "y":
  mobile_friendly = True
else:
  mobile_friendly = False

game = True

while game == True:

  main_menu(time_span, player_Clan, communer, mobile_friendly)

  print("Unfortunately, despite your best efforts...")
  print("The Clan could not withstand the fierce wilderness...")
  print("And disbanded.")
  print("Sending you back to main menu...")




