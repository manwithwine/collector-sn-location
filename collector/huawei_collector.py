from .base_collector import BaseCollector
import re


class HuaweiCollector(BaseCollector):
    @classmethod
    def detect(cls, output):
        return 'Huawei' in output or 'huawei' in output.lower()

    def get_commands(self):
        return [
            "display sysname",
            "display device esn",
            "display device manufacture-info",
            "display cur | i location"
        ]

    def parse_output(self, output):
        # Hostname extraction
        hostname_match = re.search(r'Command: display sysname\s+([^\n]+)', output)
        if hostname_match:
            self.hostname = hostname_match.group(1).strip()

        # Serial extraction (try ESN first, then manufacture-info)
        esn_match = re.search(r'ESN of slot \d+:\s+(\S+)', output)
        if esn_match:
            self.serial = esn_match.group(1)
        else:
            # Fall back to manufacture-info
            serial_match = re.search(r'\d+\s+--\s+\S+\s+(\S+)', output)
            if serial_match:
                self.serial = serial_match.group(1)

        # Location extraction
        location_match = re.search(r'snmp-agent sys-info location\s+(.+)', output)
        if location_match:
            self.location = location_match.group(1).strip()