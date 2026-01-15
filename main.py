#socket Bilgisayarların ağ üzerinden konuşmasını sağlar.
#socket Ağ kapılarını yoklamak için gereken araç
import socket


def scan_port(target_ip,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP socket oluşturur
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip,port))#Bir porta bağlanmayı dener ve sonuç kodu döndürür
        sock.close()

        if result == 0:
            return True
        
        else:
            return False
        
    except socket.error:
        return False    
    

def port_scanner():
    print('\n Red Team - Port Scanner\n')

    target_ip =  input('Hedef Ip (192.168.0.87)')   
    
    start_port = int(input('baslangic port: '))

    end_port = int(input('bitis port: '))

    print(f'\n {target_ip} taraniyor...\n')

    open_ports = []

    for port in range(start_port,end_port+1):
        if scan_port(target_ip,port):
            print(f'\n Port {port} Acik')
            open_ports.append(port)

    
    if open_ports: #if len(open_ports) > 0:

        print(f'\n Acik portlar', open_ports)

    else:
        print('\n Acik port bulunamadi.')


if __name__ == '__main__':
    port_scanner()