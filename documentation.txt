|||||||||||||||||||||||||||||||||||||||||||||||||||| Class Screen ||||||||||||||||||||||||||||||||||||||||||||||||||||


-------------------------------------------------------------------------------------
$$$ Screen $$$

screen = Screen()     // You must make object of Screen class for makeing "Screen" (Saying screen I mean part of terminal for drawing)

Arguments:
	rows = 10              # Count of rows
	columns = 20           # Count of columns
	main_symbol = " "      # Main symbol which will be in all screen
	main_color = ""        # Main color which will be used for every symbol
-------------------------------------------------------------------------------------













-------------------------------------------------------------------------------------
$$$ Get Matrix $$$

screen.getMatrix()    // You will get screen as Matrix

[NO ARGUMENTS]
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Change Symbol $$$

screen.changeSymbol(3,4,"A") // You will change symbol in 3 row ant 4 column to A

Arguments:
	row             # Coordinate row
	column          # Coordinate column
	symbol = " "    # New symbol for changeing
	color=""        # Color of symbol
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Remove Symbol $$$

screen.removeSymbol(3,4) // You will change symbol in 3 row ant 4 column to space (as remoc\veing)

Arguments:
	row             # Coordinate row
	column          # Coordinate column
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Change Symbol Color $$$

screen.changeSymbolColor(3,4,"red") // You will change symbol color in 3 row ant 4 column to red

Arguments:
	row             # Coordinate row
	column          # Coordinate column
	color=""        # Color of symbol
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Reset Screen $$$

screen.resetScreen() // You will reset all symbols to main_symbol and all colors to main_color
screen.resetScreen("=","green") // You will you will change all symbols to = with color green

Arguments:
	main_symbol=self.mainsymbol             # All symbols will be main_symbol
	main_color =self.maincolor     	        # All colors will be color of main_color
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Screen Symbols $$$

screen.changeScreenSymbols() // You will change all symbols to given symbol

Arguments:
	main_symbol=self.mainsymbol             # All symbols will be main_symbol
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Change Screen Size $$$

screen.changeScreenSize(50,50) // You will change screen size to 50 rows and 50 columns

Arguments:
	rows            # New rows count
	columns         # New columns count
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Screen Color $$$

screen.changeScreenColor() // You will change all symbols colors to given color

Arguments:
	main_color=self.maincolor           # All symbols colors will be main_color
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Change Symbols $$$

screen.changeSymbols([[2,3],[3,3],[1,4]],"A") // You will change symbols in coordinates in massive

Arguments:
	symbols         # Coordinates for changeing
	symbol = " "    # New symbol for changeing
	color=""        # Color of symbols
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Remove Symbols $$$

screen.removeSymbols([[2,3],[3,3],[1,4]]) // You will change symbols in coordinates in massive to space (as removeing)

Arguments:
	symbols         # Coordinates for changeing
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Symbols Colors$$$

screen.changeSymbolsColors([[2,3],[3,3],[1,4]],"red") // You will change symbols colors in coordinates to red

Arguments:
	symbols         # Coordinates for changeing
	color=""        # New color of symbols
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Change Row Symbol $$$

screen.changeRowSymbols(3,"X")   // Will change all symbols in 3 row to "X"

Arguments:
	row         # Row in screen
	symbol      # New symbol to change
	color=""    # Color of row symbols
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Row Color $$$

screen.changeRowColor(3,"red")   // Will change all symbols colors in 3-th row to "red"

Arguments:
	row         # Row to change colors
	color=""    # Color of row symbols
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Column Color $$$

screen.changeColumnColor(3,"red")   // Will change all symbols colors in 3-th column to "red"

Arguments:
	column      # Column to change colors
	color=""    # Color of row symbols
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Change Column Symbol $$$

screen.changeColumnSymbols(3,"X")   // Will change all symbols in 3 column to "X"

Arguments:
	Column      # Column in screen
	symbol      # New symbol to change
	color=""    # Color of row symbols
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Draw Square $$$

