# animal_game
A different version of the Pokemon game 
Link to Pokemon Game and Project Brief: https://github.com/ShekinahBa/pokemon/tree/main

After coding the pokemon game myself out of pure excitement, I remembered this was a group project! The team decided to take the project in a different direction to make it more exciting and change the project to an animal game.

This was a great opportunity to work with a team and also fix some mistakes/bad practice that I had in my pokemon project. I had reached out to 2 amazing developers who immediately spotted a few of my sins which I've outlined bellow.

I learn a lot working in a team, most importantly I learnt the importance of working with Git because we definately encounted some problems cycling through different solutions such as co-lab, Notion and even google docs! I also learnt the importance of TESTING! The code might not break but is it really doing what you it's suppose to? So, Test Driven Development (TDD) is coming up soon in the cirriculum I created for myself.


Bad Practice I fixed from the Pokemon game:
1) Using global variables which is kind of okay for small self contained program
2) Breaking the "DRY RULE" (Don't Repeat Yourself)

Global Variable: To fix the the global variable issue, I just had to find a better way of putting the parts together 

DRY: To fix repeating this block of code :

 print("Pokemon Names and Stats")
  
    print("Pokemon Names and Stats")
    print("1: {:12} -> Height: {:2}, Weight: {:2} ".format(option1['name'].upper(),option1['height'],option1['weight'] ))
    print("2: {:12} -> Height: {:2}, Weight: {:2} ".format(option2['name'].upper(), option2['height'], option2['weight']))
    print("3: {:12} -> Height: {:2}, Weight: {:2} ".format(option3['name'].upper(), option3['height'], option3['weight']))
    print("4: {:12} -> Height: {:2}, Weight: {:2} ".format(option4['name'].upper(), option4['height'], option4['weight']))
    print("5: {:12} -> Height: {:2}, Weight: {:2} ".format(option5['name'].upper(), option5['height'], option5['weight']))
    
I used loops instead:

    for i in animal_dict:
        print('Option {}: {:20} -> Speed: {:5}, Weight: {:6}, Size {:5}'.format(numbers, animal_dict[i]['name'],
                                                                                animal_dict[i]['speed'],
                                                                                animal_dict[i]['weight'],
                                                                                animal_dict[i]['size']))
                                                                                
                                 
                                                                                
 So much better right? (Thank you Alex!) 

 
 There are many things I could do to continue improving this project like adding a leaderboard and working with Pandas but I would like to choose a project of my own that's a bit more challenging. So keep an eye out
                                                                            
