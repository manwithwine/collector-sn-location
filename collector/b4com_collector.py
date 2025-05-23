from .base_collector import BaseCollector
import re


class B4COMCollector(BaseCollector):
    @classmethod
    def detect(cls, output):
        return 'BCOM' in output or 'bcom' in output.lower()

    def get_commands(self):
        return [
            "show hostname",
            "show system-information board-info",
            "show run | i location"
        ]

    def parse_output(self, output):
        # Hostname extraction
        hostname_match = re.search(r'Command: show hostname\s+([^\n]+)', output)
        if hostname_match:
            self.hostname = hostname_match.group(1).strip()

        # Serial extraction
        serial_match = re.search(r'Serial Number\s+: (\S+)', output)
        if serial_match:
            self.serial = serial_match.group(1)

        # Location extraction (handles vrf management case)
        location_match = re.search(r'snmp-server location\s+(?:vrf management\s+)?(.+)', output)
        if location_match:
            self.location = location_match.group(1).strip()