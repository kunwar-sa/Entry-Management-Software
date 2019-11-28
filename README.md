# InnovaccerAssignment
The Assignment for Innovaccer SummerGeeks program

*IMPORTANT*

I started making this application on 27th November (and the submission deadline was on 28th November)
because on 27th my college sent me the mail about this programm.
Everything that you see here has been made overnight and in less than 24 hours.
I gave it all I had.
I managed to meet all the requirements of the the assignment like sending visitor details
through email to host on check in and to the visitor when he checks out.
If I had been working on this from 18th November like everyone else I would have made it a 
10 times better including SMS notification and multiple visitor sessions.

SO PLEASE CONSIDER MY CHALLENGING SITUATION DURING EVALUATION. I AM CAPABLE OF MUCH MORE.

TOOLS USED:
Flask (A python min-framework)
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
Visit http://entryms.herokuapp.com
OR
Download it from my github repository. 
Open the root folder
Open the command prompt or terminal in root directory.
Run ‘python run.py’
Copy the localhost address ‘http://127.0.0.1:5000/’
And open it in your browser
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



