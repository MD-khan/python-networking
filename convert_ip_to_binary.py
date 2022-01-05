#!/usr/bin/env python3

def convert_ip_to_binary( ip_address ):
    ip = ip_address.replace(".", " ").split()
    ip_binary = []
    for ip_segment in ip:
        int_ip = int(ip_segment)
        binary = decimal_to_binary(int_ip)
        #ip_binary.append(binary)
        # Format Remove comma and []
        separator =  ""
        format_b = separator.join(map(str, binary))
        ip_binary.append(format_b)
   # Formt, ipv4 
    separator =  "."
    format_a = separator.join(map(str, ip_binary))
    return format_a


def decimal_to_binary( number ):
    decimal_values = [128, 64, 32, 16, 8, 4, 2, 1]
    binary_digits = []
    #input_d=214
    for decimal in decimal_values:
        if decimal <= number:
            binary_digits.append(1)
            number = number - decimal
        else:
            binary_digits.append(0)
    return binary_digits

print(convert_ip_to_binary("219.103.21.59"))
#convert_ip_to_binary("219.103.21.59")