screen.drawSquare(row=4,column=4,size=7,symbol="@",color="red")   // Will draw square in 4th row and in 4th column with size 7 with symbol @ and with red color             
Arguments:
        row           # Start row
		column        # Start colum
		size          # Size of square
        symbol        # Symbol for drawing
        color="red"   # Color of square
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Draw Pyramid $$$

screen.drawPyramide(row=4,column=4,size=7,symbol="@",color="red")   // Will draw pyramide in 4th row and in 7th column with size 7 with symbol @ and with red color
Arguments:
    row           # Start row
    column        # Start column
    size          # Size of square
    symbol        # Symbol for drawing
    color="red"   # Color of square
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Draw Chess Board $$$

screen.drawChessBoard(row=5,column=5,symbol1="+",color1="green",symbol2="=",color2="blue",height=10,width=20)
Arguments:
    row            # Start row
    column         # Start column
    height         # Height of board
    width          # Width of board
    symbol1        # First symbol
    color1         # First symbol color
	symbol2        # Second symbol
    color2         # Second symbol color
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Find Symbol $$$

screen.findSymbol(symbol="-")   // Will find all symbols which is "-" and will return it
Arguments:
    symbol        # Symbol for searching
Return:
	list of coordinates
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Find Color $$$

screen.findColor(color="red")   // Will find all symbols which color is red and will return it
Arguments:
    color        # Color for searching
Return:
	list of coordinates
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Draw Rectangle $$$

screen.drawRectangle(row=4,column=4,width=7,height=19,symbol="@",color="red")   // Will draw rectangle in 4th row and in 4th column with width 7 and height 19 with symbol @ and with red color
Arguments:
    row           # Start row
	column        # Start colum
	width         # Width of rectangle
	height        # Height of rectangle
	symbol        # Symbol for drawing
    color="red"   # Color of rectangle
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Open File $$$

screen.openFile(file="art.txt",row=4,column=4,color="red",auto_background=False)   // Will open and diplay file "art.txt" in our coordinates with red color
Arguments:
	file          # File to read 
    row           # Start row
    column        # Start column
	symbol        # Symbol for drawing
    color="red"   # Color of text
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Draw Line $$$

screen.drawLine(2,2,7,17,'B','red')   // Will draw line from 2,2 to 7,7
Arguments:
	x1           # X to start 
    y1           # Y to start
    x2           # X to finish
    y2           # Y to finish
	symbol       # Symbol for drawing line
    color="red"  # Color of line
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Draw Horizontal Line $$$

screen.drawHorizontalLine(2,2,7,'B','red')   // Will draw horizontal line from 2,2 with length 7
Arguments:
	x               # X to start 
    y               # Y to start
	length          # Length of line
	symbol="#"       # Symbol for drawing horizontal line
    color="red"     # Color of line
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Draw Vertical Line $$$

screen.drawVerticalLine(2,2,7,'B','red')   // Will draw vertical line from 2,2 with length 7
Arguments:
	x               # X to start 
    y               # Y to start
	length          # Length of line
	symbol="#"       # Symbol for drawing vertical line
    color="red"     # Color of line
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Draw Checkbox $$$

screen.drawCheckbox(["Cheese","Vine","Potato",'blue'],9,9,'blue',style='dot')   // Will draw checkbox in coordinates 9,9 with blue color eith style dot,style can be number too
Arguments:
	values          # List with checkbox values
	x               # X to draw
    y               # Y to draw
    color="red"     # Color of line
    style="number" ("dot")     # Style of checkbox
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Change Border $$$

screen.changeBorder(border=3,symbol="0",color="green")   // Will make border (width is 3) with color green
screen.changeBorder(border_left=2,border_top=1,border_bottom=4,border_right=3,symbol="0",color="green")   // Will make border with selected border parameters with color green

