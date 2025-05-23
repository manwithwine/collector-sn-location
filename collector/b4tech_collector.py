from .base_collector import BaseCollector
import re


class B4TECHCollector(BaseCollector):
    @classmethod
    def detect(cls, output):
        return 'B4TECH' in output

    def get_commands(self):
        return [
            "show run | inc hostname",
            "show version",
            "show run | i location"
        ]

    def parse_output(self, output):
        # Hostname extraction
        for line in output.split('\n'):
            if 'hostname' in line.lower() and not line.strip().startswith('Command'):
                self.hostname = line.split()[-1]
                break

        # Serial extraction
        serial_match = re.search(r'System serial number is (\S+)', output)
        if serial_match:
            self.serial = serial_match.group(1)

        # Location extraction
        location_match = re.search(r'snmp-server system-location\s+(.+)', output)
        if location_match:
            self.location = location_match.group(1).strip()