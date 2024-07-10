# ZeroMQ Publisher-Subscriber with PyQt5 GUI

## Overview
This project demonstrates a communication system using ZeroMQ for message passing between a publisher and subscriber, integrated into a PyQt5 graphical user interface (GUI). ZeroMQ facilitates efficient and flexible messaging patterns, while PyQt5 provides a robust framework for building interactive applications.

## Components
### Publisher (`publisher.py`)
- Establishes a ZeroMQ PUB socket.
- Sends periodic messages (e.g., "Hello from the publisher").
- Runs continuously in a loop.

### Subscriber (`subscriber.py`)
- Utilizes a PyQt5 QWidget for the GUI.
- Implements a QThread-based SubscriberThread for non-blocking message reception.
- Connects to the publisher via ZeroMQ SUB socket.
- Displays incoming messages in real-time within a QTextEdit widget.
- Includes a Clear button to reset the display.

## Dependencies
- Python 3.x
- PyZMQ (Python bindings for ZeroMQ)
- PyQt5 (for GUI components)

## Usage
1. **Setup Environment:**
   - Install Python 3.x, `pyzmq`, and `pyqt5` dependencies.

2. **Run Publisher:**
   - Execute `publisher.py` to start publishing messages.

3. **Run Subscriber GUI:**
   - Execute `subscriber.py` to launch the PyQt5 subscriber application.
   - Messages published by the publisher will appear in the GUI in real-time.
   - Use the Clear button to reset the message display.

4. **Customization:**
   - Modify the messages sent by the publisher.
   - Customize the PyQt5 GUI layout and functionality as per requirements.

## Example Scenario
- The publisher sends periodic messages, which are received and displayed in the PyQt5 GUI subscriber application.
- Demonstrates real-time communication and GUI integration using ZeroMQ and PyQt5.