Arguments:
	symbol            # Border symbol
	border            # Will make all border sizes the same
	border_bottom     # Bottom border size
	border_left       # Left border size
	border_right      # Right border size
	border_top        # Top border size
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Write String $$$

screen.writeString(string="I Love Python",row=10,column=10,color="red")   // Will write one line string in 10,10 coordinates in red color

Arguments:
	string                   # one line text to display
	row=1                    # Row coordinate to display text
	column=1                 # Column coordinate to display text
	color=""                 # Color of row symbols
	auto_background          # spaces will be main symbol
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Write Text $$$

text_example = """
This is two
line text
"""
screen.writeText(text=text_example,row=10,column=10,color="red")   // Will write long text in 10,10 coordinates in red color

Arguments:
	text                     # multiline text to display
	row=1                    # Row coordinate to display text
	column=1                 # Column coordinate to display text
	color=""                 # Color of row symbols
	auto_background          # spaces will be main symbol
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Get Screen $$$

screen.getScreen()   // You will get screen as text
-------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------
$$$ Save Screen As File $$$

model.saveScreenAsFile("screen1.txt")     // You will save screen as screen1.txt

Arguments:
	file_name = "screen1.txt"  # File name to save

-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Get Symbol $$$

screen.getSymbol(row,column)         // Get symbol by coordinates

Arguments:
	row     # Row of symbol
	column  # Column of symbol
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Get Symbol Neighbours$$$

screen.getSymbolNeighbours(row,column)         // Get symbol neighbours coordinates,symbols and colors

Arguments:
	row     # Row of symbol
	column  # Column of symbol
Returns:
	neighbour # array Ex. [[2,3,"=","red"],[3,3,"-","green"]]
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Get Symbol Neighbours With Symbol $$$

screen.getSymbolNeighboursWithSymbol(row,column,searchsymbol)         // Get symbol neighbours coordinates,symbols and colors which symbol is given symbol

Arguments:
	row            # Row of symbol
	column         # Column of symbol
	searchsymbol   # Symbol to search in neighbours
Returns:
	neighbour # array Ex. [[2,3,"=",""],[3,3,"-","green"]]
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Get Symbol Neighbours With Color $$$

screen.getSymbolNeighboursWithColor(row,column,searchcolor)         // Get symbol neighbours coordinates,symbols and colors which color is given color

Arguments:
	row            # Row of symbol
	column         # Column of symbol
	searchcolor    # Color to search in neighbours
Returns:
	neighbour # array Ex. [[2,3,"=",""],[3,3,"-","green"]]
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Get Symbols Neighbours $$$

screen.getSymbolsNeighbours([[20,20],[21,20],[27,21],[27,27],[30,30],[27,26],[27,25],[27,24],[27,23]])         // Get symbols neighbours coordinates,symbols and colors

Arguments:
	symbols   # List of symbols (first row, second column)
Returns:
	neighbour # array Ex. [[2,3,"=","red"],[3,3,"-","green"]]
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Get Symbols Neighbours With Symbol $$$

screen.getSymbolsNeighboursWithSymbol([[20,20],[21,20],[27,21],[27,27],[30,30],[27,26],[27,25],[27,24],[27,23]])         // Get symbols neighbours coordinates,symbols and colors which symbol is our given symbol

Arguments:
	symbols         # List of symbols (first row, second column)
	searchsymbol    # Symbol to search in neighbours
Returns:
	neighbour # array Ex. [[2,3,"=","red"],[3,3,"-","green"]]
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Get Symbols Neighbours With Color $$$

screen.getSymbolsNeighboursWithColor([[20,20],[21,20],[27,21],[27,27],[30,30],[27,26],[27,25],[27,24],[27,23]])         // Get symbols neighbours coordinates,symbols and colors which symbol is our given color

Arguments:
	symbols        # List of symbols (first row, second column)
	searchcolor    # Color to search in neighbours
Returns:
	neighbour # array Ex. [[2,3,"=","red"],[3,3,"-","green"]]
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Replace Symbol $$$

