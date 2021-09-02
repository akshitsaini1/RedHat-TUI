import os
import getpass
import lvm

os.system("sudo tput setaf 1")
print("\t\t\t -------------------------------------------")

os.system("sudo tput setaf 1")
print("\t\t\t -------------------------------------------")
os.system("sudo tput setaf 2")
print("ENTER YOUR LOGIN DETAILS:")
pas=getpass.getpass()
if pas=='12345':
 os.system("sudo tput setaf 3")
 print("Hey where do you want to perform the operations on your local machine or on any other ip?")

 os.system("sudo tput setaf 7") 
 def all():
 
  print("Press 1 for Local and 2 for remote")
  ch=input()
  if ch=='1':
   while True:
    print("press 1: for adding new user")
    print("press 2: for entering Configuring management menu" )
    print("press 3: If you want to download something")
    print("press 4: For Creating HardDisk partition ")
    print("press 5: For running a command directly!!")
    print("press 6: For Creating LVM")
    print("press 7: For Start Using DOCKER")
    print("press 0: to exit")
    os.system("sudo tput setaf 3")
    print("enter your choice:")
    print("-----------------")
    a=input()
    os.system("sudo tput setaf 7")
    if a=='1':
        os.system("sudo tput setaf 1")
        print("\t\t\tUSERADD")
        print("enter name of user:")
        x=input()
        os.system("sudo useradd {}".format(x))
        print("Give password to user mandatory for security purpose")       
        os.system("sudo passwd {}".format(x))
        os.system("sudo tput setaf 7")
    if a=='2':
        os.system("sudo tput setaf 1")
        print("\t\t\twelcome to congiguration world ")
        print("\t\t\t-------------------------------")
        os.system("sudo tput setaf 7")
        print("press y to see list to configure and any key to exit")
        b=input()
        if b=='y':
            print("press 1: For HTPPD configuration")
            print("press 2: For DOCKER configuration")
            print("press 3: For VSFTPD configuration")
            print("press 4: For FIREWALLD configuration")
            print("press 5: For NAS configuration")
            print("press 6: For Main Menu")
            z=input()
            if z=='1':
                print("do you wanna download HTTPD y for yes and N for no")
                http=input()
                if http=='y':
                    os.system("sudo yum install httpd -y")
                else:
                    print("so seems you have already downloaded HTTPD")
                os.system("sleep 2")
                print("Well after download copy paste the files to /var/www/html/ folder, or you can change additional settings.")
                os.system("sudo tput setaf 2")
                print("for this we can provide you extra terminal press y or n")
                os.system("sudo tput setaf 7")
                paste=input()
                if paste=='y':
                    os.system("sudo gnome-terminal")
                else:
                    print("hope you have settled everything")
                os.system("sleep 2")
                print("lets start the service and you are good to go!")
                os.system("sudo tput setaf 1")
              
                print("""httpd Services Started
                    ---  ---
                    (.)  (.)
                        ~ 
                     ======= 
                          """  )
                os.system("sudo systemctl start httpd")
                print("\t\tALRIGHT your service started you are a host now KEEP GOING")
                os.system("sudo tput setaf 7")
            if z=='2': 
                os.system("sudo tput setaf 1")
                print("so we will begin to install docker to skip press N:")
                doc=input()
                os.system("sudo tput setaf 7")
                if doc=='n':
                    print("Means docker is downloaded")
                else:
                    os.system("sudo yum install docker-ce  --nobest -y")
                os.system("sleep 2")
                os.system("sudo tput setaf 2")
                input("press enter to start services")
                os.system("sudo tput setaf 7")
                os.system("sudo systemctl start docker")
                os.system("sudo tput setaf 1")
                print("""Docker Services Started
                    ---  ---
                    (.)  (.)
                        ~ 
                     ======= 
                          """   )
                os.system("sudo tput setaf 7")
                input("press enter to continue")
                print("")
                    
            if z=='3':
                print("do you like to install VSFTPD ? y for yes and n for no")
                vsftpd=input()
                if vsftpd=='y':
                    os.system("sudo yum install vsftpd")
                print("VSFTPD already installed")
                os.system("sudo tput setaf 1")
                input("press any key to continue")
                os.system("sudo tput setaf 7")
                print("start services: ")
                os.system("sudo tput setaf 1")
                input("press enter to continue")
                os.system("sudo tput setaf 7")
                os.system("sudo systemctl start vsftpd")
                os.system("sudo tput setaf 1")
                print("""VSFTPD Services Started
                    ---  ---
                    (.)  (.)
                        ~   
                     =======
                          """   )
                os.system("sudo tput setaf 7")
            if z=='4':
                print("do you like to install FIREWALLD ? y for yes and n for no")
                FIREWALLD=input()
                if FIREWALLD=='y':
                   os.system("sudo yum install firewalld")
                print("firewalld already installed")
                os.system("sudo tput setaf 1")
                input("press any key to continue")
                os.system("sudo tput setaf 7")
                print("start services: ")
                os.system("sudo tput setaf 1")
                input("press enter to continue")
                os.system("sudo tput setaf 7")
                os.system("sudo systemctl start firewalld")
                os.system("sudo tput setaf 1")
                print("""FIREWALLD Services Started
                    ---  ---
                    (.)  (.)
                        ~
                     =======
                          """   )
                os.system("sudo tput setaf 7")
            if z=='5':
                print("""
                  /\/\/\/\ UNDER CONSTRUCTION /\/\/\/\
                           ------------------ 
                           """)
            if z=='6':
                input("Press any key for main menu")
                os.system("clear")
                all()
          
    if a=='3':
        os.system("sudo tput setaf 2")
        print("Just write what you wanna download:")
        c=input()
        os.system("sudo yum install {}".format(c))
        os.system("sudo tput setaf 7")
    if a=='4':
      
        os.system("sudo tput setaf 2")
        print("\t\t\tWELCOME TO PARTITION MENU")
        print("press y to continue:")
        d=input()
        if d=='y':
         def partition():
             print("press A: for checking the disks details:")
             print("press B: for creation of partition")
             print("press C: for formatting the drive")
             print("press D: for creation of new folder to mount")
             print("press E: for mounting the existing folder to your disk")
             print("press F: for going to main menu:")
             part=input()
             if part=='a':
                 os.system("sudo tput setaf 1")
                 print("So you are here to check the disk details here you go")
                 os.system("sudo tput setaf 7")
                 input("press any key to continue")
                 os.system("sudo fdisk -l")
                 input("now to see mount details press any key")
                 os.system("sudo df -h")
                 print("Press Enter To Continue")
                 os.system("clear")
             if part=='b':
                 os.system("sudo tput setaf 1")
                 print("Hey create partition freely")
                 os.system("sudo tput setaf 3")
                 print("""Before going into partition main menu just some points/instructions for you:
                     that 1st press n then enter
                     after decide 'p' for primary partition and 'e' for logical
                     3rd time just enter for by default
                     4th step to gave partition size gave by '+1G' example 
                     """)
                 os.system("sudo tput setaf 7")
                 print("write name of disk you want to use, just gave disk name for eg. sda1, sda2 etc:")
                 pd=input()
                 os.system("sudo fdisk /dev/{}".format(pd))
                 os.system("sudo udevadm settle")
                 input("to go to partition menu press key")
                 os.system("clear")
                 partition()
             if part=='c':
                 print("Format your disk:")
                 input("press enter to continue")
                 print("by defautl this will format to .ext4")
                 print("now again gave your DISk name:")
                 disk=input()
                 os.system("sudo mkfs.ext4 /dev/{}".format(disk))
                 os.system("sudo tput setaf 1")
                 print("FORMATTING DONE SUCCESS")
                 os.system("sudo tput setaf 7")
                 print("now back to partition menu")
                 os.system("clear")
                 partition()
             if part=='d':
                 print("enter the folder name you wanna create for mount")
                 fold=input()
                 os.system("sudo mkdir /{}".format(fold))
                 input("folder created press any key to enter partition menu ")
                 os.system("clear")
                 partition()
             os.system("sudo tput setaf 7")
             if part=='e':
                 os.system("sudo tput setaf 1")
                 print("So You Are Here To Mount")
                 os.system("sudo tput setaf 7")
                 input("/\/\Press Any Key/\/\ ")
                 print("give folder name to mount")
                 foo=input()
                 print("give your disk name")
                 dii=input()
                 os.system("sudo mount /dev/{}  /{}".format(dii,foo))
                 os.system("sudo tput setaf 1")
                 print("mount done!!")
                 os.system("sudo tput setaf 7")
                 print("press enter to continue")
                 os.system("clear")
             if part=='f':
                 os.system("clear")
                 all()
             os.system("sudo tput setaf 7")
         partition()
    if a=='5':
        print("Run Your Command Here!!, directly by giving command for eg: 'mkdir project', now give yours")
        os.system("sudo tput setaf 1")
        print("Now you are getting continous access to terminal just write commands according to your wish and press '0' to came out")
        while True:
         cmd=input()
         os.system("sudo {}".format(cmd))       
         if cmd=='0':
           all()
         os.system("sudo tput setaf 7")
    if a=='6':
        os.system("sudo tput setaf 1")
        print("WELCOME TO LVM MENU")
        print("-------------------")
        os.system("sudo tput setaf 7")
        input("press a key to continue")
        os.system("sudo tput setaf 2")
        print("""
         BEFORE CONTINUE MAKE SURE THE NEW DISK YOU HAVE ATTACHED MUST HAVE DONE THE PARTITION FORMAT MOUNT IF NOT DONE THEN PRESS 'N' FOR CONTINUE PRESS ANY OTHER KEY
      """)
        os.system("sudo tput setaf 7")
        lv=input()
        if lv=='n':
            partition()
      
        def lvmm():
            print("WELOCME TO LVM ")
            os.system("sudo tput setaf 2")
            print("""
             press 1: To Check Partition!!
             press 2: To Create PV!!
             press 3: To Create VG!!
             press 4: To Create LV!!
             press 5: To Enter Main Menu!!
          """)
            os.system("sudo tput setaf 7")
            lvm=input()
            if lvm=='1':
                print("to check partition of system")
                input("press any key to continue")
                os.system("sudo fdisk -l")
                input("press a key to enter LVM menu again!!")
                lvmm()
            if lvm=='2':
                print("welcome to create PV here:")
                input("press any key to continue")
                print("give your disk name to convert to PV for eg: sdc,sda")
                pvc=input()
                os.system("sudo pvcreate /dev/{}".format(pvc))
                os.system("sudo tput setaf 2")
                print("""Do you want to create annother pv?
                      press y for yes and n for no""")
                os.system("sudo tput setaf 7")
                pva=input()
                if pva=='y':
                    input("press any key to continue")
                    print("give your disk name to convert to PV for eg: sdc,sda")
                    pvc=input()
                    os.system("sudo pvcreate /dev/{}".format(pvc))
                os.system("sudo tput setaf 1")
                print("PV CREATED !!")
                os.system("sudo tput setaf 7")
                print("press any key to navigate LVM main menu:")
                lvmm()
            if lvm=='3':
                print("Welcome To Create VG")
                print("create vg from 2 pv")
                print("Enter the name of Vg you wanna create")
                vgn=input()
                print("give the name of 1st disk")
                vgd=input()
                print("give name of 2nd disk")
                vgdd=input()
                input("ALRIGHT PRESS ANY KEY TO CONTINUE!!")
                os.system("sudo vgcreate {} /dev/{} /dev/{}".format(vgn,vgd,vgdd))
                os.system("sudo tput setaf 2")
                print("VG CREATED!!")
                os.system("sudo tput setaf 7")
                input("press any key to check your VG")
                os.system("sudo vgdisplay {}".format(vgn))
                os.system("sudo tput setaf 3")
                input("press any key to LVM menu")
                os.system("sudo tput setaf 7")
                lvmm()
            if lvm=='4':
                print("WELCOME TO CREATE LV !!")
                input("press enter to continue")
                print("Give Name of lv you wanna create")
                lvc=input()
                print("Give Size Of Your LV You Wanna Create, for ex 50G, 60G etc")
                lvs=input()
                print("Give name of existing VG ")
                lvvg=input()
                os.system("sudo lvcreate --size{} --name {} {} ".format(lvs,lvc,lvvg))
                os.system("sudo tput setaf 2")
                print("LV CREATED")
                os.system("sudo tput setaf 7")
                input("press any key for Main Menu")
                all()
            lvmm()
            input("Press any key to continue")
            os.system("clear")
    if a=='7':
            dic = {
            1: "docker images",
            2: "docker pull",
            3: "docker ps",
            4: "docker ps -a",
            5: "docker run -dit",
            6: "docker stop",
            7: "docker info",
            8: "docker rm -f",
            9: "docker rmi "
             }
        
        
            def help():
                    print("""
                    1: List Images
                    2: Download Image
                    3: List Running Containers
                    4: List All Containers
                    5: Start Container
                    6: Stop Container
                    7: Describe container
                    0: Main Menu
                    *: Exit
                    """)



            def take_input():
                    ip= input("Enter your choce of h for help: ")
                    if ip == '*':
                            return ip
                    if ip == 'h':
                            return ip
                    try:
                            ip=int(ip)
                            return str(ip)
                    except:
                            print("Enter valid choice")
                            help()
                            return take_input()

            def dockerMenu():
                    ip = take_input()
                    while ip != '*':
                        if(ip == '1'):
                            os.system(dic[1])
                        elif(ip == '2'):
                            img_name = input("Enter image name to download or c for cancel: ")
                            if img_name == 'c':
                                continue
                            else:
                                os.system("{} {}".format(dic[2], img_name))
                        elif(ip == '3'):
                            os.system(dic[3])
                        elif(ip == '4'):
                            os.system(dic[4])
                        elif(ip == '5'):
                            img_name = input("Enter image name of container or c to cancel: ")
                            if img_name == 'c':
                                continue
                            c_name = input("Enter name of container or c to cancel: ")
                            if c_name == 'c':
                                continue
                            else:
                                os.system("{} --name {} {}".format(dic[5], c_name, img_name))
                        elif ip == '6':
                            id = input("Enter id of container to be stopped or c to cancel: ")
                            if id == 'c':
                                continue
                            else:
                                os.system("{} {}".format(dic[6], id))
                        elif ip == '7':
                            id = input("Enter id to see info or c to cancel: ")
                            if id == 'c':
                                continue
                            else:
                                os.system("{} {}".format(dic[7], id))
                        elif ip == '8':
                            id = input("Enter id of container to be stopped or c to cancel: ")
                            if id =='c':
                                    continue
                            else:
                                    os.system("{} {}".format(dic[8],id))
                        elif ip== '9':
                                img_name=input('Enter image name that is to be removed or c to cancel: ')
                                if img_name=='c':
                                        continue
                                else:
                                        os.system("{} {}".format(dic[9],img_name))
                        elif ip==0:
                                return
                        elif ip =='*':
                                sys.exit(0)
                        elif ip == 'h':
                                help()            
                        ip=take_input()
            dockerMenu()


    if a=='0':
        exit()
    input("press any key to continue")
    os.system("clear")
  elif ch=='2':
    os.system("sudo tput setaf 3")
    print("GIVE THE IP OF SYSTEM WHERE YOU WANNA DO YOUR WORK BUT YOU MUST KNOW THE PASSWORD OF IT")
    os.system("sudo tput setaf 7")
    user=input("Enter user name: ")
    passwd=getpass.getpass("Enter user passwd: ")
    ip=input("Enter user ip: ")
    
    ssh="sshpass -p {} ssh {}@{} -o StrictHostKeyChecking=no".format(passwd,user,ip)
    while True:
        print("press 1: for adding new user")
        print("press 2: for entering Configuring management menu")
        print("press 3: If you want to download something")
        print("press 4: For Creating HardDisk partition ")
        print("press 5: For running a command directly!!")
        print("press 6: For Creating LVM")
        print("press 7: For Start Using DOCKER")
        print("press 0: to exit")
        os.system("sudo tput setaf 3")
        print("enter your choice:")
        print("-----------------")
        a=input()
        os.system("sudo tput setaf 7")
        if a=='1':
            os.system("sudo tput setaf 1")
            print("\t\t\tUSERADD")
            print("enter name of user:")
            x=input()
            os.system("{} sudo useradd {}".format(ssh,ssh,x))
            print("Give password to user mandatory for security purpose")       
            os.system("{} sudo passwd {}".format(ssh,ssh,x))
            os.system("sudo tput setaf 7")
        if a=='2':
            os.system("sudo tput setaf 1")
            print("\t\t\twelcome to congiguration world ")
            print("\t\t\t-------------------------------")
            os.system("sudo tput setaf 7")
            print("press y to see list to configure and any key to exit")
            b=input()
            if b=='y':
                print("press 1: For HTPPD configuration")
                print("press 2: For DOCKER configuration")
                print("press 3: For VSFTPD configuration")
                print("press 4: For FIREWALLD configuration")
                print("press 5: For NAS configuration")
                print("press 6: For Main Menu")
                z=input()
                if z=='1':
                    print("do you wanna download HTTPD y for yes and N for no")
                    http=input()
                    if http=='y':
                        os.system("{} sudo yum install httpd -y".format(ssh,ssh))
                    else:
                        print("so seems you have already downloaded HTTPD")
                    os.system("{} sleep 2".format(ssh,ssh))
                    print("Well after download copy paste the files to /var/www/html/ folder, or you can change additional settings.")
                    os.system("sudo tput setaf 2")
                    print("for this we can provide you extra terminal press y or n")
                    os.system("sudo tput setaf 7")
                    paste=input()
                    if paste=='y':
                        os.system("sudo gnome-terminal")
                    else:
                        print("hope you have settled everything")
                    os.system("{} sleep 2".format(ssh,ssh))
                    print("lets start the service and you are good to go!")
                    os.system("sudo tput setaf 1")
                  
                    print("""httpd Services Started
                        ---  ---
                        (.)  (.)
                            ~ 
                         ======= 
                              """  )
                    os.system("{} sudo systemctl start httpd".format(ssh,ssh))
                    print("\t\tALRIGHT your service started you are a host now KEEP GOING")
                    os.system("sudo tput setaf 7")
                if z=='2': 
                    os.system("sudo tput setaf 1")
                    print("so we will begin to install docker to skip press N or enter to continue:")
                    doc=input()
                    os.system("sudo tput setaf 7")
                    if doc=='n':
                        print("Means docker is downloaded")
                    else:
                        os.system("{} sudo yum install docker-ce  --nobest -y".format(ssh,ssh))
                    os.system("sleep 2")
                    os.system("sudo tput setaf 2")
                    input("press enter to start services")
                    os.system("sudo tput setaf 7")
                    os.system("{} sudo systemctl start docker".format(ssh))
                    os.system("sudo tput setaf 1")
                    print("""Docker Services Started
                        ---  ---
                        (.)  (.)
                            ~ 
                         ======= 
                              """   )
                    os.system("sudo tput setaf 7")
                    input("press enter to continue")
                    print("")
                        
                if z=='3':
                    print("do you like to install VSFTPD ? y for yes and n for no")
                    vsftpd=input()
                    if vsftpd=='y':
                        os.system("{} sudo yum install vsftpd".format(ssh))
                    print("VSFTPD already installed")
                    os.system("sudo tput setaf 1")
                    input("press any key to continue")
                    os.system("sudo tput setaf 7")
                    print("start services: ")
                    os.system("sudo tput setaf 1")
                    input("press enter to continue")
                    os.system("sudo tput setaf 7")
                    os.system("{} sudo systemctl start vsftpd".format(ssh))
                    os.system("sudo tput setaf 1")
                    print("""VSFTPD Services Started
                        ---  ---
                        (.)  (.)
                            ~   
                         =======
                              """   )
                    os.system("sudo tput setaf 7")
                if z=='4':
                    print("do you like to install FIREWALLD ? y for yes and n for no")
                    FIREWALLD=input()
                    if FIREWALLD=='y':
                       os.system("{} sudo yum install firewalld".format(ssh))
                    print("firewalld already installed")
                    os.system("sudo tput setaf 1")
                    input("press any key to continue")
                    os.system("sudo tput setaf 7")
                    print("start services: ")
                    os.system("sudo tput setaf 1")
                    input("press enter to continue")
                    os.system("sudo tput setaf 7")
                    os.system("{} sudo systemctl start firewalld".format(ssh))
                    os.system("sudo tput setaf 1")
                    print("""FIREWALLD Services Started
                        ---  ---
                        (.)  (.)
                            ~
                         =======
                              """   )
                    os.system("sudo tput setaf 7")
                if z=='5':
                    print("""
                      /\/\/\/\ UNDER CONSTRUCTION /\/\/\/\
                               ------------------ 
                               """)
                if z=='6':
                    input("Press any key for main menu")
                    os.system("clear")
                    all()
              
        if a=='3':
            os.system("sudo tput setaf 2")
            print("Just write what you wanna download:")
            c=input()
            os.system("{} sudo yum install {}".format(ssh,c))
            os.system("sudo tput setaf 7")
        if a=='4':
        
            os.system("sudo tput setaf 2")
            print("\t\t\tWELCOME TO PARTITION MENU")
            print("press y to continue:")
            d=input()
            if d=='y':
             def partition():
                 print("press A: for checking the disks details:")
                 print("press B: for creation of partition")
                 print("press C: for formatting the drive")
                 print("press D: for creation of new folder to mount")
                 print("press E: for mounting the existing folder to your disk")
                 print("press F: for going to main menu:")
                 part=input()
                 if part=='a':
                     os.system("sudo tput setaf 1")
                     print("So you are here to check the disk details here you go")
                     os.system("sudo tput setaf 7")
                     input("press any key to continue")
                     os.system("{} sudo fdisk -l".format(ssh))
                     input("now to see mount details press any key")
                     os.system("{} sudo df -h".format(ssh))
                     print("Press Enter To Continue")
                     os.system("clear")
                 if part=='b':
                     os.system("sudo tput setaf 1")
                     print("Hey create partition freely")
                     os.system("sudo tput setaf 3")
                     print("""Before going into partition main menu just some points/instructions for you:
                         that 1st press n then enter
                         after decide 'p' for primary partition and 'e' for logical
                         3rd time just enter for by default
                         4th step to gave partition size gave by '+1G' example 
                         """)
                     os.system("sudo tput setaf 7")
                     print("write name of disk you want to use, just gave disk name for eg. sda1, sda2 etc:")
                     pd=input()
                     os.system("{} sudo fdisk /dev/{}".format(ssh,pd))
                     os.system("{} sudo udevadm settle".format(ssh))
                     input("to go to partition menu press key")
                     os.system("clear")
                     partition()
                 if part=='c':
                     print("Format your disk:")
                     input("press enter to continue")
                     print("by defautl this will format to .ext4")
                     print("now again gave your DISk name:")
                     disk=input()
                     os.system("{} sudo mkfs.ext4 /dev/{}".format(ssh,disk))
                     os.system("sudo tput setaf 1")
                     print("FORMATTING DONE SUCCESS")
                     os.system("sudo tput setaf 7")
                     print("now back to partition menu")
                     os.system("clear")
                     partition()
                 if part=='d':
                     print("enter the folder name you wanna create for mount")
                     fold=input()
                     os.system("{} sudo mkdir /{}".format(ssh,fold))
                     input("folder created press any key to enter partition menu ")
                     os.system("clear")
                     partition()
                 os.system("sudo tput setaf 7")
                 if part=='e':
                     os.system("sudo tput setaf 1")
                     print("So You Are Here To Mount")
                     os.system("sudo tput setaf 7")
                     input("/\/\Press Any Key/\/\ ")
                     print("give folder name to mount")
                     foo=input()
                     print("give your disk name")
                     dii=input()
                     os.system("{} sudo mount /dev/{}  /{}".format(ssh,dii,foo))
                     os.system("sudo tput setaf 1")
                     print("mount done!!")
                     os.system("sudo tput setaf 7")
                     print("press enter to continue")
                     os.system("clear")
                 if part=='f':
                     os.system("clear")
                     all()
                 os.system("sudo tput setaf 7")
             partition()
        if a=='5':
            print("Run Your Command Here!!, directly by giving command for eg: 'mkdir project', now give yours")
            os.system("sudo tput setaf 1")
            print("Now you are getting continous access to terminal just write commands according to your wish and press '0' to came out")
            while True:
             cmd=input()
             os.system("{} sudo {}".format(ssh,cmd))       
             if cmd=='0':
               all()
             os.system("sudo tput setaf 7")
        if a=='6':
            os.system("sudo tput setaf 1")
            print("WELCOME TO LVM MENU")
            print("-------------------")
            os.system("sudo tput setaf 7")
            input("press a key to continue")
            os.system("sudo tput setaf 2")
            print("""
             BEFORE CONTINUE MAKE SURE THE NEW DISK YOU HAVE ATTACHED MUST HAVE DONE THE PARTITION FORMAT MOUNT IF NOT DONE THEN PRESS 'N' FOR CONTINUE PRESS ANY OTHER KEY
          """)
            os.system("sudo tput setaf 7")
            lv=input()
            if: lv=='n':
                lvm.lvm_partition()
            # if lv=='n':
                # partition()
          
                def lvmm():
                    print("WELOCME TO LVM ")
                    os.system("sudo tput setaf 2")
                    print("""
                     press 1: To Check Partition!!
                     press 2: To Create PV!!
                     press 3: To Create VG!!
                     press 4: To Create LV!!
                     press 5: To Enter Main Menu!!
                  """)
                os.system("sudo tput setaf 7")
                lvm=input()
                if lvm=='1':
                    print("to check partition of system")
                    input("press any key to continue")
                    os.system("{} sudo fdisk -l".format(ssh))
                    input("press a key to enter LVM menu again!!")
                    lvmm()
                if lvm=='2':
                    print("welcome to create PV here:")
                    input("press any key to continue")
                    print("give your disk name to convert to PV for eg: sdc,sda")
                    pvc=input()
                    os.system("{} sudo pvcreate /dev/{}".format(ssh,pvc))
                    os.system("{} sudo tput setaf 2".format(ssh))
                    print("""Do you want to create annother pv?
                          press y for yes and n for no""")
                    os.system("sudo tput setaf 7")
                    pva=input()
                    if pva=='y':
                        input("press any key to continue")
                        print("give your disk name to convert to PV for eg: sdc,sda")
                        pvc=input()
                        os.system("{} sudo pvcreate /dev/{}".format(ssh,pvc))
                    os.system("sudo tput setaf 1")
                    print("PV CREATED !!")
                    os.system("sudo tput setaf 7")
                    print("press any key to navigate LVM main menu:")
                    lvmm()
                if lvm=='3':
                    print("Welcome To Create VG")
                    print("create vg from 2 pv")
                    print("Enter the name of Vg you wanna create")
                    vgn=input()
                    print("give the name of 1st disk")
                    vgd=input()
                    print("give name of 2nd disk")
                    vgdd=input()
                    input("ALRIGHT PRESS ANY KEY TO CONTINUE!!")
                    os.system("{} sudo vgcreate {} /dev/{} /dev/{}".format(ssh,vgn,vgd,vgdd))
                    os.system("sudo tput setaf 2")
                    print("VG CREATED!!")
                    os.system("sudo tput setaf 7")
                    input("press any key to check your VG")
                    os.system("{} sudo vgdisplay {}".format(ssh,vgn))
                    os.system("sudo tput setaf 3")
                    input("press any key to LVM menu")
                    os.system("sudo tput setaf 7")
                    lvmm()
                if lvm=='4':
                    print("WELCOME TO CREATE LV !!")
                    input("press enter to continue")
                    print("Give Name of lv you wanna create")
                    lvc=input()
                    print("Give Size Of Your LV You Wanna Create, for ex 50G, 60G etc")
                    lvs=input()
                    print("Give name of existing VG ")
                    lvvg=input()
                    os.system("{} sudo lvcreate --size{} --name {} {} ".format(ssh,lvs,lvc,lvvg))
                    os.system("sudo tput setaf 2")
                    print("LV CREATED")
                    os.system("sudo tput setaf 7")
                    input("press any key for Main Menu")
                    all()
                lvmm()
                input("Press any key to continue")
                os.system("clear")
        if a=='7':
                dic = {
                1: "docker images",
                2: "docker pull",
                3: "docker ps",
                4: "docker ps -a",
                5: "docker run -dit",
                6: "docker stop",
                7: "docker info",
                8: "docker rm -f",
                9: "docker rmi "
                 }
            
            
                def help():
                        print("""
                        1: List Images
                        2: Download Image
                        3: List Running Containers
                        4: List All Containers
                        5: Start Container
                        6: Stop Container
                        7: Describe container
                        0: Main Menu
                        *: Exit
                        """)
    
    
    
                def take_input():
                        ip= input("Enter your choce of h for help: ")
                        if ip == '*':
                                return ip
                        if ip == 'h':
                                return ip
                        try:
                                ip=int(ip)
                                return str(ip)
                        except:
                                print("Enter valid choice")
                                help()
                                return take_input()
    
                def dockerMenu():
                        ip = take_input()
                        while ip != '*':
                            if(ip == '1'):
                                os.system("{} {}".format(ssh,dic[1]))
                            elif(ip == '2'):
                                img_name = input("Enter image name to download or c for cancel: ")
                                if img_name == 'c':
                                    continue
                                else:
                                    os.system("{} {} {}".format(ssh,dic[2], img_name))
                            elif(ip == '3'):
                                os.system("{} {}".format(ssh,dic[3]))
                            elif(ip == '4'):
                                os.system("{} {}".format(ssh,dic[4]))
                            elif(ip == '5'):
                                img_name = input("Enter image name of container or c to cancel: ")
                                if img_name == 'c':
                                    continue
                                c_name = input("Enter name of container or c to cancel: ")
                                if c_name == 'c':
                                    continue
                                else:
                                    os.system("{} {} --name {} {}".format(ssh,dic[5], c_name, img_name))
                            elif ip == '6':
                                id = input("Enter id of container to be stopped or c to cancel: ")
                                if id == 'c':
                                    continue
                                else:
                                    os.system("{} {} {}".format(ssh,dic[6], id))
                            elif ip == '7':
                                id = input("Enter id to see info or c to cancel: ")
                                if id == 'c':
                                    continue
                                else:
                                    os.system("{} {} {}".format(ssh,dic[7], id))
                            elif ip == '8':
                                id = input("Enter id of container to be stopped or c to cancel: ")
                                if id =='c':
                                        continue
                                else:
                                        os.system("{} {} {}".format(ssh,dic[8],id))
                            elif ip== '9':
                                    img_name=input('Enter image name that is to be removed or c to cancel: ')
                                    if img_name=='c':
                                            continue
                                    else:
                                            os.system("{} {} {}".format(ssh,dic[9],img_name))
                            elif ip==0:
                                    exit()
                            elif ip =='*':
                                    exit()
                            elif ip == 'h':
                                    help()            
                            ip=take_input()
                dockerMenu()


        if a=='0':
            exit()
        input("press any key to continue")
        os.system("clear")
 

 all() 
else:
    print("you need to exit you gave wrong credentials sorry ")
