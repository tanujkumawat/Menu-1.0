import os
import subprocess
import getpass



os.system("tput setaf 4")
print("##########\tWelcome to the Menu Program\t##########")
os.system("tput setaf 0")
print("##########\t***************************\t##########")


password = getpass.getpass("Enter the password to use tool :")

if password == "tanuj":

	whileVar = True
	while whileVar:
		print("""Press 1 : Show Date
Press 2 : Show Cal
Press 3 : Change colour of terminal to red
Press 4 : Create a new User
Press 5 : Click photo graph
Press 6 : Check IP address
Press 7 : Ping IP address
Press 8 : Setup Hadoop
Press 9 : Exit
""")

		print("Enter input :", end = "")
		usrinput = input()
		ch = int(usrinput)

		if ch == 1 :
			os.system("date")
		elif ch == 2 :
			os.system("cal")
		elif ch == 3 :
			os.system("tput setaf 5")
		elif ch == 4 :
			print("Enter the usr name")
			usrname = input()
			command = "useradd "+usrname
			p=subprocess.getoutput(command)
			command = "passwd "+usrname
			os.system(command)
		elif ch == 5 :
			os.system("python36 capture.py")
		elif ch == 6 :
			os.system("ifconfig")
		elif ch == 7 : 
			print("Enter the IP address you want to ping :" , end = "")
			IP = input()
			command = "ping "+IP
			print(command)
			os.system(command)
		elif ch == 9 :
			whileVar=False
		elif ch == 8 :
			print("""
	Press 1 : Check current Java version
	Press 2 : Install Java version 8 Oracle(Hotspot) using rpm
	Press 3 : Install Hadoop using rpm
	Press 4 : Enter IP address of Hosts(Master and Slave)
	Press 5 : Check ping of hosts (4 step neccessary)
	Press 6 : Auto-Setup Hadoop including master and Slave
	""")
			print("Enter your choice :" , end = "")
			choice = input()
			choice = int(choice)
			if choice == 1 :
				p=subprocess.getoutput("java -version")
			elif choice == 2:
				p=subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
				f=open("/root/.bashrc","w")
				f.write("""# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/
export PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH

""")
				f.close()
				#os.system("exec bash")
				#os.system("java -version")
				print("Installation Successful.....")
			elif choice == 3:
				p=subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
				print("Your Hadoop Version is :")
				p=subprocess.getoutput("hadoop version")
			elif choice == 4:
				print("Enter IP addresses")
				print("Master :" , end="")
				IPm1=input()
				print("Slave1 :" , end="")
				IPs1=input()
				print("Slave2 :" , end="")
				IPs2=input()
				print("Slave3 :" , end="")
				IPs3=input()
			elif choice == 5:
				print("Press IP position to ping :" , end="")
				choice = input()
				choice = int(choice)
				if choice == 1:
					command = "ping "+IPm1
				elif choice == 2:
					command = "ping " + IPs1
				elif choice == 3:
					command = "ping " + IPs2
				elif choice == 4:
					command = "ping " + IPs3
				p=subprocess.getoutput(command)
			elif choice == 6:
				#installing JAVA hotspot
				os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
				f=open("/root/.bashrc","w")
				f.write("""# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/
export PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH

""")
				f.close()
				#os.system("exec bash")
				#os.system("java -version")
				print("Installation Successful.....")
				#installing Hadoop
				p=subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
				#Enter IP address
				ipList = []
				print("Enter IP addresses")
				print("Master :" , end="")
				IPm1=input()
				pingCheck = True
				while pingCheck :
					com_mand = "ping -c 2 " + IPm1				
					p , q = subprocess.getstatusoutput(com_mand)
					if p==0:
						ipList.append(IPm1)
						command = ['ssh',IPm1+' hostnamectl set-hostname master.ak.com',]
						p= subprocess.Popen(command)
						
						pingCheck = False
					else:
						print("Could not connect with Host. Try again!")
						print("Master :" , end="")
						IPm1=input()
				print("Slave1 :" , end="")
				IPs1=input()
				pingCheck = True
				while pingCheck :				
					com_mand = "ping -c 2 " + IPs1
					p , q = subprocess.getstatusoutput(com_mand)
					if p==0:
						ipList.append(IPs1)
						command = ['ssh',IPs1+' hostnamectl set-hostname slave1.ak.com',]
						p= subprocess.Popen(command)
						p.wait()
						pingCheck = False
					else:
						print("Could not connect with Host. Try again!")
						print("Slave1 :" , end="")
						IPs1=input()
				print("Slave2 :" , end="")
				pingCheck = True
				IPs2=input()
				while pingCheck :				
					com_mand = "ping -c 2 " + IPs2
					p , q = subprocess.getstatusoutput(com_mand)
					if p==0:
						ipList.append(IPs2)
						command = ['ssh',IPs2+' hostnamectl set-hostname slave2.ak.com',]
						p= subprocess.Popen(command)
						p.wait()
						pingCheck = False
					else:
						print("Could not connect with Host. Try again!")
						print("Slave2 :" , end="")
						IPs2=input()
				print("Slave3 :" , end="")
				IPs3=input()
				pingCheck = True
				while pingCheck :				
					com_mand = "ping -c 2 " + IPs3
					p , q = subprocess.getstatusoutput(com_mand)
					if p==0:
						ipList.append(IPs3)
						command = ['ssh',IPs3+' hostnamectl set-hostname slave3.ak.com',]
						p= subprocess.Popen(command)
						p.wait()
						pingCheck = False
					else:
						print("Could not connect with Host. Try again!")
						print("Slave3 :" , end="")
						IPs3=input()

				#print(ipList)
			
			
				for z in ipList:
					setupIP=z
				
					command = ['ssh',setupIP+'rpm -ivh /root/jdk-8u171-linux-x64.rpm']
					p= subprocess.Popen(command)
					p.wait()
	


					command = ['scp', '/root/.bashrc' , setupIP+':/root/.bashrc']
					p= subprocess.Popen(command)
					p.wait()
	
					command = ['ssh' ,setupIP + 'rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force' ]
					p= subprocess.Popen(command)
					p.wait()
	
					#command = "ssh " + setupIP + "ls"			
					#os.system(command)
			
			
					coreSite="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://"""+IPm1+""":9001</value>
</property>

</configuration>"""





					if setupIP != IPm1:
		
						hdfsSite="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<name>dfs.data.dir</name>
