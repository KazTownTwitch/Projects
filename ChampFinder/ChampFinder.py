
def yes(question):
  print(question)
  inp = input()
  return inp.upper() == "Y" or inp.upper() == "YES" or inp.upper() == "YEET" or inp.upper() == "YES MA'AM"

while True:
  champ = None
  if yes("Do you want to play with other people?"):
    if yes("Do you want a champion with at least one ability that you have to aim?"):
      
      #Family 1: Shielders and Healers
      if yes("Do you want an ability that shields or heals an ally?"):
        if yes("Would you give your entire dick for your allies?"):
          if yes("And then fuck over all your allies with your ultimate?"):
            champ = "Bard"
          elif yes("Have you ever catfished someone?"):
            champ = "Tahm Kench"
          elif yes("Is it better to have hair on your head than on your upper lip?"):
            champ = "Taric"
          else:
            champ = "Braum"
        elif yes("Do you want to fuck people up at close range?"):
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
          elif yes("What about one that pushes the WHOLE ENEMY TEAM BACK A LITTLE BIT!?!?"):
            champ = "Janna"
          elif yes("What about one that pulls the WHOLE ENEMY TEAM IN A LITTLE BIT!?!?"):
            champ = "Orianna"
          elif yes("Do do you want an ablity that can make an ally fasty fast?"):
            if yes("Are you a creepy clock guy?"):
              champ = "Zilean"
            elif yes("Do you like turning people into squirrels?"):
              champ = "Lulu"
            elif yes("Do you want to also watch and movie and build a desk while you play?"):
              champ = "Yuumi"
            elif yes("Do you like targetting your abilities?"):
              champ = "Nami"
            else:
              champ = "Sona"
          elif yes("72 hours is a reasonable stun duration?"):
            champ = "Morgana"
          else:
            champ = "Soraka"
        else:
          champ = "Karma"
      
      #Family 2: Ranged Top Laners
      elif yes("Do you need to be ranged vs melee to win the top lane?"):
        if yes("Do you want to suck even after winning lane?"):
          if yes("While you suck, do you you want to have six abilities?"):
            champ = "Jayce"
          else:
            champ = "Kennen"
        elif yes("Do leavers make you...mega upset?"):
          champ = "Gnar"
        else:
          champ = "Quinn"
      
      #Family 3: Hookers
      elif yes("Are you a hooker?"):
        if yes("But are you more than just a hooker?"):
          if yes("Are you racing to get 20 kills as a huge 'fuck you' to your noob ADC?"):
            champ = "Pyke"
          elif yes("Do you want to say 'BEEP BEEP BEEP BEEP' when you cast your ultimate?"):
            champ = "Nautilus"
          else:
            champ = "Thresh"
        else:
          champ = "Blitzcrank"
      
      #Family 4: Ammo bois
      elif yes("Do you think 'ammo' is a fun and exiting game mechanic?"):
        if yes("Do you think gaining temporary armor is a fun and exicting ability?"):
          champ = "Graves"
        else:
          champ = "Jhin"
        
      #Family 5: Invisible 
      elif yes("Do you need to be invisible to get a kill?"):
        if yes("Do you also need to have 2 copies of yourself to get a kill?"):
          champ = "Shaco"
        elif yes("Are mushrooms your favorite pizza topping?"):
          champ = "Teemo"
        elif yes("But when you are visible, you want to be sexy, right?"):
          champ = "Twitch"
        else:
          champ = "Evelynn"
      elif yes("Do you need to be underground to get a kill?"):
        champ = "Rek'sai"
      elif yes("Do you need to be on a icy coating of your own creation to get a kill?"):
        champ = "Trundle"
          
      #Family 6: Sustained damage
      elif yes("Is 'sustained ranged DPS' a panty-dropper for you?"):
        if yes("Is it a double-panty-dropper if it's Magic Damage?"):
          if yes("Snakes in bras?"):
            champ = "Cassiopoeia"
          else:
            champ = "Azir"
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
        elif yes("Okay, but you want some kind of flashy ultimate right?"):
          if yes("Like, a really weird one that nobody understands even 4 years later?"):
            champ = "Kalista"
          elif yes("Wait, were you trying tp have great ranged DPS from the jungle?!?!"):
            champ = "Kindred"
          elif yes("Do you like boobs?"):
            if yes("Do you REALLY like boobs?"):
              champ = "Miss Fortune"
            else:
              champ = "Kai'sa"
          elif yes("Do you want like, 5 different weapons and 2 spells, and 4 hats, and 3 belts or something?"):
            champ = "Aphelios"
          elif yes("Do you want to bounce around like a kangaroo on speed?"):
            champ = "Tristana"
          else:
            champ = "Lucian"
        else:
          champ = "Corki"
        elif yes("Wait, so you're the only dedicated bot-laner that doesn't offer sustained ranged DPS?"):
          champ = "Samira"
            
        #Family 7: Point-and-click CC
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
              
        #Family 8: No skill Assassins
        elif yes("Do you want a midlane assassin but are tired of using skill?"):
          if yes("What about just ONE single skillshot?"):
            champ = "Diana"
          else:
            champ = "Talon"
              
        #Family 9: Hypermobile bois
        elif yes("Do you want to dance around fights and type 'outplayed'?"):
          if yes("And cancel animations like they are season 2 of No Game; No Life?"):
            champ = "Riven"
          elif yes("Does outplaying mean using at least 3 dashes or teleports per fight?"):
            if yes("Do you want to be perma-banned?"):
              if yes("Are you like Yasuo?"):
                if yes("Are you Yasuo?"):  
                  champ = "Yasuo"
                else:
                  champ = "Yone"
              else:
                champ = "Zed"
            elif yes("May we add some CC to your already high damage, high mobility champion?"):
              if yes("May we add some tankiness as well, thus removing all weakness?"):
                champ = "Irelia"
              elif yes("Does your dream girls have 9 thick, hariy, tails?"):
                champ = "Ahri"
              else:
                  champ = "LeBlanc"
            elif yes("May we add extreme scaling to your already high damage, high mobility champion?"):
              champ = "Kassadin"
            elif yes("Is picking shit up off the ground an exciting game mechanic?"):
              champ = "Katarina"
            else:
              champ = "Akali"
          elif yes("Does outplaying mean throwing your ultimate anywhere in the jungle and still hitting everyone?"):
            champ = "Qiyana"
          elif yes("Does outplaying mean pressing R because you fucked up the engage?"):
            champ = "Ekko"
          elif yes("Does outplaying mean looking like a sexy vampire while you get your pentakill?"):
            champ = "Vladimir"    
          else:
            champ = "Fizz"
              
        #Family 10: High-damage Midlaners
        elif yes("Are you a midlaner who types 'Look at my damage!' in the post game lobby even though you died 12 times?"):
          if yes("Are you 'that guy' who always has to play the most obscure character?"):
            champ = "Aurelion Sol"
          elif yes("Are you getting top damage because your opponent's ultimate looks better on you?"):
            champ = "Sylas"
          elif yes("Can you cope with the fact that some of your abilities may not do damage?"):
            if yes("Do you wanna be a spooky guy with a broken, no-skill ultimate?"):
              if yes("A short spooky guy?"):
                champ = "Veigar"
              elif yes("A skinny spooky guy?"):
                champ = "Fiddlesticks"
              else:
                champ = "Karthus"
            if yes("Do you want an ultimate that takes you somewhere else?"):
              if yes("But like, where it takes you is right next to you, and it doesn't even really take you there?"):
                champ = "Zoe"
              else:
                champ = "Taliyah"
            elif yes("Is Articuno your favorite Pokemon?"):
              champ = "Anivia"
            elif yes("Do you hate wondering which items to buy?"):
              champ = "Viktor"
            elif yes("Do you like playing dress-up?"):
              champ = "Neeko"
            else:
              champ = "Zyra"
          elif yes("Would Riot really make a champion that has FOUR damaging abilities AND is tanky?"):
            champ = "Swain"
          elif yes("So you want inifnity damage and 75% of it to be on a point-and-click?"):
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
            champ = "Vel'koz"
          else:
            champ = "Xerath"
          
          #Family 11: Top-laners
          elif yes("Do you want to snowball two kills in the toplane into an unstoppable pentakill machine?"):
            if yes("And by pentakill machine, do you mean, tenta-kill machine?"):
              champ = "Illaoi"
            elif yes("Will any of your kills take place in a death arena of some sort?"):
              if yes("A hexagonal one?"):
                champ = "Camille"
              else:
                champ = "Mordekaiser"
            elif yes("Do you like to stun people?"):
              if yes("By being really, really, ridculously good looking?"):
                champ = "Sett"
              elif yes("Are you scared of being turned into a purse one day, or perhaps a pair of fancy shoes?):
                champ = "Renekton"
              else:
                champ = "Volibear"
            elif yes("Does winning require spinning?"):
              if yes("If Riot made a champion that was a copy of Garen, would you prefer it to Garen?"):
                champ = "Darius"
              else:
                champ = "Garen"
            elif yes("Pharaoh doge?"):
              champ = "Nasus"
            else:
              champ = "Aatrox"
          elif yes("Do you want to snowball two kills in the toplane into a game loss for your team?"):
            champ = "Fiora"
          elif yes("Nothing can go wrong with a squishy, melee toplaner, right?"):
            if yes("Especially one that is very mechanically intense?"):
              champ = "Gangplank"
            else:
              champ = "Rumble"
          
          #Family 12: Chaser Downers
          elif yes("Are you a master chaser downer?"):
            if yes("And you like throwing shit at people?"):
              if yes("Do you riding on some Monsters Inc critter shit?"):
                if yes("You rather ride on Sully from Monsters Inc than Randall from Monsters Inc?"):
                  champ = "Nunu"
                else:
                  champ = "Kled"
              elif yes("Do you live for the bush?"):
                champ = "Rengar"
              else:
                champ = "Olaf"
            elif yes("Are you a scythe-y boy?"):
              if yes("And horse-y boy?"):
                champ = "Hecarim"
              else:
                champ = "Kayn"
            elif yes("You're a good boy! Yes you are! Yes you are?"):
              champ = "Warwick"
            elif yes("While running people down, do you intend to attack them at any point?"):
              if yes("And shake them like a polaroid picture?"):
                champ = "Rammus"
              else:
                champ = "Nocturne"
            else:
              champ = "Singed"
                       
          #Family 13: Meatballs
          elif yes("Does the term 'scarifical meatball' mean anything to you?"):
            if yes("Do you want a big AoE ultimate?"):
              if yes("With you in the center?"):
                if yes("Are you green?"):
                  if yes("And round?"):
                    if yes("And wrapped in toilet paper?"):
                      champ = "Amumu"
                    else:
                      champ = "Zac"
                  else:
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
              elif yes("Do you want bark for a weapon?"):
                champ = "Maokai"
              else:
                champ = "Sion"
            elif yes("Do you want a big single target ultimate?"):
              if yes("Do you want to emasculate your jungler by eating every large objective?"):
                champ = "Cho'gath"
              elif yes("Do you have a kink for legs?"):
                champ = "Urgot"
              else:
                champ = "Sejuani"
            elif yes("Do you want Dr. Mundo's ultimate?"):
              champ = "Dr. Mundo"
            else:
              champ = "Alistar"
          
          #Family 14: Miscellaneous
          elif yes("How crazy are magnets, like 'whaaaaa...', they are like magic?"):
            champ = "Rell"
          elif yes("Did you complete the 'Pacifist' route in Undertale?"):
            champ = "Ivern"
          elif yes("Your Pokemon is evolving?"):
            champ = "Kha'zix"
          elif yes("Do you want a dragon Animorph?"):
            champ = "Shyvana"
          elif yes("Do you want a spider Animorph?"):
            champ = "Elise"
          elif yes("Do you want a cougar Animorph?"):
            champ = "Nidalee"
          elif yes("Do you want to be a monkey, just a monkey, not a monkey Animorph?"):
            champ = "Wukong"
          elif yes("But you must want animal features of some kind! Junglers must have some animal feature?"):
            champ = "Lillia"
          else:
            champ = "Gragas"
                      
    #Family 15: No abilities 
    elif yes("Do you wanna go fast?"):
      if yes("Because you're a man-bear-pig?"):
        champ = "Udyr"
      elif yes("Because men can wear dresses, too?"):
        champ = "Master Yi"
      else:
        champ = "Vayne"          
    elif yes("Do you love lamp?"):
      champ = "Jax"
    else:
      champ = "Xin Zhao" 
  
  #Family 16: Single player                     
  elif yes("Other ghouls?"):
    champ = "Yorick"
  else:
    champ = "Tryndamere"

  print("\n\nYour dream LoL champion is... " + champ + "!")
  inp = ''
  while inp != "q" and inp != "s":
    print("Type 's' to start over, 'q' to quit")
    inp = input()
  if inp == 'q':
    break
