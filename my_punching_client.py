import socket
import time
import json
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sock.bind(('0.0.0.0', 18881))


recv_msg=""

def recv_func(_sock):
    global recv_msg
    while True:
        data, server = _sock.recvfrom(4096)
        print(data.decode("utf-8"), server)
        recv_msg=data.decode("utf-8")
        

identifier="client1"

data = {"COMMAND": "register", "key": "zhb1", "identifier": identifier}
msg = json.dumps(data).encode()
sent = sock.sendto(msg, ('175.178.109.217', 8478))
time.sleep(1)

t = threading.Thread(target=recv_func, args=(sock,))
t.start()


# 如果收到了对方的ip和端口，就开始下一步动作
while True:
    data = {"COMMAND": "get_peer", "key": "zhb1"}
    msg = json.dumps(data).encode()
    sent = sock.sendto(msg, ('175.178.109.217', 8478))
    time.sleep(1)

    peers=json.loads(recv_msg)

    if len(peers)>=2:
        break

print(peers)

for peer in peers:
    if peer["identifier"]==identifier:
        self_peer=peer
    if peer["identifier"]!=identifier:
        other_peer=peer

self_ip=self_peer["ip"]
self_port=self_peer["port"]

other_ip=other_peer["ip"]
other_port=other_peer["port"]

print(other_ip)
print(other_port)


# sent = sock.sendto(b"0", (other_ip, other_port))
time.sleep(15)

while True:
    msg="hello!"
    sent = sock.sendto(msg.encode(), (other_ip, other_port))
    time.sleep(1)
    print("send success!")




    