screen.replaceSymbol("-","0")         // Will replace "-" to "0"

Arguments:
	symbol     # Symbol to replace
	newsymbol  # New symbol
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Draw Folder Icon $$$

drawFolderIcon(row=1,column=1,name="Documents",color="red")         // Will draw desktop folder icon on 1 row and 1 column with color red

Arguments:
	row            # Row to draw folder icon
	column         # Column to draw folder icon
	name           # Name under folder
	color          # Color of folder
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Draw File Icon $$$

drawFileIcon(row=1,column=1,name="simple_file.txt",color="red")         // Will draw desktop file icon on 1 row and 1 column with color red

Arguments:
	row            # Row to draw file icon
	column         # Column to draw file icon
	name           # Name under file
	color          # Color of file
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Draw Recycle Bin Icon $$$

drawRecycleBinIcon(row=1,column=1,name="simple_file.txt",color="red")         // Will draw desktop recycle bin icon on 1 row and 1 column with color red

Arguments:
	row            # Row to draw recycle bin icon
	column         # Column to draw recycle bin icon
	name           # Name under recycle bin
	color          # Color of recycle bin
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Draw Notepad $$$

drawNotepad(row=1,column=1,width=50,height=20,text="",title="",border_symbol="█",color="green",auto_background=False)     // Function for drawing notepad with this parameters
Arguments:
	row=1                        # Row of symbol
	column=1                     # Column of symbol
	width=50                     # Width of notepad
	height = 20                  # Height of notepad
	text=""                      # Text of notepad
	title=""                     # Title of notepad
	border_symbol="█"            # Symbol of border
	color="yellow"               # Color of notepad
	auto_background=False        # If it is True all spaces will be replaced to main symbol
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Open File On Notepad $$$

openFileOnNotepad(file="file_to_open.txt",row=1,column=1,width=30,height=10,title="File",color="yellow",border_symbol="█",auto_background=False)
Arguments:
	file                         # File to open
	row=1                        # Row of symbol
	column=1                     # Column of symbol
	width=50                     # Width of notepad
	height = 10                  # Height of notepad
	title=""                     # Title of notepad
	border_symbol="█"            # Symbol of border
	color="yellow"               # Color of notepad
	auto_background=False        # If it is True all spaces will be replaced to main symbol
-------------------------------------------------------------------------------------







-------------------------------------------------------------------------------------
$$$ Update $$$

screen.update()  // For drawing it in screen

[NO ARGUMENTS] 
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Auto Update $$$

screen.autoUpdate(wait_time=0.1,count=100)  // For auto updateing screen

Arguments:
	count (default is "infinite" for infinite update)         # Count for updateing
	wait_time                                                 # Time for waiting between updates
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Stop Auto Update $$$

screen.stopAutoUpdate()  // For stoping auto update

[NO ARGUMENTS] 
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Pause Auto Update $$$

screen.pauseAutoUpdate(seconds=2)  // For pausing auto update for 2 seconds

Arguments:
	seconds=1    # Seconds for pausing auto update

-------------------------------------------------------------------------------------
































|||||||||||||||||||||||||||||||||||||||||||||||||||| Class Model ||||||||||||||||||||||||||||||||||||||||||||||||||||

-------------------------------------------------------------------------------------
$$$ Model $$$

model = Model()     // You will make new model and then you can display it on your screen

Arguments:
	id                          # Id of model
	row=1                       # Row of model
	column=1                    # Column of model
	color = ""                  # Color of model
	auto_background = False     # Will replace all symbols to main symbol
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Print Model $$$

model.printModel()     // You will just print model as text

[NO ARGUMENTS]
-------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------
$$$ Save Model As File $$$

model.saveModelAsFile("model1.txt")     // You will save model as file in your pc

Arguments:
	file_name = "model1.txt"  # File name to save

-------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------
$$$ Change Color $$$

model.changeColor()     // You will change model color

