from netmiko import ConnectHandler

def configure_device(host, port, config_file):
    print(f"\n=== Kapcsolódás: {host}:{port} ===")

    device = {
        "device_type": "cisco_ios_telnet",
        "host": host,
        "port": port,
    }

    # Kapcsolódás
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    # Parancsok beolvasása
    with open(config_file, "r") as f:
        commands = f.read().splitlines()

    print(f"=== {config_file} küldése az eszköznek ===")
    output = net_connect.send_config_set(commands)
    print(output)

    net_connect.disconnect()
    print(f"=== {host}:{port} kész ===\n")



# MAIN_R1 konfigurálása
configure_device(
    host="192.168.0.124",
    port=5000,
    config_file="MAIN_R1.txt"
)

# MAIN_R2 konfigurálása
configure_device(
    host="192.168.0.124",
    port=5001,
    config_file="MAIN_R2.txt"
)


# UpWards_SW konfigurálása
configure_device(
    host="192.168.0.124",
    port=5002,
    config_file="UpWards_SW.txt"
)