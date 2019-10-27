user_sad = input("Are you sad? Please type 'yes' or 'no'.\n")
food_sadness = input("Are you sad because you are hungry? Please type 'yes' or 'no'.\n")
current_project = input("Do you have a project you should be doing for school Please type 'yes' or 'no'.\n")
work_rough = input("Was today a rough day at work for  you? Please type 'yes' or 'no'.\n")
music_mixing = input("Do you feel like mixing today? Please type 'yes' or 'no'.\n")
print("So, should you watch a KPop video?\n")
if  current_project == 'yes':
    print("Work on your project.\n")
elif user_sad == 'yes' and food_sadness == 'yes':
    print("You're hungry. Get some food.\n")  

elif  user_sad == 'yes' and food_sadness == 'no':   
      print("OK, go watch a KPop video\n")   
elif user_sad == 'yes' and (work_rough == 'yes' and music_mixing == 'no'):
     print("Yes, go watch some KPop to cheer you up\n")
elif user_sad == 'yes' and (current_project == 'yes' or food_sadness =='yes'):
    print("If you're hungry, go eat food first, if you have work to do, you can only watch one KPop video, then work on your project.\n") 
elif current_project == 'yes' and user_sad == 'yes':
    print("Watch one video, then work on your project\n")
elif user_sad == 'yes' and (work_rough == 'yes' and music_mixing == 'yes'):
    print("Try mixing some music then, it will probably cheer you up more.\n")
else:       
    print("You may watch a KPop video\n")
def kpop_music(): #Defining Python function
    mood = input("What is your mood?\nPlease type 'happy' , 'sad', or 'tired'\nSong choices according to your mood will be displayed.\n") #User picks their mood out of the options given.
    mood_music = {
    "happy" : "'Wolf' by EXO, 'Running to You' by SVT, 'Go Go' by BTS, 'Into The New World' by SNSD", 
    "sad" : "'Don't Wanna Cry Acoustic Version' by SVT, 'Spring Day' by BTS, 'Breathe' by Lee Hi",
    "tired" : " 'CLAP' by SVT, 'Mic Drop' by BTS,'Rising Sun' TVXQ"
}#Dictionary holding recommendations of kpop music based on mood. 
    if mood == "happy":
       print (mood_music.get("happy", None)) #Gets the values of whichever key that the user types in
    if mood == "sad":
       print( mood_music.get("sad",  None))
    if mood == "tired":
      print(mood_music.get("tired",  None))
kpop_music()
