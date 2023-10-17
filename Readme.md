

### Python Server for Sensor Data (IoTech Server)
- **Purpose:** This Python server script is designed to receive sensor data from devices, specifically temperature and humidity values. It also monitors critical temperature thresholds and sends email alerts if those thresholds are exceeded. The script interacts with a MySQL database to store the collected data.
- **Functionality:**
  - Listens for incoming sensor data from IoT devices on a specified host and port.
  - Utilizes SSL for secure communication between devices and the server.
  - Connects to a MySQL database to store temperature and humidity data, associating the data with a specific device.
  - Monitors temperature values and triggers email alerts when the temperature exceeds a critical threshold.
  - The email alert includes detailed information about the temperature spike and a link to a monitoring platform.
- **Usage:** The script is intended for use as a central server in a smart home or IoT environment. It provides real-time monitoring and data storage capabilities, ensuring that temperature and humidity values are recorded and alerts are sent in the case of critical temperature levels.

### Python Sensor Data Sender (IoTech Sensor)
- **Purpose:** This Python script is designed to read temperature and humidity data from a DHT22 sensor and transmit it to a remote server over a secure connection. It's a sensor node that continuously measures environmental data and forwards it to the server.
- **Functionality:**
  - Reads temperature and humidity values from a DHT22 sensor.
  - Establishes a secure connection to a remote server via SSL/TLS.
  - Periodically transmits the sensor data to the server in the format of "temperature,humidity."
- **Usage:** The script is intended to be deployed on IoT devices equipped with DHT22 sensors, serving as sensor nodes in a smart home or IoT ecosystem. It securely sends environmental data to a central server for monitoring and analysis.

These scripts contribute to the open-source community and can be used as building blocks for IoT and smart home projects. They enable data collection, real-time monitoring, and alerting for temperature and humidity values, making them valuable tools for IoT and smart home applications.