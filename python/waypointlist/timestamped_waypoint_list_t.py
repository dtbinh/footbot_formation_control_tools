"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import waypointlist.timestamped_waypoint_t

class timestamped_waypoint_list_t(object):
    __slots__ = ["timestamp", "robotid", "n", "waypoints"]

    def __init__(self):
        self.timestamp = 0
        self.robotid = 0
        self.n = 0
        self.waypoints = []

    def encode(self):
        buf = BytesIO()
        buf.write(timestamped_waypoint_list_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qBi", self.timestamp, self.robotid, self.n))
        for i0 in range(self.n):
            assert self.waypoints[i0]._get_packed_fingerprint() == waypointlist.timestamped_waypoint_t._get_packed_fingerprint()
            self.waypoints[i0]._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != timestamped_waypoint_list_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return timestamped_waypoint_list_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = timestamped_waypoint_list_t()
        self.timestamp, self.robotid, self.n = struct.unpack(">qBi", buf.read(13))
        self.waypoints = []
        for i0 in range(self.n):
            self.waypoints.append(waypointlist.timestamped_waypoint_t._decode_one(buf))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if timestamped_waypoint_list_t in parents: return 0
        newparents = parents + [timestamped_waypoint_list_t]
        tmphash = (0xa669e1d1b74d4951+ waypointlist.timestamped_waypoint_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if timestamped_waypoint_list_t._packed_fingerprint is None:
            timestamped_waypoint_list_t._packed_fingerprint = struct.pack(">Q", timestamped_waypoint_list_t._get_hash_recursive([]))
        return timestamped_waypoint_list_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
