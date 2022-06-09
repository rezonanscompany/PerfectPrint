from perfectprint import Screen
from perfectprint import Model
from perfectprint import Object
import time
import keyboard


# Flying peramyde, square, rectangle with colorful colors in cyan screen
def flyingShapes():
    screen = Screen(rows=40, columns=85, main_symbol="=", main_color="cyan")
    while True:
        for i in range(15):
            screen.resetScreen()
            screen.drawPyramid(7+i*2,20+i*4,5,"●","green")
            screen.drawSquare(7,4+i*4,5,"■","red")
            screen.drawRectangle(7+i*2,7,5,20,"#","blue")
            screen.update()
            time.sleep(0.06)
        for i in reversed(range(15)):
            screen.resetScreen()
            screen.drawPyramid(7+i*2,20+i*4,5,"●","green")
            screen.drawSquare(7,4+i*4,5,"■","red")
            screen.drawRectangle(7+i*2,7,5,20,"#","blue")
            screen.update()
            time.sleep(0.06)



# Flying keyboard
def flyingKeyboard():
    screen = Screen(rows=63, columns=205, main_symbol="=", main_color="cyan")
    while True:
        t = 0.05
        text = """
,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
|1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
| ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |
|-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |
| Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    |
|----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|
|    | < | Z | X | C | V | B | N | M | , | . | - |          |
|----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
| ctrl |  | alt |                          |altgr |  | ctrl |
'------'  '-----'--------------------------'------'  '------'"""
        for i in range(40): 
            screen.writeText(text,1+i,10+i,"yellow",auto_background=False,)
            screen.update()
            time.sleep(t)
        for i in range(40): 
            screen.writeText(text,41-i,50+i,"yellow",auto_background=False)
            screen.update()
            time.sleep(t)
        for i in range(40): 
            screen.writeText(text,1+i,90+i,"yellow",auto_background=False)
            screen.update()
            time.sleep(t)
        for i in range(11): 
            screen.writeText(text,41-i,130+i,"yellow",auto_background=False)
            screen.update()
            time.sleep(t)
        for i in range(30): 
            screen.writeText(text,30-i,140-i,"yellow",auto_background=False)
            screen.update()
            time.sleep(t)
        for i in range(50): 
            screen.writeText(text,1+i,110-i,"yellow",auto_background=False)
            screen.update()
            time.sleep(t)
        for i in range(50): 
            screen.writeText(text,50-i,60-i,"yellow",auto_background=False)
            screen.update()
            time.sleep(t)


