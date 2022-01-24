class Data:
    timestamp = None
    satellite = None
    phase_tec = None
    p_range_tec = None

    def __init__(self, timestamp, satellite, phase_tec, p_range_tec):
        self.timestamp = timestamp
        self.satellite = satellite
        self.phase_tec = phase_tec
        self.p_range_tec = p_range_tec

    def to_str(self):
        return '{} {}: {} {}'.format(
            self.timestamp,
            self.satellite,
            self.phase_tec,
            self.p_range_tec,
        )