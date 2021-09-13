import os
import getpass
import subprocess
import time


def ping():
    x=subprocess.check_output("ping -c4 google.com | grep bytes | wc -l",shell=True)
    if x.decode()=='5\n':
        print("You have great connectivity !!")
    else:
        print("""No Connectivity !\n
        1. Check your connection in host.
        2. Check Network setting, it should be Bridged.
        3. Restart your Virtual Machine.""")


print("""\t\tWelcome to my Terminal User Interface
\t\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
passwd = getpass.getpass("Enter the password for Validation: ")
print()
if passwd == 'daksh':
    loc = input("""Correct Password :)
Would you like to use your local system or some remote access?
local/remote ->""")
    print()
    if loc == 'local':
        while True:
            print("""Your available options are:
                1. Date
                2. Any specific calendar
                3. Create any folder
                4. Create file
                5. Check you IP Address
                6. Check Connectivity to Internet
                7. Open Firefox
                8. Open new Terminal
                9. Open Calculator
                10. Install / Uninstall Softwares
                11. Check IP Address of any Website
                12. Configure Web Server
                13. Add User
                14. Exit\n""")
            choice = int(input("Enter your choice: "))
            print()

            if choice == 1:
                os.system("date")

            elif choice == 2:
                ask = input("Current? y/N -> ")
                print()
                if ask == 'y':
                    os.system("cal")
                elif ask == 'N':
                    mm = int(input("Specify Month in number: "))
                    yyyy = int(input("Specify Year in number: "))
                    os.system("cal {0} {1}\n".format(mm,yyyy))
                else:
                    print("Invalid Choice")

            elif choice == 3:
                foldername = input("Write the name of the folder: ")
                os.system("mkdir {}".format(foldername))
                print("Your folder {} has been created.\n".format(foldername))

            elif choice == 4:
                filename = input("Write the name of file with extension: ")
                os.system("touch {}".format(filename))
                print("Your file {} has been created.\n".format(filename))

            elif choice == 5:
                print("Please wait!")
                ping()
                os.system("ifconfig enp0s8 | grep 'inet '\n")

            elif choice == 6:
                print("Please wait! Checking connectivity...")
                ping()

            elif choice == 7:
                print("Please wait...")
                os.system("firefox&")
                time.sleep(3)

            elif choice == 8:
                os.system("gnome-terminal")

            elif choice == 9:
                print("Press Ctrl+C to Exit the calculator")
                print()
                os.system("bc")

            elif choice == 10:
                os.system("clear")
                while True:
                    print("""    Welcome to the DNF
    ^^^^^^^^^^^^^^^^^^

    1. To list softwares
    2. To list your repos
    3. To search for the name of a software
    4. To install a software
    5. To uninstall a software
    6. Exit DNF""")
                    print()
                    choice1 = int(input("Enter your choice: "))
                    print()
                    if choice1 == 1:
                        print("Listing all softwares...\nPlease wait...\n")
                        time.sleep(1)
                        os.system("dnf list")

                    elif choice1 == 2:
                        print("Listing all repos...\nPlease wait...\n")
                        time.sleep(1)
                        os.system("dnf repolist")

                    elif choice1 == 3:
                        sw = input("Enter name of software you want to check: ")
                        os.system("dnf list | grep {}".format(sw))

                    elif choice1 == 4:
                        sw = input("Enter name of Software to install: ")
                        ping()
                        os.system("dnf install {} -y".format(sw))

                    elif choice1 == 5:
                        sw = input("Enter name of Software to uninstall: ")
                        confirm = input("Are you sure? y/N -> ")
                        if confirm == 'y':
                            os.system("dnf remove {} -y".format(sw))
                        else:
                            pass

                    elif choice1 == 6:
                        break

                    else:
                        print("check the options and try again...")
                        print()
                        input("Press Enter to continue using DNF....")
                        os.system("clear")

            elif choice == 11:
                site = input("Enter the complete name of the website: ")
                print("Please wait!")
                print()
                time.sleep(1)
                os.system("nslookup {}".format(site))

            elif choice == 12:
                print("""Setting up webserver...
