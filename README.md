# InnovaccerAssignment
The Assignment for Innovaccer SummerGeeks program

For detailed report of this product read the "READ THIS.pdf" file...

TOOLS USED:
Flask (A python mini-framework)
Python (Databases, routes, sessions, encryption)
SQLite (Database)
HTML (Layout)
CSS (Styling)
Jinja 2 (To wrap the HTML and CSS around python functions)

On Home Page, once the user clicks on ‘Check In’ button on the top right corner, he is directed to this check in page. 
And as soon as he fills in his details and clicks on the blue ‘Check In’ button, he enters into his activity session 
and gets directed to the next window.
A prompt telling the user of his check in success. Simultaneously an email has already been sent to the HOST 
containing the visitor’s details.
Once the user’s visit is over and he wants to check out, he can click on the ‘check out’ button and get checked out.
Pressing the check out button will trigger an email  to the visitor himself…Containing his session details

How to run:
Visit http://entryms.herokuapp.com (HEROKU IS (sometimes)GIVING 'INTERNAL SERVER ERROR' ON CLICKING THE 'CHECK OUT' BUTTON.
IT IS NOT A PROBLEM WITH THE APP BUT WITH HEROKU SERVER AND CAN BE RESOLVED BY REFRESHING THE ERROR SCREEN(keep hitting refresh
till you see the 'checked out' alert :P))
OR
Download it from my github repository. 
Open the root folder and run the 'run' python file.
Open the command prompt or terminal in root directory.
Execute this command : ‘python run.py’
Copy the localhost address similar to this from the terminal : ‘http://127.0.0.1:5000/’
And (paste)open it in your browser
Requirements:
Python Installed
Environment Variable for python command set(to run from the Command Prompt)

To set the HOST Email address.
Go to entrysystem\routes.py.Scroll to ‘send_reset_email()’ function on line 63
And reset the recipients argument
recipients = ‘sample@mail.com’
TO SET THE account from which mails are sent
Go to entrysystem\__init__.py 
And reset sender to ‘sample@mail.com’
Then go back to routes.py
And in ‘MAIL_USERNAME’ set the same mail address that you just put in routes.py
And in ‘MAIL_PASSWORD’ set the password of that mail.
Also go to https://myaccount.google.com/u/2/lesssecureapps
And change “Allow less secure apps:” to ON
Or else google will not let you send email from the above email

Read the "READ THIS.pdf" for more details.

