# Importing some important libraries
import os
import time
import random
import math
import threading

# Defining Object class
class Object():

    # Function for setuping
    def __init__(self,screen,model):
        self.model = model 
        self.row = self.model.row
        self.column = self.model.column
        self.color = self.model.color
        self.screen = screen 
        self.coords = []
        self.vertAnimation = False
        self.horAnimation = False
        self.animationStart = False
    
    # Function for showing model
    def showObject(self):
        row = self.row - 1
        column = self.column - 1
        d = 0
        text = self.model.model
        for i in range(len(text)):
            try:
                self.coords.append([row+1,column+d+1])
                if text[i] == "\n":
                    row += 1
                    d = 0
                    continue
                if text[i] == "\t":
                    column += 4
                    continue
                if text[i] == " " and self.model.auto_background == True:   
                    self.screen.screen[row][column+d][0] = self.screen.mainsymbol
                    if self.screen.maincolor == "random":
                        self.screen.screen[row][column + d][1] = self.screen.colors[self.screen.randomColor()]
                    else:
                        self.screen.screen[row][column+d][1] = self.screen.colors[self.screen.maincolor]
                    d += 1
                    continue
                self.screen.screen[row][column+d][0] = text[i]
                if self.color == "random":
                    self.screen.screen[row][column+d][1] = self.screen.colors[self.screen.randomColor()]
                else:
                    self.screen.screen[row][column+d][1] = self.screen.colors[self.color]
                d += 1
            except:
                pass

    # Function for changeing screen color
    def changeColor(self,color):
        self.color = color
        for i in self.coords:
            if self.color == "random":
                self.screen.screen[i[0]][i[1]][1] = self.screen.colors[self.screen.randomColor()]
            else:
                self.screen.screen[i[0]-1][i[1]-1][1] = self.screen.colors[self.color]

    # Function for changeing object row coordinate
    def changeRow(self,row):
        self.row = row
        self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
        self.coords = []
        self.showObject()

    # Function for changeing object column coordinate
    def changeColumn(self,column):
        self.column = column
        self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
        self.coords = []
        self.showObject()

    # Function for changeing object coordinates
    def changeCoordinates(self,row,column):
        self.row = row
        self.column = column
        self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
        self.coords = []
        self.showObject()

    # Function for moveing object up
    def moveUp(self,steps=1):
        self.model.row -= steps
        self.row -= steps
        self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
        self.coords = []
        self.showObject()

    # Function for moveing object down
    def moveDown(self,steps=1):
        self.model.row += steps
        self.row += steps
        self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
        self.coords = []
        self.showObject()

    # Function for moveing object left
    def moveLeft(self,steps=1):
        self.model.column -= steps
        self.column -= steps
        self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
        self.coords = []
        self.showObject()

    # Function for moveing object right
    def moveRight(self,steps=1):
        self.model.column += steps
        self.column += steps
        self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
        self.coords = []
        self.showObject()

    # Function for vertical sinus moveing animation
    def verticalSinusAnimation(self,speed=0.1,count="infinite"):
        self.vertAnimation = True
        self.animationStart = True
        row = math.floor(self.screen.rows/2)
        if count == "infinite":
            count=1000**1000
        column = self.column
        def mainUpdate():
            dg = 0
            for i in range(count):
                if self.vertAnimation == False or self.animationStart==False:
                    break
                dg+=0.05
                if row + math.floor(math.sin(dg)*row)-self.model.model.count("\n")>0:
                    self.row = row + math.floor(math.sin(dg)*row)-self.model.model.count("\n")
                    self.model.row = row + math.floor(math.sin(dg)*row)-self.model.model.count("\n")
                    self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
                    self.coords = []
                    self.showObject()
                    time.sleep(speed)
                else:
                    while row + math.floor(math.sin(dg)*row)-self.model.model.count("\n")<=0:
                        dg+=0.05

        x = threading.Thread(target=mainUpdate)
        x.start()

    # Function for horizontal sinus moveing animation
    def horizontalSinusAnimation(self,speed=0.1,count="infinite"):
        self.horAnimation = True
        self.animationStart = True
        column = math.floor(self.screen.columns/2)
        if count == "infinite":
            count=1000**1000
        row = self.row
        sl = 0
        sb = 0
        for i in self.model.model:
            if i=="\n":
                if sb>sl:
                    sl = sb
                sb = 0
            else:
                sb+=1
        def mainUpdate():
            dg = 0
            for i in range(count):
                if self.horAnimation == False or self.animationStart==False:
                    break
                dg+=0.05
                if column + math.floor(math.sin(dg)*column)-sl>0:
                    self.column = column + math.floor(math.sin(dg)*column)-sl
                    self.model.column = column + math.floor(math.sin(dg)*column)-sl
                    self.screen.changeSymbols(self.coords,self.screen.mainsymbol,self.screen.maincolor)
                    self.coords = []
                    self.showObject()
                    time.sleep(speed)
                else:
                    while column + math.floor(math.sin(dg)*column)-sl<=0:
                        dg+=0.05
        x = threading.Thread(target=mainUpdate)
        x.start()

    # Function for simple vertical moveing animation
    def verticalMoveAnimation(self,speed=0.05,count="infinite"):
        self.vertAnimation = True
        self.animationStart = True
        if count=="infinite":
            count=1000**1000
        def mainUpdate():
            direction = 1
            for i in range(count):
                if self.vertAnimation == False or self.animationStart==False:
                    break
                if (direction==1):
                    self.moveDown()
                else:
                    self.moveUp()
                if (self.row<=1 or self.row>=self.screen.rows-self.model.model.count("\n")):
                    direction*=-1
                time.sleep(speed)
        x = threading.Thread(target=mainUpdate)
        x.start()

    # Function for simple horizontal moveing animation
    def horizontalMoveAnimation(self,speed=0.05,count="infinite"):
        self.horAnimation = True
        self.animationStart = True
        if count=="infinite":
            count=1000**1000
        def mainUpdate():
            direction = 1
            for i in range(count):
                if self.horAnimation == False or self.animationStart==False:
                    break
                sl = 0
                sb = 0
                for i in self.model.model:
                    if i=="\n":
                        if sb>sl:
                            sl = sb
                        sb = 0
                    else:
                        sb+=1
                if (direction==1):
                    self.moveRight()
                else:
                    self.moveLeft()
                if (self.column<=1 or self.column>=self.screen.columns-sl):
                    direction*=-1
                time.sleep(speed)
        x = threading.Thread(target=mainUpdate)
        x.start()

    # Function for stopping vertical animation
    def stopVerticalAnimation(self):
        self.vertAnimation = False 

    # Function for stopping horizontal animation
    def stopHorizontalAnimation(self):
        self.horAnimation = False 

    # Function for stopping all animations
    def stopAnimations(self):
        self.animationStart = False

    # Function for checking is objeckt touches to another objeckts (which we gave)
    def objectTouchesObjects(self,*args):
        for obex in args:
            isT = False
            for i in self.coords:
                for j in obex.coords:
                    if i[0]==j[0] and i[1]==j[1]:
                        isT = True
                        return isT

    # Function for checking if objeckt touched to border.Will return true or false
    def objectTouchesBorders(self):
        for i in self.coords:
            if i[0]<=1:
                return "top"
            if i[1]<=1:
                return "left"
            if i[0]>=self.screen.rows:
                return "bottom"
            if i[1]>=self.screen.columns:
                return "right"
        return False
    


