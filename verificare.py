
# while True:
#     intrebare = input("Hei! Da-mi un numar de la 3 la 10 (sau scrie 'stop'): ")

#     if intrebare.lower() == "stop":
#         print("Paa! 👋")
#         break

#     if not intrebare.isdigit():
#         print("❌ Te rog sa introduci un numar valid!")
#         continue

#     numar = int(intrebare)

#     if numar < 3 and numar > 10:
#         print("⚠️ Te rog scrie un numar intre 3 si 10!")
#         continue

#     for i in range(numar, 0, -1):
#         print(i)

#     print("Start! 🚀\n")


# #Exercitiul 3
# scor = int(input("Ce scor ai obtinut? "))

# if scor > 5:
#     print("Bravo!")

# elif scor >= 4:
#     print("Aproape!")
# else:
#     print("Mai incearca!")  
import turtle
ecran = turtle.Screen()                                                                                                                                                                                        
t = turtle.Turtle()                                                                                                                                                                                            
t.shape("turtle")                                                                                                                                                                                              
t.color("blue")                                                                                                                                                                                                
while True:                                                                                                                                                                                                    
    turtle.clear()                                                                                                                                                                                             
    for i in range(4):                                                                                                                                                                                         
        turtle.forward(100)                                                                                                                                                                                    
        turtle.left(10)                                                                                                                                                                                        
        break                                                                                                                                                                                                  
    turtle.left(20)                                                                                                                                                                                                                                                                                                                                                                                        
turtle.bye()()