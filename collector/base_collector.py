from abc import ABC, abstractmethod


class BaseCollector(ABC):
    def __init__(self, net_connect):
        self.net_connect = net_connect
        self.hostname = "Unknown"
        self.serial = "Unknown"
        self.location = "Unknown"
        self.vendor = self.__class__.__name__.replace('Collector', '')

    @classmethod
    @abstractmethod
    def detect(cls, output):
        """Determine if this collector should handle the device"""
        pass

    @abstractmethod
    def get_commands(self):
        """Return list of vendor-specific commands"""
        pass

    @abstractmethod
    def parse_output(self, output):
        """Parse raw output into structured data"""
        pass

    def collect(self):
        """Standard collection workflow"""
        commands = self.get_commands()
        combined_output = ""

        for cmd in commands:
            combined_output += f"Command: {cmd}\n"
            output = self.net_connect.send_command(cmd)
            combined_output += output + "\n\n"

        self.parse_output(combined_output)
        return {
            'hostname': self.hostname,
            'serial': self.serial,
            'location': self.location,
            'vendor': self.vendor
        }