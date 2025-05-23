from .base_collector import BaseCollector
import re


class CiscoCollector(BaseCollector):
    @classmethod
    def detect(cls, output):
        return 'Cisco' in output or 'cisco' in output.lower()

    def get_commands(self):
        return [
            "show hostname",
            "show version | i Board",
            "show run | i location"
        ]

    def parse_output(self, output):
        # Hostname extraction
        hostname_match = re.search(r'Command: show hostname\s+([^\n]+)', output)
        if hostname_match:
            self.hostname = hostname_match.group(1).strip()

        # Serial extraction
        serial_match = re.search(r'Processor Board ID\s+(\S+)', output)
        if serial_match:
            self.serial = serial_match.group(1)

        # Location extraction
        location_match = re.search(r'snmp-server location\s+(.+)', output)
        if location_match:
            self.location = location_match.group(1).strip()