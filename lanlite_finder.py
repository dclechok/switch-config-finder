import paramiko
import time

host = "10.7.1.200" #eventually create a list of all rack switches, and will create groups as we expand
username = "admin"
password = "Lun@R4ck65$!"

print('hello')

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
print(client.get_transport().is_active())

shell = client.invoke_shell()

out = shell.recv(9999)
print(out.decode("ascii"))
shell.sendall("en\r")
shell.sendall(password + "\r")
time.sleep(3)

out = shell.recv(9999)
print(out.decode("ascii"))

shell.sendall("show version\r")
time.sleep(3)

out = shell.recv(99999)

shell.sendall("\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r")

time.sleep(3)

out = shell.recv(99999)
print(str(out.decode("ascii")))
if str(out).find("lanlite"):
    print(host + ' is Lanlite!')
# channel.sendall_stderr(username)
# out = channel.recv(9999)
# print(out)

shell.close()

# input("Press enter to exit ;)")