def girlWar():
    screen = Screen(rows=60,columns=200,main_symbol="_",main_color="yellow")
    t = 0.05
    text = """
          .,asnnn.                     
       ,+adXXXXXXbn.                       
      ,d>XXXXXXXXXXXb.     .,an-.                   o 
       ,dXXXXXXXXXXXXPW.,adXXXXX<_               ,;;.
      ,dXXXXXXXP"'   >H*XXXXXXXXXXbn.           ,;;;
      ;XXXXXXXP    .aXXXXXXXXXXXXXX<          ,::;;
      iXXXXXXI    ;XXXXXX'I;;"XXXXXI       , ;::;'
      IXXXXXX!    'YXXXXX;....YXXXX!    ,aP ,$$$;
      IXXXXXX;      YXXXX'.,--.XXXP'   a$Y,a$$$$
     .dXXXXXX;      '"MYV.(  , YXX"  ,$$Y,d$$$$'
     ;XXXXXXX;       (@M"..`-..;YX   ^^^,d$$$P\.
     iXXXXXXX'         !.......;;      ,d$$$$.$/
    ,dXXXXXP"         ,;...,,,;;;     ($$$^^^$;
_.,aXXXYXXP'          ;'...**=-="        (::$n..
'"~*@^' "'          ,,;....;..,           ,.$$$>
                  ,'..'...."'..;.        ,..$$$'
               ,-'...;  .....;....      ,..;^^ 
              ,'......) '..,.. '...`. ,'...'
             ;.......,    ..;'  '....\....'
             '..../.,'           ;......./
            ;....;''             ;',..../
           ;....'  `.         ,,'
           ;...'     .        ;
          ;.../      )        ,
         :$n--.      ,        ;
         :oo$$'     ,an,..___,>
         :X$$,'    adHHHHHHHHHb                
         :X$$,    idHHHHHHHHHHHb                
         :$$'    ,dHHHHHHHHHHHHHi                
         ,..-.   dHHHHHHHHHHHHHHb                  
        ;.....) dHHHHHHHHHHHHHHHH.                 
         '-__; ,HHHHHHHHHYHHHHHHHb                  
               aHHHHHHHHYHHHHHHHHH;                 
               iHHHHHHP" VHHHHHHHH;                
               IHHHHHP'   VHHHHHHHi              
              aHHHHHP'     VHHHHHHI             
             dHHHHHP'       VHHHHH!            
            dHHHHHP          VHHHH;          
           dHHHHHP           dHHHH;          
          /^HHHHP           dHHHHH          
          $$$nnnd          ,HHHHHP.    
         ,$$$$$$'          i******;            
         :HHHH$"           I$$$$$"           
         :$***$            i$$==='           
         i$$$$'            :$$HHH           
         'HHHY             :$$$$;          
         I*HH"             ;$$HHH   
       ,$$$$$             ($$$***.     
      ,$$$$$$              '"$$$$$.     
     <$$$$$*                   '$$$$. 
       '""'                      '""'"""
    while True:
        for i in range(50):
            screen.writeText(text,1,140-i,color="blue",auto_background=True)
            screen.writeText(text,1,1+i,color="green",auto_background=True)
            screen.update()
            screen.resetScreen()
            time.sleep(t)
        for i in reversed(range(50)):
            screen.writeText(text,1,140-i,color="blue",auto_background=True)
            screen.writeText(text,1,1+i,color="green",auto_background=True)
            screen.update()
            screen.resetScreen()
            time.sleep(t)


