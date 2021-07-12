def defang_ip (ip_address):
    split_ip = ip_address.split(".")
    sep = "[.]"
    output = sep.join(split_ip)
    return output


def refang_ip (ip_address):
    split_ip = ip_address.split("[.]")
    sep = "."
    output = sep.join(split_ip)
    return output


"""Detect defang or refang need and return converted ip address"""
def defang_refang_ip (ip_address):
    input_sep = "."
    output_sep = "[.]"
    if "[.]" in ip_address:
        input_sep = "[.]"
        output_sep = "."
    split_ip = ip_address.split(input_sep)
    output = output_sep.join(split_ip)
    return output


original_ip = "1.2.3.4.5"
output_ip = defang_refang_ip(original_ip)
print(output_ip)

original_ip = "1[.]2[.]3[.]4[.]5"
output_ip = defang_refang_ip(original_ip)
print(output_ip)