<value>/data</value>
</configuration>"""

						command = ['ssh' ,setupIP + 'mkdir /data' ]
						p= subprocess.Popen(command)
						p.wait()



					else :
						hdfsSite="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<name>dfs.name.dir</name>
<value>/master</value>
</configuration>"""
						command = ['ssh' ,setupIP + 'mkdir /master' ]
						p= subprocess.Popen(command)
						p.wait()

			
					f=open("core-site.xml","w")
					f.write(coreSite)
					f.close()
					f=open("hdfs-site.xml","w")
					f.write(hdfsSite)
					f.close()		
					command = ['scp', 'core-site.xml' , setupIP+':/etc/hadoop/core-site.xml']
					p= subprocess.Popen(command)
					p.wait()

			
					command = ['scp', 'hdfs-site.xml' , setupIP+':/etc/hadoop/hdfs-site.xml']
					p= subprocess.Popen(command)
					p.wait()

					hosts="""127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

"""+IPm1+""" master.ak.com
"""+IPs1+""" slave1.ak.com
"""+IPs2+""" slave2.ak.com
"""+IPs3+""" slave3.ak.com
"""
					f=open("hosts","w")
					f.write(hosts)
					f.close()
				
					command = ['scp', 'hosts' , setupIP+':/etc/']
					p= subprocess.Popen(command)
					p.wait()

					command = ['ssh', setupIP+' iptables -F']
					p= subprocess.Popen(command)
					p.wait()
				
					if setupIP != IPm1:
						command = ['ssh', setupIP+' hadoop-daemon.sh start datanode']
						p= subprocess.Popen(command)
						p.wait()
					

				command = ['ssh', IPm1+' hadoop-daemon.sh start namenode']
				p= subprocess.Popen(command)
				p.wait()
				print("##################__Hadoop setup sucessfully__####################")
			
			else :
				print("Invalid option")	
		else :
			print("Invalid option")
else:
	print("Invalid Password !")
