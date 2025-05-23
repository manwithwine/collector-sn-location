# Network Device Inventory Collector

A Python script to collect device information (hostname, serial number, location) from network devices.

## Features

- Supports multiple vendors: B4TECH (B4COM 21XX), B4COM (B4COM 41XX), Cisco (Nexus 9000 series), Huawei (CE16808, CE6885, CE6820)
- Stores raw output and structured Excel report
- Secure credential handling via environment variables
- Easy to extend for new device types

## Installation

1. Clone the repository:
2. Install dependencies:
   pip install -r requirements.txt
3. Set username and password in .env
4. Set IP addresses in IP

## Adding New Device Types

1. Create new collector file (collector/newvendor_collector.py)
2. Update CollectorFactory (collector/collector_factory.py)
3. Update device detection (main.py)
