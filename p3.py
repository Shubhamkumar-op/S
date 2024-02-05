import time

def leaky_bucket():
    bucket_size = int(input("Enter bucket size: "))
    outgoing_rate = int(input("Enter outgoing rate: "))
    n = int(input("Enter the number of inputs: "))
    store = 0

    while n != 0:
        incoming = int(input("Incoming size is: "))
        print("Bucket buffer size is {} out of {}".format(store, bucket_size))

        if incoming <= (bucket_size - store):
            store += incoming
            print("Bucket buffer size is {} out of {}".format(store, bucket_size))
        else:
            print("Packet loss: {}".format(incoming - (bucket_size - store)))
            store = bucket_size
            print("Bucket buffer size is {} out of {}".format(store, bucket_size))

        store -= outgoing_rate
        if store < 0:
            store = 0

        print("After outgoing: {} packets left out of {} in buffer".format(store, bucket_size))
        n -= 1
        time.sleep(3)

if _name_ == "_main_":
    leaky_bucket()
