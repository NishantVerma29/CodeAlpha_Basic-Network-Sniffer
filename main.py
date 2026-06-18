packets = [
    {
        "src": "192.168.1.10",
        "dst": "142.250.193.78",
        "protocol": "TCP"
    },
    {
        "src": "192.168.1.10",
        "dst": "8.8.8.8",
        "protocol": "UDP"
    }
]

print("Basic Network Sniffer Simulation")
print("-" * 40)

for packet in packets:
    print("Source IP:", packet["src"])
    print("Destination IP:", packet["dst"])
    print("Protocol:", packet["protocol"])
    print("-" * 40)