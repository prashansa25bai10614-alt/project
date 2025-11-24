project title - shopping list maagement system



Project Overview — Shopping List Program
The Shopping List Program is a simple, menu-driven Python application designed to help users manage their shopping items efficiently. It allows users to add items, remove items, view the complete shopping list, and exit the program. The project demonstrates the use of basic Python concepts such as lists, loops, functions, conditionals, and user input handling.
The program starts by displaying a menu that guides the user to choose one of the four operations. The core data is stored in a Python list called shopping_list, which acts as temporary in-memory storage during the execution of the program. Each menu option triggers specific logic—adding new items, removing existing ones, or displaying the list in a clean, numbered format.
The application runs inside an infinite loop (while True:), ensuring the user can perform multiple operations without restarting the program. The loop continues until the user selects the exit option. Proper validation and feedback messages are included to ensure the program remains user-friendly and stable, even when incorrect inputs are entered.
Overall, this project serves as an excellent introduction to Python programming. It helps beginners understand how to structure a program, handle user interactions, apply list operations, and build a functional tool that has practical real-life use.








Features of the Shopping List Management System

1. Add New Items
Users can add any number of items to the shopping list.
Prevents duplicates to avoid confusion.

2. Remove Items
Allows users to delete items they no longer need.
If an item is not found, the program shows a proper message.

3. View Shopping List
Displays all items currently present in the list.
If the list is empty, it informs the user clearly.

4. User-Friendly Menu
A simple menu system that guides the user with options.
Easy to understand even for beginners.

5. Continuous Operation
Program runs in a loop until the user chooses to exit.
Makes the system convenient for multiple actions in one run.

6. Error Handling
Shows clear messages for invalid actions.
Avoids crashes through proper input validation.

7. Simple and Clean Interface
Text-based interface suitable for beginners.
No unnecessary complexity; easy to maintain.






Technologies/Tools Used

1. Python Programming Language
The project is fully developed using Python.
Easy syntax, beginner-friendly, and powerful for text-based applications.

2. Python IDLE / VS Code (any code editor)
Used for writing, editing, and executing the Python code.
You can mention any editor you used:
IDLE
VS Code
PyCharm
Jupyter Notebook (optional)

3. Command Line / Terminal
Used to run the program.
Acts as the user interface for the menu-driven system.

4. Python Built-in Data Structures
List is used to store the shopping items.
No external libraries needed.

5. Operating System
Windows / macOS / Linux (whichever you used for development).







Steps to Install and Run the Project

1. Install Python
If Python is not installed on your computer:
Windows

1. Go to the official Python website:
https://www.python.org/downloads
2. Download the latest version of Python.
3. Run the installer and check the box “Add Python to PATH.”
4. Complete the installation.
Mac / Linux
Python is usually pre-installed.
To check, open Terminal and type:
python3 --version

2. Set Up the Project File
1. Open your code editor (IDLE / VS Code / PyCharm / Notepad++).
2. Create a new file named:
shopping_list.py
3. Copy and paste the full program code into the file.
4. Save the file.


3. Run the Program
Method 1: Using VS Code / Any Editor
1. Open the file shopping_list.py
2. Click Run or press:
Ctrl + F5   (Windows)
Command + F5 (Mac)

Method 2: Using Command Prompt / Terminal
1. Navigate to the folder where the file is saved.
2. Run this command:
python shopping_list.py
or (on some systems):
python3 shopping_list.py


4. Use the Application
Once the program starts:
You will see:

--- Shopping List Menu ---
1. Add item
2. Remove item
3. View list
4. Exit

Then:
Press 1 to add an item
Press 2 to remove an item
Press 3 to view your shopping list
Press 4 to exit the program

5. End the Program
Select Option 4 to safely exit.







Instructions for Testing
1. Purpose of Testing
To ensure that all features of the Shopping List Program work correctly, and the system behaves as expected for both valid and invalid inputs.


🔍 2. Test Preparation
Before starting the tests:
Make sure Python is installed.
Ensure the program file shopping_list.py is saved.
Run the program using:
python shopping_list.py


🧪 3. Testing Instructions
Test Case 1: Add Item
Steps:
1. Run the program.
2. Choose option 1 from the menu.
3. Enter any item name, e.g., Milk.
Expected Result:
The program should display:
“✅ Milk added to your shopping list.”

Test Case 2: Remove Existing Item
Steps:
1. Add an item (e.g., Eggs).
2. Choose option 2.
3. Enter Eggs to remove it.
Expected Result:
The program removes the item and shows:
“❌ Eggs removed from your shopping list.”

Test Case 3: Remove Non-existing Item
Steps:
1. Choose option 2.
2. Enter an item not in the list (e.g., Chocolate).
Expected Result:
Program should display:
“Item not found in the list.”

Test Case 4: View Shopping List (Items Present)
Steps:
1. Add a few items.
2. Choose option 3.
Expected Result:
Displays all items in numbered format:
1. Milk
2. Bread
3. Butter

Test Case 5: View Empty Shopping List
Steps:
1. Run the program.
2. Directly choose option 3.
Expected Result:
Message shown:
“Your shopping list is empty.”

Test Case 6: Invalid Menu Option
Steps:
1. Enter an invalid choice (e.g., 7, abc, @).
Expected Result:
Program should display:
“Invalid choice. Please enter 1–4.”

Test Case 7: Exit Program
Steps:
1. Choose option 4.
Expected Result:
Program displays:
“Goodbye! 🛍”
and stops execution.


📝 4. Testing Approach
Manual testing
Black-box testing
Input validation checks
Positive & negative test scenarios
Repeated testing to check stability
Press 4 to exit the program

5. End
