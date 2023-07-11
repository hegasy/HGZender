⚠️Only for educational purposes⚠️
# HGZender

HGZender is a Python script that uses an SMTP server to send bulk email messages. It provides a simple and efficient way to send personalized emails to a list of recipients.

## Features

- Retrieves SMTP details from a text file named "smtp.txt" which is formatted as host|port|username|password.
- Selects a random "From Name" from a text file named "fromnames.txt".
- Chooses a random "Email From" address from a text file named "mailfrom.txt".
- Utilizes an HTML letter from a file named "letter.html".
- Randomly selects an email subject from a text file named "subjects.txt".
- Retrieves the recipient list from a file named "maillist.txt".
- Supports multithreading for faster sending of emails.
- Prints "Email sent" message for each successfully sent email.
- Saves successfully sent recipients to "sent.txt".
- Saves unsuccessfully sent recipients to "error.txt".

## Usage

1. Prepare the necessary files:
   - Create a text file named "smtp.txt" and add the SMTP server details in the format: `host|port|username|password`. Each line should contain a different SMTP server.
   - Create a text file named "fromnames.txt" and add different "From Names" on each line.
   - Create a text file named "mailfrom.txt" and add different "Email From" addresses on each line.
   - Create an HTML file named "letter.html" with the content of the email letter.
   - Create a text file named "subjects.txt" and add different email subjects on each line.
   - Create a text file named "maillist.txt" and add the list of recipients' email addresses, one address per line.

2. Run the script:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script and the files.
   - Run the command: `python HGZender.py`.
   - Follow the prompts to enter the number of threads to use for parallel sending.

3. Monitor the progress:
   - The script will start sending emails to the recipients using the SMTP servers specified in "smtp.txt".
   - Each successful email sending will display an "Email sent" message on the screen.
   - Successfully sent recipient email addresses will be saved in the "sent.txt" file.
   - Unsuccessfully sent recipient email addresses will be saved in the "error.txt" file.

## Notes

- It is important to ensure that the SMTP servers provided in the "smtp.txt" file are valid and accessible.
- The number of threads used for sending emails affects the speed of sending. Adjust the number based on your system capabilities and network conditions.
- The script uses Python's built-in `smtplib` and `threading` modules to send emails and handle multithreading.
