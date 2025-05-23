from .b4tech_collector import B4TECHCollector
from .b4com_collector import B4COMCollector
from .cisco_collector import CiscoCollector
from .huawei_collector import HuaweiCollector


class CollectorFactory:
    COLLECTORS = [B4TECHCollector, B4COMCollector, CiscoCollector, HuaweiCollector]

    @staticmethod
    def create_collector(net_connect):
        """Auto-detect device type with vendor-specific fallbacks"""
        # Try standard show version first
        try:
            version_output = net_connect.send_command("show version", delay_factor=2)
            for collector_class in CollectorFactory.COLLECTORS:
                if collector_class.detect(version_output):
                    return collector_class(net_connect)
        except:
            pass

        # Huawei-specific fallback
        try:
            version_output = net_connect.send_command("display version", delay_factor=2)
            if 'Huawei' in version_output:
                return HuaweiCollector(net_connect)
        except:
            pass

        print("Could not determine device type with either show/display version")
        return None