# Defining Model class
class Model():

    # Main function for makeing model
    def __init__(self, id, row=1, column=1, color="", auto_background=False,modelastext = ""):
        self.id = id
        self.row = row
        self.column = column
        self.color = color
        self.auto_background = auto_background
        self.models = {
            "000000" : ["alien","                   .-.\n    .-\"\"`\"\"-.    |(@ @)\n _/`oOoOoOoOo`\_ \ \-/\n\'.-=-=-=-=-=-=-.\' \/ \\ \n  `-=.=-.-=.=-\'    \ /\\ \n     ^  ^  ^       _H_ \\"],
            "000001" : ["alien","  _________\n /___   ___\\ \n//@@@\ /@@@\\\ \n\\\@@@/ \@@@//\n \___ \" ___/\n    | - |\n     \_/"],
            "000002" : ["alien","    .  .\n     \/\n    (@@)\n g/\_)(_/\e\ng/\(=--=)/\e\n    //\\\ \n   _|  |_"],
            "000003" : ["alien","    _..._\n  .\'     \'.\n / \     / \\ \n(  |     |  )\n(`\"`  \"  `\"`)\n \         /\n  \  ___  /\n   \'.___.\'"],
            "000004" : ["alien"," o            o\n  \          /\n   \        /\n    :-\'\"\"\'-:\n .-\'  ____  `-.\n( (  (_()_)  ) )\n `-.   ^^   .-\'\n    `._==_.\'\n     __)(___"],
            "000005" : ["alien","     ___\n ___/   \___\n/   \'---\'   \\ \n\'--_______--\'\n     / \\ \n    /   \\ \n    /\O/\\ \n    / | \\ \n    // \\"],
            "000006" : ["alien","          (\n       __..)__\n     .\'       `\'.\n    / - -        `\\ \n   /(\')(\')         \\ \n   /  ^        )   |\n   \.--.           |\n    \--\'          /\n     \__.-\' __..\'\'\n       /     |"],
            "000007" : ["alien","   .-\"\"\"\"-.\n  /        \\ \n /_        _\\ \n// \      / \\\ \n|\__\    /__/|\n \    ||    /\n  \        /\n   \  __  /\n    \'.__.\'\n     |  |\n     |  |"],
            "000008" : ["alien","o\n \_/\o\n( Oo)                    \|/\n(_=-)  .===O-  ~~Z~A~P~~ -O-\n/   \_/U\'                /|\\ \n||  |_/\n\\  |\n{K ||\n | PP\n | ||\n (__\\"],
            "000009" : ["alien","    o   o\n     )-(\n    (O O)\n     \=/\n    .-\"-.\n   //\ /\\\ \n _// / \ \\_\n=./ {,-.} \.=\n    || ||\n    || ||\n  __|| ||\n `---\" \"---\'"],
            "00000a": ["apple", "  ,--./,-.\n / #      \\\ \n|          |\n \        /\n  `._,._,'"],
            "00000b": ["apple", "\n ,--./,-.\n/,-._.--~\n __}  {\n\`-._,-`-,\n `._,._,' "],
            "00000c": ["apple", "                             ___\n                          _/`.-\'`.\n                _      _/` .  _.\'\n       ..:::::.(_)   /` _.\'_./\n     .oooooooooo\ \o/.-\'__.\'o.\n    .ooooooooo`._\_|_.\'`oooooob.\n  .ooooooooooooooooooooo&&oooooob.\n .oooooooooooooooooooo&@@@@@@oooob.\n.ooooooooooooooooooooooo&&@@@@@ooob.\ndoooooooooooooooooooooooooo&@@@@ooob\ndoooooooooooooooooooooooooo&@@@oooob\ndooooooooooooooooooooooooo&@@@ooooob\ndooooooooooooooooooooooooo&@@oooooob\n`dooooooooooooooooooooooooo&@ooooob\'\n `doooooooooooooooooooooooooooooob\'\n  `doooooooooooooooooooooooooooob\'\n   `doooooooooooooooooooooooooob\'\n    `doooooooooooooooooooooooob\'\n     `doooooooooooooooooooooob\'\n      `dooooooooobodoooooooob\'\n       `doooooooob dooooooob\'\n         `\"\' `\'"],
            "00000d": ["apple", "       , \n      .@, \n     .@a@a,. \n     S@@ss@@@@a,. \n    sS@@@ss@@@@@Ss,  , \n , SSSSS@@@ss@@@SSSs @, \n @sSSSSSSSS@@ss@SSSSs@@s, , \n `@@@@@SSSSSSSSssSSS@@@@@sSs, \n   @@@@@@@@@@@@@@ss@@@@@@@@SSs , \n , `@@@@@@@@@@@@@@ss@@@@@@@SSSs@, \n  SsSSSS@@@@@@@@@@@ss@@@@@@SSSSS@, \n  `SSSSSSSSS@@@@@@@@@ss@@@@SSSSS@@ \n   `SSSSSSSSSSSS@@@@@@ss@@SSSSSS@@\',\'\'\', \n   , `SSSSSSSSSSSSSSS@@ss@SSSSS@@@;%,.,,` \n    @aSSSSSSSSSSSSSSSSSSssSSSS@@@@;%;%%\' \n     `@@@@@@@SSSSSSSSSSSSssSSS@@@@;%;%\' \n        `@@@@@@@@@@@@@@@SSSssS@@@@;%;% \n           `@@@@@@@@@@@@@@@@@ss@@@;%;%    ...,,,,,,,,,,.. \n               `@@@@@@@@@@@@@@@ssS;%;%  .;;%%;%%;%%%;%%;%%%,. \n         .,::;;;;;;;;`SSSSSSSSSSSss;%%,::;%;%%%%%%%;%%%%%%;%%%%,. \n      .:::;;;;;%;;;;;;;,;;,;;,;;,::,.,::;%%%%%;%%%%%%%%%%%%%%%;%%%;, \n    .:::;;;%;;;;;%;%;%;%;%;%;%%%%;%%%%%;%%%%%%%%%%;%%%%%;%%%%%%%%;%%;. \n   :::;%;;;;%;;%;;;%;%;;%%%;%%%%%%%;%%%%%%%;%%%%%%%%%x%x%%%%%%%%;%%;%;, \n  :::;;;;;%;;%;;;%;;%;%%%%%%%%;%%%%%%%%%%%%%%%%%%%%%%%x%x%%%%%%%%%%%;%;, \n :::;;;;;%;;;;;;%;%%;%xx%;%%%%%%%;%%%%%%%x%%%%%%%%%%%%%x%x%x%%%%%%%;%;%; \n,:::;%;;%;;;%;%;;%;%%x%;%%%%%%%%%%%%%x%x%%x%%%%%%%%%%%%%x%%x%x%%%%%%;%%;, \n:::;;;;%;;%;;%;;%%%;x%x%%%;%%%%%%%%%%%%%x%%x%%%%%%%%%%%xx%x%x%%%%%%%%;;%; \n:::%;;;;;%;;%;;%%;%%;%;%%%%%%%%%%%%;%%x%%x%%x%;%%%%%%%%%x%x%%%%%%%%%;%;%; \n:::;;;%;;;;%;%;%;%%;%%%%%%%;%%%%%%%%%%%x%%x%%%%%%%%%%%%x%x%%x%%%%%%;%;%%; \n`:::;;;;%;%;%;%;%%;%%;%%%%%%%%%%%%%%%%%%%x%x%%%%%%%%%%xx%x%%%%%%%%%;%;%;\' \n `:::;;%;%;;%;;%%;%%;%;%%;%%%%%;%%%%%%%%%%%%%%%%%%;%%%%x%%%%%%%%%;%%;%;\' \n  `:::;;;;;%;;%%;%%;%%%%%%%;%%%%%%%%%%;%%%%%%%%;%%%%%;%%%%%%%%%;%%;%%;\' \n   `:::;;%;;;%;;;%%%;%%;%%%%%%%%%%;%%%%%%%%%%;%%%%%%%%%%%%%%;%;%;%%%;\' \n     `:::;;%;;;%%;%;%;%%;%;%%%%%%%%%%%%%%%%%%%%%%;%%;%%%%;%%%;%;%;%;\' \n       `:::;;;%;;%;;%%;%;%%%%%%%%%%%%%%%%%%;%%%%%%%%%%%;%%%;%%;%%;\' \n         `:::;;;%;;%;%;%%%%;%%%%%%;%%%%%%%%%%%%;%%%;%%;%%;%%;%%;\' \n           `:::;;%;;%;;%;%%%%%%;%%%%%%%%%%%%;%%%%%%%%%%%;%;%%;\' \n             `:::;%;;;%;;%;%x%%%%%;%%%%%%%%x%%%%%%;%%%;%%;%;\' \n               `:::;;;%;%;;%;x%x%x%%x%;%x%x%%%%;%%%%%;%;%;\' \n                 `:::%;%;;%:%:,xx%%x%%x%xx,:%%%%;%%;%%%;\' \n                   `:::%;;;;:%:`xx%x%xx%x\':%%%;%%%%%%;\' \n                    `:::;;%;;%:,`%x%xx%x\',:%;%%%%;%%;\' \n                      `:::;;;;;:::\'   `:::;;;;;;:::\'"],
            "00000e": ["apple", "                        .8 \n                      .888\n                    .8888\'\n                   .8888\'\n                   888\'\n                   8\'\n      .88888888888. .88888888888.\n   .8888888888888888888888888888888.\n .8888888888888888888888888888888888.\n.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\'\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\'\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\'\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.\n`%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.\n `00000000000000000000000000000000000\'\n  `000000000000000000000000000000000\'\n   `0000000000000000000000000000000\'\n     `###########################\'\n       `#######################\'\n         `#########\'\'########\'\n           `\"\"\"\"\"\"\'  `\"\"\"\"\"\'"],
            "00000f": ["apple", "          .:\'\n      __ :\'__\n   .\'`__`-\'__``.\n  :__________.-\'\n  :_________:\n   :_________`-;\n    `.__.-.__.\'"],
            "00000g": ["apple and worm", "                           .\n                         .OO\n                       .OOOO\n                      .OOOO\'\n                      OOOO\'          .-~~~~-.\n                      OOO\'          /   (o)(o)\n              .OOOOOO `O .OOOOOOO. /      .. |\n          .OOOOOOOOOOOO OOOOOOOOOO/\    \____/\n        .OOOOOOOOOOOOOOOOOOOOOOOO/ \\   ,\_/\n       .OOOOOOO%%OOOOOOOOOOOOO(#/\     /.\n      .OOOOOO%%%OOOOOOOOOOOOOOO\ \\  \/OO.\n     .OOOOO%%%%OOOOOOOOOOOOOOOOO\   \/OOOO.\n     OOOOO%%%%OOOOOOOOOOOOOOOOOOO\_\/\OOOOO\n     OOOOO%%%OOOOOOOOOOOOOOOOOOOOO\###)OOOO\n     OOOOOO%%OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n     OOOOOOO%OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n     `OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\'\n   .-~~\OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\'\n  / _/  `\(#\OOOOOOOOOOOOOOOOOOOOOOOOOOOO\'\n / / \  / `~~\OOOOOOOOOOOOOOOOOOOOOOOOOO\'\n|/\'  `\//  \\ \OOOOOOOOOOOOOOOOOOOOOOOO\'\n       `-.__\_,\OOOOOOOOOOOOOOOOOOOOO\'\n           `OO\#)OOOOOOOOOOOOOOOOOOO\'\n             `OOOOOOOOO\'\'OOOOOOOOO\'\n               `\"\"\"\"\"\"\'  `\"\"\"\"\"\"\'__.\\\'"],
            "00000h": ["apple", "             .:\'\n         __ :\'__\n      .\'`  `-\'  ``.\n     :             :\n     :             :\n      :           :\n       `.__.-.__.\'"],
            "00000i": ["apple", "             .:\'\n         __ :\'__\n      .\'`  `-\'  ``.\n     :          .-\'\n     :         :\n      :         `-;\n       `.__.-.__.\'\n"],
            "00000j": ["keyboard", "  ,----.   ,------. ,------. ,------. ,------. ,------.   ,------. ,------. ,------. ,------. ,------.                  _    _ __    __\n j|Esc`|i j| F1  `|V| F2  `|V| F3  `|V| F4  `|V| F5  `|i j| F6  `|V| F7  `|V| F8  `|V| F9  `|V| F10 `|i           /|    /|  /| ||  //\' |    /|\n ||    || ||      |||      |||      |||      |||      || ||      |||      |||      |||      |||      ||          /||   /|| /|| || /|  __   /||    H.DISK  =====\n |;----:| |;------:|;------:|;------:|;------:|;------:| |;------:|;------:|;------:|;------:|;------:|         /-||  / ||/ || || ||  ||  /-||    F.DISK  =====\n |______| |________|________|________|________|________| |________|________|________|________|________|        /  || /  |/  || || \_\,|/ /  ||    POWER   =====\n                                                                                                              \"\"  \"\"\"\"      \"\" \"\"   \"\"  \"\"  \"\"\n  ,-------. ,----. ,----. ,----. ,----. ,----. ,----. ,----. ,----. ,----. ,----. ,----. ,----. ,----. ,----.   ,-------. ,--------.   ,----. ,----. ,----. ,----.\n j| ~    `|V| !  |V| \" @|V| £ #|V| $  |V| %  |V| & ^|V| / &|V| ( *|V| ) (|V| = )|V| ? _|V| ` +|V| |  |V| <-`|i j| Del  `|V| Help  `|i j| { `|V| } `|V| / `|V| * `|i\n || `     ||| 1  ||| 2  ||| 3  ||| 4  ||| 5  ||| 6  ||| 7  ||| 8  ||| 9  ||| 0  ||| + -||| ´ =||| \  |||    || ||       |||        || || [  ||| ]  |||    |||    ||\n |;-------:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:| |;-------:|;--------:| |;----:|;----:|;----:|;----:|\n |,-----------._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,-------.| |_________|__________| |,----.|,----.|,----.|,----.|\n j| |<--     `|V| Q  |V| W  |V| E  |V| R  |V| T  |V| Y  |V| U  |V| I  |V| O  |V| P  |V| Å  |V| ^  |V|      `|i                        j| 7  |V| 8  |V| 9  |V| - `|i\n || -->|      |||    |||    |||    |||    |||    |||    |||    |||    |||    |||    |||    ||| ¨  |||     | ||                        ||    |||    |||    |||    ||\n |;-----------:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;-,   | ||                        |;----:|;----:|;----:|;----:|\n |,------._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----.j|   | ||         ,----.         |,----.|,----.|,----.|,----.|\n j|Ctrl `|V|Caps|V| A  |V| S  |V| D  |V| F  |V| G  |V| H  |V| J  |V| K  |V| L  |V| Ö :|V| Ä \"|V| *  |i| <-\' ||        j| ^  |i        j| 4  |V| 5  |V| 6  |V| + `|i\n ||      |||Lock|||    |||    |||    |||    |||    |||    |||    |||    |||    |||   ;|||   ´||| \'  |||     ||        || |  ||        ||    |||    |||    |||    ||\n |;------:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;-----:|        |;----:|        |;----:|;----:|;----:|;----:|\n |,----------._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,----._,---------------.|  ,----.|,----.|,----.  |,----.|,----.|,----.|,----.|\n j| /\      `|V| >  |V| Z  |V| X  |V| C  |V| V  |V| B  |V| N  |V| M  |V| ; <|V| : >|V| _ ?|V| /\           `|i j| <- |V| |  |V| -> |i j| 1  |V| 2  |V| 3  |V| E `|i\n || ||       ||| <  |||    |||    |||    |||    |||    |||    |||    ||| ,  ||| .  ||| - /||| ||            || ||    ||| v  |||    || ||    |||    |||    ||| n  ||\n |;----------:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;----:|;---------------:| |;----:|;----:|;----:| |;----:|;----:|;----:|| t  ||\n |_____,------._,------._,------------------------------------------------------------._,------._,------.____| |______|______|______| |,-----------.|,----.|| e  ||\n      j| Alt `|V|  /# `|V|                                                            |V|  /] `|V| Alt `|i                            j| 0         |V| .  |i| r  ||\n      ||      ||| /\"#  |||                                                            ||| /\"]  |||      ||                            ||           |||    |||    ||\n      |;------:|;------:|;------------------------------------------------------------:|;------:|;------:|                            |;-----------:|;----:|;----:|\n      |________|________|_________________________________________________________itz__|________|________|                            |____Ins______|_Del__|______|"],
            "00000k": ["keyboard", ".-----------------------------------------------------------------------------.\n||Es| |F1 |F2 |F3 |F4 |F5 | |F6 |F7 |F8 |F9 |F10|                  C= AMIGA   |\n||__| |___|___|___|___|___| |___|___|___|___|___|                             |\n| _____________________________________________     ________    ___________   |\n||~  |! |\" |§ |$ |% |& |/ |( |) |= |? |` || |<-|   |Del|Help|  |{ |} |/ |* |  |\n||`__|1_|2_|3_|4_|5_|6_|7_|8_|9_|0_|ß_|´_|\_|__|   |___|____|  |[ |]_|__|__|  |\n||<-  |Q |W |E |R |T |Z |U |I |O |P |Ü |* |   ||               |7 |8 |9 |- |  |\n||->__|__|__|__|__|__|__|__|__|__|__|__|+_|_  ||               |__|__|__|__|  |\n||Ctr|oC|A |S |D |F |G |H |J |K |L |Ö |Ä |^ |<\'|               |4 |5 |6 |+ |  |\n||___|_L|__|__|__|__|__|__|__|__|__|__|__|#_|__|       __      |__|__|__|__|  |\n||^    |> |Y |X |C |V |B |N |M |; |: |_ |^     |      |A |     |1 |2 |3 |E |  |\n||_____|<_|__|__|__|__|__|__|__|,_|._|-_|______|    __||_|__   |__|__|__|n |  |\n|   |Alt|A  |                       |A  |Alt|      |<-|| |->|  |0    |. |t |  |\n|   |___|___|_______________________|___|___|      |__|V_|__|  |_____|__|e_|  |\n|                                                                             |\n`-----------------------------------------------------------------------------\'"],
            "00000l": ["keyboard", "|\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\".---------------.\"\"|\n|                                                          |/\"\'_ Commodore |  |\n|                                                          |\_.\"A-500 Plus |  |\n|mga                                                       \'---------------\'  |\n|-----------------------------------------------------------------------------|\n||Es| |F1 |F2 |F3 |F4 |F5 | |F6 |F7 |F8 |F9 |F10|                Power [____] |\n||__| |___|___|___|___|___| |___|___|___|___|___|                Drive [____] |\n| _____________________________________________     ________    ___________   |\n||   |! |\" |£ |$ |% |^ |& |* |( |) |_ |+ || |<-|   |Del|Help|  |( |) |/ |* |  |\n||___|1_|2_|3_|4_|5_|6_|7_|8_|9_|0_|-_|=_|\_|__|   |___|____|  |__|__|__|__|  |\n||<-  |Q |W |E |R |T |Y |U |I |O |P |{ |} |   ||               |7 |8 |9 |- |  |\n||->__|__|__|__|__|__|__|__|__|__|__|[_|]_|_  ||               |__|__|__|__|  |\n||Ctr|oC|A |S |D |F |G |H |J |K |L |: |@ |  |<\'|               |4 |5 |6 |+ |  |\n||___|_L|__|__|__|__|__|__|__|__|__|;_|\'_|__|__|       __      |__|__|__|__|  |\n||^    |  |Z |X |C |V |B |N |M |< |> |? |^     |      |A |     |1 |2 |3 |E |  |\n||_____|__|__|__|__|__|__|__|__|__|__|__|______|    __||_|__   |__|__|__|n |  |\n|   |Alt|A  |                       |A  |Alt|      |<-|| |->|  |0    |. |t |  |\n|   |___|___|_______________________|___|___|      |__|V_|__|  |_____|__|e_|  |\n|                                                                             |\n\'-----------------------------------------------------------------------------\'"],
            "00000m": ["computer", "    .__________________________.\n    | .___________________. |==|\n    | | ................. | |  |\n    | | ::::::::::::::::: | |  |\n    | | ::::::::::::::::: | |  |\n    | | ::::::::::::::::: | |  |\n    | | ::::::::::::::::: | |  |\n    | | ::::::::::::::::: | |  |\n    | | ::::::::::::::::: | | ,|\n    | !___________________! |(c|\n    !_______________________!__!\n   /                            \\ \n  /  [][][][][][][][][][][][][]  \\ \n /  [][][][][][][][][][][][][][]  \\ \n(  [][][][][____________][][][][]  )\n \ ------------------------------ /\n  \______________________________/"],
            "00000n": ["computer", "         ______________\n        /             /|\n       /             / |\n      /____________ /  |\n     | ___________ |   |\n     ||           ||   |\n     ||           ||   |\n     ||           ||   |\n     ||___________||   |\n     |   _______   |  /\n    /|  (_______)  | /\n   ( |_____________|/\n    \\ \n.=======================.\n| ::::::::::::::::  ::: |\n| ::::::::::::::[]  ::: |\n|   -----------     ::: |\n`-----------------------\'"],
            "00000o": ["computer", "                       __________________________\n               __..--/\".\'                        \'.\n       __..--\"\"      | |                          |\n      /              | |                          |\n     /               | |    ___________________   |\n    ;                | |   :__________________/:  |\n    |                | |   |                 \'.|  |\n    |                | |   |                  ||  |\n    |                | |   |                  ||  |\n    |                | |   |                  ||  |\n    |                | |   |                  ||  |\n    |                | |   |                  ||  |\n    |                | |   |                  ||  |\n    |                | |   |                  ||  |\n    |                | |   |______......-----\"\|  |\n    |                | |   |_______......-----\"   |\n    |                | |                          |\n    |                | |                          |\n    |                | |                  ____----|\n    |                | |_____.....----|#######|---|\n    |                | |______.....----\"\"\"\"       |\n    |                | |                          |\n    |. ..            | |   ,                      |\n    |... ....        | |  (c ----- \"\"\"           .\'\n    |..... ......  |\|_|    ____......------\"\"\"|\"\n    |. .... .......| |\"\"\"\"\"\"                   |\n    \'... ..... ....| |                         |\n      \"-._ .....  .| |                         |\n          \"-._.....| |             ___...---\"\"\"\'\n              \"-._.| | ___...---\"\"\"\n                  \"\"\"\"\""],
            "00000p": ["computer", "       ______________________________________________________________\n     .\'  __________________________________________________________  \'.\n     : .\'                                                          \'. :\n     | |      ________________________________________________      | |\n     | |    .:________________________________________________:.    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |                                                  |    | |\n     | |    |            __________________________            |    | |\n     | |    |           |  |  |  |  |  |  |  |  |  |           |    | |\n     | |    \'.__________|__|__|__|__|__|__|__|__|__|__________.\'    | |\n     | |                                                            | |\n     | |                            LG                              | |\n     : \'.__________________________________________________________.\' :\n      \".____________________________\__/____________________________.\"\n                                     ||\n                                     ||\n                                     ||\n                                  ___||___\n                            _.--\"\"   \"\"   \"\"--._\n                         .\'\"       .-L-.        \"\'.\n                       .\'          : _ (           \'.\n                     .\'             \" \"              \'.\n                    .\'                                \'.\n                    :         ________________         :\n                   .\'       .\'                \'.       \'.\n                   :        \'.________________.\'        :\n                   |----......______    ______......----|\n                   :                \"\"\"\"                :\n                   \'.                                  .\'\n                     \"-.____. . . . . . . . . . ____.-\"\n                            \"\"\"\"\"\"--------\"\"\"\"\"\""],
            "00000q": ["tetris", " ___\n|[_]|\n|+ ;|\n`---\'"],
            "00000r": ["tetris", "     _______\n    |.-----.|\n    ||     ||\n    ||_____/|\n    | .     |\n    |-|-  oo|\n    |  _ _  |\n    |       /\n    `\"\"\"\"\"\"`"],
            "00000s": ["tetris", " _____________________________   \n/        _____________        \  \n| == .  |             |     o |  \n|   _   |             |    B  |  \n|  / \  |             | A   O |  \n| | O | |             |  O    |  \n|  \_/  |             |       |  \n|       |             | . . . |  \n|  :::  |             | . . . |  \n|  :::  |_____________| . . . |  \n|           S N K             |  \n\_____________________________/"],
            "00000t": ["cat", ":~-._                                                 _.-~:\n: :.~^o._        ________---------________        _.o^~.:.:\n : ::.`?88booo~~~.::::::::...::::::::::::..~~oood88P\'.::.:\n :  ::: `?88P .:::....         ........:::::. ?88P\' :::. :\n  :  :::. `? .::.            . ...........:::. P\' .:::. :\n   :  :::   ... ..  ...       .. .::::......::.   :::. :\n   `  :\' .... ..  .:::::.     . ..:::::::....:::.  `: .\'\n    :..    ____:::::::::.  . . ....:::::::::____  ... :\n   :... `:~    ^~-:::::..  .........:::::-~^    ~::.::::\n   `.::. `\   (8)  \b:::..::.:.:::::::d/  (8)   /\'.::::\'\n    ::::.  ~-._v    |b.::::::::::::::d|    v_.-~..:::::\n    `.:::::... ~~^?888b..:::::::::::d888P^~...::::::::\'\n     `.::::::::::....~~~ .:::::::::~~~:::::::::::::::\'\n      `..:::::::::::   .   ....::::    ::::::::::::,\'\n        `. .:::::::    .      .::::.    ::::::::\'.\'\n          `._ .:::    .        :::::.    :::::_.\'\n             `-. :    .        :::::      :,-\'\n                :.   :___     .:::___   .::\n      ..--~~~~--:+::. ~~^?b..:::dP^~~.::++:--~~~~--..\n        ___....--`+:::.    `~8~\'    .:::+\'--....___\n      ~~   __..---`_=:: ___gd8bg___ :==_\'---..__   ~~\n       -~~~  _.--~~`-.~~~~~~~~~~~~~~~,-\' ~~--._ ~~~-\n          -~~            ~~~~~~~~~   _ Seal _  ~~-"],
            "00000u": ["cat", "       ,\n       \`-._           __\n        \\  `-..____,.\'  `.\n         :`.         /    \`.\n         :  )       :      : \\\ \n          ;\'        \'   ;  |  :\n          )..      .. .:.`.;  :\n         /::...  .:::...   ` ;\n         ; _ \'    __        /:\\ \n         `:o>   /\o_>      ;:. `.\n        `-`.__ ;   __..--- /:.   \\ \n        === \_/   ;=====_.\':.     ;\n         ,/\'`--\'...`--....        ;\n              ;                    ;\n            .\'                      ;\n          .\'                        ;\n        .\'     ..     ,      .       ;\n       :       ::..  /      ;::.     |\n      /      `.;::.  |       ;:..    ;\n     :         |:.   :       ;:.    ;\n     :         ::     ;:..   |.    ;\n      :       :;      :::....|     |\n      /\     ,/ \      ;:::::;     ;\n    .:. \:..|    :     ; \'.--|     ;\n   ::.  :\'\'  `-.,,;     ;\'   ;     ;\n.-\'. _.\'\      / `;      \,__:      \\ \n`---\'    `----\'   ;      /    \,.,,,/\n                   `----`"],
            "00000v": ["cat", "		M.					   .:M\n		MMMM.					.:MMMM\n		MMMMMMMM			     .:MMMMMMM\n		:MMHHHMMMMHMM.	.:MMMMMMMMM:.	   .:MMHHMHMM:\n		 :MMHHIIIHMMMM.:MMHHHHIIIHHMMMM. .:MMHIHIIHHM:\n		  MMMHIIIIHHMMMIIHHMHHIIIIIHHMMMMMMHHHIIIIHHM:\n		  :MMHIIIIIHMMMMMMMHHIIIIIIHHHMMMMMHHII:::IHM.\n		   MH:I:::IHHMMMMMHHII:::IIHHMMMHHHMMM:I:IHMM\n		   :MHI:HHIHMMHHIIHII::.::IIHMMHHIHHMMM::HMM:\n		    MI::HHMMIIM:IIHII::..::HM:MHHII:::IHHMM:\n		    MMMHII::..:::IHMMHHHMHHMMI:::...::IHM:\n		    :MHHI::....::::HMMMMMMHHI::.. ..:::HM:\n		     :MI:.:MH:.....:HMMMMHHMIHMMHHI:HH.:M\n		     M:.I..MHHHHHMMMIHMMMMHMMHHHHHMMH:.:M.\n		     M:.H..H  I:HM:MHMHI:IM:I:MM::  MMM:M:\n		     :M:HM:.M I:MHMIIMMIIHM I:MM::.:MMI:M.\n		     \'M::MM:IMH:MMII MMHIMHI :M::IIHMM:MM\n		      MH:HMMHIHMMMMMMHMMIMHIIHHHHIMMHHMM\n		       MI:MMMMHI:::::IMM:MHI:::IMMMMHIM\n			:IMHIHMMMMMM:MMMMMHHHHMMMHI:M\n			 HI:IMIHMMMM:MMMMMMHHHMI:.:M	  .....\n	     ............M::..:HMMMMIMHIIHMMMMHII:M:::\'\'\'\'\n		 ....:::MHI:.:HMMMMMMMMHHHMHHI::M:::::::\'\'\'\'\'\'\n		\'\'   ...:MHI:.::MMHHHMHMIHMMMMHH.MI..........\n		   \'\'  ...MHI::.::MHHHHIHHMM:::IHM           \'\'\'\n		      \'  IMH.::..::HMMHMMMH::..:HM:\n			:M:.H.IHMIIII::IIMHMMM:H.MH\n			 IMMMH:HI:MMIMI:IHI:HIMIHM:\n		       .MMI:.HIHMIMI:IHIHMMHIHI:MIM.\n		      .MHI:::HHIIIIIHHI:IIII::::M:IM.\n		     .MMHII:::IHIII::::::IIIIIIHMHIIM\n		     MHHHI::.:IHHII:::.:::IIIIHMHIIHM:\n		    MHHHII::..::MII::.. ..:IIIHHHII:IM.\n		   .MHHII::....:MHII::.  .:IHHHI::IIHMM.\n		   MMHHII::.....:IHMI:. ..:IHII::..:HHMM\n		   MHHII:::......:IIHI...:IHI::.....::HM:\n		  :MMH:::........ ...::..::....  ...:IHMM\n		  IMHIII:::..........	  .........::IHMM.\n		  :MHIII::::......	    .......::IHMM:\n		   MHHIII::::...	     ......::IHMM:\n		   IMHHIII:::...	     .....::IIHMM,\n		   :MHHIII:::I:::...	 ....:::I:::IIHMM\n		    MMHHIII::IHI:::...........:::IIH:IHMM\n		    :MMHHII:IIHHI::::::.....:::::IH:IHMIM\n		     MMMHHII:IIHHI:::::::::::::IHI:IIHM:M.\n		     MMMHHIII::IHHII:::::::::IHI:IIIHMM:M:\n		     :MMHHHIII::IIIHHII::::IHI..IIIHHM:MHM\n		     :MMMHHII:..:::IHHMMHHHHI:IIIIHHMM:MIM\n		     .MMMMHHII::.:IHHMM:::IIIIIIHHHMM:MI.M\n		   .MMMMHHII::.:IHHMM:::IIIIIIHHHMM:MI.M\n		 .MMMMHHMHHII:::IHHMM:::IIIIIHHHHMM:MI.IM.\n		.MMHMMMHHHII::::IHHMM::I&&&IHHHHMM:MMH::IM.\n	       .MMHHMHMHHII:::.::IHMM::IIIIHHHMMMM:MMH::IHM\n	       :MHIIIHMMHHHII:::IIHMM::IIIHHMMMMM::MMMMHHHMM.\n	       MMHI:IIHMMHHHI::::IHMM:IIIIHHHMMMM:MMMHI::IHMM.\n	       MMH:::IHMMHHHHI:::IHMM:IIIHHHHMMMM:MMHI:.:IHHMM.\n	       :MHI:::IHMHMHHII::IHMM:IIIHHHMMMMM:MHH::.::IHHM:\n	       \'MHHI::IHMMHMHHII:IHMM:IIHHHHMMMM:MMHI:...:IHHMM.\n		:MHII:IIHMHIHHIIIIHMM:IIHHHHMMMM:MHHI:...:IIHMM:\n		\'MHIII:IHHMIHHHIIHHHMM:IHHHMMMMM:MHHI:..::IIHHM:\n		 :MHHIIIHHMIIHHHIHHHMM:HHHHMMMMM:MHII::::IIIHHMM\n		  MHHIIIIHMMIHHHIIHHMM:HHHHMMMM:MMHHIIHIIIIIHHMM.\n		  \'MHHIIIHHMIIHHIIIHMM:HHHMMMMH:MHHMHII:IIIHHHMM:\n		   \'MHHIIIHMMIHHHIHHMM:HHHMMMHH:MMIMMMHHHIIIHHMM:\n		    \'MHHIIHHMIHHHHHMMM:HHHMMMH:MIMMMMMMMMMMHIHHM:\n		     \'MHIIIHMMIHHHHHMM:HHHMMMH:IMMMMMHHIHHHMMHHM\'\n		      :MHHIIHMIHHHHHMM:HHHMMMM:MMHMMHIHMHI:IHHHM\n		       MHHIIHM:HHHHHMM:HHHMMMM:MMMHIHHIHMM:HHIHM\n			MHHIHM:IHHHHMM:HHHHMM:MMHMIIHMIMMMHMHIM:\n			:MHIHMH:HHHHMM:HHHHMM:MMHIIHMIIHHMMHIHM:\n			 MMHHMH:HHHHMM:HHHHMM:MHHIHMMIIIMMMIIHM\'\n			 \'MMMMH:HHHHMM:HHHMM:MHHHIMMHIIII::IHM:\n			  :MMHM:HHHHMM:HHHMM:MHIHIMMHHIIIIIHM:\n			   MMMM:HHHHMM:HHHHM:MHHMIMMMHHHIHHM:MMMM.\n			   :MMM:IHHHMM:HHHMM:MHHMIIMMMHHMM:MMMMMMM:\n			   :MMM:IHHHM:HHHHMM:MMHHHIHHMMM:MMMMMMMMMM\n			    MHM:IHHHM:HHHMMM:MMHHHHIIIMMIIMMMMMMMMM\n			    MHM:HHHHM:HHHMMM:HMMHHHHHHHHHMMMMMMMMM:\n			 .MI:MM:MHHMM:MHMMHMHHMMMMHHHHHHHMMMMMMMMM\'\n			:IM:MMIM:M:MM:MH:MM:MH:MMMMMHHHHHMMMMMMMM\'\n			:IM:M:IM:M:HM:IMIHM:IMI:MMMMMHHHMMMMMM:\'\n			 \'M:MHM:HM:MN:HMIHM::M\'   \'::MMMMMMM:\'\n			    \'M\'HMM\'M\'\'M\'\'HM\'I\'"],
            "00000w": ["light", "  ..---..\n /       \\ \n|         |\n:         ;\n \  \~/  /\n  `, Y ,\'\n   |_|_|\n   |===|\n   |===|\n    \_/"],
            "00000x": ["camera", "        .---.\n        |[X]|\n _.==._.\"\"\"\"\".___n__\nd __ ___.-\'\'-. _____b\n|[__]  /.\"\"\"\".\ _   |\n|     // /\"\"\ \\_)  |\n|     \\ \__/ //    |\n|pentax\`.__.\'/     |\n\=======`-..-\'======/\n `-----------------\'"],
            "00000y": ["camera", "            ___\n           / _ \\ \n          | / \ |\n          | \_/ |\n           \___/ ___\n           _|_|_/[_]\__==_\n          [---------------]\n          | O   /---\     |\n          |    |     |    |\n          |     \___/     |\n          [---------------]\n                [___]\n                 | |\\\ \n                 | | \\\ \n                 [ ]  \\_\n                /|_|\  ( \\ \n               //| |\\  \ \\ \n              // | | \\  \ \\ \n             //  |_|  \\  \_\\ \n            //   | |   \\\ \n           //\   | |   /\\\ \n          //  \  | |  /  \\\ \n         //    \ | | /    \\\ \n        //      \|_|/      \\\ \n       //        [_]        \\\ \n      //          H          \\\ \n     //           H           \\\ \n    //            H            \\\ \n   //             H             \\\ \n  //              H              \\\ \n //                               \\\ \n//                                 \\"],
            "00000z": ["phone", "   _\n  | |\n  |_|\n  /_\    \ | /\n.-\"\"\"------.----.\n|          U    |\n|               |\n| ====o======== |\n| ============= |\n|               |\n|_______________|\n| ________GF337 |\n||   Welcome   ||\n||             ||\n||_____________||\n|__.---\"\"\"---.__|\n|---------------|\n|[Yes][(|)][ No]|\n| ___  ___  ___ |\n|[<-\'][CLR][.->]|\n| ___  ___  ___ |\n|[1__][2__][3__]|\n| ___  ___  ___ |\n|[4__][5__][6__]|\n| ___  ___  ___ |\n|[7__][8__][9__]|\n| ___  ___  ___ |\n|[*__][0__][#__]|\n`--------------\'\n{__|\"\"|_______\'-\n`---------------\'"],
            "00000A": ["saturn","         ,MMM8&&&.\n    _...MMMMM88&&&&..._\n .::\'\'\'MMMMM88&&&&&&\'\'\'::.\n::     MMMMM88&&&&&&     ::\n\'::....MMMMM88&&&&&&....::\'\n   `\'\'\'\'MMMMM88&&&&\'\'\'\'`\n         \'MMM8&&&\'"],
            "00000B": ["earth","        _____\n    ,-:` \;\',`\'-, \n  .\'-;_,;  \':-;_,\'.\n /;   \'/    ,  _`.-\\ \n| \'`. (`     /` ` \`|\n|:.  `\`-.   \_   / |\n|     (   `,  .`\ ;\'|\n \     | .\'     `-\'/\n  `.   ;/        .\'\n    `\'-._____."],
            "00000C" : ["earth planet","             _____\n          .-\'.  \':\'-.\n        .\'\'::: .:    \'.\n       /   :::::\'      \\ \n      ;.    \':\' `       ;\n      |       \'..       |\n      ; \'      ::::.    ;\n       \       \'::::   /\n        \'.      :::  .\'\n          \'-.___\'_.-\'"],
            "00000D" : ["saturn planet","                    .::.\n                  .:\'  .:\n        ,MMM8&&&.:\'   .:\'\n       MMMMM88&&&&  .:\'\n      MMMMM88&&&&&&:\'\n      MMMMM88&&&&&&\n    .:MMMMM88&&&&&&\n  .:\'  MMMMM88&&&&\n.:\'   .:\'MMM8&&&\'\n:\'  .:\'\n\'::\'"],
            "00000E" : ["saturn planet","        ~+\n\n                 *       +\n           \'                  |\n       ()    .-.,=\"``\"=.    - o -\n             \'=/_       \     |\n          *   |  \'=._    |\n               \     `=./`,        \'\n            .   \'=.__.=\' `=\'      *\n   +                         +\n        O      *        \'       ."],
            "00000F" : ["earth planet","             _______\n          .-\' _____ \'-.\n        .\' .-\'.  \':\'-. \'.\n       / .\'\'::: .:    \'. \\ \n      / /   :::::\'      \ \\ \n     | ;.    \':\' `       ; |\n     | |       \'..       | |\n     | ; \'      ::::.    ; |\n      \ \       \'::::   / /\n       \ \'.      :::  .\' /\n        \'. \'-.___\'_.-\' .\'\n          \'-._______.-"],
            "00000G" : ["earth planet","o               .        ___---___                    .                   \n       .              .--\        --.     .     .         .\n                    ./.;_.\     __/~ \.     \n                   /;  / `-\'  __\    . \                            \n .        .       / ,--\'     / .   .;   \        |\n                 | .|       /       __   |      -O-       .\n                |__/    __ |  . ;   \ | . |      |\n                |      /  \\_    . ;| \___|    \n   .    o       |      \  .~\\___,--\'     |           .\n                 |     | . ; ~~~~\_    __|\n    |             \    \   .  .  ; \  /_/   .\n   -O-        .    \   /         . |  ~/                  .\n    |    .          ~\ \   .      /  /~          o\n  .                   ~--___ ; ___--~       \n                 .          ---         .              -JT"],
            "00000H" : ["solar system","                      :\n                       :\n                       :\n                       :\n        .              :\n         \'.            :           .\'\n           \'.          :         .\'\n             \'.   .-\"\"\"\"\"\"-.   .\'                                   .\'\':\n               \'.\"          \".\'                               .-\"\"\"\"-.\'         .---.          .----.        .-\"\"\"-.\n                :            :                _    _        .\"     .\' \".    ...\"     \"...    .\"      \".    .\"       \".\n        .........            .........    o  (_)  (_)  ()   :    .\'    :   \'..:.......:..\'   :        :    :         :   o\n                :            :                              :  .\'      :       \'.....\'       \'.      .\'    \'.       .\'\n                 :          :                             .\'.\'.      .\'                        `\'\'\'\'`        `\'\'\'\'\'`\n                  \'........\'                              \'\'   ``````\n                 .\'    :   \'.\n               .\'      :     \'.\n             .\'        :       \'.\n           .\'          :         \'.\n                       :\n                       :\n                       :\n                       :"],
            "00000I" : ["saturn as seen from one of its moons","                .                                            .\n     *   .                  .              .        .   *          .\n  .         .                     .       .           .      .        .\n        o                             .                   .\n         .              .                  .           .\n          0     .\n                 .          .                 ,                ,    ,\n .          \          .                         .\n      .      \   ,\n   .          o     .                 .                   .            .\n     .         \                 ,             .                .\n               #\##\#      .                              .        .\n             #  #O##\###                .                        .\n   .        #*#  #\##\###                       .                     ,\n        .   ##*#  #\##\##               .                     .\n      .      ##*#  #o##\#         .                             ,       .\n          .     *#  #\#     .                    .             .          ,\n                      \          .                         .\n____^/\___^--____/\____O______________/\/\---/\___________---______________\n   /\^   ^  ^    ^                  ^^ ^  \'\ ^          ^       ---\n         --           -            --  -      -         ---  __       ^\n   --  __                      ___--  ^  ^                         --  __"],
            "00000J" : ["earth planet","              _-o#&&*\'\'\'\'?d:>b\_\n          _o/\"`\'\'  \'\',, dMF9MMMMMHo_\n       .o&#\'        `\"MbHMMMMMMMMMMMHo.\n     .o\"\" \'         vodM*$&&HMMMMMMMMMM?.\n    ,\'              $M&ood,~\'`(&##MMMMMMH\\ \n   /               ,MMMMMMM#b?#bobMMMMHMMML\n  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk\n ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L\n|               |MMMMMMMMMMMMMMMMMMMMbMH\'   T,\n$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}\'  `?\n]MMH#             \"\"*\"\"\"\"*#MMMMMMMMMMMMM\'    -\nMMMMMb_                   |MMMMMMMMMMMP\'     :\nHMMMMMMMHo                 `MMMMMMMMMT       .\n?MMMMMMMMP                  9MMMMMMMM}       -\n-?MMMMMMM                  |MMMMMMMMM?,d-    \'\n :|MMMMMM-                 `MMMMMMMT .M|.   :\n  .9MMM[                    &MMMMM*\' `\'    .\n   :9MMk                    `MMM#\"        -\n     &M}                     `          .-\n      `&.                             .\n        `~,   .                     ./\n            . _                  .-\n              \'`--._,dd###pp=\"\"\'"],
            "00000K" : ["saturn planet","                                                                    ..;===+.\n                                                                .:=iiiiii=+=\n                                                             .=i))=;::+)i=+,\n                                                          ,=i);)I)))I):=i=;\n                                                       .=i==))))ii)))I:i++\n                                                     +)+))iiiiiiii))I=i+:\'\n                                .,:;;++++++;:,.       )iii+:::;iii))+i=\'\n                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+\'\n                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:\n                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+\n                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,\n                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+\n                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i=\'\n                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`\n                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:\'\n                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,\n                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;\n                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;\n                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:\n                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=\n                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+\n                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i\'\n                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;\n              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;\n             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;\n           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,\n         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+\'\n       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+\n      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:\'\n     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+\'\n   .+=:))iiiiiiii)))+ii;\n  .+=;))iiiiii)));ii+\n .+=i:)))))))=+ii+\n.;==i+::::=)i=;\n,+==iiiiii+,\n`+=+++;`"],
            "00000L" : ["satellite","               }--O--{\n                  [^]\n                 /ooo\\ \n ______________:/o   o\:______________\n|=|=|=|=|=|=|:A|\":|||:\"|A:|=|=|=|=|=|=|\n^\"\"\"\"\"\"\"\"\"\"\"\"\"\"!::{o}::!\"\"\"\"\"\"\"\"\"\"\"\"\"\"^\n                \     /\n                 \.../\n      ____       \"---\"       ____\n     |\/\/|=======|*|=======|\/\/|\n     :----\"       /-\       \"----:\n                 /ooo\\ \n                #|ooo|#\n                 \___/"],
            "00000M" : ["satellite","         ooo\n        / : \\ \n       / o0o \\ \n _____\"~~~~~~~\"_____\n \+###|U * * U|###+/\n  \...!(.>..<)!.../\n   ^^^^o|   |o^^^^\n+=====}:^^^^^:{=====+#\n.____  .|!!!|.  ____.\n|#####:/\" \" \"\:#####|\n|#####=|  O  |=#####|\n|#####>\_____/<#####|\n ^^^^^   | |   ^^^^^\n         o o"],
            "00000N" : ["satellite","==================-+-+-+-+-+-+-+-+-+-+==================\n   ++++++\ /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//++++++\n          \_______ .  .  .  .  .  .  ._______/\n                 \_______ oooo _______/\n                    |    \||||/    |\n                    |    [++++]    |\n                   }:{    |><|    }:{\n                        (((II)))\n                          /::\\ \n                          \::/\n                           ||\n                      (((((oo)))))\n                           !!\n                           YY\n                           /\\ \n                          /><\\ \n               !----------|UU|----------!\n               |__________\  /__________|\n                           ++"],
            "00000O" : ["satellite","           .       .                   .       .      .     .      .\n          .    .         .    .            .     ______\n      .           .             .               ////////\n                .    .   ________   .  .      /////////     .    .\n           .            |.____.  /\        ./////////    .\n    .                 .//      \/  |\     /////////\n       .       .    .//          \ |  \ /////////       .     .   .\n                    ||.    .    .| |  ///////// .     .\n     .    .         ||           | |//`,/////                .\n             .       \\        ./ //  /  \/   .\n  .                    \\.___./ //\` \'   ,_\     .     .\n          .           .     \ //////\ , /   \                 .    .\n                       .    ///////// \|  \'  |    .\n      .        .          ///////// .   \ _ /          .\n                        /////////                              .\n                 .   ./////////     .     .\n         .           --------   .                  ..             .\n  .               .        .         .                       .\n                        ________________________\n____________------------                        -------------_________"],
            "00000P" : ["star","   ,\n__/ \__\n\     /\n/_   _\\ \n  \ /\n   \'"],
            "00000Q" : ["star","     /\\ \n____/  \____\n\          /\n >        <\n/___    ___\\ \n    \  /\n     \/"],
            "00000R" : ["star","    A\n___/_\___\n \',. ..\'\n /.\'^\'.\\ \n/\'     \'\ "],
            "00000S" : ["star","       .\n  ---./|\.---\n  \'._/ | \_.\'\n_.-\'_\'.|.\'_\'-._\n \'-._.\'|\'._.-\'\n  .\' \ | / \'.\n  ---\'\|/\'---\n       \'"],
            "00000T" : ["star","      ,\n   \  :  /\n`. __/ \__ .\'\n_ _\     /_ _\n   /_   _\\ \n .\'  \ /  `.\n   /  :  \\ \n      \'"],
            "00000U" : ["star","         /\\ \n   .--._/  \_.--.\n    `)        (`\n _.-\'          \'-._\n\'-.              .-\'\n   `)          (\'\n   /.-\"-.  .-\"-.\\ \n   `     \/"],
            "00000V" : ["star sky","   *  .  . *       *    .        .        .   *    ..\n .    *        .   ###     .      .        .            *\n    *.   *        #####   .     *      *        *    .\n  ____       *  ######### *    .  *      .        .  *   .\n /   /\  .     ###\#|#/###   ..    *    .      *  .  ..  *\n/___/  ^8/      ###\|/###  *    *            .      *   *\n|   ||%%(        # }|{  #\n|___|,  \\         }|{"],
            "00000W" : ["star","        .\n       ,O,\n      ,OOO,\n\'oooooOOOOOooooo\'\n  `OOOOOOOOOOO`\n    `OOOOOOO`\n    OOOO\'OOOO\n   OOO\'   \'OOO\n  O\'         \'O"],
            "00000X" : ["star","                 \'\n            *          .\n                   *       \'\n              *                *\n\n\n\n\n\n   *   \'*\n           *\n                *\n                       *\n               *\n                     *\n\n         .                      .\n         .                      ;\n         :                  - --+- -\n         !           .          !\n         |        .             .\n         |_         +\n      ,  | `.\n--- --+-<#>-+- ---  --  -\n      `._|_,\'\n         T\n         |\n         !\n         :         . : \n         .       *"],
            "00000Y" : ["pathfinder mars car robot","                                                                    ||\n                                                  __..--\".          ||\n                                 __..--\"\"`._..--\"\" . . . .`.        ||\n                         __..--\"\". . . . . . .`. . . . . . .`.      ||\n                 __..--\"\". . . . .`. . . . . . .`. . . . . . .`.   //\n         __..--\"\". . `.  . . . . . .`. . . . . . .`. . . . . . .`.//\n  _..--\"\"  . . . . . . `.  . . . . . .`. . . . . . .`. . . . . . .||\n:\". . . .`.  . . . . . . `.  . . . . . .`. . . . . . .`. . . . . .||`.\n`:. . . . .`.  . . . . . . `.  . . . . . .`. . . . . . .`. . . . .||__>\n  `:. . . . .`.  . . . . . . `.  . . . . . .`. . . . . . .`.__..-o||\n    `:. . . . .`.  . . . . . . `.  . . . . . .`. . . . .`;Y\"->.  \"\"\n      `:. . . . .`.  . . . . . . `.  . . . . . .`. . . __.>.:\'\n        `:. . . . .`.  . . . . . . `.  . . . . __..--\"\" ..+\"`.\n   _..-._ `:. . . . .`.  . . . . . . `.__..--\"\" ....:::::.|   `.\n .\"`` \_--\" >:. . . . .`.  . . __..,-|\" . ..::::::::::::::`--\"\"-:.\n\' ..`\J.-  \"8-`:. . .  __..--\"\" ...-I  \ `. `::::::::::::::::::::\".\n`/\'\\88o. ,O \  `:.--\"\"....:|:::\'\'\'`\'\ =\'. }-._\'::::::::::::::::::|\n8  8|PP|\"(:. \-\" \"\"`:::::::|:::.((::=\'/ .\\ \"\"-.:_ \':::::::::::\'\'_.\'  _..\n 8  8|::/ \`::Y  _____`:::::|::::.\\[ .\ \"/\"..* *\"-. \'\'\'__..--\"\")\,\"\".-.\_\n`\b d/\"\"===\==V::.--..__`:::|:::::.|,\'*.\"\".:.. \"_-.*`.\"\"    _.-\"-\"\"\? \"_=``.\n\\`\".`\"\' .: :-.::.        `:|:::.\'.\'*.\' __..--\"\"   `.*`:--\"\".-\"?,  .)=\"\"`\ \\ \\ \n `.``...\'\'_/   ``::      _\\--.\'.\'*.\'-\"\"   _..-._ _..>.*;-\"\"@_.-/-\" `\.-\"\"\"-.\\ \n   `-::--\"            .-\"@\"}.\'.\'*.:)     .\"\` \ \`.--\'_`-\'     `\. \-\'-\"\"-   `.\n                     <\  _...\'*.\'      .\' \.`\ `\ \\\"\"         `\ `\' \' .-.\   |\n                     _\\ \"\" .---\'        -\. `\.-\"\"\"-.\           \`|    ._)/   \'\n                   .\"\.`-\"\`.         `\. \-\'-\"\"-   `.           \\  `---\"   /\n                 .\' \.`\ `\ \\        `\ `\' \' .-.\   |            `.       _/\n                 -\. `\.-\"\"\"-.\        \`|    ._)/   \'              `-..--\"\n                `\. \-\'-\"\"-   `.        \\  `---\"   /\n                `\ `\' \' .-.\   |         `.       _/\n                 \`|    ._)/   \'           `-..--\"\n                  \\  `---\"   /\n                   `.       _/\n                     `-..--\" "],
            "00000Z" : ["mars pathfinder lander nasa","[\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"]\n[ \--------MARS PATHFINDER MISSION - 1997-----~~~~~~~/ ]\n[ |                                          {USA ///} ]\n[ |      ...Go America! Mars or bust!!       {32 /*\/} ]\n[ |                                          {  /* *\} ]\n[ |                                           ~~~~~~~| ]\n[ |              __                       _          | ]\n[ |             /\ `\_                   /\`\_       | ]\n[ |            /  ~   \      .          /  ~  \      | ]\n[ |___________/________\_____|_________/_______\_____| ]\n[ |   .^^____  ^       ______|_^.^  ___ ^ .  _ .^^  .| ]\n[ |.^. _/   _\_^  Q]-,  | __ |_  ^ |   \ ^^ / \  ^. ^| ]\n[ | ^ |    \'   \.     \_|/__\_|_ ^ \____\.^ \__\ ^ ^.| ]\n[ |^.^\____\____\^.^  (o):(o):(o)::::::::::::::::::::| ]\n[ /--------------------------------------------------\ ]\n\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\""],
            "000010" : ["alien","            ____\n     _,-ddd888888bbb-._\n   d88888888888888888888b\n d888888888888888888888888b\n6888888888888888888888888889\n68888b8\"\"8q8888888p8\"\"8d88889\n`d8887     p88888q     4888b\'\n `d8887    p88888q    4888b\'\n   `d887   p88888q   488b\'\n     `d8bod8888888dob8b\'\n       `d88888888888d\'\n         `d8888888b\'\n           `d8888b\'\n             `bd\'"],
            "000011" : ["alien","      .--.   |V|\n     /    \ _| /\n     q .. p \ /\n      \--/  //\n     __||__//\n    /.    _/\n   // \  /\n  //   ||\n  \\  /  \\ \n   )\|    |\n  / || || |\n  |/\| || |\n     | || |\n     \ || /\n   __/ || \__\n  \____/\____/"],
            "000012" : ["alien","     _____\n ___/     \___\n`-._)     (_,-`\n    \O _ O/\n     \ - /\n      `-(\n       ||\n      _||_\n     |-..-|\n     |/. \|\n     |\__/|\n   ._|//\\|_,\n   `-((  ))-\'\n    __\\//__\n    >_ /\ _<,\n      \'\'"],
            "000013" : ["alien","                                                      _____\n                         .() .\'()                    ( .--.)\n                 .---.  / / / .\'                     /.)  \'\n               .\'     )/ /-/ /  .\'()                ((/>\n             .\'    .---.( / (`./  .\'                \n           .\'     (-./  \\\_//  .\'     _____         \n  ,-._.   /        <\//  \`--\_/\    .\'     `-._       <,. \/>\n,,== \> \/    .\'.-\' <\//  \   |  `---\    `--.  `-._/>_/>/>  )\n    `(__/  (  |-<____<\/ .-\')-+\'``\'`\'`\       `.   _ __ __ _ \\ \n        \.-<\ )--------)/  /      ///--\        )-\' \> \> \>`\'\n          / )/        // /\'`-----\'      `-.    (___        `-._  _\n        ,(   )\n                / ||-- \                  / | ---\`         //---\'"],
            "000014" : ["alien",".     .       .  .   . .   .   . .    +  .\n  .     .  :     .    .. :. .___---------___.\n       .  .   .    .  :.:. _\".^ .^ ^.  \'.. :\"-_. .\n    .  :       .  .  .:../:            . .^  :.:\.\n        .   . :: +. :.:/: .   .    .        . . .:\\ \n .  :    .     . _ :::/:               .  ^ .  . .:\\ \n  .. . .   . - : :.:./.                        .  .:\\ \n  .      .     . :..|:                    .  .  ^. .:|\n    .       . : : ..||        .                . . !:|\n  .     . . . ::. ::\(                           . :)/\n .   .     : . : .:.|. ######              .#######::|\n  :.. .  :-  : .:  ::|.#######           ..########:|\n .  .  .  ..  .  .. :\ ########          :######## :/\n  .        .+ :: : -.:\ ########       . ########.:/\n    .  .+   . . . . :.:\. #######       #######..:/\n      :: . . . . ::.:..:.\           .   .   ..:/\n   .   .   .  .. :  -::::.\.       | |     . .:/\n      .  :  .  .  .-:.\":.::.\             ..:/\n .      -.   . . . .: .:::.:.\.           .:/\n.   .   .  :      : ....::_:..:\   ___.  :/\n   .   .  .   .:. .. .  .: :.:.:\       :/\n     +   .   .   : . ::. :.:. .:.|\  .:/|\n     .         +   .  .  ...:: ..|  --.:|\n.      . . .   .  .  . ... :..:..\"(  ..)\"\n .   .       .      :  .   .: ::/  .  .::\\ "],
            "000015" : ["alien","     _                      _______                      _\n  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_\n dP\'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb\n V      ~\"Mb          dOOOOOOOOOOOOOOOOOb          dM\"~      V\n          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM\'\n           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP\'\n      __     `YMMM| OP\'~\"YOOOOOOOOOOOP\"~`YO |MMMP\'     __\n    ,dMMMb.     ~~\' OO     `YOOOOOP\'     OO `~~     ,dMMMb.\n _,dP~  `YMba_      OOb      `OOO\'      dOO      _aMMP\'  ~Yb._\n\n             `YMMMM\`OOOo     OOO     oOOO\'/MMMMP\'\n     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO\'dMMP~\'       ,aa.\n   ,dMYYMba._         `OOOOOOOOOOOOOOOOO\'          _,adMYYMb.\n  ,MP\'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP\'   `YM.\n  MP\'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM\n  YMb           ~YMMMM\`OOOOI`````IOOOOO\'/MMMMP~           dMP\n   `Mb.           `YMMMb`OOOI,,,,,IOOOO\'dMMMP\'           ,dM\'\n     `\'                  `OObNNNNNdOO\'                   `\'\n                           `~OOOOO~\'"],
            "000016" : ["alien","                                .do-\"\"\"\"\"\'-o..                         \n                             .o\"\"            \"\"..                       \n                           ,,\'\'                 ``b.                   \n                          d\'                      ``b                   \n                         d`d:                       `b.                 \n                        ,,dP                         `Y.               \n                       d`88                           `8.               \n ooooooooooooooooood888`88\'                            `88888888888bo, \nd\"\"\"    `\"\"\"\"\"\"\"\"\"\"\"\"Y:d8P                              8,          `b \n8                    P,88b                             ,`8           8 \n8                   ::d888,                           ,8:8.          8 \n:                   dY88888                           `\' ::          8 \n:                   8:8888                               `b          8 \n:                   Pd88P\',...                     ,d888o.8          8 \n:                   :88\'dd888888o.                d8888`88:          8 \n:                  ,:Y:d8888888888b             ,d88888:88:          8 \n:                  :::b88d888888888b.          ,d888888bY8b          8 \n                    b:P8;888888888888.        ,88888888888P          8 \n                    8:b88888888888888:        888888888888\'          8 \n                    8:8.8888888888888:        Y8888888888P           8 \n,                   YP88d8888888888P\'          \"\"888888\"Y            8 \n:                   :bY8888P\"\"\"\"\"\'\'                     :            8 \n:                    8\'8888\'                            d            8 \n:                    :bY888,                           ,P            8 \n:                     Y,8888           d.  ,-         ,8\'            8 \n:                     `8)888:           \'            ,P\'             8 \n:                      `88888.          ,...        ,P               8 \n:                       `Y8888,       ,888888o     ,P                8 \n:                         Y888b      ,88888888    ,P\'                8 \n:                          `888b    ,888888888   ,,\'                 8 \n:                           `Y88b  dPY888888OP   :\'                  8 \n:                             :88.,\'.   `\' `8P-\"b.                   8 \n:.                             )8P,   ,b \'  -   ``b                  8 \n::                            :\':   d,\'d`b, .  - ,db                 8 \n::                            `b. dP\' d8\':      d88\'                 8 \n::                             \'8P\" d8P\' 8 -  d88P\'                  8 \n::                            d,\' ,d8\'  \'\'  dd88\'                    8 \n::                           d\'   8P\'  d\' dd88\'8                     8 \n :                          ,:   `\'   d:ddO8P\' `b.                   8 \n :                  ,dooood88: ,    ,d8888\"\"    ```b.                8 \n :               .o8\"\'\"\"\"\"\"\"Y8.b    8 `\"\'\'    .o\'  `\"\"\"ob.           8 \n :              dP\'         `8:     K       dP\'\'        \"`Yo.        8 \n :             dP            88     8b.   ,d\'              ``b       8 \n :             8.            8P     8\"\"\'  `\"                 :.      8 \n :            :8:           :8\'    ,:                        ::      8 \n :            :8:           d:    d\'                         ::      8 \n :            :8:          dP   ,,\'                          ::      8 \n :            `8:     :b  dP   ,,                            ::      8 \n :            ,8b     :8 dP   ,,                             d       8 \n :            :8P     :8dP    d\'                       d     8       8 \n :            :8:     d8P    d\'                      d88    :P       8 \n :            d8\'    ,88\'   ,P                     ,d888    d\'       8 \n :            88     dP\'   ,P                      d8888b   8        8 \n \'           ,8:   ,dP\'    8.                     d8\'\'88\'  :8        8 \n             :8   d8P\'    d88b                   d\"\'  88   :8        8 \n             d: ,d8P\'    ,8P\"\"\".                      88   :P        8 \n             8 ,88P\'     d\'                           88   ::        8 \n            ,8 d8P       8                            88   ::        8 \n            d: 8P       ,:  -hrr-                    :88   ::        8 \n            8\',8:,d     d\'                           :8:   ::        8 \n           ,8,8P\'8\'    ,8                            :8\'   ::        8 \n           :8`\' d\'     d\'                            :8    ::        8 \n           `8  ,P     :8                             :8:   ::        8 \n            8, `      d8.                            :8:   8:        8 \n            :8       d88:                            d8:   8         8 \n ,          `8,     d8888                            88b   8         8 \n :           88   ,d::888                            888   Y:        8 \n :           YK,oo8P :888                            888.  `b        8 \n :           `8888P  :888:                          ,888:   Y,       8 \n :            ``\'\"   `888b                          :888:   `b       8 \n :                    8888                           888:    ::      8 \n :                    8888:                          888b     Y.     8, \n :                    8888b                          :888     `b     8: \n :                    88888.                         `888,     Y     8: \n ``ob...............--\"\"\"\"\"\'----------------------`\"\"\"\"\"\"\"\"\'\"\"\"`\'\"\"\"\"\""],
            "000017" : ["alien","                            ______\n                         ___)    (___\n                      __/     __     \__\n                     /     \_/  \_/     \\ \n                    /      / \__/ \      \\ \n                   |          /\          |\n                  /       ---(  )---       \\ \n                 |            \/            |\n                 | ........................ |\n                / ._________/    \_________. \\ \n               | ./ _________    _________ \. |\n               |./ //#/\###())~~(()###/\#\\ \.|\n               |/ //#([])##// ~~ \\##([])#\\ \|\n               | //###\/##//  ~~  \\##\/###\\ |\n               | \\######//   ~~   \\######// |\n                \             /\             /                  .^. .^.\n                 )      __   !II!   __      (                   |~| |~|\n                /\' .___//    !II!    \\___. \'\                  |~| |~|\n               (  \' .__/     [II]     \__. \'  )         __      |~| |~|\n                \  \'          YY          \'  /          \)\_    |~| |~|\n                 \  \'  |   ________   |  \'  /            \~~\   |~~V~~|\n                  \  \' | _/\'      \'\_ | \'  /              \~~\_ |~~|~~~\\ \n                   \  \'|/____________\|\'  /                \~~~\~~~~~~~~)\n                    \   V___======___V   /                  \~~~\~~~~~~/\n                     \  V   \____/   V  /                    \~~~|~~~~~\\ \n                      \ V   ~~  ~~   V /                      )~~|~~~~~~)\n                       \V  ~~\~~/~~  V/                       \~~~~~~~~/\n                       _V ~~~~\/~~~~ V_                        \~~~~~~|\n                   ___/ V\____/\____/V \_____                   \~~~~~|\n                __/ :   V    :  :    V   :  :\___                |====|\n              _/\' .\' .\' V  .\' .\' .\'  V .\' .\' .\' .\_              |.\' .|\n             /:  :  :  :  :  :  :  :  :  :  :  :  :\             |  : |\n            /. `. `. `. `. `. `. `. `. `. `. `. `. `\            |`. `|\n           /  :  :  :  :  :  :  :  :  :  :  :  :  :  \           |  : |\n          / .\' .\' .\' .\' .\' \\  \'  // \' .\' .\' .\' .\' .\' \          |.\' .|\n         / :  :  :  :  :    ))   ((   :  :  :  :  :  : \         |  : |\n        |`. `. `. `. `. `. ((  .  )) . `. `. `. `. `. `.\        |`. `|\n        |  :  :  :  :  :    ))   ((   :  :  :  :  :  :  :\       |  : |\n       / .\' .\'  \' .\' .\' .\' ((  \'  )) \' .\' .\' .\'  \' .\' .\' .|      /.\' .|\n      | :  : //  :  :  :    ))   ((   :  :  :   \\:  :  : |     |:  : |\n      |. `. || `. `. `. `. ((  .  )) . `. `. `.  ||`. `. `.\    | `. `\\ \n     /  :  :||   :  :  :    ))   ((   :  :  :  : ||  :  :  :|   |:  :  |\n    | .\' .\' || .\' .\' .\' .\' ((  \'  )) \' .\' .\' .\'  ||.\' .\' .\' |   | .\' .\'|\n    |:  :  :||   :  :  :    ))   ((   :  :  :  : ||  :  :  : \  |:  :  |\n   /. `. `. || `. `. `. `. ((  .  )) . `. `. `.  ||\. `. `. `.\ | `. `.|\n  |  :  :  : \\  :  :  :  :  :  : _   :  :  :   //  \:  :  :  :\|:  :  |\n  |.\' .\' .\' .\'\\  .\' .\' .\' . _ \' ._\ \' .\' .\' . //|   \.\' .\' .\' .| .\' .\'|\n./:  :  :  :  :\\   :  :  : /_  :  \\ :  :   _// |    \ :  :  : |:  :  |\n|. `. `. `. __ `\\_  `. `. // `. `. \\______/_/ `|     | `. `. `| `. `.|\n| :/ :  :  /  |  \_\______// :  :  : \______/  : |     |:  :  : |:  :  |\n.\'|.\' .\' ./   |.\' .\______/.\' .\' .\' .\' .\' .\' .\' .|      \.\' .\' .\' .\' .\'|\n  |  :  :|    \  :  :  :  :  :  :  :  :  :  :  :/        \ : o   :  :  |\n`/ `. `. |     |. `. `. `. `. `. `. `. `. `. `.|          | o  `. `. `.|\n| :  :  /      | :  :  :  :  :  :  :  :  :  :  |          | o :  :  :  |\n|\' .\' .|       |\' .\' .\' .\' .\' .\' .\' .\' .\' .\' .\'|           \ o .\' .\' .\'|\n  :  : |       | :  :  :  :  :  :  :  :  :  :  :\           \ o  :  :  |\n`. `. /       /`. `. `. I  `. `. `. `. ` I . `. `\           \ oo `  o.|\n  :  |       /:  :  :  : I   :  :  :  :  I  :  :  \           \_ oooo  |\n.\' .\'|      /\' .\' .\' .\'  I .\' .\' .\' .\' . I \' .\' .\' \            \_____/\n  : /      /  :  :  :  : I   :  :  :  : I   :  :  : \\ \n`. |      | `. `. `. `.  I `. `. `. `.  I `. `. `. `.\\ \n  :|      |:  :  :  :  : I   :  H H   : I   :  :  :  :\\ \n.\' |     /\' .\' .\' .\' .\' . I \' . H H .\'  I .\' .\' .\' .\' .\\ \n  :|    |  :  :  :  :  :   I :  H H    I :  :  :  :  :  \\ \n`. |    |`. `. `. `. `. `. I  ` L L `. I  `. `. `. `. `. \\ \n  :|    |  :  :  :  :  :  : I    H H  I  :  :  :_ :  :  : \\ \n.\' |    |.\' .\' .\' .\' .\' .\' . I \' H H I .\' .\' .\' .\ .\' .\' .\'\\ \n  :|    |  :  :___  :  :  :   I  H HI :  :  :  :  \  :  :  :\\ \n`. |    |`. `.|   |. `. `. `.  I H H . `. ` _`. `.|\. `. `. `|\n  :|    /  :  |   | :  :  :  :  IH H  :  : | _ :  | \:  :  : |\n.\' |   | .\' .\'|   |\' .\' _  .\' .\' H H \' .\'  ||   .\'|  \.\' .\' .|\n  :|   |:  :  |   | :  _ |   :   H H  :   //   :  |   | :  : |\n`. /   | `. `./   |. `. || `. `. H H . ` //  `. `.|   |. `. `|\n  |    |:  : |    | :  : \\  :   H H  :_//  :  :  |   | :  : |\n.\'|    / .\' .|    /\' .\' . \\  .\' H H \' _/ .\' .\' .\'\   |\' .\' .|\n  |   | :  : |   |  :  :   \\    H H  :  :  :  :  :|  | :  : |\n`.|   |. `. `|   |`. `. `.  \\_. H H . `. `. `. `. |  |. `. `|\n  |   | :  :/   |:  :  :  :  \_  H H  :  :  :  :  :|  | :  : |\n.\'|   |\' .\' |  |\' .\' .\' .\' .\' .\' H H \' .\' .\' .\' .\' |  |\' .\' .|\n  |   | :  :|  | :  :  :  :  :   H H  :  :  :  :  :|  | :  : |\n`.|  /`. `. |  |. `. `. `. `. `. `. `. `. `. `. `. |   \ `. `|\n  / |:  :  :/  / :  : __  :  :  :  :  :  :  :__   :\    |  :  \\ \n.|  | .\' .\'|  |.\' .\' |XX\\' .\' .\' .\' .\' .\' .\'/XX|.\' .\   |.\' .\'|\n.|  /:  :  |  |  :  :  \X\:  :  :  :  :  : /X/ :  :  |  |  :  |\n`| |. `. `.|  |`. `. `. \X\_. `. `. `. `._/X/`. `. `.|  |`. `.|\n.| | :  :  |  |  :  :  : \XX\_  :  :  :_/XX/:  :  :  |  |  :  |\n.| |\' .\' ./   /.\' .\' .\' .\' \XX\\' .\' .\'/XX/.\' .\' .\' .\'|  |.\' .\'|\n.| | :  :|   |:  :  :  :  :  \X\_____/X/ :  :  :  :  |  |  :  |\n`| |. `. |   | `. `. `. `. `. |XXXXXXX|`. `. `. `. `.|  \`. `.|\n.| | :  :|   |:  :  :  :  :  :|XX| |XX|  :  :  :  :  |   | :  |\n.| |\' .\' |   | .\' .\' .\' .\' .\'  \ |V| / .\' .\' .\' .\' .\'|   |\' .\'|\n.| / :  :|   |:  :  :  :  :  : /\/ \/\:  :  :  :  :  |   | :  |\n=||`. `./    | `. `. `. `. `. |       |`. `. `. `. `.|   |. `.|\n~\|  : |     |:  :  :  :  :  :|       |  :  :  :  :  |   | :  |\n~~|.\' .|      \.\' .\' .\' .\' .\' |       |.\' .\' .\' .\' .\'|    \ .\' \\ \n~~|  : |       | :  :  :  :  :|       |  :  :  :  :  |     \  : \\ \n~~|`. `|       |. `. `. `. `. |       |`. `. `. `. `.|      \. `.|\n_~|  : |        \:  :  :  :  :|       |  :  :  :  : /        |:  |\n.||.\' .|         |.\' .\' .\' .\' |       |.\' .\' .\' .\' |         |===|\n.||  : \         |  :  :  :  :|       |  :  :  :  :|         /~~~\\ \n  V\. `.|        |`. `. `. `. |       |`. `. `. `. |        |~~~~~\\ \n    |===|        |  :  :  :  :|       |  :  :  :  :|        \~~~~~~)\n    /~~~\        |.\' .\' .\' .\' |       |.\' .\' .\' .\' |         )~~~~/\n   /~~~~~|        \ :  :  :  :|       |  :  :  :  /         /~_~~~\\ \n  (~~~~~~/         | `. `. `. |       |`. `. `. `|         |~| |~~~)\n   \~~~~(          |:  :  :  :|       |  :  :  : |         |~| |~~/\n   /~~~_~\         | .\' .\' .\' |       |.\' .\' .\' .|          V  |~|\n  (~~~| |~|        |:  :  :  :|       |  :  :  : |             |~|\n   \~~| |~|        | #. `. `. `\     / `. `. `.#`|             |~|\n    |~|  V        / : #:  : #:  )   ( : #:  : #:  \            |~|\n    |~|           )\' .# .\' #\' .(     ) .\'#.\' .# .\'(             V\n    |~|           \ : ###### :  )   ( :  ######:  /\n    |~|           /. `# `. #. `(     ) `.#`. `# `.\\ \n     V            ) : #:  :# :  )   ( :  #  : #:  (\n                  \\' .# .\' .# ./     \ .# .\' .# .\'/\n                   |:# :  :  :|       |  :  :  # |\n                   | `. `. `. |       |`. `. `. `|\n                   |:  :  :  :|       |  :  :  : |\n                   | .\' .\' .\' \       /.\' .\' .\' .|\n                   |:  :  :  : |     |:  :  :  : |\n                  /. `/   |`. `|     | `. |   \ `.\\ \n                 |  :/     \ : |     |:  /     \  :|\n                 |.\'[  ( )  ] .|     | .[  ( )  ]\' |\n                 |  [       ]: |     |: [       ] :|\n                 |`. \     /. `|     | `.\     /`. |\n                  \ : \   |  : |     |:  :|   /:  /\n                   \ .\' .\' .\' /       \.\' .\' .\' ./\n                    |  :  :  |         | :  :  :|\n                    |`. `. `.|         |. `. `. |\n                    |  :  :  |         | :  :  :|\n                     \\' .\' .\'|         |\' .\' .\'/\n                      \:  :  |         | :  : /\n                       |`. `.|         |. `. |\n                       |  :  |         | :  :|\n                       |.\' .\'|         |\' .\' |\n                       |  :  |         | :  :|\n                       |`. `.|         |. `. |\n                      /:  :  |         | :  : \\ \n                     |\' .\' .\'|         |\' .\' .\'|\n                     | :  :  |         | :  :  |\n                     |. `. `.|         |. `. `.|\n                     | :  :  |         | :  :  |\n                     |\' .\' .\'|         |\' .\' .\'|\n                    /  :  :  |         | :  :  :\\ \n                   / `. `. `./         \. `. `. `\\ \n                  / :  :  : |           |:  :  :  \\ \n                 /.\' .\' _/ .|           | .\_.\' .\' \M\n                /:  : _/  :/             \  :\_:  : \E\n               /. `._/ |`./               \. | \_. `.\P\n              /  :_/  /: /                 \: \  \_  :\H\n             / ._/   /\' /                   \ \'\   \_ .\\ \n            /__/    |  /                     \  |    \__\\ \n                    |_/                       \_|"],
            "000018" : ["satellite star ship","                   /\\ \n                  /\'\'\\ \n                 /    \\ \n                /      \\ \n               /        \\ \n              /          \\ \n             \'------------\'\n              |__________|\n              /----/\----\\ \n             /|    ||    |\\ \n            //|____||____|\\\ \n           //  |   ||   |  \\\ \n          / |  |___||___|  | \\ \n          | |   \'._||_.\'   | |\n          | |    |_||_|    | |\n          | |  .\'  ||  \'.  | |\n          | | /    ||    \ | |\n          | ||     ||     || |\n          | ||     ||     || |\n          | | \    ||    / | |\n          | |  \'. _||_ .\'  | |\n          | | _    ||    _ | |\n          | |/ \_.\'||\'._/ \| |\n          | |\_/ \'.||.\' \_/| |\n          | |     _||_     | |\n         /| |  .\'  ||  \'.  | |\\ \n        / \'.| /    ||    \ |.\' \\ \n       /   |||     ||     |||   \\ \n      /    |||     ||     |||    \\ \n     /     || \    ||    / ||     \\ \n    /____/\||__\'. _||_ .\'__||/\____\\ \n           |_.--^--||--^--._|\n          / .\'/_\'\'\'||\'\'\'_\\'. \\ \n         / /   /___||___\   \ \\ \n        / /     /__||__\     \ \\ \n       / /         ||         \ \\ \n      /.\'          ||          \'.\\ \n     //            ||            \\\ \n  __//_          __||__          _\\__\n \'=====\'        \'======\'        \'=====\'"],
            "000019" : ["satellite star ship","                        A\n                        M\n                        M\n                        M\n                        M\n                        M\n                        M\n                        M\n                       /M\\ \n                      \'[V]\'\n                       [A]\n                      [,-\']\n                      [/\"\]\n                      / _ \\ \n                     / / | \\ \n                    / /_O_| \\ \n                   /______|__\\ \n                   |=_==_==_=|\n                   |  |   |  |\n                  V|  |.V.|__|V\n                  A|  |\'A\'| =|A\n                   |__|___|= |\n                   |__|___| =|\n                   |####|####|\n                  |    o|     |\n                  |     |     |\n                  |     |     |\n                 |      |      |\n                 |      |      |\n                 |      |      |\n                |       |       |\n                |       |       |\n                |-------|-------|\n               |        |        |\n               |        |        |\n               |___.____|____.___|\n              |                   |\n              |___________________|\n             /|HH|      |HH][HHHHHI\n             [|##|      |##][#####I\n             [|##|      |#########I\n             [|##|______|#######m#I\n             [I|||||||||||||||||||I\n             [I|||||||||||||||||||I\n             [|                   |\n             [|    H  H          H|\n             [|    H  H          H|\n             [|    \hdF          V|\n             [|     `\'            |\n             [|    d##b          d|\n             [|    #hn           #|\n             [|     \"\"#          }|\n             [|    \##/          V|\n             [|                   |\n             [|     dh           d|\n             [|    d/\h          d|\n             [|    H\"\"H          H|\n             [|    \"  \"          \"|\n             [|________.^.________|\n             [I########[ ]########I\n             [I###[]###[.]########I\n             [I###|||||[_]####||||I\n             [####II####|        n |\n            /###########|         \" \\ \n            ############|           |\n           /############|            \\ \n           ######\"######|            |\n          /             |####### #####\\ \n          |             |#######.######\n         /              |##############\\ \n         |              |###############\n        /_______________|###############\\ \n        I|||||||||||||||||||||||||||||||I\n        I|||||||||||||||||||||||||||||||I\n        I|||||||||||||||||||||||||||||||I\n        I|||||||||||||||||||||||||||||||I\n        |                               |\n        |-------------------------------|\n        |                               |\n        | [                  U          |\n        | [                  N          |\n        | !                  I          |\n        | [                  T          |\n        | [                  E          |\n        | }                  D          |\n        |                               |\n        |                               |\n        | {                  S          |\n        | [                  T          |\n        | :                  A          |\n        | [                  T          |\n        | [                  E          |\n       /| {  /|              S    |\    |\n      | |   | |                   | |   |\n      | |   | |                   | |   |\n      | |   | |                   | |   |\n      |_|___|_|___________________|_|___|\n      | |   | |                   | |   |\\ \n      | |___| |___________________| |___|]\n      | |###| |###################| |###|]\n      | |###| |###################| |###|]\n      | |###| |\"\"\"\"\"\"\"\"\"\"#########| |\"\"\"|]\n      | |###| |         |#########| |   |]\n       \|####\|---------|#########|/----|]\n        |#####|         |#########|     |/\n        |#####|         |#########|     |\n       /]##### |        | ######## |    [\\ \n       []##### |        | ######## |    []\n       []##### |        | ######## |    []\n       []##### |        | ######## |    []\n       []##### |        | ######## |    []\n        |#####|---------|#########|-----|\n        |#####|         |#########|     |\n        |#####|         |##H######|     |\n        |#####|         |##H######|     |\n        |#####|         |##H######|     |\n        |#####|_________|##H######|_____|\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |     ####\"\"\"\"\"\"\"  H            |\n        |     ####\"\"\"\"\"\"\"  H            |\n        |     \"\"\"\"\"\"\"\"\"\"\"  H            |\n        |     \"\"\"\"\"\"\"\"\"\"\"  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |                  H            |\n        |__________________H____________|\n        |                  H            |\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        I||||||||||||||||||H||||||||||||I\n        |#####|         |##H######|     |\n        |#####|         |##H######|     |\n        |#####|  H   H  |##H######|   H |\n        |#####|  H   H  |##H######|   H |\n        |#####|  H   H  |##H######|   H |\n        |#####|  \h_dF  |##H######|   Vm|\n        |#####|   `\"\'   |##H######|    \"|\n        |#####|         |##H######|     |\n        |#####|  /###\  |##H######|   /#|\n        |#####|  #   \'  |##H######|   # |\n        |#####|  \###\  |##H######|   \#|\n        |#####|  .   #  |##H######|   . |\n        |#####|  \###/  |##H######|   \#|\n        |#####|         |##H######|     |\n        |#####|    H    |##H######|     [\n        |#####|   dAh   |##H######|    H|\n        |#####|  dF qL  |##H######|   dF|\n        |#####|  HhmdH  |##H######|   Hm|\n        |#####|  H   H  [%]H#apx##|   H |\n        |#####|         |##H######|     |\n        |#####A         |##H######A     |\n        |####| |        |##H#####|#|    |\n        |####| |        |##H#####|#|    |\n        |###|   |       |##H####|###|   |\n        |###|   |       |##H####|###|   |\n        |##|     |      |##H###|#####|  |\n        |#-|     |      |##H###|#####|-_|\n     _-\"==|       |     |##H##|#######|==\"-_\n  _-\"=[]==|       |     |##H##|#######|==[]=\"-_\n |========|_______|_____|##H##|#######|========|\n !=======|=========|____|##H#|=========|=======!\n         !=========! /#####\ !=========!\n          /#######\ /#######\ /#######\\ \n         d#########V#########V#########h\n         H#########H#########H#########H\n        |###########H#######H###########|\n        |###########|\"\"\"\"\"\"\"|###########|\n         \"\"\"\"\"\"\"\"\"\"\"         \"\"\"\"\"\"\"\"\"\"\""],
            "00001a" : ["satellite star ship","           ___\n     |     | |\n    / \    | |\n   |--o|===|-|\n   |---|   |d|\n  /     \  |w|\n | U     | |b|\n | S     |=| |\n | A     | | |\n |_______| |_|\n  |@| |@|  | |\n___________|_|_"],
            "00001b" : ["satellite star ship","                 ____\n                /___.`--.____ .--. ____.--(\n                       .\'_.- (    ) -._\'.\n                     .\'.\'    |\'..\'|    \'.\'.\n              .-.  .\' /\'--.__|____|__.--\'\ \'.  .-.\n             (O).)-| |  \    |    |    /  | |-(.(O)\n              `-\'  \'-\'-._\'-./      \.-\'_.-\'-\'  `-\'\n                 _ | |   \'-.________.-\'   | | _\n              .\' _ | |     |   __   |     | | _ \'.\n             / .\' \'\'.|     | /    \ |     |.\'\' \'. \\ \n             | |( )| \'.    ||      ||    .\' |( )| |\n             \ \'._.\'   \'.  | \    / |  .\'   \'._.\' /\n              \'.__ ______\'.|__\'--\'__|.\'______ __.\'\n             .\'_.-|         |------|         |-._\'.\n            //\\  |         |--::--|         |  //\\\ \n           //  \\ |         |--::--|         | //  \\\ \n          //    \\|        /|--::--|\        |//    \\\ \n         / \'._.-\'/|_______/ |--::--| \_______|\`-._.\' \\ \n        / __..--\'        /__|--::--|__\        `--..__ \\ \n       / /               \'-.|--::--|.-\'               \ \\ \n      / /                   |--::--|                   \ \\ \n     / /                    |--::--|                    \ \\ \n _.-\'  `-._                 _..||.._                  _.-` \'-._\n\'--..__..--\'               \'-.____.-\'                \'--..__..-\'"],
            "00001c" : ["satellite star ship","        _..-.._\n     .\'  _   _  `.\n    /_) (_) (_) (_\\ \n   /               \\ \n   |\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'|\n  /                 \\ \n |                   |\n |-------------------|\n |                   |\n |                   |\n |\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'|\n |             .--.  |\n |            //  \\=|\n |            ||- || |\n |            \\__//=|\n |             \'--\'  |\n |...................|\n |___________________|\n |___________________|\n |___________________|\n |___________________|\n   /_______________\  "],
            "00001d" : ["guitar","       ___ \n     o|* *|o \n     o|* *|o \n     o|* *|o \n      \===/ \n       ||| \n       ||| \n       ||| \n       ||| \n    ___|||___ \n   /   |||   \ \n  /    |||    \ \n |     |||     | \n  \   (|||)   / \n   |   |||   | \n  /    |||    \ \n /     |||     \ \n/      |||      \ \n|     [===]     | \n \             / \n  \'.         .\' \n    \'-------\' "],
            "00001e" : ["electric guitar","                  _,., \n                ,\'   ,\' \n               /   ,\' \n              /   ,  \n             /   , \n            /   \' \n           /   ,\' \n           \'.__| \n            |  | \n            |__| \n            |  | \n            |__| \n            |  | \n            |__| \n            |  | \n            |__| \n            |, | \n            |--| \n            |__| \n            |  | \n            |--| \n            |__| \n            |__|        ,-. \n            |__|\'     ,\'  / \n       _,.-\'     \',_,\' o / \n      /     8888        / \n      |                / \n       1              / \n       `L   8888     / \n        |           / \n       /    ====    \ \n      /     ____     \ \n     /     (____)  o  \ \n    /             o    \ \n   /             o     ,\' \n  /               _,.\'^ \n /        __,.-\"~^ \n\',,..--~~^ "],
            "00001f" : ["santa claus new year","                    _... \n              o_.-\"`    `\ \n       .--.  _ `\'-._.-\'\"\"-;     _ \n     .\'    \`_\_  {_.-a\"a-}  _ / \ \n   _/     .-\'  \'. {c-._o_.){\|`  | \n  (@`-._ /       \{    ^  } \\ _/ \n   `~\  \'-._      /\'.     }  \}  .-. \n     |>:<   \'-.__/   \'._,} \_/  / ())   \n     |     >:<   `\'---. ____\'-.|(`\"` \n     \            >:<  \\_\\_\ | ; \n      \                 \\-{}-\/  \ \n       \                 \'._\\\'   /) \n        \'.                       /( \n          `-._ _____ _ _____ __.\'\ \ \n            / \     / \     / \   \ \  \n         _.\'/^\\'._.\'/^\\'._.\'/^\\'.__) \ \n     ,==\'  `---`   \'---\'   \'---\'      ) \n     `\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"` "],
            "00001g" : ["electric guitar","           ._.-..-._. \n           | Gibson | \n         0-| o    o |-0 \n           |        | \n         0-| o    o |-0 \n           |        | \n         0-| o    o |-0 \n           |        | \n           \'.      .\' \n             \'____\' \n             |    | \n             |    | \n             |____| \n             |    | \n             |    | \n             |____| \n             |    | \n             |    | \n             |____| \n             |    | \n             |    | \n             |----| \n             |    | \n             |____| \n             |    | \n             |____| \n             |    | \n             |____| \n             |____| \n             |____| \n        _..--|____|       _ \n     .\'      |____|      \' \' \n    .        |____|\'.__.\'   \' \n    :  (o)   ______         \' \n    \'       |OOOOOO|       \' \n     \'      |______|      \' \n      \'                  \' \n       \'                \' \n       :                : \n       \'                \' \n      \'                  \' \n    .\'       ______       \'. \n   \'        |      |        \' \n  \'         |OOOOOO|         \' \n \'          ________          \' \n.          (________)          . \n:                              : \n\'           ________       o   \' \n .         0________0   o      . \n  .                        o  . \n   .                    o    .  \n    \'.                     .\' \n      \'.._             _..\' \n          ^\'--.....--\'^  \n                8 "],
            "00001h" : ["guitar violin","                            ,-. \n                           ((o)) \n                      _  ,-,,-\' \n                     ( `/=//_ \n                    _  /=/=\'_) \n                   ( `/=//_ \n                     /=/=\'_) \n                    /_/ | \n                   / /`.\' \n                  / // \n                 / // \n                / // \n               / // \n              / / | \n           _ / / -._ \n         .\' / /     `. \n        /  / /       `-. \n       /  /_/        \' ` \n      \'             :  \' \n     \'.       ,-  ,-\'.: \n     / /     /.  /  ,-\' \n    /  __   7   / / \n .,\'  \'  ` \'   `._ \n /    |/\|      ,\'. \n/ _   _        / ,\' \n:\' ` | /     ,\' / \n`.   |/ _ , \' ,\' \n   ---\"\"__ ,-\' "],
            "00001i" : ["castle building"," _   |~  _ \n[_]--\'--[_] \n|\'|\"\"`\"\"|\'| \n| | /^\ | | \n|_|_|I|_|_| "],
            "00001j" : ["castle building"," [][][] /\"\"\ [][][] \n  |::| /____\ |::| \n  |[]|_|::::|_|[]| \n  |::::::__::::::| \n  |:::::/||\:::::| \n  |:#:::||||::#::| \n #%*###&*##&*&#*&## \n##%%*####*%%%###*%*# "],
            "00001k" : ["castle building","                             -|             |- \n         -|                  [-_-_-_-_-_-_-_-]                  |- \n         [-_-_-_-_-]          |             |          [-_-_-_-_-] \n          | o   o |           [  0   0   0  ]           | o   o | \n           |     |    -|       |           |       |-    |     | \n           |     |_-___-___-___-|         |-___-___-___-_|     | \n           |  o  ]              [    0    ]              [  o  | \n           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________ \n_____----- |     ]              [ ||||||| ]              [     | \n           |     ]              [ ||||||| ]              [     | \n       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_ \n      ( (__________------------_____________-------------_________) ) "],
            "00001l" : ["castle building","  _______________________________________ \n /                                       \ \n/   _   _   _                 _   _   _   \ \n|  | |_| |_| |   _   _   _   | |_| |_| |  | \n|   \   _   /   | |_| |_| |   \   _   /   | \n|    | | | |     \       /     | | | |    | \n|    | |_| |______|     |______| |_| |    | \n|    |              ___              |    | \n|    |  _    _    (     )    _    _  |    | \n|    | | |  |_|  (       )  |_|  | | |    | \n|    | |_|       |       |       |_| |    | \n|   /            |_______|            \   | \n|  |___________________________________|  | \n\        US Army Corps of Engineers       / \n \_______________________________________/ "],
            "00001m" : ["castle building","               T~~ \n               | \n              /\"\ \n      T~~     |\'| T~~ \n  T~~ |    T~ WWWW| \n  |  /\"\   |  |  |/\T~~ \n /\"\ WWW  /\"\ |\' |WW| \nWWWWW/\| /   \|\'/\|/\"\ \n|   /__\/]WWW[\/__\WWWW \n|\"  WWWW\'|I_I|\'WWWW\'  | \n|   |\' |/  -  \|\' |\'  | \n|\'  |  |LI=H=LI|\' |   | \n|   |\' | |[_]| |  |\'  | \n|   |  |_|###|_|  |   | \n\'---\'--\'-/___\-\'--\'---\' "],
            "00001n" : ["castle building","   /\                                                        /\ \n  |  |                                                      |  | \n /----\                  Lord Dark\'s Keep                  /----\ \n[______]             Where Brave Knights Tremble          [______] \n |    |         _____                        _____         |    | \n |[]  |        [     ]                      [     ]        |  []| \n |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    | \n |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    | \n |             |     |/\'    ____..____    \'\|     |             | \n  \  []        |     |    /\'    ||    \'\    |     |        []  / \n   |      []   |     |   |o     ||     o|   |     |  []       | \n   |           |  _  |   |     _||_     |   |  _  |           | \n   |   []      | (_) |   |    (_||_)    |   | (_) |       []  | \n   |           |     |   |     (||)     |   |     |           | \n   |           |     |   |      ||      |   |     |           | \n /\'\'           |     |   |o     ||     o|   |     |           \'\'\ \n[_____________[_______]--\'------\'\'------\'--[_______]_____________] "],
            "00001o" : ["castle building"," \n                                                |>>> \n                                                | \n                                            _  _|_  _ \n                                           |;|_|;|_|;| \n                                           \\.    .  / \n                                            \\:  .  / \n                                             ||:   | \n                                             ||:.  | \n                                             ||:  .| \n                                             ||:   |       \,/ \n                                             ||: , |            /`\ \n                                             ||:   | \n                                             ||: . | \n              __                            _||_   | \n     ____--`~    \'--~~__            __ ----~    ~`---,              ___ \n-~--~                   ~---__ ,--~\'                  ~~----_____-~\'   `~----~~ "],
            "00001p" : ["castle building","                    |>>>                        |>>> \n                    |                           | \n                _  _|_  _                   _  _|_  _ \n               | |_| |_| |                 | |_| |_| | \n               \  .      /                 \ .    .  / \n                \    ,  /                   \    .  / \n                 | .   |_   _   _   _   _   _| ,   | \n                 |    .| |_| |_| |_| |_| |_| |  .  | \n                 | ,   | .    .     .      . |    .| \n                 |   . |  .     . .   .  ,   |.    | \n     ___----_____| .   |.   ,  _______   .   |   , |---~_____ \n_---~            |     |  .   /+++++++\    . | .   |         ~---_ \n                 |.    | .    |+++++++| .    |   . |              ~-_ \n              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_ \n     ____--`~    \'--~~__ .    |++++ __|----~    ~`---,              ___^~-__ \n-~--~                   ~---__|,--~\'                  ~~----_____-~\'   `~----~ "],
            "00001q" : ["castle building","   ^    / \:/ \      ^               +                        |> \n  / \      ^        / \        *    / \    *              |>  | \n /   \             /   \      OnO  :xxx:  OnO             |  III     |> \n(_____)           (_____)     I I   I I   I I           /-|\ III i>  | \n |   |  _   _   _  |   |      I I   I I   I I         _|__|__III i   ^ \n | O |_| |_| |_| |_| O |     O_O_O_O_O_O_O_O_O     |>\______/III i  ^^^ \n |   |   - _^_     |   |     \_______________/     |   !__!__III/\ ^^^^^ \n |  _|    //|\\  - |   |      I     ___     I     /\\ ////|====IIII === \n |   |   ///|\\\   |  -|      I    / i \    I    /\\\/////|====IIII === \n |-  |_  |||||||   |   |      I   I: i :I   I    | | ||||::::::IIII === \n |   |   |||||||   |-  |      I___I:_i_:I___I    | | ||||      IIII === \n |___|___|||||||___|___|                         ----------------------- \n         (      ( \n          \      \            . o       c ,              0   \0 \n           )      )           `\'#v-- --v#`\'             /0--- :\ \n           |      |            /\'>     <`\              / >  / > \n           (      ) \n            \      \ "],
            "00001r" : ["castle building","  / \               / \ \n /   \             /   \ \n(_____)           (_____) \n |   |  _   _   _  |   | \n | O |_| |_| |_| |_| O | \n |-  |          _  | - | \n |   |   - _^_     |   | \n |  _|    //|\\  - |   | \n |   |   ///|\\\   |  -| \n |-  |_  |||||||   |   | \n |   |   |||||||   |-  | \n |___|___|||||||___|___| \n         (      ( \n          \      \ \n           )      ) \n           |      | \n           (      ( \n            \      \ "],
            "00001s" : ["castle building","                                  |>>> \n                                  | \n                    |>>>      _  _|_  _         |>>> \n                    |        |;| |;| |;|        | \n                _  _|_  _    \\.    .  /    _  _|_  _ \n               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;| \n               \\..      /    ||;   . |    \\.    .  / \n                \\.  ,  /     ||:  .  |     \\:  .  / \n                 ||:   |_   _ ||_ . _ | _   _||:   | \n                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  | \n                 ||:   ||.    .     .      . ||:  .| \n                 ||: . || .     . .   .  ,   ||:   |       \,/ \n                 ||:   ||:  ,  _______   .   ||: , |            /`\ \n                 ||:   || .   /+++++++\    . ||:   | \n                 ||:   ||.    |+++++++| .    ||: . | \n              __ ||: . ||: ,  |+++++++|.  . _||_   | \n     ____--`~    \'--~~__|.    |+++++__|----~    ~`---,              ___ \n-~--~                   ~---__|,--~\'                  ~~----_____-~\'   `~----~~ "],
            "00001t" : ["castle building","       /\         /\                    .           /\ \n      /  \       /  \                   |@>        /  \ \n     /    \     / .  \                  |         /    \ \n    /      \   /  |@> \       /\       / \       /      \ \n   /     /\ \ /   |    \     /  \     /   \     /        \ \n  /     /  \ /  _ | _   \   /    \    | O |    /          _   _   _ \n /     /    \  |_|_|_|   \ /      \   |___|   /          | |_| |_| | \n/     /      \  | O |     /        \  | |_|  /      /\   |         | \n    _   _   _ \ |___|    /          \ |__|| /      /  \  |  O   O  | \n   | |_| |_| |  | |_|   /             | |_|       /    \ |   __ _  | \n   |         |  |__||  /              |_| |      /       |     |   | \n   | O  O  O |  | |_| /               |__ |     /        | O  O  O | \n   |  _      |  _   _   _        ______   |   _   _   _  |  _      | \n   | |__|_ | |_| |_| |_| |______|      |_____| |_| |_| |_| |__|_ |_| \n   |  |   _| |        _  |  | _|  ____     _||        _  |  |    | | \n   |   _| _  ||_|   _|_  | _|_   |||||| |_| _||_|   _|_  |   _| _| | \n   |  __|  |_|  |_       | | |__ |++++|   |_||  |_      ||  __|  |_| \n   |_________|___________|-------------------|___________|_________| \n                                 /_/_/ \n                                /_/_/ "],
            "00001u" : ["castle building","    |>>>                                                      |>>> \n    |                     |>>>          |>>>                  | \n    *                     |             |                     * \n   / \                    *             *                    / \ \n  /___\                 _/ \           / \_                 /___\ \n  [   ]                |/   \_________/   \|                [   ] \n  [ I ]                /     \       /     \                [ I ] \n  [   ]_ _ _          /       \     /       \          _ _ _[   ] \n  [   ] U U |        {#########}   {#########}        | U U [   ] \n  [   ]====/          \=======/     \=======/          \====[   ] \n  [   ]    |           |   I |_ _ _ _| I   |           |    [   ] \n  [___]    |_ _ _ _ _ _|     | U U U |     |_ _ _ _ _ _|    [___] \n  \===/  I | U U U U U |     |=======|     | U U U U U | I  \===/ \n   \=/     |===========| I   | + W + |   I |===========|     \=/ \n    |  I   |           |     |_______|     |           |   I  | \n    |      |           |     |||||||||     |           |      | \n    |      |           |   I ||vvvvv|| I   |           |      | \n_-_-|______|-----------|_____||     ||_____|-----------|______|-_-_ \n   /________\         /______||     ||______\         /________\ \n  |__________|-------|________\_____/________|-------|__________| "],
            "00001v" : ["castle building","                           o                     \n                       _---|         _ _ _ _ _  \n                    o   ---|     o   ]-I-I-I-[  \n   _ _ _ _ _ _  _---|      | _---|    \ ` \' /  \n   ]-I-I-I-I-[   ---|      |  ---|    |.   |  \n    \ `   \'_/       |     / \    |    | /^\|  \n     [*]  __|       ^    / ^ \   ^    | |*||  \n     |__   ,|      / \  /    `\ / \   | ===|  \n  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _| \n  I_I__I_I__I_I  (====(_________)___|_|____|____ \n  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|  \n   |[]      \'|   | []  |`__  . [  \-\--|-|--/-/   \n   |.   | |\' |___|_____I___|___I___|---------|  \n  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |  \n <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \   \n ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>  \n ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [  \n <===>     \' ||||| |   |   | ||||.||  []   <===> \n  \T/  | |-- ||||| | O | O | ||||.|| . |\'   \T/  \n   |      . _||||| |   |   | ||||.|| |     | | \n../|\' v . | .|||||/____|____\|||| /|. . | . ./ \n.|//\............/...........\........../../\\\ \n "],
            "00001w" : ["castle building","                  ^ \n                 / \ \n            ^   _|.|_   ^ \n          _|I|  |I .|  |.|_ \n          \II||~~| |~~||  / \n           ~\~|~~~~~~~|~/~ \n             \|II I ..|/ \n        /\    |II.    |    /\ \n       /  \  _|III .  |_  /  \ \n       |-~| /(|I.I I  |)\ |~-| \n     _/(I | +-----------+ |. )\_ \n     \~-----/____-~-____\-----~/ \n      |I.III|  /(===)\  |  .. | \n      /~~~-----_________---~~~\ \n     `##########!\-#####%!!!!!| |\ \n    _/###########!!\~~-_##%!!!\_/| \n    \##############!!!!!/~~-_%!!!!\ \n     ~)#################!!!!!/~~--\_ \n  __ /#####################%%!!!!/ / \n  \,~\-_____##############%%%!!!!\/ \n  /!!!!\ \ \~-_###########%%%!!!!\ \n /#####!!!!!!!\~-_#######%%%!!!!!!\_ \n/#############!!!\#########%%%!!!!!!\ "],
            "00001x" : ["castle building","                   (   .                   _ _ _ _ _ \n    (   .     .  .=##                      ]-I-I-I-[                    / \n  .=##   .  (      ( .                     \ `  \' /        \\\\' ,      / // \n    ( .   .=##  .       .                   |\'  []          \\\//    _/ //\' \n  .     .   ( .    .        _----|          |.  \'|           \_-//\' /  //<\' \n                             ----|_----|    | \' .|             \ ///  >   \\\` \n    ]-I-I-I-I-[       ----|      |     |    |. ` |            /,)-^>>  _\` \n     \ `   \'_/            |     / \    |    | /^\|            (/   \\ / \\\ \n      []  `__|            ^    / ^ \   ^    | |*||                  //  //\\\ \n      |__   ,|           / \  / ^ ^`\ / \   | ===|                 ((` \n   ___| ___ ,|__        / ^  /=_=_=_=\ ^ \  |, `_| \n   I_I__I_I__I_I       (====(_________)_^___|____|____                  \n   \-\--|-|--/-/       |     I  [ ]__I I_I__|____I_I_|                      \n    |[] `    \'|__   _  |_   _|`__  ._[  _-\--|-|--/-/                       \n   / \  [] ` .|  |-| |-| |-| |_| |_| |_| | []   [] |                 \n  <===>    `  |.            .      .     |    \'    | \n  ] []|  `    |   []    --   []      `   |   [] \'  | \n  <===>.  `   |  .   \'  .       \'  .[]   | \'       |              \n   \_/    .   |       .       \'          |   `  [] |            \n    | []    . |   .  .           ,  .    | ,    .  |                    \n    |    . \'  |       . []  \'            |    []\'  | \n   / \   ..   |  `      .    .     `[]   | -   `   |                      \n  <===>      .|=-=-=-=-=-=-=-=-=-=-=-=-=-|    .   / \                    \n  ] []|` ` [] |`  .  .   _________   .   |-      <===>             \n  <===>  `  \' | \'   |||  |       |  |||  |  []   <===>                       \n   \_/     -- |   . |||  |       |  |||  | .  \'   \_/                      \n  ./|\' . . . .|. . .||||/|_______|\|||| /|. . . . .|\_ "],
            "00001y" : ["castle building","                  [\ \n                  |\)                                ____ \n                  |                               __(_   )__ \n                  Y\          ___               _(          ) \n                 T  \       __)  )--.          (     )-----` \n                J    \   ,-(         )_         `---\' \n               Y/T`-._\ (     (       _)                 __ \n               /[|   ]|  `-(__  ___)-`  |\          ,-(  __) \n               | |    |      (__)       J\'         (     ) \n   _           | |  ] |    _           /;\          `-  \' \n  (,,)        [| |    |    L\'         /;  \ \n             /||.| /\ |   /\         /.,-._\        ___ _ \n            /_|||| || |  /  \        | |{  |       (._.\'_) \n  L/\       | \| | \'` |_ _ {|        | | U |   /\ \n /v^v\/\   `|  Y | [  \'-\' \'--\'\'-\'\'-\"-\'`\'   | ,`^v\ /\,`\ \n/ ,\'./  \.` |[   |       [     __   L    ] |      /^v\  \ \n,\'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_ \n--   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y \n   Y Y  --;`~T   |      }   \####U|[\ _,.-(^) ,-\'  _  (^)__  _ \n  Y  YY   ;\'~~l  |   L     [|\###U\'E\'\  \ \Y-` _  (^) _Y  _ \n Y  Y Y   ;\~~/\{| [      _,\'-\`= = \'.\_ ,`   (^)(^) (^) (^) \n     --   ;\~~~/\|  _,.-\'`_  `.\_..-\'\"  _ . ,_ Y_ Y_ _Y  _Y__ \n    _    _; \~~( Y``   Y (^) / `,      (^)      _   (^) (^) \n   (^)  (^)`._~ /  L \  _.Y\'`  _  ` --  Y - - -(^) - Y - Y - \n    Y    Y    `\'--..,-\'`      (^)   _  -    _   Y ____ \n      --           _    _ --   Y   (^)   _ (^)  ===   ---- \n          __   -  (^)  (^)      --- Y   (^) Y \n      _            Y    Y                Y             lt. "],
            "00001z" : ["castle building","                                                  !_ \n                                                  |*~=-., \n                                                  |_,-\'` \n                                                  | \n                                                  | \n                                                 /^\ \n                   !_                           /   \ \n                   |*`~-.,                     /,    \ \n                   |.-~^`                     /#\"     \ \n                   |                        _/##_   _  \_ \n              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ] \n             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_| \n           !_ |_=_ =-_-_  = =_|           !_ |=_= -    | \n           |*`--,_- _        |            |*`~-.,= []  | \n           |.-\'|=     []     |   !_       |_.-\"`_-     | \n           |   |_=- -        |   |*`~-.,  |  |=_-      | \n          /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  | \n      _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      | \n     [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    | \n      |/#\"     \_=-___=__=__- =-_ -=_ /#\"     \| _ []  | \n     _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\ \n    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \ \n    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \ \n     | _- =-     |-_   | ((* |      |= _=       | -    |___\ \n     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\| \n     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+|| \n     |-_=- _     |=_   =            |=_= -_     |  =   ||+|| \n     |=_- /+\    | -=               |_=- /+\    |=_    |^^^| \n     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  | \n     |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/ \n     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/ \n     | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/ \n     |=_ =       | =_-_| |  | |     |   =_      | -_   | \n     |_=-_       |=_=  | |  | |     |=_=        |=-    | \n^^^^^^^^^^`^`^^`^`^`^^^\"\"\"\"\"\"\"\"^`^^``^^`^^`^^`^`^``^`^``^``^^ "],
            "00001A" : ["castle building","                                 ____                                          \n                              .-\"    `-.      ,                                \n                            .\'          \'.   /j\                               \n                           /              \,/:/#\                /\            \n                          ;              ,//\' \'/#\              //#\           \n                          |             /\' :   \'/#\            /  /#\          \n                          :         ,  /\' /\'    \'/#\__..--\"\"\"\"/    /#\__       \n                           \       /\'\\'-._:__    \'/#\        ;      /#, \"\"\"--- \n                            `-.   / ;#\\']\" ; \"\"\"--./#J       \':____...!        \n                               `-/   /#\  J  [;[;[;Y]         |      ;         \n\"\"\"\"\"\"---....             __.--\"/    \'/#\ ;   \" \"  |     !    |   #! |         \n             \"\"--.. _.--\"\"     /      ,/#\\'-..____.;_,   |    |   \'  |         \n                   \"-.        :_....___,/#} \"####\" | \'_.-\",   | #[\'  |         \n                      \'-._      |[;[;[;[;|         |.;\'  /;\  |      |         \n                      ,   `-.   |        :     _   .;\'    /;\ |   #\" |         \n                      !      `._:      _  ;   ##\' .;\'      /;\|  _,  |         \n                     .#\ \"\"\"---..._    \';, |      .;{___     /;\  ]#\' |__....-- \n          .--.      ;\'/#\         \    ]! |       \"| , \"\"\"--./_J    /          \n         /  \'%;    /  \'/#\         \   !\' :        |!# #! #! #|    :`.__       \n        i__..\'%] _:_   ;##J         \      :\"#...._!   \'  \"  \"|__  |    `--.._ \n         | .--\"\"\" !|\"\"\"\"  |\"\"\"----...J     | \'##\"\" `-._       |  \"\"\"---.._     \n     ____: |      #|      |         #|     |          \"]      ;   ___...-\"T,   \n    /   :  :      !|      |   _______!_    |           |__..--;\"\"\"     ,;MM;   \n   :____| :    .-.#|      |  /\      /#\   |          /\'               \'\'MM;   \n    |\"\"\": |   /   \|   .----+  ;      /#\  :___..--\"\";                  ,\'MM;  \n   _Y--:  |  ;     ;.-\'      ;  \______/#: /         ;                  \'\'MM;  \n  /    |  | ;_______;     ____!  |\"##\"\"\"MM!         ;                    ,\'MM; \n !_____|  |  |\"#\"#\"|____.\'\"\"##\"  |       :         ;                     \'\'MM   \n  | \"\"\"\"--!._|     |##\"\"         !       !         :____.....-------\"\"\"\"\"\" |\' \n  |          :     |______                        ___!_ \"#\"\"#\"\"#\"\"\"#\"\"\"#\"\"\"|   \n__|          ;     |MM\"MM\"\"\"\"\"---..._______...--\"\"MM\"MM]                   |    \n  \"\-.      :      |#                                  :                   |   \n    /#\'.    |      /##,                                !                   |   \n   .\',/\'\   |       #:#,                                ;       .==.       |   \n  /\"\\'#\"\\',.|       ##;#,                               !     ,\'||||\',     |   \n        /;/`:       ######,          ____             _ :     M||||||M     |   \n       ###          /;\"\.__\"-._   \"\"\"                   |===..M!!!!!!M_____|   \n                           `--..`--.._____             _!_                     \n                                          `--...____,=\"_.\'`-.____  "],
            "00001B" : ["castle building","                                o \n                            .-\'\"| \n                            |-\'\"| \n                                |   _.-\'`. \n                               _|-\"\'_.-\'|.`. \n                              |:^.-\'_.-\'`.;.`. \n                              | `.\'.   ,-\'_.-\'| \n                              |   + \'-\'.-\'   J \n           __.            .d88|    `.-\'      | \n      _.--\'_..`.    .d88888888|     |       J\'b. \n   +:\" ,--\'_.|`.`.d88888888888|-.   |    _-.|888b. \n   | \ \-\'_.--\'_.-+888888888+\'  _>F F +:\'   `88888bo. \n    L \ +\'_.--\'   |88888+\"\'  _.\' J J J  `.    +8888888b. \n    |  `+\'        |8+\"\'  _.-\'    | | |    +    `+8888888._-\'. \n  .d8L  L         J  _.-\'        | | |     `.    `+888+^\'.-|.`. \n d888|  |         J-\'            F F F       `.  _.-\"_.-\'_.+.`.`. \nd88888L  L     _.  L            J J J          `|. +\'_.-\'    `_+ `; \n888888J  |  +-\'  \ L         _.-+.|.+.          F `.`.     .-\'_.-\"J \n8888888|  L L\    \|     _.-\'     \'   `.       J    `.`.,-\'.-\"    | \n8888888PL | | \    `._.-\'               `.     |      `..-\"      J.b \n8888888 |  L L `.    \     _.-+.          `.   L+`.     |        F88b \n8888888  L | |   \   _..--\'_.-|.`.          >-\'    `., J        |8888b \n8888888  |  L L   +:\" _.--\'_.-\'.`.`.    _.-\'     .-\' | |       JY88888b \n8888888   L | |   J \ \_.-\'     `.`.`.-\'     _.-\'   J J        F Y88888b \nY888888    \ L L   L \ `.      _.-\'_.-+  _.-\'       | |       |   Y88888b \n`888888b    \| |   |  `. \ _.-\'_.-\'   |-\'          J J       J     Y88888b \n Y888888     +\'\   J    \ \'_.-\'       F    ,-T\"\   | |    .-\'      )888888 \n  Y88888b.      \   L    +\'          J    /  | J  J J  .-\'        .d888888 \n   Y888888b      \  |    |           |    F  \'.|.-\'+|-\'         .d88888888 \n    Y888888b      \ J    |           F   J    -.              .od88888888P \n     Y888888b      \ L   |          J    | .\' ` \d8888888888888888888888P \n      Y888888b      \|   |          |  .-\'`.  `\ `.88888888888888888888P \n       Y888888b.     J   |          F-\'     \\ ` \ \88888888888888888P\' \n        Y8888888b     L  |         J       d8`.`\  \`.8888888888888P\' \n         Y8888888b    |  |        .+      d8888\  ` .\'  `Y888888P\' \n         `88888888b   J  |     .-\'     .od888888\.-\' \n          Y88888888b   \ |  .-\'     d888888888P\' \n          `888888888b   \|-\'       d888888888P \n           `Y88888888b            d8888888P\' \n             Y88888888bo.      .od88888888 \n             `8888888888888888888888888888 \n              Y88888888888888888888888888P \n               `Y8888888888888888888888P\' \n                 `Y8888888888888P\' \n                      `Y88888P\' "],
            "00001C" : ["building house home","  /^\ \n  |#| \n |===| \n  |0| \n  | | \n ===== \n_||_||_ "],
            "00001D" : ["building house home","                                                  _ \n  __                   ___                       ( ) \n |\"\"|  ___    _   __  |\"\"\"|  __                   ` \n |\"\"| |\"\"\"|  |\"| |\"\"| |\"\"\"| |\"\"|        _._ _ \n |\"\"| |\"\"\"|  |\"| |\"\"| |\"\"\"| |\"\"|       (__((_( \n |\"\"| |\"\"\"|  |\"| |\"\"| |\"\"\"| |\"\"|      \\'-:--:-. \n \"\'\'\'\"\'\'\"\'\"\"\'\"\"\"\'\'\"\'\'\'\'\"\"\"\'\"\"\'\"\"\'~~~~~~\'-----\'~~~~  "],
            "00001E" : ["building white house home","                 _ _.-\'`-._ _ \n                ;.\'________\'.; \n     _________n.[____________].n_________ \n    |\"\"_\"\"_\"\"_\"\"||==||==||==||\"\"_\"\"_\"\"_\"\"] \n    |\"\"\"\"\"\"\"\"\"\"\"||..||..||..||\"\"\"\"\"\"\"\"\"\"\"| \n    |LI LI LI LI||LI||LI||LI||LI LI LI LI| \n    |.. .. .. ..||..||..||..||.. .. .. ..| \n    |LI LI LI LI||LI||LI||LI||LI LI LI LI| \n ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,, \n;;jgs;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; "],
            "00001F" : ["building house home","             + \n             A \n          __/_\__ \n         /\-\'o\'-/\ \n        _||:<_>:||_ \n       /\_/=====\_/\ \n      _|:_:_[I]_:_:|_ \n   _/::::::::::::::::\_ \n _/::::::::::::::::::::\_ \n/::::::::::::::::::::::::\ "],
            "00001G" : ["building house home city town","                   \  |  /         ___________ \n    ____________  \ \_# /         |  ___      |       _________ \n   |            |  \  #/          | |   |     |      | = = = = | \n   | |   |   |  |   \\#           | |`v\'|     |      |         | \n   |            |    \#  //       |  --- ___  |      | |  || | | \n   | |   |   |  |     #_//        |     |   | |      |         | \n   |            |  \\ #_/_______  |     |   | |      | |  || | | \n   | |   |   |  |   \\# /_____/ \ |      ---  |      |         | \n   |            |    \# |+ ++|  | |  |^^^^^^| |      | |  || | | \n   |            |    \# |+ ++|  | |  |^^^^^^| |      | |  || | | \n^^^|    (^^^^^) |^^^^^#^| H  |_ |^|  | |||| | |^^^^^^|         | \n   |    ( ||| ) |     # ^^^^^^    |  | |||| | |      | ||||||| | \n   ^^^^^^^^^^^^^________/  /_____ |  | |||| | |      | ||||||| | \n        `v\'-                      ^^^^^^^^^^^^^      | ||||||| | \n         || |`.      (__)    (__)                          ( ) \n                     (oo)    (oo)                       /---V \n              /-------\/      \/ --------\             * |  | \n             / |     ||        ||_______| \ \n            *  ||W---||        ||      ||  * \n               ^^    ^^        ^^      ^^ "],            
            "00001H" : ["house home building","                                               /\      /\ \n                                               ||______|| \n                                               || ^  ^ || \n                                               \| |  | |/ \n                                                |______| \n              __                                |  __  | \n             /  \       ________________________|_/  \_|__ \n            / ^^ \     /=========================/ ^^ \===| \n           /  []  \   /=========================/  []  \==| \n          /________\ /=========================/________\=| \n       *  |        |/==========================|        |=| \n      *** | ^^  ^^ |---------------------------| ^^  ^^ |-- \n     *****| []  [] |           _____           | []  [] | | \n    *******        |          /_____\          |      * | | \n   *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| | \n  ***********]  [] |  []  []  |  |  |  []  []  | ===***** | \n *************     |         @|__|__|@         |/ |*******| \n***************   ***********--=====--**********| ********* \n***************___*********** |=====| **********|*********** \n *************     ********* /=======\ ******** | ********* "],
            "00001I" : ["house home building","                                                     ___ \n                                             ___..--\'  .`. \n                                    ___...--\'     -  .` `.`. \n                           ___...--\' _      -  _   .` -   `.`. \n                  ___...--\'  -       _   -       .`  `. - _ `.`. \n           __..--\'_______________ -         _  .`  _   `.   - `.`. \n        .`    _ /\    -        .`      _     .`__________`. _  -`.`. \n      .` -   _ /  \_     -   .`  _         .` |Train Depot|`.   - `.`. \n    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`. \n  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`| \n    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ | \n    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    | \n    |     |--|  |    | _ | |\'--\'| |---| |   _|---|     |---|_   | \n    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    | \n ---``--._      |    |   |=|\'--\'|=|___|=|====|___|=====|___|====| \n -- . \'\'  ``--._| _  |  -|_|.--.|_______|_______________________| \n`--._           \'--- |_  |:|\'--\'|:::::::|:::::::::::::::::::::::| \n_____`--._ \'\'      . \'---\'``--._|:::::::|:::::::::::::::::::::::| \n----------`--._          \'\'      ``--.._|:::::::::::::::::::::::| \n`--._ _________`--._\'        --     .   \'\'-----..............LGB\' \n     `--._----------`--._.  _           -- . :\'\'           -    \'\' \n          `--._ _________`--._ :\'              -- . :\'\'      -- . \'\' \n -- . \'\'       `--._ ---------`--._   -- . :\'\' \n          :\'        `--._ _________`--._:\'  -- . \'\'      -- . \'\' \n  -- . \'\'     -- . \'\'    `--._----------`--._      -- . \'\'     -- . \'\' \n                              `--._ _________`--._ \n -- . \'\'           :\'              `--._ ---------`--._-- . \'\'    -- . \'\' \n          -- . \'\'       -- . \'\'         `--._ _________`--._   -- . \'\' \n:\'                 -- . \'\'          -- . \'\'  `--._----------`--._ "],
            "00001J" : ["church building","   + \n   A_ \n  /\-\ \n _||\"|_ \n~^~^~^~^ "],
            "00001K" : ["rip cross church","      ,-=-.       ______     _ \n     /  +  \     />----->  _|1|_ \n     | ~~~ |    // -/- /  |_ H _| \n     |R.I.P|   //  /  /     |S| \n\vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/, "],
            "00001L" : ["church building","            + \n           /_\ \n ,%%%______|O| \n %%%/_________\ \n `%%| /\[][][]|% \n___||_||______|%&,__  "],
            "00001M" : ["church","      /\ \n     /\/\ \n    /\/\/\ \n   /\/\/\/\ \n  /\/\/\/\/\ \n /\/\/\/\/\/\ \n/\/\/\/\/\/\/\______________________________ \n|~~~~~~~~~~~~|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n|  /\    /\  | \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n|  \/    \/  |  \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n|            |   \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n|     __     |    \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n|    /  \    |     |   /\   /\   /\   /\   /\   | \n|   |    |   |     |  |  | |  | |  | |  | |  |  | \n|   |-   |   |     |  |__| |__| |__| |__| |__|  | \n|___|____|___|_____|____________________________| "],
            "00001N" : ["church","         _ \n        / \ \n       //_\\ \n      //(_)\\ \n       |/^\|  \n       // \\    ,@@@@@@@, \n      //   \\ ,@@@\@@@@/@@, \n     // === \\ @@\@@@/@@@@@ \n    // =-=-= \\@@@@\@@@@@@;% \n   //   ===   \\@@@@@@/@@@%%%, \n  //|         |\\@\\//@@%%%%%% \n  ~ |         | ~ @|| %\\//%%% \n    |  __ __  |    || %%||%%\' \n    | |  |  | |    ||   || \n    | | -|- | |    ||   || \n    |_|__|__|_|    ||   || \n  /`  =======  `\__||_._|| \n/`    =======            `\ "],
            "00001O" : ["church","                  _|_ \n                   | \n                  / \ \n                 //_\\ \n                //(_)\\ \n                 |/^\|  \n       ,%%%%     // \\    ,@@@@@@@, \n     ,%%%%/%%%  //   \\ ,@@@\@@@@/@@, \n @@@%%%\%%//%%%// === \\ @@\@@@/@@@@@ \n@@@@%%%%\%%%%%// =-=-= \\@@@@\@@@@@@;%#####, \n@@@@%%%\%%/%%//   ===   \\@@@@@@/@@@%%%######, \n@@@@@%%%%/%%//|         |\\@\\//@@%%%%%%#/#### \n\'@@@@@%%\\/%~ |         | ~ @|| %\\//%%%#####; \n  @@\\//@||   |  __ __  |    || %%||%%\'###### \n   \'@||  ||   | |  |  | |    ||   ||##\//#### \n     ||  ||   | | -|- | |    ||   ||\'#||###\' \n     ||  ||   |_|__|__|_|    ||   ||  || \n     ||  ||_/`  =======  `\__||_._||  || \n   __||_/`      =======            `\_||___ "],
            "00001P" : ["church","                                               /\      /\ \n                                               ||______|| \n                                               || ^  ^ || \n                                               \| |  | |/ \n                                                |______| \n              __                                |  __  | \n             /  \       ________________________|_/  \_|__ \n            / ^^ \     /=========================/ ^^ \===| \n           /  []  \   /=========================/  []  \==| \n          /________\ /=========================/________\=| \n       *  |        |/==========================|        |=| \n      *** | ^^  ^^ |---------------------------| ^^  ^^ |-- \n     *****| []  [] |           _____           | []  [] | | \n    *******        |          /_____\          |      * | | \n   *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| | \n  ***********]  [] |  []  []  |  |  |  []  []  | ===***** | \n *************     |         @|__|__|@         |/ |*******| \n***************   ***********--=====--**********| ********* \n***************___*********** |=====| **********|*********** \n *************     ********* /=======\ ******** | ********* "],
            "00001Q" : ["church","        _|_ \n         |  \n         | \n        / \ \n       //_\\ \n      //(_)\\ \n       |/^\| \n       ||_|| \n       // \\ \n      //   \\ \n     // === \\ \n    // =-=-= \\ \n   //   ===   \\ \n  //|         |\\ \n    |         | \n    |  __ __  | \n    | |  |  | | \n    | | -|- | | \n    |_|__|__|_| \n  /`  =======  `\ \n/`    =======    `\ "],
            "00001R" : ["church","             . \n            -|- \n             | \n            /A\ \n           //^\\ \n         ,// _ \\, \n         |/`/_\`\| \n          |  ,  | \n          | /^\ | \n          |//\'\\| \n        ,//` _ `\\, \n      ,//` .\'|\'. `\\, \n    ,//`   |-|-|   `\\, \n  ,//`     [_|_]     `\\, \n  |/T                 T\| \n    |  _   __ __   _  | \n    | /_\ |  |  | /_\ | \n    | |_| | .|. | |_| | \n    |     |__|__|     | \n    \'----[_______]----\' \n          ======= \n         ====== \n      ====== "],
            "00001S" : ["church","                                    + \n                                    | \n                                   ,|, \n                                   ||| \n                                  / | \ \n                                  | | | \n                                  | | | \n                                 /  |  \ \n                                 |  |  | \n                                 |  |   \ \n                                /    \  | \n                                |    |  | \n                                |    |   \ \n                               /     |   | \n                8              |     |   | \n              \"\"8\"\"           /      |    \ \n                8            /        \   ,\ \n              ,d8888888888888|========|=\"\" | \n            ,d\"  \"88888888888|  ,aa,  |  a | \n          ,d\"      \"888888888|  8  8  |  8 | \n       ,d8888888b,   \"8888888|  8aa8  |  8,| \n     ,d\"  \"8888888b,   \"88888|========|=\"\" | \n   ,d\"      \"8888888b,   \"888|  a  a  |  a | \n ,d\"   ,aa,   \"8888888b,   \"8|  8  8  |  8,| \n/|    d\"  \"b    |\"\"\"\"\"\"|     |========|=\"\" | \n |    8    8    |      |     |  ,aa,  |  a | \n |    8aaaa8    |      |     |  8  8  |  8 | \n |              |      |     |  \"\"\"\"  | ,,=| \n |aaaaaaaaaaaaaa|======\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\" "],
            "00001T" : ["church","                                    + \n                                    | \n                                   ,|, \n                                   ||| \n                                  / | \ \n                                  | | | \n                                  | | | \n                                 /  |  \ \n                                 |  |  | \n                                 |  |   \ \n                                /    \  | \n                                |    |  | \n                                |    |   \ \n                               /     |   | \n                8              |     |   | \n              \"\"8\"\"           /      |    \ \n                8            /        \   ,\ \n              ,d8888888888888|========|=\"\" | \n            ,d\"  \"88888888888|  ,aa,  |  a | \n          ,d\"      \"888888888|  8  8  |  8 | \n       ,d8888888b,   \"8888888|  8aa8  |  8,| \n     ,d\"  \"8888888b,   \"88888|========|=\"\" | \n   ,d\"      \"8888888b,   \"888|  a  a  |  a | \n ,d\"   ,aa,   \"8888888b,   \"8|  8  8  |  8,| \n/|    d\"  \"b    |\"\"\"\"\"\"|     |========|=\"\" | \n |    8    8    |      |     |  ,aa,  |  a | \n |    8aaaa8    |      |     |  8  8  |  8 | \n |              |      |     |  \"\"\"\"  | ,,=| \n |aaaaaaaaaaaaaa|======\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\" "],
            "00001U" : ["church","                                      . \n                                    .\' \'. \n                                  .\'  |  `. \n                                .\'    |    `. \n                              .`---.._|_..---\'. \n                               ||    |=|    || \n                               ||_.-\'|=|`-._|| \n                               ||`-._|=|_.-\'|| \n                          _____||    |=|    ||__ \n            ____________.\'     `-.   |=|  .\'_.\'\/`. \n          .\'       _  .\' _______  `-.|_|.\' .\'\.\'`./`. \n        .\'     _   _.\'      _   _        .\'\.\' `._`./`. \n      .\' _       _.\' __          __    .\'\.\'  ___`._`./`. \n    .\'        _ .\'   _____           .\'\.\'         `._`./`. \n  .\'  _  _    .\'       ______      .\'\.\'  __         `._`./`. \n.\'`--...__ _.\'            ______ .\'\.\'           __    `._`./`. \n `--...__ .\'   ____            .\'\.\'           _         `._`./`. \n |      .`--...__            .\'\.\'     _               ____`._`./`. \n | /`-._ `--...__`--...___ .\'\.\'              _______       _`._`./`. \n | | ) ( |       `--...____\.\'     _     _  .\'      .`.        `._`./ \n | |)   (| /`-._             |            .\'      .\'   `.     _ | \n | |(--| | | )( |  /`-._`--._|____       /      .\'       `.     | \n | | ) `.| |(  )|  | )( |    | _      _ /      /   .---.  `\    | \n | `--._ | |/  \|  |(  )|`-  |         /`--.._/   /     \  \' _  | \n | `-.   | |)-.(|  |/  \|    |       __|      |_  |`-   |  |  _ | \n |    `-.| |) |(|  |)-.(|    |  ___  _ |  __  | __| \`- |  |    | \n \'-._    | `--._/  |) |(|    |      __ |      |   | |`- |  | _  | \n     `-._| `--.    `--._/    |  ___    | _    |   | |`- |  |   \'| \n         |      `--._        |       _ |    \' |   |O|`- | _| _  | \n         \'--._         `--._ |         | _    |_ \"| |`- |. |  __| \n              `--._          |       __|      |   | |`- |. | __ | \n                   `--._     |__       |   _  |\"  | |`- |  |___ | \n                        `--._|_________|_     | _ |  `- |_ |____| \n                                         \'--._|___|     |__| "],
            "00001V" : ["alcatraz","                    __            ================================ \n         ALCATRAZ  /__\            ||     ||<(.)>||<(.)>||     ||  \n       ____________|  |            ||    _||     ||     ||_    ||  \n       |_|_|_|_|_|_|  |            ||   (__D     ||     C__)   ||  \n       |_|_|_|_|_|_|__|            ||   (__D     ||     C__)   || \n      A@\|_|_|_|_|_|/@@Aa          ||   (__D     ||     C__)   || \n   aaA@@@@@@@@@@@@@@@@@@@aaaA      ||   (__D     ||     C__)   || \n  A@@@@@@@@@@@DWB@@@@@@@@@@@@A     ||     ||     ||     ||  dwb|| \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ================================ "],
            "00001W" : ["book","    _______ \n   /      /, \n  /      // \n /______// \n(______(/ "],
            "00001X" : ["book","      ______ ______ \n    _/      Y      \_ \n   // ~~ ~~ | ~~ ~  \\ \n  // ~ ~ ~~ | ~~~ ~~ \\ \n //________.|.________\\ \n`----------`-\'----------\' "],
            "00001Y" : ["book"," ooooO   .=====i=====.   Ooooo \n|    /   |     |     |   \    | \n|   |   <|     |     |>   |   | \n|   |\~-.|_____|_____|.-~/|   | \n|   \ \   ~-.(___).-~   / /   | \n \__/-/_________________\-\__/ "],
            "00001Z" : ["book","      __...--~~~~~-._   _.-~~~~~--...__ \n    //               `V\'               \\  \n   //                 |                 \\  \n  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\  \n //__.....----~~~~._\ | /_.~~~~----.....__\\ \n====================\\|//==================== \n                    `---` "],
            "000020" : ["paper book","(\  \n\\'\  \n \\'\     __________   \n / \'|   ()_________) \n \ \'/    \ ~~~~~~~~ \ \n   \       \ ~~~~~~   \ \n   ==).      \__________\ \n  (__)       ()__________) "],
            "000021" : ["book","       __..._   _...__ \n  _..-\"      `Y`      \"-._ \n  \           |           / \n  \\          |          // \n  \\\         |         /// \n   \\\ _..---.|.---.._ /// \n    \\`_..---.Y.---.._`// \n     \'`               `\' "],
            "000022" : ["book shelf library","      _ _ \n .-. | | | \n |M|_|A|N| \n |A|a|.|.|<\ \n |T|r| | | \\ \n |H|t|M|Z|  \\ \n | |!| | |   \> \n\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\" "],
            "000023" : ["book shelf library","             .--.           .---.        .-. \n         .---|--|   .-.     | A |  .---. |~|    .--. \n      .--|===|Ch|---|_|--.__| S |--|:::| |~|-==-|==|---. \n      |%%|NT2|oc|===| |~~|%%| C |--|   |_|~|CATS|  |___|-. \n      |  |   |ah|===| |==|  | I |  |:::|=| |    |GB|---|=| \n      |  |   |ol|   |_|__|  | I |__|   | | |    |  |___| | \n      |~~|===|--|===|~|~~|%%|~~~|--|:::|=|~|----|==|---|=| \n      ^--^---\'--^---^-^--^--^---\'--^---^-^-^-==-^--^---^-\' "],
            "000024" : ["book","  __ \n (`/\ \n `=\/\ __...--~~~~~-._   _.-~~~~~--...__ \n  `=\/\               \ /               \\ \n   `=\/                V                 \\ \n   //_\___--~~~~~~-._  |  _.-~~~~~~--...__\\ \n  //  ) (..----~~~~._\ | /_.~~~~----.....__\\ \n ===( INK )==========\\|//==================== \n__ejm\___/________dwb`---`____________________________________________ "],
            "000025" : ["book","         ,..........   .........., \n     ,..,\'          \'.\'          \',.., \n    ,\' ,\'            :            \', \', \n   ,\' ,\'             :             \', \', \n  ,\' ,\'              :              \', \', \n ,\' ,\'............., : ,.............\', \', \n,\'  \'............   \'.\'   ............\'  \', \n \'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\';\'\'\';\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\' \n                    \'\'\' "],
            "000026" : ["book",",         , \n|\\\\ ////| \n| \\\V/// | \n|  |~~~|  | \n|  |===|  | \n|  |   |  | \n|  |   |  | \n \ |   | / \n  \|===|/ \n   \'---\' "],
            "000027" : ["book","   ,   , \n  /////| \n ///// | \n|~~~|  | \n|===|  | \n|   |  | \n|   |  | \n|   | / \n|===|/ \n\'---\' "],
            "000028" : ["books shelf library","       .--.                   .---. \n   .---|__|           .-.     |~~~| \n.--|===|--|_          |_|     |~~~|--. \n|  |===|  |\'\     .---!~|  .--|   |--| \n|%%|   |  |.\'\    |===| |--|%%|   |  | \n|%%|   |  |\.\'\   |   | |__|  |   |  | \n|  |   |  | \  \  |===| |==|  |   |  | \n|  |   |__|  \.\'\ |   |_|__|  |~~~|__| \n|  |===|--|   \.\'\|===|~|--|%%|~~~|--| \n^--^---\'--^    `-\'`---^-^--^--^---\'--\' "],
            "000029" : ["book","        _.-\"\ \n    _.-\"     \ \n ,-\"          \ \n( \            \ \n \ \            \ \n  \ \            \ \n   \ \         _.-; \n    \ \    _.-\"   : \n     \ \,-\"    _.-\" \n      \(   _.-\" \n       `--\" \n "],
            "00002a" : ["book","      _.--._  _.--._ \n,-=.-\":;:;:;\\':;:;:;\"-._ \n\\\:;:;:;:;:;\:;:;:;:;:;\ \n \\\:;:;:;:;:;\:;:;:;:;:;\ \n  \\\:;:;:;:;:;\:;:;:;:;:;\ \n   \\\:;:;:;:;:;\:;::;:;:;:\ \n    \\\;:;::;:;:;\:;:;:;::;:\ \n     \\\;;:;:_:--:\:_:--:_;:;\ \n      \\\_.-\"      :      \"-._\ \n       \`_..--\"\"--.;.--\"\"--.._=> \n        \" "],
            "00002b" : ["table book","    _____ \n   /    /|_ ___________________________________________ \n  /    // /|                                          /| \n (====|/ //   An apple a day...            _QP_      / | \n  (=====|/     keeps the teacher at bay   (  \' )    / .| \n (====|/                                   \__/    / /|| \n/_________________________________________________/ / || \n|  _____________________________________________  ||  || \n| ||                                            | || \n| ||                                            | || \n| |                                             | |  "],
            "00002c" : ["book","   /|~|\ \n  / |=| \ \n /  | |  \ \n|   | |   | \n|   | |   | \n|   | |   | \n|   |=|   | \n|  //A\\  | \n| /// \\\ | \n|///   \\\| \n`         ` "],
            "00002d" : ["books shelf library","           .--.   _ \n       .---|__| .((\=. \n    .--|===|--|/    ,(, \n    |  |===|  |\      y \n    |%%|   |  | `.__,\' \n    |%%|   |  | /  \\\ \n    |  |   |  |/|  | \`----. \n    |  |   |  ||\  \  |___.\'_ \n   _|  |   |__||,\  \-+-._.\' )_ \n  / |  |===|--|\  \  \      /  \ \n /  `--^---\'--\' `--`-\'---^-\'    \ \n\'================================` "],
            "00002e" : ["book","    __________________   __________________ \n.-/|                  \ /                  |\-. \n||||                   |                   |||| \n||||                   |       ~~*~~       |||| \n||||    --==*==--      |                   |||| \n||||                   |                   |||| \n||||                   |                   |||| \n||||                   |     --==*==--     |||| \n||||                   |                   |||| \n||||                   |                   |||| \n||||                   |                   |||| \n||||                   |                   |||| \n||||__________________ | __________________|||| \n||/===================\|/===================\|| \n`--------------------~___~-------------------\'\' "],
            "00002f" : ["book","        _________   _________ \n   ____/      452\ /     453 \____ \n /| ------------- |  ------------ |\ \n||| ------------- | ------------- ||| \n||| ------------- | ------------- ||| \n||| ------- ----- | ------------- ||| \n||| ------------- | ------------- ||| \n||| ------------- | ------------- ||| \n|||  ------------ | ----------    ||| \n||| ------------- |  ------------ ||| \n||| ------------- | ------------- ||| \n||| ------------- | ------ -----  ||| \n||| ------------  | ------------- ||| \n|||_____________  |  _____________||| \nL/_____/--------\\_//W-------\_____\J "],
            "00002g" : ["books shelf library"," _________________________________________________________ \n||-------------------------------------------------------|| \n||.--.    .-._                        .----.             || \n|||==|____| |H|___            .---.___|\"\"\"\"|_____.--.___ || \n|||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---||| \n|||==|    | | |   | \         |   |   |_\/_|Black|  | ^ ||| \n|||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ ||| \n|||  |    | | |   |_\ \_( oo )|   |   |    |Magus|  | ^ ||| \n|||==|====| |H|xxx|  \ \ |\'\'| |+++|=-=|\"\"\"\"|-=+=-|==|---||| \n||`--^----\'-^-^---\'   `-\' \"\"  \'---^---^----^-----^--^---^|| \n||-------------------------------------------------------|| \n||-------------------------------------------------------|| \n||               ___                   .-.__.-----. .---.|| \n||              |===| .---.   __   .---| |XX|<(*)>|_|^^^||| \n||         ,  /(|   |_|III|__|\'\'|__|:x:|=|  |     |=| Q ||| \n||      _a\'{ / (|===|+|   |++|  |==|   | |  |Illum| | R ||| \n||      \'/\\/ _(|===|-|   |  |\'\'|  |:x:|=|  |inati| | Y ||| \n||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z ||| \n||       _(____)|===|+|[I]|DK|\'\'|==|:x:|=|XX|<(*)>|=|^^^||| \n||              `---^-^---^--^--\'--^---^-^--^-----^-^---^|| \n||-------------------------------------------------------|| \n||_______________________________________________________|| "],
            "00002h" : ["books shelf library","   ____________________________________________________ \n  |____________________________________________________| \n  | __     __   ____   ___ ||  ____    ____     _  __  | \n  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | | \n  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| | \n  ||  |##||  | | || | |   |||-|  | |==|+|+||-|-|~||__| | \n  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_| \n  ||_______________________||__________________________| \n  | _____________________  ||      __   __  _  __    _ | \n  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /| \n  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / | \n  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__| \n  |____________________ /\~()/()~//\ __________________| \n  | __   __    _  _     \_  (_ .  _/ _    ___     _____| \n  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | | \n  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=| \n  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_| \n  |_________________ _/    \/\/\/    \_ _______________| \n  | _____   _   __  |/      \../      \|  __   __   ___| \n  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-||| \n  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | ||| \n  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_||| \n  |_________ __________\___\____/___/___________ ______| \n  |__    _  /    ________     ______           /| _ _ _| \n  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%| \n  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=| \n__|  \/\|/   /(____|/ //                    /  /||~|~|~|__ \n  |___\_/   /________//   ________         /  / ||_|_|_| \n  |___ /   (|________/   |\_______\       /  /| |______| \n      /                  \|________)     /  / | | "],
            "00002i" : ["sherlock holmes tale","   ,_        \n ,\'  `\,_    \n |_,-\'_)     \n /##c \'\  (  \n\' |\'  -{.  ) \n  /\__-\' \[] \n /`-_`\      \n \'     \   "],
            "00002j" : ["three little pigs tale","                                            ( \n                                           (  ) \n                     .___.            ,-.  __) \n      \|/           //===\\        ,-\' o `-!| \n    .\'+^+`.        //=|_|=\\    ,-\'---------`-. \n  .\'///|\\\`.     //=======\\    | [+]   [+] |   .-------------. \n //////|\\\\\\   //|||\'\"`|||\\   |    ___    |  <   huff, puff  > \n/((|||^..|||))\  |||||.^ |||||   |   |   |  //   `--v----------\' \n ((|||(oo)|||)   |||||o) |||||   |   |\'  |  |..~~~O \n                                           {   ~vv\' \n                                             | \n                                            >O< "],
            "00002k" : ["alice tale","                    _.---.---._ \n                  ,\'     |     `. \n                ,\'       |       `. \n               /         :         \ \n              .        ,\' `.        . \n              :    _,-\'     `-._    : \n              |  ,\'___       ___`.  | \n              | : \' __`-   -\'__ ` : | \n              | | ,\',.`.   ,\',.`. | | \n              | | `.`\'_,\' `._`\',\' | | \n              | |                 | | \n              | :        )        ; | \n              |  \      (_       /  | \n              |   \             /   | \n              |    \   ,-.-.   /    | \n              |    :`.  `-\'  ,\':    | \n              |    |,|`.___,\'|.|    | \n              |    | :       ; |    | \n              |    |  \     /  |    | \n              |    |   `---\'   |    | \n              :    |           |    ; \n               `.  |           |  ,\' \n                 `-\'           `-\' "],
            "00002l" : ["alice girl tale","              ___ \n            ,\'/|\`. \n           :,\',^.`.: \n           |,\'_ _`.| \n           |:`*)*\';| \n           ;|\ _ /|: \n        ,-(||.)-(.||)-. \n       |\'  \|(\ /)|/  `| \n       `:. (  `|\'  ) .;\' \n        | : \ ,^. / : | \n       ,\'`\'\-`.._/_/; | \n       `:=..-...______;_ \n       \`\ \\'`. .-\'\`: / \n       ;\' \ \/|  \_,\ `: \n      /  / \ \;   \  \ .\ \n     / //  _) `.\'--`-----, \n    /  /  `-\'-.)____...-\' \ \n   / ,(    ;    |  .    ) \\ \n  //   `-./     |   \.-\'    \ \n /   /     ``---\'-\'\'  \  .   \ \n(   ,   ,     |     \  `  `   ) \n `./      ,   \' .   .     \_.\' \n    `-._ /    . |    \ _.\'\' \n        ``-.._|___..-\'\' \n             |.\'// \n             |\':: \n             |=|| \n            ,\'.|`._ \n           \'--^\'^--` "],
            "00002m" : ["rabbit alice tale","                                  ,;;;,  \n                                ,;;;;;;;,  \n             .;;;,            ,;;;;;;;;;;;,  \n            .;;%%;;;,        ,;;;;;;;;;;;;;,  \n            ;;%%%%%;;;;,.    ;;;;;;;;;;;;;;;  \n            ;;%%%%%%%%;;;;;, ;;;;;;;;;;;;;;;  \n            `;;%%%%%%%%%;;;;;,;;;;;;;;;;;;;\'  \n             `;;%%%%%%%%%%;;;;,;;;;;;;;;;;\'  \n               `;;;%%%%%%%%;;;;,;;;;;;;;;\'  \n                  `;;;%%%%%%;;;;.;;;.;;;  \n                     `;;;%%%;;;;;;.;;;,; .,;;\'  \n                         `;;;;;;;;;;,;;;;;;\'.,;;;,  \n                          ;;;;;;;;;;;;;;;;;;;;;,.  \n          .          ..,,;;;;;......;;;;;;;.... \';  \n          ;;,..,;;;;;;;;;;;;..;;;;;;..;;;;.;;;;;.  \n           \';;;;;;;;;;;;;;..;;;a@@@@a;;;;;;;a@@@@a,  \n        .,;;;;;;;;;;;;;;;.;;;a@@@@@@@@;;;;;,@@@@@@@a,  \n      .;;;,;;;;;;;;;;;;;;;;;@@@@@\'  @@;;;;;;,@  `@@@@;,  \n     ;\' ,;;;,;;;;;;;;;;;;;;;@@@@@aa@@;;;;,;;;,@aa@@@@;;;,.,;  \n       ;;;,;;;;;;;;;;;;;;;;;;@@@@@@@;;;,;a@@\'      `;;;;;;;\'  \n       \' ;;;,;;;;;;;;;;;;;;;;;;;;;;;;,;a@@@       #  ;;,;;,  \n.//////,,;,;;;;;;;;;;;;;;;,;;;;;;;;,;;a@@@a,        ,a;;;,;;,  \n%,/////,;;;;;;;;;;;;;;;;;;;;,;,;,;;;;a@@@@@@aaaaaaa@@@;;;;;\';  \n`%%%%,/,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@@@@@;00@@;;;;;\'  \n  %%%%%%,;;;;;;;;;;;;;;;;;;;;;;;;;;;a@@@@@@@@@@;00@@;;;;;\'  \n   `%%%%%%%%%%,;;;;;;;;;;;;;;;;;;;;a@@@@@@@@@;00@@;;;;;\'  \n     `%%%%%%%%%%%%%%%,::::;;;;;;;;a@@@@@@@;00@@@::;;;%%%%%,  \n       `%%%%%%%%%%%%%%%,::::;;;;;@@@@@@\' 0@@@@::;;%%%%%%%%\'  \n          Oo%%%%%%%%%%%%,::::;;a@@@@@\'  ,@@@::;;%%%%%%%\'  \n           `OOo%%%%%%%%%%,::::@@@@@\'    @@;::;%%%%%%\'  \n             `OOOo%%%%%%%%,:::@@@@,;;;,a@:;;%%%%%\'  \n               `OOOOOo%%%%%,:::@@@aaaa@\';;%%%%\'  \n                  `OOOO;@@@@@@@@aa@@@@@@@@@\'  \n                      ;@@@@@@@@@@@@@@@@@@@\'  \n                       @@@@@@@@\'`@@@@@@@@\'  \n                       `@@@@@\'    @@@@@\'  \n                        `@@\'       @@\' "],
            "00002n" : ["harry potter","          _ \n      /b_,dM\__,_ \n    _/MMMMMMMMMMMm, \n   _YMMMMMMMMMMMM( \n  `MMMMMM/   /   \   _   ,     \n   MMM|  __  / __/  ( |_| \n   YMM/_/# \__/# \    | |_)arry \n   (.   \__/  \__/     ___   \n     )       _,  |    \'_|_) \n_____/\     _   /       | otter \n    \  `._____,\' \n     `..___(__ \n              ``-. \n                  \ \n                   ) "],
            "00002o" : ["harry potter","         ,/////\\, \n       ,///////\\\\\ \n     ,//////   > \\\\ \n     ////  __ `   _\\ \n     //__//  \--//  \ \n     /\'--\\_O/  \\_O/ \n     \_         \   | \n       \      ,__>  / \n       |\   ,____  / \n       | \   \__| / \n       |  \'._____/ \n       |      | \n     /``\"--._ \/`\ \n    /        \|  /`--. \n  /```\"\"--..__;.\'     `\ "],
            "00002p" : ["harry potter","            _            _.,----, \n __  _.-._ / \'-.        -  ,._  \)  \n|  `-)_   \'-.   \       / < _ )/\" } \n/__    \'-.   \   \'-, ___(c-(6)=(6) \n , `\'.    `._ \'.  _,\'   >\    \"  ) \n :;;,,\'-._   \'---\' (  ( \"/`. -=\'/ \n;:;;:;;,  \'..__    ,`-.`)\'- \'--\' \n;\';:;;;;;\'-._ /\'._|   Y/   _/\' \ \n      \'\'\'\"._ F    |  _/ _.\'._   `\ \n             L    \   \/     \'._  \ \n      .-,-,_ |     `.  `\'---,  \_ _| \n      //    \'L    /  \,   (\"--\',=`)7 \n     | `._       : _,  \  /\'`-._L,_\'-._ \n     \'--\' \'-.\__/ _L   .`\'         \'.// \n                 [ (  / \n                  ) `{ \n                  \__) "],
            "00002q" : ["dobby harry potter","   _____ \n  /     \ \n/- (*) |*)\ \n|/\.  _>/\| \n    \__/    |\ \n   _| |_   \-/ \n  /|\__|\  // \n |/|   |\\// \n |||   | ~\' \n ||| __| \n /_\| || \n \_/| || \n   |7 |7 \n   || || \n   || || \n   /\ \ \ \n  ^^^^ ^^^ "],
            "00002r" : ["harry potter","                                         _ __ \n        ___                             | \'  \ \n   ___  \ /  ___         ,\'\_           | .-. \        /| \n   \ /  | |,\'__ \  ,\'\_  |   \          | | | |      ,\' |_   /| \n _ | |  | |\/  \ \ |   \ | |\_|    _    | |_| |   _ \'-. .-\',\' |_   _ \n// | |  | |____| | | |\_|| |__    //    |     | ,\'_`. | | \'-. .-\',\' `. ,\'\_ \n\\_| |_,\' .-, _  | | |   | |\ \  //    .| |\_/ | / \ || |   | | / |\  \|   \ \n `-. .-\'| |/ / | | | |   | | \ \//     |  |    | | | || |   | | | |_\ || |\_| \n   | |  | || \_| | | |   /_\  \ /      | |`    | | | || |   | | | .---\'| | \n   | |  | |\___,_\ /_\ _      //       | |     | \_/ || |   | | | |  /\| | \n   /_\  | |           //_____//       .||`      `._,\' | |   | | \ `-\' /| | \n        /_\           `------\'        \ |   AND        `.\  | |  `._,\' /_\ \n                                       \|       THE          `.\ \n                                            _  _  _  _  __ _  __ _ /_ \n                                           (_`/ \|_)/ \'|_ |_)|_ |_)(_ \n                                           ._)\_/| \\_,|__| \|__| \ _) \n                                                           _ ___ _      _ \n                                                          (_` | / \|\ ||__ \n                                                          ._) | \_/| \||___ "],
            "00002s" : ["harry potter","        ______ \n        /      \ \n       |        | \n       |:/-\\--\. \n        ( )-( )/, \n         | ,  . \n        / \- /. \ \n       | ||L  / \ \ \n      / /  \/    | * \n     / /          \  \ \n     | |      []   |\ | \n    /| |           ||  | \n    || |           ||  | \n    |  |           ||  | \n    /_ |__________|||  | \n   /_ \| ---------||   | \n   /_ / |         ||   | \n  /  | ||         | |      \n  \//  ||         | |  | \n  /  | ||    T    | |  | \n /   | ||    |     | \n/ "],
            "00002t" : ["boy man people","                                     ...,,,,,...                             \n                      :        ..eed$$$$$$$$$$$$$bee..                       \n                  .   U    ued$$$$$$$$$$$$$$$$$$$$$$$$eu                     \n                  `~m.$  u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e.                  \n              ..     \"$.d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u                \n              \"\"#=q.  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u              \n                 .d8u.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u            \n               .e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e.          \n             u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u         \n           .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e        \n          u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$I?$b       \n         u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$b      \n        :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b`$$U     \n        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:`$$     \n       !$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ \"$:   \n       $$$$$$$$$$$$$$$$$$$$$$u\"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$: $!    \n       $$$$$$$$$$$$$$$$$$$$$$$u \"?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$U !!    \n      !$$$$$$$$$$$$$$$$$$$$$$$$$:. \"??$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ `~    \n      `$$$$$$$$$$$$$$$$$$$$$$$$$;T$eu.`\"\"???$$$$$$$$$$$$$$$$$$$$$$$$$$       \n       $$$$$$$$$$$$$$$$$$$$$$$$$t;$$$$$beeu..`\"\"\'..,,,..`\"\"??$$$$$$$$$       \n       ?$$$$$$$$$$$$$$$$*$$$$$$$F;$$$$$$$\"\".,,CI$$$$$$$$$$$Wu`\"?$$$$$$;      \n       `$$$$$$$$$$$$$$$T!$$$$$$$`!$$$$$\'.ud$$$$$$$$$$$$$$$$$$e. \"?$$$$       \n        ?$$$$$$$$$$$$$$!!$$$$$$$ U$$$$\'u$$$$$$$$$$$$$$$$$$$\"I$*:  \"$$$       \n         $$$$$$$$$$$$$f``$$$$$$\':$$$$$e$$$$$$F\"?$$$$$$$$$*(m\"(ueu  \"?T       \n         `$$$$$$$$$$$\"   \"$$$$f.$$$$$$$$$$F\"  ,$$$$$$$$$\"u\"  !$$T            \n          `$$$$$$$$$f ee. \"$$$ $$$$$$$$$$\"    d$$$$$$$$f.F   W$$             \n            \"$$$$$$$` $$$ee.\"\'u$$$$$$$$$$    u$$$$$$$$$ 4b.u$$$$            \n             \"$$$$$$  ?$$$$$u.$$$$$$$$$$$u..e$$$$$$$$$$.\"$$$$$$$u            \n               ?$$$$U `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W$$$$$$$$.           \n                \"?$$$u \"?$$$$?$$$$$$$$$$$$$$$$$$$$$$$$$$$T\"$$$$$$W           \n                  \"$\"$Wu.\"\"??i~$$$$$$$$$$$$$$$$$$$$**$$$*`u$$$$$$T           \n                     *$$$WWu .:\"$$$$$$$$$$$$$**$$$WWW$*?.e$$$$$$$`           \n                     `$$$$$$ ($ \"$$$$$$$$$$* -@$$$$$$$$$$$*I$$$F\'            \n                      $$$$$*  $W.\"$$$$$$$$$UW$e `\"\"\"\"\"\"?CuW$$$F              \n                     :$**\"`   $$$u \"$$$$$$$$$$$W.\"Wu   $$$$$$\"               \n                      `      -$$$$W.\"?$$$$$$$$$$$eC?(.u$$$$\"                 \n                           . :$$$$$$e.`\"$$$$$$$$$****\"I$$F`                  \n                         :!! !$$$$$$$$e. \"??$$$$$WeeW$$F\"                    \n                       :!!!\' W$$$$$$$$$$$eu. `\"\"\"****\"`                      \n                       !!;\'  $$$$$$$$$$$$$$$u   ....:::                      \n                      !!!:  :$$$$$$$$$$$$$$$$$:  !!!!!!!.                    \n                      !!!!!:. \"\"?$$$$$$$$$$$$$W  !!!!!!!!:                   \n                      !!!!!!!!!:. \"?$$$$$$$$$$$u `!!!!!!!!!                  \n                      !!!!!!!!!!!!:. \"?$$$$$$$$$e.` !!!~~!!.                 \n                   .:. `!!!!!!!!!!!!!:.\"?$$$$$$$$$$u !`.. `!                 \n                :!!!!!:  `!!!!!!!!!!!!!!: \"?$$$$$$$$ ~ !!: `                 \n             :!!!:.`\'!!!:  `!!!!!!!!!!!!!!:.\"?$$$$$$   !!!!                  \n          ::!!!!!!!! `!!!!:  `!!!!!!!!!\'  !!: \"$$$$f  !!!!!!.                \n       .:!!!!!!!!!!!. `!!!!!:  `!!!!!!  :!!!!: T$$$` !!!!! !!:               \n     :!!!!!!!!!!!!!!!  `!!!!!!.  !!!!\' .!!!!!!  ?$$  !!!!!: !!!              \n   :!!!!!!!!!!!!!!!!!!  !!!!!!!!. `!!  !!!!!!!! `$T  !!!!!!  !!!:            \n :!!!!!!!!!!!!!!!!!!!!  !!!!!!!!!: `!  !!!!!!!!: \"!  !!!!!!! `!!!!:          \n!!!!!!!!!!!!!!!!!!!!!!. (!!!!!!!!!!:  !!!!!!!!!!. ~ "],
            "00002u" : ["beach sand seeside","_\/_                 |                _\/_ \n/o\\             \       /            //o\ \n |                 .---.                | \n_|_______     --  /     \  --     ______|__ \n         `~^~^~^~^~^~^~^~^~^~^~^~` "],
            "00002v" : ["beach sand seeside","                   ____ \n                  (_  _) \n        .  .       / / \n     .`_._\'_..    / / \n     \   o   /   / / \n      \ /   /  _/ /_  \n`. ~. `\___/\'./~.\' /.~\'`. \n.`\'`.`.\'`\'`.~.`\'~.`\'`.~` "],
            "00002w" : ["beach sand seeside","          | \n        \ _ / \n      -= (_) =- \n        /   \         _\/_ \n          |           //o\  _\/_ \n   _____ _ __ __ ____ _ | __/o\\ _ \n =-=-_-__=_-= _=_=-=_,-\'|\"\'\"\"-|-,_ \n  =- _=-=- -_=-=_,-\"          | \n    =- =- -=.--\" "],
            "00002x" : ["beach sand seeside","                                        | \n                                      \ _ / \n                                    -= (_) =- \n   .\/.                               /   \ \n.\\//o\\                      ,\/.      |              ,~ \n//o\\|,\/.   ,.,.,   ,\/.  ,\//o\\                     |\ \n  |  |//o\  /###/#\  //o\  /o\\|                      /| \ \n^^|^^|^~|^^^|\' \'|:|^^^|^^^^^|^^|^^^\"\"\"\"\"\"\"\"(\"~~~~~~~~/_|__\~~~~~~~~~~ \n .|\'\' . |  \'\'\'\"\"\'\"\'\'. |`===`|\'\'  \'\"\" \"\" \" (\" ~~~~ ~ ~======~~  ~~ ~ \n    ^^   ^^^ ^ ^^^ ^^^^ ^^^ ^^ ^^ \"\" \"\"\"( \" ~~~~~~ ~~~~~  ~~~ ~ "],
            "00002y" : ["beach sand seeside","          ___   ____ \n        /\' --;^/ ,-_\     \ | / \n       / / --o\ o-\ \\   --(_)-- \n      /-/-/|o|-|\-\\|\\   / | \ \n       \'`  ` |-|   `` \' \n             |-| \n             |-|O \n             |-(\,__ \n          ...|-|\--,\_.... \n      ,;;;;;;;;;;;;;;;;;;;;;;;;,. \n~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,  ______   ---------   _____     ------ "],
            "00002z" : ["beach seeside sand castle","                         ____ \n                  /^\   / -- ) \n                 / | \ (____/ \n                / | | \ / / \n               /_|_|_|_/ / \n                |     / / \n __    __    __ |    / /__    __    __ \n[  ]__[  ]__[  ].   / /[  ]__[  ]__[  ] \n|__            ____/ /___           __| \n   |          / .------  )         | \n   |         / /        /          | \n   |        / /        /           | \n~~~~~~~~~~~~-----------~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "],
            "00002A" : ["beach seeside sand","              ,.  _~-.,               . \n           ~\'`_ \/,_. \_ \n          / ,\"_>@`,__`~.)             |           . \n          | |  @@@@\'  \",! .           .          \' \n          |/   ^^@     .!  \          |         / \n          `\' .^^^     ,\'    \'         |        .             . \n           .^^^   .          \                /          . \n          .^^^       \'  .     \       |      /       . \' \n.,.,.     ^^^             ` .   .,+~\'`^`\'~+,.     , \' \n&&&&&&,  ,^^^^.  . ._ ..__ _  .\'             \'. \'_ __ ____ __ _ .. .  . \n%%%%%%%%%^^^^^^%%&&;_,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-., \n&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~= \n%%%%%&&&&&&&&&&&%%%%&&&_,.;^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,__, \n%%%%%%%%%&&&&&&&&&-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-==--^\'~=-.,__,.-=~\' \n##mjy#####*\"\' \n_,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,.-=~\'`^`\'~=-.,__,.-=~\' \n \n~`\'^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-=~\'`^`\'~=-.,__,.-=~\'`^ "],
            "00002B" : ["beach seeside sand","      \.  -   -  . \n     \'          _ , -`. \n   \'        _,\'     _,\' \n  \'      ,-\'      _/ \n \'    ,-\' \     _/       __,,_ \n\'   ,\'     \  _\'        ////6 6 \n\'  \'       _\\'          \\\\'  > \n\' ,    _,-\'  \    _______ ) _= \n\,_,--\'       \   \\__ __/ /_\ \n               \   \\+/   ___ \ \n                \   \\| \'/ ),__) \n                 \   \\ /\/ ( +\ \n                  \   \\ \___`-.________ \n                   \   \\__,( \_____  - \ \n                    \   \`---\/\----), ) \ \n                     \   ||+=+=+=+=/  /\  \ \n                      \  ||________| /\ `. \ \n                       \ ||------- )/-\\  ) \ \n                        \||      ,\'/   \\  \ \ \n                                / /         \'-` \n                                \/ "],
            "00002C" : ["beach seeside sand","                           ##### \n                       ####### \n            ######    ########       ##### \n        ###########/#####\#####  ############# \n    ############/##########--##################### \n  ####         ######################          ##### \n ##          ####      ##########/@@              ### \n#          ####        ,-.##/`.#\#####               ## \n          ###         /  |$/  |,-. ####                 # \n         ##           \_,\'$\_,\'|  \  ### \n         #              \_$$$$$`._/   ## \n                          $$$$$_/     ## \n                          $$$$$        # \n                          $$$$$ \n                          $$$$$ \n                          $$$$$ \n                          $$$$$ \n                         $$$$$ \n                         $$$$$ \n                         $$$$$ \n                         $$$$$        ___ \n                         $$$$$    _.-\'   `-._ \n                        $$$$$   ,\'           `. \n                        $$$$$  /               \ \n~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~\'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~ \n   ~      ~  ~    ~  ~ $$$$$  ~   ~       ~          ~ \n       ~ ~      .o,    $$$$$     ~    ~  ~        ~ \n  ~            ~ ^   ~ $$$$$~        ______    ~        ~ \n_______________________$$$$$________|\\\\\\\_________________ \n                       $$$$$        |>\\\\\\\ \n    ______             $$$$$        |>>\\\\\\\ \n   \Q%=/\,\            $$$$$       /\>>|#####| \n    `------`           $$$$$      /=|\>|#####| \n                       $$$$$        ||\|#####| \n                      $$$$$$$          ||\"\"\"|| \n                      $$$$$$$          ||   || \n                     $$$$$$$$$ \n\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"$$$$$$$$$\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\" \n                        $$$ "],
            "00002D" : ["beach seeside sand"," (              ````                                             \n;`             ;;                                                \n ;;  -\"\"-.   ;;                 -;\'  -.                          \n   \"\"     ``                      `.   `.                        \n                                    ;    `                       \n           `;                  -          ;         -.        ;` \n             `-  `.         .\'`  .-\'             .--`  ;     ;   \n              ;    `-.   ;    `-\'             .;`     ;       `. \n              .        ``                                        \n               `            .--------.             .\'            \n             ...        .--\'``````````\'--.        ;.             \n            `      . .-\' .``          ``. \'-. .      `.          \n          ;-.;  .  .\' .`                  `. \'.  .    ;          \n              .\' .\' .`                      `. \'. \'.    .        \n_____/\'.-..___________________________ mvn,, ___________________ \n                             )\     nMmIEFooPTn                  \n                            ( (    Li1iiJl1ItTIjp                \n                             ) \  i i_BP_LWmKK`  J  `            \n`                .          /  (   i1 LL 1I`L            .       \n             ..             \   \  i   X  Y o1                   \n                        .    )   )  `   l   p      ..            \n;                           /   (,      l(@) l                .. \n  q      ` .  \'            (     \.     i    p   R          .;   \n   \  t            ;        )     \`   j,.. ,.q,/Pqoj          ` \n    \/            `       ./       \`;     `\'     `          ..  \n  \'-     \;            -\'.\'    ;    \ `                     `. ` \n.--.`.; ,-.. ,.-, ;\' `.-\'       `    `.\'.   .--.\"\"-._        .;  \n    `............---\"\"     ;_.         )   (  \'=    /         `- \n ~                                    /     `------\'     .       \n                 ~                  ,\'  \|//            `\'       \n                ~           ~       ; `. \"\"                   .. \n                                     `.  )     \\\"       .--\"\"\" "],
            "00002E" : ["cloud sky","   __   _ \n _(  )_( )_ \n(_   _    _) \n  (_) (__) "],
            "00002F" : ["cloud sky","          .-~~~-. \n  .- ~ ~-(       )_ _ \n /                     ~ -. \n|                           \ \n \                         .\' \n   ~- . _____________ . -~ "],
            "00002G" : ["cloud sky","          .-~~~-. \n  .- ~ ~-(       )_ _ \n /                    ~ -. \n|                          \', \n \                         .\' \n   ~- ._ ,. ,.,.,., ,.. -~ \n           \'       \' "],
            "00002H" : ["cloud sky","                _                                   \n              (`  ).                   _            \n             (     ).              .:(`  )`.        \n)           _(       \'`.          :(   .    )       \n        .=(`(      .   )     .--  `.  (    ) )       \n       ((    (..__.:\'-\'   .+(   )   ` _`  ) )                  \n`.     `(       ) )       (   .  )     (   )  ._    \n  )      ` __.:\'   )     (   (   ))     `-\'.-(`  )  \n)  )  ( )       --\'       `- __.\'         :(      ))  \n.-\'  (_.\'          .\')                    `(    )  )) \n                  (_  )                     ` __.:\'           \n                                         \n--..,___.--,--\'`,---..-.--+--.,,-,,..._.--..-._.-\':\'--. "],
            "00002I" : ["cloud sky","                                        ___    ,\'\"\"\"\"\'. \n                                    ,\"\"\"   \"\"\"\"\'      `. \n                                   ,\'        _.         `._ \n                                  ,\'       ,\'              `\"\"\"\'. \n                                 ,\'    .-\"\"`.    ,-\'            `. \n                                ,\'    (        ,\'                : \n                              ,\'     ,\'           __,            `. \n                        ,\"\"\"\"\'     .\' ;-.    ,  ,\'  \             `\"\"\"\". \n                      ,\'           `-(   `._(_,\'     )_                `. \n                     ,\'         ,---. \ @ ;   \ @ _,\'                   `. \n                ,-\"\"\'         ,\'      ,--\'-    `;\'                       `. \n               ,\'            ,\'      (      `. ,\'                          `. \n               ;            ,\'        \    _,\',\'                            `. \n              ,\'            ;          `--\'  ,\'                              `. \n             ,\'             ;          __    (                    ,           `. \n             ;              `____...  `78b   `.                  ,\'           ,\' \n             ;    ...----\'\'\'\' )  _.-  .d8P    `.                ,\'    ,\'    ,\' \n_....----\'\'\' \'.        _..--\"_.-:.-\' .\'        `.             ,\'\'.   ,\' `--\' \n              `\" mGk \"\" _.-\'\' .-\'`-.:..___...--\' `-._      ,-\"\'   `-\' \n        _.--\'       _.-\'    .\'   .\' .\'               `\"\"\"\"\" \n  __.-\'\'        _.-\'     .-\'   .\'  / \n \'          _.-\' .-\'  .-\'        .\' \n        _.-\'  .-\'  .-\' .\'  .\'   / \n    _.-\'      .-\'   .-\'  .\'   .\' \n_.-\'       .-\'    .\'   .\'    / \n       _.-\'    .-\'   .\'    .\' \n    .-\'            .\' "],
            "00002J" : ["mountain hills","          /\ \n         /**\ \n        /****\   /\ \n       /      \ /**\ \n      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\ \n     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \ \n    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \ \n   /  /      \/  \/\   \  /      \    /   /    \ \n__/__/_______/___/__\___\__________________________________________________ "],
            "00002K" : ["mountain hills","             o\ \n   _________/__\__________ \n  |                  - (  | \n ,\'-.                 . `-| \n(____\".       ,-.    \'   || \n  |          /\,-\   ,-.  | \n  |      ,-./     \ /\'.-\ | \n  |     /-.,\      /     \| \n  |    /     \    ,-.     \ \n  |___/_______\__/___\_____\  "],
            "00002L" : ["mountain hills","    .                  .-.    .  _   *     _   . \n           *          /   \     ((       _/ \       *    . \n         _    .   .--\'\/\_ \     `      /    \  *    ___ \n     *  / \_    _/ ^      \/\\'__        /\/\  /\  __/   \ * \n       /    \  /    .\'   _/  /  \  *\' /    \/  \/ .`\'\_/\   . \n  .   /\/\  /\/ :\' __  ^/  ^/    `--./.\'  ^  `-.\ _    _:\ _ \n     /    \/  \  _/  \-\' __/.\' ^ _   \_   .\'\   _/ \ .  __/ \ \n   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \ \n  /  `-.__ ^   / .-\'.--\'    . /    `--./ .-\'  `-.  `-. `.  -  `. \n@/        `.  / /      `-.   /  .-\'   / .   .\'   \    \  \  .-  \% \n@&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)% \n@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.\'@(&%::::%@8&8)::&#@8:::: \n`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~\'8::::::::&@8:::::&8:::::\' \n `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.\' "],
            "00002M" : ["mountain hills","                                   /\ \n                              /\  //\\ \n                       /\    //\\///\\\        /\ \n                      //\\  ///\////\\\\  /\  //\\ \n         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \ \n        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \ \n       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       * \n      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\ \n     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\ \n    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\ \n   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\ \n  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       | \n / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           | \n/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo  | \nooooooooooooooooooooooooooooooooooooooooooooooooooooooooo "],
            "00002N" : ["mountain hills","                                                 ******* \n                                 ~             *---******* \n                                ~             *-----******* \n                         ~                   *-------******* \n                        __      _   _!__     *-------******* \n                   _   /  \_  _/ \  |::| ___ **-----********   ~ \n                 _/ \_/^    \/   ^\/|::|\|:|  **---*****/^\_ \n              /\/  ^ /  ^    / ^ ___|::|_|:|_/\_******/  ^  \ \n             /  \  _/ ^ ^   /    |::|--|:|---|  \__/  ^     ^\___ \n           _/_^  \/  ^    _/ ^   |::|::|:|-::| ^ /_  ^    ^  ^   \_ \n          /   \^ /    /\ /       |::|--|:|:--|  /  \        ^      \ \n         /     \/    /  /        |::|::|:|:-:| / ^  \  ^      ^     \ \n   _Q   / _Q  _Q_Q  / _Q    _Q   |::|::|:|:::|/    ^ \   _Q      ^ \n  /_\)   /_\)/_/\\)  /_\)  /_\)  |::|::|:|:::|          /_\) \n_O|/O___O|/O_OO|/O__O|/O__O|/O__________________________O|/O__________ \n////////////////////////////////////////////////////////////////////// "],
            "00002O" : ["mountain hills","                                               _ \n                 ___                          (_) \n               _/XXX\ \n_             /XXXXXX\_                                    __ \nX\__    __   /X XXXX XX\                          _       /XX\__      ___ \n    \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX\ \n  \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \__/ \n ___/   \__/   \ \__     \\__           /  \_//  _ _ \  \     __  /  \____// \n/  __    \  /     \ \_   _//_\___     _/    //           \___/  \/     __/ \n__/_______\________\__\_/________\_ _/_____/_____________/_______\____/_______ \n                                  /|\ \n                                 / | \ \n                                /  |  \ \n                               /   |   \ \n                              /    |    \ \n                             /     |     \ \n                            /      |      \ \n                           /       |       \ \n                          /        |        \ \n                         /         |         \ "],
            "00002P" : ["mountain hills","           .          .           .     .                .       . \n  .      .      *           .       .          .                       . \n                 .       .   . *              \n  .       ____     .      . .            .     \n         >>         .        .               . \n .   .  /WWWI; \  .       .    .  ____               .         .     .          \n  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             . \n  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         . \n     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * . \n . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     . \n  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              . \n /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     * \n/WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \     . \nWWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \    \nWWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::       \ \n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXX \n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXX \n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXX \n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXX \n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXX \n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXXXXXXXX "],
            "00002Q" : ["mountain hills","                      _ \n                     /#\ \n                    /###\     /\ \n                   /  ###\   /##\  /\ \n                  /      #\ /####\/##\ \n                 /  /      /   # /  ##\             _       /\ \n               // //  /\  /    _/  /  #\ _         /#\    _/##\    /\ \n              // /   /  \     /   /    #\ \      _/###\_ /   ##\__/ _\ \n             /  \   / .. \   / /   _   { \ \   _/       / //    /    \\ \n     /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\ \n  _ /  \  /// / .\  ..%:.  /... /\ . \ {:  \\   /. \     / \  /   ___   /  \ \n /.\ .\.\// \/... \.::::..... _/..\ ..\:|:. .  / .. \\  /.. \    /...\ /  \ \ \n/...\.../..:.\. ..:::::::..:..... . ...\{:... / %... \\/..%. \  /./:..\__   \ \n .:..\:..:::....:::;;;;;;::::::::.:::::.\}.....::%.:. \ .:::. \/.%:::.:..\ \n::::...:::;;:::::;;;;;;;;;;;;;;:::::;;::{:::::::;;;:..  .:;:... ::;;::::.. \n;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;];;;;;;;;;;::::::;;;;:.::;;;;;;;;:.. \n;;;;;;;;;;;;;;ii;;;;;;;;;;;;;;;;;;;;;;;;[;;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;; \n;;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;;};;ii;;iiii;;;;i;;;;;;;;;;;;;;;ii;;; \niiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii{iiIIiiiiiiiiiiiiiiii;;;;;iiiilliiiii \nIIIiiIIllllllIIlllIIIIlllIIIlIiiIIIIIIIIIIIIlIIIIIllIIIIIIIIiiiiiiiillIIIllII \nIIIiiilIIIIIIIllTIIIIllIIlIlIIITTTTlIlIlIIIlIITTTTTTTIIIIlIIllIlIlllIIIIIIITT \nIIIIilIIIIITTTTTTTIIIIIIIIIIIIITTTTTIIIIIIIIITTTTTTTTTTIIIIIIIIIlIIIIIIIITTTT \nIIIIIIIIITTTTTTTTTTTTTIIIIIIIITTTTTTTTIIIIIITTTTTTTTTTTTTTIIIIIIIIIIIIIITTTTT "],
            "00002R" : ["desert cactus sand","           ,,                               .-. \n          || |                               ) ) \n          || |   ,                          \'-\' \n          || |  | | \n          || \'--\' | \n    ,,    || .----\' \n   || |   || | \n   |  \'---\'| | \n   \'------.| |                                  _____ \n   ((_))  || |      (  _                       / /|\ \ \n   (o o)  || |      ))(\"),                    | | | | | \n____\_/___||_|_____((__^_))____________________\_\|/_/__ "],
            "00002S" : ["sand cactus desert","    .    _    +     .  ______   .          . \n (      /|\      .    |      \      .   + \n     . |||||     _    | |   | | ||         . \n.      |||||    | |  _| | | | |_||    . \n   /\  ||||| .  | | |   | |      |       . \n__||||_|||||____| |_|_____________\__________ \n. |||| |||||  /\   _____      _____  .   . \n  |||| ||||| ||||   .   .  .         ________ \n . \|`-\'|||| ||||    __________       .    . \n    \__ |||| ||||      .          .     . \n __    ||||`-\'|||  .       .    __________ \n.    . |||| ___/  ___________             . \n   . _ ||||| . _               .   _________ \n_   ___|||||__  _ \\--//    .          _ \n     _ `---\'    .)=\oo|=(.   _   .   .    . \n_  ^      .  -    . \.| "],
            "00002T" : ["sand cactus desert","           ,                        \'           .        \'        ,   \n   .            .        \'       .         ,          \n                                                   .       \'     + \n       +          .-\'\'\'\'\'-.      \n                .\'         `.   +     .     ________|| \n       ___     :             :     |       /        ||  .     \'___ \n  ____/   \   :               :   ||.    _/      || ||\_______/   \ \n /         \  :      _/|      :   `|| __/      ,.|| ||             \ \n/  ,   \'  . \  :   =/_/      :     |\'_______     || ||  ||   .      \ \n    |        \__`._/ |     .\'   ___|        \__   \\||  ||...    ,   \ \n   l|,   \'   (   /  ,|...-\'        \   \'   ,     __\||_//___           \n ___|____     \_/^\/||__    ,    .  ,__             ||//    \    .  , \n           _/~  `\"\"~`\"` \_           \'\'(       ....,||/       \'    \n ..,...  __/  -\'/  `-._ `\_\__        | \           ||  _______   . \n              \'`  `\   \  \-.\        /(_1_,..      || / \n                                            ______/\"\"\"\" "],
            "00002U" : ["sand cactus desert","                /||\ \n                |||| \n                |||| \n                |||| /|\ \n           /|\  |||| ||| \n           |||  |||| ||| \n           |||  |||| ||| \n           |||  |||| d|| \n           |||  |||||||/ \n           ||b._||||~~\' \n           \|||||||| \n            `~~~|||| \n                |||| \n                |||| \n~~~~~~~~~~~~~~~~||||~~~~~~~~~~~~~~ \n  \/..__..--  . |||| \/  .  .. \n\/         \/ \/    \/ \n        .  \/              \/    . \n. \/             .   \/     . \n   __...--..__..__       .     \/ \n\/  .   .    \/     \/    __..--.. "],
            "00002V" : ["sand cactus desert snake","                /||\ \n                |||| \n                ||||                      _____.-..-. \n                |||| /|\               .-~@@/ / q  p \ \n           /|\  |||| |||             .\'@ _@/..\-.__.-/ \n           |||  |||| |||            /@.-~/|~~~`\|__|/ \n           |||  |||| |||            |\'--<||     \'~~\' \n           |||  |||| d||            |>--<\@\ \n           |||  |||||||/            \>---<\@`\. \n           ||b._||||~~\'              `\>---<`\@`\. \n           \||||||||                   `\>----<`\@`\. \n            `~~~||||               _     `\>-----<`\@`\. \n                ||||              (_)      `\>-----<`\.@`\. \n                ||||              (_)        `\>------<`\.@`\. \n~~~~~~~~~~~~~~~~||||~~~~~~~~~~~~~~(__)~~~~~~~~~`\>-------<`\.@`\~~~~~~~~~~~~~ \n  \/..__..--  . |||| \/  .  ..____( _)@@@--..____\..--\@@@/~`\@@>-._   \/ . \n\/         \/ \/    \/     / - -\@@@@--@/- - \@@@/ - - \@/- -@@@@/- \.   --._ \n   .   \/    _..\/-...--.. |- - -\@@/ - -\@@@@/~~~~\@@@@/- - \@@/- - |   .\/ \n        .  \/              | - - -@@ - - -\@@/- - - \@@/- - - @@- - -|      . \n. \/             .   \/     ~-.__ - - - - -@@- - - - @@- - - - -__.-~  . \/ \n   __...--..__..__       .  \/   ~~~--..____- - - - -____..--~~~    \/_..--.. \n\/  .   .    \/     \/    __..--... \/      ~~~~~~~~~     \/ . \/  . "],
            "00002W" : ["sand cactus desert dog parrot","                              .-. \n                             (  o)-. \n                              ) )\|\) \n                           _./ (,_  \n                          ( \'**\"  ) \n                          \\\   /// \n                           \\\|/// \n                     _______//|\\____________               . \n                   ,\'______///|\\\________,\'|            \  :  / \n     _ _           |  ____________________|,\'             \' _ \' \n    \' Y \' _ _      | ||              |                -= ( (_) )=- \n    _ _  \' Y \'     | ||              |                    .   . \n   \' Y \'_ _        | ||              |                   /  :  \ \n       ( Y )       | ||              8                      \' \n                   | ||              8 \n                   | ||        /\/\  8 \n                   | ||      .\'   ``/| \n                   | ||      | x   ``| \n                   | ||      |  /. `/`  \n                   | ||      \'_/|  /```                 .-. \n                   | ||        (_,\' ````                |.| \n  |J               | ||         |       \             /)|`|(\ \n L|                | ||       ,\'         \           (.(|\'|)`) \n  |                | ||     ,\',\'| .\'      \           `\`\'./\' \n~~~~               | ||~~~~~||~~||.       \~~~~~~~~~~~~|.|~~~~~~~~~~~  \n                   | ||     ||  || \        \          ,|`|. \n  ~~               | ||     \"\"  \"\"  \        \          \"\'\"   ~~ \n                   | ||              )   .   )    \n                   | ||             / ,   ),\'|      ~~ \n             ~~    | ||         ___/ /   ,\'  |              (_) \n      ((__))       | ||   ~~   I____/  ,\'    |              /\"/ \n      ( 0 0)       | ||         I____,\'      *             ^~^ \n       `\_\\       | ||                          ~~ \n         \"\'\"\'      | ||   \n  ~~               | ||         ~~                          ~~ \n                   |_|/ "],
            "00002X" : ["island","     __ |              \n     __\|,-            \n     ,-`=--.          \n      /=8\             \n       =               \n       =               \n       = \n       = \n~..:::::::::::::..~~ \n~~~~~~~~~~~~~~~~~~~~ "],
            "00002Y" : ["island","           _  _             _  _ \n  .       /\\/%\       .   /%\/%\     . \n      __.<\\%#//\,_       <%%#/%%\,__  . \n.    <%#/|\\%%%#///\    /^%#%%\///%#\\ \n      \"\"/%/\"\"\ \\ \"\"//|   |/\"\"\'/ /\//\"//\' \n .     L/\'`   \ \  `    \"   / /  ``` \n        `      \ \     .   / /       . \n .       .      \ \       / /  . \n        .        \ \     / /          . \n   .      .    ..:\ \:::/ /:.     .     . \n______________/ \__;\___/\;_/\________________________________ \nYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYw "],
            "00002Z" : ["island","                                                    ____ \n                                         v        _(    ) \n        _ ^ _                          v         (___(__) \n       \'_\V/ ` \n       \' oX` \n          X                            v \n          X \n          X                                                 . \n          X        \O/                                      |\ \n          X.a##a.   M                                       |_\ \n       .aa########a.>>                                    __|__ \n    .a################aa.                                 \   / \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "],
            "000030" : ["bananas fruit","   _    \n _ \\'-_,# \n_\\'--\',\'`| \n\`---`  / \n `----\'` "],
            "000031" : ["bananas fruit","      .-. \n     /  | \n    |  / \n .\'\|.-; _ \n/.-.;\  |\| \n\'   |\'._/ ` \n    |  \ \n     \  | \n      \'-\' "],
            "000032" : ["bananas fruit"," _ \n//\ \nV  \ \n \  \_ \n  \,\'.`-. \n   |\ `. `.        \n   ( \  `. `-.                        _,.-:\ \n    \ \   `.  `-._             __..--\' ,-\';/ \n     \ `.   `-.   `-..___..---\'   _.--\' ,\'/ \n      `. `.    `-._        __..--\'    ,\' / \n        `. `-_     ``--..\'\'       _.-\' ,\' \n          `-_ `-.___        __,--\'   ,\' \n             `-.__  `----\"\"\"    __.-\' \n                  `--..____..--\' "],
            "000033" : ["monkey bananas","                 __,__ \n        .--.  .-\"     \"-.  .--. \n       / .. \/  .-. .-.  \/ .. \ \n      | |  \'|  /   Y   \  |\'  | | \n      | \   \  \ 0 | 0 /  /   / | \n       \ \'- ,\.-\"`` ``\"-./, -\' / \n        `\'-\' /_   ^ ^   _\ \'-\'` \n        .--\'|  \._ _ _./  |\'--.  \n      /`    \   \.-.  /   /    `\ \n     /       \'._/  |-\' _.\'       \ \n    /          ;  /--~\'   |       \ \n   /        .\'\|.-\--.     \       \ \n  /   .\'-. /.-.;\  |\|\'~\'-.|\       \ \n  \       `-./`|_\_/ `     `\\'.      \ \n   \'.      ;     ___)        \'.`;    / \n     \'-.,_ ;     ___)          \/   / \n      \   ``\'------\'\       \   `  / \n       \'.    \       \'.      |   ;/_ \n     ___>     \'.       \_ _ _/   ,  \'--. \n   .\'   \'.   .-~~~~~-. /     |--\'`~~-.  \ \n  // / .---\'/  .-~~-._/ / / /---..__.\'  / \n ((_(_/    /  /      (_(_(_(---.__    .\' \n           | |     _              `~~` \n           | |     \\'. \n            \ \'....\' | \n             \'.,___.\' "],
            "000034" : ["beer",".~~~~. \ni====i_ \n|cccc|_) \n|cccc| \n`-==-\' "],
            "000035" : ["beer drink","         . . \n       .. . *. \n- -_ _-__-0oOo \n _-_ -__ -||||) \n    ______||||______ \n~~~~~~~~~~`\"\"\' "],
            "000036" : ["beer drink","  .   *   ..  . *  * \n*  * @()Ooc()*   o  . \n    (Q@*0CG*O()  ___ \n   |\_________/|/ _ \ \n   |  |  |  |  | / | | \n   |  |  |  |  | | | | \n   |  |  |  |  | | | | \n   |  |  |  |  | | | | \n   |  |  |  |  | | | | \n   |  |  |  |  | \_| | \n   |  |  |  |  |\___/ \n   |\_|__|__|_/| \n    \_________/ "],
            "000037" : ["beer drink","                         .sssssssss. \n                   .sssssssssssssssssss \n                 sssssssssssssssssssssssss \n                ssssssssssssssssssssssssssss \n                 @@sssssssssssssssssssssss@ss \n                 |s@@@@sssssssssssssss@@@@s|s \n          _______|sssss@@@@@sssss@@@@@sssss|s \n        /         sssssssss@sssss@sssssssss|s \n       /  .------+.ssssssss@sssss@ssssssss.| \n      /  /       |...sssssss@sss@sssssss...| \n     |  |        |.......sss@sss@ssss......| \n     |  |        |..........s@ss@sss.......| \n     |  |        |...........@ss@..........| \n      \  \       |............ss@..........| \n       \  \'------+...........ss@...........| \n        \________ .........................| \n                 |.........................| \n                /...........................\ \n               |.............................| \n                  |.......................| \n                      |...............| \n "],
            "000038" : ["beer drink"," ___________________________ \n(                           ) \n|                           | \n|                           | \n|                           |___________ \n|                           |           | \n|                           |________   | \n|                           |        |  | \n|                           |        |  | \n|    ___________________    |        |  | \n|---|S I E G B U R G E R|-dd|        |  | \n|    \"|B R A U H A U S|\"    |        |  | \n|      \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"      |        |  | \n|          ._- -_,          |        |  | \n|        .:8:   :8:.        |        |  | \n|       :8:`  _  \':8:       |        |  | \n|       \"`  C B    \'\"       |        |  | \n|          C\\ \" (            |        |  | \n|           \_ |            |        :  : \n|            /__\           |        :  : \n|    ___   ,//  \\   ___    |       :  : \n|    :  \  \"\"  ,//  /  :    |       :  : \n|     \  `._   \"\"_.\'  /     |      :  : \n|      `.   \"\"\"\"\"   ,\'      |     /  / \n|        `-._____,-\'        |    /  / \n|                           |   /  / \n|____        ____        ___|  /  / \n|____\      /____\      /___| /  / \n|    ||    ||    ||    ||   |\"  / \n|    ||    ||    ||    ||   |  / \n|    ||    ||    ||    ||   | / \n|    ||    ||    ||    ||   |/ \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|    ||    ||    ||    ||   | \n|____||    ||____||    ||___| \n|____/      \____/      \___| \n\\_________________________// \n/                           \ \n\___________________________/ "],
            "000039" : ["candle candy","        . \n      ,i \ \n    ,\' 8b \ \n  ,;o  `8b \ \n ;  Y8. d8  \ \n-+._ 8: d8. i: \n    `:8 `8i `8 \n      `._Y8  8:  ___ \n         `\'---Yjdp  \"8m._ \n              ,\"\' _,o9   `m._ \n              | o8P\"   _.8d8P`-._ \n              :8\'   _oodP\"   ,dP\'`-._ \n               `: dd8P\'   ,odP\'  do8\'`. \n                 `-\'   ,o8P\'  ,o8P\' ,8P`. \n                   `._dP\'   ddP\'  ,8P\' ,.. \n                      \"`._ PP\'  ,8P\' _d8\'L..__ \n                          `\"-._88\'  .PP,\'7 ,8.`-.._ \n                               ``\'\"--\"\'  | d8\' :8i `i. \n                                         l d8  d8  dP/ \n                                          \`\' J8\' `P\' \n                                           \ ,8F  87 \n                                           `.88  ,\' \n                                            `.,-\'  "],
            "00003a" : ["ice cream","         _.-. \n       ,\'/ //\ \n      /// // /) \n     /// // //| \n    /// // /// \n   /// // /// \n  (`: // /// \n   `;`: /// \n   / /:`:/ \n  / /  `\' \n / / \n(_/ "],
            "00003b" : ["ice cream","                                 ,\'\',  \n                              .a@a.  \n                              `@@@\'  \n                         .,:::::::::::,.  \n                     .,%%::::%%:::%:::%%%%,.  \n                   .%%%%%%::%%%%:%%%:::%%%%%%.  \n              .a@@@@@@@@a%%:%%%%%%%%::%%%%%%%%  \n  .%%%,.     a@;@@@;@@@;@@;;%%%%%%%%%:mm:::::::::mm,.    .,%%%,  \n %%%%%%%%,;;;@;;;@@;;@@;;;@;;;%%%%mmmmm::mm:::mm:::mmmm,%%%%%%%%  \n`%%%%%%%%%%;;;;;;@;;;;@;;;;;;;;;mmmmmm::mmmm::mmmm::mm%%%%%%%%%%\'  \n `%%%%%%%%%%%%:::@::::::::::::::mmmmmmm:mmmmmmmmmmm:%%%%%%%%%%%\'  \n.\\\\,\\\\,\\\\,\\\\,\\\\,\\\\,\|/,////,////,////,/::/,////,////.  \n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|//////////////////:////////////  \n   `\\\\\\\\\\\\\\\\\\\\\\\\\\\\|/////////////////://////////\'  \n        `\\\\\\\\\\\\\\\\\\\\\\\|/////////////////://///\'  \n             `\\\\\\\\\\\\\\\\\\|///////////////////\'  \n                   `\\\\\\\\\\\\|////////////\'  \n                          `\\\\\|/////\'          ;  \n                            `\\\|///\'           .:.  \n                              \\|//            :::::  \n                           .,///|\\\,.         `:::\'  \n                        .///////|\\\\\\\. "],
            "00003c" : ["ice cream","            .oo. \n          oGGGGGGo \n         GGGGGGGGGG \n  .mMMMMMMGGGGGGEEEE= \n MMMMMMMMMMMGGEEEEEEEE \nMMMMMMMMMMMNICKEEEEEEEE \nMMMMMMMMMMMMMEEEEEEEEEE \n!MMMMMMMMMMMOOEEEEEEEE \n MMM!MMMMMMOOOOOOE!= \n  MM!!!!!!!!!!!!!!! \n   MM!!!!!!!!!!!!!\' \n   !M!!!!!!!!!!!!! \n    MM!!!!!!!!!!!\' \n    MM!!!!!!!!!!! \n    ! `!!!!!!!!!\' \n    .  !!!!!!!!! \n       `!!!!!!!\' \n        !!!!!!! \n        `!!!!!\' \n         !!!!! \n         `!!!\' \n          !!! \n          `!\' \n           ! "],
            "00003d" : ["candy chocolate"," _____________,-.___     _ \n|____        { {]_]_]   [_] \n|___ `-----.__\ \_]_]_    . ` \n|   `-----.____} }]_]_]_   , \n|_____________/ {_]_]_]_] , ` \n              `-\' "],
            "00003e" : ["candy chocolate","    __________________,.............,     \n   /_/_/_/_/_/_/_/_/,-\',  ,. -,-,--/| \n  /_/_/_/_/_/_/_/,-\' //  /-| / /--/ / \n /_/_/_/_/_/_/,-\' `-\'\'--\'  `\' \'--/ / \n/_/_/_/_/_/_,:................../ / \n|________,\'                   hh|/ \n         \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\' "],
            "00003f" : ["chocolate candy","  ___  ___  ___  ___  ___.---------------. \n.\'\__\\'\__\\'\__\\'\__\\'\__,`   .  ____ ___ \ \n|\/ __\/ __\/ __\/ __\/ _:\   |`.  \  \___ \ \n \\\'\__\\'\__\\'\__\\'\__\\'\_`.__|\"\"`. \  \___ \ \n  \\/ __\/ __\/ __\/ __\/ __:                \ \n   \\\'\__\\'\__\\'\__\ \__\\'\_;-----------------` \n    \\/   \/   \/   \/   \/ :               hh| \n     \|______________________;________________| "],
            "00003g" : ["drinks cup glass cocktail wine"," _____ \n/.---.\ \n|`````| \n\     / \n `-.-\'           ____ \n   |    /\     .\'   /\ \n __|__  |K----;    |  | \n`-----` \/     \'.___\/ "],
            "00003h" : ["drinks cup glass cocktail","    . \n |^ . \n\O___.____ / \n  \   .  / \n    \ ,/ \n     [] \n     [] \n     [] \n  -------- "],
            "00003i" : ["drinks cup glass cocktail","   . \n  . \n . . \n  ... \n\~~~~~/ \n \   / \n  \ / \n   V \n   | \n   | \n  --- "],
            "00003j" : ["drinks cup glass cocktail wine","  _ \n {_} \n |(| \n |=| \n/   \ \n|.--| \n||  | \n||  |    .    \' . \n|\'--|  \'     \~~~/ \n\'-=-\' \~~~/   \_/ \n       \_/     Y \n        Y     _|_ \n       _|_ "],
            "00003k" : ["cup glass drink wine cocktail"," ____________ \n<____________> \n|            | \n|            | \n|            | \n \          / \n  \________/ \n      || \n      || \n      || \n      || \n   ___||___ \n  /   ||   \ \n  \________/ "],
            "00003l" : ["cup glass drink wine cocktail"," _..--\"\"````\"\"--.._ \n(_                _;..--\"\"````\"\"--.._ \n\ ```\"\"\"----\"\"\"```(_                _) \n \'-.            .-\ ```\"\"\"----\"\"\"``` / \n    `\        /`   \'-.            .-\' \n      \'-.__.-\'        `\        /` \n         ||             \'-.__.-\' \n         ||                || \n         ||                || \n         ||                || \n    _..--||--.._           || \n   (_          _)     _..--||--.._ \n     ```\"\"\"\"```      (_          _) \n                       ```\"\"\"\"``` "],
            "00003m" : ["cup glass drink wine cocktail bottle","                           ( \n*                           )   * \n              )     *      ( \n    )        (                   ( \n   (          )     (             ) \n    )    *           )        )  ( \n   (                (        (      * \n    )          H     )        ) \n              [ ]            ( \n       (  *   |-|       *     )    ( \n *      )     |_|        .          ) \n       (      | |    .   \n )           /   \     .    \' .        * \n(           |_____|  \'  .    .   \n )          | ___ |  \~~~/  \' .   ( \n        *   | \ / |   \_/  \~~~/   ) \n            | _Y_ |    |    \_/   ( \n*           |-----|  __|__   |      * \n            `-----`        __|__ "],
            "00003n" : ["cup glass drink cocktail","()   ()      ()    / \n  ()      ()  ()  / \n   ______________/___ \n   \            /   / \n    \^^^^^^^^^^/^^^/ \n     \     ___/   / \n      \   (   )  / \n       \  (___) / \n        \ /    / \n         \    / \n          \  / \n           \/ \n           || \n           || \n           || \n           || \n           || \n           /\ \n          /;;\ \n     ============== "],
            "00003o" : ["cup glass drink cocktail","                   o           o  \n                      o   o     \n                         o         o \n \n                     o       o  o  \n                  ________._____________ \n                  |   .                | \n                  |^^^.^^^^^.^^^^^^.^^^| \n                  |     .   .   .      | \n                   \      . . . .     / \n                     \     .  .     /  \n                       \    ..    /  \n                         \      / \n                           \  / \n                            \/ \n                            || \n                            || \n                            || \n                            || \n                            || \n                            /\ \n                           /;;\ \n                      ============== "],
            "00003p" : ["wine coctail drink cup glass","*      *    .   *    . \n     ..  *    o \n   o   *  .    * \n     ________ \n    (________) \n    |    o   | \n    | o    o | \n    |   o    | \n    | o    o | \n    | o  o   | \n    |      o | \n    ( o      ) \n     \   o  / \n      \    / \n       \  / \n        || \n        || \n        || \n        || \n        || \n     ___||___ \n    /   ||   \ \n    \________/ "],
            "00003q" : ["wine coctail drink cup glass","                                                   .\'\'\'\'. \n                                                  /,.--. ) \n                             .\'``.        __   __((\- -(\) \n                    _______.\'     \_.-\'\'\'\'  ``\'  /)) - .\| \n   __....::::::::::\'\'\'\'\'\'\'/    .   \\'\'\'\'\'\'\'::::::(/ `-\'`.) \n.:\'::.  .  o ~ .  ~  o ~ /    /     \'.o ~ . _.....--- `  \ \n \':. \':::::.___.____,___/   ,\'_\      \ _.-\'___..___..._,\' \n   \':.  o~  `::::::::::::::::::::::::::::::::::::::::\'  (\ \n    `\':.  o ~  o   ..   o  ,  ~  \ . o~   -.  ~   .\'.:\'\\'( \n       \':.  ,..   o  ~   o  . ,  \'o.    ~ o   ~ o\'.:\'  \(/ \n         \'.   o   ~   .    ~    o ~ \',o :  :  .\' .\' (\'\/ | \n           \'-._    ~    o  , o  ,  .  ~._ _.o_.-\'  \/ ) ( \n               \'- .._  .    ~    ~      _.. -\' \n                     \'\'\' - .,.,. - \'\'\' \n                          (:\' .:) \n                           :| \'| \n                           |. || \n                           || :| \n                           :| |\' \n                           || :| \n                           \'| || \n                           |: \': \n                           || :| \n                     __..--:| |\'--..__ \n               _...-\'  _.\' |\' :| \'.__ \'-..._ \n             / -  ..---    \'\'\'\'\'   ---...  _ \ \n             \  _____  ..--   --..     ____  / \n              \'-----....._________.....-----\' "],
            "00003r" : ["coffee and tea","  ;)( ; \n :----:     o8Oo./ \nC|====| ._o8o8o8Oo_. \n |    |  \========/ \n `----\'   `------\' "],
            "00003s" : ["tea teapot","             ;,\' \n     _o_    ;:;\' \n ,-.\'---`.__ ; \n((j`=====\',-\' \n `-\     / \n    `-=-\' "],
            "00003t" : ["coffee mug","      )  ( \n     (   ) ) \n      ) ( ( \n    _______)_ \n .-\'---------|   \n( C|/\/\/\/\/| \n \'-./\/\/\/\/| \n   \'_________\' \n    \'-------\' "],
            "00003u" : ["tea cup glass coffee","    (  )   (   )  ) \n     ) (   )  (  ( \n     ( )  (    ) ) \n     _____________ \n    <_____________> ___ \n    |             |/ _ \ \n    |               | | | \n    |               |_| | \n ___|             |\___/ \n/    \___________/    \ \n\_____________________/ "],
            "00003v" : ["teabag tea","            .------.____ \n         .-\'       \ ___) \n      .-\'         \\\ \n   .-\'        ___  \\) \n.-\'          /  (\  |) \n         __  \  ( | | \n        /  \  \__\'| | \n       /    \____).-\' \n     .\'       /   | \n    /     .  /    | \n  .\'     / \/     | \n /      /   \     | \n       /    /    _|_ \n       \   /    /\ /\ \n        \ /    /__v__\ \n         \'    |       | \n              |     .#| \n              |#.  .##| \n              |#######| \n              |#######| \n "],
            "00003w" : ["tea cup glass coffee","                      ( \n                        )     ( \n                 ___...(-------)-....___ \n             .-\"\"       )    (          \"\"-. \n       .-\'``\'|-._             )         _.-| \n      /  .--.|   `\"\"---...........---\"\"`   | \n     /  /    |                             | \n     |  |    |                             | \n      \  \   |                             | \n       `\ `\ |                             | \n         `\ `|                             | \n         _/ /\                             / \n        (__/  \                           / \n     _..---\"\"` \                         /`\"\"---.._ \n  .-\'           \                       /          \'-. \n :               `-.__             __.-\'              : \n :                  ) \"\"---...---\"\" (                 : \n  \'._               `\"--...___...--\"`              _.\' \n    \\\"\"--..__                              __..--\"\"/ \n     \'._     \"\"\"----.....______.....----\"\"\"     _.\' \n        `\"\"--..,,_____            _____,,..--\"\"` \n                      `\"\"\"----\"\"\"` "],
            "00003x" : ["grapes fruit","  \ \n ()() \n()()() \n ()() \n  () "],
            "00003y" : ["pizza eat","// \"\"--.._ \n||  (_)  _ \"-._ \n||    _ (_)    \'-. \n||   (_)   __..-\' \n \\__..--\"\" "],
            "00003z" : ["egg food","  ,\'\"`. \n /     \ \n:       : \n:       : \n `.___, "],
            "00003A" : ["eggs food","  ,-\"\"\"\"-.     ,\'\"`. \n /        `.  /     \ \n|           );       : \n \        ,\' :       ; \n  `-....-\'    `.___,\' "],
            "00003B" : ["gingerbread man","   ,-. \n _(*_*)_ \n(_  o  _) \n  / o \ \n (_/ \_) "],
            "00003C" : ["cake food","   $$  $$  $$ \n __||__||__||__ \n| * * * * * * *| \n|* * * * * * * | \n| * * * * * * *| \n|______________| "],
            "00003D" : ["pineapple","   \||/ \n   \||/ \n .<><><>. \n.<><><><>. \n\'<><><><>\' \n \'<><><>\' "],
            "00003E" : ["pie food","         ( \n          ) \n     __..---..__ \n ,-=\'  /  |  \  `=-. \n:--..___________..--; \n \.,_____________,./ "],
            "00003F" : ["cheese food","    ___ \n  .\'o O\'-._ \n / O o_.-`| \n/O_.-\'  O | \n| o   o .-` \n|o O_.-\' \n\'--` "],
            "00003G" : ["wok"," __       ___,.-------..__        __ \n//\\ _,-\'\'                `\'--._ //\\ \n\\ ;\'                           `: // \n `(                               )\' \n   :.                           ,; \n    `.`--.___           ___.--\',\' \n      `.     ``-------\'\'     ,\' \n         -.               ,- \n            `-._______.-\' "],
            "00003H" : ["acorn","          _ \n        _/-\_  \n     .-`-:-:-`-. \n    /-:-:-:-:-:-\ \n    \:-:-:-:-:-:/ \n     |`       `| \n     |         | \n     `\       /\' \n       `-._.-\' \n          ` "],
            "00003I" : ["grappes fruit","   _         )). \n,))-._--__.-)) \n   .-.||.  .. \n  (°  )\'°)(° ) \n   \'-\'_)(° ). )  \n   (_ .-.\'\'_ )_   \n  (° (°  )° )  \')) \n   \'\' \'-\'.-\'.-. \n   mrf(°  )(.° ). _ \n   ____\'_\'(__)\'__)_). "],
            "00003J" : ["bowl","    (\ \n     \ \ \n __    \/ ___,.-------..__        __ \n//\\ _,-\'\\               `\'--._ //\\ \n\\ ;\'      \\                   `: // \n `(          \\                   )\' \n   :.          \\,----,         ,; \n    `.`--.___   (    /  ___.--\',\' \n      `.     ``-----\'-\'\'     ,\' \n         -.               ,- \n            `-._______.-\' "],
            "00003K" : ["pizza food","        _....._ \n    _.:`.--|--.`:._ \n  .: .\'\o  | o /\'. \'. \n // \'.  \ o|  /  o \'.\ \n//\'._o\'. \ |o/ o_.-\'o\\ \n|| o \'-.\'.\|/.-\' o   || \n||--o--o-->| "],
            "00003L" : ["raspberry fruit","            _ \n        /> //  __ \n    ___/ \// _/ / \n  ,\' , \_/ \/ _/__ \n /    _/ |--\  `  `~, \n\' , ,/  /`\ / `  `   `, \n|    |  |  \> `  `  ` | \n|  ,  \/ \' \'    `  `  / \n`,   \'  \'    \' `  \'  / \n  \ `      \'  \' ,  ,\' \n   \ ` ` \'    ,  ,/ \n    `,  `  \'  , ,\' \n      \ `  ,   /         \n       `~----~\' "],
            "00003M" : ["graphes wine cup glass fruit","     __ \n __ {_/  \n \_}\\ _ \n    _\(_)_ \n   (_)_)(_)_ \n  (_)(_)_)(_) \n   (_)(_))_)  ____ \n    (_(_(_)  |    |  ____ \n     (_)_)   |~~~~| |    | \n      (_)    \'-..-\' |~~~~| \n               ||   \'-..-\' \n              _||_    || \n             `\"\"\"\"`  _||_ \n                    `\"\"\"\"` "],
            "00003N" : ["croissant food","   ____                                    ?~~bL \n  z@~ b                                    |  `U, \n ]@[  |                                   ]\'  z@\' \n d@~\' `|, .__     _----L___----, __, .  _t\'   `@j \n`@L_,   \"-~ `--\"~-a,           `C.  ~\"\"O_    ._`@ \n q@~\'   ]P       ]@[            `Y=,   `H+z_  `a@ \n `@L  _z@        d@               Ya     `-@b,_a\' \n  `-@d@a\'       )@[               `VL      `a@@\' \n    aa~\'   ],  .a@\'                qqL  ), ./~ \n    @@_  _z~  _d@[                 .V@  .L_d\' \n     \"~@@@\'  ]@@@\'        __      )@n@bza@-\" \n       `-@zzz@@@L        )@@z     ]@@=%-\" \n         \"~~@@@@@bz_    _a@@@@z___a@K \n             \"~-@@@@@@@@@@@@@@@@@@~\" \n                `~~~-@~~-@@~~~~~\' "],
            "00003O" : ["milk bottle","   _________ \n  | _______ | \n / \         \ \n/___\_________\ \n|   | \       | \n|   |  \      | \n|   |   \     | \n|   | M  \    | \n|   |     \   | \n|   |\  I  \  | \n|   | \     \ | \n|   |  \  L  \| \n|   |   \     | \n|   |    \  K | \n|   |     \   | \n|   |      \  | \n|___|_______\_| "],
            "00003P" : ["piece cake","                   . \n                  / `. \n                .\'... `-. \n              .\'.. .   ..\ \n             /. . . .   ..`. \n            /...  ... .    .\ \n           /.. . ........   .\ \n         .\'.   ...   ......  .| \n       .\' ... . ..... . ..--\'.| \n     .\' ...  ...   ._.--\'    .| \n   .\'... . ...  _.-\'O   OO O .| \n  /... .___.---\'O OO .O. OO O.| \n /__.--\' OO O  .OO O  OO O ...| \n | OO OO O OO . .O. OO O  ..O.| \n (O. OO. .O O O O  OO  ..OO O.| \n ( OO .O. O  O  OO............| \n (OOO........O_______.-------\' \n |_____.-----\' "],
            "00003Q" : ["cherries","                d888P \n      d8b d8888P:::P \n    d:::888b::::::P \n   d:::dP8888b:d8P \n  d:::dP 88b  Yb   .d8888b. \n d::::P  88Yb  Yb .P::::::Y8b \n 8:::8   88`Yb  YbP::::   :::b \n 8:::P   88 `8   8!:::::::::::b \n 8:dP    88  Yb d!!!::::::::::8 \n 8P    ..88   Yb8!!!::::::::::P \n  .d8:::::Yb  d888VKb:!:!::!:8 \n d::::::  ::dP:::::::::b!!!!8 \n8!!::::::::P::::::::::::b!8P \n8:!!::::::d::::::: ::::::b \n8:!:::::::8!:::::::  ::::8 \n8:!!!:::::8!:::::::::::::8 \nYb:!!:::::8!!::::::::::::8 \n 8b:!!!:!!8!!!:!:::::!!:dP \n  `8b:!!!:Yb!!!!:::::!d88 \n      \"\"\"  Y88!!!!!!!d8P \n              \"\"\"\"\"\"\" "],
            "00003R" : ["happy birthday cake","              (        ( \n             ( )      ( )          ( \n      (       Y        Y          ( ) \n     ( )     |\"|      |\"|          Y \n      Y      | |      | |         |\"| \n     |\"|     | |.-----| |---.___  | | \n     | |  .--| |,~~~~~| |~~~,,,,\'-| | \n     | |-,,~~\'-\'___   \'-\'       ~~| |._ \n    .| |~       // ___            \'-\',,\'. \n   /,\'-\'     <_// // _  __             ~,\ \n  / ;     ,-,     \\_> <<_______________;_) \n  | ;    {(_)} _,      . |================| \n  | \'-._ ~~,,,           | ,,             | \n  |     \'-.__ ~~~~~~~~~~~|________________|    \n  |\         `\'----------| \n  | \'=._                 | \n  :     \'=.__            | \n   \         `\'==========| \n    \'-._                 | \n        \'-.__            | \n             `\'----------| "],
            "00003S" : ["kitchen dinner cook ","                            _          _ \n                           (c)___c____(c) \n                            \ ........../ \n                             |.........| \n                              |.......| \n                              |.......| \n                              |=======| \n                              |=======| \n                             __o)\"\"\"\"::? \n                            C__    c)::; \n                               >--   ::     /\ \n                               (____/      /__\ \n                               } /\"\"|      |##| \n                    __/       (|V ^ )\     |##| \n                    o | _____/ |#/ / |     |##| \n           @        o_|}|_____/|/ /  |     |##| \n                          _____/ /   |     ~!!~ \n              ======ooo}{|______)#   |     /`\'\ \n          ~~~~ ;    ;          ###---|8     \"\" \n        ____;_____;____        ###====     /:|\ \n       (///0///@///@///)       ###@@@@| \n       |~~~~~~~~~~~~~~~|       ###@@@@| \n        \             /        ###@@@@|               + \n         \___________/         ###xxxxx      /\      // \n           H H   H  H          ###|| |      /  \    // \n           H H   H  H           | || |     /____\  /~_^_ \n           H H   H  H           C |C |     _|@@|_ /__|#|_ \n           H H   H  H            || ||    /_|@@|_/___|#|/| \n v    \/   H(o) (o) H            || ::   |:::::::::::::|#| \n ~    ~~  (o)      (o)        Ccc__)__)  |ROMAN CANDLES|#| \n  \|/      ~   @* & ~                    |:::::::::::::|/  \|/ \n   ~           \|/        !!        \ !/  ~~~~~~~~~~~~~    ~~~ \n               ~~~        ~~         ~~           ~~ \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "],
            "00003T" : ["cake happy birthday","                       *  \n                                  *  \n     *                                             *  \n                                          *  \n               *  \n                             *  \n                                                       *  \n    *  \n                                             *  \n        *  \n                      *             *  \n                                                *  \n *                                                               *  \n          *  \n                          (             )  \n                  )      (*)           (*)      (  \n         *       (*)      |             |      (*)  \n                  |      |~|           |~|      |          *  \n                 |~|     | |           | |     |~|  \n                 | |     | |           | |     | |  \n                ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.  \n           .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.  \n         ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,  \n        a@@@@@@@@@@@@@@@@@@@@@\' . `@@@@@@@@@@@@@@@@@@@@@@@@a  \n        ;`@@@@@@@@@@@@@@@@@@\'   .   `@@@@@@@@@@@@@@@@@@@@@\';  \n        ;@@@`@@@@@@@@@@@@@\'     .     `@@@@@@@@@@@@@@@@\'@@@;  \n        ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;  \n        ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;  \n        ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;  \n        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;  \n        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@a;  \n    ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,  \n .%%%%%%;;;;;;;a@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,  \n.%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,  \n%%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;\'%%%%%%%%  \n%%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;\'%%%%%%%%%%%%  \n`%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%\'  \n  `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\'  \n      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\'  \n             \"\"\"\"\"\"\"\"\"\"\"\"\"\"`,,,,,,,,,\'\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"  \n                            `%%%%%%%\'  \n                             `%%%%%\'  \n                               %%%  \n                              %%%%%  \n                           .,%%%%%%%,.  \n                      ,%%%%%%%%%%%%%%%%%%%,  \n          --------------------------------------------- "],
            "00003U" : ["amnesty international logo","          |\ \n         /  |          \n        |  /           \n        _\|__          \n       |     |         \n   __X-|     |-X__     \n /~    |     |     \   \nX      |     |      X \n       |     |     / \n   _X-----X----X ~     \n /     |     | \nX      |     |      X  \n \     |     |    _/   \n   X~--|     |-X~~     \n       |_    |         \n         ~--_| "],
            "00003V" : ["bio hazard logo","      .  . \n      dOO  OOb \n     dOP\'..\'YOb \n     OOboOOodOO \n   ..YOP.  .YOP.. \n dOOOOOObOOdOOOOOOb \ndOP\' dOYO()OPOb \'YOb \n    O   OOOO   O     \nYOb. YOdOOOObOP .dOP \n YOOOOOOP  YOOOOOOP \n   \'\'\'\'      \'\'\'\' "],
            "00003W" : ["bio hazard logo","         _   _ \n       .-_; ;_-. \n      / /     \ \ \n     | |       | | \n      \ \.---./ / \n  .-\"~   .---.   ~\"-. \n,`.-~/ .\'`---`\'. \~-.`, \n\'`   | | \(_)/ | |   `\' \n,    \  \ | | /  /    , \n;`\'.,_\  `-\'-\'  /_,.\'`; \n \'-._  _.-\'^\'-._  _.-\' \n        ``         `` "],
            "00003X" : ["bio hazard logo","                         __    _                                    \n                    _wr\"\"        \"-q__                              \n                 _dP                 9m_      \n               _#P                     9#_                          \n              d#@                       9#m                         \n             d##                         ###                        \n            J###                         ###L                       \n            {###K                       J###K                       \n            ]####K      ___aaa___      J####F                       \n        __gmM######_  w#P\"\"   \"\"9#m  _d#####Mmw__                   \n     _g##############mZ_         __g##############m_                \n   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_              \n  a###\"\"          ,Z\"#####@\" \'######\"\g          \"\"M##m             \n J#@\"             0L  \"*##     ##@\"  J#              *#K            \n #\"               `#    \"_gmwgm_~    dF               `#_           \n7F                 \"#_   ]#####F   _dK                 JE           \n]                    *m__ ##### __g@\"                   F           \n                       \"PJ#####LP\"                                  \n `                       0######_                      \'            \n                       _0########_                                    \n     .               _d#####^#####m__              ,               \n      \"*w_________am#####P\"   ~9#####mw_________w*\"                   \n          \"\"9@#####@M\"\"           \"\"P@#####@M\"\"            "],
            "00003Y" : ["hello kitty"," _   _         _  _          _   __ _ \n| | | |  ___  | || |  ___   | | / /(_)  _     _ \n| |_| | / _ \ | || | / _ \  | |/ /  _ _| |_ _| |_  _  _ \n|  _  |/ /_\ \| || |/ / \ \ |   /  | |_   _|_   _|| |/ / \n| | | |\ ,___/| || |\ \_/ / | |\ \ | | | |_  | |_ | / / \n|_| |_| \___/ |_||_| \___/  |_| \_\|_| \___| \___||  / \n                       _           _              / / \n                      / \_______ /|_\             \/ \n                     /          /_/ \__ \n                    /             \_/ / \n                  _|_              |/|_ \n                  _|_  O    _    O  _|_ \n                  _|_      (_)      _|_ \n                   \                 / \n                    _\_____________/_ \n                   /  \/  (___)  \/  \ \n                   \__(  o     o  )__/ "],
            "00003Z" : ["hello kitty","             ..                     .\'\'. \n            c  \'.          _,,    .\'    \' \n           ,     ,   ___  7###. .\'       \' \n          .       `-\'   \'\'|####;#\'. .##, . \n          ,               \'####.##,######. \n         .                 \'  \' \'\' ,####. \n        \'                           \'##\'. \n       \'                                . \n__,,--.--                                \' \n      \'                                  \' \n  .--|-        &&                        -\'-\'\'\'-.._ \n     |         \'&              &&         \' \n    __,-                       \'&        -\'---. \n  \'\'  ,                                   ; \n       .             kk.                 -.-,_ \n        -_           \'\'KK                ; \n          \'\'--,_                        , \n                \'\'--,__           __,,--\' \n                       \'\'--..,--\'\' "],                        
            "000040" : ["coca cola coke","         __                              ___   __        .ama     , \n      ,d888a                          ,d88888888888ba.  ,88\"I)   d \n     a88\']8i                         a88\".8\"8)   `\"8888:88  \" _a8\' \n   .d8P\' PP                        .d8P\'.8  d)      \"8:88:baad8P\' \n  ,d8P\' ,ama,   .aa,  .ama.g ,mmm  d8P\' 8  .8\'        88):888P\' \n ,d88\' d8[ \"8..a8\"88 ,8I\"88[ I88\' d88   ]IaI\"        d8[          \n a88\' dP \"bm8mP8\'(8\'.8I  8[      d88\'    `\"         .88           \n,88I ]8\'  .d\'.8     88\' ,8\' I[  ,88P ,ama    ,ama,  d8[  .ama.g \n[88\' I8, .d\' ]8,  ,88B ,d8 aI   (88\',88\"8)  d8[ \"8. 88 ,8I\"88[ \n]88  `888P\'  `8888\" \"88P\"8m\"    I88 88[ 8[ dP \"bm8m88[.8I  8[ \n]88,          _,,aaaaaa,_       I88 8\"  8 ]P\'  .d\' 88 88\' ,8\' I[ \n`888a,.  ,aadd88888888888bma.   )88,  ,]I I8, .d\' )88a8B ,d8 aI \n  \"888888PP\"\'        `8\"\"\"\"\"\"8   \"888PP\'  `888P\'  `88P\"88P\"8m\" "],
            "000041" : ["coca cola coke","         __                              ___   __        .ama     , \n      ,d888a                          ,d88888888888ba.  ,88\"I)   d \n     a88\']8i                         a88\".8\"8)   `\"8888:88  \" _a8\' \n   .d8P\' PP                        .d8P\'.8  d)      \"8:88:baad8P\' \n  ,d8P\' ,ama,   .aa,  .ama.g ,mmm  d8P\' 8  .8\'        88):888P\' \n ,d88\' d8[ \"8..a8\"88 ,8I\"88[ I88\' d88   ]IaI\"        d8[ \n a88\' ]P \"bm8mP8\'(8\'.8I  8[      d88\'    `\"         .88 \n,88I ]P[  .I\'.8     88\' ,8\' I[  ,88P ,ama    ,ama,  d8[  .ama.g \n[88\' I8, .I\' ]8,  ,88B ,d8 aI   (88\',88\"8)  d8[ \"8. 88 ,8I\"88[ \n]88  `8888\"  \'8888\" \"88P\"8m\"    I88 88[ 8[ ]P \"bm8m88[.8I  8[ \n]88,          _,,aaaaaa,_       I88 8\"  8 ]P[  .I\' 88 88\' ,8\' I[ \n`888a,.  ,aadd88888888888bma.   )88,  ,]I I8, .I\' )88a8B ,d8 aI \n  \"888888PP\"\'        `8\"\"\"\"\"\"8   \"888PP\'  `8888\"  `88P\"88P\"8m\" "],
            "000042" : ["coca cola coke","           .e$.                           z$$e.d$$$.      z$b   z \n         d$\" .d                        .$$\" d\"F ^*$$$e  z$\" $ .$ \n       e$P   $%                       d$P .\"  F    \"$$\"d$  .e$\" \n      $$F                           .$$\"  F  J       \"$$z$$$\" \n    .$$\"   .$\"3   .$\"\"  .$P $$  $$ 4$$\"  $  4\"       $$  . \n   .$$F   d$  4  d$ d$ z$\" J$%    4$$\"   $.d\"       $$  .\" \n   $$P   $$ \".$z$$  ^ z$\" .$P    .$$F              $$\" .\" \n  $$$   d$F  J $$F   z$$  $$ .   $$$   ze     .c  J$F z  .e.ze \n 4$$F   $$  4\" $$   z$$  $$\".\"  d$$  d$\" $  z$\" $ $$ @  $$\".$F \n $$$   4$$.d\" 4$$ .$3$$.$$$e%   $$P J$P  P d$*  %$$$\"  $$  $$ \n $$$    $$*    $$$\" ^$$\"\'$$    4$$% $$\" . d$\" \"$\"$$   $$  $$ \n $$$                           $$$  \"   P4$P  z 4$F  $$\" J$% % \n \'$$c          .e$$$$$$$$e     $$$F    $ $$  z\" $$  $$$ 4$$ P \n  \"$$b.   .e$*\"     \"$$$$$$$   \'$$$c.dP  $$$$\"  $$$\"$$$$$$$P \n    \"*$$$*\"           \"          *$$*\"   \"$*    \"$\" ^$* \"$\" \nGilo94\' "],
            "000043" : ["coca cola coke","     z$$$$$. $$ \n    $$$$$$$$$$$ \n   $$$$$$**$$$$             eeeeer \n  $$$$$%   \'$$$             $$$$$F \n 4$$$$P     *$$             *$$$$F \n $$$$$      \'$$    .ee.      ^$$$F            ..e. \n $$$$$       \"\"  .$$$$$$b     $$$F 4$$$$$$   $$$$$$c \n4$$$$F          4$$$\"\"$$$$    $$$F \'*$$$$*  $$$P\"$$$L \n4$$$$F         .$$$F  ^$$$b   $$$F  J$$$   $$$$  ^$$$. \n4$$$$F         d$$$    $$$$   $$$F J$$P   .$$$F   $$$$ \n4$$$$F         $$$$    3$$$F  $$$FJ$$P    4$$$\"   $$$$ \n4$$$$F        4$$$$    4$$$$  $$$$$$$r    $$$$$$$$$$$$ \n4$$$$$        4$$$$    4$$$$  $$$$$$$$    $$$$******** \n $$$$$        4$$$$    4$$$F  $$$F4$$$b   *$$$r \n 3$$$$F       d$$$$    $$$$\"  $$$F *$$$F  4$$$L     . \n  $$$$$.     d$$$$$.   $$$$   $$$F  $$$$.  $$$$    z$P \n   $$$$$e..d$$$\"$$$b  4$$$\"  J$$$L  \'$$$$  \'$$$b..d$$ \n    *$$$$$$$$$  ^$$$be$$$\"  $$$$$$$  3$$$$F \"$$$$$$$\" \n     ^*$$$$P\"     *$$$$*    $$$$$$$   $$$$F  ^*$$$\" "],
            "000044" : ["no smokeing sign","      __    __    ) \n      \\\  ///   ( \n   _ __\\\///_____ ) \n  [_[___>><<______# \n       ///\\\ \n      ///  \\\ "],
            "000045" : ["no smokeing sign","       _..----.._ \n    _-\'_..----.._\'-_ \n  .\'.  \       ( `\'.\'. \n / / `\ `\       )  \ \ \n| |   _`\ `\____(    | | \n| |  [__]_\ `\__()   | | \n| |        `\ `\     | | \n \ \         `\ `\  / / \n  \'.\'-._       `\ `\'.\' \n    `-._`\'----\'`_.-\' \n        `\"----\"` "],
            "000046" : ["no smokeing sign","                          .,aad88888888888baa,. \n                     ,ad8888888888888888888888888ba,. \n                 ,ad888888888888888888888888888888888ba, \n              ,ad888888888P\"\"\'            \"\"\"Y88888888888ba. \n            ,d88888888P\"\"                       \"\"Y888888888ba \n          a888888888\"                               \"\"Y88888888b, \n        ,888888888b,                                   \"\"Y8888888b, \n       d888888888888b,                                    \"Y8888888b, \n     ,8888888\' \"888888b,                                    \"Y8888888b \n    ,888888\"     \"Y88888b,                                    \"Y888888b \n   ,888888\'        \"Y88888b,                                    \"888888b \n  ,888888\'     a,  8a\"Y88888b,                                   `888888a \n ,888888\'      `8, `8) \"Y88888b,                  ,adPPRg,        `888888, \n 888888\'        8)  ]8   \"Y88888b,            ,ad888888888b        Y88888b \nd88888P        ,8\' ,8\'     \"Y88888b,      ,gPPR888888888888        `888888, \n888888\'       ,8\' ,8\'        \"Y88888b,,ad8\"\"   `Y888888888P         )88888) \n888888        8)  8)           \"Y888888\"        (8888888\"\"          (88888) \n888888        8,  8,          ,ad8Y88888b,      d888\"\"              d88888) \n888888        `8, `8,     ,ad8\"\"   \"Y88888b,,ad8\"\"                  888888) \n888888         `8, `\" ,ad8\"\"         \"Y88888b\"                     ,888888\' \nY88888,           ,gPPR8b           ,ad8Y88888b,                   d888888 \n`88888b          dP:::::Yb      ,ad8\"\"   \"Y88888b,                ,888888P \n 888888,         8):::::(8  ,ad8\"\"         \"Y88888b,              d888888\' \n `888888,        Yb:;;;:d888\"\"               \"Y88888b,           d888888P \n  Y888888,        \"8ggg8P\"                     \"Y88888b,       ,d888888P \n   Y88888b,                                      \"Y88888b,    ,8888888\" \n    Y88888b,                                       \"Y88888b, d8888888\" \n     Y888888,                                        \"Y888888888888P\' \n      \"888888b,                                        \"8888888888\" \n        Y888888b,                                     ,888888888\" \n          Y8888888ba,                              ,a888888888\" \n            \"Y88888888ba,._                   .,ad888888888P\" \n               \"Y88888888888bbaa,,_____,,aadd88888888888\"\" \n                   \"Y8888888888888888888888888888888\"\" \n                       \"\"Y888888888888888888888P\"\" \n                              \"\"\"\"\"\"\"\"\"\"\"\"\"\" "],
            "000047" : ["dollar money","___________________________________ \n|#######====================#######| \n|#(1)*UNITED STATES OF AMERICA*(1)#| \n|#**          /===\   ********  **#| \n|*# {G}      | (\") |             #*| \n|#*  ******  | /v\ |    O N E    *#| \n|#(1)         \===/            (1)#| \n|##=========ONE DOLLAR===========##| \n------------------------------------ "],
            "000048" : ["dollar money coin","          __-----__ \n     ..;;;--\'~~~`--;;;.. \n   /;-~IN GOD WE TRUST~-.\ \n  //      ,;;;;;;;;      \\ \n.//      ;;;;;    \       \\ \n||       ;;;;(   /.|       || \n||       ;;;;;;;   _\      || \n||       \';;  ;;;;=        || \n||LIBERTY | \'\'\;;;;;;      || \n \\     ,| \'\  \'|><| 1995 // \n  \\   |     |      \  A // \n   `;.,|.    |      \'\.-\'/ \n     ~~;;;,._|___.,-;;;~\' \n         \'\'=--\' "],
            "000049" : ["dollar money coin","        _.-\'~~`~~\'-._ \n     .\'`  B   E   R  `\'. \n    / I               T \ \n  /`       .-\'~\"-.       `\ \n ; L      / `-    \      Y ; \n;        />  `.  -.|        ; \n|       /_     \'-.__)       | \n|        |-  _.\' \ |        | \n;        `~~;     \\        ; \n ;  INGODWE /      \\)P    ; \n  \  TRUST \'.___.-\'`\"     / \n   `\                   /` \n     \'._   1 9 9 7   _.\' \n        `\'-..,,,..-\'` "],
            "00004a" : ["dollar money","||====================================================================|| \n||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\|| \n||(100)==================| FEDERAL RESERVE NOTE |================(100)|| \n||\\$//        ~         \'------========--------\'                \\$//|| \n||<< /        /$\              // ____ \\                         \ >>|| \n||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<|| \n||<<|        \\ //           || <||  >\  ||                        |>>|| \n||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<|| \n||<<|      L38036133B        *\\  |\_/  //* series                 |>>|| \n||>>|  12                     *\\/___\_//*   1989                  |<<|| \n||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>|| \n||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\|| \n||(100)===================  ONE HUNDRED DOLLARS =================(100)|| \n||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//|| \n||====================================================================|| "],
            "00004b" : ["dollar money","  _____________________________________________________________________ \n |.============[_F_E_D_E_R_A_L___R_E_S_E_R_V_E___N_O_T_E_]============.| \n ||%&%&%&%_    _        _ _ _   _ _  _ _ _     _       _    _ %&%&%&%&|| \n ||%&%&%&/||_||_ | ||\||||_| \ (_ ||\||_(_  /\|_ |\|V||_|)|/ |\ \%&%&%|| \n ||&%.--.}|| ||_ \_/| ||||_|_/ ,_)|||||_,_) \/|  ||| ||_|\|\_||{.--.%&|| \n ||%/__ _\                ,-----,-\'____\'-,-----,               /__ _\ || \n ||||_ / \|              [    .-;\"`___ `\";-.    ]             ||_ / \||| \n |||  \| || \"\"\"\"\"\"\"\"\"\" 1  `).\'.\'.\'`_ _\'.  \'.\'.(` A 76355942 J |  \| |||| \n |||,_/\_/|                //  / .\'    \'\    \\               |,_/\_/||| \n ||%\    /   d8888b       //  | /   _  _ |    \\      .-\"\"\"-.  \    /%|| \n ||&%&--\'   8P |) Y8     ||   //;   a \a \     ||    //A`Y A\\  \'--\'%&|| \n ||%&%&|    8b |) d8     ||   \\ \'.   _> .|    ||    ||.-\'-.||   |&%&%|| \n ||%&%&|     Y8888P      ||    `|  `-\'_ ` |    ||    \\_/~\_//   |&%&%|| \n ||%%%%|                 ||     ;\'.  \' ` /     ||     \'-...-\'    |%&%&|| \n ||%&%&|  A 76355942 J  /;\  _.-\'. `-..\'`>-._  /;\               |%&%&|| \n ||&%.--.              (,  \':     \; >-\'`    ;` ,)              .--.%&|| \n ||%( 50 ) 1  \"\"\"\"\"\"\"  _( \  ;...---\"\"---...; / )_```\"\"\"\"\"\"\"1  ( 50 )%|| \n ||&%\'--\'============\`----------,----------------`/============\'--\'%&|| \n ||%&JGS&%&%&%&%&&%&%&) F I F T Y   D O L L A R S (%&%&%&%&%&%&&%&%&%&|| "],
            "00004c" : ["dollar money","  ______________________________________________________________________ \n |.============[_F_E_D_E_R_A_L___R_E_S_E_R_V_E___N_O_T_E_]=============.| \n ||%&%&%&%_    _        _ _ _   _ _  _ _ _     _       _    _  %&%&%&%&|| \n ||%&.-.&/||_||_ | ||\||||_| \ (_ ||\||_(_  /\|_ |\|V||_|)|/ |\ %&.-.&&|| \n ||&// |\ || ||_ \_/| ||||_|_/ ,_)|||||_,_) \/|  ||| ||_|\|\_|| &// |\%|| \n ||| | | |%               ,-----,-\'____\'-,-----,               %| | | ||| \n ||| | | |&% \"\"\"\"\"\"\"\"\"\"  [    .-;\"`___ `\";-.    ]             &%| | | ||| \n ||&\===//                `).\'\' .\'`_.- `. \'.\'.(`  A 76355942 J  \\===/&|| \n ||&%\'-\'%/1                // .\' /`     \    \\                  \%\'-\'%|| \n ||%&%&%/`   d8888b       // /   \  _  _;,    \\      .-\"\"\"-.  1 `&%&%%|| \n ||&%&%&    8P |) Yb     ;; (     > a  a| \    ;;    //A`Y A\\    &%&%&|| \n ||&%&%|    8b |) d8     || (    ,\   \ |  )   ||    ||.-\'-.||    |%&%&|| \n ||%&%&|     Y8888P      ||  \'--\'/`  -- /-\'    ||    \\_/~\_//    |&%&%|| \n ||%&%&|                 ||     |\`-.__/       ||     \'-...-\'     |&%&%|| \n ||%%%%|                 ||    /` |._ .|-.     ||                 |%&%&|| \n ||%&%&|  A 76355942 J  /;\ _.\'   \  } \  \'-.  /;\                |%&%&|| \n ||&%.-;               (,  \'.      \  } `\   \\'  ,)   ,.,.,.,.,   ;-.%&|| \n ||%( | ) 1  \"\"\"\"\"\"\"   _( \  ;...---------.;.; / )_ ```\"\"\"\"\"\"\" 1 ( | )%|| \n ||&%\'-\'==================\`------------------`/==================\'-\'%&|| \n ||%&JGS&%&%&%&%%&%&&&%&%%&)O N E  D O L L A R(%&%&%&%&%&%&%%&%&&&%&%%&|| \n \'\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"` "],
            "00004d" : ["dollar money","   ||====================================================================|| \n   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\|| \n   ||(100)==================| FEDERAL RESERVE NOTE |================(100)|| \n   ||\\$//        ~         \'------========--------\'                \\$//|| \n   ||<< /        /$\              // ____ \\                         \ >>|| \n   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<|| \n   ||<<|        \\ //           || <||  >\  ||                        |>>|| \n   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<|| \n||====================================================================||>|| \n||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<|| \n||(100)==================| FEDERAL RESERVE NOTE |================(100)||>|| \n||\\$//        ~         \'------========--------\'                \\$//||\|| \n||<< /        /$\              // ____ \\                         \ >>||)|| \n||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/|| \n||<<|        \\ //           || <||  >\  ||                        |>>||=|| \n||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<|| \n||<<|      L38036133B        *\\  |\_/  //* series                 |>>|| \n||>>|  12                     *\\/___\_//*   1989                  |<<|| \n||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>|| \n||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\|| \n||(100)===================  ONE HUNDRED DOLLARS =================(100)|| \n||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//|| \n||====================================================================|| "],
            "00004e" : ["dollar money coin","             _.oood\"\"\"\"\"\"\"booo._ \n         _.o\"\"      _____    * \"\"o._ \n       oP\"  _.ooo\"\"\"\"   \"\"\"\"o|o*_* \"Yo \n     o8   oP                 | |\"._* `8o \n    d\'  o8\'_.--._            | |/  ,\* `b \n   d\'  d\'.\' __   \".          | |: (( `\ \n  8\'  d\'/,-\"  `.   :         | |  ||\_/* `8 \n 8   8\'|/      :   :    |)   _ |  || |`|   8 \n,8  8          :  :   /)| \ || |\_|| | |8  8. \n8\' ,8         /  :    \" /_) |`:\' | | | |8. `8 \n8  8\'        /  /       _ _=\'  \ \' __   __  8 \n8  8        /  /        \|__ |  | |  | | 8| 8 \n8  8.      /  /         ||   |  | |-:\' | 8| 8 \n8. `8    ,\' ,\'       __/ |__ |__| |  \ |__|,8 \n`8  8  ,\' ,\'      _ /     __ . . . . . .8LL8\' \n 8   8\"   `------\'/(    ,\'  `.`. | | ,-|8  8 \n  8.(_________dd_/  \__/ \'  0|`.`: |: (8 ,8 \n   Y.  Y.                    | :/| |,\|* .P \n    Y.  \"8.          .,o     | | |,|\"*  ,P \n     \"8.  \"Yo_               | |p|\"* ,8\" \n       \"Y_   `\"ooo.__   __.oo|\"* * _P\" \n         `\'\"oo_     \"\"\"\"\"    * _oo\"\"\' \n              `\"\"\"boooooood\"\"\"\' "],
            "00004f" : ["balloons party","        ,,,,,,,,,,,,, \n    .;;;;;;;;;;;;;;;;;;;,. \n  .;;;;;;;;;;;;;;;;;;;;;;;;, \n.;;;;;;;;;;;;;;;;;;;;;;;;;;;;. \n;;;;;@;;;;;;;;;;;;;;;;;;;;;;;;\' ............. \n;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;\'................. \n;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;\'................... \n`;;;;@;;;;;;;;;;;;;;;@;;;;;;;\'..................... \n `;;;;;;;;;;;;;;;;;;;@@;;;;;\'..................;.... \n   `;;;;;;;;;;;;;;;;@@;;;;\'....................;;... \n     `;;;;;;;;;;;;;@;;;;\'...;.................;;.... \n        `;;;;;;;;;;;;\'   ...;;...............;..... \n           `;;;;;;\'        ...;;.................. \n              ;;              ..;............... \n              `                  ............ \n             `                      ...... \n            `                         .. \n           `                           \' \n          `                           \' \n         `                           \' \n        `                           ` \n        `                           `, \n        ` \n         ` \n           `. "],
            "00004g" : ["balloons party","             .#############.  \n          .###################.  \n       .####%####################.,::;;;;;;;;;;,  \n      .####%###############%######:::;;;;;;;;;;;;;,  \n      ####%%################%######:::;;;;;;;;@;;;;;;,  \n      ####%%################%%#####:::;;;;;;;;;@;;;;;;,  \n      ####%%################%%#####:::;;;;;;;;;@@;;;;;;  \n      `####%################%#####:::;;;;;;;;;;@@;;;;;;  \n        `###%##############%####:::;;;;;;;;;;;;@@;;;;;;  \n           `#################\'::%%%%%%%%%%%%;;;@;;;;;;\'  \n             `#############\'.%%%%%%%%%%%%%%%%%%;;;;;\'  \n               `#########\'%%%%#%%%%%%%%%%%%%%%%%%%,  \n                 `#####\'.%%%%#%%%%%%%%%%%%%%#%%%%%%,  \n                   `##\' %%%%##%%%%%%%%%%%%%%%##%%%%%  \n                   ###  %%%%##%%%%%%%%%%%%%%%##%%%%%  \n                    \'   %%%%##%%%%%%%%%%%%%%%##%%%%%  \n                   \'    `%%%%#%%%%%%%%%%%%%%%#%%%%%\'  \n                  \'       `%%%#%%%%%%%%%%%%%#%%%%\'  \n                  `         `%%%%%%%%%%%%%%%%%%\'  \n                   `          `%%%%%%%%%%%%%%\'  \n                    `           `%%%%%%%%%%\'  \'  \n                     \'            `%%%%%%\'   \'  \n                    \'              `%%%\'    \'  \n                   \'               .%%      `  \n                  `                %%%       \'  \n                   `                \'       \'  \n                    `              \'      \'  \n                    \'            \'      \'  \n                   \'           \'       `  \n                  \'           \'        \'  \n                              `       \'  \n                               \'  \n                              \'  \n                             \'  \n "],
            "00004h" : ["doll toy","    &&& \n   (+.+) \n ___\=/___ \n(|_ ~~~ _|) \n   |___| \n   / _ \ \n  /_/ \_\ \n /_)   (_\ "],
            "00004i" : ["doll toy","  &&&&&&& \n &&(+.+)&& \n ___\=/___ \n(|_ ~~~ _|) \n   )___( \n /\'     `\ \n~~~~~~~~~~~ \n`~//~~~\\~\' \n /_)   (_\ "],
            "00004j" : ["doll toy","       ,,,,,,,,,,,,,,, \n    ,(((((((((())))))))), \n  ,((((((((((()))))))))))), \n ,(((((((((\\\|///))))))))), \n,((((((((((///|\\\)))))))))), \n((((((((//////^\\\\\\)))))))) \n((((((\' .-\"\"-   -\"\"-. \')))))) \n(((((  `\.-.     .-./`  ))))) \n((((( -=(0) )   (0) )=- ))))) \n\'((((   /\'-\'     \'-\'\   ))))\' \n ((((\   _,   A  ,_    /)))) \n \'((((\    \     /    /))))\' \n   \'(((\'.   `-o-\'   .\')))\' \n         \'-.,___,.-\' "],
            "00004k" : ["sun","    | \n  \ | / \n   \*/ \n--**O**--  \n   /*\ \n  / | \ \n    | "],
            "00004l" : ["sun","     . \n   \ | / \n \'-.;;;.-\' \n-==;;;;;==- \n .-\';;;\'-. \n   / | \ \n     \' "],
            "00004m" : ["sun","       \' \n     \  ,  / \n \' ,___/_\___, \' \n    \ /o.o\ / \n-=   > \_/ <   =- \n    /_\___/_\ \n . `   \ /   ` . \n     /  `  \ \n        . "],
            "00004n" : ["sun","           | \n     \     |     / \n       \       / \n         ,d8b,           ., \n (\')-\")_ 88888 ---   ;\';\'  \';\'. \n(\'-  (. \')98P\'      \';.,;    ,; \n \'-.(PjP)\'     \       \'.\';.\' \n           |     \ \n           | "],

            }
        if id=="manual":
            self.model = modelastext
        else:
            self.model = self.models[id][1]
    
    # Function for changeing model color
    def changeColor(self,color):
        self.color = color

    # Function for changeing model row coordinate
    def changeRow(self,row):
        self.row = row

    # Function for changeing model column coordinate
    def changeColumn(self,column):
        self.column = column

    # Function for changeing model coordinates
    def changeCoordinates(self,row,column):
        self.row = row
        self.column = column

    # Print Model
    def printModel(self):
        print(self.models[self.id][1])

    # Save model as file
    def saveModelAsFile(self, file_name="model1.txt"):
        with open(file_name, "w") as f:
            f.write(self.model)


# Defining Screen class
class Screen():

    # Main function for setuping tools,makeing screen
    def __init__(self, rows=10, columns=20, main_symbol=" ", main_color=""):
        self.rows = rows
        self.columns = columns
        self.mainsymbol = main_symbol
        self.maincolor = main_color
        self.auto_update = True
        self.ostype = "linux"
        self.clearcommand = "clear"
        self.colors = {
            "": "",
            "reset": "\u001b[0m",
            "amaranth": "\033[38;2;229;43;80m",
            "amber": "\033[38;2;255;191;0m",
            "amethyst": "\033[38;2;153;102;204m",
            "apricot": "\033[38;2;251;206;177m",
            "aquamarine": "\033[38;2;127;255;212m",
            "azure": "\033[38;2;0;127;255m",
            "babyblue": "\033[38;2;137;207;240m",
            "beige": "\033[38;2;245;245;220m",
            "brickred": "\033[38;2;203;65;84m",
            "black": "\033[38;2;0;0;0m",
            "blue": "\033[38;2;0;0;255m",
            "bluegreen": "\033[38;2;0;149;182m",
            "blueviolet": "\033[38;2;138;43;226m",
            "blush": "\033[38;2;222;93;131m",
            "bronze": "\033[38;2;205;127;50m",
            "brown": "\033[38;2;150;75;0m",
            "burgundy": "\033[38;2;128;0;32m",
            "byzantium": "\033[38;2;112;41;99m",
            "carmine": "\033[38;2;150;0;24m",
            "cerise": "\033[38;2;222;49;99m",
            "cerulean": "\033[38;2;0;123;167m",
            "champagne": "\033[38;2;247;231;206m",
            "chartreusegreen": "\033[38;2;127;255;0m",
            "chocolate": "\033[38;2;123;63;0m",
            "cobaltblue": "\033[38;2;0;71;171m",
            "coffee": "\033[38;2;111;78;55m",
            "copper": "\033[38;2;184;115;51m",
            "coral": "\033[38;2;255;127;80m",
            "crimson": "\033[38;2;220;20;60m",
            "cyan": "\033[38;2;0;255;255m",
            "desertsand": "\033[38;2;237;201;175m",
            "electricblue": "\033[38;2;125;249;255m",
            "emerald": "\033[38;2;80;200;120m",
            "erin": "\033[38;2;0;255;63m",
            "gold": "\033[38;2;255;215;0m",
            "gray": "\033[38;2;128;128;128m",
            "green": "\033[38;2;0;255;0m",
            "harlequin": "\033[38;2;63;255;0m",
            "indigo": "\033[38;2;75;0;130m",
            "ivory": "\033[38;2;255;255;240m",
            "jade": "\033[38;2;0;168;107m",
            "junglegreen": "\033[38;2;41;171;135m",
            "lavender": "\033[38;2;181;126;220m",
            "lemon": "\033[38;2;255;247;0m",
            "lilac": "\033[38;2;200;162;200m",
            "lime": "\033[38;2;191;255;0m",
            "magenta": "\033[38;2;255;0;255m",
            "magentarose": "\033[38;2;255;0;175m",
            "maroon": "\033[38;2;128;0;0m",
            "mauve": "\033[38;2;224;176;255m",
            "navyblue": "\033[38;2;0;0;128m",
            "ochre": "\033[38;2;204;119;34m",
            "olive": "\033[38;2;128;128;0m",
            "orange": "\033[38;2;255;102;0m",
            "orangered": "\033[38;2;255;69;0m",
            "orchid": "\033[38;2;218;112;214m",
            "peach": "\033[38;2;255;229;180m",
            "pear": "\033[38;2;209;226;49m",
            "periwinkle": "\033[38;2;204;204;255m",
            "persianblue": "\033[38;2;28;57;187m",
            "pink": "\033[38;2;253;108;158m",
            "plum": "\033[38;2;142;69;133m",
            "prussianblue": "\033[38;2;0;49;83m",
            "puce": "\033[38;2;204;136;153m",
            "purple": "\033[38;2;128;0;128m",
            "raspberry": "\033[38;2;227;11;92m",
            "red": "\033[38;2;255;0;0m",
            "redviolet": "\033[38;2;199;21;133m",
            "rose": "\033[38;2;255;0;127m",
            "ruby": "\033[38;2;224;17;95m",
            "salmon": "\033[38;2;250;128;114m",
            "sangria": "\033[38;2;146;0;10m",
            "sapphire": "\033[38;2;15;82;186m",
            "scarlet": "\033[38;2;255;36;0m",
            "silver": "\033[38;2;192;192;192m",
            "slategray": "\033[38;2;112;128;144m",
            "springbud": "\033[38;2;167;252;0m",
            "springgreen": "\033[38;2;0;255;127m",
            "tan": "\033[38;2;210;180;140m",
            "taupe": "\033[38;2;72;60;50m",
            "teal": "\033[38;2;0;128;128m",
            "turquoise": "\033[38;2;64;224;208m",
            "ultramarine": "\033[38;2;63;0;255m",
            "violet": "\033[38;2;127;0;255m",
            "viridian": "\033[38;2;64;130;109m",
            "white": "\033[38;2;255;255;255m",
            "yellow": "\033[38;2;255;255;0m",
        }
        if self.ostype == "windows":
            self.colors = {
            "": "",
            "reset": "",
            "amaranth": "",
            "amber": "",
            "amethyst": "",
            "apricot": "",
            "aquamarine": "",
            "azure": "",
            "babyblue": "",
            "beige": "",
            "brickred": "",
            "black": "",
            "blue": "",
            "bluegreen": "",
            "blueviolet": "",
            "blush": "",
            "bronze": "",
            "brown": "",
            "burgundy": "",
            "byzantium": "",
            "carmine": "",
            "cerise": "",
            "cerulean": "",
            "champagne": "",
            "chartreusegreen": "",
            "chocolate": "",
            "cobaltblue": "",
            "coffee": "",
            "copper": "",
            "coral": "",
            "crimson": "",
            "cyan": "",
            "desertsand": "",
            "electricblue": "",
            "emerald": "",
            "erin": "",
            "gold": "",
            "gray": "",
            "green": "",
            "harlequin": "",
            "indigo": "",
            "ivory": "",
            "jade": "",
            "junglegreen": "",
            "lavender": "",
            "lemon": "",
            "lilac": "",
            "lime": "",
            "magenta": "",
            "magentarose": "",
            "maroon": "",
            "mauve": "",
            "navyblue": "",
            "ochre": "",
            "olive": "",
            "orange": "",
            "orangered": "",
            "orchid": "",
            "peach": "",
            "pear": "",
            "periwinkle": "",
            "persianblue": "",
            "pink": "",
            "plum": "",
            "prussianblue": "",
            "puce": "",
            "purple": "",
            "raspberry": "",
            "red": "",
            "redviolet": "",
            "rose": "",
            "ruby": "",
            "salmon": "",
            "sangria": "",
            "sapphire": "",
            "scarlet": "",
            "silver": "",
            "slategray": "",
            "springbud": "",
            "springgreen": "",
            "tan": "",
            "taupe": "",
            "teal": "",
            "turquoise": "",
            "ultramarine": "",
            "violet": "",
            "viridian": "",
            "white": "",
            "yellow": "",
        }
        if self.ostype=="windows":
            self.clearcommand="cls"
        screen = []
        for y in range(rows):
            row_list = []
            for x in range(columns):
                if main_color == "random":
                    new_cell = [main_symbol, self.colors[self.randomColor()]]
                else:
                    new_cell = [main_symbol, self.colors[main_color]]
                row_list.append(new_cell)
            screen.append(row_list)
        self.screen = screen

    # $Functions for editing screen$

    # Function for changeing screen size

    def changeScreenSize(self, rows, columns):
        screen = []
        for y in range(rows):
            row_list = []
            for x in range(columns):
                try:
                    new_cell = [self.screen[y][x][0], self.screen[y][x][1]]
                except Exception:
                    if self.maincolor == "random":
                        new_cell = [self.mainsymbol,
                                    self.colors[self.randomColor()]]
                    else:
                        new_cell = [self.mainsymbol,
                                    self.colors[self.maincolor]]
                row_list.append(new_cell)
            screen.append(row_list)
        self.screen = screen
        self.rows = rows
        self.columns = columns

    # Function for changeing symbol by coordinates
    def changeSymbol(self, row, column, symbol=" ", color=""):
        row -= 1
        column -= 1
        self.screen[row][column][0] = symbol
        if color == "random":
            self.screen[row][column][1] = self.colors[self.randomColor()]
        else:
            self.screen[row][column][1] = self.colors[color]

    # Function for removeing symbol by coordinates

    def removeSymbol(self, row, column):
        row -= 1
        column -= 1
        self.screen[row][column][0] = " "

    # Function for changeing symbol color by coordinates
    def changeSymbolColor(self, row, column, color=""):
        row -= 1
        column -= 1
        if color == "random":
            self.screen[row][column][1] = self.colors[self.randomColor()]
        else:
            self.screen[row][column][1] = self.colors[color]

    # Function for changeing symbols by coordinates
    def changeSymbols(self, symbols, symbol=" ", color=""):
        if symbols!=None:
            for s in symbols:
                row = s[0]-1
                column = s[1]-1
                self.screen[row][column][0] = symbol
                if color == "random":
                    self.screen[row][column][1] = self.colors[self.randomColor()]
                else:
                    self.screen[row][column][1] = self.colors[color]

    # Function for removeing symbols by coordinates

    def removeSymbols(self, symbols):
        for s in symbols:
            row = s[0]-1
            column = s[1]-1
            self.screen[row][column][0] = " "

    # Function for changeing symbols colors by coordinates
    def changeSymbolsColors(self, symbols, color=""):
        for s in symbols:
            row = s[0]-1
            column = s[1]-1
            if color == "random":
                self.screen[row][column][1] = self.colors[self.randomColor()]
            else:
                self.screen[row][column][1] = self.colors[color]

    # Function for changeing all symbols in selected row

    def changeRowSymbols(self, row, symbol, color=""):
        row -= 1
        for i in range(len(self.screen[row])):
            self.screen[row][i][0] = symbol
            if color == "random":
                self.screen[row][i][1] = self.colors[self.randomColor()]
            else:
                self.screen[row][i][1] = self.colors[color]

    # Function for changeing all symbols colors in selected row

    def changeRowColor(self, row, color=""):
        row -= 1
        for i in range(len(self.screen[row])):
            if color == "random":
                self.screen[row][i][1] = self.colors[self.randomColor()]
            else:
                self.screen[row][i][1] = self.colors[color]

    # Function for changeing all symbols in selected column
    def changeColumnSymbols(self, column, symbol, color=""):
        column -= 1
        for i in range(self.rows):
            self.screen[i][column][0] = symbol
            if color == "random":
                self.screen[i][column][1] = self.colors[self.randomColor()]
            else:
                self.screen[i][column][1] = self.colors[color]

    # Function for changeing all symbols colors in selected column

    def changeColumnColor(self, column, color=""):
        column -= 1
        for i in range(self.rows):
            if color == "random":
                self.screen[i][column][1] = self.colors[self.randomColor()]
            else:
                self.screen[i][column][1] = self.colors[color]

    # Function for drawing border (or makeing border)
    def changeBorder(self, border_left=0, border_right=0, border_top=0, border_bottom=0, border=-1, symbol="O", color=""):
        if border != -1:
            border_top = border
            border_bottom = border
            border_left = border
            border_right = border
        for i in range(border_top+1):
            self.changeRowSymbols(i, symbol, color)
        for i in range(border_bottom):
            self.changeRowSymbols(self.rows-i, symbol, color)
        for i in range(border_left+1):
            self.changeColumnSymbols(i, symbol, color)
        for i in range(border_right):
            self.changeColumnSymbols(self.columns-i, symbol, color)

    # Function for reseting screen (changeing all symbols to main symbol)
    def resetScreen(self, main_symbol="--", main_color="--"):
        if main_symbol == "--":
            main_symbol = self.mainsymbol
        if main_color == "--":
            main_color = self.maincolor
        for y in range(self.rows):
            for x in range(self.columns):
                self.screen[y][x][0] = main_symbol
                if main_color == "random":
                    self.screen[y][x][1] = self.colors[self.randomColor()]
                else:
                    self.screen[y][x][1] = self.colors[main_color]

    # Function for changeing all symbols to given symbol

    def changeScreenSymbols(self, main_symbol="--"):
        if main_symbol == "--":
            main_symbol = self.mainsymbol
        for y in range(self.rows):
            for x in range(self.columns):
                self.screen[y][x][0] = main_symbol

    # Function for changeing all symbols colors to given color
    def changeScreenColor(self, main_color="--"):
        if main_color == "--":
            main_color = self.maincolor
        for y in range(self.rows):
            for x in range(self.columns):
                if main_color == "random":
                    self.screen[y][x][1] = self.colors[self.randomColor()]
                else:
                    self.screen[y][x][1] = self.colors[main_color]

    # Function for replaceing symbol
    def replaceSymbol(self, symbol, newsymbol):
        for y in range(self.rows):
            for x in range(self.columns):
                if self.screen[y][x][0] == symbol:
                    self.screen[y][x][0] = newsymbol

    # Function for drawing simple string text
    def writeString(self, string, row=1, column=1, color="", auto_background=False):
        row -= 1
        column -= 1
        for i in range(len(string)):
            if string[i] == " " and auto_background == True:
                self.screen[row][column+i][0] = self.mainsymbol
                self.screen[row][column+i][1] = self.colors[self.maincolor]
                continue
            self.screen[row][column+i][0] = string[i]
            self.screen[row][column+i][1] = self.colors[color]

    # Function for drawing simple string text
    def writeText(self, text, row=1, column=1, color="", auto_background=False):
        row -= 1
        column -= 1
        d = 0
        for i in range(len(text)):
            if text[i] == "\n":
                row += 1
                d = 0
                continue
            if text[i] == "\t":
                column += 4
                continue
            if text[i] == " " and auto_background == True:
                self.screen[row][column+d][0] = self.mainsymbol
                if self.maincolor == "random":
                    self.screen[row][column +
                                     d][1] = self.colors[self.randomColor()]
                else:
                    self.screen[row][column+d][1] = self.colors[self.maincolor]
                d += 1
                continue
            self.screen[row][column+d][0] = text[i]
            if color == "random":
                self.screen[row][column+d][1] = self.colors[self.randomColor()]
            else:
                self.screen[row][column+d][1] = self.colors[color]
            d += 1

    # Function for drawing folder icon
    def drawFolderIcon(self, row=1, column=1, name="", color="white"):
        text = f""".----.______\n|          |\n|    ___________\n|   /          /\n|  /          /\n| /          /\n|/__________/\n\n{name}"""
        self.writeText(text, row, column, color)

    # Function for drawing file icon
    def drawFileIcon(self, row=1, column=1, name="", color="white"):
        text = f""".---------.\n| --------|\\\ \n| --------- |\n| --------- |\n| --------- |\n| --------- |\n| --------- |\n'-----------'\n\n{name}"""
        self.writeText(text, row, column, color)

    # Function for drawing recycle bin icon
    def drawRecycleBinIcon(self, row=1, column=1, name="", color="white"):
        text = f""" ___/-\___\n|---------|\n | | | | |\n | | | | |\n | | | | |\n | | | | |\n |_______|\n\n {name}"""
        self.writeText(text, row, column, color)

    # Function for drawing square
    def drawSquare(self, row, column, size, symbol="0", color="red"):
        row -= 1
        column -= 1
        for y in range(row, row+size):
            for x in range(column, column+size*2):
                self.screen[y][x][0] = symbol
                if color == "random":
                    self.screen[y][x][1] = self.colors[self.randomColor]
                else:
                    self.screen[y][x][1] = self.colors[color]

    # Function for drawing rectangle
    def drawRectangle(self, row, column, height, width, symbol="0", color="red"):
        row -= 1
        column -= 1
        for y in range(row, row+height):
            for x in range(column, column+width):
                self.screen[y][x][0] = symbol
                if color == "random":
                    self.screen[y][x][1] = self.colors[self.randomColor]
                else:
                    self.screen[y][x][1] = self.colors[color]

    # Function for drawing pyramid
    def drawPyramid(self, row, column, size, symbol="*", color="red"):
        size += 1
        row = row - 2
        column = column - 1
        d = 0
        count = 0
        for i in range(size):
            for a in range(-count, count):
                self.screen[row+d][column+a][0] = symbol
                if color == "random":
                    self.screen[row+d][column +
                                       a][1] = self.colors[self.randomColor()]
                else:
                    self.screen[row+d][column+a][1] = self.colors[color]
            d += 1
            count += 1

    # Function for drawing button
    def drawButton(self, row=2, column=2, height=3, width=16, text="Button", color="", border_symbol="█"):
        button_text = ""
        for i in range(math.floor((height-1)/2)):
            button_text += border_symbol*width + "\n"
        button_text += math.floor((width-len(text))/2)*border_symbol+text+(
            width-len(text)-math.floor((width-len(text))/2))*border_symbol+"\n"
        for i in range(height-math.floor((height-1)/2)-1):
            button_text += border_symbol*width + "\n"
        self.writeText(button_text, row, column, color)

    # Function for drawing chess board

    def drawChessBoard(self, row=1, column=1, height=10, width=10, color1="blue", symbol1="=", color2="red", symbol2=" "):
        row -= 1
        column -= 1
        for y in range(height):
            for x in range(width):
                if y % 2 == 0:
                    if x % 2 == 0:
                        self.screen[row+y][column+x][0] = symbol1
                        self.screen[row+y][column+x][1] = self.colors[color1]
                    else:
                        self.screen[row+y][column+x][0] = symbol2
                        self.screen[row+y][column+x][1] = self.colors[color2]
                else:
                    if x % 2 == 0:
                        self.screen[row+y][column+x][0] = symbol2
                        self.screen[row+y][column+x][1] = self.colors[color2]
                    else:
                        self.screen[row+y][column+x][0] = symbol1
                        self.screen[row+y][column+x][1] = self.colors[color1]

    # Function for opening,reading and displaying file on screen
    def openFile(self, file, row=1, column=1, color="white", auto_background=False):
        with open(file, "r") as f:
            text = f.read()
        self.writeText(text, row, column, color,
                       auto_background=auto_background)

    # Function for drawing line with between two coordinates
    def drawLine(self, x1, y1, x2, y2, symbol="#", color="red"):
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        distX = abs(x1-x2)
        distY = abs(y1-y2)
        rpc = distY/distX
        posX = 1
        posY = 1
        if x2 < x1:
            posX = -1
        if y2 < y1:
            posY = -1
        for x in range(distX+1):
            self.screen[y1+math.floor(x*rpc*posY)][x1+posX*x][0] = symbol
            if color == "random":
                self.screen[y1+math.floor(x*rpc*posY)][x1 +
                                                       posX*x][1] = self.colors[self.randomColor()]
            else:
                self.screen[y1+math.floor(x*rpc*posY)
                            ][x1+posX*x][1] = self.colors[color]

    # Function for drawing horizontal line
    def drawHorizontalLine(self, x, y, length, symbol="#", color="red"):
        x -= 1
        y -= 1
        position = 1
        if length < 0:
            position = -1
        for i in range(abs(length)):
            self.screen[y][x+i*position][0] = symbol
            if color == "random":
                self.screen[y][x+i *
                               position][1] = self.colors[self.randomColor()]
            else:
                self.screen[y][x+i*position][1] = self.colors[color]

    # Function for drawing vertical line
    def drawVerticalLine(self, x, y, length, symbol="#", color="red"):
        x -= 1
        y -= 1
        position = 1
        if length < 0:
            position = -1
        for i in range(abs(length)):
            self.screen[y+i*position][x][0] = symbol
            if color == "random":
                self.screen[y+i*position][x][1] = self.colors[self.randomColor()]
            else:
                self.screen[y+i*position][x][1] = self.colors[color]

    # Function for drawing checkbox
    def drawCheckbox(self, values, row=1, column=1, color="red", style="number"):
        text = ""
        if style == "number":
            for i in range(len(values)):
                text += "{}.{}\n".format(i+1, values[i])
        elif style == "dot":
            for i in range(len(values)):
                text += "● {}\n".format(values[i])
        else:
            raise "Style Error: style must be \"number\" or \"dot\""
        self.writeText(text, row, column, color)

    # Function for drawing notepad
    def drawNotepad(self, row=1, column=1, width=50, height=20, text="", title="", border_symbol="█", color="green", auto_background=False):
        if height <= 4:
            raise "Notepad height must be bigger then 4"
        if width < len(title)+2:
            raise "Notepad width must be bigger then title length plus 2 borders"
        notepad_text = ""
        notepad_text += border_symbol*width+"\n"
        notepad_text += border_symbol * \
            math.floor(width/8) + title+border_symbol * \
            (width-math.floor(width/8)-len(title))+"\n"
        notepad_text += border_symbol*width+"\n"
        linetext = ""
        linecount = 4
        for s in range(len(text)):
            if linecount >= height:
                break
            if text[s] == "\n":
                linecount += 1
                notepad_text += border_symbol+linetext + \
                    (width-len(linetext)-2)*" " + border_symbol+"\n"
                linetext = ""
                continue
            if text[s] == "\t":
                continue
            elif len(linetext) >= (width-2):
                linecount += 1
                notepad_text += border_symbol+linetext+border_symbol+"\n"
                linetext = ""
            linetext += text[s]
        notepad_text += border_symbol+linetext + \
            (width-len(linetext)-2)*" "+border_symbol+"\n"
        for i in range(1, height-linecount):
            notepad_text += border_symbol+(width-2)*" " + border_symbol+"\n"
        notepad_text += border_symbol*width+"\n"
        self.writeText(notepad_text, row, column, color,
                       auto_background=auto_background)

    # Function for displaying file on notepa
    def openFileOnNotepad(self, file, row=1, column=1, width=30, height=10, title="--", color="yellow", border_symbol="█", auto_background=False):
        if title == "--":
            title = file
        file_text = ""
        with open(file, "r") as f:
            file_text = f.read()
        self.drawNotepad(row, column, width, height, file_text, title,
                         border_symbol, color, auto_background=auto_background)

    # $Functions for getting some information about screen$

    # function for getting information from matrix

    def getMatrix(self):
        return self.screen

    # Function for getting screen as text
    def getScreen(self):
        text = ""
        for y in self.screen:
            for x in y:
                text += x[0]
            text += "\n"
        return text

    # Function for getting symbol by coordinates
    def getSymbol(self, row, column):
        row -= 1
        column -= 1
        return self.screen[row][column][0]

    # Function for getting symbol all neighbours
    def getSymbolNeighbours(self, row, column):
        """
            Hello Apeeer
        """
        list_of_key = list(self.colors.keys())
        list_of_values = list(self.colors.values())

        def findInDict(color):
            newColor = list_of_key[list_of_values.index(color)]
            return newColor

        def oneNeighbour(newR, newC, rows=self.rows, columns=self.columns):
            if newR >= 0 and newR < self.rows and newC >= 0 and newC < self.columns:
                newN = [newR+1, newC+1, self.screen[newR][newC]
                        [0], findInDict(self.screen[newR][newC][1])]
                return newN
        row -= 1
        column -= 1
        returnList = []
        if oneNeighbour(row-1, column-1) != None:
            returnList.append(oneNeighbour(row-1, column-1))
        if oneNeighbour(row-1, column) != None:
            returnList.append(oneNeighbour(row-1, column))
        if oneNeighbour(row-1, column+1) != None:
            returnList.append(oneNeighbour(row-1, column+1))
        if oneNeighbour(row, column-1) != None:
            returnList.append(oneNeighbour(row, column-1))
        if oneNeighbour(row, column+1) != None:
            returnList.append(oneNeighbour(row, column+1))
        if oneNeighbour(row+1, column-1) != None:
            returnList.append(oneNeighbour(row+1, column-1))
        if oneNeighbour(row+1, column) != None:
            returnList.append(oneNeighbour(row+1, column))
        if oneNeighbour(row+1, column+1) != None:
            returnList.append(oneNeighbour(row+1, column+1))
        return returnList

    # Function for getting symbol neighbours which symbol is given symbol
    def getSymbolNeighboursWithSymbol(self, row, column, searchsymbol):
        list_of_key = list(self.colors.keys())
        list_of_values = list(self.colors.values())

        def findInDict(color):
            newColor = list_of_key[list_of_values.index(color)]
            return newColor

        def oneNeighbour(newR, newC, rows=self.rows, columns=self.columns):
            if newR >= 0 and newR < self.rows and newC >= 0 and newC < self.columns and self.screen[newR][newC][0] == searchsymbol:
                newN = [newR+1, newC+1, self.screen[newR][newC]
                        [0], findInDict(self.screen[newR][newC][1])]
                return newN
        row -= 1
        column -= 1
        returnList = []
        if oneNeighbour(row-1, column-1) != None:
            returnList.append(oneNeighbour(row-1, column-1))
        if oneNeighbour(row-1, column) != None:
            returnList.append(oneNeighbour(row-1, column))
        if oneNeighbour(row-1, column+1) != None:
            returnList.append(oneNeighbour(row-1, column+1))
        if oneNeighbour(row, column-1) != None:
            returnList.append(oneNeighbour(row, column-1))
        if oneNeighbour(row, column+1) != None:
            returnList.append(oneNeighbour(row, column+1))
        if oneNeighbour(row+1, column-1) != None:
            returnList.append(oneNeighbour(row+1, column-1))
        if oneNeighbour(row+1, column) != None:
            returnList.append(oneNeighbour(row+1, column))
        if oneNeighbour(row+1, column+1) != None:
            returnList.append(oneNeighbour(row+1, column+1))

        return returnList

    # Function for getting symbol neighbours where color is given color
    def getSymbolNeighboursWithColor(self, row, column, searchcolor):
        list_of_key = list(self.colors.keys())
        list_of_values = list(self.colors.values())

        def findInDict(color):
            newColor = list_of_key[list_of_values.index(color)]
            return newColor

        def oneNeighbour(newR, newC, rows=self.rows, columns=self.columns):
            if newR >= 0 and newR < self.rows and newC >= 0 and newC < self.columns and findInDict(self.screen[newR][newC][1]) == searchcolor:
                newN = [newR+1, newC+1, self.screen[newR][newC]
                        [0], findInDict(self.screen[newR][newC][1])]
                return newN
        row -= 1
        column -= 1
        returnList = []
        if oneNeighbour(row-1, column-1) != None:
            returnList.append(oneNeighbour(row-1, column-1))
        if oneNeighbour(row-1, column) != None:
            returnList.append(oneNeighbour(row-1, column))
        if oneNeighbour(row-1, column+1) != None:
            returnList.append(oneNeighbour(row-1, column+1))
        if oneNeighbour(row, column-1) != None:
            returnList.append(oneNeighbour(row, column-1))
        if oneNeighbour(row, column+1) != None:
            returnList.append(oneNeighbour(row, column+1))
        if oneNeighbour(row+1, column-1) != None:
            returnList.append(oneNeighbour(row+1, column-1))
        if oneNeighbour(row+1, column) != None:
            returnList.append(oneNeighbour(row+1, column))
        if oneNeighbour(row+1, column+1) != None:
            returnList.append(oneNeighbour(row+1, column+1))

        return returnList

    # Function for getting neighbours of many symbols
    def getSymbolsNeighbours(self,symbols):
        returnList = []
        for s in symbols:
            sn=self.getSymbolNeighbours(s[0],s[1])
            for i in sn:
                append = True
                for j in returnList:
                    if i[0]==j[0] and i[1]==j[1]:
                        append=False
                for j in symbols:
                    if i[0]==j[0] and i[1]==j[1]:
                        append=False
                if append:
                    returnList.append(i)

    # Function for getting neighbours of many symbols with selected symbol
    def getSymbolsNeighboursWithSymbol(self,symbols,searchsymbol):
        returnList = []
        for s in symbols:
            sn=self.getSymbolNeighboursWithSymbol(s[0],s[1],searchsymbol)
            for i in sn:
                append = True
                for j in returnList:
                    if i[0]==j[0] and i[1]==j[1]:
                        append=False
                for j in symbols:
                    if i[0]==j[0] and i[1]==j[1]:
                        append=False
                if append:
                    returnList.append(i)

    # Function for getting neighbours of many symbols with selected color
    def getSymbolsNeighboursWithColor(self,symbols,searchcolor):
        returnList = []
        for s in symbols:
            sn=self.getSymbolNeighboursWithColor(s[0],s[1],searchcolor)
            for i in sn:
                append = True
                for j in returnList:
                    if i[0]==j[0] and i[1]==j[1]:
                        append=False
                for j in symbols:
                    if i[0]==j[0] and i[1]==j[1]:
                        append=False
                if append:
                    returnList.append(i)


        
        return returnList

    # Function for finding symbol in screen
    def findSymbol(self, symbol):
        symbols = []
        for y in range(self.rows):
            for x in range(self.columns):
                if self.screen[y][x][0] == symbol:
                    symbols.append([y+1, x+1, self.screen[y][x]
                                   [0], self.screen[y][x][1]])
        return symbols

    # Function for finding symbols by color
    def findColor(self, color):
        symbols = []
        for y in range(self.rows):
            for x in range(self.columns):
                if self.screen[y][x][1] == self.colors[color]:
                    symbols.append([y+1, x+1, self.screen[y][x]
                                   [0], self.screen[y][x][1]])
        return symbols

    # Function for drawing Model
    def drawModel(self, model):
        self.writeText(model.model, model.row, model.column,
                       model.color, model.auto_background)

    # Function for saveing screen as file
    def saveScreenAsFile(self, file_name="screen1.txt"):
        with open(file_name, "w") as f:
            f.write(self.getScreen())

    # Function for generateing random color (but it is just for using inside class)
    def randomColor(self):
        return random.choice(list(self.colors.items()))[0]

    # $General functions$

    # Function for update

    def update(self):
        os.system(self.clearcommand)
        for y in self.screen:
            for x in y:
                print(x[1]+x[0], end="")
            print()

    # Function for auto update
    def autoUpdate(self, wait_time=0, count="infinite"):
        if count == "infinite":
            count = 1000**1000

        def mainUpdate():
            for i in range(count):
                if self.auto_update == "pause":
                    continue
                if self.auto_update == False:
                    break
                self.update()
                time.sleep(wait_time)
        x = threading.Thread(target=mainUpdate)
        x.start()
    
    # Function for pausing auto update for given time
    def pauseAutoUpdate(self,seconds=1):
        self.auto_update = "pause"
        time.sleep(seconds)
        self.auto_update = True

    # Function for stoping auto update
    def stopAutoUpdate(self):
        self.auto_update = False

