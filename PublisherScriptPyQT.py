import zmq
import time

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")

    while True:
        message = "Hello from the publisher"
        print(f"Publishing message: {message}")
        socket.send_string(message)
        time.sleep(1)

if __name__ == "__main__":
    main()
