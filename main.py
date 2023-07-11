import random
import smtplib
import threading

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def send_email(smtp_host, smtp_port, smtp_username, smtp_password, from_name, mail_from, subject, letter_html, recipient):
    message = f"From: {from_name} <{mail_from}>\n"
    message += f"To: {recipient}\n"
    message += f"Subject: {subject}\n"
    message += "Content-Type: text/html; charset=utf-8\n\n"
    message += letter_html

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(mail_from, recipient, message)
        print(f"Email sent to {recipient}")
        return True
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")
        return False

# Print banner
print("""
██   ██  ██████  ███████ ███████ ███    ██ ██████  ███████ ██████  
██   ██ ██          ███  ██      ████   ██ ██   ██ ██      ██   ██ 
███████ ██   ███   ███   █████   ██ ██  ██ ██   ██ █████   ██████  
██   ██ ██    ██  ███    ██      ██  ██ ██ ██   ██ ██      ██   ██ 
██   ██  ██████  ███████ ███████ ██   ████ ██████  ███████ ██   ██ 

by @hegasy                                                                  
""")

# Read SMTP details from smtp.txt
smtp_details = read_file('smtp.txt')

# Read the other necessary files
from_names = read_file('fromnames.txt')
mail_from_list = read_file('mailfrom.txt')
letter_html = ''.join(read_file('letter.html'))
subjects = read_file('subjects.txt')
recipients = read_file('maillist.txt')

# Ask user for the number of threads to use
threads = int(input("Enter the number of threads to use: "))

# Initialize counters for successful and unsuccessful emails
success_count = 0
error_count = 0

# Create a threading lock
lock = threading.Lock()

# Define the email sending function for each thread
def send_emails_thread(thread_id):
    # Calculate the range of recipients for the thread
    start_index = thread_id * (len(recipients) // threads)
    end_index = start_index + (len(recipients) // threads)
    if thread_id == threads - 1:
        end_index = len(recipients)

    # Iterate over recipients and send emails for the thread's range
    for i in range(start_index, end_index):
        recipient = recipients[i]

        # Retry sending email with different SMTP server if connection fails
        while True:
            if not smtp_details:
                print("All SMTP servers failed. Exiting thread.")
                return

            # Randomly select SMTP details for each connection
            smtp_host, smtp_port, smtp_username, smtp_password = random.choice(smtp_details).split('|')

            # Randomly select from name, from email, and subject for each email
            from_name = random.choice(from_names)
            mail_from = random.choice(mail_from_list)
            subject = random.choice(subjects)

            if send_email(smtp_host, int(smtp_port), smtp_username, smtp_password, from_name, mail_from, subject, letter_html, recipient):
                with lock:
                    global success_count
                    success_count += 1
                    with open('sent.txt', 'a') as file:
                        file.write(recipient + '\n')
                break
            else:
                with lock:
                    global error_count
                    error_count += 1
                    with open('error.txt', 'a') as file:
                        file.write(recipient + '\n')
                smtp_details.remove(f"{smtp_host}|{smtp_port}|{smtp_username}|{smtp_password}")

# Create and start the threads
thread_list = []
for i in range(threads):
    thread = threading.Thread(target=send_emails_thread, args=(i,))
    thread_list.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in thread_list:
    thread.join()

print("Sent:", success_count)
print("Error:", error_count)
