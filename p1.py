def divide(div, divisor, rem):
    cur = 0
    while True:
        for i in range(len(divisor)):
            rem[cur + i] ^= divisor[i]
        while rem[cur] == 0 and cur != len(rem) - 1:
            cur += 1
        if len(rem) - cur < len(divisor):
            break
    return rem

data_bits = int(input("Enter number of data bits: "))
data = [int(input(f"Enter data bit ({i + 1}): ")) for i in range(data_bits)]

divisor_bits = int(input("Enter number of bits in divisor: "))
divisor = [int(input(f"Enter divisor bit ({i + 1}): ")) for i in range(divisor_bits)]

tot_length = data_bits + divisor_bits - 1

div = data + [0] * (divisor_bits - 1)
rem = div.copy()
crc = [0] * len(div)

print("Dividend (after appending 0's):", div)

rem = divide(div, divisor, rem)

crc = [div[i] ^ rem[i] for i in range(len(div))]
print("CRC code:")
print(" ".join(map(str, crc)))

crc_input = [int(input(f"Enter CRC bit {i + 1} of {tot_length} bits: ")) for i in range(tot_length)]

for j in range(len(crc)):
    rem[j] = crc[j]

rem = divide(crc, divisor, rem)

error_detected = any(rem[i] != 0 for i in range(len(rem)))

if error_detected:
    print("Error detected.")
else:
    print("No error detected.")