Installing HTTPD
Copying index.html to default directory
Starting the service
Testing webpage...""")
                print("\n\n\n")
                os.system("yum install httpd -y")
                os.system("cp ./index.html /var/www/html/")
                os.system("systemctl start httpd --now")
                print("\n\n\n")
                print("OUTPUT OF CURL")
                print("^^^^^^^^^^^^^^")
                os.system("curl http://localhost:80")
                print("\n")
                print("Web Server successfully setup...")

            elif choice == 13:
                username = input("Specify the username: ")
                os.system("useradd {}".format(username))
                print("User {} has been created.\n".format(username))
                password =  getpass.getpass("Enter password for user {}: ".format(username))
                os.system("echo {} | passwd {} --stdin".format(password,username))
                print("Password has been set!")

            elif choice == 14:
                print("Thank You for using our tool!!\n")
                exit()

            else:
                print("Please input a valid menu option")
            print()
            input("Enter to continue...")
            os.system("clear")


    elif loc == 'remote':
        remoteIP = input("Please enter the IP you would like to connect to -> ")
                #os.system("ssh root@{}".format(remoteIP))
        print("You are now connected to IP ",remoteIP)
                #os.system("ssh-keygen")
                #os.system("ssh-copy-id root@{}".format(remoteIP))
        print()
        while True:
            print("""Your available options are:
                1. Date
                2. Any specific calendar
                3. Display IP Address of Client and Server
                4. Check Connectivity
                5. Open a Graphical command
                5. Exit\n""")
            choice = int(input("Enter your choice: "))
            print()
            if choice == 1:
                os.system("ssh root@{} date".format(remoteIP))
                
            elif choice == 2:
                ask = input("Current? y/N -> ")
                print()
                if ask == 'y':
                    os.system("ssh root@{} cal".format(remoteIP))
                elif ask == 'N':
                    mm = int(input("Specify Month in number: "))
                    yyyy = int(input("Specify Year in number: "))
                    os.system("ssh root@{0} cal {1} {2}\n".format(remoteIP,mm,yyyy))
                else:
                    print("Invalid Choice")
                    
            elif choice == 3:
                print("Your IP is: ")
                os.system("ifconfig enp0s3 | grep 'inet '\n")
                print("Remote IP is: ")
                os.system("ssh root@{} ifconfig enp0s3 | grep 'inet '\n".format(remoteIP))
                
            elif choice == 4:
                x=subprocess.check_output("ssh root@{} ping -c4 google.com | grep bytes | wc -l".format(remoteIP),shell=True)
                if x.decode()=='5\n':
                    print("You have great connectivity !!")
                else:
                    print("""No Connectivity !\n
1. Check your connection in host.
2. Check Network setting, it should be Bridged.
3. Restart your Virtual Machine.""")
                    
            elif choice == 5:
                a = input("""Do you want to launch a Graphical Software on your PC or the Server?
Mine/Server -> """)
                if a == 'Mine':
                    cmd1=input("Enter the command to run on your PC: ")
                    os.system("ssh root@{0} -X {1}".format(remoteIP,cmd1))
                elif a == 'Server':
                    print("I will help you to activate Graphical Software on the server")
                    os.system("ssh root@{}".format(remoteIP))
                    os.system("export DISPLAY=:0")
                    os.system("xhost +")
                    cmd2=input("Now enter the command to run on the server: ")
                    os.system("{1}&".format(cmd2))
                    print("The software is now opened in the Server computer.")
                    
            elif choice == 6:
                print("Thank You for using our tool!!\n")
                print("Logging Out....")
                os.system("exit")
                exit()
                    
            else:
                print("Please input a valid menu option")
                    
            print()
            input("Enter to continue......")
            os.system("clear")


    else:
        print("Option not supported!!")
else:
    print("Password is wrong")
