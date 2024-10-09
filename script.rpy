# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")
define a = Character("Harry")
define b = Character("Steve")

# The game starts here.
       (Testing commits 1)
(Testing commits 2)
label start:
    $ left_place = False
    $ Look_person = False
    $ ka_boom = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show hythe range 2 with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    e "You walking on the path way"

    e "After walking to the end you see a hole in the fence"

menu:  

     "What should you do?"
     
     "Go inside.":
           "You went inside"


     "Leave the place.":
         $ left_place = True
         jump ending

   # test branching  
   
scene hythe range with fade

menu:
     "What should you do now?"

     "Try to find someone":
         "You walk around and see a solider."
         $ Look_person = True
       
     "Turn around and go home":
         $ left_place = True
         jump ending

label after_menu:

     show soldierrr

     a "What are you doing here?"

     "I am trying to find the way out"
     
     a "Follow me I will show you where to go"
 
menu: 


    "Follow the soldier":
        "You followed a soldier and you came to another soldier"
        
    "Go on the land mine":
        "You stepped on a line, you are dead - good job '"
        $ ka_boom = True
        jump ending

label after_menu2:
      show soldie at right

      a "Hey Steve can you show this guy the exit"
      b "Okay Harry no problem"
      b "Hey follow me I will show you where is the exit"


      e "You followed Steve and made it to the exit safe"
              
     

label ending:
    if left_place:
        "You left the place and went home"
    else:
        "The end."
return