def displayAllColors():
    screen = Screen(rows=37, columns=220, main_symbol="█", main_color="taupe")
    screen.drawButton(row=2,column=2,text=" amaranth ", color="amaranth",width=20)
    screen.drawButton(row=2,column=24,text=" amber ", color="amber",width=20)
    screen.drawButton(row=2,column=46,text=" amethyst ", color="amethyst",width=20)
    screen.drawButton(row=2,column=68,text=" apricot ", color="apricot",width=20)
    screen.drawButton(row=2,column=90,text=" aquamarine ", color="aquamarine",width=20)
    screen.drawButton(row=2,column=112,text=" azure ", color="azure",width=20)
    screen.drawButton(row=2,column=134,text=" babyblue ", color="babyblue",width=20)
    screen.drawButton(row=2,column=156,text=" beige ", color="beige",width=20)
    screen.drawButton(row=2,column=178,text=" brickred ", color="brickred",width=20)
    screen.drawButton(row=2,column=200,text=" black ", color="black",width=20)
    screen.drawButton(row=6,column=2,text=" blue ", color="blue",width=20)
    screen.drawButton(row=6,column=24,text=" bluegreen ", color="bluegreen",width=20)
    screen.drawButton(row=6,column=46,text=" blueviolet ", color="blueviolet",width=20)
    screen.drawButton(row=6,column=68,text=" blush ", color="blush",width=20)
    screen.drawButton(row=6,column=90,text=" bronze ", color="bronze",width=20)
    screen.drawButton(row=6,column=112,text=" brown ", color="brown",width=20)
    screen.drawButton(row=6,column=134,text=" burgundy ", color="burgundy",width=20)
    screen.drawButton(row=6,column=156,text=" byzantium ", color="byzantium",width=20)
    screen.drawButton(row=6,column=178,text=" carmine ", color="carmine",width=20)
    screen.drawButton(row=6,column=200,text=" cerise ", color="cerise",width=20)
    screen.drawButton(row=10,column=2,text=" cerulean ", color="cerulean",width=20)
    screen.drawButton(row=10,column=24,text=" champagne ", color="champagne",width=20)
    screen.drawButton(row=10,column=46,text=" chartreusegreen ", color="chartreusegreen",width=20)
    screen.drawButton(row=10,column=68,text=" chocolate ", color="chocolate",width=20)
    screen.drawButton(row=10,column=90,text=" cobaltblue ", color="cobaltblue",width=20)
    screen.drawButton(row=10,column=112,text=" coffee ", color="coffee",width=20)
    screen.drawButton(row=10,column=134,text=" copper ", color="coffee",width=20)
    screen.drawButton(row=10,column=156,text=" coral ", color="coral",width=20)
    screen.drawButton(row=10,column=178,text=" crimson ", color="crimson",width=20)
    screen.drawButton(row=10,column=200,text=" cyan ", color="cyan",width=20)
    screen.drawButton(row=14,column=2,text=" desertsand ", color="desertsand",width=20)
    screen.drawButton(row=14,column=24,text=" electricblue ", color="electricblue",width=20)
    screen.drawButton(row=14,column=46,text=" emerald ", color="emerald",width=20)
    screen.drawButton(row=14,column=68,text=" erin ", color="erin",width=20)
    screen.drawButton(row=14,column=90,text=" gold ", color="gold",width=20)
    screen.drawButton(row=14,column=112,text=" gray ", color="gray",width=20)
    screen.drawButton(row=14,column=134,text=" green ", color="green",width=20)
    screen.drawButton(row=14,column=156,text=" harlequin ", color="harlequin",width=20)
    screen.drawButton(row=14,column=178,text=" indigo ", color="indigo",width=20)
    screen.drawButton(row=14,column=200,text=" ivory ", color="ivory",width=20)
    screen.drawButton(row=18,column=2,text=" jade ", color="jade",width=20)
    screen.drawButton(row=18,column=24,text=" junglegreen ", color="junglegreen",width=20)
    screen.drawButton(row=18,column=46,text=" lavender ", color="lavender",width=20)
    screen.drawButton(row=18,column=68,text=" lemon ", color="lemon",width=20)
    screen.drawButton(row=18,column=90,text=" lilac ", color="lilac",width=20)
    screen.drawButton(row=18,column=112,text=" lime ", color="lime",width=20)
    screen.drawButton(row=18,column=134,text=" magenta ", color="magenta",width=20)
    screen.drawButton(row=18,column=156,text=" magentarose ", color="magentarose",width=20)
    screen.drawButton(row=18,column=178,text=" maroon ", color="maroon",width=20)
    screen.drawButton(row=18,column=200,text=" mauve ", color="mauve",width=20)
    screen.drawButton(row=22,column=2,text=" navyblue ", color="navyblue",width=20)
    screen.drawButton(row=22,column=24,text=" ochre ", color="ochre",width=20)
    screen.drawButton(row=22,column=46,text=" olive ", color="olive",width=20)
    screen.drawButton(row=22,column=68,text=" orange ", color="orange",width=20)
    screen.drawButton(row=22,column=90,text=" orangered ", color="orangered",width=20)
    screen.drawButton(row=22,column=112,text=" orchid ", color="orchid",width=20)
    screen.drawButton(row=22,column=134,text=" peach ", color="peach",width=20)
    screen.drawButton(row=22,column=156,text=" pear ", color="pear",width=20)
    screen.drawButton(row=22,column=178,text=" periwinkle ", color="periwinkle",width=20)
    screen.drawButton(row=22,column=200,text=" mauve ", color="mauve",width=20)
    screen.drawButton(row=26,column=2,text=" persianblue ", color="persianblue",width=20)
    screen.drawButton(row=26,column=24,text=" pink ", color="pink",width=20)
    screen.drawButton(row=26,column=46,text=" plum ", color="plum",width=20)
    screen.drawButton(row=26,column=68,text=" prussianblue ", color="prussianblue",width=20)
    screen.drawButton(row=26,column=90,text=" puce ", color="puce",width=20)
    screen.drawButton(row=26,column=112,text=" purple ", color="purple",width=20)
    screen.drawButton(row=26,column=134,text=" raspberry ", color="raspberry",width=20)
    screen.drawButton(row=26,column=156,text=" red ", color="red",width=20)
    screen.drawButton(row=26,column=178,text=" redviolet ", color="redviolet",width=20)
    screen.drawButton(row=26,column=200,text=" rose ", color="rose",width=20)
    screen.drawButton(row=30,column=2,text=" ruby ", color="ruby",width=20)
    screen.drawButton(row=30,column=24,text=" salmon ", color="salmon",width=20)
    screen.drawButton(row=30,column=46,text=" sangria ", color="sangria",width=20)
    screen.drawButton(row=30,column=68,text=" sapphire ", color="sapphire",width=20)
    screen.drawButton(row=30,column=90,text=" scarlet ", color="scarlet",width=20)
    screen.drawButton(row=30,column=112,text=" silver ", color="silver",width=20)
    screen.drawButton(row=30,column=134,text=" slategray ", color="slategray",width=20)
    screen.drawButton(row=30,column=156,text=" springbud ", color="springbud",width=20)
    screen.drawButton(row=30,column=178,text=" springgreen ", color="springgreen",width=20)
    screen.drawButton(row=30,column=200,text=" taupe ", color="taupe",width=20)
    screen.drawButton(row=34,column=2,text=" teal ", color="teal",width=20)
    screen.drawButton(row=34,column=24,text=" turquoise ", color="turquoise",width=20)
    screen.drawButton(row=34,column=46,text=" ultramarine ", color="ultramarine",width=20)
    screen.drawButton(row=34,column=68,text=" violet ", color="violet",width=20)
    screen.drawButton(row=34,column=90,text=" viridian ", color="viridian",width=20)
    screen.drawButton(row=34,column=112,text=" white ", color="white",width=20)
    screen.drawButton(row=34,column=134,text=" yellow ", color="yellow",width=20)

    screen.update()

