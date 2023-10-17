import socket
import mysql.connector
import ssl
import random
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def start_server(host, port, certfile, keyfile):
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_socket.bind((host, port))
    listener_socket.listen(1)
    print(f"Listening on {host}:{port}...")
    
    # credentials of the database 
    mydb = mysql.connector.connect(
     host="",
     user="",
     password="",
     database="",
     port=""
    )

    
    # mail server credentials
    smtpServer = ""
    smtpPort = 1234
    username = ""
    password = ""

    # sender and receiver
    sender = ""
    reciever = ""

    # defice var active
    activ = False

    # proof if a value is too high
    while True:
        client_socket, client_address = listener_socket.accept()
        print(f"Connection from {client_address}")

        try:

            client_socket = ssl.wrap_socket(client_socket, keyfile=keyfile, certfile=certfile, server_side=True, ssl_version=ssl.PROTOCOL_TLS)
            
            while True:
                data = client_socket.recv(1024)
                if not data:
                  break
                message = data.decode('utf-8')
                allValues = message.split(",")
                valueTemp = allValues[0]
                valueHumid = allValues[1]
                print(f"Received: {message}")
                ConValueTemp = round(float(valueTemp), 2)
                ConValueHumid = round(float(valueHumid), 2)

                device = "2"

                if activ and ConValueTemp < 40:
                    active = False


                if ConValueTemp >= 40 and not activ: 
                    activ = True
                    print("Value over 40")

                    # send email 
                    # content of the mail
                    subject = "Temperatursensorwarnung"
                    body = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Temperatursensorwarnung - Kritischer Wert überschritten</title>
                        <style>
                            body {
                                font-family: Arial, sans-serif;
                                background-color: #f0f0f0;
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                max-width: 600px;
                                margin: 0 auto;
                                background-color: #fff;
                                padding: 20px;
                                border-radius: 5px;
                                box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
                            }

                            h1 {
                                color: #ff5733;
                            }

                            p {
                                line-height: 1.6;
                            }

                            a {
                                color: #007bff;
                                text-decoration: none;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h1>Temperatursensorwarnung - Kritischer Wert überschritten</h1>

                            <p>Sehr geehrte/r Empfänger/in,</p>

                            <p>Der Temperatursensor hat soeben einen kritischen Wert überschritten. Es ist wichtig, sofort Maßnahmen zu ergreifen, um mögliche Probleme zu verhindern.</p>

                            <p>Temperaturwert: 80°C</p>

                            <p>Um weitere Informationen zu erhalten oder um sich anzumelden und die Situation zu überwachen, klicken Sie bitte auf den folgenden Link:</p>

                            <a href="https://dddrey.info">Anmelden</a>

                            <p>Wir empfehlen dringend, die Ursache für die Temperaturüberschreitung zu ermitteln und geeignete Schritte zur Behebung des Problems zu unternehmen.</p>

                            <p>Vielen Dank für Ihre Aufmerksamkeit und Ihr sofortiges Handeln.</p>

                            <p>Mit freundlichen Grüßen, IoTech</p>
                        </div>
                    </body>
                    </html>

                    """

                    # define all relevant objects
                    msg = MIMEMultipart()
                    msg['Subject'] = subject
                    msg['From'] = sender
                    msg['To'] = reciever

                    part = MIMEText(body, 'html')
                    msg.attach(part)

                    # login to mail-server
                    smtpObj = smtplib.SMTP(smtpServer, smtpPort)
                    smtpObj.set_debuglevel(1)
                    smtpObj.starttls()
                    smtpObj.login(username, password)

                    # absenden der E-Mail
                    smtpObj.sendmail(sender, reciever, msg.as_string())

                mycursor = mydb.cursor()

                sql = "INSERT INTO humidity (humidity, deviceId) VALUES (%s, %s)"
                val = (ConValueHumid , device)
                mycursor.execute(sql, val)

                mydb.commit()

                print(mycursor.rowcount, "record inserted.")

                sql = "INSERT INTO humidity (temperature, deviceId) VALUES (%s, %s)"
                val = (ConValueTemp , device)
                mycursor.execute(sql, val)

                mydb.commit()

                print(mycursor.rowcount, "record inserted.")

        except KeyboardInterrupt:
            print("Server stopped by user.")
            break
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    host = '0.0.0.0'  # IP-address of the Server that is listening
    port = 1234  # port of the Server that is listening
    certfile = 'home/kern/key/cert.crt'  # path to tls cert
    keyfile = 'pfad/zum/key.key'    # path to tls key

    start_server(host, port, certfile, keyfile)
