# phoneAndEmail

a python script that can find all phone numbers and emails within a specific webpage or the current clipboard of the user

## Usage

### Using the Terminal (scanning the webpage)

Run the script from the command line using `./phoneAndEmail.py _websiteURL_` (on Linux or OS X).


On Windows, create a batch file like so:
> @py.exe C:\path\to\pythonScript.py %*  
> @pause

then call the batch file using the command `phoneAndEmail _websiteURL_`

### Running the Script by Itself (scanning the clipboard)

Simply run the script and the scrip will look through the current clipboard and scan for any phone numbers and emails within it.

## Output

The script will list all phone numbers and emails found within the terminal.
If no phone numbers or emails can be found, an appropriate message will be given.
If the script is called incorrectly (i.e. too many arguments), the program will end with an error message.

Any found phone number and emails will be copied to the user's clipboard for use.