def threeApples():
    screen = Screen(rows=60, columns=100, main_symbol="+", main_color="black")
    apple1 = Model("00000c", 5, 5, "red", True)
    apple2 = Model("00000c", 5, 50, "green", True)
    apple3 = Model("00000c", 30, 25, "yellow", True)
    screen.drawModel(apple1)
    screen.drawModel(apple2)
    screen.drawModel(apple3)
    screen.update()

def moveAndTouch():
    screen1= Screen(30,60,"-","rose")
    model1 = Model("00000B",20,10,"yellow",True)
    object1 = Object(screen1,model1)
    model2 = Model("00000a",20,40,"yellow",True)
    object2 = Object(screen1,model2)
    model3 = Model("00000a",10,40,"magenta",True)
    object3 = Object(screen1,model3)
    object2.showObject()
    object1.showObject()
    screen1.autoUpdate(0.1)
    object2.horizontalMoveAnimation()
    object1.horizontalMoveAnimation(0.03)
    object2.verticalMoveAnimation()
    object3.verticalMoveAnimation()
    object1.changeColor("cyan")
    while True:
        if object1.objectTouchesObjects(object2,object3):
            object1.changeColor("cyan")
        else:
            object1.changeColor("green")
        time.sleep(0.1)


#flyingShapes()
#flyingKeyboard()
#girlWar()
#displayAllColors()
#threeApples()
#moveAndTouch()

coords = [[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],[10,11],[10,12],[10,13],[10,14],[10,15]]
length = len(coords)

screen = Screen(50,100," ","black")
screen.autoUpdate(0.07)
newX = 16
newY = 10
dir = "right"
while True:
    screen.changeBorder(border=2,color="red",symbol="█")
    screen.changeSymbols(coords,"█","lime")
    del coords[0]
    30
    coords.append([newY,newX])
    if keyboard.is_pressed('up arrow') and dir !="down":
        dir = "up"
    if keyboard.is_pressed('down arrow') and dir !="up":
        dir = "down"
    if keyboard.is_pressed('left arrow') and dir !="right":
        dir = "left"
    if keyboard.is_pressed('right arrow') and dir !="left":
        dir = "right"


    if dir == "left":
        newX-=1
    elif dir == "right":
        newX+=1
    elif dir == "up":
        newY-=1
    elif dir == "down":
        newY+=1
    for i in coords:
        if newY==i[0] and newX==i[1]:
            screen.stopAutoUpdate()
            time.sleep(0.1)
            print("Game Over")
            break
    if newX<1 or newY<1 or newX>screen.columns or newY>screen.rows:
        screen.stopAutoUpdate()
        time.sleep(0.1)
        print("Game Over")
        break
    time.sleep(0.08)
    screen.resetScreen()