Arguments:
	color     # New color of model
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Change Row $$$

model.changeRow()     // You will change model row

Arguments:
	row     # New row of model
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Column $$$

model.changeColumn()     // You will change model column

Arguments:
	column     # New column of model
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Coordinates $$$

model.changeCoordinates()     // You will change model coordinates

Arguments:
	row     # New row of model
	column     # New column of model
-------------------------------------------------------------------------------------

































|||||||||||||||||||||||||||||||||||||||||||||||||||| Class Object ||||||||||||||||||||||||||||||||||||||||||||||||||||


-------------------------------------------------------------------------------------
$$$ Object $$$

object1 = Object()     // You will make new object with arguments screen (as parent screen) and new model

Arguments:
	screen                          # Parent screen
	model                          # New model for object
-------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------
$$$ Show Object $$$

object1.showObject()     // You will display object on screen

[NO ARGUMENTS]
-------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------
$$$ Change Color $$$

object1.changeColor()     // You will change object color

Arguments:
	color          # new color
-------------------------------------------------------------------------------------







-------------------------------------------------------------------------------------
$$$ Move Up $$$

object1.moveUp(steps=1)     // You will move object up with 1 step

Arguments:
	steps=1       # Steps count
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Move Down $$$

object1.moveDown(steps=1)     // You will move object down with 1 step

Arguments:
	steps=1       # Steps count
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Move Left $$$

object1.moveLeft(steps=1)     // You will move object left with 1 step

Arguments:
	steps=1       # Steps count
-------------------------------------------------------------------------------------







-------------------------------------------------------------------------------------
$$$ Move Right $$$

object1.moveRight(steps=1)     // You will move object right with 1 step

Arguments:
	steps=1       # Steps count
-------------------------------------------------------------------------------------






-------------------------------------------------------------------------------------
$$$ Change Row $$$

object1.changeRow()     // You will change object row

Arguments:
	row     # New row of object
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Column $$$

object1.changeColumn()     // You will change object column

Arguments:
	column     # New column of object
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Change Coordinates $$$

object1.changeCoordinates()     // You will change object coordinates

Arguments:
	row     # New row of object
	column     # New column of object
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Vertical Sinus Animation $$$

object1.verticalSinusAnimation()     // You will move object vertical with sinus graph

Arguments:
	speed                # Speed of update
	count="infinite"     # Count to update
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Horizontal Sinus Animation $$$

object1.horizontalSinusAnimation()     // You will move object horizontal with sinus graph

Arguments:
	speed                # Speed of update
	count="infinite"     # Count to update
-------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------
$$$ Vertical Move Animation $$$

object1.verticalMoveAnimation()     // You will move object vertical with same speed graph

Arguments:
	speed                # Speed of update
	count="infinite"     # Count to update
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Horizontal Move Animation $$$

object1.horizontalMoveAnimation()     // You will move object horizontal with same speed graph

Arguments:
	speed                # Speed of update
	count="infinite"     # Count to update
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
$$$ Stop Vertical Animation $$$

object1.stopVerticalAnimation()     // You will stop vertical animation for selected object

[NO ARGUMENTS]
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Stop Horizontal Animation $$$

object1.stopHorizontalAnimation()     // You will stop horizontal animation for selected object

[NO ARGUMENTS]
-------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------
$$$ Stop Animations $$$

object1.stopAnimations()     // You will stop all animations for selected object

[NO ARGUMENTS]
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Object Touches Objects $$$

object1.objectTouchesObjects(object2,object3,object4)     // You will get if it toches the given objects

Arguments:
	*args       // Objeckts for checking if our objeckt is touched them
-------------------------------------------------------------------------------------




-------------------------------------------------------------------------------------
$$$ Object Touches Borders $$$

object1.objectTouchesBorders()     // WIll return False if not touches or touched porder position => "left","right","top","bottom"

[NO ARGUMENTS]
-------------------------------------------------------------------------------------


