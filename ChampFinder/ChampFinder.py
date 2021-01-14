
def yes(question):
  print(question)
  inp = input()
  return inp.upper() == "Y" or inp.upper() == "YES" or inp.upper() == "YEET" or inp.upper() == "YES MA'AM"

while True:
  champ = None
  
  #Family 1: Single player
  if yes("Is League of Legends a single player game?"):       
    elif yes("And pressing 'R' is a cheat code that makes it so you can't die?"):
      champ = "Tryndamere"
    else:
      champ = "Yorick"
      
  #Family 2: Shielders and Healers
  elif yes("Do you want an ability that shields or heals an ally?"):
    if yes("So you just want to be a No-damage Nancy?"):
      if yes("And then fuck over all your allies with your ultimate?"):
        champ = "Bard"
      elif yes("Have you ever catfished someone?"):
        champ = "Tahm Kench"
      elif yes("Is it better to have hair on your head than on your upper lip?"):
        champ = "Taric"
      else:
        champ = "Braum"
    elif yes("Do you want to mess people up at close range?"):
      if yes("You like kickin' shit?"):
        champ = "Lee Sin"
      elif yes("Do you spend 95% of the game watching your allies' screens instead of your own?"):
        champ = "Shen"
      elif yes("You like getting bonus range, damage, and AOE on your basic attacks, and becoming an unkillable late-game god?"):
        champ = "Kayle"
      else:
        champ = "Rakan"
    elif yes("Do you want to follow your champion on Twitter?"):
      champ = "Seraphine"
    elif yes("Ultimates are cool, right?"):
      if yes("Yeah, like shooting a GIANT laser through everyone?"):
        if yes("And for some reason the laser also heals your allies?"):
          champ = "Senna"
        else:
          champ = "Lux"
      elif yes("What about one that PUSHES THE WHOLE ENEMY TEAM BACK A LITTLE BIT!?!?"):
        champ = "Janna"
      elif yes("What about one that PULLS THE WHOLE ENEMY TEAM IN A LITTLE BIT!?!?"):
        champ = "Orianna"
      elif yes("Do you like to make your allies super speedy?"):
        if yes("Are you a creepy clock guy?"):
          champ = "Zilean"
        elif yes("Do you like turning people into squirrels?"):
          champ = "Lulu"
        elif yes("Do you want to also watch and movie and build a desk while you play?"):
          champ = "Yuumi"
        elif yes("Do you like having to aim your abilities?"):
          champ = "Nami"
        else:
          champ = "Sona"
      elif yes("72 hours is a reasonable stun duration?"):
        champ = "Morgana"
      else:
        champ = "Soraka"
    else:
      champ = "Karma"

  #Family 3: Ranged Top Laners
  elif yes("Do you need to be ranged vs melee to win the top lane?"):
    if yes("Do you want to suck even after winning lane?"):
      if yes("While you suck, do you you want to have six abilities?"):
        champ = "Jayce"
      else:
        champ = "Kennen"
    elif yes("Do leavers make you...mega upset?"):
      champ = "Gnar"
    elif yes("Is your character a hot chick?"):
      champ = "Vladimir"
    else:
      champ = "Quinn"

  #Family 4: Hookers
  elif yes("Are you a hooker?"):
    if yes("But are you more than just a hooker?"):
      if yes("Are you racing to get 20 kills as a huge 'fuck you' to your shitty ADC?"):
        champ = "Pyke"
      elif yes("Do you want to say 'BEEP BEEP BEEP BEEP' when you cast your ultimate?"):
        champ = "Nautilus"
      else:
        champ = "Thresh"
    else:
      champ = "Blitzcrank"

  #Family 5: Ammo bois
  elif yes("Do you think reloading ammo is a fun and exiting game mechanic?"):
    if yes("Do you think gaining temporary armor is a fun and exicting game mechanic?"):
      champ = "Graves"
    else:
      champ = "Jhin"

  #Family 6: Invisible 
  elif yes("Do you need to be invisible to get a kill?"):
    if yes("Do you also need to have 2 copies of yourself to get a kill?"):
      champ = "Shaco"
    elif yes("Are mushrooms your favorite pizza topping?"):
      champ = "Teemo"
    elif yes("For the few moments when you are visible, you want to be sexy, right?"):
      champ = "Twitch"
    else:
      champ = "Evelynn"

  #Family 7: Sustained ranged damage
  elif yes("Is 'sustained ranged DPS' a panty-dropper for you?"):
    if yes("Is it a double-panty-dropper if it's Magic Damage?"):
      if yes("Do you want a wrist injury after one game?"):
        champ = "Cassiopoeia"
      elif ("Are you scared of planes?):
        champ = "Azir"
      else:
        champ = "Corki"
    elif yes("Are you so bad at skillshots that you need one that goes through the minions?"):
      if yes("And defensive abilities are for pussies, right?"):
        if yes("But at least when you die, you have a back-up plan, right?"):
          champ = "Kog'Maw"
        elif yes("You're gonna lose all your stacks when you die, aren't you?"):
          champ = "Draven"
        else:
          champ = "Varus"
      elif yes("Is it your first time playing League of Legends?"):
        if yes("Is it your first time playing any video game?"):
          champ = "Caitlyn"
        else:
          champ = "Sivir"
      else:
        champ = "Xayah"
    elif yes("Global ults, am I right?"):
      if yes("And spamming skillshots?"):
        champ = "Ezreal"
      elif yes("What about chompy bois?"):
        champ = "Jinx"
      else:
        champ = "Ashe"
    elif yes("Do you want every auto-attack to feel like a chore?"):
      champ = "Kalista"
    elif yes("Wait, you aren't the physical manifestation of life and death, are you?"):
      champ = "Kindred"
    elif yes("Wait, you aren't the physical manifestation of me throwing my computer out the window, are you?"):  
      champ = "Vayne"
    elif yes("Do you like boobs?"):
      if yes("Do you like boobs that are even bigger than Kai'Sa's boobs?"):
        champ = "Miss Fortune"
      else:
        champ = "Kai'Sa"
    elif yes("Do you want like, 5 different weapons, and 7 hats, and 9 belts or something?"):
      champ = "Aphelios"
    elif yes("Do you want to bounce around like a kangaroo on speed?"):
      champ = "Tristana"
    else:
      champ = "Lucian"

  #Family 8: Samira
  elif yes("That was the ADC section, but Samira is the only dedicated bot-laner that doesn't have sustained long range DPS, so are you Samira?"):
    champ = "Samira"
            
  #Family 9: Point-and-click CC
  elif yes("Do you have 'I <3 Point-and-Click CC' tattooed on your ass?"):
    if yes("Do you at least want some damage?"):
      if yes("Do you like teleporting?"):
        if yes("Are you going to make the rest of your team like telepoting, too?"):
          champ = "Ryze"
        else:
          champ = "Twisted Fate"
      elif yes("Okay, but jumping to other lanes is basically teleporting. Do you want to do that?"):
        champ = "Pantheon"
      elif yes ("Would Riot make a champion that has point-and-click hard CC AND damage AND some bullshit spell shield thing?"):
        champ = "Malzahar"
      elif yes("Would you put your own balls in an ice bath if it would make you invulnerable?"):
        champ = "Lissandra"
      else:
        champ = "Annie"
    elif yes("Have you ever wished you were a tractor?"):
      champ = "Skarner"
    else:
      champ = "Jarvin IV"

  #Family 10: No skill Assassins
  elif yes("Do you want a midlane assassin but are tired of using skill?"):
    if yes("What about just ONE single skillshot?"):
      champ = "Diana"
    else:
      champ = "Talon"

  #Family 11: Mobile Mid-laners
  elif yes("Are you a midlaner who spams dashes, dodges, and blinks, wastes half their damage, then types 'outplayed' in all chat?"):
    if yes("Does outplaying mean pressing W whenever you are out of position?")
      champ = "Akali"
    elif yes("Does outplaying mean throwing your ultimate anywhere in the jungle and still hitting everyone?"):
      champ = "Qiyana"
    elif yes("Does outplaying mean pressing R because you fucked up the engage?"):
      champ = "Ekko" 
    elif yes("Does outplaying mean standing behind a windwall until Gragas knocks an enemy airborne?"):
      champ = "Yasuo"       
    elif yes("May we add some CC to your already high damage, high mobility champion?"):
      if yes("May we add some tankiness as well, thus removing all weakness?"):
        if yes("Well this just sounds like Yasuo?"):
          champ = "Yone"
        if yes("Do you want your mobile, high-damage, tanky champion with CC to also have 5 ultimates?"):
          champ = "Sylas"
        else:
          champ = "Irelia"       
      elif yes("Does your dream girls have 9 thick, hairy tails?"):
        champ = "Ahri"
      elif yes("Does she have no genitalia and a trident?"):
        champ = "Fizz"
      else:
        champ = "LeBlanc"     
    elif yes("Do you want your champion to be useful before 30 minutes?"):
      elif yes("Is picking shit up off the ground an exciting game mechanic?"):
        champ = "Katarina"
      else:
        champ = "Zed"
    else:
      champ = "Kassadin"

  #Family 12: Immobile Midlaners
  elif yes("Are you a midlaner who types 'Look at my damage!' in post-game lobby even though you died 12 times?"):
    if yes("Are you 'that guy' who always has to play the most obscure character?"):
      champ = "Aurelion Sol"
    elif yes("Do you wanna be a spooky guy with a broken, no-skill ultimate?"):
      if yes("A short spooky guy?"):
        champ = "Veigar"
      elif yes("A skinny spooky guy?"):
        champ = "Fiddlesticks"
      else:
        champ = "Karthus"
    elif yes("Can you cope with the fact that some of your abilities may not do damage?"):   
      if yes("Do you want an ultimate that takes you somewhere else?"):
        if yes("But like, where it takes you is right next to you, and even if you're like 'Wow, I like it here', you can't stay there?"):
          champ = "Zoe"
        else:
          champ = "Taliyah"
      elif yes("Is Articuno your favorite Pokemon?"):
        champ = "Anivia"
      elif yes("Do you hate wondering which items to buy?"):
        champ = "Viktor"
      elif yes("Are you basically just Lux?"):
        champ = "Neeko"
      else:
        champ = "Zyra"
    elif yes("Would Riot really make a champion that has FOUR damaging abilities AND is tanky?"):
      champ = "Swain"
    elif yes("Do you want 75% of your damage to just be on a point-and-click?"):
      if yes("Are you at least wearing a shirt?"):
        champ = "Syndra"
      else:
        champ = "Brand"
    elif yes("Do you have strong feelings about turrets, either love or hate?"):
      if yes("Do you love turrets?"):
        champ = "Heimerdinger"
      else:
        champ = "Ziggs"
    elif yes("Are you aiming for enemies that are even on your screen?"):
      champ = "Vel'Koz"
    else:
      champ = "Xerath"
            
  #Family 13: Rides on some Monsters Inc critter shit
  elif yes("Do you riding on some Monsters Inc critter shit?"):
    if yes("You rather ride on Sully from Monsters Inc than Randall from Monsters Inc?"):
      champ = "Nunu"
    else:
      champ = "Kled"

  #Family 14: Top lane Carries
  elif yes("Do you want to snowball two kills in the top lane into being an unstoppable pentakill machine?"):
    if yes("And by pentakill machine, do you mean, tenta-kill machine?"):
      champ = "Illaoi"
    elif yes("Do you want to snowball your pentakill into a game loss for your team?"):
      champ = "Fiora"
    elif yes("Do you plan to get the pentakill by running away in the shape of a dick and balls?"):
      champ = "Singed"
    elif yes("Will any of your kills take place in a death arena of some sort?"):
      if yes("A hexagonal one?"):
        champ = "Camille"
      else:
        champ = "Mordekaiser"
     elif yes("Does winning require spinning?"):
      if yes("One day humans will go extinct. Animals, creatures of raw beauty and brawn, will then rise and once again dominate the Earth?"):
        if yes("Did you just pick the character that looks the coolest? What are you, 9 years old?):
          champ = "Renekton"
        else:
          champ = "Wukong"
      elif yes("If Riot made a champion that was a copy of Garen, would you prefer it to Garen?"):
        champ = "Darius"
      else:
        champ = "Garen"
    elif yes("Do you like to stun people?"):
      if yes("By being really, really, ridculously good looking?"):
        champ = "Sett"
      elif yes("Do you cancel animations like they're season 2 of No Game; No Life?"):
        champ = "Riven"
      else:
        champ = "Volibear"
    elif yes("Pharaoh doge wants a Scooby-stack?"):
      champ = "Nasus"
    elif yes("Do you love lamp?"):
      champ = "Jax"
    elif yes("Do you have a kink for legs?"):
      champ = "Urgot"
    elif yes("Is your champion just the hamster version of Doctor Eggman from Sonic?"):
      champ = "Rumble"
    elif yes("Can an orange bring you home from the Death Realm?"):
      champ = "Gangplank"
    else:
      champ = "Aatrox"

  #Family 15: Meatballs
  elif yes("Does the term 'scarifical meatball' mean anything to you?"):
    if yes("Do you want a big AoE ultimate?"):
      if yes("With you in the center?"):
        if yes("Are you green?"):
          if yes("And short?"):
            if yes("And Bowser's son?"):
              champ = "Rammus"
            else:
              champ = "Amumu"
          else:
            champ = "Zac"
        elif: yes("Do you have any non-ultimate abilities?"):
          champ = "Galio"
        else:
          champ = "Malphite"  
      elif yes("Do you want a hammer for a weapon?"):
        if yes("And a moustache for an even deadlier weapon?"):
          champ = "Ornn"
        else:
          champ = "Poppy"
      elif yes("Do you want a sword for a weapon?"):
        champ = "Leona"
      elif yes("Do you want soft, supple, tree bark for a weapon?"):
        champ = "Maokai"
      else:
        champ = "Sion"
    elif yes("Do you want a big single target ultimate?"):
      if yes("Do you like to emasculate your jungler by eating every large objective?"):
        champ = "Cho'Gath"
      else:
        champ = "Sejuani"
    elif yes("Do you want Dr. Mundo's ultimate?"):
      champ = "Dr. Mundo"
    else:
      champ = "Alistar"
  
  #Family 16: Chaser Downers
  elif yes("Are you a master chaser downer?"):
    if yes("Projectiles are for pussies?"):
      if yes("Scythes are for pussies?"):
        if yes("Swords are for pussies?"):
          if yes("Gauntlets are for pussies?"):
            if yes("Abiltiies are for pussies?"):
               champ = "Udyr"
            else:
               champ = "Warwick"
          else:
            champ = "Vi"
        else:
          champ = "Master Yi"
      elif("Can you step into walls like Danny Phantom?")
        champ = "Kayn"
      else:
        champ = "Hecarim"            

    elif yes("Does your champion evolve like a Pokemon?"):
      champ = "Kha'Zix"
    elif yes("Is your Pokemon Ghost type?):
       champ = "Nocturne"
    elif yes("Does your Pokemon rhyme with 'Gengar'?"):      
      champ = "Rengar"
    elif yes("Does your Pokemon know TM28 - Dig?"):
        champ = "Rek'sai"          
    elif yes("I'm starting to think you're not a Pokemon. Are you more like a hot centaur anime chick in a movie about preserving the environment?"):
      champ = "Lillia"        
    else:
      champ = "Olaf"

  #Family 17: Leftovers
  elif yes("So, you made it all the way here, to the generic champs that aren't very interesting. Errr, I mean...the very special unique champs. Hey, magnets are cool, right?"):
    champ = "Rell"                     
  elif yes("Did you complete the 'Pacifist' route in Undertale?"):
    champ = "Ivern"             
  elif yes("Do you want a dragon Animorph?"):
    champ = "Shyvana"
  elif yes("Do you want a spider Animorph?"):
    champ = "Elise"
  elif yes("Do you want a cougar Animorph?"):
    champ = "Nidalee"
  elif yes("Seriously, isn't there anything interesting about your champion? Do you at least have an exciting ultimate?"):
    champ = "Gragas"
  elif yes("Or maybe an ability that alters the terrain or something?"): 
    champ = "Trundle"
  else:
    champ = "Xin Zhao"

  print("\n\nYour dream LoL champion is... " + champ + "!")
  print("Type 's' to start over, 'q' to quit")
  inp = input()
  if inp.upper() == 'Q' or inp.upper() == 'QUIT':
    break
