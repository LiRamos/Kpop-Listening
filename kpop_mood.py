lissette_sad = input("Is Lissette sad? Please type 'yes' or 'no'.")
food_sadness = input("Is she sad because she is hungry? Please type 'yes' or 'no'.")
lissette_project = input("Do you have a project you should be doing for school Please type 'yes' or 'no'.")
work_rough = input("Was today a rough day at work for Lissette? Please type 'yes' or 'no'.")
music_mixing = input("Does she feel like mixing today? Please type 'yes' or 'no'.")
print("So, should you watch a KPop video?")
if  lissette_project == 'yes':
    print("Work on your project.")
elif lissette_sad == 'yes' and food_sadness == 'yes':
    print("You're hungry, friend. Get some food.")  

elif  lissette_sad == 'yes' and food_sadness == 'no':   
      print("OK, go watch a KPop video")   
elif lissette_sad == 'yes' and (work_rough == 'yes' and music_mixing == 'no'):
     print("Yes, go watch some KPop to cheer you up")
elif lissette_sad == 'yes' and (lissette_project == 'yes' or food_sadness =='yes'):

     print("If you're hungry, go eat food first, if you have work to do, you can only watch one KPop video, then work on your project.") 
elif lissette_project == 'yes' and lissette_sad == 'yes':
    print("Watch one video, then work on your project")
elif lissette_sad == 'yes' and (work_rough == 'yes' and music_mixing == 'yes'):
    print("Try mixing some music then, it will probably cheer you up more.")
else:       

    print("You may watch a KPop video")
def kpop_music(): #Defining Python function
    mood = input("What is your mood? Please type 'happy' , 'sad', or 'tired' Song choices according to your mood will be displayed") #User picks their mood out of the options given.
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