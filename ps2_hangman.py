#Proble set - 2
#name -Sheetal kumari
#time spent - 2 days


import random
                    
 
name = input("ਤੁਹਾਡਾ ਨਾਮ ਕੀ ਹੈ ")
                                     #  enter the name 
 
print("ਵਾਹਿਗੁਰੂ ਜੀ ਦਾ ਖਾਲਸਾ ਵਾਹਿਗੁਰੂ ਜੀ ਦੀ ਫਤਿਹ ! ", name)
print("ਵਾਹਿਗੁਰੂ ਜੀ ਮੇਹਰ ਕਰੀ")
 
words = ['game', 'copy', 'pen', 'laptop','program', 'english', 'juice', 'tree','car', 'rose', 'colors',] 
        
 

                              
word = random.choice(words)     
 
 
print("ਸ਼ਬਦਾਂ ਦਾ ਅਨੁਮਾਨ ਲਗਾਓ")
 
guesses = ''
 
                
turns = 12              
 
 
while turns > 0:
     
                         
    failed = 0
     
                         
    for char in word:
         
                                
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
                                 
            failed += 1
             
 
    if failed == 0:
                              
        print("ਤੁਸੀਂ ਜੇਤੂ ਹੋ")         #you are the winner
         
        
        print("ਸ਼ਬਦ ਹੈ ", word)    # this is the  correct word
        break
     
    
    guess = input("ਸ਼ਬਦਾਂ ਦਾ ਅਨੁਮਾਨ ਲਗਾਓ") # guess the characters
     
    
    guesses += guess
     
    
    if guess not in word:
         
        turns -= 1
         
        
        print("ਤੁਸੀ ਗਲਤ ਹੋ")    #you are wrong
         
    
        print("ਤੁਹਾਡੇ ਕੋਲ ਹੈ", + turns, 'ਹੋਰ ਅਨੁਮਾਨ')
         
         
        if turns == 0:
            print("ਤੁਸੀਂ ਹਾਰ ਗਏ ਹੋ") #you are looser
