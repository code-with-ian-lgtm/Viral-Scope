Viral Scope

Overview
Viral Scope is a desktop application designed for managing patient information and facilitating sample collection. The application is built using customtkinter and tkinter for the graphical user interface, and PIL for image processing. The project aims to streamline the process of registering patients, saving their information, and viewing their details in a user-friendly interface.

Features
Patient Registration:

Input fields for first name, last name, year of birth, gender, email, and county.
Automatic calculation of age based on the year of birth.
Generates a unique patient ID for each registration.
Validates input to ensure all required fields are filled out correctly.
Saves patient details to a document file using a file dialog.
View Patient Records:

Displays patient records in a Treeview widget.
Configurable appearance and layout for the tree view.
Supports additional functionalities like adding, viewing, and modifying patient records.
User Interface:

Customizable appearance with options for Light, Dark, and System modes.
Utilizes customtkinter for a modern and responsive UI.
Includes buttons for obtaining samples, viewing patients, and running diagnostics.
Organized layout with frames and grid configurations for easy navigation.
Image Handling:

Loads and displays images using PIL and ImageTk.
Supports custom icons for buttons and UI elements.
Technologies Used
Python
tkinter and customtkinter for GUI
PIL for image processing
random for generating unique IDs
os and filedialog for file handling
webbrowser for potential future integrations
How to Run
Ensure you have Python installed on your machine.
Install the required packages using pip install -r requirements.txt.
Run the main application script: python main.py.
Future Enhancements
Integration with a database for persistent storage of patient records.
Enhanced input validation and error handling.
Additional functionalities for diagnostics and sample management.
Improved UI/UX with more customization options.
